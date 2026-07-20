# NotebookLM — Grafiche Post-Gara PG01

## Dietro la Quota | Messico vs Sudafrica

---

## COME USARE QUESTO FILE

In NotebookLM carica **sempre** la Fonte 0 (Design System).
Per ogni grafica, aggiungi **solo** la fonte corrispondente (Fonte 1, Fonte 2, ecc.).
Non caricare tutte le fonti insieme o NotebookLM userà tutto il testo.

Workflow:

1. Crea notebook → carica Fonte 0
2. Per G1: aggiungi Fonte 1 → usa Prompt G1 → esporta → rimuovi Fonte 1
3. Per G2: aggiungi Fonte 2 → usa Prompt G2 → esporta → rimuovi Fonte 2
4. Ripeti per ogni grafica

---

## FONTE 0 — Design System (carica sempre)

```text
DESIGN SYSTEM — DIETRO LA QUOTA
Serie grafica unica per tutta la rubrica. Ogni infografica deve sembrare
parte dello stesso sistema visivo — non slide isolate.

== STILE UNICO ==
Data visualization editoriale: essenziale, leggibile, autorevole.
Ispirazione: schermi di analisi finanziaria. Dati al centro, zero decorazioni.
Zero gradienti. Zero ombre. Zero bordi arrotondati. Zero elementi ornamentali.

== FORMATO ==
1920 × 1080 px, 16:9. Sfondo sempre #0D0D0D. Margini 80px su tutti i lati.

== PALETTE BRAND ==
#0D0D0D  → sfondo (unico, invariabile)
#FFFFFF  → testo primario, dati
#F5A623  → accento ambra — UN solo elemento per grafica, il dato principale
#888888  → testo secondario: etichette, categorie, note, didascalie
#333333  → linee divisorie, 1px, mai più spesse
#1A1A1A  → sfondo riga/blocco in evidenza
#4CAF50  → solo su G8: esito positivo
#FF9800  → solo su G8: esito intermedio
#EF5350  → solo su G8: esito negativo/sorpresa

== TIPOGRAFIA ==
Font: Montserrat — unico per tutta la serie, nessuna eccezione.
Pesi ammessi: Bold per dati e titoli, Regular per testo e note.

Gerarchia leggibilità (minimo 16pt per qualsiasi testo):
  Dato dominante   → 72pt  Bold     bianco (o accento se è il focus)
  Titolo interno   → 28pt  Bold     bianco
  Testo corpo      → 22pt  Regular  bianco
  Etichetta        → 18pt  Regular  grigio #888888
  Nota / didascalia→ 16pt  Regular  grigio #888888

Nessun testo sotto i 16pt — garantisce leggibilità anche in video compresso.

== REGOLA ACCENTO ==
#F5A623 va su UN solo elemento per grafica.
È il punto dove l'occhio deve arrivare per primo.
Eccezione unica: G8 Verdetto usa i colori semantici (verde/arancio/rosso).

== STRUTTURA COMUNE ==
Ogni grafica ha:
  1. Etichetta categoria in alto (18pt grigio) + linea divisoria 1px #333333
  2. Elemento dominante al centro (dato, punteggio, formula, lista)
  3. Eventuale nota grigia in basso (didascalia, fonte, data)
Stesso schema visivo = serie riconoscibile a colpo d'occhio.
```

---

## FONTE 1 — G1 Title Card

```text
GRAFICA G1 — Title Card Post-Gara
Layout tipo A (centrato).

Elemento dominante (dato principale, 72pt bianco): MESSICO VS SUDAFRICA
Sopra, etichetta categoria (16pt #888888): POST-GARA
Sotto, testo corpo (22pt #888888): Dietro la Quota · 11 giugno 2026

L'accento #F5A623 non è usato su questa card — è una title card neutra.
Nessun altro elemento.
```

