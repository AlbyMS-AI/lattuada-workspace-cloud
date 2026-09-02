# Agenti Workspace — Roster e Stato

> **Aggiornato: 01/09/2026** — ALDO riscritto in v2, nuova routine Check serale, `Linear-deadline-reminder` in dismissione. Registro task unificato su Linear, convenzioni in `linear-convenzioni.md`. Dettaglio nella sezione "ALDO v2 e il registro unico su Linear". Terzo caso della stessa classe di errore (elenco di progetti hardcoded dentro il prompt di ALDO), da cui la regola generalizzata: **mai un elenco di entità mutevoli dentro un prompt**.
>
> Aggiornato in precedenza: 12/08/2026 (check completo workspace — stato verificato su `launchctl list`, `crontab -l`, `RemoteTrigger list`, log locali e chiamate live ai connettori, non dichiarato a memoria). Questo è il file operativo di riferimento: la memoria di Claude punta qui.
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
| **ALDO v2** | **Assistente personale / Agenda giornaliera** (Calendar + Gmail + Linear + Slack) | Cloud cron | **Tutti i giorni 08:30 Roma** (`30 6 * * *` UTC) | ✅ Attivo — `trig_01Li3P6YAkhP2gLGb5VzsDsm`. **Riscritto il 01/09/2026** (vedi sezione dedicata sotto): non è più un aggregatore di tre fonti ma un assistente bidirezionale. Sequenzia al massimo cinque azioni ordinate, ha orizzonte a 72 ore, chiude le issue leggendo la risposta di Alberto al check serale, e il lunedì genera le ricorrenze LasVegas. Resta a 7 giorni su 7 con versione leggera nel weekend (deciso 12/08). Modello Sonnet 5 |
| **Check serale** | Chiede ad Alberto cosa ha chiuso oggi | Cloud cron | **Lun-ven 18:30 Roma** (`30 16 * * 1-5` UTC) | ✅ Attivo dal 01/09/2026 — `trig_01J3Go9PV537sbW6qanj9Gvc`. **Non scrive su Linear**: chiede e basta, la scrittura la fa ALDO il mattino dopo leggendo il thread. Se non ci sono issue scadute o in scadenza oggi non manda niente, per non diventare rumore quotidiano. Prende il posto nel bilancio del `Linear-deadline-reminder` |
| **OTTO** | Check workspace del sabato | **Solo cloud** | Sab 08:30 Roma (`30 6 * * 6` UTC) | ✅ Attivo — `trig_01LRGJfc8rvJb3SGnMLbWqDf`, verificato via `RemoteTrigger list_runs` il 31/08: run regolari 01, 08, 15, 22, 29/08, nessun buco. Output solo via DM Slack dal 20/07 (non più su `automations/check-sabato/`, che resta ferma all'08/08 come residuo pre-migrazione: normale, non un guasto). Regola di onestà dell'08/08 invariata |
| **Linear-deadline-reminder** | Scadenze Linear a 3 giorni → bozza Gmail + DM Slack | Cloud cron | Ogni giorno 08:00 Roma (`0 6 * * *` UTC) | ⏳ **Attivo ma in dismissione dal 01/09/2026** — `trig_01KPMhuagKVioGPGeaEkwf4k`. La sua funzione (orizzonte a 3 giorni) è ora dentro ALDO v2, sezione "Entro [giorno]", incrociata con calendario ed email. **Va disattivato dopo due giorni di ALDO v2 verificato, non prima**: se v2 avesse un problema, nel frattempo l'orizzonte resta coperto. La rete di sicurezza sul fallimento del connettore Linear, decisa il 09/08, è già replicata in ALDO con lo stesso testo. La bozza Gmail che produce non va preservata, Alberto non la apre |
| TONY | LasVegas (campagne + community) | — | — | ⏸ Bloccato: serve allineamento con Luigi + nessun connector LasVegas. Non costruire prima |

### PIERO: job schedulato e skill allineati (12/08/2026)

Prima del 12/08 il job launchd e la skill `/piero` facevano cose diverse: il job salvava l'archivio in `03-giornalismo/news-igaming 2026/` e mandava il DM Slack, la skill stampava solo in chat. Conseguenza: nei giorni in cui il Mac era spento all'alba e Alberto lanciava `/piero` a mano, l'archivio restava bucato e OTTO il sabato segnalava PIERO come fermo, perché cerca proprio quel DM come prova di vita. Buchi reali negli ultimi 30 giorni: 26/07, 29/07, 30/07.

Dal 12/08 la skill fa le stesse tre cose del job (chat, archivio, DM Slack con prefisso `PIERO |`). Se il brief del giorno esiste già non lo sovrascrive, lo affianca come `morning-brief-manuale.md`. Il job resta caricato come rete di sicurezza.

### Run da 60-100 minuti e timeout, corretto il 31/08/2026

Check completo del 31/08: negli ultimi 17 giorni mancavano sei brief (15, 16, 25, 26, 27, 30/08) e quelli usciti arrivavano 70-100 minuti dopo l'avvio, non ai 5-10 minuti attesi. Il log mostrava sei `TimeoutExpired` a 600s tra il 25 e il 30/08. Causa: la chiamata `claude -p` che genera il brief girava con accesso pieno a tutti i tool (nessun `--tools` in `piero.py`), quindi con `--dangerously-skip-permissions` il modello era libero di aprire i link delle notizie per verificarli invece di limitarsi a scrivere il testo. Prova: la chiamata gemella che manda il DM Slack, stesso binario e stesso flag di permessi ma senza link da seguire, impiegava 22 secondi.

Corretto aggiungendo `--tools ""` alla chiamata di generazione in `piero.py` (disabilita tutti i tool, forza puro completamento testuale). Testato lo stesso giorno con i dati reali del 18/08 (30 storie, il tetto `MAX_STORIES`) e del 31/08 (9 storie): 292s e 116s rispettivamente, output conforme al formato atteso. Timeout della subprocess abbassato da 600s a 420s, con margine reale sopra il caso peggiore misurato.

Non toccata la chiamata Slack (già veloce). Restano da recuperare via `/piero` manuale, se serve, i sei giorni senza brief.

### Falso allarme ALDO/VERA nei report OTTO — colpa del prompt di OTTO, corretto il 31/08/2026

Il report OTTO del 29/08 (e già quello del 22/08) segnalava un'anomalia: "ALDO ha coperto tutti i giorni della finestra senza buchi, weekend compresi: stessa anomalia di cadenza segnalata nelle ultime due settimane, ancora da chiarire se voluta o un errore." Verificato con `RemoteTrigger`: ALDO gira tutti i giorni senza un buco dal 22/08 al 31/08. Non è ALDO il problema.

Causa reale, trovata leggendo il prompt live della routine OTTO (`trig_01LRGJfc8rvJb3SGnMLbWqDf`, `updated_at` fermo all'08/08): il prompt aveva ancora hardcoded "ALDO: lun-ven" e "VERA: venerdì", cadenze cambiate il 12/08 (ALDO a 7 giorni su 7) e il 17/08 (VERA da brief del venerdì a lock editoriale del giovedì) — mai riportate nel prompt di OTTO. Stessa identica classe di errore delle date hardcoded corrette il 12/08 su ALDO e MARCO, stavolta dentro OTTO stesso, l'agente che dovrebbe fare da rete di controllo.

Corretto il 31/08: il prompt di OTTO non hardcoda più le cadenze attese. Ora legge `automations/agents-roster.md` (già nello scope del repo cloud) a ogni run e confronta i DM trovati con la cadenza reale lì dentro, con una nota esplicita che spiega perché (per non farlo ripetere in futuro se questo file cambia ancora). Prossima verifica naturale: run di sabato 05/09.

### ALDO v2 e il registro unico su Linear (01/09/2026)

Implementazione di `plans/2026-09-01-sistema-task-unico-linear-assistente.md`. Il punto di partenza era che Alberto perdeva i task: il calendario editoriale LinkedIn e i task LasVegas vivevano quasi solo in `04-linkedin/task-list.md` e `06-lasvegas/collaborazioni/task-list.md`, file che nessuna routine legge.

⚠️ **Correzione del 02/09 alla diagnosi.** Il 01/09 questa sezione diceva "cinque issue aperte a fronte di circa venticinque task reali". Il numero era sbagliato: veniva da una query filtrata su Todo e In Progress, che ignorava il Backlog. Le issue non completate erano **28**, con 23 in Backlog. L'errore ha prodotto un duplicato (ALB-105 creata su un ALB-94 che esisteva già) e ha fatto sopravvalutare quanto fosse vuoto il registro. La sostanza del problema regge, il calendario editoriale non era tracciato e ALDO ne vedeva metà, ma il numero no. Conseguenze misurate il 01/09: due contenuti scaduti da oltre due settimane, due consegne per il 02/09 che nessun promemoria avrebbe segnalato, cinque revisioni ricorrenti LasVegas inesistenti in qualsiasi sistema.

**Terzo caso della stessa classe di errore, trovato leggendo il prompt live.** ALDO faceva `list_issues` su un elenco di quattro progetti scritto dentro il prompt (Italy Market, BizDev Deals, Crypto & Special, BizDev Internal). I progetti sono otto: LasVegas, ML Russo e ogni issue senza progetto erano invisibili al brief **pur essendo dentro Linear**. Tre issue su cinque non arrivavano ad Alberto. È lo stesso meccanismo delle date hardcoded corrette il 12/08 su ALDO e MARCO e delle cadenze hardcoded corrette il 31/08 su OTTO: un elenco scritto in un prompt invecchia in silenzio e nessuno se ne accorge finché non lo si rilegge.

**Regola generalizzata:** un prompt non contiene mai un elenco di entità che possono cambiare (date, cadenze, progetti, fonti). Si interroga la sorgente a ogni run, oppure si legge da un file del repo.

Cosa fa ALDO v2, in ordine di run:

1. Legge il proprio DM del giorno prima e le risposte di Alberto nel thread del check serale, e **chiude su Linear** i task che Alberto dichiara fatti. Se un riferimento è ambiguo non chiude niente e lo segnala
2. Calendario di oggi
3. Email prioritarie, solo lun-ven
4. `list_issues` **sul team**, senza filtro progetto, separando in scadute/oggi, entro 72 ore, ferme su altri
5. Solo il lunedì: clona il repo pubblico e legge la sezione "Ricorrenze" di `06-lasvegas/collaborazioni/task-list.md`, creando le issue mancanti della settimana. Controlla prima se esistono già, così un secondo run non produce duplicati. Nessuna cadenza nel prompt
6. Compone il DM: *Agenda oggi*, *La tua giornata* (massimo cinque azioni **ordinate**, ognuna col motivo per cui è lì, più una riga di conteggio per il resto), *Entro [giorno]*, *Email*, *Fermo su altri*

La sezione "Fermo su altri" esiste perché un task bloccato da una decisione di terzi non deve stare in una sequenza di cose da fare: Alberto non può agirci, e metterlo in lista lo fa sembrare inadempiente su qualcosa che non dipende da lui.

**Tutta la scrittura automatica su Linear è concentrata in ALDO.** Il check serale chiede e basta. Se scrivessero in due sullo stesso registro, un disallineamento diventerebbe impossibile da attribuire.

**Pezzo fragile da sorvegliare nei primi giorni:** finora ALDO ha solo letto. Se la chiusura automatica dal thread si rivela inaffidabile, il fallback è tenere il check serale come promemoria puro e chiudere a mano con `/agenda` una volta a settimana.

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
| `com.albertol.cleanup` (launchd) | ✅ Migrato da crontab il 31/08/2026 | Il crontab (`47 12 28 * *`) non aveva mai prodotto un run dallo spostamento all'orario 12:47 del 28/07. Verificato con `pmset -g log`: il 28/08/2026 il Mac era in "Maintenance Sleep" esattamente tra le 12:43 e le 12:52, dentro la finestra di sparo. Causa reale: cron non ha modo di svegliare il Mac né di recuperare un giro saltato mentre dorme, a differenza di launchd (già usato per PIERO). Crontab rimosso, sostituito da `com.albertol.cleanup.plist` con lo stesso orario (giorno 28, 12:47), script testato in dry-run lo stesso giorno (funziona). Prossimo run reale: 28/09/2026 |

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
- `linear-convenzioni.md` — **convenzioni del registro Linear** (progetti e ID, label, formato titoli, regola sulla due date, chi scrive cosa). Letto da ALDO, dal check serale e dalla skill `/agenda`. Se una convenzione cambia si cambia qui, mai dentro un prompt
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
| Linear deadline reminder (3gg) | trig_01KPMhuagKVioGPGeaEkwf4k | ⏳ Attiva, da spegnere dopo 2 giorni di ALDO v2 verificato |
| Check serale | trig_01J3Go9PV537sbW6qanj9Gvc | Attiva dal 01/09/2026 |
| ALB-17 Weekly Review Reminder | trig_01L2wP4nyxfp1UHhkqGrBmvg | Disattivata 02/08 |
| LinkedIn Post Reminder 24h | trig_01WyDwxbxyNBTmET6Qc3KmtK | Disattivata 02/08 |
