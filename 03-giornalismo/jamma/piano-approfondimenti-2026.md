# Piano Editoriale — Approfondimenti Jamma (mercoledì e venerdì)

**Creato:** 7 settembre 2026
**Uscita:** ogni mercoledì e venerdì
**Piano gemello:** `piano-newsletter-linkedin-2026.md` — stessa testata, stesso registro, ciclo diverso. I due piani si leggono insieme: la newsletter del lunedì resta il pezzo di punta della settimana, questo ciclo lo affianca senza mai ripeterlo.

---

## Identità

**Cosa sono questi pezzi.** Articoli Jamma.it da 1000-1400 parole, stesso meccanismo editoriale, stesso tono, stesse regole stilistiche della newsletter (`guidelines.md`, `../../01-tono-di-voce/anti-ai-checklist.md`) — **senza** le due rubriche fisse ("Il precedente internazionale", "Cosa deve decidere chi guida"), che restano un tratto distintivo solo della newsletter del lunedì. Nessuna grafica: solo testo, ottimizzato SEO.

**Lettore:** lo stesso della testata — top management, C-level, direzione compliance, chi decide su budget e strategia.

**Cosa li distingue dalla newsletter.** La newsletter nasce dal fatto più forte della settimana, scelto al lock del giovedì con la regola di assegnazione a tre canali. Questi due pezzi nascono da un meccanismo più leggero e più vicino alla notizia: **approfondiscono un tema che il settore sta già trattando** (comprese le news di Jamma stessa, scritte dalla redazione) **oppure portano un argomento nuovo** che nessuno ha ancora articolato. Non riportano mai la notizia: la espandono, ne cercano la struttura sotto, esattamente come richiede `guidelines.md` ("l'angolo diverso dalla concorrenza non è l'esclusiva sulla notizia, è la profondità sulla struttura").

**Cosa non sono.** Non sono un secondo ciclo di news: quello lo fa la redazione di Jamma.it. Non sono un doppione della newsletter: se il tema regge le due rubriche fisse e il respiro della newsletter, è un tema da newsletter, non da mer/ven — vale la stessa regola di smistamento già in uso tra Jamma e Bottadiculo ("se non si riesce a nominare una decisione vera, il tema era di Bottadiculo": qui, se il tema è abbastanza forte da riempire le due rubriche fisse, è un tema da lock del giovedì, non da questo ciclo).

---

## Fonte dei temi

**Primaria: PIERO.** La rassegna quotidiana (skill `piero`, 13 fonti RSS, filtro 48 ore su IT/BE/CZ/DE/IE) genera angoli già suddivisi per testata. È la fonte che ha storicamente alimentato la maggior parte degli articoli mer/ven di Jamma, verificabile in `../articoli-pubblicati.md`. Si lancia la mattina stessa della pubblicazione: rassegna → scelta angolo → verifica non sovrapposizione → scrittura → fact-check → umanizzazione, in un'unica sessione.

**Riserva: banca temi.** Se la rassegna del giorno non produce nulla che superi il controllo di non sovrapposizione, si pesca da `banca-temi.md` (target 4 schede, vedi nota lì). La banca resta pensata soprattutto per la newsletter, ma una scheda strutturale regge anche come approfondimento mer/ven quando serve.

**Se nessuna delle due fonti produce un tema valido**, il pezzo salta. Meglio un'uscita persa e dichiarata (visibile su Linear come issue non chiusa) che un pezzo scritto per riempire lo slot senza un angolo vero — è la stessa regola di `guidelines.md`: "un articolo senza angolo proprio non vale pubblicarlo su Jamma."

---

## Non sovrapposizione

Prima di scegliere il tema, controllo in due punti:

1. **`../articoli-pubblicati.md`, ultimi 7 giorni**, tutte le testate. Non solo Jamma: un tema già coperto da Bottadiculo o dalla newsletter personale di Alberto nella stessa settimana non si ripete qui con un angolo diverso, a meno che l'angolo sia davvero un livello di analisi in più, non una riformulazione.
2. **Le news di Jamma.it della settimana**, quelle scritte dalla redazione (non da questo ciclo). Se il pezzo approfondisce una notizia già coperta lì, deve aggiungere un livello di analisi che la notizia non aveva — mai limitarsi a riscriverla più lunga. Checklist già in `workflows/article-1000-1400.md`, Step 6: "qualcuno di Jamma ha già scritto questo angolo? Se sì, trovane un altro."

---

## Calendario slot — 09/09 → 12/10

Il piano fissa i giorni, non i temi: si scelgono la mattina stessa dalla rassegna PIERO.

| Settimana | Mercoledì | Venerdì |
|---|---|---|
| 1 | 09/09 | 11/09 |
| 2 | 16/09 | 18/09 |
| 3 | 23/09 | 25/09 |
| 4 | 30/09 | 02/10 |
| 5 | 07/10 | 09/10 |

**Checkpoint: lunedì 12/10/2026**, insieme al checkpoint già fissato nel piano newsletter — un'unica sessione di revisione su tutto il sistema Jamma (newsletter + mer/ven), non due controlli separati.

---

## Valvola di sicurezza

Il carico aggiuntivo di questo ciclo si somma a un calendario già pieno (giovedì lock newsletter, venerdì scrittura, domenica rifinitura, lunedì pubblicazione, più turni e Softswiss). Se una settimana è troppo piena:

1. **Salta prima il pezzo di venerdì**, poi eventualmente quello di mercoledì solo in casi eccezionali.
2. **La newsletter del lunedì non salta mai** per fare spazio a un pezzo di questo ciclo: resta il pezzo di punta della settimana.
3. Un'uscita saltata resta visibile come issue Linear non chiusa (vedi `../task-list.md`), non sparisce in silenzio.

Se dopo il rodaggio (checkpoint 12/10) il carico si rivela insostenibile anche con la valvola attiva, la prima leva da considerare è ridurre a 1×/settimana, non comprimere la qualità dei due pezzi.

---

## SEO

Ogni pezzo di questo ciclo segue la sezione SEO aggiunta a `workflows/article-1000-1400.md` (Step 3bis): H1 con keyword del tema, H2/H3 come affermazioni che contengono comunque una keyword correlata, meta title e meta description quando il pezzo va anche sul CMS, almeno un link esterno a fonte primaria e uno interno quando esiste un articolo Jamma correlato.

---

## Output per edizione

| File | Quando |
|---|---|
| `drafts/AAAA-MM-GG-[slug].md` | Stesso giorno di pubblicazione |

Nessun file companion (no SEO separato, no grafiche, no versione blog): i campi SEO sono dentro l'articolo stesso. Dopo la pubblicazione, confermata da Alberto: riga in `../articoli-pubblicati.md`, tabella unica ordinata per data decrescente.

---

## Cosa questo ciclo non fa

- Non riporta una notizia come la redazione di Jamma.it: approfondisce o porta un tema nuovo
- Non usa le due rubriche fisse della newsletter
- Non produce grafiche
- Non esce senza controllo di non sovrapposizione sui 7 giorni precedenti
- Non esce senza fact-check e umanizzazione, mai, anche se il ciclo è più leggero della newsletter
- Non sacrifica la newsletter del lunedì per reggere il ritmo mer/ven
