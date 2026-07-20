# Workflow Completo — Newsletter Bottadiculo.it
# Gambling Insights (domenicale)

---

## Input necessari prima di iniziare

- Tema / fatto della settimana
- Fonti disponibili
- A chi parla questa edizione? (affiliato / PVR / compliance / operativo di sala)

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

```
H1: [diretto, contiene la tesi — può essere più tagliente di Jamma]

APERTURA (2-3 paragrafi corti):
- Fatto + implicazione immediata in 2-4 frasi brevi
- La tesi: cosa sta succedendo che nessuno dice chiaramente

SVILUPPO (4-6 sezioni H2):
- Intestazioni come affermazioni operative, non domande
- Ogni sezione: fatto → angolo inedito → implicazione per il lettore
- Dati specifici con fonte
- Paragrafi max 3-4 righe

CHIUSURA:
- Domanda operativa concreta al lettore
- Non un riassunto
```

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

Al termine della newsletter approvata, produce in sequenza i quattro output qui sotto.

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


## File di output

| File | Percorso |
|---|---|
| Newsletter | `archive/bottadiculo/newsletter/[data]-[slug].md` |
| SEO | `drafts/[data]-[slug]-seo.md` |
| Post LinkedIn | `../../04-linkedin/contenuti/bottadiculo/[data]_[slug].md` |
| Brief grafiche | `drafts/[data]-[slug]-grafiche.md` |
