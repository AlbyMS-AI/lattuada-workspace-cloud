# Workflow Completo — Newsletter Bottadiculo.it, Gambling Insights (lunedì, 7:30)

> **Il piano editoriale ha la precedenza su questo file.**
> `../piano-newsletter-linkedin-2026.md` fissa giorno di uscita, regola di assegnazione dei temi
> rispetto a Jamma, ritmo settimanale, banca temi, calendario slot e numerazione delle edizioni.
> Questo workflow descrive come si scrive una singola edizione, non come si decide cosa scriverci.
> Aggiornato il 17/08/2026: la newsletter era domenicale, ora esce il lunedì insieme a quella di Jamma.

---

## Input necessari prima di iniziare

- Tema / fatto della settimana — **arriva dal lock del giovedì**, non si sceglie qui
- Fonti disponibili
- A chi parla questa edizione? (affiliato / PVR / compliance / operativo di sala)

**Regola di assegnazione (rivista il 17/08/2026).** Gerarchia di priorità: LinkedIn personale di
Alberto, poi Jamma, poi Bottadiculo. Al lock del giovedì si chiede prima se il fatto più forte
regge tre letture (tesi personale di Alberto + decisione da board nominabile + azione da campo
entro trenta giorni): tre sì e il fatto è condiviso con tre angoli distinti, anche un solo no e i
tre canali prendono tre fatti diversi in ordine di priorità. Bottadiculo prende il residuo che
supera i suoi tre filtri — orizzonte trenta giorni, azionabilità, prossimità italiana. Se nessun
residuo passa, si pesca dalla banca, non si prende in prestito il tema di Jamma e non si salta
l'uscita. Regola completa in `../piano-newsletter-linkedin-2026.md`.

---

## FASE 1 — Angolo operativo

Domanda filtro: **cosa significa questo per chi lavora sul campo ogni giorno?**

Non le implicazioni strategiche (quelle sono Jamma). L'implicazione quotidiana, concreta,
quella che un compliance officer o un affiliato sente direttamente nel suo lavoro.

Esempi di rotazione dell'angolo:
- Sentenza → non cosa significa per il CdA, ma per chi apre il punto vendita domani
- Dato di mercato → non la lettura del board, ma cosa cambia per chi ottimizza campagne
- Nomina ADM → non la governance istituzionale, ma chi hai davanti la prossima volta che mandi un'email all'ufficio

**Checkpoint**: struttura prima, testo dopo. Proponi l'angolo e attendi conferma.

---

## FASE 2 — Struttura

Scheletro fisso dal 16/08/2026. Le caselle non cambiano da un'edizione all'altra: il piano
fissa la struttura, il lock del giovedì decide solo cosa ci va dentro. Le due rubriche
contrassegnate non si saltano mai, sono il segnale di riconoscimento del prodotto.

```
H1: [contiene la keyword del tema e la tesi — può essere più tagliente di Jamma]

APERTURA                            80-120 parole
- Due o tre frasi. Fatto + implicazione immediata
- Nessuna premessa, nessun contesto introduttivo
- Contrasto dentro una frase sola come default

IL FATTO                            200-250 parole
- Cosa è successo, dato con fonte primaria
- Chi lo ha detto, quando, dove sta scritto

LA PARTE CHE NESSUNO SOTTOLINEA     250-350 parole
- L'angolo inedito reso esplicito
- È la sezione che giustifica l'edizione: se manca,
  il pezzo è una notizia riscritta e non esce
- Unica sezione che può espandersi per arrivare a 1400

▸ COSA CAMBIA DA DOMANI [FISSA]     250-300 parole
- Tre o quattro punti operativi concreti
- Se non se ne trovano almeno tre, il tema non aveva
  superato davvero il filtro di azionabilità

▸ IL NUMERO DELLA SETTIMANA [FISSA] 100-150 parole
- Una cifra sola, con fonte e contesto
- Non deve venire dal tema dell'edizione: è il dato
  laterale che il lettore non ha visto passare

CHIUSURA                            50-80 parole
- Domanda operativa concreta al lettore
- Non un riassunto, non un invito generico
```

**Intestazioni H2 e SEO:** le due rubriche fisse vanno intitolate con le keyword del tema,
non con il nome della rubrica. "Cosa cambia da domani per chi gestisce [x]", non "Cosa cambia
da domani". Il nome della rubrica è la funzione, non il titolo.

---

## FASE 3 — Scrittura

- Frasi brevi ai punti di svolta
- Paragrafi max 3-4 righe
- Nessuna prima persona
- Nessun aggettivo vuoto, nessuna frase da AI
- Nessun trattino (- o —) nel corpo del testo
- Nessun avverbio in -mente
- Registro: come spiegheresti questa cosa a un collega affiliato al bar dopo una fiera

---

## FASE 4 — Fact-check e umanizzazione

Fact-check:
- [ ] Ogni dato è verificabile e ha una fonte
- [ ] Nomi, date, titoli istituzionali sono corretti
- [ ] Nessuna affermazione inventata o inferita senza base

