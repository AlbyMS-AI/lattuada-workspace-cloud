#!/usr/bin/env python3
"""PIERO — iGaming News Radar per Alberto Lattuada.

NON PIU' SCHEDULATO (dal 20/07/2026): migrato a routine cloud
trig_01R5LLasoxRqBYz2w48MSRh6 (vedi automations/agents-roster.md).
File conservato come riferimento storico della logica, plist locale scaricato.

Comportamento originale, quando era schedulato via launchd alle 07:00:
1. Scarica RSS feeds da fonti iGaming
2. Filtra storie delle ultime 48 ore per keyword di rilevanza
3. Chiama claude CLI per generare angoli editoriali per testata
4. Salva morning-brief.md in news-igaming 2026/YYYY-MM-DD/
"""

import feedparser
import json
import subprocess
import datetime
import sys
from pathlib import Path

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


def is_relevant(entry) -> bool:
    text = f"{entry.get('title', '')} {entry.get('summary', '')}".lower()
    return any(kw in text for kw in KEYWORDS)


def fetch_stories(sources: list) -> list:
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=HOURS_BACK)
    stories = []
    seen = set()

    for src in sources:
        if not src.get("enabled", True):
            continue
        log(f"Fetching {src['name']}...")
        try:
            feed = feedparser.parse(src["url"])
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
            log(f"ERROR {src['name']}: {e}")

    stories = stories[:MAX_STORIES]
    log(f"Collected {len(stories)} relevant stories (capped at {MAX_STORIES})")
    return stories


def build_prompt(stories: list, today: str) -> str:
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
    stories = fetch_stories(sources)

    if not stories:
        log("No relevant stories found. Exiting.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = output_dir / "piero-raw.json"
    raw_path.write_text(json.dumps(stories, ensure_ascii=False, indent=2))
    log(f"Raw stories saved: {raw_path}")

    prompt = build_prompt(stories, today)
    log(f"Calling claude CLI ({len(stories)} stories)...")

    result = subprocess.run(
        [CLAUDE_BIN, "-p", prompt, "--dangerously-skip-permissions"],
        capture_output=True, text=True, timeout=600
    )

    if result.returncode != 0:
        log(f"Claude error (exit {result.returncode}): {result.stderr[:300]}")
        sys.exit(1)

    output_path.write_text(result.stdout)
    log(f"Morning brief saved: {output_path}")

    subprocess.run([
        "osascript", "-e",
        f'display notification "Morning brief pronto — {len(stories)} notizie iGaming" with title "PIERO" subtitle "{today}" sound name "Glass"'
    ])

    headlines = "\n".join(f"• {s['title']}" for s in stories[:3])
    slack_msg = (
        f"*PIERO | {today}* — {len(stories)} notizie iGaming\n\n"
        f"{headlines}\n\n"
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
