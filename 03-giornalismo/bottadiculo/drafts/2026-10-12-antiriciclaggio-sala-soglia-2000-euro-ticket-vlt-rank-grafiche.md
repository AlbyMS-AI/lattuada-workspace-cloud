# Grafiche — Gambling Insights #85 (antiriciclaggio in sala, soglia dei 2.000 euro, ticket VLT)

Pilota grafiche (piano `plans/2026-10-05-upgrade-grafiche-main-image-infografiche.md`): infografiche con `infografica-template.html` e la lib, copertina in due varianti affiancate. Palette Bottadiculo. Nessun nome di operatore italiano, nessun orario di pubblicazione.

---

## MAIN IMAGE — variante A (template fisso), fatta

Kicker "#85 · 12 ottobre 2026" · H1 "Guardare solo i 2.000 euro non basta" (hook diverso dal titolo) · Sub "Il contante sotto soglia si vede nel comportamento."

File: `bottadiculo/grafiche/2026-10-12-antiriciclaggio-sala-cover.png` (1280×720)

## MAIN IMAGE — variante B (foto), fatta l'11/10

Sorgente pronto: `bottadiculo/grafiche/src/2026-10-12-antiriciclaggio-sala-cover-foto.html`, stessi testi (15/18 parole, `check-grafica.py` ok). Foto generata con Gemini da Alberto l'11/10, in `bottadiculo/grafiche/inbox/2026-10-12-antiriciclaggio-sala.png` (bancone, ticket, schermi sfocati). File: `bottadiculo/grafiche/2026-10-12-antiriciclaggio-sala-cover-foto.png`. **Scelta di Alberto l'11/10: B (foto).** È la copertina da usare.

Prompt Gemini (16:9, da `lib/prompt-gemini.md`):

```
Fotografia editoriale orizzontale 16:9, alta risoluzione, stile reportage da rivista di settore.
Soggetto: il bancone cassa di una sala giochi di notte, visto da vicino: una piccola pila di banconote in euro tenute da un elastico e accanto un ticket di carta stampato, appoggiati sul piano lucido; sullo sfondo, molto sfocate, le luci degli schermi delle macchine.
Composizione: soggetto nella metà sinistra dell'inquadratura, metà destra sfocata e scura (sarà coperta in parte dal pannello di testo). Profondità di campo ridotta.
Luce: ombre profonde viola indaco, un solo punto luce caldo arancio.
Nessun testo, nessuna scritta, nessun numero, nessun logo, nessuna insegna leggibile.
Nessuna persona riconoscibile in volto.
```

Dopo il salvataggio: `render.sh png src/2026-10-12-antiriciclaggio-sala-cover-foto.html 2026-10-12-antiriciclaggio-sala-cover-foto.png 1280x720` e scelta A/B di Alberto.

---

## INFOGRAFICA 1 — fatta, confronto binario

Frase: la soglia vede la singola cifra, il contante che gira sta nel comportamento ripetuto. Struttura: confronto binario ("i due lati condividono lo stesso perimetro: gli obblighi dell'art. 53"). Sinistra "Cosa fa scattare la soglia" (giocata da 2.000 euro, ticket VLT da 500, ogni operazione guardata da sola), esito "Identificazione del cliente". Destra, in evidenza, "Cosa la soglia non vede" (contante sotto soglia visita dopo visita, ticket di qualunque importo con poche o nessuna vincita, il sospetto «quale che sia l'importo»), esito "Qui serve il controllo, con il perché scritto". Fonte: D.lgs. 231/2007, art. 53, commi 6 e 7.

`check-grafica.py`: 112/140 parole, fonte sì. Gate: messaggio 2, funzione 2, integrità 2, struttura 2, gerarchia 2, specificità 1, mobile 2, originalità 2 = 15/16.

File: `bottadiculo/grafiche/2026-10-12-antiriciclaggio-sala-infografica-1.png` (1080×1350)

## INFOGRAFICA 2 — fatta, quattro azioni con icona

"Cosa cambia da domani", griglia 2×2 (scheletro diverso dall'infografica 1): lente (ultimi tre mesi, traccia e ticket con poche vincite), busta con orologio (entro 10 giorni, conservazione 2 anni), foglio con persona (procedura anomalie a tutti i turni), penna (sotto soglia, scrivi perché). Fonte: D.lgs. 231/2007, artt. 52 e 53.

`check-grafica.py`: 89/140 parole, fonte sì. Gate: messaggio 2, funzione 1, integrità 2, struttura 2, gerarchia 2, specificità 2, mobile 2, originalità 2 = 15/16.

File: `bottadiculo/grafiche/2026-10-12-antiriciclaggio-sala-infografica-2.png` (1080×1350)

---

| File | Stato |
|---|---|
| `2026-10-12-antiriciclaggio-sala-cover.png` | fatta (variante A) |
| `2026-10-12-antiriciclaggio-sala-cover-foto.png` | fatta, **scelta** (variante B, foto) |
| `2026-10-12-antiriciclaggio-sala-infografica-1.png` | fatta |
| `2026-10-12-antiriciclaggio-sala-infografica-2.png` | fatta |

Alt text: vedi il companion SEO.
