#!/usr/bin/env python3
"""PIERO — iGaming News Radar per Alberto Lattuada.

SCHEDULATO IN LOCALE via launchd (com.albertol.piero), ogni giorno alle 07:00 e 12:40.
La versione cloud (trig_01R5LLasoxRqBYz2w48MSRh6) resta disattivata: la sandbox
cloud non raggiunge le fonti RSS (blocco di rete del 23/07/2026). PIERO e'
l'unico agente che deve girare per forza sul Mac.

Flusso:
1. Scarica RSS feeds da fonti iGaming (solo quelle enabled in piero-sources.json)
2. Filtra storie delle ultime 48 ore per keyword di rilevanza
3. Chiama claude CLI per generare angoli editoriali per testata
4. Salva morning-brief.md in news-igaming 2026/YYYY-MM-DD/ e manda DM Slack

Hardening 08/08/2026: timeout di rete per fonte. Senza, una fonte lenta
appendeva la run per ore (AGiMeG e Agipro News, run del 02, 03, 07 e 08/08).
"""

import feedparser
import json
import socket
import subprocess
import datetime
import sys
import time
from pathlib import Path

# Timeout di rete globale: feedparser usa urllib, che senza questo attende
# all'infinito. E' la causa delle run appese osservate fino all'08/08/2026.
FETCH_TIMEOUT = 20
socket.setdefaulttimeout(FETCH_TIMEOUT)

USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")

WORKSPACE   = Path("/Users/albertol./workspace")
NEWS_DIR    = WORKSPACE / "03-giornalismo/news-igaming 2026"
SOURCES_FILE = Path(__file__).parent / "piero-sources.json"
CLAUDE_BIN  = "/Users/albertol./.local/bin/claude"
HOURS_BACK  = 48
MAX_STORIES = 30

KEYWORDS = [
    "italy", "italia", "italian", "adm",
    "belgium", "belgio", "czech", "repubblica ceca",
    "germany", "germania", "ireland", "irlanda",
    "igaming", "i-gaming", "gambling", "casino", "betting", "sportsbook",
    "aggregator", "provider", "platform", "supplier", "b2b",
    "licence", "license", "regulation", "compliance", "mga", "ukgc",
    "acquisition", "merger", "acquires", "deal", "funding", "investment",
    "european", "europe",
]


def log(msg: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] PIERO: {msg}", flush=True)


def download(url: str) -> bytes:
    """Scarica il feed con curl invece che con urllib.

    Alcune fonti (Casino Beats, verificato 08/08/2026) chiudono la connessione
    con le librerie Python ma rispondono a curl. Il --max-time e' anche la
    seconda barriera contro le run appese, oltre al socket timeout.
    """
    cmd = ["curl", "-sL", "--max-time", str(FETCH_TIMEOUT), "-A", USER_AGENT,
           "-H", "Accept: application/rss+xml,application/xml;q=0.9,*/*;q=0.8", url]
    for attempt in (1, 2):
        result = subprocess.run(cmd, capture_output=True, timeout=FETCH_TIMEOUT + 10)
        if result.returncode == 0 and result.stdout:
            return result.stdout
        if attempt == 1:
            time.sleep(2)  # Casino Beats risponde a intermittenza, un retry basta
    raise RuntimeError(f"curl exit {result.returncode} dopo 2 tentativi")


def is_relevant(entry) -> bool:
    text = f"{entry.get('title', '')} {entry.get('summary', '')}".lower()
    return any(kw in text for kw in KEYWORDS)


