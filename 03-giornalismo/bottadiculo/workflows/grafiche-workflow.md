# Workflow Grafiche — Newsletter Bottadiculo.it
# 1 main image + 2 infografiche interne

**Palette (corretta il 05/09/2026):** quella reale di Bottadiculo.it, estratta dal sito live
il 13/07/2026 e documentata in `../../04-linkedin/palette-brand.md` — non la palette navy
personale di Alberto. Sfondo indigo `#1C0F3A`, accento unico arancio `#F9511F`, secondario
viola `#6330C7`, testo bianco `#FFFFFF`. Le query sotto sono state aggiornate di conseguenza;
prima erano rimaste sulla palette blu (`#0D1B2A`/`#1B4F8A`) usata per errore nel primo
tentativo del 13/07.

---

## 3 output per ogni edizione

| Output | Formato | Strumento | Chi lo fa |
|---|---|---|---|
| Main image | 1200×630px (16:9) | Canva | Claude |
| Infografica 1 | 1080×1350px (4:5) | Canva | Claude |
| Infografica 2 | 1080×1350px (4:5) | NotebookLM | Utente |

**Logica di assegnazione strumento:**
- Canva (Claude): grafiche tipografiche, visive, minimal testo — quote card, hook card, stat card
- NotebookLM (utente): grafiche strutturate con testo abbondante — checklist, profile card, before/after

---

## MAIN IMAGE — Canva via Claude

### Quando usarla
Sempre la stessa logica: hook tipografico — le 2-3 frasi più forti dell'apertura della newsletter.
La main image deve funzionare senza contesto: chi la vede nel feed capisce il punto anche senza aver letto nulla.

### Formato query Canva

```
Design type: infographic
Formato: 1200x630px

Query:
Crea una grafica tipografica editoriale per newsletter iGaming italiana.
Sfondo pieno #1C0F3A (indigo scuro).
Testo principale #FFFFFF (bianco).
Accento #F9511F (arancio, accento unico) per evidenziare una parola o elemento.

Testo da mostrare (nessun testo aggiunto oltre a questo):
[FRASE 1 — max 6 parole]
[FRASE 2 — max 6 parole]
[FRASE 3 — max 6 parole, opzionale]
Label in basso a destra, piccolo: "Bottadiculo.it"

Layout: tipografico, frasi impilate verticalmente al centro.
Nessuna illustrazione, nessuna icona, nessuna foto.
Solo tipografia bold su sfondo scuro.
Font sans-serif moderno, peso black o extrabold per le frasi principali.
```

### Fallback se Canva non produce risultati soddisfacenti
Usare Gemini con la stessa query + specificare "flat design, no illustrations, typography only".

---

## INFOGRAFICA 1 — Canva via Claude

### Quando usarla
Per il momento visivo più sintetico della newsletter: una frase-perno isolata oppure un dato chiave.
Tipicamente la sezione con la frase più condivisibile.

### Formato query Canva

```
Design type: infographic
Formato: 1080x1350px (4:5)

Query:
Crea un'infografica editoriale per LinkedIn, stile iGaming professionale italiano.
Sfondo #1C0F3A, testo #FFFFFF, accento #F9511F, secondario #6330C7.
Nessuna illustrazione. Solo tipografia e blocchi colore.

Tipo: [quote card / stat card — scegli uno]

SE quote card:
Frase grande al centro tra virgolette tipografiche:
"[FRASE CHIAVE — max 12 parole]"
Sotto, piccolo: "Gambling Insights #[N] | Bottadiculo.it"

SE stat card:
Numero grande al centro: [NUMERO + UNITÀ]
Una riga sopra, piccola: [CONTESTO DEL DATO — max 5 parole]
Una riga sotto, piccola: [FONTE — max 5 parole]
```

---

## INFOGRAFICA 2 — NotebookLM (utente)

### Quando usarla
Per la sezione più strutturata della newsletter: checklist, profilo in punti, before/after.
NotebookLM gestisce meglio i layout con testo multiplo e gerarchie visive.

### Fonte da caricare in NotebookLM

| Tipo infografica | Cosa caricare |
|---|---|
| Quote card | Il paragrafo singolo con la frase |
| Checklist | La sezione H2 completa (titolo + elenco) |
| Profile card | La sezione H2 completa (titolo + punti del profilo) |
| Before/After | Due sezioni H2 consecutive |
| Stat card | Il paragrafo con il dato + una frase di contesto |

