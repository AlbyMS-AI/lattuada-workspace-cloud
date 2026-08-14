# Recensioni Bookmaker — Piano

**Committente**: Bottadiculo.it (richiesta caporedattore, 27/07/2026)
**Formato**: recensione completa operatore (bonus, quote, palinsesto, pagamenti, sicurezza, FAQ, comparativa) — modello: Recensione SNAI 2026
**Cadenza**: 1-2 recensioni a settimana
**Nota**: formato diverso dal solito editoriale Bottadiculo (post/newsletter). Voce affiliate/recensione, non voce Bottadiculo standard (niente "domanda sotto la domanda", ammesse prima persona plurale redazionale e CTA verso l'operatore).

## Pipeline operatori

| # | Operatore | Stato | Data pubblicazione | File |
|---|---|---|---|---|
| 1 | Betflag | Inviata al caporedattore (05/08/2026) | — | `betflag/recensione-betflag-2026.{md,docx,pdf}` |
| 2 | Planetwin365 | Bozza pronta, da inviare al caporedattore (14/08/2026) | — | `planetwin365/recensione-planetwin365-2026.{md,docx,pdf}` |
| 3 | Lottomatica | Da fare | — | — |
| 4 | Goldbet | Da fare | — | — |
| 5 | My Lotteries Play | Da fare | — | — |

## Generazione docx/pdf nello stile approvato (SNAI)

Il design (colori, tabelle, box) è stato estratto direttamente dal docx/pdf SNAI originali
già approvati da Bottadiculo (`Recensione_SNAI_2026.pdf/.docx`), non ricreato a occhio.
Motore riutilizzabile in `_template/`:

- `_template/review_docx_builder.py` — libreria Python (python-docx) con le funzioni per
  titolo, box rating, barra CTA gold, tabella info, box "contro" rosa, tabella valutazioni
  con header blu scuro, box nota blu, box voto finale crema, tabella comparativa
- `_template/review_style.css` — stesso design system in CSS, usato per generare l'HTML
  che poi diventa PDF via Chrome headless

Per una nuova recensione (es. Planetwin365): copiare `betflag/build_betflag_docx.py` e
`betflag/build_betflag_html.py` nella cartella del nuovo operatore, sostituire i contenuti,
poi:

```
/tmp/docxenv/bin/python build_<operatore>_docx.py   # richiede venv con python-docx installato
python3 build_<operatore>_html.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --no-pdf-header-footer --print-to-pdf="recensione-<operatore>-2026.pdf" \
  "file://$(pwd)/recensione-<operatore>-2026.html"
```

Nota: l'header/footer ripetuto su ogni pagina (titolo/data in alto, "Pagina X" in basso)
funziona correttamente solo nel DOCX (meccanismo nativo Word). Nel PDF, Chrome headless
non ripete in modo affidabile elementi fissi su più pagine stampate (si sovrappongono al
contenuto): il PDF ha quindi una nota di intestazione solo in cima al documento, senza
numerazione di pagina ripetuta.

## Template struttura (da Recensione SNAI 2026)

1. Header + info essenziali (licenza, proprietà, bonus, metodi pagamento, servizio clienti, deposito minimo, registrazione rapida)
2. Perché [operatore] potrebbe non fare al caso tuo (contro sintetici)
3. Prefazione
4. Valutazioni (tabella per categoria + media)
5. Pro & contro (sviluppati)
6. Panoramica eventi e streaming
7. Tipologia di giochi disponibili
8. Promozioni (dettaglio percorsi bonus)
9. Grafici e report — statistiche comparative (payout, volume offerta)
10. Info su quote, mercati, funzionalità + come piazzare una scommessa
11. Top uscite e scelte degli esperti
12. Conto di scommessa e registrazione
13. Metodi di pagamento (depositi/prelievi)
14. Sicurezza
15. Customer support
16. Focus demo
17. Altri prodotti nell'offerta
18. Feedback e recensioni utenti
19. Tabella comparativa vs 2 competitor
20. Il nostro giudizio + voto finale
21. FAQ
22. Le migliori alternative

## Regola dati

Ogni cifra (bonus, rollover, licenza ADM, payout, limiti pagamento) va verificata su fonte primaria (sito ufficiale operatore, T&C) prima della pubblicazione. Se un dato non si incrocia, si approfondisce o si omette — mai pubblicare con avviso di incertezza.
