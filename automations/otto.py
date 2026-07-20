#!/usr/bin/env python3
"""OTTO — Check settimanale del workspace (sabato mattina).

Scheduled via launchd sabato 08:30.
Replica il "grosso check del sabato" fatto manualmente il 12/07/2026:
1. Stato agenti locali (launchd + log PIERO/VERA) e ultimi DM di MARCO/ALDO su Slack
2. Stato task list (LinkedIn, LasVegas) e tracker articoli-pubblicati.md
3. File modificati negli ultimi 7 giorni per dominio
4. Igiene struttura (cartelle "copia", temp/, draft senza stato di pubblicazione)
Compone il report con claude CLI, lo salva in automations/check-sabato/ e manda DM Slack.
"""

import datetime
import subprocess
import sys
import time
from pathlib import Path

WORKSPACE = Path("/Users/albertol./workspace")
OUTPUT_DIR = WORKSPACE / "automations/check-sabato"
CLAUDE_BIN = "/Users/albertol./.local/bin/claude"
SLACK_USER = "U09TCJ89NJJ"

TASK_FILES = [
    WORKSPACE / "04-linkedin/task-list.md",
    WORKSPACE / "06-lasvegas/collaborazioni/task-list.md",
]
PUBBLICATI = WORKSPACE / "03-giornalismo/articoli-pubblicati.md"
LOGS = WORKSPACE / "automations/logs"


def log(msg: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] OTTO: {msg}", flush=True)


