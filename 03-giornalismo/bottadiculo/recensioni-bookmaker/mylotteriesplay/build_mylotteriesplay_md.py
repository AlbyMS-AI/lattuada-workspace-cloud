# -*- coding: utf-8 -*-
# Genera il .md sorgente dal contenuto condiviso e ci aggiunge le note fact-check,
# che restano solo qui: sono per Alberto e il caporedattore, non vanno nel docx/pdf.
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
import content as c

OUT = os.path.join(HERE, "recensione-mylotteriesplay-2026.md")

FACT_CHECK = """## Note fact-check

Prima stesura del 28/09/2026, revisionata il 29/09/2026 dopo un check Codex high-effort (voto 5,5/10 sulla prima stesura) e poi dopo il check Astra (#527, stesso giorno). Ogni punto segnalato è stato riverificato sulle pagine live prima di correggerlo.

### Correzioni dopo il check Astra (29/09/2026)

Astra non conosce le regole della serie: i punti sono stati filtrati. Applicati:

- **Concessione**: riformulata come "16049, in vigore dal 13/11/2025 con il nuovo regime; in precedenza GAD n. 15478", per non far sembrare incerta l'attuale. 16049 confermata anche nel footer di mylotteriesplay.it (curl diretto) e, secondo Astra, nell'elenco ADM dei concessionari (la pagina ADM non restituisce l'elenco al mio fetch)
- **Concessioni del gruppo precisate**: la formula "le società del gruppo sono concessionarie" era ambigua. Ora: concessionario per le lotterie istantanee e differite (Gratta e Vinci e Lotteria Italia), testo di brightstarlottery.it/chi-siamo (fetch diretto), e per Lotto, 10eLotto, MillionDAY e FAI3 FAI4 attraverso LottoItalia, 61,5% (lotto-italia.it, fetch diretto). Non nominata Lotterie Nazionali S.r.l., trovata solo in risultati di ricerca
- **Rollover**: ora riportato con la formula del regolamento, "moltiplicatore di giocata 45x sui Fun Bonus erogati" e "massimale di conversione del 50%". La prima revisione interpretava il 50% come "metà dell'importo": due letture della stessa pagina davano formulazioni diverse, quindi resta la dicitura contrattuale
- **Bonus Multipla**: percentuale calcolata sulla vincita netta (esempio nel regolamento), scaglioni 3% con 4 eventi, 25% con 10, 89% con 20, 650% con 30; riserva di modifica o sospensione. Il regolamento non dice se l'importo è in denaro o bonus, né indica un tetto in euro: non scritto
- **App Store**: Astra e Codex vedono 3,7/5 su 23. L'API ufficiale iTunes (lookup, country=it, 29/09/2026) dà averageUserRating 3,58333 e userRatingCount 24, e i dati strutturati della pagina dicono 3,6 e 24: mantenuto 3,6 su 24. Dalla stessa API: versione 1.0 del 27/04/2026, 1.0.1 del 17/06/2026, anno ora nel testo. **Da ricontrollare il giorno della pubblicazione**, come Trustpilot
- **Android**: le info essenziali ora dicono esplicitamente che la disponibilità di My Lotteries PLAY su Android non è verificata; l'app per iOS e Android è My Lotteries, quella solo lotterie
- **Comparativa**: tolta la riga licenze, perché lasciare "dato non verificato" la rendeva incompleta. Sisal 16020 compare in due fonti secondarie, ma sisal.it non risponde (timeout) e lottomatica.it risponde 403: nessun numero di concessione dei concorrenti pubblicato
- **"Garanzia di legalità"** sostituita: la concessione attesta l'autorizzazione, non garantisce esperienza o risultati. Stessa logica nella FAQ "è sicuro?"
- **Bonus e condizioni vicini**: il rating box ora dice "moltiplicatore 45x, non prelevabile" accanto ai 2.000€
- **Avvertenza**: il footer aggiunge "può causare dipendenza patologica". Vale la pena estenderla alle altre quattro recensioni
- **Notorietà**: precisato che riguarda My Lotteries Play come marchio di gioco online, non il gruppo
- **Trustpilot nei Contro**: "nel piccolo campione consultato prevalgono i giudizi negativi, che non rappresentano necessariamente l'esperienza di tutti i clienti"
- **Ripetizioni**: tolto dal giudizio finale il bonus sport mancante (resta nel box iniziale, nei Contro e nella sezione sport); tolta la chiusura generica della Prefazione; spiegazione del voto resa riconoscibile ("Come si arriva al voto")
- **Formule**: "sposta poco" diventa "incide poco"; "senza un conteggio pubblico dei titoli" diventa "numero aggiornato dei giochi non trovato"; "oltre 10 giochi di lotteria" diventa "oltre 10 tra lotterie e giochi numerici"
- **Nomi dei giochi**: controllati, "Super Win for Life", "FAI3 FAI4", "MillionDAY" e "Play Your Date" come nelle pagine ufficiali, usati in modo uniforme

Non applicati, con il motivo:

- **Revisione legale di CTA, link affiliati e natura promozionale** (Decreto Dignità art. 9, AGCOM): decisione di Alberto del 13/09/2026, il presidio per l'intera serie è il caporedattore. La dichiarazione di un eventuale rapporto di affiliazione dipende da un fatto che non conosco: da chiedere al caporedattore
- **Indice navigabile, link alle fonti nelle singole sezioni, tabelle per mobile, metadati SEO nel documento**: il formato della serie è il docx/pdf sul modello SNAI consegnato al caporedattore, che impagina sul CMS. Proposta SEO qui sotto, fuori dal testo
- **Riscrivere per i rilevatori AI**: coerente con la regola del workspace, si interviene su precisione e ritmo, non per battere un rilevatore
- **Ricontrollo il giorno della pubblicazione** (rating, Trustpilot, bonus): passaggio di processo, non modifica al testo. Va fatto quando il caporedattore fissa la data

### Proposta SEO per il caporedattore

- **SEO title**: Recensione My Lotteries Play 2026: bonus, lotterie e scommesse
- **Meta description**: My Lotteries Play, concessione ADM 16049: bonus di benvenuto da 25€ a 2.000€, Lotto, Gratta e Vinci, SuperEnalotto, scommesse sportive e pagamenti. Voto 3,5/5.
- **Slug**: recensione-my-lotteries-play

### Correzioni dopo il check Codex (29/09/2026)

Ogni punto segnalato da Codex è stato riverificato sulle pagine live prima di correggerlo: Codex aveva lavorato in parte su copie indicizzate, perché molte pagine del sito andavano in timeout.

- **Bonus di benvenuto, errore sostanziale corretto**: la prima stesura parlava di "tre offerte attive, fino a 50€". Il censimento completo della categoria "Bonus Benvenuto" su /bonus (fetch diretto) mostra tre offerte online: Slot 200% fino a 2.000€, Slot e Lotterie 100% fino a 50€, Lotterie 100% fino a 25€. La categoria "Bonus Benvenuto in Ricevitoria" ne mostra altre tre: Slot 50% fino a 20€, Lotterie 100% fino a 30€, Slot e Lotterie 50% fino a 40€. La prima stesura aveva letto solo le pagine uscite nei risultati di ricerca. Crollata la tesi dei "bonus piccoli": rivisti rating box, info essenziali, Pro, Contro, voto Bonus (da 6,5 a 7) e giudizio. I benvenuti Gratta e Vinci (15€) e Lotto (15€) sono ancora linkati dalla pagina bonus ma scaduti il 31/03/2026: esclusi
- **Regolamenti completati (fetch diretto su ogni pagina)**: Slot 2.000€, cinque tranche ogni 48 ore da massimo 400€, ognuna valida 2 giorni, rollover 45x su dieci slot, conversione massima del 50% in Real Bonus Slot entro 72 ore, da rigiocare almeno una volta, valido 72 ore, iniziativa 16/04 al 31/12/2026. Slot e Lotterie: Fun Bonus 10x con conversione fino al 100% in Real Bonus Slot da rigiocare una volta, valido 5 giorni. Bonus in ricevitoria: tutti "da rigiocare integralmente almeno una volta prima del prelievo", tutti validi 5 giorni, iniziative dal 27/05/2026 (Slot, Slot e Lotterie) e dal 18/08/2026 (Lotterie) al 31/12/2026. Scelta nel modulo di registrazione e unicità del benvenuto: FAQ bonus e regolamenti (fetch diretto). Non trovata sulla pagina Slot 2.000€ l'esclusione del bonifico, quindi non è scritta per quell'offerta
- **Conti rifatti**: 200% di 1.000€ = 2.000€ = 5 tranche da 400€; Slot e Lotterie con ricarica minima di 20€ = 10€ + 10€, massimo 25€ + 25€ con 50€; ricevitoria Slot e Lotterie 20€ + 20€ = 40€ (50% di 80€); media valutazioni (8,5 + 6 + 6,5 + 7 + 6 + 6,5 + 6 + 8,5) = 55, diviso 8 = 6,875, arrotondato a 6,9, pari a 3,44 su 5. Voto finale 3,5/5 dichiarato come sintesi editoriale, con il valore lineare esplicito nel testo
- **MillionDAY non è di Sisal, errore corretto**: la prima stesura, sulla base di uno snippet di ricerca, definiva Sisal "concessionario di SuperEnalotto e MillionDay". Su lotto-italia.it/chi-siamo (fetch diretto) MillionDAY è gestito da LottoItalia, consorzio guidato da Brightstar (61,5%), insieme a Lotto, 10eLotto e FAI3 FAI4. Sisal è concessionario del SuperEnalotto e dei giochi numerici a totalizzatore nazionale (sisal.com, ADM, Agipronews, da risultati di ricerca: sisal.com in timeout al fetch diretto). Il dato LottoItalia è ora anche nella Prefazione
- **Bonus Lottomatica tolto**: il bonus sport da 2.050€, ripreso dalla recensione Lottomatica, secondo Codex risulta in archivio sul sito Lottomatica, terminato l'08/06/2026. lottomatica.it risponde HTTP 403 sia via WebFetch sia via curl: non è stato possibile verificare né la scadenza né l'offerta attuale. Tolta l'intera riga bonus dalla comparativa, anche per Sisal
- **Rete Lottomatica riformulata**: "oltre 4.000 punti vendita scommesse e 1.100 sale gioco" è un dato del gruppo, non del solo marchio Lottomatica.it (verificato da Codex su lottomaticagroup.com; il sito del gruppo risponde 403 al mio fetch diretto). Il claim "Lottomatica unico brand con rete fisica" non è ripreso
- **Pagamenti**: la tabella ufficiale delle ricariche (/assistenza/cerca/ricarica/come-ricaricare, fetch diretto) elenca solo carte (da 10€ a 1.000€), PayPal (da 10€ a 950€) e bonifico ordinario e istantaneo (nessun minimo né massimo, spese bancarie, da 2 a 3 giorni lavorativi). **Tolti OnShop e MyBank**: OnShop veniva da una pagina di assistenza vecchia e non è nella tabella; MyBank compariva solo in una FAQ. Il deposito minimo non è più "10€" generico
- **Scommesse sportive**: la scheda App Store (fetch diretto) elenca discipline e mercati: la prima stesura diceva "discipline e mercati non dichiarati", affermazione estesa a tutto il sito partendo da poche pagine. Ora il testo riporta l'elenco della scheda e dichiara solo che non è stato verificato un conteggio completo. Voto sport da 5,5 a 6. Bonus Multipla (sport) aggiunto: pagina ufficiale, dal 3% con 4 eventi al 650% con 30, quota minima 1,25, fino al 31/12/2026; la pagina non dice se è riservato ai nuovi clienti, quindi il testo non lo dice. "Nessun bonus sport" ora è "nelle pagine bonus consultate non abbiamo individuato un bonus di benvenuto dedicato allo sport": la categoria Bonus Benvenuto (fetch diretto) contiene solo Slot, Slot e Lotterie, Lotterie
- **App**: versione 1.0 del 27 aprile, 1.0.1 del 17 giugno (anno non indicato in scheda). La FAQ sullo sport non lega più la disponibilità in app a febbraio 2026. Rating: il mio fetch del 29/09/2026 dà 3,6/5 su 24 valutazioni (due fetch concordi); Codex ha visto 3,7/5 su 23. Probabile differenza di istantanea: mantenuto 3,6 su 24 con data
- **My Club**: casinò live a 2 punti per euro (omesso nella prima stesura), nessun punto sulle frazioni di euro, conversione il primo giorno del mese successivo (regolamento, fetch diretto)
- **Registrazione**: tolti "residenza in Italia" (non dimostrata: la FAQ registrazione non la cita e secondo Codex il modulo elenca anche nazioni estere) e "sei passaggi" (non verificabile nell'interfaccia). Validazione entro 2 giorni e obbligo di conto validato per prelevare: FAQ registrazione (fetch diretto)
- **Brightstar**: nome annunciato il 17/06/2025, cessione Gaming e Digital prevista dal 01/07/2025 (comunicato su brightstarlottery.it, fetch diretto). La prima stesura sovrapponeva i due momenti. "Quasi cinquant'anni" è una dichiarazione del gruppo, attribuita come tale
- **Trustpilot**: la prima stesura neutralizzava troppo il dato ("chi lascia un giudizio negativo è sempre sovrarappresentato", "il punteggio non misura la qualità del servizio"). Ora: TrustScore 1,7/5 su 23 recensioni, quasi tutte a una stella, profilo non reclamato, nessun invito alla recensione inviato dall'azienda (avviso di Trustpilot, fetch diretto del 29/09/2026), campione piccolo e autoselezionato che segnala insoddisfazione tra chi ha recensito
- **Giudizio di Alberto concentrato**: nella prima stesura la notorietà tornava in Prefazione, Contro, Feedback, Giudizio e FAQ, in parte presentata come descrizione del mercato. Ora è in un solo passaggio attribuito (Contro), richiamato una volta nel Giudizio. La FAQ sul punto debole è sostituita da una domanda pratica sull'unicità del bonus. Tolti "conto solido", "gruppo affidabile" e "uno dei soggetti più strutturati": aggettivi non dimostrabili senza test
- **Claim negativi ristretti al perimetro verificato**: "nella pagina contatti consultata", "nelle pagine consultate", "nelle pagine bonus consultate". Tolto il rinvio interno "dettagliato in nota, in fondo", che il lettore del docx/pdf non vede
- **Stile**: decimali con la virgola; "febbraio 2026" ridotto da nove a tre occorrenze; "pre-match" sostituito da "prima dell'evento"

### Dati confermati da entrambe le verifiche

- Proprietà MyLotteries S.r.l., direzione e coordinamento Brightstar Lottery S.p.A., gruppo IVA Brightstar; concessione 16049, precedente GAD 15478; nuovo regime dal 13/11/2025 (anno ricavato dalla data del contratto di conto gioco)
- Lancio scommesse sportive: news ufficiale del 26/02/2026
- Oltre 100 Gratta e Vinci da 0,10€ a 25€, app My Lotteries per iOS e Android (pagina /mobile)
- Prelievi: carta da 10€ a 2.000€ in 24-48 ore, PayPal da 10€ a 8.000€, bonifico da 10€ senza massimo; tempi PayPal discordanti tra due pagine ufficiali, dichiarato nel testo; tetto online di 10.000€ settimanali (FAQ ricariche)
- Contatti: numero verde e due email, nessuna chat né orari nella pagina contatti
- Sisal acquisita da Flutter il 04/08/2022; Lottomatica concessione 16010; Goldbet 4,8/5 su circa 25.000 valutazioni (fetch dell'11/09/2026, riconfermato da Codex)

### Decisioni di Alberto sui punti aperti (29/09/2026)

- **Compliance AGCOM e Decreto Dignità** (segnalati di nuovo da Codex e Astra): presidio del caporedattore, come deciso il 13/09/2026 per la serie
- **Eventuale accordo di affiliazione**: non rilevante per il pezzo, nessuna dichiarazione da aggiungere
- **Ricontrollo dei dati prima dell'invio** (previsto a inizio ottobre): non necessario, i dati non dovrebbero cambiare in pochi giorni
- **Trustpilot**: poco peso. Tolto il richiamo dai Contro; in Feedback resta solo punteggio e dimensione del campione. I temi delle recensioni (conti bloccati, prelievi lenti) restano fuori
- **Non verificati**: disponibilità di My Lotteries PLAY su Android, streaming, bonus e concessioni attuali di Sisal e Lottomatica

**Giudizio personale di Alberto (28/09/2026)**: su domande mirate, il giudizio raccolto è il seguente. Reputazione: brand che deve ancora emergere, non "chiacchierato" dai giocatori, soprattutto online. Trattamento di vincenti e bonus abuser: nessun riscontro diretto. Apertura del conto in ricevitoria: conta poco. Il vero neo: non è un brand molto conosciuto, deve farsi conoscere online. Dopo la revisione del 29/09 questo giudizio compare in un solo passaggio attribuito (primo paragrafo dei Contro) e in un richiamo nel giudizio finale. Sul trattamento dei vincenti la recensione non dice nulla, né in positivo né in negativo, per assenza di riscontro. È opinione editoriale basata sull'esperienza diretta di Alberto nel settore, non un dato verificato su fonte primaria terza: va trattata come tale se il caporedattore ne chiede conto.
"""