def fetch_stories(sources: list) -> tuple:
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=HOURS_BACK)
    stories = []
    seen = set()
    health = []

    for src in sources:
        if not src.get("enabled", True):
            continue
        started = time.monotonic()
        try:
            feed = feedparser.parse(download(src["url"]))
            elapsed = time.monotonic() - started
            n_entries = len(feed.entries)
            log(f"{src['name']}: {n_entries} entries in {elapsed:.1f}s")
            if n_entries == 0:
                log(f"WARN {src['name']}: feed vuoto o non parsabile, controllare l'URL")
                health.append({"name": src["name"], "lang": src.get("lang", "EN"),
                               "ok": False, "detail": "feed vuoto o non parsabile"})
            else:
                health.append({"name": src["name"], "lang": src.get("lang", "EN"),
                               "ok": True, "detail": f"{n_entries} entries"})
            for entry in feed.entries:
                title = entry.get("title", "").strip()
                if not title or title.lower() in seen:
                    continue
                pub = entry.get("published_parsed") or entry.get("updated_parsed")
                if pub:
                    pub_dt = datetime.datetime(*pub[:6], tzinfo=datetime.timezone.utc)
                    if pub_dt < cutoff:
                        continue
                if not is_relevant(entry):
                    continue
                seen.add(title.lower())
                stories.append({
                    "title": title,
                    "source": src["name"],
                    "url": entry.get("link", ""),
                    "published": entry.get("published", "")[:16] if entry.get("published") else "",
                    "summary": entry.get("summary", "")[:600].strip(),
                })
        except Exception as e:
            elapsed = time.monotonic() - started
            log(f"ERROR {src['name']} dopo {elapsed:.1f}s: {e}")
            health.append({"name": src["name"], "lang": src.get("lang", "EN"),
                           "ok": False, "detail": str(e)[:120]})

    # Il taglio a MAX_STORIES era secco sulla lista in ordine di fonte: iGaming
    # Business, che pubblica 100 item al giorno, saturava la quota e Jamma e
    # AGiMeG (ultime della lista) restavano fuori dal brief. Verificato l'08/08.
    # Ora si prende a giro: una storia per fonte a rotazione, cosi' ogni fonte
    # entra nel brief e le testate italiane non vengono mai schiacciate.
    by_source = {}
    for story in stories:
        by_source.setdefault(story["source"], []).append(story)

    balanced = []
    while len(balanced) < MAX_STORIES and any(by_source.values()):
        for source in list(by_source):
            if by_source[source] and len(balanced) < MAX_STORIES:
                balanced.append(by_source[source].pop(0))

    coverage = ", ".join(f"{s}:{sum(1 for b in balanced if b['source'] == s)}"
                         for s in dict.fromkeys(b["source"] for b in balanced))
    log(f"Collected {len(balanced)} relevant stories (cap {MAX_STORIES}) — {coverage}")
    return balanced, health


def italian_coverage(health: list) -> dict:
    """Stato delle fonti italiane per il run corrente.

    Serve a distinguere due cose che nel brief si somigliano e non sono affatto
    la stessa: "oggi in Italia non e' successo niente" e "oggi le fonti italiane
    non rispondevano". Senza questo controllo il brief mostra solo una fila di
    'Angle Sitiscommesse.com -> N/A', che letta di fretta sembra assenza di
    notizie invece che assenza di fonti. Stessa regola di onesta' data a OTTO.

    Caso reale che l'ha motivato: il 13/08/2026 Jamma e AGiMeG erano entrambe
    irraggiungibili dalla rete WiFi di Alberto (503 su HTTP, reset su HTTPS) e
    il brief usciva con 19 angoli Sitiscommesse su 20 a N/A, senza dirlo.
    """
    it = [h for h in health if h["lang"] == "IT"]
    down = [h for h in it if not h["ok"]]
    return {"totale": len(it), "giu": down, "tutte_giu": bool(it) and len(down) == len(it)}


def coverage_banner(cov: dict) -> str:
    """Riga di avviso da mettere in cima al brief. Stringa vuota se tutto ok."""
    if not cov["giu"]:
        return ""
    nomi = ", ".join(h["name"] for h in cov["giu"])
    if cov["tutte_giu"]:
        return (f"> ⚠️ **Nessuna fonte italiana raggiungibile** ({nomi}). "
                f"Questo brief non copre il mercato IT: gli angoli Sitiscommesse.com sono "
                f"inaffidabili e l'assenza di notizie italiane non significa che non ce ne siano. "
                f"Causa tipica: rete che filtra i domini (verificato il 13/08/2026 sulla WiFi di Alberto). "
                f"Per il mercato IT controllare le fonti a mano prima di scriverci sopra.\n")
    return (f"> ⚠️ **Copertura italiana parziale**: {nomi} non raggiungibile. "
            f"Il mercato IT in questo brief e' coperto solo in parte.\n")


