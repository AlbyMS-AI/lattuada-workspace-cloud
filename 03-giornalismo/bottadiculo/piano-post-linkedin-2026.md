# Piano Editoriale — Post LinkedIn Bottadiculo (mercoledì e venerdì)

**Creato:** 7 settembre 2026
**Uscita:** ogni mercoledì e venerdì
**Piano gemello:** `piano-newsletter-linkedin-2026.md` — stessa testata, stesso registro, ciclo diverso. La newsletter del lunedì resta il pezzo di punta della settimana, questo ciclo lo affianca senza mai ripeterlo.

---

## Identità

**Cosa sono questi pezzi.** Post LinkedIn Bottadiculo da 150-300 parole, stesso meccanismo editoriale della testata (`guidelines.md`), sempre con grafica. Non sono newsletter: niente SEO companion, niente versione blog, niente post di supporto separato — sono l'unità finita.

**Lettore:** lo stesso della testata — affiliati, compliance operativa, PVR, operatori di sala, professionisti iGaming mid-level.

**Cosa li distingue dalla newsletter.** La newsletter nasce dal fatto più forte della settimana, scelto al lock del giovedì con la regola di assegnazione a tre canali, e ha lo scheletro fisso con le due rubriche ("Cosa cambia da domani", "Il numero della settimana"). Questi due post nascono da un meccanismo più leggero: seguono la stessa "domanda sotto la domanda" ma in formato compresso, sull'angolo operativo del giorno.

---

## Fonte dei temi

**Primaria: PIERO.** Stessa rassegna che alimenta il ciclo Jamma, angoli già filtrati per Bottadiculo. Si lancia la mattina stessa della pubblicazione: rassegna → scelta angolo → verifica non sovrapposizione → scrittura → fact-check → umanizzazione → grafica, in un'unica sessione.

**Riserva: banca temi.** Se la rassegna del giorno non produce nulla di utilizzabile, si pesca da `banca-temi.md` (target 5 schede, vedi nota lì).

**Se nessuna delle due fonti produce un tema valido**, il post salta. Vale la stessa regola del ciclo Jamma: un'uscita persa e dichiarata è meglio di un post senza angolo vero.

---

## Non sovrapposizione

Prima di scegliere il tema, controllo in due punti:

1. **`../articoli-pubblicati.md`, ultimi 7 giorni**, tutte le testate — compresa la newsletter LinkedIn personale di Alberto.
2. **Il tema scelto per il pezzo Jamma dello stesso giorno**, quando entrambi i cicli pescano dalla rassegna PIERO della stessa mattina: mai lo stesso fatto sui due canali nello stesso giorno, stessa regola già in vigore tra le due newsletter del lunedì.

---

## LinkedIn — applicazione a una pagina editoriale

`../../04-linkedin/CLAUDE.md` descrive l'algoritmo e le best practice LinkedIn per il personal brand di Alberto. Quello che vale anche per una pagina editoriale come Bottadiculo, senza cambiare le regole di voce già in `guidelines.md`:

- **360Brew e i salvataggi.** Vale lo stesso principio: salvataggi e inoltri privati pesano più di like e commenti. I post di questo ciclo devono dare al lettore operativo qualcosa da tenere da parte (un dato, una checklist implicita, una sintesi), non solo un'opinione da commentare
- **Orari.** Mercoledì 11:00-16:00 (stessa fascia indicata per i caroselli, buona anche per un post con immagine). Venerdì mattina, prima che cali l'attenzione del pomeriggio — non a ridosso del weekend
- **No hashtag, no emoji fuori dalla regola già in `guidelines.md`.** Bottadiculo ammette un emoji con parsimonia quando rinforza il punto: resta così, non diventa "mai" solo perché è la regola del profilo personale di Alberto. Sono due voci editoriali distinte, la nota resta scritta qui per evitare che si confondano in futuro
- **CTA in chiusura sempre esplicita**, come da `guidelines.md`: "salvati questo post", "giralo al team", o rimando alla newsletter quando pertinente

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

**Checkpoint: lunedì 12/10/2026**, insieme al checkpoint già fissato nel piano newsletter.

---

## Valvola di sicurezza

Stesso principio del ciclo Jamma: il carico si somma a un calendario già pieno.

1. **Salta prima il post di venerdì**, poi eventualmente quello di mercoledì solo in casi eccezionali.
2. **La newsletter del lunedì non salta mai** per fare spazio a un post di questo ciclo.
3. Un'uscita saltata resta visibile come issue Linear non chiusa (vedi `../task-list.md`).

Se dopo il rodaggio (checkpoint 12/10) il carico si rivela insostenibile, la prima leva è ridurre a 1×/settimana, non comprimere qualità del testo o saltare la grafica.

---

## Grafiche

**Sempre.** Ogni post di questo ciclo produce una main image, nessuna eccezione salvo istruzione esplicita di Alberto — vedi `workflows/post-linkedin.md`, Step 5, e il template fisso `../../04-linkedin/grafiche/src/templates/bottadiculo-post-template.html`.

Cosa cambia a ogni post: kicker (il tema del pezzo), H1 (l'hook, la frase che ferma lo scroll). Cosa resta fisso: icona di marca, palette, layout. Stessa logica già validata il 06/09/2026 sulla main image della newsletter: nessuna illustrazione Gemini per-edizione, template compilabile in pochi minuti.

---

## Output per edizione

| File | Quando |
|---|---|
| `drafts/AAAA-MM-GG-[slug].md` | Stesso giorno di pubblicazione |
| `../../04-linkedin/grafiche/[data]-[slug]-cover.png` | Stesso giorno, dal template |

Dopo la pubblicazione, confermata da Alberto: riga in `../articoli-pubblicati.md`, tabella unica ordinata per data decrescente.

---

## Cosa questo ciclo non fa

- Non produce il set completo della newsletter (SEO companion, post di supporto, versione blog): qui il post è l'unità finita
- Non esce senza grafica
- Non esce senza controllo di non sovrapposizione sui 7 giorni precedenti e sul pezzo Jamma dello stesso giorno
- Non esce senza fact-check e umanizzazione, anche in 150-300 parole
- Non sacrifica la newsletter del lunedì per reggere il ritmo mer/ven
