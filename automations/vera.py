#!/usr/bin/env python3
"""VERA — Agente editoriale settimanale per Alberto Lattuada.

Scheduled via launchd venerdì 12:00.
1. Legge dal workspace gli articoli e i draft della settimana (Jamma, Bottadiculo, Sitiscommesse)
2. Legge il piano editoriale LinkedIn vivo (04-linkedin/piano-editoriale-2026.md)
3. Chiama claude CLI per comporre il brief editoriale con connessioni articolo -> LinkedIn
4. Salva il brief in 03-giornalismo/brief-editoriale/ e invia DM Slack ad Alberto

Nessun accesso a siti esterni: la fonte è il workspace, non gli RSS.
"""

import datetime
import subprocess
import sys
import time
from pathlib import Path

WORKSPACE  = Path("/Users/albertol./workspace")
GIORNALISMO = WORKSPACE / "03-giornalismo"
PIANO_LINKEDIN = WORKSPACE / "04-linkedin/piano-editoriale-2026.md"
PUBBLICATI = GIORNALISMO / "articoli-pubblicati.md"
OUTPUT_DIR = GIORNALISMO / "brief-editoriale"
CLAUDE_BIN = "/Users/albertol./.local/bin/claude"
SLACK_USER = "U09TCJ89NJJ"
DAYS_BACK  = 7

DRAFT_DIRS = [
    ("Jamma", GIORNALISMO / "jamma/drafts"),
    ("Bottadiculo", GIORNALISMO / "bottadiculo/drafts"),
    ("Sitiscommesse", GIORNALISMO / "sitiscommesse"),
    ("LinkedIn", WORKSPACE / "04-linkedin"),
]


def log(msg: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] VERA: {msg}", flush=True)


def notify_failure(reason: str):
    subprocess.run([
        "osascript", "-e",
        f'display notification "{reason}" with title "VERA — run fallito" sound name "Basso"'
    ])


def run_claude(args: list, timeout: int, retries: int = 1, delay: int = 5):
    """Chiama claude CLI con timeout stretto e un retry. Ritorna il CompletedProcess (anche se fallito)."""
    last = None
    for attempt in range(retries + 1):
        try:
            last = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
            if last.returncode == 0:
                return last
        except subprocess.TimeoutExpired:
            log(f"Timeout ({timeout}s) al tentativo {attempt + 1}/{retries + 1}")
            last = None
        if attempt < retries:
            time.sleep(delay)
    return last


def first_heading(path: Path) -> str:
    try:
        for line in path.read_text(errors="ignore").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return path.stem


def recent_files() -> str:
    cutoff = datetime.datetime.now() - datetime.timedelta(days=DAYS_BACK)
    rows = []
    for testata, folder in DRAFT_DIRS:
        if not folder.is_dir():
            continue
        for f in sorted(folder.glob("*.md")):
            mtime = datetime.datetime.fromtimestamp(f.stat().st_mtime)
            if mtime >= cutoff and f.name not in ("CLAUDE.md", "README.md"):
                rows.append(f"- {testata} | {f.name} | modificato {mtime.strftime('%d/%m')} | titolo: {first_heading(f)}")
    return "\n".join(rows) if rows else "Nessun file modificato negli ultimi 7 giorni."


def piano_calendario() -> str:
    text = PIANO_LINKEDIN.read_text(errors="ignore")
    cut = text.find("## Legenda")
    return text[:cut] if cut > 0 else text[:4000]


def next_week_dates() -> str:
    today = datetime.date.today()
    monday = today + datetime.timedelta(days=(7 - today.weekday()))
    days = ["Lun", "Mar", "Mer", "Gio", "Ven"]
    return ", ".join(
        f"{days[i]} {(monday + datetime.timedelta(days=i)).strftime('%d/%m')}"
        for i in range(5)
    )


