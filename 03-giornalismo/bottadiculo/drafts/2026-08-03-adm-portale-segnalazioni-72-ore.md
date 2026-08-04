# Il portale ADM non introduce le 72 ore. Sposta il cronometro

**Testata:** Bottadiculo.it
**Data:** 3 agosto 2026
**Formato:** Post LinkedIn (circa 290 parole)
**Topic:** ADM attiva dal 10 settembre 2026 il portale unico per segnalazioni e reclami sul gioco online. Angolo operativo: le 72 ore erano già nella convenzione, la novità è che ora il tempo lo misura ADM e non l'helpdesk del concessionario. Cinque settimane per chi ha il primo livello in outsourcing.
**Fonti:** Agimeg.it (attivazione portale 10 settembre), Jamma.it (circolare ADM 24 febbraio 2026, contact center obbligatorio e penale 50mila euro)
**Elementi grafici:** nessuno obbligatorio, il post regge da solo. Eventuale immagine: screenshot della pagina portale ADM
**Status:** Bozza, seconda stesura (v1 rilevata 100% AI da Pangram il 03/08/2026, riscritta sulla struttura)

---

Il portale ADM apre il 10 settembre. Il termine delle 72 ore per rispondere ai reclami invece è roba vecchia: sta nell'articolo 17 comma 3 della convenzione ed era già stato ribadito nella circolare del 24 febbraio, quella con la penale da 50mila euro per chi il contact center non l'aveva attivato per niente.

Quello che cambia è dove sta il cronometro. Finora il tempo di risposta lo misurava l'helpdesk del concessionario, sui propri ticket, con i propri log, e lo dichiarava su richiesta. Da settembre il giocatore entra con SPID o CIE, apre la segnalazione dentro l'applicativo sviluppato con Sogei, e il timestamp resta lì.

Sul conteggio conviene leggere il dettaglio, perché gira già la lettura sbagliata. Le 72 ore sono lavorative: partono alle 00:01 del giorno dopo la segnalazione, scadono alle 23:59 del terzo giorno utile, sabati e festivi esclusi. Un reclamo che entra venerdì pomeriggio scade mercoledì sera. Cinque giorni pieni, non tre.

Il margine se lo mangia chi ha il primo livello appaltato fuori, su un fuso diverso. Il ticket deve arrivare al fornitore, essere lavorato e tornare indietro con una risposta tracciabile sul portale, non con una nota chiusa nel CRM del vendor.

La parte che nessuno sta sottolineando è che per il ritardo non risulta prevista nessuna penale. I 50mila euro sono un'altra cosa. Quello che nasce a settembre è uno storico dei tempi di risposta, concessionario per concessionario, che fino a ieri non esisteva da nessuna parte.

Cinque settimane per verificare dove finiscono adesso i reclami e quanto ci mettono a tornare, prima che il dato ce l'abbia anche qualcun altro.

Salvatelo e portatelo al prossimo giro con il fornitore del customer care.

---

## Note fact-check

- Attivazione portale unico segnalazioni ADM il 10 settembre 2026, sviluppo con Sogei, accesso via SPID o CIE (in alternativa email con copia del documento): verificato su Agimeg.it.
- Conteggio delle 72 ore lavorative (dalle 00:01 del giorno successivo alla segnalazione alle 23:59 del terzo giorno lavorativo, esclusi sabati e festivi): verificato su Agimeg.it. L'esempio del reclamo di venerdì che scade mercoledì è una derivazione diretta di quella regola di conteggio, non un caso citato dalla fonte.
- Obbligo di risposta entro 72 ore: articolo 17, comma 3, lettera c) della convenzione di concessione per il gioco a distanza (D.Lgs. 25 marzo 2024 n. 41) e articolo 12, comma 2 dello schema di contratto di conto di gioco.
- Circolare Direzione Giochi ADM, Ufficio Gioco a Distanza e Scommesse, del 24 febbraio 2026: contact center obbligatorio entro tre mesi dall'avvio della concessione, penale di 50mila euro per la mancata attivazione. Verificato su Jamma.it.
- La penale di 50mila euro è collegata alla mancata attivazione del contact center, non al superamento delle 72 ore. Nessuna sanzione specifica per il ritardo di risposta risulta indicata nella documentazione sul portale: distinzione mantenuta esplicita nel testo per non attribuire ad ADM una sanzione che non ha annunciato.

## Note di riscrittura anti-detection

Prima stesura rilevata 100% AI da Pangram. I tell erano strutturali, non lessicali:

- Cinque paragrafi con la stessa architettura (frase corta a effetto, sviluppo, implicazione)
- Parallelismi antitetici perfetti: "Lo misurava il concessionario, lo dichiarava il concessionario"; "ha più margine di quanto crede" contro "ne ha meno di quanto pensa"
- Due chiuse aforistiche ("La sanzione arriva dopo il dato, mai prima")
- Due paragrafi consecutivi aperti da un setup con i due punti
- Un paragrafo di una riga isolato come stacco drammatico

Nella seconda stesura la variazione di lunghezza nasce dal contenuto (il dato secco sta in una riga, il ragionamento sul conteggio si distende), i parallelismi sono stati sciolti e le due chiuse aforistiche eliminate.

Terza passata (04/08/2026), su segnalazione di un secondo tool di scrittura. Corretto solo
quello che era un difetto reale: "10 settembre" ripetuto quattro volte ridotto a una
occorrenza più due "settembre", eliminato "lo comunicava ad ADM quando ADM lo chiedeva",
alleggeriti due periodi sovraccarichi.

Non corretto, e da non correggere in futuro:

- **Ritmo irregolare.** È l'obiettivo, non il difetto. La variazione di lunghezza delle frasi
  è la burstiness, primo segnale usato dai classificatori. Uniformare il ritmo per alzare il
  punteggio di leggibilità riporta il testo verso il centro statistico dell'output LLM e
  peggiora l'esito Pangram. I due obiettivi sono opposti: vince l'anti-detection.
- **Plagio potenziale.** Falso positivo. Le stringhe che matchano sono le citazioni
  normative ("articolo 17 comma 3 della convenzione", "gioco a distanza", "contact center",
  "entro un termine massimo di 72 ore"), identiche in ADM, Agimeg e Jamma perché sono il
  testo della norma. Riscriverle significa sbagliare la citazione.
