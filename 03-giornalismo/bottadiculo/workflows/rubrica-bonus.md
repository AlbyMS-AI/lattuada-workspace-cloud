# Workflow — Rubrica Bonus (Bottadiculo.it)

## Cos'è
Rubrica in aggiornamento continuativo sulle offerte bonus degli operatori ADM. Serve come riferimento pratico per il lettore che vuole capire cosa c'è sul mercato.

## Quando aggiornare
- Quando un operatore lancia un nuovo bonus o modifica un'offerta esistente
- Revisione periodica (almeno mensile) per verificare la validità delle offerte

## Struttura scheda singolo bonus

```
## [Nome Operatore] — [Tipo di Bonus]
**Aggiornato al**: [data]

| Campo | Dettaglio |
|---|---|
| Tipo | Welcome / Reload / Cashback / Free Spin / No Deposit |
| Importo | [es. 100% fino a €500] |
| Requisito di puntata | [es. 30x sul bonus] |
| Giochi validi | [es. slot, escludi live casino] |
| Validità | [giorni per completare il wagering] |
| Codice promo | [se presente] |
| Licenza | ADM |

**Giudizio sintetico**: [1-2 righe. Onesto: è buono? È nella media? Attenzione a cosa?]

**Link**: [landing page operatore]
```

## Tono della rubrica
- Come un amico esperto che ti dice la verità
- Non sei un affiliato che deve convertire: sei un giornalista che valuta
- Se un bonus fa schifo, dillo (con educazione e argomentazione)
- Segnala sempre il requisito di puntata: è il dato più importante per il giocatore reale

## Step per aggiungere/aggiornare una scheda

### Step 1 — Raccolta dati
- Recupera T&C aggiornati dall'operatore
- Verifica che il bonus sia ancora attivo
- Nota: data di scadenza o validità dell'offerta

### Step 2 — Compilazione scheda
- Compila tutti i campi della struttura
- Scrivi il giudizio sintetico con onestà

### Step 3 — Aggiornamento pagina
- Aggiorna o aggiungi la scheda nel file `../templates/rubrica-bonus-[anno].md`
- Aggiorna la data "aggiornato al" anche per le schede revisionate

## Output
- File aggiornato: `../templates/rubrica-bonus-[anno].md`