def build_prompt(today_str: str) -> str:
    return f"""Sei VERA, l'agente editoriale di Alberto Lattuada (giornalista iGaming per Jamma.it, Bottadiculo.it, Sitiscommesse.com e BDM Softswiss).

Oggi è venerdì {today_str}. La settimana prossima è: {next_week_dates()}.

Componi il brief editoriale settimanale usando SOLO i dati del workspace riportati sotto. Non inventare articoli o date.

## DATI 1 — Indice articoli pubblicati (articoli-pubblicati.md)

{PUBBLICATI.read_text(errors="ignore")}

## DATI 2 — File modificati negli ultimi 7 giorni nel workspace

{recent_files()}

## DATI 3 — Piano editoriale LinkedIn (fonte viva, usa queste date, non altre)

{piano_calendario()}

## COMPITO

Componi il brief in formato Slack (asterischi singoli per il grassetto, nessun heading markdown #):

*VERA | Brief Editoriale — {today_str}*

*Scritto o pubblicato questa settimana*
Lista: Testata | Titolo | data. Distingui ciò che risulta pubblicato da ciò che è solo draft (usa l'indice DATI 1 e i file DATI 2). Se un draft recente non compare nell'indice pubblicati, segnalalo come "draft, stato da confermare".

*LinkedIn settimana prossima*
Solo gli slot del piano (DATI 3) che cadono nelle date della settimana prossima indicate sopra. Formato: GG/MM Formato | Topic | Fonte: titolo articolo/draft della settimana se pertinente, altrimenti "Da creare".

*Connessioni articolo -> LinkedIn*
Per ogni articolo o draft della settimana: se il topic alimenta uno slot LinkedIn delle prossime 2 settimane, indica la connessione. Se nessuna: "Nessuna sovrapposizione diretta questa settimana."

*Azione entro domenica*
Massimo 2 punti concreti per preparare i post di settimana prossima. Se l'indice articoli-pubblicati.md risulta incompleto rispetto ai draft recenti, uno dei punti deve essere aggiornarlo.

REGOLE: niente trattini lunghi nel testo, niente avverbi in -mente, tono asciutto da insider. Rispondi SOLO con il testo del brief, nulla prima o dopo."""


def main():
    today = datetime.date.today()
    today_str = today.strftime("%d/%m")
    output_path = OUTPUT_DIR / f"{today.strftime('%Y-%m-%d')}-vera.md"

    if output_path.exists():
        log(f"Brief già generato oggi ({output_path.name}), esco.")
        return

    prompt = build_prompt(today_str)
    log("Chiamo claude CLI per comporre il brief...")

    result = run_claude(
        [CLAUDE_BIN, "-p", prompt, "--dangerously-skip-permissions"],
        timeout=180, retries=1
    )
    if result is None or result.returncode != 0 or not result.stdout.strip():
        err = result.stderr[:300] if result is not None else "timeout dopo retry"
        log(f"Claude error: {err}")
        notify_failure("Brief non generato, vedi log/vera.error.log")
        sys.exit(1)

    brief = result.stdout.strip()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(brief + "\n")
    log(f"Brief salvato: {output_path}")

    slack_prompt = f"Usa slack_send_message per inviare questo DM a {SLACK_USER}. Invia il testo così com'è, senza modifiche:\n\n{brief}"
    slack_result = run_claude(
        [CLAUDE_BIN, "-p", slack_prompt, "--dangerously-skip-permissions"],
        timeout=60, retries=1
    )
    if slack_result is None or slack_result.returncode != 0:
        err = slack_result.stderr[:200] if slack_result is not None else "timeout dopo retry"
        log(f"Slack error: {err}")
        notify_failure(f"Brief salvato ma DM Slack non inviato: {output_path.name}")
        sys.exit(1)
    log("DM Slack inviato")

    subprocess.run([
        "osascript", "-e",
        f'display notification "Brief editoriale pronto" with title "VERA" subtitle "{today_str}" sound name "Glass"'
    ])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"Errore non gestito: {e}")
        notify_failure(f"Errore non gestito: {e}")
        sys.exit(1)
