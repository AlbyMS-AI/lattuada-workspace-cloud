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

Verifica del 28/09/2026. A differenza di Goldbet, il sito ufficiale dell'operatore ha risposto al fetch diretto: quasi tutti i dati della recensione vengono da fonte primaria. Dove non è così, è indicato sotto.

- **Proprietà**: MyLotteries S.r.l., Viale del Campo Boario 56/D, Roma, P.IVA 17681931006, società a socio unico soggetta a direzione e coordinamento di Brightstar Lottery S.p.A., gruppo IVA Brightstar Lottery (P.IVA 16866691005). Fetch diretto su mylotteriesplay.it/chi-siamo (fonte primaria). **Non fa parte del Gruppo Lottomatica**: il device narrativo "stesso gruppo di Betflag, Planetwin365, Goldbet e Lottomatica" delle recensioni precedenti qui non si applica
- **Concessione**: n. 16049, subentrata alla GAD n. 15478. Fetch diretto su chi-siamo e sulla pagina "Nuova concessione" (fonte primaria). La pagina dice "dal 13 novembre" senza anno: l'anno 2025 si ricava dalla data di aggiornamento del contratto di conto gioco (13/11/2025, fetch diretto) ed è coerente con il cambio di regime già verificato su Goldbet, Lottomatica e Planetwin365
- **Brightstar Lottery**: denominazione assunta da IGT Lottery a giugno 2025 (il Giornale, 17/06/2025, fetch diretto), in coincidenza con la cessione delle attività gaming e digital di IGT a Voyager Parent, società controllata da fondi Apollo (closing previsto al 01/07/2025). Concessioni di gruppo in Italia per Lotto, Gratta e Vinci e Lotteria Italia: sito brightstarlottery.it (fetch diretto). Il "quasi cinquant'anni nel settore" è una frase dell'amministratore delegato riportata nello stesso articolo, per questo nel testo è attribuita al gruppo. Il numero di punti vendita della rete Brightstar è omesso: sul sito del gruppo compaiono due cifre diverse (oltre 58.000 punti vendita lotterie, oltre 45.000 ricevitori)
- **Bonus**: tutti e tre verificati con fetch diretto sulle pagine ufficiali dei singoli bonus (fonte primaria): Slot e Lotterie (iniziativa dal 16/04/2026 al 31/12/2026), Lotterie (dal 03/08/2026 al 31/12/2026), Lotterie in Ricevitoria (dal 18/08/2026 al 31/12/2026). Somma verificata: 25€ Fun Bonus + 25€ Real Bonus = 50€. Escluso il bonus Lotto/10eLotto/MillionDay (100% fino a 15€), scaduto il 31/03/2026, che alcune recensioni di terzi (casinolegali.net) presentano ancora come offerta attiva. Scartato anche il "bonus fino a 2.000€ + 200 free spin" di oddschecker.com, senza alcun riscontro sulle pagine ufficiali. Esclusa la promozione stagionale "Gratta e Vinci Week" (28/09 al 04/10/2026): non fa parte del benvenuto. Il "nessun requisito di puntata" sul Real Bonus Lotterie significa che le condizioni ufficiali non ne indicano uno, formulazione mantenuta nel testo
- **Scommesse sportive**: news ufficiale del 26/02/2026 (fetch diretto), pre-match e live, da desktop e mobile, "il calcio, ma non solo". Numero di discipline, mercati e streaming non indicati né nella news né nella pagina /scommesse (fetch diretto): per questo la categoria ha un voto prudente e il testo dichiara che non esprime giudizi su ciò che non si può verificare. "Non risulta un bonus sport" è un claim negativo: verificato sulla pagina /bonus (fetch diretto), che non ne mostra uno di benvenuto, formulato come "alla data di verifica non risulta"
- **Virtual**: discipline dalla pagina /virtual (snippet di ricerca sulla pagina ufficiale, non fetch diretto)
- **Casinò**: la pagina /casino (fetch diretto) non indica numero di titoli né fornitori. Casinolegali.net riporta 122 slot, 53 giochi live e 50 jackpot, ma è una fonte singola e parzialmente datata (bonus scaduto, app descritta come solo lotterie): cifre non pubblicate. Giochi di carte (Briscola, Tresette, Scopa) dalla pagina App Store (fetch diretto)
- **Gratta e Vinci**: oltre 100 titoli online, giocate da 0,10€ a 25€: pagina /mobile (fetch diretto)
- **Pagamenti**: tabella prelievi da /assistenza/cerca/prelievo/metodi-di-prelievo (fetch diretto). Ricariche: carte, PayPal, bonifico e OnShop da snippet delle pagine ufficiali di assistenza; MyBank dalla FAQ ricariche (fetch diretto). Tetto settimanale di 10.000€ dalla FAQ ricariche (fetch diretto). Deposito minimo 10€ da snippet della pagina ricariche, coerente con il minimo dei bonus Lotterie. **Discrepanza dichiarata nel testo**: per PayPal la tabella metodi indica "entro 24 ore", la pagina "come prelevare con PayPal" indica "entro 3 giorni lavorativi" previa verifica. Per MyBank e OnShop "non indicato tra i metodi di prelievo" e non "solo deposito": la pagina prelievi elenca solo carta, PayPal e bonifico
- **Registrazione**: pagina /registrazione (fetch diretto): due modalità, sei passaggi, documenti accettati, OTP, cellulare italiano. Sospensione a 48 ore dal contratto di gioco (fetch diretto). SPID e CIE non compaiono tra le modalità: nel testo non è scritto "SPID non disponibile" come claim negativo, ma sono descritte le due modalità previste
- **Apertura del conto in ricevitoria**: pagina del bonus dedicato (fetch diretto), "aprono un conto gioco presso uno dei nostri Punti Vendita"
- **Contatti**: pagina /contatti (fetch diretto): numero verde, due email. Orari e live chat non indicati nella pagina, formulato così nel testo
- **My Club**: pagina /programma-fedelta-my-club (fetch diretto). Punti: 10 per euro sulle lotterie, 5 per euro sugli altri giochi; moltiplicatori da x1 (Bronzo) a x4 (Diamante)
- **App**: My Lotteries PLAY su App Store, 3,6/5 su 24 valutazioni, versione 1.0.1, sviluppatore Brightstar Lottery S.p.A.: fetch diretto (fonte primaria), "valutazioni" e non "recensioni". App My Lotteries (solo lotterie) per iOS e Android: pagina /mobile (fetch diretto). Disponibilità di My Lotteries PLAY su Android non verificata, dichiarato in nota metodologica
- **Trustpilot**: 1,7/5 su 23 recensioni, 96% a una stella, profilo non rivendicato: fetch diretto su it.trustpilot.com. **Non riportate** le accuse ricorrenti nelle recensioni (conti bloccati dopo vincite, prelievi lenti, giochi "truccati"): su 23 recensioni non hanno peso statistico e Alberto non ne ha riscontro diretto. Nel testo resta solo il punteggio, letto come segnale di scarsa presenza online e non come misura del servizio
- **Sisal**: proprietà Flutter dal 04/08/2022 (comunicato Sisal e AGIMEG, da risultati di ricerca), concessionario di SuperEnalotto e MillionDay (fonti di stampa convergenti). Bonus e numero di concessione non verificati: sisal.it in timeout, oddschecker e sportytrader bloccati con HTTP 403. Gli snippet indicano un bonus lotterie fino a 50€ e la concessione GAD 16020 da fonte singola: non pubblicati, "dato non verificato alla data di aggiornamento"
- **Lottomatica** (comparativa e alternative): concessione 16010, rete di oltre 4.000 agenzie e 1.100 sale, bonus sport 2.050€ riutilizzati dalla recensione Lottomatica. Il bonus in quella sede era stato ricostruito da fonti secondarie convergenti, non da fetch diretto: stesso livello di confidenza qui. Il claim "Lottomatica unico brand del gruppo con rete fisica" **non** è ripreso
- **Goldbet** (alternative): 4,8/5 su circa 25.000 valutazioni App Store, fetch diretto dell'11/09/2026 nella recensione Goldbet
- **Controlli aritmetici**: media valutazioni (8,5 + 5,5 + 6,5 + 6,5 + 6 + 7 + 6 + 8,5) / 8 = 6,81, arrotondata a 6,8; 6,8/10 in scala lineare = 3,4/5, voto finale 3,5/5 dichiarato come sintesi editoriale. Bonus Slot e Lotterie 25 + 25 = 50€

**Giudizio personale di Alberto (28/09/2026)**: su domande mirate, il giudizio raccolto è il seguente. Reputazione: brand che deve ancora emergere, non "chiacchierato" dai giocatori, soprattutto online. Trattamento di vincenti e bonus abuser: nessun riscontro diretto. Apertura del conto in ricevitoria: conta poco. Il vero neo: non è un brand molto conosciuto, deve farsi conoscere online. Questo giudizio ha orientato il primo paragrafo dei Contro, la lettura dei dati Trustpilot e App Store come segnale di scarsa presenza online, il paragrafo centrale del giudizio finale e la FAQ sul punto debole. Sul trattamento dei vincenti la recensione non dice nulla, né in positivo né in negativo, per assenza di riscontro. È opinione editoriale basata sull'esperienza diretta di Alberto nel settore, non un dato verificato su fonte primaria terza: va trattata come tale se il caporedattore ne chiede conto.
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
