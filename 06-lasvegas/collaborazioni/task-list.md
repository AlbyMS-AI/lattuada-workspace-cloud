# Piano — Collaborazioni LasVegas

> **Questo file è il piano, non il registro.** Dal 01/09/2026 le scadenze operative vivono su Linear, progetto **LasVegas**. Qui restano il ragionamento, i blocchi noti, i workflow da costruire e le ricorrenze che ALDO legge ogni lunedì.
>
> Se cambia qualcosa: aggiorna prima questo file, poi lancia `/agenda` per riallineare Linear. Convenzioni: `../../automations/linear-convenzioni.md`.
>
> Aggiornato: 2026-09-01. Prima di oggi era fermo al 12/07/2026, con due task datati "metà agosto" mai fatti e cinque revisioni ricorrenti che non esistevano in nessun sistema di promemoria. È uno dei due casi che hanno motivato `plans/2026-09-01-sistema-task-unico-linear-assistente.md`.

---

## PRIORITÀ ALTA — Azioni immediate

- [x] **Codice affiliazione GoldBet** — confermato: **Edisonsrl21** (27/06/2026)
- [x] **Ciclo sala virtuale "chiudo e apro 20 gg"** — meccanismo chiarito con Luigi (29/06/2026)
- [~] **Quantificare proposta Stefano Peduzzi** — definire valore per: 3 incontri con giocatori + intervista + presenza. Fee? In kind? % GGR? — **derubricato (02/08/2026)**: non più prioritario per ora, tolto dal tracker attivo

---

## GOLDBET

- [x] **Strutturare workflow onboarding giocatore Goldbet** — dal primo contatto alla segnalazione bonus slot (300€ / 1.500€). Costruito in `workflows/` — chiuso (06/07/2026)
- [~] **Definire meccanismo poker giovedì** — password dedicata, chi invitare, come comunicarlo, follow-up — **derubricato (02/08/2026)**: non più prioritario per ora, tolto dal tracker attivo
- [~] **Chiarire massimali ippica + sport** — chiedere al referente Goldbet i limiti bonus su ippica e sport — **derubricato (02/08/2026)**: non più prioritario per ora, tolto dal tracker attivo

---

## BETFLAG

- [~] **Fissare call Betflag per Exchange** — obiettivo: personalizzazioni possibili su Exchange, ippica, casinò — **derubricato (02/08/2026)**: non più prioritario per ora, tolto dal tracker attivo
- [~] **Analizzare bonus Betflag** — URL: https://info.betflag.it/promozioni-e-bonus/ — estrarre meccaniche, confrontarle con Goldbet, identificare leve di personalizzazione — **derubricato (02/08/2026)**: non più prioritario per ora, tolto dal tracker attivo
- [~] **Mappare opportunità personalizzazione Betflag** — dopo analisi bonus: quali si possono customizzare per la rete? — **derubricato (02/08/2026)**: non più prioritario per ora, tolto dal tracker attivo

---

## LASVEGAS DIRETTI

- [ ] **Progettare campagna dormienti LasVegas** → **ALB-108** — identificare segmento (ultimi X mesi senza gioco), canale (WhatsApp/email/DM), offerta, CTA. Era datato "metà agosto (14-16/08)", mai fatto. ⚠️ Su Linear è senza scadenza: serve la data reale da Alberto, non una inventata
- [ ] **Mappare community mancanti** → **ALB-109** — lista community di giocatori non ancora nella rete, prioritizzate per verticale (poker, slot, sport, ippica). Stessa situazione: era "metà agosto", ⚠️ senza scadenza su Linear in attesa della data di Alberto

---

## Ricorrenze

> **Sezione letta da ALDO ogni lunedì mattina.** Per ogni riga sotto, se la ricorrenza cade nella settimana corrente e non esiste già una issue aperta con quel titolo e quella data, ALDO la crea su Linear (progetto LasVegas, label `ricorrente`).
>
> **Formato vincolante:** non cambiare le colonne senza aggiornare anche lo STEP 5 del prompt di ALDO. Le cadenze stanno solo qui, mai dentro un prompt: è la regola nata dai falsi allarmi di OTTO del 31/08/2026.
>
> Cadenza a calendario, non legata al comportamento del singolo giocatore. Testi in `../strategia/messaggi-educativi-giocatore-sostenibile.md`, trigger di dettaglio in `../strategia/piano-conversione-bonus-abuser.md`.

| Titolo issue | Cadenza | Giorno | Cosa controllare |
|---|---|---|---|
| Rollover chiusi settimana precedente → Messaggio 1 | settimanale | lunedì | Chi ha chiuso il rollover nella settimana precedente |
| Inattivi 3+ giorni post-bonus → Messaggio 2 | settimanale | lunedì | Giocatori fermi da almeno 3 giorni dopo il bonus |
| Nuovi ingressi con conto GoldBet preesistente → Messaggio 4 | quindicinale | lunedì, ancora 07/09/2026 | Chi entra avendo già un conto GoldBet |
| Soglia cashback 2.000€ superata → Messaggio 3 | mensile | ultimo giorno del mese | Chi ha superato i 2.000€ di NGR |
| Tier alti 1.500€+ con pattern a picchi → Messaggio 5 | mensile | ultimo giorno del mese | Solo profili "Value player", **mai** profili "Rischio RG" |

**Ancora della quindicinale:** 07/09/2026 è un lunedì. Da lì, ogni due settimane. L'ancora sta qui e non nel prompt di ALDO proprio perché è un dato, non una regola di comportamento.

**Vincolo su tutte:** nessuna promessa di vincita garantita, nessun targeting di soggetti vulnerabili. Il Messaggio 5 non va mai su profili "Rischio RG".

### Storico (chiuso)

- [x] **Messaggio 0 — primo invio** (01/08/2026): inviato come post al gruppo Telegram generale (tutti i potenziali giocatori + iscritti già registrati), non come messaggio 1:1 di onboarding come da disegno originale. Deviazione dal workflow: `onboarding-goldbet.md` Step 1bis resta valido per i nuovi ingressi 1:1, il gruppo è stato un lancio aggiuntivo per la base già esistente.
- [x] **Video HeyGen Messaggio 0** — prodotto e condiviso (01/08/2026), script in `../strategia/video-script/script-messaggio-0.md`, mai su profili "Rischio RG"

---

## DA COSTRUIRE (workflow)

- [x] Workflow onboarding giocatore Goldbet — chiuso 06/07/2026
- [ ] Workflow riattivazione dormienti LasVegas
- [ ] Workflow gestione poker giovedì
- [ ] Workflow valutazione ambassador (Peduzzi come template)

---

## NOTE / BLOCCHI

| Task | Bloccante |
|---|---|
| Bonus slot Goldbet 300€/1.500€ | Richiede segnalazione manuale → serve numero o username giocatore |
| Cashback mensile | NGR minimo 2.000€ — da comunicare chiaramente ai giocatori |
| "APRO CHIUDO MEMLO DA" | Significato non chiaro — rischio scadenza non rispettata |