def _coverage_rule(cov: dict) -> str:
    """Istruzione da passare al modello quando mancano le fonti italiane."""
    if not cov["giu"]:
        return ""
    nomi = ", ".join(h["name"] for h in cov["giu"])
    stato = "Nessuna fonte italiana" if cov["tutte_giu"] else f"Fonti italiane mancanti ({nomi})"
    return (f"- ATTENZIONE COPERTURA: {stato} ha risposto in questo run. "
            f"Non dedurre che in Italia non sia successo nulla e non inventare "
            f"angoli Sitiscommesse.com da notizie internazionali per riempire il vuoto: "
            f"se una notizia non tocca davvero il mercato italiano, l'angolo resta N/A.")


def build_prompt(stories: list, today: str, cov: dict) -> str:
    return f"""Sei PIERO, l'agente News Radar di Alberto Lattuada (giornalista iGaming e BDM Softswiss Game Aggregator).

Alberto scrive per tre testate con identità editoriali distinte:

JAMMA.IT — B2B strategico
- Audience: top management (operatori, fornitori, regolatori, avvocati iGaming)
- Angolo: la domanda sotto la domanda — cosa significa questa notizia per il mercato B2B e i mercati regolamentati EU?
- Tono: analitico, autorevole, nessuna prima persona
- Priorità: M&A, regulation EU/IT, provider B2B, mercati DE/BE/CZ/IE/IT

BOTTADICULO.IT — Operativo, senza filtri
- Audience: affiliati, compliance officer, operativi mid-level
- Angolo: stesso fatto visto dal lato del campo — cosa cambia concretamente per chi lavora nel settore?
- Tono: diretto, senza filtri, non lato C-level

SITISCOMMESSE.COM — B2C italiano
- Audience: scommettitori e giocatori italiani
- Angolo: impatto diretto sul giocatore italiano (ADM, operatori con licenza IT, quote, bonus, normativa)
- Tono: neutro, solo fatti, zero opinioni
- CRITICO: N/A se la notizia non riguarda direttamente il mercato o il giocatore italiano

FORMATO OUTPUT (rispettare esattamente):

# iGaming Morning Brief — {today}

---

## M&A & Business Moves

### Titolo della notizia
**Source:** Nome Fonte — Data

Sintesi della notizia in 3-4 righe. Solo fatti, no aggettivi vuoti.

**Angle Jamma.it** → angolo editoriale specifico oppure N/A
**Angle Bottadiculo.it** → angolo editoriale specifico oppure N/A
**Angle Sitiscommesse.com** → angolo editoriale specifico oppure N/A

---

## Regulation & Compliance
[stesse storie con stesso schema]

## Market Expansion
[stesse storie con stesso schema]

## Industry News
[stesse storie con stesso schema]

---

## Sources
- [Nome Fonte](url)

REGOLE:
- Raggruppa ogni storia nella sezione tematica corretta
- Includi solo storie con almeno un angolo non-N/A
- No trattini nel corpo del testo, no avverbi in -mente
- Il testo della sintesi deve essere in italiano
- Se una sezione non ha storie, omettila
{_coverage_rule(cov)}

NOTIZIE DA ELABORARE ({len(stories)} storie, ultime 48 ore):

{json.dumps(stories, ensure_ascii=False, indent=2)}

Genera il morning-brief completo ora."""