def notify_failure(reason: str):
    subprocess.run([
        "osascript", "-e",
        f'display notification "{reason}" with title "OTTO — run fallito" sound name "Basso"'
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


def sh(cmd: str) -> str:
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        return (r.stdout or r.stderr).strip()
    except Exception as e:
        return f"(errore: {e})"


def tail(path: Path, n: int = 12) -> str:
    if not path.exists():
        return "(log assente)"
    lines = path.read_text(errors="ignore").splitlines()
    return "\n".join(lines[-n:])


def recent_files() -> str:
    cutoff = datetime.datetime.now() - datetime.timedelta(days=7)
    rows = []
    for f in WORKSPACE.rglob("*.md"):
        if any(p in f.parts for p in ("archive", "node_modules", ".git")):
            continue
        try:
            mtime = datetime.datetime.fromtimestamp(f.stat().st_mtime)
        except OSError:
            continue
        if mtime >= cutoff:
            rows.append(f"- {f.relative_to(WORKSPACE)} ({mtime.strftime('%d/%m %H:%M')})")
    return "\n".join(sorted(rows)) or "Nessun file .md modificato negli ultimi 7 giorni."


def igiene() -> str:
    copie = sh(f'find "{WORKSPACE}" -iname "*copia*" -not -path "*/archive/*" | head -10') or "nessuna"
    temp = sh(f'ls "{WORKSPACE}/temp" | head -10')
    return f"Cartelle/file 'copia' fuori da archive:\n{copie}\n\nContenuto temp/:\n{temp}"


def slack_recon() -> str:
    """Chiede a claude di verificare gli ultimi DM di MARCO, ALDO e PIERO (tutti cloud). Best effort."""
    prompt = (
        "Cerca su Slack (slack_search_public_and_private, include_bots=true) gli ultimi DM ricevuti da Alberto "
        "che iniziano con 'MARCO |', 'ALDO |' e 'PIERO |' negli ultimi 8 giorni. "
        "Rispondi SOLO con tre righe: 'MARCO: ultimo brief GG/MM' (o 'MARCO: nessun brief trovato'), idem per ALDO e per PIERO."
    )
    r = run_claude([CLAUDE_BIN, "-p", prompt,
                     "--allowedTools", "mcp__claude_ai_Slack__slack_search_public_and_private"],
                    timeout=90, retries=1)
    if r is not None and r.returncode == 0 and r.stdout.strip():
        return r.stdout.strip()
    return "MARCO/ALDO/PIERO: verifica Slack non riuscita (controllare a mano i DM)."


def build_prompt(today_str: str) -> str:
    task_dump = "\n\n".join(f"### {p}\n{p.read_text(errors='ignore')[:6000]}" for p in TASK_FILES if p.exists())
    return f"""Sei OTTO, l'agente di revisione settimanale del workspace di Alberto Lattuada (freelance iGaming: BDM Softswiss, giornalismo Jamma/Bottadiculo/Sitiscommesse, LinkedIn, LasVegas).

Oggi è sabato {today_str}. Componi il check settimanale del workspace usando SOLO i dati sotto. Non inventare nulla: se un dato manca, scrivi "da verificare".

## DATI 1 — Agenti locali (launchctl: '-' o PID = caricato; assente = NON caricato). Solo VERA e OTTO girano in locale, PIERO è passato a cloud cron dal 20/07/2026.
{sh("launchctl list | grep albertol")}

Ultime righe log VERA:
{tail(LOGS / "vera.log")}

Errori recenti VERA:
{tail(LOGS / "vera.error.log", 5)}

## DATI 2 — Agenti cloud (ultimi DM Slack: MARCO, ALDO, PIERO)
{slack_recon()}

## DATI 3 — Task list correnti
{task_dump}

## DATI 4 — Tracker articoli pubblicati (prime 60 righe)
{chr(10).join(PUBBLICATI.read_text(errors="ignore").splitlines()[:60])}

## DATI 5 — File modificati negli ultimi 7 giorni
{recent_files()}

## DATI 6 — Igiene struttura
{igiene()}

## COMPITO

Componi il report in formato Slack (asterischi singoli per il grassetto, nessun heading markdown #):

*OTTO | Check Workspace — sabato {today_str}*

*Agenti* — una riga per agente (PIERO, VERA, MARCO, ALDO): girato o no, quando, problemi (es. fonti RSS in timeout nei log).
*Cosa va* — massimo 3 punti: cosa ha funzionato questa settimana (produzione, cadenze rispettate).
*Cosa non va* — massimo 4 punti: task list non aggiornate, deadline "creare entro" a rischio nei prossimi 7 giorni, draft senza stato di pubblicazione, igiene struttura.
*Settimana prossima* — le 3 scadenze più vicine dalle task list, con data e giorno.
*Suggerimento* — un solo intervento concreto per la settimana, il più utile.

REGOLE: niente trattini lunghi, niente avverbi in -mente, tono asciutto. Verifica i giorni della settimana contro l'ancora 01/07/2026 = mercoledì. Rispondi SOLO con il testo del report."""


def main():
    today = datetime.date.today()
    today_str = today.strftime("%d/%m")
    output_path = OUTPUT_DIR / f"{today.strftime('%Y-%m-%d')}-check.md"

    if output_path.exists():
        log(f"Check già generato oggi ({output_path.name}), esco.")
        return

    log("Raccolgo i dati e chiamo claude CLI...")
    prompt = build_prompt(today_str)

    result = run_claude(
        [CLAUDE_BIN, "-p", prompt],  # composizione pura, nessun tool necessario
        timeout=180, retries=1
    )
    if result is None or result.returncode != 0 or not result.stdout.strip():
        err = result.stderr[:300] if result is not None else "timeout dopo retry"
        log(f"Claude error: {err}")
        notify_failure("Check non generato, vedi log/otto.error.log")
        sys.exit(1)

    report = result.stdout.strip()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report + "\n")
    log(f"Check salvato: {output_path}")

    slack_prompt = f"Usa slack_send_message per inviare questo DM a {SLACK_USER}. Invia il testo così com'è, senza modifiche:\n\n{report}"
    slack_result = run_claude(
        [CLAUDE_BIN, "-p", slack_prompt,
         "--allowedTools", "mcp__claude_ai_Slack__slack_send_message"],
        timeout=60, retries=1
    )
    if slack_result is None or slack_result.returncode != 0:
        err = slack_result.stderr[:200] if slack_result is not None else "timeout dopo retry"
        log(f"Slack error: {err}")
        notify_failure(f"Check salvato ma DM Slack non inviato: {output_path.name}")
        sys.exit(1)
    log("DM Slack inviato")

    subprocess.run([
        "osascript", "-e",
        f'display notification "Check workspace pronto" with title "OTTO" subtitle "{today_str}" sound name "Glass"'
    ])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"Errore non gestito: {e}")
        notify_failure(f"Errore non gestito: {e}")
        sys.exit(1)
