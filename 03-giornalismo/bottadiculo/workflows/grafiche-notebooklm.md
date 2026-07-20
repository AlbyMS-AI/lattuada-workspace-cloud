# Workflow — Grafiche Newsletter con NotebookLM
# Bottadiculo.it — Gambling Insights

---

## Obiettivo

Trasformare ogni newsletter in 4-6 slide/grafiche da usare come:
- Carosello LinkedIn (PDF) → accompagnamento al post della newsletter
- Immagine in evidenza per WordPress
- Grafiche standalone per post mid-week

---

## Quando eseguire

Dopo che la newsletter è in stato "approvata / pronta per pubblicazione".
Non prima: le grafiche devono rispecchiare la versione finale, non la bozza.

---

## Step 1 — Identifica i momenti visivi

Ogni newsletter contiene 4 tipi di momenti che si prestano a grafica.
Individua quali sono presenti in questa edizione:

| Tipo | Quando usarlo | Esempio |
|---|---|---|
| **Quote card** | C'è una frase-perno breve e netta | "Non si farà raccontare il settore." |
| **Checklist** | C'è un elenco di azioni o punti concreti | "3 azioni in 30 giorni" |
| **Profile card** | C'è un protagonista con caratteristiche chiave | Chi è Giuliani in 3 punti |
| **Before/After** | C'è un contrasto temporale o situazionale | Prima del vuoto governance / adesso |
| **Stat card** | C'è un numero o dato chiave | +34,6% fisico maggio 2026 |
| **Hook slide** | Sempre — è la prima slide del carosello | Frase di apertura della newsletter |

Scegli massimo 5 momenti. Uno di più è rumore.

---

## Step 2 — Prepara il brief per NotebookLM

### Cosa caricare come fonte

Il testo della newsletter in versione finale (markdown o testo pulito).
Rimuovi metadata, frontmatter e note interne prima di caricare.

### Brief da fornire a NotebookLM

```
Genera una presentazione di [N] slide per LinkedIn basata su questo testo.

Formato: slide LinkedIn (formato 1:1 o 4:5)
Palette colori:
- Sfondo dominante: #0D1B2A
- Testo principale: #F0F8FF
- Accento editoriale: #1B4F8A (contenuto giornalistico/normativa)
- Accento BDM: #00CC66 (solo se contenuto Softswiss-adjacent)
- Secondario chiaro: #7DC8E0

Struttura richiesta:
- Slide 1: [hook — frase di apertura della newsletter]
- Slide 2: [momento visivo identificato in Step 1]
- Slide 3: [momento visivo identificato in Step 1]
- Slide 4: [momento visivo identificato in Step 1]
- Slide finale: CTA — "Leggi la newsletter completa su Bottadiculo.it"

Stile testo:
- Nessun hashtag
- Nessuna emoji
- Frasi brevi: max 2 righe per slide
- Quote card: testo grande, una frase sola
- Checklist: bullet chiari, icona semplice (non decorativa)
- No aggettivi vuoti

Tono: diretto, operativo, settore iGaming italiano
```

---

## Step 3 — Slide per tipo di newsletter

### Newsletter normativa / governance (es. ADM, nuove regole)
Slide obbligatorie:
1. Hook (frase apertura)
2. Chi è il protagonista / cosa è successo (profile card o event card)
3. Cosa cambia operativamente (before/after o bullet)
4. Cosa fare adesso (checklist)
5. CTA

### Newsletter dati / mercato (es. GGR mensile, quote mercato)
Slide obbligatorie:
1. Hook con il numero chiave (stat card grande)
2. Il dato in contesto (prima/dopo, confronto)
3. L'angolo che nessuno sottolinea (quote card)
4. Implicazione operativa per il lettore (bullet)
5. CTA

### Newsletter sentenza / norma (es. TAR, CdS, decreti)
Slide obbligatorie:
1. Hook (il fatto in una frase)
2. Cosa dice esattamente (sintesi dispositivo)
3. Chi è colpito e come (before/after o profilo colpiti)
4. Cosa fare adesso (checklist)
5. CTA

---

## Step 4 — Revisione prima di pubblicare

Prima di usare le slide come carosello LinkedIn o grafica:

- [ ] La palette è coerente con il tipo di contenuto (blu per editoriale, verde per BDM)
- [ ] Nessun hashtag nelle slide
- [ ] La slide finale ha CTA chiara con URL o rimando alla newsletter
- [ ] Il testo di ogni slide è leggibile senza zoom su mobile (test: 30% zoom su schermo)
- [ ] La hook slide funziona da sola come immagine in evidenza WordPress

---

## Step 5 — Output e dove salvare

| Output | Formato | Dove salvare |
|---|---|---|
| File sorgente (brief + slide text) | .md | `bottadiculo/drafts/[data]-[slug]-grafiche.md` |
| Slide esportate | .pdf o .png | `bottadiculo/grafiche/[data]-[slug]/` |
| Immagine in evidenza WordPress | .jpg o .png (1200x630) | `bottadiculo/grafiche/[data]-[slug]/cover.jpg` |

---

## Mapping newsletter → tipo grafica (riferimento rapido)

| Newsletter | Tipo | Slide prioritarie |
|---|---|---|
| Nomine / governance ADM | Normativa | Hook + Profile + Before/After + Checklist + CTA |
| Dati mensili (GGR, quote) | Dati/mercato | Stat card + Contesto + Quote + Implicazione + CTA |
| Sentenze / TAR / CdS | Sentenza/norma | Hook + Dispositivo + Chi è colpito + Checklist + CTA |
| Riordino licenze / operatori | Normativa + dati | Hook + Before/After + Stat + Checklist + CTA |
| Mondiali / eventi stagionali | Dati/mercato | Stat + Contesto + Angolo + Implicazione + CTA |

---

## Note operative

**NotebookLM e duplicazione SEO**: le slide non sono testo indicizzabile.
Usare liberamente i punti chiave della newsletter nelle slide senza rischio
di cannibalizzazione SEO con Bottadiculo.it o LinkedIn Newsletter.

**Quando NON fare le grafiche**: se la newsletter è prevalentemente narrativa
senza punti secchi estraibili. In quel caso preferire un post LinkedIn diretto
invece del carosello.

**Aggiornamento workflow**: ogni volta che si trova un tipo di momento visivo
non mappato in questo file, aggiungerlo alla tabella di Step 1.
