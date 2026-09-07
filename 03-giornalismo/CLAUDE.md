# Giornalismo iGaming — Contesto

## Ruolo

Giornalista e divulgatore iGaming per tre testate con identità editoriali distinte.

## Lingua

Solo italiano per tutti i contenuti editoriali.

## Testate

### Jamma.it

Testata B2B di riferimento per l'industria iGaming italiana. Lettore: operatori,
fornitori, regolatori, professionisti del settore.

- Tono: analitico, informativo, tecnico ma leggibile
- Formato principale: articoli di approfondimento, interviste, news settoriali
- Newsletter LinkedIn "Gioco & Business": 1000-1400 parole, esce il **lunedì alle 7:30**
- **Due articoli di approfondimento a settimana, mercoledì e venerdì** (dal 07/09/2026): stessa
  lunghezza e stesso registro, senza le due rubriche fisse della newsletter, nessuna grafica,
  ottimizzati SEO. Piano dedicato: `jamma/piano-approfondimenti-2026.md`
- Linee guida: `jamma/guidelines.md`
- Piano newsletter: `jamma/piano-newsletter-linkedin-2026.md`
- Piano approfondimenti mer/ven: `jamma/piano-approfondimenti-2026.md`
- Workflow: `jamma/workflows/`
- Archivio: `archive/` + `jamma/drafts/`

### Bottadiculo.it

Voce edgy e diretta del settore. Più personale, più opinione, meno istituzionale.
Lato del campo, non lato C-level. Lettore: operatori, affiliati, addetti ai lavori.

- Tono: diretto, senza filtri, operativo
- Formato principale: post 150-300 parole (mer/ven), newsletter 1000-1400 parole
- Newsletter LinkedIn "Gambling Insights" (numerata): esce il **lunedì alle 7:30**. Ogni edizione
  produce sempre quattro file — newsletter, companion SEO, post di supporto, versione blog
- **Due post LinkedIn a settimana, mercoledì e venerdì** (dal 07/09/2026): cadenza fissa, non più
  occasionale, sempre con grafica (template fisso, vedi sotto). Piano dedicato:
  `bottadiculo/piano-post-linkedin-2026.md`
- Linee guida: `bottadiculo/guidelines.md`
- Piano newsletter: `bottadiculo/piano-newsletter-linkedin-2026.md`
- Piano post mer/ven: `bottadiculo/piano-post-linkedin-2026.md`
- Workflow: `bottadiculo/workflows/`
- Archivio: `bottadiculo/drafts/` + `archive/`

### Sitiscommesse.com

Focus news e notizie del settore scommesse. Zero opinioni, solo fatti.

- Tono: neutro, informativo, zero commento personale
- Formato: struttura HTML fissa — intro + 6 paragrafi in due blocchi h2
- Lunghezza body: 450-550 parole (esclusi titoli e sottotitoli)
- Link interni: solo a sezioni news, mai a pagine operatori
- Linee guida: `sitiscommesse/guidelines.md`
- Workflow: `sitiscommesse/workflows/`
- IMPORTANTE: topic deve essere approvato dal caporedattore prima di scrivere

## Le due newsletter del lunedì

Jamma e Bottadiculo pubblicano la propria newsletter LinkedIn lo stesso giorno, il lunedì alle 7:30.
I due piani (`jamma/piano-newsletter-linkedin-2026.md` e `bottadiculo/piano-newsletter-linkedin-2026.md`)
si leggono in coppia e hanno la precedenza sui workflow, che descrivono come si scrive una singola
edizione ma non come si decide cosa scriverci.

Le regole che valgono per entrambe:

- **Gerarchia di priorità (17/08/2026): LinkedIn personale di Alberto, poi Jamma, poi Bottadiculo.**
  È priorità di scelta del tema, non di pubblicazione. Sostituisce la regola del 16/08 in cui
  Bottadiculo sceglieva per primo
- **Regola mista sul fatto della settimana.** Al lock del giovedì si chiede se il fatto più forte
  regge tre letture: serve una tesi personale di Alberto, una decisione da board nominabile, e
  un'azione da campo entro trenta giorni. Tre sì → fatto condiviso, tre angoli distinti sui tre
  canali. Anche un solo no → tre fatti separati, assegnati in ordine di priorità
- **Tocco personale su ogni angolo.** Su LinkedIn personale con la prima persona; su Jamma e
  Bottadiculo, dove la prima persona resta vietata, attraverso il POV raccolto con domande mirate
  **al lock del giovedì**, non in fase di scrittura
- **Lock giovedì, scrittura venerdì, rifinitura domenica.** Il lunedì è solo giorno di pubblicazione
- **Banca temi** (`*/banca-temi.md`): se la settimana non produce un fatto abbastanza forte si pesca
  da lì, non si salta l'uscita. Tre schede per Jamma, **quattro per Bottadiculo**, che pescando per
  ultimo dal bacino più stretto è il canale che si scopre per primo
- **Rubriche fisse** che non si saltano mai: "Cosa cambia da domani" e "Il numero della settimana"
  su Bottadiculo, "Il precedente internazionale" e "Cosa deve decidere chi guida" su Jamma

## I due cicli del mercoledì/venerdì

