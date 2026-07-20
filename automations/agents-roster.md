# Agenti Workspace — Roster e Stato

> Aggiornato: 20/07/2026 (migrazione PIERO a cloud + hardening VERA/OTTO). Questo è il file operativo di riferimento: la memoria di Claude punta qui.

## Roster attivo

| Agente | Ruolo | Dove gira | Schedule | Stato verificato 20/07 |
|---|---|---|---|---|
| **PIERO** | News Radar iGaming (RSS → morning brief → Slack) | **Cloud cron** (migrato 20/07, era locale) | Ogni giorno 07:00 Roma (`0 5 * * *` UTC) | ✅ Migrato in cloud — routine `trig_01R5LLasoxRqBYz2w48MSRh6`. Plist locale scaricato (`launchctl unload`), file `piero.py` conservato ma non più schedulato. Non salva più file locale: il brief completo va per intero nel DM Slack |
| **MARCO** | BDM / Pipeline review (Pipedrive Dealbot + Linear + Granola) | Cloud cron | Lun 07:00 Roma | ✅ Attivo — fired 20/07 regolare. ⚠️ Legato a Pipedrive: da rifare con la migrazione HubSpot |
| **VERA** | Brief editoriale settimanale (workspace → brief → Slack) | Locale, launchd `com.albertol.vera` | Ven 12:00 | ⚠️ Run 17/07 fallito (appeso 1h44m poi exit 1, probabile sleep del Mac durante ferie) — **hardening 20/07**: timeout ridotto a 180s/60s, un retry automatico, notifica macOS locale se fallisce anche dopo retry |
| **ALDO** | General Manager / Daily brief (Calendar + Gmail + Linear) | Cloud cron | Lun-Ven 08:30 Roma | ✅ Attivo — fired 20/07 regolare |
| **OTTO** | Check workspace del sabato | Locale, launchd `com.albertol.otto` | Sab 08:30 | ⚠️ Run 18/07 fallito (appeso 3h03m poi exit 1, stessa causa di VERA) — **hardening 20/07**: stesso fix di VERA + audit aggiornato (PIERO non è più tra gli "agenti locali" da controllare via launchd, ora è cercato tra i DM cloud insieme a MARCO/ALDO) |
| TONY | LasVegas (campagne + community) | — | — | ⏸ Bloccato: serve allineamento con Luigi + nessun connector LasVegas. Non costruire prima |

Post-call workflow: skill on demand (`/post-call`), non schedulata — invariata.

## Perché PIERO è passato al cloud e VERA/OTTO no

20/07/2026: Alberto ha chiesto affidabilità totale anche a laptop chiuso (ferie). Diagnosi: i job locali dipendono dal Mac acceso e in rete — se il lid si chiude a metà run, la chiamata a `claude CLI` resta appesa per ore (osservato: PIERO bloccato 9h, VERA 1h44m, OTTO 3h03m, tutti nella finestra ferie 14-22/07) e alla riapertura esce con `exit 1` senza stderr utile.

PIERO è stato l'unico migrabile subito in cloud puro: legge solo RSS esterni e scrive solo un DM Slack, nessuna dipendenza dal filesystem locale.

VERA (legge draft/piano editoriale dal workspace) e OTTO (audita launchd e file locali per definizione) **non possono girare in cloud** finché `workspace/` non diventa un repo git accessibile alle routine cloud — è una decisione strutturale non ancora presa, discussa il 20/07 e rimandata. Fino ad allora restano locali ma con timeout stretti + retry + notifica macOS di fallback, così un blocco dura minuti non ore ed è sempre visibile (anche offline) invece di fallire in silenzio.

## Lezioni operative

- **launchd:** un plist in `~/Library/LaunchAgents/` non basta — va caricato (`launchctl load ...`) e verificato con `launchctl list | grep albertol`. Il fallimento è silenzioso: nessun log = mai partito.
- **Job locali che chiamano claude CLI + rete:** vulnerabili a sleep/lid-close del Mac — la chiamata resta appesa per ore invece di fallire. Mitigazione applicata (VERA/OTTO, 20/07): timeout stretti (180s/60s) + un retry + notifica macOS locale su fallimento finale. Non risolve "Mac spento per giorni", solo "blocco silenzioso di ore".
- **Permessi claude CLI negli script:** mai `--dangerously-skip-permissions` su job non presidiati. Si usano permessi scopati: `--allowedTools "mcp__claude_ai_Slack__slack_send_message"` (OTTO già così; VERA ancora con `--dangerously-skip-permissions`, da migrare).
- **Slack DM a se stesso** = canale di output standard degli agenti (auto-approvato). Qualsiasi messaggio a terzi resta manuale.

## Cosa serve davvero al lavoro quotidiano — valutazione 12/07

Il set attuale copre bene: rassegna stampa (PIERO), pipeline commerciale (MARCO), agenda giornaliera (ALDO), raccordo editoriale (VERA), supervisione (OTTO). Interventi utili, in ordine di valore:

1. **Deadline contenuti dentro ALDO** — oggi le scadenze "creare entro" della task list LinkedIn non arrivano nel brief mattutino perché ALDO (cloud) non legge il workspace. Via più semplice: creare issue Linear per le deadline di contenuto (il post-call già usa Linear, ALDO già lo legge). Nessun agente nuovo.
2. **Skill "analizza post" + "aggiorna analytics"** — task MLR Lezione 6 ancora aperti; è il pezzo mancante del ciclo LinkedIn (pubblichi ma non misuri in modo sistematico). Da fare come skill on demand, non come cron.
3. **Manutenzione PIERO** — disabilitare o sostituire la fonte "iGaming Today" (timeout da 2 giorni, allunga la run di 10 minuti); migrare a `--allowedTools` scopati come OTTO.
4. **MARCO v2 su HubSpot** — non investire altro sul workaround Dealbot/Pipedrive; quando la migrazione HubSpot è operativa, rifare la fonte dati di MARCO. Fino ad allora MARCO resta com'è.
5. **Niente agenti nuovi oltre questi** — TONY resta congelato finché Luigi non è allineato; il valore adesso è far girare bene i cinque esistenti, non aggiungerne.

## File tecnici

- `piero.py` + `piero-sources.json` — versione locale storica, non più schedulata dal 20/07 (logica replicata nel prompt della routine cloud)
- `vera.py` — VERA (hardening 20/07: timeout/retry/notifica)
- `otto.py` — OTTO (check sabato, hardening 20/07) → report in `check-sabato/`
- `post-call-cron.md` — workflow post-call
- `logs/` — vera.log, otto.log (+ .error.log). piero.log resta come storico pre-migrazione
- Plist launchd: `~/Library/LaunchAgents/com.albertol.{vera,otto}.plist` attivi; `com.albertol.piero.plist` scaricato (`launchctl unload`) ma non cancellato, per rollback

## Routine ID (cloud)

| Agente | Trigger ID |
|---|---|
| PIERO | trig_01R5LLasoxRqBYz2w48MSRh6 |
|---|---|
| MARCO | trig_018CSmAP6w4tyJcyenYNZBMd |
| ALDO | trig_01Li3P6YAkhP2gLGb5VzsDsm |
| VERA (cloud, DISATTIVATA 03/07) | trig_01DA1gYJLFTNbqUwcG4rw1uA — sostituita dal launchd locale |