Umanizzazione:
- [ ] L'apertura entra subito nel vivo, senza premesse
- [ ] Ogni paragrafo ha peso informativo — niente riempitivo
- [ ] La chiusura lascia qualcosa su cui riflettere, non riassume
- [ ] Il tono è punchy — non accademico, non da comunicato
- [ ] L'angolo è operativo, non solo strategico

---

## FASE 5 — Output finale

Al termine della newsletter approvata, produce in sequenza i tre output qui sotto. Sono tutti
obbligatori, nessuno si salta: la newsletter Bottadiculo non è consegnata finché non esistono
anche il companion SEO, il post di supporto e la versione blog.

---

### 5A — SEO (Yoast)

Compilare tutti i campi per Bottadiculo.it (WordPress + Yoast).

**Focus keyphrase**
Stringa di 3-4 termini chiave che combina: brand/nome protagonista + tema + contesto istituzionale.
Usare il termine istituzionale corretto (es. "gioco a distanza", non "gioco online").

**SEO Title** *(max 60 caratteri — appare in Google)*
Formato: `[Soggetto]: [fatto] — [implicazione breve]`
Contenere la focus keyphrase. Diverso dall'H1 della newsletter.

**Slug**
Kebab-case, senza anno se l'articolo è analisi (non solo news datata).
Contenere i 2-3 termini principali della keyphrase.

**Meta description** *(max 154 caratteri)*
Struttura: [fatto in una frase] + [angolo inedito] + [perché leggerlo]
Contenere la focus keyphrase nella prima metà.

**Open Graph — Titolo social**
Può coincidere con l'H1 o essere una variante più editoriale.
Max 60 caratteri consigliati per anteprima LinkedIn.

**Open Graph — Descrizione social** *(max 160 caratteri)*
Chi è colpito + cosa cambia + rimando implicito al contenuto.

**Alt text immagine in evidenza**
[Nome protagonista o tema] + [ruolo/contesto] + [anno]

**Categoria WordPress** / **Tag WordPress**
Categoria: massimo una, descrittiva (es. "Normativa e Compliance")
Tag: 5-8 termini, includere nome protagonista, ufficio/ente, anno, tema operativo

**Keyphrases secondarie (Yoast Premium)**
3 varianti della focus keyphrase con ordine delle parole diverso.

**Checklist Yoast prima di pubblicare**
- [ ] Keyphrase nel SEO title
- [ ] Keyphrase nello slug
- [ ] Keyphrase nella meta description (prima metà)
- [ ] Keyphrase nell'H1
- [ ] Keyphrase nel primo paragrafo
- [ ] Keyphrase in almeno un H2
- [ ] Almeno 1 link in uscita (fonte esterna verificata)
- [ ] Almeno 1 link interno (articolo Bottadiculo correlato)
- [ ] Immagine in evidenza con alt text compilato

---

### 5B — Post LinkedIn di accompagnamento

Il post non deve spoilerare la newsletter. Deve spingere all'apertura.

**Struttura:**
```
INCIPIT: forma attiva, tempo presente, max 15 parole — è tutto

SVILUPPO (3-4 paragrafi brevi):
- Il fatto in 1-2 frasi
- La frase-perno del pezzo (isolata su riga propria)
- L'angolo che non si trova altrove — senza rivelarlo per intero
- La promessa di cosa si trova nella newsletter

CTA finale:
"[Titolo newsletter] è uscita. Leggi la newsletter completa [link]"
```

**Regole:**
- Ritmo misto: frasi discorsive alternate a frasi-perno brevi su riga propria
- 150-200 parole (non oltre: il post è un teaser, non un estratto)
- Nessun hashtag, nessuna emoji
- Nessun trattino nel corpo del testo
- Nessun avverbio in -mente
- Tu singolare

---


### 5C — Versione blog Bottadiculo.it

La newsletter LinkedIn e il pezzo sul blog non possono essere lo stesso testo: Google penalizza
la duplicazione e le due pagine finirebbero per competere sulla stessa query.

- **Apertura inedita**, diversa da quella della newsletter. Nessun paragrafo ripreso alla lettera
- Sviluppo ridotto, 500-600 parole
- **Slug diverso** da quello LinkedIn
- Link incorporato alla newsletter completa su LinkedIn, con segnaposto da sostituire dopo
  la pubblicazione delle 7:30

---

## File di output

Tutti in `../drafts/`, con lo stesso prefisso `[data]-[slug]`.

| File | Nome |
|---|---|
| Newsletter | `[data]-[slug]-newsletter-linkedin.md` |
| SEO companion | `[data]-[slug]-newsletter-linkedin-seo.md` |
| Post di supporto LinkedIn | `[data]-[slug]-post-supporto.md` |
| Versione blog WordPress | `[data]-[slug]-versione-blog.md` |
| Brief grafiche (se serve) | `[data]-[slug]-grafiche.md` |

Dopo la pubblicazione, confermata da Alberto: una riga in `../../articoli-pubblicati.md`,
tabella unica ordinata per data decrescente.
