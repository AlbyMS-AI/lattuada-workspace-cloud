# Grafiche — Gambling Insights #80 (Lottomatica-CIRSA / rete fisica / PREU)

3 output: main image (Gemini + composizione HTML/render.sh, come da pipeline validata
13/07/2026) + due infografiche interne (NotebookLM, lato utente).

**Palette Bottadiculo (reale, da bottadiculo.it — non la navy personale di Alberto):**
sfondo indigo `#1C0F3A` · accento unico arancio `#F9511F` · secondario viola `#6330C7` ·
testo bianco `#FFFFFF`.

---

## MAIN IMAGE — prompt Gemini (nessun testo nell'immagine)

Genera tu il visual su Gemini con il prompt sotto, poi salvalo in
`04-linkedin/grafiche/inbox/lottomatica-cirsa-rete-fisica-brand.png`. Una volta lì compongo
il testo sopra via template HTML e `render.sh`, stessa pipeline di
`04-linkedin/grafiche/src/2026-07-13-invisible-funnel-onboarding-kyc.html`, e ti mostro il
risultato prima di darlo per definitivo.

```
Illustrazione editoriale flat design, verticale 4:5 (1080x1350px).
Nessun testo, nessuna scritta, nessuna lettera, nessun logo reale, nessun volto umano.

Soggetto: due blocchi geometrici solidi si fondono in un'unica forma più grande al
centro dell'immagine, in leggera diagonale verso l'alto, a comunicare crescita e
concentrazione. Alla base della composizione, staccata dal resto e più piccola, una
singola tessera quadrata si spezza via dalla forma principale con una crepa netta e
cade isolata verso il basso, senza alcun collegamento visivo con la massa sopra.
Contrasto netto tra la forma che cresce e sale e la tessera piccola che si stacca
e scende, sola.

Palette colori obbligatoria: sfondo indigo scuro (#1C0F3A), la forma principale in
bianco quasi puro (#FFFFFF), accento arancio (#F9511F) solo sulla tessera che si
stacca alla base, per farla risaltare come punto focale. Nessun altro colore fuori
palette, nessun viola in questa immagine (resta per la tipografia in composizione).

Stile: minimal, forme geometriche pulite, alto contrasto, illustrazione editoriale
da rivista di business, non 3D, non fotorealistico, nessuna icona generica.
```

---

## INFOGRAFICA 1 — NotebookLM (utente), stat card

### Fonte da caricare in NotebookLM
Il paragrafo con i dati Flutter/Paddy Power in "Il fatto" della newsletter
(`2026-09-04-lottomatica-cirsa-rete-fisica-paddy-power-newsletter-linkedin.md`).

### Brief (copia e incolla)

```
Level of detail: Concise

Tipo: stat card

Titolo: 100 negozi sotto revisione

Contenuto:
100 negozi Paddy Power, Regno Unito
Sotto revisione dal 3 settembre 2026
Causa: Remote Gaming Duty dal 21% al 40%
Fonte: SBC News, 03/09/2026

Cosa NON includere:
Nessuna icona di negozio, nessun logo Paddy Power o Flutter, nessuna bandiera

Layout: centrato, numero dominante, gerarchia chiara tra numero e testo di contesto
Palette: sfondo #1C0F3A, testo #FFFFFF, numero in accento #F9511F, dettaglio
secondario #6330C7
Formato: 4:5 (1080x1350px)
```

---

## INFOGRAFICA 2 — NotebookLM (utente), before/after

### Fonte da caricare in NotebookLM
Le sezioni "Il fatto" e "La parte che nessuno sottolinea" della newsletter.

### Brief (copia e incolla)

```
Level of detail: Normal

Tipo: before-after (due colonne)

Titolo: Stesso meccanismo, tempi diversi

Contenuto:
COLONNA SINISTRA — "Regno Unito: dopo lo shock"
- RGD dal 21% al 40% da aprile 2026
- 100 negozi Paddy Power sotto revisione
- 400 posti di lavoro a rischio

COLONNA DESTRA — "Italia: prima dello shock"
- PREU già al 25,5% e 24,5%, salito più volte
- Blackstone: 24% e due poltrone nel board
- Nessun impegno scritto sulla rete fisica

Cosa NON includere:
Nessuna freccia animata, nessuna icona, nessun logo, nessuna bandiera

Layout: due colonne simmetriche, separatore verticale in #6330C7
Palette: sfondo #1C0F3A, colonna sinistra accento #F9511F, testo #FFFFFF
Formato: 4:5 (1080x1350px)
```

---

## Export e salvataggio

| File | Nome | Dove |
|---|---|---|
| Immagine Gemini grezza (utente) | `lottomatica-cirsa-rete-fisica-brand.png` | `04-linkedin/grafiche/inbox/` |
| Main image composta (Claude, dopo) | `2026-09-07-lottomatica-cirsa-cover.png` | `04-linkedin/grafiche/` |
| Infografica 1 (NotebookLM, utente) | `2026-09-07-lottomatica-cirsa-infografica-1.png` | `04-linkedin/grafiche/inbox/` poi spostata |
| Infografica 2 (NotebookLM, utente) | `2026-09-07-lottomatica-cirsa-infografica-2.png` | `04-linkedin/grafiche/inbox/` poi spostata |

Alt text per tutte e tre: schema [soggetto] + [dato/contesto] + [2026], vedi il file
`...-newsletter-linkedin-seo.md`.

**Prossimo passo:** genera l'immagine Gemini per la main image e falla arrivare (inbox o
qui in chat), poi scrivo l'HTML e lancio `render.sh` per il file finale.
