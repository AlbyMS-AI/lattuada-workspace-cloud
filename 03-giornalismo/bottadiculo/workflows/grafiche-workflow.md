# Workflow Grafiche — Newsletter Bottadiculo.it
# 1 main image + 2 infografiche interne

**Palette (corretta il 05/09/2026):** quella reale di Bottadiculo.it, estratta dal sito live
il 13/07/2026 e documentata in `../../04-linkedin/palette-brand.md` — non la palette navy
personale di Alberto. Sfondo indigo `#1C0F3A`, accento unico arancio `#F9511F`, secondario
viola `#6330C7`, testo bianco `#FFFFFF`.

**Main image standardizzata il 06/09/2026** (vedi sezione dedicata sotto): niente più
Canva/Gemini per-edizione. Motivo: un'illustrazione diversa ogni settimana non comunica il
tema specifico senza testo (provato con l'edizione #80, Lottomatica-CIRSA) e aggiunge un
giro manuale (Gemini → inbox → composizione) a ogni uscita. Un formato fisso rende Gambling
Insights riconoscibile a colpo d'occhio nel feed, sullo stesso modello di "The Betting Edge"
(newsletter personale di Alberto): cambia solo il testo, l'identità visiva resta.

---

## 3 output per ogni edizione

| Output | Formato | Strumento | Chi lo fa |
|---|---|---|---|
| Main image | 1280×720px (16:9) | Template HTML fisso | Claude |
| Infografica 1 | 1080×1350px (4:5) | NotebookLM | Utente |
| Infografica 2 | 1080×1350px (4:5) | NotebookLM | Utente |

**Logica di assegnazione strumento:**
- Template HTML (Claude): main image, sempre lo stesso layout, solo il testo cambia — vedi sotto
- NotebookLM (utente): grafiche strutturate con testo — checklist, profile card, before/after, stat card

---

## MAIN IMAGE — template fisso (Claude, no tool esterni)

### Come si usa
Sorgente: `../../../04-linkedin/grafiche/src/templates/gambling-insights-cover-template.html`.
Per ogni edizione: copiarlo in `../../../04-linkedin/grafiche/src/[data]-[slug]-cover.html`,
compilare solo tre campi nella sezione `.box` (kicker `#N · data`, h1, sub — una frase che
riprende l'angolo, non riassume la newsletter), poi:

```
cd 04-linkedin/grafiche
./render.sh png src/[data]-[slug]-cover.html [data]-[slug]-cover.png 1280x720
```

Il pannello sinistro (identità fissa: tassello arancio spezzato su sfondo indigo, wordmark
"Bottadiculo.it") non si tocca mai — è lui a rendere riconoscibile l'edizione nel feed, non
un'illustrazione nuova ogni volta. Palette e struttura: vedi commento in testa al file
template.

### Perché non più Canva/Gemini per-edizione
Archiviato il 06/09/2026 dopo il tentativo sull'edizione #80: il formato 1200×630 dell'iterazione
precedente non era quello corretto per la newsletter LinkedIn (serve 16:9 in 1280×720, non
630px di altezza), e un'illustrazione Gemini su misura per il fatto della settimana rischiava
di non comunicare il tema senza leggere il testo. Il template fisso risolve entrambi i problemi.

---

## INFOGRAFICHE 1 e 2 — NotebookLM (utente)

### Quando usarle
Infografica 1: il momento visivo più sintetico della newsletter — una frase-perno isolata
(quote card) oppure un dato chiave (stat card), tipicamente la sezione più condivisibile.
Infografica 2: la sezione più strutturata — checklist, profilo in punti, before/after.
NotebookLM gestisce entrambi i casi, testo minimo o abbondante che sia.

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

## Export e salvataggio

| File | Nome | Dove |
|---|---|---|
| Main image (template HTML, Claude) | `[data]-[slug]-cover.png` | `04-linkedin/grafiche/` |
| Infografica 1 (NotebookLM, utente) | `[data]-infografica-1.png` | `04-linkedin/grafiche/inbox/` poi spostata |
| Infografica 2 (NotebookLM, utente) | `[data]-infografica-2.png` | `04-linkedin/grafiche/inbox/` poi spostata |
| Brief grafiche | `[data]-[slug]-grafiche.md` | `bottadiculo/drafts/` |

---

## Checklist finale prima di usare le grafiche

- [ ] Main image leggibile a 300px di larghezza (anteprima mobile WordPress)
- [ ] Infografiche leggibili a 540px (feed LinkedIn mobile)
- [ ] Nessun testo troncato o tagliato dai bordi
- [ ] Palette coerente tra i 3 output (stesso sfondo, stessi accenti)
- [ ] Alt text pronto per tutte e tre le grafiche (vedere SEO output)
