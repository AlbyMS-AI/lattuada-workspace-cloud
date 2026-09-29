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

Prima stesura del 28/09/2026, revisionata il 29/09/2026 dopo un check Codex high-effort (voto 5,5/10 sulla prima stesura). Ogni punto segnalato da Codex è stato riverificato sulle pagine live prima di correggerlo: Codex aveva lavorato in parte su copie indicizzate, perché molte pagine del sito andavano in timeout. Manca ancora il check Astra.

### Correzioni dopo il check Codex (29/09/2026)

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

### Punti aperti

- **Compliance AGCOM** (delibera 132/19/CONS): Codex segnala di nuovo il rischio di pubblicità indiretta legato a CTA, voto, "Perché scegliere" e "Le migliori alternative". Come deciso da Alberto il 13/09/2026 per la serie, il presidio è il passaggio dal caporedattore prima della pubblicazione: nessuna modifica in autonomia
- **Temi delle recensioni Trustpilot** (conti bloccati dopo vincite, prelievi lenti, accesso al conto, giochi "truccati"): verificati come presenti nelle recensioni, non come fatti. Non riportati nel testo perché Alberto non ne ha riscontro diretto e riguardano soldi degli utenti: da decidere con Alberto se citarli in forma neutra
- **Non verificati**: disponibilità di My Lotteries PLAY su Android, streaming, bonus attuali di Sisal e Lottomatica

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
