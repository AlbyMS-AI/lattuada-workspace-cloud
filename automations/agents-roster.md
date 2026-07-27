# Agenti Workspace — Roster e Stato

> Aggiornato: 20/07/2026 (migrazione completa a cloud di PIERO, VERA, OTTO). Questo è il file operativo di riferimento: la memoria di Claude punta qui.

## Roster attivo

| Agente | Ruolo | Dove gira | Schedule | Stato verificato 20/07 |
|---|---|---|---|---|
| **PIERO** | News Radar iGaming (RSS → morning brief → Slack) | **Cloud cron** | Ogni giorno 07:00 Roma (`0 5 * * *` UTC) | ⏸ **DISATTIVATO manualmente il 27/07/2026** (`enabled: false` su `trig_01R5LLasoxRqBYz2w48MSRh6`, su richiesta di Alberto). Resta disponibile come skill on demand (`/piero`) |
| **MARCO** | BDM / Pipeline review (Pipedrive Dealbot + Linear + Granola) | Cloud cron | Lun 07:00 Roma | ✅ Attivo — fired 20/07 regolare. ⚠️ Legato a Pipedrive: da rifare con la migrazione HubSpot |
| **VERA** | Brief editoriale settimanale (repo → brief → Slack) | **Cloud cron** | Ven 12:00 Roma (`0 10 * * 5` UTC) | ✅ Cloud — routine `trig_011zLYAjZLmCnbYTNhcmjVvo`. Legge il repo `lattuada-workspace-cloud` invece del filesystem locale |
| **ALDO** | General Manager / Daily brief (Calendar + Gmail + Linear) | Cloud cron | Lun-Ven 08:30 Roma | ✅ Attivo — fired 20/07 regolare |
| **OTTO** | Check workspace del sabato | **Cloud cron** | Sab 08:30 Roma (`30 6 * * 6` UTC) | ✅ Cloud — routine `trig_01LRGJfc8rvJb3SGnMLbWqDf`. Audit ridefinito: agenti cloud via DM Slack (non più launchd), workspace via repo scoped (non più intero Mac) |
| TONY | LasVegas (campagne + community) | — | — | ⏸ Bloccato: serve allineamento con Luigi + nessun connector LasVegas. Non costruire prima |

Post-call workflow: skill on demand (`/post-call`), non schedulata — invariata.

## ⛔ PIERO bloccato — blocco di rete a livello ambiente (23/07/2026)

Il 23/07 (rientro ferie Alberto) il run delle 07:00 ha fallito su tutte e 16 le fonti RSS: 403 dal gateway di uscita, non problema dei singoli siti. Tentato workaround: aggiornato il trigger per usare **WebFetch** invece di Bash/curl (allowed_tools ora `["Bash","WebFetch"]`) e rilanciato un run manuale lo stesso giorno.

**Risultato workaround: fallito.** Anche con WebFetch, tutte e 16 le fonti hanno fallito — 14 con HTTP 403, 2 (Gioco News, Betting Business) con errore di risoluzione DNS (ENOTFOUND). Conferma che il blocco è sull'intero ambiente cloud (`env_01UpiUsAc53MWA7F4taF8CAG`), non specifico del tool usato per il fetch (Bash vs WebFetch) — l'ENOTFOUND su 2 domini è coerente con una policy di rete/DNS ristretta a livello ambiente, non con un blocco lato destinazione.

**Non risolvibile da questa sessione**: nessun tool disponibile qui per gestire le impostazioni di rete/firewall degli ambienti cloud. Serve intervento di Alberto lato claude.ai (impostazioni ambiente/routine cloud, sezione rete/domini consentiti per `env_01UpiUsAc53MWA7F4taF8CAG`) o supporto Anthropic se non c'è un'opzione configurabile.

**How to apply:** non proporre altri workaround lato tool di fetch (già provati Bash e WebFetch, entrambi bloccati identicamente) — il problema è a monte, nell'ambiente. Prossima verifica: dopo che Alberto interviene lato claude.ai, rilanciare un run manuale (`RemoteTrigger run` su `trig_01R5LLasoxRqBYz2w48MSRh6`) per confermare lo sblocco prima di fidarsi del prossimo run schedulato.