Lunghezza ideale fonte: 80-200 parole. Oltre, NotebookLM perde il focus.

---

### Brief NotebookLM — template da compilare

```
Level of detail: [Concise / Normal / Detailed]

Concise  → parole chiave sole, max 3-4 elementi. Per quote card e stat card.
Normal   → 1 frase corta per elemento, max 5 elementi. Default.
Detailed → 2 frasi per elemento, max 4 elementi. Per before/after e checklist con contesto.

---

Describe the infographic:

Tipo: [checklist / before-after / profile card]

Titolo: [max 6 parole — deve stare su una riga]

Contenuto:
[Scrivi esattamente il testo che deve comparire — non descrivere, trascrivi.
Max 5 elementi. 1 elemento = 1 riga. Niente frasi lunghe.]

Cosa NON includere:
[Elenca 2-3 elementi da escludere esplicitamente, altrimenti NotebookLM li aggiunge]

Layout: [verticale a lista / due colonne / centrato]

Palette:
Sfondo: #1C0F3A — Testo: #FFFFFF — Accento: #F9511F — Secondario: #6330C7

Formato: 4:5 (1080x1350px)

Note visive: nessuna icona generica, nessuna illustrazione, solo tipografia e blocchi colore
```

---

### Esempio compilato — tipo checklist

```
Level of detail: Normal

Tipo: checklist

Titolo: Cosa fare adesso — 3 azioni

Contenuto:
1. Allinea la rendicontazione trimestrale agli orientamenti recenti
2. Aggiorna i contatti interni dell'ufficio ADM
3. Manda un follow-up sui dossier aperti da mesi
Nota in fondo: "Chi è presente con dossier in ordine costruisce credibilità."

Cosa NON includere:
Nessuna spiegazione aggiuntiva per ogni punto, nessuna icona decorativa, nessun logo ADM

Layout: verticale a lista, checkbox o numeri come marker
Palette: sfondo #1C0F3A, testo #FFFFFF, accento checklist #F9511F
Formato: 4:5
```

### Esempio compilato — tipo before/after

```
Level of detail: Normal

Tipo: before-after (due colonne)

Titolo: Prima e dopo

Contenuto:
COLONNA SINISTRA — "Governance incerta"
- Pratiche rallentate
- Follow-up senza risposta
- Scadenze slittate

COLONNA DESTRA — "Governance confermata"
- Interlocutore tecnico stabile
- Finestra operativa aperta
- Chi si muove adesso costruisce credibilità

Cosa NON includere:
Nessuna freccia animata, nessuna icona, nessun logo, nessuna data

Layout: due colonne simmetriche, separatore verticale in #6330C7
Palette: sfondo #1C0F3A, colonna sinistra accento #F9511F, testo #FFFFFF
Formato: 4:5
```

---

## Processo Canva passo per passo (quando Claude genera)

1. Claude lancia `generate-design` con la query compilata
2. Canva restituisce 3-4 design candidate
3. Utente sceglie il candidate preferito
4. Claude lancia `create-design-from-candidate` con l'ID scelto
5. Claude lancia `export-design` → PNG
6. URL di download condiviso con l'utente

Nota: i design Canva sono editabili dopo la generazione. Se colori o testo non sono esatti, si corregge nell'editor prima dell'export.

---

## Export e salvataggio

| File | Nome | Dove |
|---|---|---|
| Main image | `[data]-cover.png` | `bottadiculo/grafiche/[data]-[slug]/` |
| Infografica 1 (Canva) | `[data]-infografica-1.png` | `bottadiculo/grafiche/[data]-[slug]/` |
| Infografica 2 (NotebookLM) | `[data]-infografica-2.png` | `bottadiculo/grafiche/[data]-[slug]/` |
| Brief grafiche | `[data]-[slug]-grafiche.md` | `bottadiculo/drafts/` |

---

## Checklist finale prima di usare le grafiche

- [ ] Main image leggibile a 300px di larghezza (anteprima mobile WordPress)
- [ ] Infografiche leggibili a 540px (feed LinkedIn mobile)
- [ ] Nessun testo troncato o tagliato dai bordi
- [ ] Palette coerente tra i 3 output (stesso sfondo, stessi accenti)
- [ ] Alt text pronto per tutte e tre le grafiche (vedere SEO output)
