# Grafiche — Gambling Insights #82 (blocco ADM / DNS / provider)

3 output, tutti fatti da Claude con la pipeline HTML/SVG + `render.sh` (nessun NotebookLM,
corretto il 20/09/2026: la sola tipografia non spiegava il meccanismo, serviva un diagramma
vero). Cartella: `bottadiculo/grafiche/` — non `04-linkedin/grafiche/`, riservata alle
grafiche personali di Alberto.

**Palette Bottadiculo:** sfondo indigo `#1C0F3A` · accento unico arancio `#F9511F` ·
secondario viola `#6330C7` · testo bianco `#FFFFFF`. Nessun giorno/orario di pubblicazione
nel testo delle grafiche.

---

## MAIN IMAGE — fatta

Kicker: "#82 · 21 settembre 2026" · H1: "Il blocco ADM non è uguale per tutti i provider" ·
Sub: "Il sito è nella lista dei domini oscurati. Non significa che sia irraggiungibile
ovunque, subito, per chiunque."

File: `bottadiculo/grafiche/2026-09-19-adm-blocco-dns-provider-cover.png` (1280×720)

---

## INFOGRAFICA 1 — fatta, diagramma del meccanismo

Non una quote card: un diagramma a due colonne che mostra perché lo stesso dominio risulta
bloccato per un utente e raggiungibile per un altro. Nodo in alto ("Sito oscurato da ADM"),
biforcazione su provider grande (icona orologio, "poche ore", icona reindirizzamento) e
provider minore (icona orologio, "anche giorni", icona sito ancora online), nota finale con
icona server ("il server estero resta online in entrambi i casi").

File: `bottadiculo/grafiche/2026-09-19-adm-blocco-dns-provider-infografica-1.png` (1080×1350)

---

## INFOGRAFICA 2 — fatta, checklist con icone

Sezione "Cosa cambia da domani", quattro punti ciascuno con icona propria coerente col
contenuto: lente di ingrandimento (brand protection/verifica), fumetto (comunicazione gioco
responsabile), radar (monitoraggio varianti dominio), cronometro (tempi di propagazione
provider minori).

File: `bottadiculo/grafiche/2026-09-19-adm-blocco-dns-provider-infografica-2.png` (1080×1350)

---

## Export e salvataggio

| File | Nome | Dove | Stato |
|---|---|---|---|
| Main image | `2026-09-19-adm-blocco-dns-provider-cover.png` | `bottadiculo/grafiche/` | **fatta** |
| Infografica 1 | `2026-09-19-adm-blocco-dns-provider-infografica-1.png` | `bottadiculo/grafiche/` | **fatta** |
| Infografica 2 | `2026-09-19-adm-blocco-dns-provider-infografica-2.png` | `bottadiculo/grafiche/` | **fatta** |

Sorgenti HTML: `bottadiculo/grafiche/src/2026-09-19-adm-blocco-dns-provider-cover.html` e
le due infografiche omonime nella stessa cartella.

Alt text per tutte e tre: vedi tabella "Featured Image — Alt Text" in
`2026-09-19-adm-blocco-dns-provider-propagazione-oscuramento-seo.md`.

**Da fare:** conferma visiva di Alberto sulle tre grafiche prima della pubblicazione.
