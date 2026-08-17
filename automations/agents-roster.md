# Agenti Workspace — Roster e Stato

> Aggiornato: 12/08/2026 (check completo workspace — stato verificato su `launchctl list`, `crontab -l`, `RemoteTrigger list`, log locali e chiamate live ai connettori, non dichiarato a memoria). Questo è il file operativo di riferimento: la memoria di Claude punta qui.
>
> **Check del 12/08:** il roster era accurato sul "dove gira cosa" (prima volta dopo due check consecutivi in cui era stale). Il problema trovato era altrove, dentro i prompt: **ALDO e MARCO avevano hardcoded la deadline "contratto Italia Staryes/VittoriaBet entro 9 luglio"**, scaduta da 34 giorni, e la ripetevano a ogni run. Stessa classe di errore del LinkedIn Post Reminder disattivato il 02/08. Correzioni applicate lo stesso giorno, dettaglio sotto.
>
> **Principio adottato:** un agente, un posto solo. Tutto su cloud tranne PIERO, che deve stare in locale perché la sandbox cloud non raggiunge le fonti RSS.
>
> **Regola nuova (12/08): nessuna data hardcoded nei prompt degli agenti.** Le scadenze si leggono da Linear a ogni run. Un prompt che contiene una data la ripeterà per sempre, anche quando è morta, e nessuno se ne accorge finché non si rilegge il prompt. ALDO e MARCO ora hanno una nota esplicita che glielo vieta e che impone di segnalare il fallimento della chiamata Linear invece di riempire il vuoto.

## Roster attivo

