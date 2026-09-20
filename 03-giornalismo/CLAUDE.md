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
  ultimo dal bacino più stretto è il canale che si scopre per primo. Entrambe le banche hanno una
  sezione "Territori di competenza e cluster" (aggiunta 12/09/2026, metodo Copelli): dice non solo
  quante schede sono pronte ma se coprono aree diverse — il target numerico da solo può nascondere
  schede tutte concentrate sullo stesso cluster
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
  newsletter — vedi `bottadiculo/grafiche/src/templates/`)
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

**Le 5W in fase di RICERCA.** Prima di passare a SVILUPPO, ogni pezzo (eccetto le rubriche
derivate da un articolo già pubblicato) deve poter rispondere a: chi, cosa, quando, dove,
perché. Non è un formalismo da news breve: è il modo in cui un fatto raccontato a metà
("è successo", senza dire a chi, con quali tempi, in quale sede) produce un pezzo debole
anche quando l'angolo è giusto. Per Jamma e Bottadiculo le 5W sono il punto di partenza
della ricerca, non il testo finale: il "perché" è spesso proprio la domanda sotto la
domanda che genera l'angolo (Step 1 dei rispettivi workflow).

**Interviste e dichiarazioni di terzi.** Alberto non fa sempre l'intervista diretta. Si può
riprendere il contenuto di un'intervista o dichiarazione già pubblicata da altri (altri
giornalisti, altre testate) per sostenere la tesi del pezzo, con due condizioni sempre
valide:

- mai in citazione diretta virgolettata
- sempre in discorso indiretto, riformulato con parole proprie, mai la fonte/testata di
  provenienza nominata nel testo

Questo vale per Jamma e Bottadiculo. **Non vale per Sitiscommesse**, dove le citazioni
dirette sono vietate sempre, indipendentemente dalla fonte (vedi guidelines e workflow
di dominio) — il formato è solo fatti, non c'è tesi da sostenere con la voce di qualcun altro.
Resta invece invariata la regola sulla citazione diretta di documenti scritti (norme,
sentenze, comunicati): quella va sempre ancorata alla fonte, perché è verificabile da
chiunque e non espone nessuno. La regola nuova riguarda solo le persone, non i testi.

**Prima di iniziare la RICERCA:** verificare che il contesto sia esplicito, non assunto — cosa ha già scritto la testata su questo tema (guidelines, articoli precedenti), quali affermazioni sono sostenibili su fonte e quali no, cosa distingue l'angolo da uno già visto altrove. Se manca, si chiede o si cerca, non si inventa. Principio di metodo: `../00-contesto/09-metodo.md`, principio 6 ("Il contesto si costruisce prima").

La fase di umanizzazione segue sempre la checklist anti-AI completa:
`../01-tono-di-voce/anti-ai-checklist.md` (punteggiatura, aperture da formula, pattern
"Non è X. È Y.", lessico da evitare, ritmo delle frasi, autocontrollo finale). Vale per
tutte e tre le testate; per Sitiscommesse non si applica il punto 7 (presa di posizione),
per il resto sì.

## Principi editoriali trasversali

- Il lettore è un addetto ai lavori: non spiegare l'ovvio
- I numeri rendono un articolo credibile: cercali sempre
- Il punto di vista personale è un valore, non un rischio (eccetto Sitiscommesse)
- **Punto di vista privilegiato, diverso per testata.** Il vantaggio di Alberto rispetto a
  chi scrive di iGaming senza il suo osservatorio non è lo stesso su Jamma e su Bottadiculo:
  - **Jamma**: l'osservatorio B2B del lavoro quotidiano in Softswiss (dinamiche aggregator/
    provider, meccanismi di deal, pattern di mercato osservati da dentro). Si applica la
    stessa disciplina di rielaborazione già in vigore per LinkedIn
    (`../04-linkedin/CLAUDE.md`, sezione "Fonti di contenuto" — fonte interna sì, dato
    interno no): mai nomi, cifre o dettagli identificabili di deal/clienti/prospect, solo
    il meccanismo o il pattern, mai competitive intelligence interna presentata come tale.
  - **Bottadiculo**: la prossimità operativa al campo (rete PVR/sottocasse, esperienza
    omnichannel terrestre/online di LasVegas) che un giornalista solo desk non ha. Qui non
    c'è un vincolo di confidenzialità aziendale equivalente a quello Softswiss, ma la stessa
    logica di fondo: raccontare cosa cambia per chi lavora sul campo con la credibilità di
    chi quel campo lo conosce, non con l'osservazione generica di chi lo racconta da fuori.

  Questo criterio non sostituisce il gate sul punto di vista personale già in uso
  (`AskUserQuestion` prima di scrivere, vedi `jamma/SKILL.md` e `bottadiculo/SKILL.md`):
  quel gate estrae il giudizio di Alberto su un fatto specifico, questo criterio riguarda
  da dove viene il suo vantaggio informativo. Non è un requisito meccanico su ogni singolo
  pezzo (la distinzione tra le due testate si affina pezzo per pezzo, non è una formula
  fissa): è un criterio da tenere presente in fase di ricerca e di scelta dell'angolo,
  soprattutto quando un tema rischia di restare una sintesi che chiunque potrebbe scrivere.
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
