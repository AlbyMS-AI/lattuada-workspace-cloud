# Sistema Oggi — regole di ALDO

> Creato: 21/10/2026, implementando `plans/2026-10-20-sistema-oggi-telegram-webapp.md`. Prende il posto di `time-blocking-regole.md` (archiviato).
>
> ALDO legge questo file a ogni run dal repo cloud. Date, progetti, cadenze e liste non stanno nel prompt di ALDO e non stanno qui: ALDO li legge da Linear e dalle `task-list.md`. Se una regola cambia, si cambia qui.
>
> Il file sta in un repo pubblico: non contiene dati riservati e non deve mai contenerne.

## Il principio

**Alberto non apre Linear.** La sua interfaccia è la pagina Oggi (web app, accesso solo con il suo account Google), annunciata ogni mattina alle 07:30 da un messaggio Telegram. Linear è il registro dietro le quinte: lo usano la pagina, gli agenti e le skill.

Chi fa cosa:

| Chi | Cosa |
|---|---|
| **ALDO** (cron, prima delle 07:30) | Sceglie le voci di Oggi, scrive il documento Linear "Oggi", smista le voci `da-smistare`, il lunedì crea le ricorrenze |
| **Pagina Oggi** (Apps Script) | Legge e scrive Linear: chiude, sposta a domani o alla settimana dopo, aggiunge, porta in Oggi |
| **Telegram** (Apps Script, 07:30) | Manda tre righe e il link. Niente nomi di deal né titoli di call |

## Label del sistema

| Label | Chi la scrive | Significato |
|---|---|---|
| `oggi` | ALDO e pagina | Le al massimo cinque voci di oggi |
| `spunto` | pagina | Idea senza data. Mai in Oggi |
| `da-smistare` | pagina | Voce aggiunta dalla pagina, senza progetto. ALDO assegna il progetto e toglie la label |
| `in-attesa` | pagina o `/agenda` | Voce ferma su altri. Mai in Oggi |

## Selezione di Oggi

Ogni mattina, in ordine, fino a un massimo di **cinque** voci:

1. **Rimaste:** le voci con `oggi` ancora aperte (il non fatto resta in Oggi, niente liste di "non segnati").
2. **Vive:** titolo con `[pubb. GG/MM]` dove il giorno di lavoro è oggi o già passato e la pubblicazione non è ancora passata; oppure due date uguale a oggi.
3. **Arretrati:** due date passata e nessuna pubblicazione futura, in ordine di priorità (Urgent, High, Medium, Low, nessuna) e poi due date **più recente** prima. Il più vecchio non è il più urgente.

Escluse sempre: voci completate, annullate o duplicate; voci `spunto`; voci `in-attesa`; voci senza due date (a meno che siano già `oggi`).

Le voci scelte prendono la label `oggi`. **La label `oggi` va tolta da ogni voce aperta non scelta.**

### Rimaste oltre cinque

Se le voci rimaste dal giorno prima sono più di cinque, le prime cinque (priorità, poi due date più recente) restano in Oggi. Le altre perdono `oggi` e ALDO ne scrive l'ID nella sezione "Da ieri" del documento. La pagina le mostra in testa a Prossimi con la scritta "da ieri".

## Smistamento

Alle voci con `da-smistare` ALDO assegna il progetto in base al contenuto (progetti e label in `linear-convenzioni.md`) e toglie la label. Nel dubbio non assegna niente e lascia la label. ALDO non cambia mai titolo, due date o altre label di una voce che smista.

## Documento Linear "Oggi"

Team AlbertoBDMGA, senza progetto, id `d3cc4001-0d40-48b0-b7d3-2a3d6f2186ed`. **Va riscritto per intero ogni mattina**, con questo formato:

```
Data: GG/MM/AAAA

## Call
HH:MM–HH:MM Titolo

## Da ieri
ALB-NNN

## Problemi
(una riga per ogni lettura fallita)
```

- **Data:** la data di oggi, calcolata dal clock della sessione. La pagina e Telegram usano questa riga per sapere se ALDO ha girato oggi.
- **Call:** una riga per ogni evento a orario del calendario Softswiss di oggi. Esclusi gli eventi di un'intera giornata, quelli con `[TB]` nella descrizione (residui del vecchio sistema) e i promemoria. Se non ci sono call, la riga `Nessuna call`.
- **Da ieri:** gli ID delle rimaste oltre cinque. Se non ce ne sono, `Nessuna`.
- **Problemi:** ogni lettura fallita (Linear, Calendar, repo), scritta in chiaro. **Mai riempire a memoria** una sezione che non si è riusciti a leggere: si scrive il problema. Se è tutto a posto, `Nessuno`.

## Ricorrenze del lunedì

Invariata rispetto a ALDO v2:

- ALDO clona il repo pubblico, trova **tutte** le `task-list.md` con una sezione "Ricorrenze" e crea le issue mancanti della settimana, con progetto e label letti dal blocco in testa a ogni sezione.
- Due date = "creare entro" (per le newsletter del lunedì, il lock del giovedì precedente).
- Anti-duplicato per data di pubblicazione, formato e testata, su tutti gli stati tranne Canceled.
- Nessuna cadenza e nessun elenco di file nel prompt.

**Novità: la copia nuova chiude quelle vecchie.** Quando ALDO crea una ricorrenza **senza** `[pubb.]` nel titolo e trova una copia ancora aperta con titolo identico, la copia vecchia passa a Canceled con il commento `superata dalla copia del GG/MM`. Le ricorrenze con `[pubb.]` hanno titoli diversi per ogni uscita e non si toccano.

## Divieti

- Non scrivere mai sul calendario. Il calendario Softswiss si legge e basta, per le call.
- Non mandare email.
- Non inventare una due date.
- Non toccare mai il titolo `[pubb. GG/MM]`.
- Non spostare a domani o alla settimana dopo: lo fa Alberto dalla pagina. Quello è l'unico modo in cui una voce cambia due date per decisione sua.
- Non scrivere nel documento "Oggi" titoli di deal o nomi di prospect: nel documento stanno solo orari e titoli delle call, più ID.

## Quando ALDO non gira

La notifica Telegram parte lo stesso e dice "ALDO non ha aggiornato il piano di oggi". La pagina mostra comunque le voci con `oggi` del giorno prima e il resto.