Dal 07/09/2026, oltre alle newsletter del lunedì, Jamma e Bottadiculo hanno ciascuna un secondo
ciclo settimanale: due articoli Jamma e due post LinkedIn Bottadiculo, mercoledì e venerdì. Piani
gemelli: `jamma/piano-approfondimenti-2026.md` e `bottadiculo/piano-post-linkedin-2026.md`.

Differenze principali rispetto alle newsletter del lunedì:

- **Fonte dei temi:** PIERO (rassegna quotidiana) come fonte primaria, non il lock del giovedì.
  Produzione same-day: rassegna del mattino, scelta angolo, scrittura, fact-check, umanizzazione
  in un'unica sessione. Le banche temi (`jamma/banca-temi.md`, `bottadiculo/banca-temi.md`, target
  alzato il 07/09) restano riserva per quando la rassegna non produce nulla di utilizzabile
- **Non sovrapposizione:** prima di ogni pezzo, controllo di `articoli-pubblicati.md` sugli ultimi
  7 giorni, tutte le testate. Per Jamma vale anche il controllo sulle news scritte dalla redazione
  di Jamma.it: questo ciclo approfondisce o porta temi nuovi, non ripete la notizia
- **Nessuna rubrica fissa**, quelle restano un tratto distintivo solo della newsletter
- **Jamma:** nessuna grafica, layer SEO nel workflow articolo
- **Bottadiculo:** grafica sempre, template fisso per post singolo (diverso da quello della
  newsletter — vedi `04-linkedin/grafiche/src/templates/`)
- **Valvola di sicurezza:** se la settimana è troppo piena, salta prima il pezzo di venerdì, la
  newsletter del lunedì non salta mai

Le sei uscite settimanali (2 newsletter + 4 pezzi mer/ven) sono tracciate come ricorrenza su
Linear in `task-list.md` (progetto Giornalismo), lette da ALDO ogni lunedì mattina.

## Flusso di lavoro (per tutti i format)

```text
1. RICERCA   — fonti primarie (comunicati, normative, dati), secondarie (analisi, altri media)
2. SVILUPPO  — scrittura basata sulla ricerca, struttura del contenuto
3. FACT-CHECK — verifica ogni dato, nome, data, cifra
4. UMANIZZAZIONE — revisione tono, rimozione strutture AI, voce personale
```

La fase di umanizzazione segue sempre la checklist anti-AI completa:
`../01-tono-di-voce/anti-ai-checklist.md` (punteggiatura, aperture da formula, pattern
"Non è X. È Y.", lessico da evitare, ritmo delle frasi, autocontrollo finale). Vale per
tutte e tre le testate; per Sitiscommesse non si applica il punto 7 (presa di posizione),
per il resto sì.

## Principi editoriali trasversali

- Il lettore è un addetto ai lavori: non spiegare l'ovvio
- I numeri rendono un articolo credibile: cercali sempre
- Il punto di vista personale è un valore, non un rischio (eccetto Sitiscommesse)
- Titoli: H1 e H2 devono contenere le keyword del topic (SEO), non solo tesi editoriali
- Apertura: entra subito nel vivo, nessuna premessa
- No trattini (- o —) nel corpo del testo
- No avverbi in -mente

## Struttura cartelle

```text
03-giornalismo/
├── jamma/              ← guidelines, piano newsletter, piano approfondimenti mer/ven, workflows, templates, drafts
├── bottadiculo/        ← guidelines, piano newsletter, piano post mer/ven, workflows, templates, drafts, mondiali2026
├── sitiscommesse/      ← guidelines, workflows, templates
├── news-igaming 2026/  ← rassegna stampa e fonti giornaliere
├── articoli-pubblicati.md ← indice cronologico di tutti gli articoli usciti
├── task-list.md        ← piano ricorrenze per ALDO (le sei uscite settimanali su Linear)
├── archive/            ← materiale di riferimento per stile
└── fatture/            ← gestione amministrativa
```

## Connessione con LinkedIn

Gli articoli pubblicati su Jamma e Bottadiculo sono la fonte primaria per i contenuti
LinkedIn. Il flusso è: articolo pubblicato → post LinkedIn / carosello.
Materiali già adattati: `../04-linkedin/contenuti/`

## E-E-A-T: l'autore come segnale SEO

Google valuta chi pubblica, non solo cosa pubblica. Ogni articolo firmato da Alberto su Jamma
e Bottadiculo contribuisce ai segnali E-E-A-T (Experience, Expertise, Authoritativeness,
Trustworthiness) che Google legge per valutare l'autorevolezza dell'autore.

LinkedIn ha altissima domain authority ed è costantemente indicizzato da Google: il profilo
LinkedIn di Alberto, quando riprende le pubblicazioni su Jamma e Bottadiculo, crea un segnale
incrociato che rafforza l'autorevolezza su entrambi i canali.

Implicazioni pratiche per i contenuti:

- Byline coerente su tutti i canali (stesso nome, stessa bio sintetica)
- Dati concreti e fonti primarie nel testo (segnale di Expertise)
- Titoli H1/H2 con keyword del topic — già regola in uso, rinforza anche la SEO dell'autore
- Ogni articolo Jamma/Bottadiculo va ripreso su LinkedIn con link alla fonte originale