def bullet(text):
    return f"- {text}"


lines = [f"# {c.HEADER.replace('  ', ' ')}", "", f"**{c.TITLE}**", c.SUBTITLE, "", c.CTA, "", "---", ""]
stars, t2, s2, t3, s3 = c.RATING
lines += [f"{stars} | {t2}: {s2} | {t3}: {s3}", ""]

for block in c.BLOCKS:
    kind, args = block[0], block[1:]
    if kind == "h1":
        lines += [f"## {args[0]}", ""]
    elif kind == "h2":
        lines += [f"### {args[0]}", ""]
    elif kind in ("body", "small"):
        lines += [args[0], ""]
    elif kind == "info":
        lines += ["| Campo | Dettaglio |", "|---|---|"] + [f"| {k} | {v} |" for k, v in args[0]] + [""]
    elif kind == "callout":
        lines += [f"### {args[0]}", ""] + [bullet(x) for x in args[1]] + [""]
    elif kind == "table":
        headers, rows = args[0], args[1]
        lines += ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
        lines += ["| " + " | ".join(r) + " |" for r in rows] + [""]
    elif kind == "avg":
        lines += [f"**{args[0]}**", ""]
    elif kind == "note":
        lines += [f"**{args[0]}**: {args[1]}", ""]
    elif kind == "final":
        lines += [f"## {args[0]}", ""]
    elif kind == "divider":
        lines += ["---", ""]

lines += [c.FOOTER, "", "---", "", FACT_CHECK]

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Salvato:", OUT)