### PROMPT G1

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "POST-GARA" 18pt grigio.
Centro dominante: "MESSICO VS SUDAFRICA" 72pt Bold bianco.
Sotto: "Dietro la Quota · 11 giugno 2026" 16pt grigio.
Molto spazio vuoto, composizione centrata, nessuna decorazione.
```

---

## FONTE 2 — G2 Card Pronostici

```text
GRAFICA G2 — Pronostici Pre-Gara
Layout tipo B (lista).

Etichetta categoria (16pt #888888): I PRONOSTICI DICEVANO
Accento #F5A623 su: le frecce → che precedono ogni voce.

Tre voci in lista verticale:
→ Vittoria Messico
→ Under 2.5 gol
→ Partita inaugurale, rischio contenuto

Le prime due voci sono il consenso principale: 22pt #FFFFFF.
La terza voce è la motivazione secondaria: 22pt #888888.
Spaziatura 32px tra le voci.
```

### PROMPT G2

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "I PRONOSTICI DICEVANO" 18pt grigio. Linea 1px #333333 sotto.
Lista verticale a sinistra, spaziatura generosa, freccia ambra → davanti a ogni voce:
→ Vittoria Messico  22pt bianco
→ Under 2.5 gol  22pt bianco
→ Partita inaugurale, rischio contenuto  22pt grigio
```

---

## FONTE 3 — G3 Tabella Quote

```text
GRAFICA G3 — Tabella Quote Pre-Match
Layout tipo C (tabella).

Etichetta categoria (16pt #888888): QUOTE PRE-MATCH
Accento #F5A623 su: i valori della riga Media (unico dato aggregato).

Tabella 4 colonne × 5 righe:
Intestazione: Bookmaker | 1 | X | 2
Riga 1: Betflag | 1.42 | 4.40 | 8.25
Riga 2: Lottomatica | 1.42 | 4.40 | 8.25
Riga 3: Sisal | 1.40 | 4.50 | 9.00
Riga Media (in evidenza): — | 1.41 | 4.43 | 8.50

La riga Media ha sfondo #1A1A1A e valori in #F5A623 Bold.
Tutte le altre righe: sfondo #0D0D0D, testo #FFFFFF Regular.
Intestazioni colonne: #888888 Regular.
Bordi 1px #333333.
```

### PROMPT G3

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "QUOTE PRE-MATCH" 18pt grigio. Linea 1px #333333 sotto.
Tabella 4 colonne (Bookmaker / 1 / X / 2), bordi 1px grigi, intestazioni 18pt grigio:
  Betflag · 1.42 · 4.40 · 8.25  (22pt bianco)
  Lottomatica · 1.42 · 4.40 · 8.25  (22pt bianco)
  Sisal · 1.40 · 4.50 · 9.00  (22pt bianco)
  Media · 1.41 · 4.43 · 8.50  (22pt ambra, sfondo #1A1A1A)
```

---

## FONTE 4 — G4 Probabilità

```text
GRAFICA G4 — Probabilità Implicita
Layout tipo A adattato (tre colonne simmetriche).

Etichetta categoria (16pt #888888): PROBABILITÀ IMPLICITA · PRE-MATCH
Accento #F5A623 su: il valore del Messico (71%) — il dato più rilevante.

Tre blocchi simmetrici affiancati, divisi da linee verticali 1px #333333:
Blocco 1: "71%"  dato principale 72pt — Messico etichetta 16pt #888888
Blocco 2: "23%"  dato principale 72pt — Pareggio etichetta 16pt #888888
Blocco 3: "12%"  dato principale 72pt — Sudafrica etichetta 16pt #888888

Il 71% del Messico è in #F5A623. Il 23% e il 12% sono in #FFFFFF.
Coerenza con la regola: un solo accento per grafica.
```

### PROMPT G4

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "PROBABILITÀ IMPLICITA · PRE-MATCH" 18pt grigio. Linea 1px #333333 sotto.
Tre blocchi simmetrici divisi da linee verticali 1px grigie.
In ogni blocco: numero 72pt Bold centrato, etichetta squadra 18pt grigio sotto.
  71% ambra → Messico  |  23% bianco → Pareggio  |  12% bianco → Sudafrica
```

---

## FONTE 5 — G5 Precedente 2010

```text
GRAFICA G5 — Precedente Storico
Layout tipo A (centrato).

Etichetta categoria (16pt #888888): PRECEDENTE STORICO
Accento #F5A623 su: il risultato "1 — 1" (il dato sorprendente).

Contenuto centrato verticalmente:
Sopra: "11 GIUGNO 2010" 26pt Bold #FFFFFF
Linea divisore 1px #333333
Centro dominante: "MESSICO  1 — 1  SUDAFRICA" 72pt Bold
  — "MESSICO" e "SUDAFRICA" in #FFFFFF
  — "1 — 1" in #F5A623
Sotto: "Partita inaugurale · Johannesburg" 16pt Regular #888888
```

### PROMPT G5

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "PRECEDENTE STORICO" 18pt grigio. Linea 1px #333333 sotto.
Centrato verticalmente: "11 GIUGNO 2010" 28pt Bold bianco, linea grigia,
risultato dominante "MESSICO  1 — 1  SUDAFRICA" 72pt Bold — il punteggio "1 — 1" in ambra.
Sotto: "Partita inaugurale · Johannesburg" 16pt grigio.
```

---

## FONTE 6 — G6 Confronto PRIMA/DOPO

```text
GRAFICA G6 — Confronto Mercato Prima/Dopo
Layout tipo D (due colonne).

Etichetta categoria (16pt #888888): MERCATO · PRIMA E DOPO

Colonna sinistra — PRIMA (dati storici, tono attenuato):
  Header "PRIMA" 16pt Regular #888888
  Messico   71%  — 26pt Regular #888888
  Pareggio  23%  — 26pt Regular #888888
  Sudafrica 12%  — 26pt Regular #888888

Linea verticale 1px #333333 al centro. Freccia → 48pt Bold #FFFFFF sovrapposta.

Colonna destra — DOPO (dato reale, tono vivace):
  Header "DOPO" 16pt Regular #888888
  Risultato: "2 — 0" 72pt Bold #F5A623
  Sotto: "Messico" 18pt Regular #888888

Il grigio a sinistra e l'ambra a destra comunicano il passaggio dal prima al dopo.
```

### PROMPT G6

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "MERCATO · PRIMA E DOPO" 18pt grigio. Linea 1px #333333 sotto.
Due colonne simmetriche divise da linea verticale 1px grigia, freccia → bianca al centro.
Sinistra — "PRIMA" 18pt grigio, dati 22pt grigio attenuato: Messico 71% · Pareggio 23% · Sudafrica 12%.
Destra — "DOPO" 18pt grigio, "2 — 0" 72pt Bold ambra, "Messico" 18pt grigio sotto.
```

---

## FONTE 7 — G7 Risultato Finale

```text
GRAFICA G7 — Risultato Finale
Layout tipo A (centrato).

Etichetta categoria (16pt #888888): RISULTATO FINALE

Esito: vince il Messico (favorito confermato) → punteggio in #FFFFFF (nessun accento — esito atteso).

Elemento dominante centrato: "MESSICO  2 — 0  SUDAFRICA" 72pt Bold #FFFFFF
Sotto: "11 giugno 2026 · Estadio Azteca" 16pt Regular #888888
```

### PROMPT G7

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "RISULTATO FINALE" 18pt grigio. Linea 1px #333333 sotto.
Centrato: "MESSICO  2 — 0  SUDAFRICA" 72pt Bold tutto bianco (esito atteso, nessun accento).
Sotto: "11 giugno 2026 · Estadio Azteca" 16pt grigio.
```

---

## FONTE 8 — G8 Verdetto

```text
GRAFICA G8 — Verdetto del Mercato
Layout tipo A (centrato).

Etichetta categoria (16pt #888888): VERDETTO

Esito: vince il Messico → Versione A.

Frase dominante: "Il mercato aveva RAGIONE"
Corpo testo in #FFFFFF 72pt Bold.
La parola RAGIONE in #4CAF50 (verde).

Nessun altro elemento.
```

### PROMPT G8

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat Bold.
Etichetta in alto: "VERDETTO" 18pt grigio. Linea 1px #333333 sotto.
Frase unica centrata 72pt: "Il mercato aveva RAGIONE"
Testo bianco, la parola RAGIONE in verde #4CAF50.
```

---

## FONTE 9 — G9 Formula

```text
GRAFICA G9 — Formula
Layout tipo A (centrato).

Etichetta categoria (16pt #888888): COME SI LEGGE UNA QUOTA

Elemento dominante: "100 ÷ quota = probabilità"
Accento #F5A623 su: i simboli matematici ÷ e = (sono la logica della rubrica).
Il resto del testo in #FFFFFF 72pt Bold.

Nessun altro elemento.
```

### PROMPT G9

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat Bold.
Etichetta in alto: "COME SI LEGGE UNA QUOTA" 18pt grigio. Linea 1px #333333 sotto.
Formula centrata 72pt: "100 ÷ quota = probabilità" — testo bianco, simboli ÷ e = in ambra.
Molto spazio vuoto intorno — la formula deve dominare senza nulla attorno.
```

---

## FONTE 10 — G10 Stats Partita (solo post-gara)

```text
GRAFICA G10 — Statistiche Partita
Layout tipo A adattato (due colonne simmetriche).

Etichetta categoria: DENTRO LA PARTITA
Accento #F5A623 su: i valori del Messico (la squadra dominante).

Due blocchi affiancati con etichetta stat sopra e valore sotto:

Blocco 1 — Expected Goals:
  Etichetta: "xG"
  Messico: 1.44 in ambra
  Sudafrica: 0.07 in grigio

Blocco 2 — Tiri in porta:
  Etichetta: "TIRI IN PORTA"
  Messico: 16 in ambra
  Sudafrica: 3 in grigio

I valori del Messico in ambra comunicano il dominio senza bisogno di commenti.
```

### PROMPT G10

```text
Stile Dietro la Quota. Sfondo #0D0D0D. Font Montserrat.
Etichetta in alto: "DENTRO LA PARTITA" 18pt grigio. Linea 1px #333333 sotto.
Due blocchi simmetrici divisi da linea verticale 1px grigia.
Blocco sinistro — "xG": Messico 1.44 ambra 72pt Bold, Sudafrica 0.07 grigio 72pt Bold.
Blocco destro — "TIRI IN PORTA": Messico 16 ambra 72pt Bold, Sudafrica 3 grigio 72pt Bold.
Etichette squadra 18pt grigio sotto ogni valore.
```

---

## RIEPILOGO FONTI E SEQUENZA

| Grafica | Fonte da caricare | Quando |
| --- | --- | --- |
| G1 Title Card | Fonte 0 + Fonte 1 | Adesso |
| G2 Pronostici | Fonte 0 + Fonte 2 | Adesso |
| G3 Tabella Quote | Fonte 0 + Fonte 3 | Adesso |
| G4 Probabilità | Fonte 0 + Fonte 4 | Adesso |
| G5 Precedente 2010 | Fonte 0 + Fonte 5 | Adesso |
| G6 Confronto (sinistra) | Fonte 0 + Fonte 6 | Adesso |
| G9 Formula | Fonte 0 + Fonte 9 | Adesso |
| G7 Risultato | Fonte 0 + Fonte 7 | Dopo partita |
| G6 Confronto (destra) | Fonte 0 + Fonte 6 | Dopo partita |
| G8 Verdetto | Fonte 0 + Fonte 8 | Dopo partita |
| G10 Stats | Fonte 0 + Fonte 10 | Dopo partita |
