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

Nessuna voce ancora — il ciclo mer/ven parte il 09/09/2026 (prima settimana a regime).
