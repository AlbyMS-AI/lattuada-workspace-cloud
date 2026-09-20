# Grafiche — Edizione #81 Gambling Insights (Bottadiculo)

Prodotte il 13/09/2026 con la pipeline locale (nessun tool esterno): main image da template fisso, infografiche da fallback HTML+render.sh (NotebookLM non usato, vedi nota affidabilità 13/09 in memoria).

## Main image

- Sorgente: `../grafiche/src/2026-09-11-fornitore-live-casino-cover.html`
- Output: `../grafiche/2026-09-11-fornitore-live-casino-cover.png` (1280×720)
- Kicker: `#81 · 14/09`
- H1: "Un fornitore fa causa. La tua due diligence non aspetta la sentenza."
- Sub: "Un report riservato, un accordo regolatorio europeo su un caso distinto, due revisioni USA già chiuse: lo stesso nome esce pulito da una parte e paga dall'altra."

## Infografica 1 — Timeline

- Sorgente: `../grafiche/src/2026-09-11-fornitore-live-casino-infografica-1.html`
- Output: `../grafiche/2026-09-11-fornitore-live-casino-infografica-1.png` (1080×1350)
- Titolo: "Una causa, quasi cinque anni, tre regolatori"
- Contenuto: 5 tappe (dic 2021 avvio causa contro la società di investigazione, 2024 chiusura revisione USA senza interventi correttivi richiesti, giu 2026 rigetto senza pregiudizio della richiesta convenuto, lug 2026 accordo regolatorio ~5M£ su episodio distinto e non collegato alla causa, set 2026 report riservato diventa pubblico)

## Infografica 2 — Checklist

- Sorgente: `../grafiche/src/2026-09-11-fornitore-live-casino-infografica-2.html`
- Output: `../grafiche/2026-09-11-fornitore-live-casino-infografica-2.png` (1080×1350)
- Titolo: "Tre verifiche prima della sentenza"
- Contenuto: 3 azioni (dati propri sui mercati serviti, stato revisioni regolatorie, provenienza e data del report indipendente) + riga di chiusura "La prossima due diligence non aspetta la sentenza"

## Note

- Nessun nome dei due fornitori in causa compare in nessuna delle tre grafiche, coerente con la scelta editoriale del testo (materia contenziosa in corso)
- Palette Bottadiculo reale: indigo `#1C0F3A`, arancio `#F9511F`, viola `#6330C7`, bianco `#FFFFFF` — invariata tra i tre output
- Checklist finale (leggibilità, testo non troncato, palette coerente, alt text) verificata visivamente su tutti e tre i render

## Seconda verifica Codex (13/09) — correzioni applicate

Cover e infografica 1 rifatte e rirenderizzate dopo la seconda verifica Codex: H1 corretto (non erano "due fornitori" a farsi causa reciproca), rigetto di giugno esplicitato come "senza pregiudizio", 2024 corretto in "senza interventi correttivi richiesti", luglio 2026 corretto in "accordo" (non "patteggiamento") ed esplicitamente marcato come episodio distinto e non collegato alla causa, "cinque anni" corretto in "quasi cinque anni". Infografica 2 (checklist) non modificata: nessun fatto contestato da Codex.

**Punto aperto per Alberto** (segnalato anche nel file SEO): l'importo, il mese e il fatto che sia un'autorità di gioco europea, combinati, sarebbero comunque sufficienti a risalire al fornitore incrociandoli col registro pubblico delle decisioni regolatorie — l'anonimizzazione dei nomi non equivale ad anonimizzazione piena. Da confermare se accettabile così o se generalizzare ulteriormente cifra/mese nel testo pubblicato.