| Agente | Ruolo | Dove gira | Schedule | Stato verificato 12/08 |
|---|---|---|---|---|
| **PIERO** | News Radar iGaming (RSS → morning brief → Slack) | **Locale** (launchd `com.albertol.piero`) + skill `/piero` on demand | Ogni giorno 07:00 e 12:40 Roma | ✅ Attivo, ultimo run 12/08 07:01 (fetch 10 fonti in ~9 secondi, l'hardening dell'08/08 ha retto). La versione cloud (`trig_01R5LLasoxRqBYz2w48MSRh6`) resta disattivata per il blocco RSS del 23/07, mai ritestato. Alberto lo lancia anche a mano con `/piero`: dal 12/08 la skill è allineata al job (salva l'archivio e manda il DM), vedi sotto |
| **MARCO** | BDM / Pipeline review (Pipedrive Dealbot + Linear + Granola) | Cloud cron | Lun 07:00 Roma (`0 5 * * 1` UTC) | ✅ Attivo — `trig_018CSmAP6w4tyJcyenYNZBMd`. Prompt corretto il 12/08: rimossa la deadline hardcoded, aggiunto il divieto di inventare date, aggiunto un controllo che segnala le issue Linear il cui titolo contraddice la due date. Modello portato a Sonnet 5. ⚠️ Resta legato a Pipedrive: da rifare con la migrazione HubSpot |
| **VERA** | **Lock editoriale settimanale** (repo → tavolo del lock → Slack) | **Solo cloud** | **Gio 09:00 Roma** (`0 7 * * 4` UTC) | ✅ Attivo — `trig_011zLYAjZLmCnbYTNhcmjVvo`, prossimo run **gio 20/08**. **Riconvertita il 17/08/2026**: era "Brief editoriale settimanale" del venerdì 12:00, che sotto il nuovo piano newsletter arrivava a scrittura già iniziata. Ora prepara il lock del giovedì: legge la rassegna PIERO del giorno, conta le schede in banca e segnala le scadute, elenca cosa è già stato coperto in settimana, ricorda il test delle tre letture. **Non decide i temi, prepara il tavolo.** Nessuna data né tema hardcoded, tutto letto dal repo a ogni run; ha una sezione obbligatoria "Buchi in questo brief" che elenca i file non leggibili invece di tacere. Orario alle 09:00 e non alle 08:00 perché il sync del repo gira ogni 3 ore e il brief PIERO delle 07:00 deve avere tempo di arrivare |
| **ALDO** | General Manager / Daily brief (Calendar + Gmail + Linear) | Cloud cron | **Tutti i giorni 08:30 Roma** (`30 6 * * *` UTC) | ✅ Attivo — `trig_01Li3P6YAkhP2gLGb5VzsDsm`. Modificato il 12/08: passato da lun-ven a **7 giorni su 7** per il requisito di copertura weekend e festivi. Nel weekend gira in **versione leggera** (salta le email Softswiss, tiene calendario e scadenze Linear); se non c'è nulla manda una riga sola invece di un brief vuoto. Rimossa la deadline hardcoded. Modello portato a Sonnet 5 |
| **OTTO** | Check workspace del sabato | **Solo cloud** | Sab 08:30 Roma (`30 6 * * 6` UTC) | ✅ Attivo — `trig_01LRGJfc8rvJb3SGnMLbWqDf`, ultimo run 08/08, prossimo 15/08. Regola di onestà dell'08/08 invariata |
| **Linear-deadline-reminder** | Scadenze Linear a 3 giorni → bozza Gmail + DM Slack | Cloud cron | Ogni giorno 08:00 Roma (`0 6 * * *` UTC) | ✅ Attivo — `trig_01KPMhuagKVioGPGeaEkwf4k`, ultimo run 12/08. Manda un DM esplicito se Linear non risponde, invece di tacere: è la rete di sicurezza decisa il 09/08 al posto di una routine di controllo dedicata |
| TONY | LasVegas (campagne + community) | — | — | ⏸ Bloccato: serve allineamento con Luigi + nessun connector LasVegas. Non costruire prima |

### PIERO: job schedulato e skill allineati (12/08/2026)

Prima del 12/08 il job launchd e la skill `/piero` facevano cose diverse: il job salvava l'archivio in `03-giornalismo/news-igaming 2026/` e mandava il DM Slack, la skill stampava solo in chat. Conseguenza: nei giorni in cui il Mac era spento all'alba e Alberto lanciava `/piero` a mano, l'archivio restava bucato e OTTO il sabato segnalava PIERO come fermo, perché cerca proprio quel DM come prova di vita. Buchi reali negli ultimi 30 giorni: 26/07, 29/07, 30/07.

Dal 12/08 la skill fa le stesse tre cose del job (chat, archivio, DM Slack con prefisso `PIERO |`). Se il brief del giorno esiste già non lo sovrascrive, lo affianca come `morning-brief-manuale.md`. Il job resta caricato come rete di sicurezza.

### Avviso copertura italiana (13/08/2026)

Il 13/08 le due sole fonti italiane, Jamma.it e AGiMeG, sono risultate irraggiungibili: 503 su porta 80 e connection reset su 443. Causa identificata da Alberto: **la rete WiFi a cui era agganciato filtra quei domini**. Non è un guasto dei siti né un problema di PIERO.

Il difetto vero non era il blocco ma il silenzio: il brief usciva con 19 angoli Sitiscommesse su 20 a `N/A`, indistinguibile da una giornata senza notizie italiane. Dato che PIERO gira in locale, il problema si ripresenta ogni volta che Alberto è su quella rete.

Correzione applicata lo stesso giorno, sia in `piero.py` (funzioni `italian_coverage`, `coverage_banner`, `_coverage_rule`) sia nella skill `/piero`:

- se **nessuna** fonte IT risponde, il brief si apre con un avviso esplicito e il DM Slack lo ripete
- se ne risponde **una sola**, avviso più leggero di copertura parziale
- in entrambi i casi il modello riceve l'istruzione di non inventare angoli Sitiscommesse da notizie internazionali per riempire il vuoto

Il banner è scritto dallo script, non chiesto al modello: deve comparire sempre quando la condizione è vera, senza dipendere dal fatto che il modello si ricordi di generarlo. Testato sui 5 casi possibili più un fetch reale contro la rete bloccata.

**Se serve la copertura italiana e la rete la blocca:** cambiare rete (hotspot) e rilanciare `/piero`, che salva il brief affiancato senza sovrascrivere quello già in archivio.

### Job locali rimasti (launchd)

| Job | Stato | Nota |
|---|---|---|
| `com.albertol.piero` | ✅ Caricato | Vedi sopra, 07:00 + 12:40 |
| `com.albertol.cloudsync` | ✅ Caricato | Sync del repo cloud ogni 3 ore. **Scope allargato il 17/08/2026:** `news-igaming 2026/` era esclusa dal 20/07 come archivio storico di PIERO pre-migrazione cloud, ma da allora PIERO è tornato locale e ci scrive il brief ogni giorno, e la nuova VERA (lock del giovedì) legge proprio quel brief dal repo. Senza quella cartella VERA non avrebbe mai trovato la rassegna. Restano esclusi i `piero-raw.json`, 1 MB dei 1,7 MB totali, inutili a VERA. Sync manuale eseguito lo stesso giorno (commit `b32bb56`) per non far dipendere il primo run del 20/08 dalla finestra automatica |
| `com.albertol.otto` | ⏸ Scaricato l'08/08 | Plist rinominato `.plist.disabled`, copia in `archive/launchd-disattivati-2026-08/` |
| `com.albertol.vera` | ⏸ Scaricato l'08/08 | Come sopra |
| crontab `cleanup.sh` | ⚠️ Caricato ma mai eseguito al nuovo orario | Spostato dalle 23:47 alle 12:47 del 28 perché alle 23:47 il Mac dorme. **Verifica del 12/08:** `cleanup-cron.log` è ancora fermo al 28/06 e mancano sia `cleanup-log-2026-07.txt` sia quello di agosto, quindi il nuovo orario non ha ancora prodotto un run. Non è una prova di guasto: lo spostamento è successivo al 28/07, quindi il primo test reale è il **28/08/2026 alle 12:47**. Se quel giorno il log resta fermo, il job è rotto e va indagato |

Post-call workflow: skill on demand (`/post-call`), non schedulata — invariata.

### ✅ Linear riconnesso il 09/08/2026

Era rimasto scollegato dal 03/08 al 08/08 (sei giorni, brief ALDO e pipeline review MARCO senza scadenze). Alberto ha riautenticato il connettore dalle impostazioni claude.ai il 09/08; verificato funzionante con `get_workspace` (workspace AlbertoBDMGA risponde).

**Decisione presa il 09/08 su come evitare che si ripeta in silenzio:** niente routine di controllo/riconnessione giornaliera — un token OAuth non si scollega per calendario, quindi ricontrollarlo ogni mattina è lavoro sprecato quando è collegato e inutile in anticipo quando si scollega. Ci si affida a `Linear-deadline-reminder` (aggiornata l'08/08), che manda già un DM Slack esplicito quando la chiamata fallisce invece di restare in silenzio, più la segnalazione diretta di Claude a inizio sessione se un tool Linear torna un errore di auth.

## Routine trovate fuori dal roster (scoperte nel check del 02/08/2026)

Interrogando `RemoteTrigger list` sono emerse 6 routine mai documentate qui, oltre ai 5 agenti sopra. Decisioni prese durante il check:

| Trigger | Cosa fa | Creata | Decisione 02/08 |
|---|---|---|---|
| `trig_01SDsLJnhYQcxE4p2tUGSCto` — "assistente editoriale iGaming" | Briefing giornaliero (08:30 Roma) sulle 3 notizie iGaming del giorno prima, via WebSearch → bozza Gmail. **Sovrappone la funzione di PIERO** con un meccanismo diverso (WebSearch+Gmail invece di RSS+Slack), creata il 08/06 — prima ancora di PIERO | 08/06/2026 | ⏸ **Disattivata l'08/08/2026.** PIERO locale produce il brief tutti i giorni via Slack, che è dove Alberto lo legge: questa faceva un terzo briefing quotidiano in una bozza Gmail che nessuno apre. Riattivabile in un secondo se serve un backup |
| `trig_01KPMhuagKVioGPGeaEkwf4k` — "daily Linear deadline reminder" | Ogni giorno (08:00 Roma) controlla le issue Linear del team AlbertoBDMGA con scadenza nei 3 giorni successivi, crea bozza Gmail con l'elenco | 09/06/2026 | **Lasciata attiva** — copre esattamente il gap che questo file segnalava come "da fare" (vedi sezione sotto): esisteva già, semplicemente non era mai stata scritta qui |
| `trig_01L2wP4nyxfp1UHhkqGrBmvg` — "ALB-17 Weekly Review Reminder" | Ogni lunedì, DM Slack con lo stato dell'issue Linear ALB-17 (Onboarding Skeleton Phase 1), scadenza indicata nel messaggio: 30/06/2026 | 10/06/2026 | ⏸ **Disattivata il 02/08** — scadenza superata da un mese, nessun riferimento ad ALB-17 nel resto del workspace, reminder ormai a vuoto. **Verificare su Linear** se l'issue è chiusa prima di riattivarla o cancellarla definitivamente |
| `trig_01WyDwxbxyNBTmET6Qc3KmtK` — "LinkedIn Post Reminder - 24h advance" | Ogni giorno (08:00 Roma) controllava se il giorno dopo coincideva con una data del piano editoriale LinkedIn, con un calendario **scritto a mano nel prompt** (hardcoded fino a inizio settembre) | 26/06/2026 | ⏸ **Disattivata il 02/08** — il calendario hardcoded non è mai stato aggiornato dopo i riflow del piano (slittamento 2 settimane del 14/07, cambio modello del 27/07, aggiornamenti del 01/08): confermato dal log, ha girato regolarmente ma su date/temi ormai disallineati dal piano reale, quindi o taceva o avrebbe segnalato il contenuto sbagliato. Coincide con l'issue già nota in memoria sui reminder che non si aggiornano da soli sui riflow |
| `trig_01RWypRJzSp6VSRxE1MGdpL2` — PIERO (versione precedente) | Copia quasi identica del prompt PIERO attuale, cron diverso (`0 6 * * *` invece di `0 5 * * *`) | 23/07/2026 | Già disabilitata, nessuna azione. Doppione residuo — l'API non espone un comando di cancellazione: se si vuole eliminarla definitivamente va fatto dall'interfaccia claude.ai (routine cloud) |
| 3 reminder one-off (Slack, S1 LinkedIn + un test) | Promemoria puntuali già scattati (`ended_reason: run_once_fired`) | giugno/luglio | Nessuna azione — esauriti, non consumano schedule |

## Cosa serve davvero — aggiornato 02/08

Le prime due righe della tabella sopra **sostituiscono** il punto "Deadline contenuti dentro ALDO" che questo file elencava come lavoro da fare: il reminder Linear a 3 giorni esiste già dal 09/06, semplicemente non era mai stato scritto qui. Non serve costruirlo di nuovo.

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
3. ~~**Manutenzione PIERO**~~ — fatta l'08/08/2026. Tutte e 16 le fonti testate una per una:
   - **10 attive e verificate**: iGaming Business, EGR Global (serve `www.`), Casino Beats, SBC News, European Gaming, Gambling Insider, CalvinAyre (senza slash finale), G3 Newswire (`g3newswire.com`), Jamma, **AGiMeG recuperata** con l'URL giusto `https://www.agimeg.it/feed/` (il vecchio `agimeg.it/feed` faceva un redirect su cui la run si appendeva).
   - **6 disattivate con motivo scritto in `piero-sources.json`**: Gioco News e Betting Business (domini inesistenti, NXDOMAIN), Agipro News (404 su ogni path di feed), Yogonet (l'URL risponde ma restituisce HTML, non RSS), FocusGN e iGaming Today (403 anti-bot su tutto il sito).
   - **Causa vera delle run appese**: `feedparser` senza timeout di rete. Ora c'è `socket.setdefaulttimeout(20)`, il download passa da `curl --max-time 20` (che risolve anche Casino Beats, che chiude la connessione alle librerie Python), un retry per fonte e il log del tempo per fonte. La fase di fetch è passata da ore a 4 secondi.
   - Resta da fare: migrare a `--allowedTools` scopati come OTTO.
4. **MARCO v2 su HubSpot** — non investire altro sul workaround Dealbot/Pipedrive; quando la migrazione HubSpot è operativa, rifare la fonte dati di MARCO. Fino ad allora MARCO resta com'è.
5. **Niente agenti nuovi oltre questi** — TONY resta congelato finché Luigi non è allineato; il valore adesso è far girare bene i cinque esistenti, non aggiungerne.

## File tecnici

- `piero.py` + `piero-sources.json` — **versione operativa**, schedulata in locale (07:00 e 12:40). Hardening dell'08/08: timeout di rete, download via curl, retry, log per fonte, fonti morte disattivate con la motivazione
- `vera.py` — VERA (hardening 20/07: timeout/retry/notifica)
- `otto.py` — OTTO (check sabato, hardening 20/07) → report in `check-sabato/`
- `post-call-cron.md` — workflow post-call
- `logs/` — vera.log, otto.log (+ .error.log). piero.log resta come storico pre-migrazione
- Plist launchd: `~/Library/LaunchAgents/com.albertol.piero.plist` attivo; `com.albertol.{vera,otto}.plist` scaricati e rinominati `.plist.disabled` l'08/08 (copia di sicurezza in `../archive/launchd-disattivati-2026-08/`)

## Routine ID (cloud) — verificate 02/08/2026 via RemoteTrigger list

| Agente | Trigger ID | Stato |
|---|---|---|
| PIERO | trig_01R5LLasoxRqBYz2w48MSRh6 | Disattivata |
| PIERO (doppione residuo) | trig_01RWypRJzSp6VSRxE1MGdpL2 | Disattivata |
| MARCO | trig_018CSmAP6w4tyJcyenYNZBMd | Attiva |
| ALDO | trig_01Li3P6YAkhP2gLGb5VzsDsm | Attiva |
| OTTO | trig_01LRGJfc8rvJb3SGnMLbWqDf | Attiva |
| VERA | trig_011zLYAjZLmCnbYTNhcmjVvo | Attiva |
| VERA (ID storico, non usare) | trig_01DA1gYJLFTNbqUwcG4rw1uA | Disattivata |
| Doppione PIERO via Gmail | trig_01SDsLJnhYQcxE4p2tUGSCto | Disattivata l'08/08/2026 |
| Linear deadline reminder (3gg) | trig_01KPMhuagKVioGPGeaEkwf4k | Attiva |
| ALB-17 Weekly Review Reminder | trig_01L2wP4nyxfp1UHhkqGrBmvg | Disattivata 02/08 |
| LinkedIn Post Reminder 24h | trig_01WyDwxbxyNBTmET6Qc3KmtK | Disattivata 02/08 |
