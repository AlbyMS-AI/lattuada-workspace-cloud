# ADM dice bloccato. Il tuo provider decide quando.

Il sito è nella lista dei domini oscurati da ADM. Sulla carta, irraggiungibile. Nella pratica, dipende da chi ti fa da provider e da che giorno chiedi.

## Cosa succede davvero quando ADM blocca un sito

Il meccanismo agisce sul DNS, cioè sull'indirizzamento, non sul contenuto. Quando un utente digita il dominio oscurato, il provider lo reindirizza alla pagina di avviso ADM invece che al sito vero. Il server estero, dall'altra parte, continua a funzionare tale e quale a prima. Non è stato tolto niente da internet. È stato tolto un cartello stradale, non demolito l'edificio.

I grandi provider italiani hanno procedure automatizzate che propagano un nuovo blocco in poche ore. I provider minori lavorano spesso a mano, con finestre di intervento più lunghe: non per scelta, per struttura. Il risultato è che lo stesso dominio, nello stesso giorno, può risultare bloccato per un utente e ancora raggiungibile per un altro, e la differenza non dipende da cosa fa l'utente, dipende da chi gli fa da provider.

La lista ha superato le dodicimila inibizioni. Cresce di continuo perché chi gestisce i siti illegali ne apre di nuovi appena uno viene bloccato, cambiando poche lettere del dominio o l'estensione. ADM rincorre, il gestore anticipa. È una lista che documenta il passato, non una barriera che ferma il presente. E ogni voce nuova che entra in quella lista è la prova che quella precedente non ha chiuso niente, ha solo spostato il problema su un altro indirizzo.

## La parte che nessuno sottolinea

C'è un dettaglio tecnico che circola tra chi si occupa di reti, ma quasi nessuno nel settore lo traduce in termini operativi: chi usa un DNS diverso da quello del proprio provider, come Google o Cloudflare, bypassa il blocco senza fare nulla di illegale e senza nemmeno saperlo, spesso perché quel DNS era già configurato sul suo router per altri motivi, tipo velocità o privacy. Non serve un profilo tecnico per farlo. Basta un'impostazione che tanti dispositivi propongono già di default, o un consiglio letto su un forum qualsiasi per motivi che non hanno niente a che fare con il gioco.

Questo non fa di chi lo usa un utente che sta cercando di aggirare l'oscuramento. È solo la conseguenza collaterale di un sistema che protegge l'indirizzamento standard, non tutti gli indirizzamenti possibili.

Il problema vero, però, è un altro: nessuno ha scritto uno standard di tempo di propagazione uguale per tutti i provider italiani. ADM ordina il blocco. Non impone un termine massimo entro cui ogni operatore di rete deve renderlo operativo. Il vuoto non è nella tecnologia, che esiste ed è collaudata da anni. È nella regola che dovrebbe imporre a tutti la stessa velocità, e che oggi non esiste.

Confronta con un altro fronte dello stesso decreto: il limite di 100 euro settimanali sulle ricariche in contanti nei PVR, entrato in vigore a maggio con un sistema di controllo centralizzato sul codice fiscale del giocatore, uguale su tutta la rete nazionale. Lì lo standard c'è, ed è uniforme per definizione perché il controllo passa da un unico sistema centrale. Sul fronte dei domini oscurati, lo stesso rigore non è mai arrivato: l'esecuzione resta affidata a decine di provider diversi, ciascuno con la propria velocità.

Questo scarica il costo su chi gestisce brand protection e comunicazione di gioco responsabile, che si trovano a lavorare su un'infrastruttura a due velocità senza saperlo. Un provider minore che impiega giorni a propagare un blocco non sta violando niente. Sta operando dentro un sistema che non gli ha mai chiesto di fare meglio, e che quindi non gli ha mai dato gli strumenti o l'obbligo per farlo. Chi ne paga il prezzo è chi, dall'altra parte, ha comunicato al proprio pubblico che quel sito "è bloccato" come se fosse un fatto uguale ovunque, in ogni momento, per chiunque lo cerchi.

## Cosa cambia da domani

Se lavori in brand protection, non dare per scontato che un dominio nella lista ADM sia irraggiungibile per tutti i tuoi utenti target. Verifica sui principali provider italiani, non solo su quello che usi tu per lavoro.

Se ti occupi di comunicazione di gioco responsabile, rivedi il linguaggio dei materiali informativi. "Il sito è bloccato" e "il sito è nella lista dei siti oscurati" non dicono la stessa cosa a chi legge, e solo la seconda è sempre vera.

Monitora le varianti di dominio, non solo l'originale già oscurato. Chi gestisce siti illegali ne registra di nuovi appena uno viene bloccato: un monitoraggio che si ferma al dominio noto arriva sempre in ritardo di un passo.

Se raccogli segnalazioni interne su siti clone o non autorizzati, chiedi sempre quale provider usa chi segnala. Una segnalazione "il sito funziona ancora" può essere corretta e riferirsi a un provider che non ha ancora propagato il blocco, non a un fallimento del blocco stesso: due letture diverse dello stesso messaggio, e solo una delle due porta a un'azione utile.

Se gestisci compliance per un provider di rete, anche piccolo, verifica i tuoi tempi di propagazione delle regole ADM rispetto ai grandi operatori. Nessuno te lo chiede ancora per norma. Ma un divario misurabile, il giorno in cui qualcuno decide di misurarlo, diventa un problema che oggi puoi ancora anticipare.

## Il numero della settimana

31,9%. È la percentuale di italiani sopra i quattordici anni che nel 2024 ha giocato soldi almeno una volta, secondo il rapporto ISTAT "Giochi e Videogiochi" pubblicato a inizio settembre. Sono 16 milioni e 609mila persone. Ma solo il 4,7% ha scommesso su sport. Il gioco più praticato resta il Gratta e Vinci, al 25,1%.

Hai mai verificato se un sito che pensavi bloccato lo sia davvero sul provider dei tuoi utenti, o te lo sei solo dato per scontato?

---

**Note di produzione (non pubblicare):**

- Fatto e meccanismo tecnico da Mondo3.com (08/09/2026), analisi sui blocchi ADM e su come i provider li applicano. Dato "oltre 12.000 inibizioni" e riferimento al blocco di 190 domini con scadenza 20/08/2026 già citati nel pezzo Bottadiculo del 18/08 (confronto Brasile), qui usati solo come contesto numerico, non come fatto centrale: il nucleo di questa edizione è il meccanismo di propagazione e il vuoto normativo sullo standard di tempo, materiale nuovo non trattato in quel pezzo.
- Angolo distinto dal fatto Jamma della stessa settimana (proroga certificazione ADM/OdV, tema completamente diverso: certificazione tecnica dei giochi, non oscuramento domini).
- ISTAT, rapporto "Giochi e Videogiochi" (dati 2024), ripreso da Jamma.it il 03/09/2026, dati citati identici alla fonte.
- ⚠️ Fact-check da fare prima della pubblicazione: verificare su fonte ADM primaria (non solo Mondo3.com) il meccanismo DNS e l'assenza di uno standard di propagazione, se possibile trovare un documento ADM che lo confermi esplicitamente.
- Spot-check anti-detection: da fare su pangram.com o QuillBot prima dell'invio.