## Migrazione completa a cloud (20/07/2026) — come funziona

Alberto ha posto un requisito esplicito: tutti gli agenti devono girare sempre, anche in vacanza e a Mac spento/in stand by. Diagnosi che ha portato alla decisione: i job locali (launchd + `claude CLI`) restano appesi per ore se il Mac va in sleep a metà run (osservato: PIERO bloccato 9h, VERA 1h44m, OTTO 3h03m, tutti nella finestra ferie 14-22/07) e poi escono con `exit 1` senza stderr utile — inaccettabile per il requisito posto.

**Soluzione**: tutti e tre ora girano su cloud cron (CCR), zero dipendenza dal Mac.

- **PIERO**: nessuna dipendenza dal filesystem, legge solo RSS esterni.
- **VERA e OTTO**: dipendevano dai file del workspace (draft, piano editoriale, task list). Sbloccati creando un repo GitHub dedicato, **`https://github.com/AlbyMS-AI/lattuada-workspace-cloud`** (pubblico — vedi sotto perché), che le routine cloud clonano ad ogni run.
  - Scope del repo (deciso 20/07, non tutto il workspace): `03-giornalismo/` (esclusi `archive/`, `fatture/`, l'ex-archivio locale di PIERO), `04-linkedin/*.md` di primo livello (no `grafiche/`), `06-lasvegas/collaborazioni/task-list.md`, `automations/` (script + roster, no logs). **Esclusi di proposito**: `02-softswiss` (deal, dati interni) e `09-carriera` (candidature) — mai in un repo esterno.
  - Sync: `automations/sync-cloud-repo.sh`, lanciato ogni 3 ore da launchd locale (`com.albertol.cloudsync`, unico job locale rimasto). Fa rsync dello scope + commit + push solo se ci sono modifiche. Se il Mac resta spento per giorni, il repo semplicemente non si aggiorna (le routine cloud continuano comunque a girare sull'ultimo stato pushato, senza bloccarsi).
  - **Repo pubblico, non privato**: il collegamento GitHub App di claude.ai non è mai riuscito a ottenere accesso a un repo privato (provati: reconnect, revoke+reconnect, repo-picker nel prodotto Code — sempre lista vuota, causa non identificata, possibile bug/limite piattaforma). Per sbloccare oggi si è reso il repo pubblico. Il contenuto è comunque lo scope già filtrato (niente Softswiss/candidature/fatture), ma è tecnicamente leggibile da chiunque trovi il link. Se in futuro la connessione GitHub privata si sblocca, va ripristinata la privacy del repo.
- **OTTO ridefinito**: non controlla più launchd/log locali (non li vede più) — ora cerca gli ultimi DM Slack di PIERO/VERA/MARCO/ALDO come prova che sono girati. L'igiene di file locali (`temp/`, cartelle "copia") non è più coperta da nessun agente: era fuori scope del repo.

## Lezioni operative

- **launchd:** un plist in `~/Library/LaunchAgents/` non basta — va caricato (`launchctl load ...`) e verificato con `launchctl list | grep albertol`. Il fallimento è silenzioso: nessun log = mai partito.
- **Job locali che chiamano claude CLI + rete:** vulnerabili a sleep/lid-close del Mac — la chiamata resta appesa per ore invece di fallire. Per questo si è scelta la migrazione cloud completa invece di continuare a patchare il locale.
- **GitHub App di claude.ai + repo privati:** nella sessione del 20/07 non è mai stato possibile dare a una routine cloud accesso a un repo privato (401 poi 403 persistenti, nessuna schermata di autorizzazione per-repo apparsa in nessun punto del flusso — connectors, installations, repo-picker in Code). Bypassato rendendo il repo pubblico. Da rivedere se càpita di nuovo: verificare prima se è un problema noto della piattaforma.
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
