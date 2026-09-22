# Task List — Giornalismo (Jamma, Bottadiculo, Sitiscommesse)

Piano operativo del dominio, non registro: contiene la cadenza delle uscite ricorrenti. Le
scadenze azionabili vivono su Linear (progetto Giornalismo), lette da ALDO ogni mattina; qui sta
la cadenza, non il calendario riga per riga di ogni singola pubblicazione — quello vive nei piani
di ciascuna testata (`jamma/piano-newsletter-linkedin-2026.md`, `jamma/piano-approfondimenti-2026.md`,
`bottadiculo/piano-newsletter-linkedin-2026.md`, `bottadiculo/piano-post-linkedin-2026.md`).

Creato il 07/09/2026, insieme al ciclo mer/ven di Jamma e Bottadiculo. Le due newsletter del
lunedì esistevano già ma non erano tracciate come ricorrenza su Linear: chiuso lo stesso gap
in questo file, non solo per le uscite nuove.

---

## Ricorrenze

> **Sezione letta da ALDO ogni lunedì mattina.** Per ogni riga sotto, se la ricorrenza cade nella
> settimana corrente e non esiste già una issue aperta con quel titolo e quella data, ALDO la crea
> su Linear (progetto Giornalismo, label `contenuto` + `ricorrente`).
>
> **Formato vincolante:** non cambiare le colonne senza aggiornare anche lo STEP di ALDO che le
> legge. Le cadenze stanno solo qui, mai dentro un prompt — stessa regola già in vigore per
> LasVegas dopo i falsi allarmi di OTTO del 31/08/2026.

| Titolo issue | Cadenza | Giorno | Cosa controllare |
|---|---|---|---|
| Newsletter Gioco & Business (Jamma) | settimanale | lunedì (pubblicazione 7:30, lock il giovedì precedente) | `jamma/piano-newsletter-linkedin-2026.md`, `jamma/banca-temi.md` |
| Newsletter Gambling Insights (Bottadiculo) | settimanale | lunedì (pubblicazione 7:30, lock il giovedì precedente) | `bottadiculo/piano-newsletter-linkedin-2026.md`, `bottadiculo/banca-temi.md` |
| Articolo approfondimento Jamma | settimanale | mercoledì | `jamma/piano-approfondimenti-2026.md`; controllo non sovrapposizione su `articoli-pubblicati.md`, ultimi 7 giorni |
| Articolo approfondimento Jamma | settimanale | venerdì | `jamma/piano-approfondimenti-2026.md`; controllo non sovrapposizione su `articoli-pubblicati.md`, ultimi 7 giorni |
| Post LinkedIn Bottadiculo | settimanale | mercoledì | `bottadiculo/piano-post-linkedin-2026.md`; controllo non sovrapposizione su `articoli-pubblicati.md` e sul pezzo Jamma dello stesso giorno; grafica sempre inclusa |
| Post LinkedIn Bottadiculo | settimanale | venerdì | `bottadiculo/piano-post-linkedin-2026.md`; controllo non sovrapposizione su `articoli-pubblicati.md` e sul pezzo Jamma dello stesso giorno; grafica sempre inclusa |

**Titolo issue reale:** ALDO compila il titolo definitivo nel formato di `automations/linear-convenzioni.md`
(`[pubb. GG/MM] Formato Lingua — Titolo`) quando genera la issue della settimana — la colonna sopra
indica solo il tipo di contenuto, non esiste ancora un titolo specifico finché il tema non è scelto.

**Valvola di sicurezza (entrambi i cicli mer/ven):** se la settimana è troppo piena, salta prima
il pezzo di venerdì, poi eventualmente quello di mercoledì solo in casi eccezionali. Le due
newsletter del lunedì non saltano mai per fare spazio ai pezzi mer/ven.

---

## Storico

- **07/09/2026** — Prima applicazione delle ricorrenze via `/agenda`. Creata `ALB-114` (Articolo Jamma, pubb. 09/09), `ALB-115` (Articolo Jamma, pubb. 11/09), `ALB-116` (Post Bottadiculo, pubb. 09/09), `ALB-117` (Post Bottadiculo, pubb. 11/09), `ALB-118` (Newsletter Jamma, pubb. 14/09), `ALB-119` (Newsletter Bottadiculo, pubb. 14/09). Chiusa `ALB-110` (lock 03/09 per la newsletter del 07/09, già pubblicata) — risolve anche la nota lasciata aperta su quella issue il 02/09 ("popolare il progetto Giornalismo con le newsletter ricorrenti è una decisione ancora aperta").
- **17/09/2026** — La settimana 2 del ciclo mer/ven (16/09-18/09) non era mai stata creata su Linear (ALDO non l'ha popolata lunedì 14/09). Corretto via `/agenda`: creata `ALB-135` (Articolo Jamma, pubb. 16/09, già Done) e `ALB-136` (Post Bottadiculo, pubb. 16/09, già Done) retroattivamente per i due pezzi già pubblicati mercoledì; create `ALB-137` (Articolo Jamma, pubb. 18/09) e `ALB-138` (Post Bottadiculo, pubb. 18/09) per il venerdì, ancora da scrivere. Chiuse anche `ALB-118` e `ALB-119` (newsletter del 14/09), rimaste aperte per errore nonostante la pubblicazione confermata in `articoli-pubblicati.md`.
- **21/09/2026** — Le ricorrenze del lunedì (newsletter Jamma/Bottadiculo) e del mercoledì 23/09 non erano mai state create (ALDO non ha girato la ricorrenza). Corretto via `/agenda`: create `ALB-142` (Newsletter Jamma, pubb. 21/09, tema ancora da definire), `ALB-143` (Newsletter Bottadiculo "ADM dice bloccato. Il tuo provider decide quando.", pubb. 21/09, **già pubblicata, chiusa retroattivamente**, aggiunta a `articoli-pubblicati.md`), `ALB-144` (Articolo Jamma, pubb. 23/09) e `ALB-145` (Post Bottadiculo, pubb. 23/09). Audit scadenze passate: `ALB-137` (Articolo Jamma venerdì 18/09) ha un draft pronto (`jamma/drafts/2026-09-19-adm-proroga-certificazione-odv-collo-di-bottiglia.md`, scritto un giorno tardi) ma non ancora confermato pubblicato — resta aperta in attesa di conferma. `ALB-138` (Post Bottadiculo venerdì 18/09) non ha nessun draft: rinominata `[arretrato, era 18/09]`, decisione (recuperare o considerare saltato) lasciata ad Alberto.
