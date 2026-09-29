# Linear — convenzioni operative

> Creato: 01/09/2026, implementando `plans/2026-09-01-sistema-task-unico-linear-assistente.md`.
>
> Questo è il file che agenti e skill leggono per non reinventare il formato a ogni run. Se una convenzione cambia, si cambia qui e basta: nessun prompt di agente deve contenerne una copia (stessa ragione per cui il 12/08 e il 31/08 sono state rimosse le date e le cadenze hardcoded da ALDO, MARCO e OTTO).

## Il principio

**Linear è il registro unico dei task su tutti i domini. I file `task-list.md` sono piani, non registri.**

Un piano contiene il ragionamento, gli slittamenti motivati, il backlog senza data, le alternative scartate. Un registro contiene solo cose con una data e un proprietario. Servono entrambi, e non sono lo stesso oggetto.

Quando i due divergono, si aggiorna prima il piano e poi si lancia `/agenda`, che riallinea il registro.

**Alberto non apre Linear (dal 29/09/2026).** Non ama usarlo per gestire i task. La sua interfaccia è il calendario Softswiss più l'email di ALDO: chiude, aggiunge e data i task con tre segnali sul calendario (`ok`, `+ testo`, `+ ALB-NNN`), descritti in `time-blocking-regole.md`, e ALDO li riporta qui ogni mattina. Linear resta il registro unico, ma lo usano gli agenti e le skill. Nessuna skill e nessun agente deve proporre ad Alberto "apri Linear e...": se serve un'azione sua, gliela si chiede sul calendario o in chat.

## Workspace e team

- Workspace Linear: **AlbertoBDMGA**
- Team key: **ALB** (unico team, `dec48cc7-d99d-414a-8936-058b00775f39`)

## Progetti

| Progetto | ID | Cosa contiene |
|---|---|---|
| **Contenuti LinkedIn** | `792b655c-91b5-4680-ad1d-22fdf79169e3` | Post, caroselli, sondaggi, newsletter "The Betting Edge", batch outbound |
| **Giornalismo** | `f829b28e-dfb7-4c5d-a24f-16297e59adc9` | Jamma, Bottadiculo, Sitiscommesse: articoli, newsletter del lunedì, recensioni bookmaker |
| **Italy Market** | `47fcc74c-8650-439b-a487-70e30ac4ed8a` | Softswiss, mercato italiano |
| **BizDev Deals** | `e1c876d8-ed58-4bc7-a8df-5e1991ec6a32` | Softswiss, deal per mercato |
| **BizDev Internal** | `625a7ce0-86ea-41df-8229-46b60d69ba90` | Softswiss, processi interni, PMO |
| **Crypto & Special** | `7559b359-f5ff-4044-8c75-e74e65f74d8c` | Softswiss, verticali speciali |
| **LasVegas** | `99c6f8b0-c34c-42df-9951-6bb795ec463f` | B2C omnichannel, rete giocatori, ricorrenze |
| **ML Russo** | `e0807770-3168-4c70-86f5-e885117cf85b` | Corso MLR, formazione |

**Chi legge deve leggere la squadra, non l'elenco dei progetti.** Fino al 01/09/2026 ALDO interrogava quattro progetti su otto, quindi LasVegas, ML Russo e qualsiasi issue senza progetto erano invisibili al brief mattutino, pur essendo dentro Linear. Un elenco di progetti scritto dentro un prompt è la stessa classe di errore delle date hardcoded: invecchia in silenzio. Interrogare `list_issues` sul team `AlbertoBDMGA` senza filtro progetto.

## Label

| Label | Quando si usa |
|---|---|
| `contenuto` | Produzione editoriale: post, caroselli, newsletter, articoli |
| `ricorrente` | Generata da ALDO il lunedì leggendo le sezioni "Ricorrenze" delle task list. **Non crearla a mano** |
| `commerciale` | Deal, prospect, outreach, pipeline (Softswiss e LasVegas) |
| `admin` | Manutenzione workspace, formazione, amministrazione |

## La due date: la data in cui devi metterti a lavorare

**Regola.** La due date su Linear è la data **"creare entro"**, mai quella di pubblicazione.

Le task list dei contenuti hanno due date per riga (quando pubblichi, entro quando devi averlo pronto). Linear ne regge una sola, e quella utile a un assistente è la data in cui bisogna agire.

La data di pubblicazione vive nel titolo, in formato fisso:

```
[pubb. GG/MM] Formato Lingua — Titolo
```

Esempi reali:

- `[pubb. 04/09] Newsletter N4 IT — Il costo reale di un'integrazione multipla` → due date 02/09
- `[pubb. 11/09] Carosello EN — Checklist compliance nuovo mercato` → due date 09/09

Per gli arretrati il prefisso diventa `[arretrato, era GG/MM]` e **la due date resta nel passato**, perché l'arretrato deve continuare a comparire come tale finché qualcuno non decide se recuperarlo o chiuderlo.

