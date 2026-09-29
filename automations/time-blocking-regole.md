# Time blocking — regole di ALDO

> Creato: 29/09/2026, implementando `plans/2026-09-29-time-blocking-calendario-aldo.md`.
>
> ALDO legge questo file a ogni run dal repo cloud. Categorie, durate, tetti e regole di piazzamento stanno qui e non nel prompt, per la stessa ragione per cui date, cadenze e progetti sono stati tolti dai prompt il 12/08, il 31/08 e il 01/09: un elenco dentro un prompt invecchia in silenzio. Se una regola cambia, si cambia qui.

## Il principio

**Alberto non apre Linear.** Guarda il calendario e legge l'email di ALDO. Tutto quello che deve dire al sistema lo scrive sul calendario, con i tre segnali qui sotto. Linear resta il registro, ma lo usano solo gli agenti e le skill.

## Disponibilità

Le fasce in cui Alberto può lavorare stanno nel documento Linear **"Finestre disponibili"** (team ALB, id `6342fcf3-8987-4de3-b130-70e6e6d595d0`), una riga per data con fasce e tetto giornaliero.

- Un blocco va solo dentro una fascia di quel documento.
- Se il documento non si legge, ALDO non piazza nessun blocco e lo scrive nell'email.
- Se la copertura del documento finisce entro 14 giorni, ALDO lo segnala nell'email.

## Grammatica del calendario (quello che scrive Alberto)

| Alberto scrive | Dove | ALDO il mattino dopo |
|---|---|---|
| `ok` davanti al titolo | su un blocco `[TB]` passato | Chiude la issue. Commento `Tempo reale: <durata del blocco> (non misurato)` |
| `ok 1h30` davanti al titolo | come sopra | Chiude la issue. Commento `Tempo reale: 1h30` |
| `+ testo`, durata facoltativa in fondo (`30m`, `1h`, `1h30`) | evento nel giorno in cui va fatto | Crea la issue con due date uguale a quel giorno, cancella l'evento `+`, piazza il blocco |
| `+ ALB-NNN` | evento in un giorno qualsiasi | Imposta la due date della issue a quel giorno, cancella l'evento `+`, piazza il blocco |

- Il riconoscimento non distingue maiuscole e minuscole e tollera spazi in più.
- Un segnale che ALDO non capisce non produce nessuna azione e finisce nell'email alla voce "Non capito".
- **Un blocco passato senza `ok` non vale come fatto.** La issue resta aperta, ALDO la ripiazza e la elenca alla voce "Non segnati". Una chiusura falsa sparisce senza che nessuno se ne accorga, un promemoria in più no.
- La chiusura via risposta al check serale resta valida come secondo canale. Se la stessa issue risulta chiusa da tutti e due, nessun problema: chiudere è idempotente.
- Per gli eventi `+`, ALDO sceglie il progetto Linear dal contenuto. Nel dubbio non mette nessun progetto e lo scrive nell'email.

## Categorie ed etichette

Sul calendario il titolo della issue non compare mai. Compare solo un'etichetta neutra.

| Origine della issue | Etichetta | colorId |
|---|---|---|
| Progetto Giornalismo, titolo con "Jamma" | Communication 1 | 3 |
| Progetto Giornalismo, titolo con "Bottadiculo" | Communication 2 | 6 |
| Progetto Giornalismo, titolo con "Sitiscommesse" | Communication 3 | 2 |
| Progetto Giornalismo, altro | Communication | 5 |
| Progetto Contenuti LinkedIn | Communication 4 | 7 |
| Progetto LasVegas | Affiliation | 11 |
| Progetti Italy Market, BizDev Deals, BizDev Internal, Crypto & Special | BD | 9 |
| Progetto ML Russo, inglese | Training | 10 |
| Nessun progetto, o label `admin` | Admin | 8 |
| Candidature, colloqui, CV, ricerca di lavoro | **mai a calendario** | — |

## Formato del blocco

- Titolo: `<Etichetta> · ALB-NNN`
- Descrizione: `[TB] ALB-NNN` più il link alla issue
- `visibility: private`, `availability: AVAILABILITY_FREE`
- Nessun invitato, `notificationLevel: NONE`
- Promemoria popup a 10 minuti

Il marcatore `[TB]` in descrizione è il modo in cui ALDO riconosce i propri blocchi. **ALDO sposta e cancella solo eventi con `[TB]` e gli eventi `+`.** Non tocca mai nessun altro evento.

## Durate

Confermate da Alberto il 29/09/2026, da ricalibrare dopo 14 giorni sui tempi reali.

| Formato | Durata |
|---|---|
| Articolo Jamma | 1h |
| Post Bottadiculo | 1h |
| Newsletter Jamma | 1h |
| Newsletter Bottadiculo | 1h30 |
| News Sitiscommesse | 1h |
| Post LinkedIn | 1h |
| Newsletter LinkedIn | 1h30 |
| Carosello | 1h |
| Messaggio ricorrente LasVegas | 30 min |
| Revisione settimanale LinkedIn | 30 min |
| Task BD o Admin senza indicazione | 1h |

Precedenza:

1. la durata nel titolo dell'evento `+`
2. la riga `Durata: Xh` nella descrizione della issue
3. questa tabella

Il blocco minimo è di 30 minuti.

## Regole di piazzamento

In ordine:

1. **Candidate:** issue non completate, non annullate e non duplicate, con due date entro oggi+3, arretrati compresi. Escluse quelle che ALDO mette in "Fermo su altri". Le issue senza due date non si piazzano.
2. **Ordine:** due date crescente, poi priorità (Urgent, High, Medium, Low, nessuna).
3. **Già piazzata:** se esiste un blocco `[TB]` futuro per quell'ID, si salta.
4. **Dove:**
   - la prima fascia libera, entro la due date compresa, in cui entra tutta la durata
   - mai spezzare un task
   - nessuna sovrapposizione con eventi a orario già presenti; gli eventi di un'intera giornata segnati "libero", come i promemoria, non contano
   - il tetto giornaliero va rispettato
5. **Preferenze, non vincoli:**
   - BD e Affiliation nelle fasce fra le 09:00 e le 18:00 dei giorni feriali, quando le persone rispondono
   - Communication nelle fasce di almeno 2h
6. **Se non entra:**
   - si può spostare un blocco `[TB]` futuro con due date più lontana
   - se non basta, niente blocco e una riga nell'email: "Non entra: ALB-NNN, servono Xh, prima di GG/MM ce ne sono Yh"
7. **Pulizia:** se una issue è chiusa e ha un blocco `[TB]` futuro, il blocco si cancella. I blocchi passati non si cancellano mai, servono per la calibrazione.

## Email di ALDO: sezione "Calendario"

Subito dopo "La tua giornata":

- blocchi di oggi con orario
- blocchi nuovi o spostati nei prossimi tre giorni
- "Non entra", "Non segnati", "Non capito"
- issue create dagli eventi `+`
- avviso di copertura del documento "Finestre disponibili", se in scadenza

**Il lunedì**, in più, la sezione **"Senza data"**: le issue aperte senza due date, una riga ciascuna con ID, così Alberto può datarle con `+ ALB-NNN` senza aprire Linear.

## Riservatezza

- Il titolo della issue non va mai nell'evento. Solo etichetta e ID.
- Questo file sta in un repo pubblico. Non contiene, e non deve mai contenere, informazioni sul perché le fasce sono quelle che sono.
