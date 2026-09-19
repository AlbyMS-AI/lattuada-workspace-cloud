# Blocco ADM ai siti illegali: perché non è mai istantaneo per tutti

**Slug:** blocco-adm-siti-illegali-provider-dns-propagazione
**Nota:** versione blog Bottadiculo.it, apertura diversa dalla newsletter LinkedIn (Gambling Insights #82). Link alla newsletter completa da inserire dopo la pubblicazione delle 7:30.

---

Hai mai controllato se un sito che pensavi bloccato lo fosse davvero, sul provider che usano i tuoi utenti, o te lo sei solo dato per scontato perché era nella lista ADM?

## Un blocco che agisce sull'indirizzo, non sul sito

Il meccanismo di oscuramento ADM funziona sul DNS: quando qualcuno digita un dominio bloccato, il provider lo reindirizza alla pagina di avviso invece che al sito vero. Il server estero continua a funzionare come prima. Non è stato tolto niente da internet. È stato tolto un cartello stradale, non demolito l'edificio.

I grandi provider italiani propagano un nuovo blocco in poche ore, con procedure automatizzate. I provider minori lavorano spesso a mano, con finestre di intervento più lunghe, non per scelta ma per struttura. Il risultato è che lo stesso dominio, nello stesso giorno, può risultare bloccato per un utente e ancora raggiungibile per un altro, e la differenza dipende da chi gli fa da provider, non da cosa fa l'utente.

La lista ha superato le dodicimila inibizioni ed è in crescita costante: chi gestisce siti illegali ne apre di nuovi appena uno viene bloccato, cambiando poche lettere del dominio o l'estensione. ADM rincorre, il gestore anticipa.

## Il vuoto che nessuno ha scritto

C'è un dettaglio tecnico noto a chi si occupa di reti ma quasi mai tradotto in termini operativi: chi usa un DNS diverso da quello del proprio provider, come Google o Cloudflare, bypassa il blocco senza fare nulla di illegale, spesso perché quel DNS era già configurato sul router per altri motivi. Non è questo il problema. È solo la conseguenza collaterale di un sistema che protegge l'indirizzamento standard, non tutti gli indirizzamenti possibili.

Il problema vero è un altro: nessuno ha scritto uno standard di tempo di propagazione uguale per tutti i provider italiani. ADM ordina il blocco. Non impone un termine massimo entro cui ogni operatore di rete deve renderlo operativo.

Vale il confronto con un altro fronte dello stesso decreto legislativo 41/2024: il limite di 100 euro settimanali sulle ricariche in contanti nei PVR, entrato in vigore a maggio con un sistema di controllo centralizzato sul codice fiscale del giocatore, uguale su tutta la rete nazionale. Lì lo standard c'è, uniforme per definizione perché passa da un unico sistema centrale. Sul fronte dei domini oscurati, lo stesso rigore non è mai arrivato: l'esecuzione resta affidata a decine di provider diversi, ciascuno con la propria velocità.

## Cosa cambia per chi lavora sul campo

Se lavori in brand protection, non dare per scontato che un dominio nella lista ADM sia irraggiungibile per tutti i tuoi utenti target. Verifica sui principali provider italiani, non solo su quello che usi tu per lavoro.

Se ti occupi di comunicazione di gioco responsabile, rivedi il linguaggio dei materiali informativi. "Il sito è bloccato" e "il sito è nella lista dei siti oscurati" non dicono la stessa cosa a chi legge, e solo la seconda è sempre vera.

Monitora le varianti di dominio, non solo l'originale già oscurato: un monitoraggio che si ferma al dominio noto arriva sempre in ritardo di un passo.

Se raccogli segnalazioni interne su siti clone, chiedi sempre quale provider usa chi segnala. Una segnalazione "il sito funziona ancora" può riferirsi a un provider che non ha ancora propagato il blocco, non a un fallimento del blocco stesso.

La newsletter completa, con il numero della settimana e la domanda operativa di chiusura, è disponibile su LinkedIn: [link].