Regola "creare entro" per i contenuti LinkedIn, da `04-linkedin/task-list.md`: contenuto di lunedì → creare entro il giovedì precedente; contenuto di mercoledì → entro il lunedì; contenuto di venerdì → entro il mercoledì.

## Durata

Facoltativa. Una riga `Durata: Xh` (o `Durata: 30m`, `Durata: 1h30`) nella descrizione della issue dice ad ALDO quanto blocco riservarle a calendario. Senza la riga vale la tabella per formato in `time-blocking-regole.md`. Il campo `estimate` di Linear non si usa.

## Quando NON mettere una due date

Una data inventata è peggio di nessuna data: produce un falso allarme tutti i giorni finché qualcuno non la guarda.

Niente due date quando:

- il task è in pausa per decisione di Alberto (esempio: i batch outbound, fermi dal 18/08)
- la data originale è passata e quella nuova la deve dare Alberto (esempio: gli arretrati LasVegas)
- è una issue ombrello che raccoglie un filone e non ha una consegna propria (esempio: ALB-46)

In tutti e tre i casi si scrive **nella descrizione** perché la data manca. Non si riempie il vuoto.

## Prima di creare una issue: cerca su TUTTI gli stati

**Regola aggiunta il 02/09/2026 dopo un duplicato reale.**

Cercare se una issue esiste già filtrando su Todo e In Progress non basta: **il Backlog è uno stato non completato a tutti gli effetti** e ci vive la maggior parte del lavoro non ancora iniziato.

Cosa è successo: il 01/09, migrando il piano editoriale, la ricerca è stata fatta su Todo e In Progress. Il risultato erano 5 issue, e su quel numero è stata costruita tutta la diagnosi. Le issue non completate erano in realtà 28, con 23 in Backlog. Fra quelle c'era ALB-94, che è stata duplicata in ALB-105.

Conseguenza pratica: `list_issues` va chiamato senza filtro di stato, scartando poi solo `completed` e `canceled` sul campo `statusType`. È lo stesso identico errore di forma dell'elenco di progetti hardcoded, applicato agli stati invece che ai progetti: si guarda un sottoinsieme e si scambia per il tutto.

## Igiene: cosa fare con una scadenza passata

Regola già registrata in memoria il 12/08/2026 e ora vincolante per `/agenda` e per chiunque tocchi il registro.

Davanti a una issue con due date passata, **non spostare la data e basta**. Prima:

1. Controllare se esiste un piano, un calendario o un thread più aggiornato (piano editoriale, note di call, Pipedrive) che dica cosa è successo davvero.
2. Se il contesto originale della issue è superato, aggiornare **titolo e descrizione**, non solo la data. Una issue che rimanda a un piano che non esiste più va riscritta, non riprogrammata.
3. Se più issue hanno scadenze passate nello stesso giro, segnalarlo come manutenzione mancata, non come eccezioni isolate.

## Chi scrive cosa

| Chi | Cosa scrive |
|---|---|
| **ALDO** (cron, 08:30) | Chiude le issue leggendo i blocchi segnati `ok` sul calendario e la risposta di Alberto al check serale, con commento `Tempo reale`. Crea issue dagli eventi `+ testo` e imposta due date dagli eventi `+ ALB-NNN`. Scrive e sposta i blocchi `[TB]` sul calendario. Il lunedì crea le issue `ricorrente` mancanti. Regole in `time-blocking-regole.md` |
| **Check serale** (cron, lun-ven 18:30) | Non scrive nulla su Linear. Chiede e basta |
| **`/agenda`** (on demand) | Sincronizza piani e registro, propone e applica solo dopo conferma di Alberto |
| **Skill di contenuto** (`linkedin-crea-post`, `linkedin-crea-newsletter`, `linkedin-crea-sondaggio`, `jamma`, `bottadiculo`, `news-sitiscommesse`) | Chiudono la issue del pezzo che hanno appena prodotto |
| **`post-call`** | Crea le issue dai task emersi in call (invariato) |
| **MARCO** (cron, lun 07:00) | Solo lettura, incrocia Linear con Pipedrive |

Tutta la scrittura automatica ricorrente è concentrata in ALDO. Se due routine scrivessero sullo stesso registro, un disallineamento diventerebbe impossibile da attribuire.

## Riservatezza

Vale la stessa regola del resto del workspace: **niente insight, dati o dettagli identificabili** che avvantaggino i competitor di Alberto o di Softswiss. Le issue di contenuto descrivono il meccanismo, non il dossier da cui è emerso.

`02-softswiss/` e le cartelle personali riservate non finiscono mai in un repo esterno (questo file sì: è nel repo cloud pubblico dal 29/09/2026, quindi non deve contenere niente di riservato). Linear è un servizio terzo: nelle issue si citano i percorsi dei file, mai il loro contenuto sensibile.
