# Manutenzione del workspace — piano

> **Questo file è il piano, non il registro.** Le scadenze operative vivono su Linear (convenzioni in `linear-convenzioni.md`). Qui stanno le ricorrenze della manutenzione del sistema: skill, agenti, automazioni. Non i contenuti né i domini, che hanno le loro task list.

---

## Ricorrenze

> **Sezione letta da ALDO ogni lunedì mattina.** Per ogni riga sotto, se la ricorrenza cade nella settimana corrente e non esiste già una issue aperta con quel titolo e quella data, ALDO la crea su Linear (nessun progetto, label `ricorrente` + `admin`). A calendario diventa un blocco "Admin" (`time-blocking-regole.md`).
>
> **Formato vincolante:** stesse colonne delle altre task list. Le cadenze stanno solo qui, mai dentro un prompt di agente.

| Titolo issue | Cadenza | Giorno | Cosa controllare |
| --- | --- | --- | --- |
| Audit skill | trimestrale | primo lunedì di gennaio, aprile, luglio, ottobre; il primo è il 04/01/2027 | In una sessione Claude Code sul Mac personale: `python3 automations/skill-usage-audit.py`. Per ogni skill mai usata decidere se migliorarla, fonderla o archiviarla in `archive/legacy-skill-drafts/`, mai cancellare senza conferma. Guardare anche i plugin dell'account in `~/.claude/plugins/synced/` e quelli mai usati. Trenta minuti |

Aggiunta il 30/09/2026 (piano `../plans/2026-09-30-igiene-skill-versioning-audit-uso.md`). Trimestrale e non mensile perché l'uso di una skill si giudica su un trimestre, e perché ogni rito in più nella settimana è un rito che si rischia di abbandonare. Lo storico delle sessioni di Claude Code è tenuto 120 giorni (`cleanupPeriodDays` in `~/.claude/settings.json`), quindi copre il trimestre con un margine se l'audit slitta di qualche settimana.