def main():
    today = datetime.date.today().strftime("%Y-%m-%d")
    output_dir = NEWS_DIR / today
    output_path = output_dir / "morning-brief.md"

    if output_path.exists():
        log(f"Brief already exists for {today}, skipping.")
        return

    sources = json.loads(SOURCES_FILE.read_text())
    stories, health = fetch_stories(sources)
    cov = italian_coverage(health)

    if cov["giu"]:
        nomi = ", ".join(h["name"] for h in cov["giu"])
        stato = "TUTTE giu'" if cov["tutte_giu"] else f"{len(cov['giu'])} su {cov['totale']} giu'"
        log(f"COPERTURA IT: {stato} — {nomi}")

    if not stories:
        log("No relevant stories found. Exiting.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = output_dir / "piero-raw.json"
    raw_path.write_text(json.dumps(stories, ensure_ascii=False, indent=2))
    log(f"Raw stories saved: {raw_path}")

    prompt = build_prompt(stories, today, cov)
    log(f"Calling claude CLI ({len(stories)} stories)...")

    # --tools "": la generazione del brief e' pura scrittura di testo, non le
    # serve nessun tool. Senza questo flag, con --dangerously-skip-permissions
    # il modello e' libero di aprire i link delle notizie per verificarle
    # invece di limitarsi a scrivere: e' quello che spiega le run da 60-100
    # minuti osservate tra il 25 e il 30/08/2026 (la chiamata Slack sotto,
    # stesso binario, stesso flag di permessi ma senza link da seguire,
    # impiega 22 secondi). Testato il 31/08/2026 con --tools "": 116s per 9
    # storie, 292s per 30 (il tetto MAX_STORIES). Timeout a 420s per margine
    # reale, contro i 600s che comunque non bastavano quando il modello si
    # metteva a navigare.
    result = subprocess.run(
        [CLAUDE_BIN, "-p", prompt, "--dangerously-skip-permissions", "--tools", ""],
        capture_output=True, text=True, timeout=420
    )

    if result.returncode != 0:
        log(f"Claude error (exit {result.returncode}): {result.stderr[:300]}")
        sys.exit(1)

    # Il banner va scritto qui e non chiesto al modello: se lo generasse lui
    # potrebbe ometterlo o ammorbidirlo, e l'avviso deve esserci sempre quando
    # la condizione e' vera. Il modello riceve comunque l'istruzione separata
    # (_coverage_rule) per non inventare angoli italiani a vuoto.
    banner = coverage_banner(cov)
    output_path.write_text(banner + ("\n" if banner else "") + result.stdout)
    log(f"Morning brief saved: {output_path}")

    subprocess.run([
        "osascript", "-e",
        f'display notification "Morning brief pronto — {len(stories)} notizie iGaming" with title "PIERO" subtitle "{today}" sound name "Glass"'
    ])

    headlines = "\n".join(f"• {s['title']}" for s in stories[:3])
    if cov["tutte_giu"]:
        alert = ("\n\n:warning: *Nessuna fonte italiana raggiungibile* "
                 f"({', '.join(h['name'] for h in cov['giu'])}). "
                 "Il brief non copre il mercato IT: verificare a mano prima di usarlo per Sitiscommesse o per il nesso Italia su Jamma.")
    elif cov["giu"]:
        alert = ("\n\n:warning: *Copertura italiana parziale*: "
                 f"{', '.join(h['name'] for h in cov['giu'])} non raggiungibile.")
    else:
        alert = ""
    slack_msg = (
        f"*PIERO | {today}* — {len(stories)} notizie iGaming\n\n"
        f"{headlines}{alert}\n\n"
        f"_Brief completo: `03-giornalismo/news-igaming 2026/{today}/morning-brief.md`_"
    )
    slack_prompt = f"Usa slack_send_message per inviare questo DM a U09TCJ89NJJ:\n\n{slack_msg}"
    slack_result = subprocess.run(
        [CLAUDE_BIN, "-p", slack_prompt, "--dangerously-skip-permissions"],
        capture_output=True, text=True, timeout=120
    )
    if slack_result.returncode != 0:
        log(f"Slack notification error: {slack_result.stderr[:200]}")
    else:
        log("Slack notification sent")


if __name__ == "__main__":
    main()
