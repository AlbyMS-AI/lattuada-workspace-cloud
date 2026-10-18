# Giornalismo iGaming — Contesto

## Ruolo

Giornalista e divulgatore iGaming per tre testate con identità editoriali distinte.

## Lingua

Solo italiano per tutti i contenuti editoriali.

## Second brain giornalismo

Dal 10/10/2026 il vault Obsidian `../second brain - giornalismo/` raccoglie tutto il pubblicato (Jamma, Bottadiculo, Sitiscommesse e LinkedIn) come wiki: una pagina per pezzo, più temi, atti, istituzioni, mercati e operatori, ciascuno con l'elenco cronologico dei pezzi e la tesi di ognuno. Prima di scegliere un tema, la domanda "cosa abbiamo già scritto su X?" si fa lì (indice in `index.md`), oltre che in `articoli-pubblicati.md`. Ogni pezzo nuovo entra nel wiki quando Alberto ne conferma la pubblicazione. Per sapere se il wiki è indietro: `python3 -I ../automations/wiki-giornalismo-mancanti.py`, che le skill `/jamma`, `/bottadiculo` e `/news-sitiscommesse` lanciano in Fase 0 (dal 10/10/2026). Regole in `../second brain - giornalismo/CLAUDE.md`; il vault non legge mai `02-softswiss/`.

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
- **Dal 16/10/2026** (feedback del caporedattore): tre famiglie di contenuto (grandi marchi, casi e persone, curiosità), contributo dal campo obbligatorio in terza persona, marchi nominabili, logo ufficiale da `bottadiculo/grafiche/brand/` e niente foto generate, recensioni da prova diretta (`bottadiculo/recensioni-bookmaker/_template/prova-sul-campo.md`). Dettaglio in `bottadiculo/guidelines.md`; piano condiviso: `bottadiculo/piano-editoriale-condiviso-2026-q4.md`
- Linee guida: `bottadiculo/guidelines.md`
- Piano newsletter: `bottadiculo/piano-newsletter-linkedin-2026.md`
- Piano post mer/ven: `bottadiculo/piano-post-linkedin-2026.md`
- Workflow: `bottadiculo/workflows/`
- Archivio: `bottadiculo/drafts/` + `archive/`

### Sitiscommesse.com

Focus news e notizie del settore scommesse. Zero opinioni, solo fatti.

- Tono: neutro, informativo, zero commento personale
- Formato: struttura HTML fissa, intro + 6 paragrafi (massimo 7) in blocco unico, niente h2.
  Cosa controlla il caporedattore: `sitiscommesse/checklist-caporedattore.md`
- Lunghezza body: 450-550 parole (esclusi titoli e sottotitoli)
- Link interni: solo a sezioni news, mai a pagine operatori
- Linee guida: `sitiscommesse/guidelines.md`
- Workflow: `sitiscommesse/workflows/`
- IMPORTANTE: topic deve essere approvato dal caporedattore prima di scrivere

## I cicli editoriali

Jamma e Bottadiculo hanno ciascuna due cicli settimanali: la newsletter LinkedIn del lunedì (tema deciso e scritto nel weekend precedente dal 16/10/2026, priorità LinkedIn personale → Jamma → Bottadiculo) e due pezzi mercoledì/venerdì con fonte PIERO, same-day. Le sei uscite sono tracciate come ricorrenza su Linear in `task-list.md` (progetto Giornalismo), lette da ALDO ogni lunedì mattina. Regole complete (gerarchia, banca temi, rubriche fisse, valvola di sicurezza): `contesto/cicli-editoriali.md`.

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

Google valuta chi pubblica, non solo cosa pubblica: ogni articolo firmato da Alberto contribuisce ai segnali E-E-A-T letti anche su LinkedIn. Dettaglio e implicazioni pratiche: `contesto/eeat-autore.md`.
