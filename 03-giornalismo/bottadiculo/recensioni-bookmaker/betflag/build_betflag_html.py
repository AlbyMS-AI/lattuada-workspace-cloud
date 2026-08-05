# -*- coding: utf-8 -*-
import os

HERE = os.path.dirname(__file__)
CSS_PATH = os.path.join(HERE, "..", "_template", "review_style.css")
OUT_HTML = os.path.join(HERE, "recensione-betflag-2026.html")

with open(CSS_PATH, "r", encoding="utf-8") as f:
    CSS = f.read()

parts = []


def top_note():
    parts.append('<div class="doc-top-note">Recensione Betflag 2026&nbsp;&nbsp;|&nbsp;&nbsp;Aggiornamento: Luglio 2026</div>')


def title(t, s):
    parts.append(f'<h1 class="doc-title">{t}</h1><p class="doc-subtitle">{s}</p>')


def rating_box(stars, t2, s2, t3, s3):
    parts.append(f'''
    <table class="rating-box"><tr>
      <td><span class="stars">{stars}</span></td>
      <td><span class="col-title">{t2}</span><span class="col-sub">{s2}</span></td>
      <td><span class="col-title">{t3}</span><span class="col-sub">{s3}</span></td>
    </tr></table>''')


def cta(text):
    parts.append(f'<div class="cta-bar">{text}</div>')


def divider():
    parts.append('<hr class="divider">')


def h1(text):
    parts.append(f'<h2 class="section avoid-break">{text}</h2>')


def h2(text):
    parts.append(f'<h3 class="subsection avoid-break">{text}</h3>')


def body(text, size=None):
    style = f' style="font-size:{size}pt"' if size else ""
    parts.append(f'<p class="body-text"{style}>{text}</p>')


def info_table(rows):
    trs = "".join(
        f'<tr><td class="label">{lab}</td><td>{val}</td></tr>' for lab, val in rows
    )
    parts.append(f'<table class="info-table">{trs}</table>')


def callout_box(heading, bullets):
    lis = "".join(f"<li>{it}</li>" for it in bullets)
    parts.append(f'''<div class="callout-box avoid-break">
      <p class="callout-heading">{heading}</p>
      <ul>{lis}</ul>
    </div>''')


def note_box(label, text):
    parts.append(f'<div class="note-box avoid-break"><span class="note-label">{label}: </span>{text}</div>')


def data_table(headers, rows, highlight_col=None):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for row in rows:
        tds = ""
        for i, val in enumerate(row):
            cls = ""
            if i == highlight_col:
                cls = ' class="highlight-col"'
            elif i == 0:
                cls = ' class="label-col"'
            tds += f"<td{cls}>{val}</td>"
        trs += f"<tr>{tds}</tr>"
    parts.append(f'<table class="data-table"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>')


def average_score(text):
    parts.append(f'<p class="average-score">{text}</p>')


def final_score_box(text):
    parts.append(f'<div class="final-score-box avoid-break">{text}</div>')


def plain_note(text):
    parts.append(f'<p class="body-text" style="text-align:center;color:#666666;font-size:8pt;font-style:italic;margin-top:18px">{text}</p>')


# ============ CONTENUTO ============
top_note()
title("RECENSIONE BETFLAG 2026", "Analisi completa dell'operatore")
rating_box(
    "⭐ 4.5/5",
    "Fino a 5.010€ di benvenuto", "Sport (100% + 10€ no deposit + 200 Fun Flag)",
    "Fino a 3.000€", "Casinò (+ 3.000€ Casinò Live)",
)
cta("VAI SU BETFLAG")
divider()

h1("INFORMAZIONI ESSENZIALI")
info_table([
    ("Licenza operativa", "ADM, concessione n. 16008 (subentrata alla precedente GAD 15007 con il nuovo bando ADM)"),
    ("Proprietà", "Betflag S.p.A., dal novembre 2022 controllata al 100% da Lottomatica Group (operazione da 310 milioni di euro, più una componente variabile fino a 50 milioni legata ai risultati 2023). Resta un brand autonomo nel portafoglio multibrand del gruppo"),
    ("Bonus sport", "100% sul primo deposito fino a 5.000€ + 10€ senza deposito immediato + 200 Fun Flag (4 tranche da 50, ogni due giorni)"),
    ("Bonus casinò", "100% sul primo deposito fino a 3.000€ (casinò) + fino a 3.000€ (casinò live)"),
    ("Bonus senza deposito (SPID/CIE)", "1.000€, erogati in 5 tranche da 200€, rollover 1.000€ per tranche, massimo 500€ convertibili"),
    ("Bonus senza deposito (registrazione classica)", "250€, erogati in 5 tranche da 50€, rollover 250€, massimo 125€ convertibili"),
    ("App disponibili", "iOS (App Store) e Android"),
    ("Metodi di pagamento", "Visa, Visa Electron, Maestro, Mastercard, PayPal, Skrill, Neteller, PostePay, bonifico bancario, Paysafecard, OnShop"),
    ("Servizio clienti", "Numero Verde 800.900.333 (da fisso, 8:00-22:00), 02-91645111 (da mobile), email tramite sezione Aiuto"),
    ("Deposito minimo", "5€ per la maggior parte dei metodi, 0,50€ per bonifico, 10€ per Skrill e Paysafecard"),
    ("Registrazione rapida", "SPID e CIE disponibili, accesso al bonus senza deposito maggiorato (1.000€ contro i 250€ della registrazione classica)"),
])

callout_box("PERCHÉ BETFLAG POTREBBE NON FARE AL CASO TUO", [
    "Quota minima richiesta per validare il bonus sport: 3,50, di poco più alta della media di settore",
    "Rollover del bonus senza deposito pari a 4 volte l'importo ricevuto su ogni tranche",
    "L'app dedicata al casinò raccoglie un volume di recensioni ancora contenuto sull'App Store: chi cerca conferme ampie farà bene a consultare anche l'app Scommesse, più recensita",
])
divider()

h1("PREFAZIONE")
body("Betflag è online dal 2004, quando il mercato italiano delle scommesse a distanza muoveva i primi passi. Ventidue anni dopo, l'operatore non è più un'azienda indipendente: dal novembre 2022 è controllato al 100% da Lottomatica Group, che lo ha acquisito per 310 milioni di euro con l'obiettivo dichiarato di rafforzare il proprio posizionamento nei casino games.")
body("La scelta del gruppo è stata mantenere Betflag come brand separato, non assorbirlo in un prodotto unico. Per chi scommette, questo significa un'offerta che si muove in parallelo a quella di Lottomatica (Better), condividendo le risorse economiche e regolatorie del gruppo ma con un'identità di prodotto ancora distinta, a partire da una caratteristica che pochi concessionari ADM offrono: il betting exchange.")
body("Operando sotto la concessione ADM n. 16008, Betflag copre l'intero spettro del gioco regolamentato: scommesse sportive, ippica, exchange, casinò, bingo, poker, lotterie. Questa recensione analizza l'offerta, dal bonus di benvenuto alla sicurezza, passando per il nodo più delicato: la distanza tra la reputazione sui grandi store e quella sulle piattaforme di recensioni indipendenti.")
divider()

h1("VALUTAZIONI")
data_table(
    ["Categoria", "Voto", "Nota sintetica"],
    [
        ["Palinsesto sportivo", "8.5/10", "Oltre 30 discipline, buona profondità su calcio ed eSport"],
        ["Quote e payout", "8/10", "Quota minima 3,50 per validare il bonus sport"],
        ["Bonus e promozioni", "9/10", "Tra le offerte più ricche del mercato ADM"],
        ["App e mobile", "8.5/10", "Suite completa (scommesse, casinò, ippica, exchange, carte, poker, lotterie), app Scommesse tra le più apprezzate del settore"],
        ["Live streaming", "7.5/10", "Copertura di Bundesliga, Lega Pro e altri campionati"],
        ["Ippica", "8.5/10", "Sezione dedicata con streaming live delle corse"],
        ["Casinò e slot", "8.5/10", "Catalogo tra i più ampi del mercato ADM, oltre 5.500 titoli"],
        ["Metodi di pagamento", "8.5/10", "13 metodi disponibili, nessuna commissione sui prelievi"],
        ["Assistenza clienti", "7.5/10", "Numero verde e canale mobile attivi; margini di miglioramento nella percezione utenti sulle dispute"],
        ["Sicurezza e compliance", "8.5/10", "Licenza ADM, garanzia patrimoniale del Gruppo Lottomatica"],
    ],
    highlight_col=1,
)
average_score("Valutazione media complessiva: 8.3/10")
divider()

h1("PRO &amp; CONTRO")
h2("Perché scegliere Betflag (Pro)")
body("Il bonus di benvenuto sport, 100% del primo deposito fino a 5.000€, è tra i più alti del mercato ADM. Il deposito minimo qualificante è di 5€, tra i più accessibili del settore: non serve un budget importante per attivare la promozione, anche se sfruttarla per intero richiede depositi consistenti.")
body("L'Exchange è la caratteristica che distingue davvero Betflag dal resto del mercato regolamentato italiano. Nel betting exchange non è il bookmaker a fissare le quote: sono gli scommettitori stessi a farlo, puntando o bancando un esito, con l'operatore che agisce da intermediario e trattiene una piccola commissione sulle giocate abbinate. La funzionalità Moneyback permette di equilibrare l'esposizione, incassando una parte della vincita o limitando una perdita prima che l'evento finisca. Pochi concessionari ADM offrono questo prodotto.")
body("La sezione ippica è un punto di forza riconosciuto: streaming live delle corse integrato nella piattaforma, in un mercato dove pochi operatori investono con continuità su questa disciplina.")
body("Il ventaglio di metodi di pagamento è ampio: 13 opzioni tra carte, e-wallet, PostePay, bonifico e OnShop, senza commissioni sui prelievi. Un dettaglio che pesa nel tempo, soprattutto per chi preleva con frequenza.")
h2("Dove Betflag può migliorare (Contro)")
body("L'app Scommesse, quella con il maggior numero di recensioni, mantiene una valutazione alta sull'App Store. Su altre piattaforme di recensioni indipendenti il quadro è più eterogeneo, con alcune segnalazioni su tempi di attesa per i prelievi, spesso legate ai controlli ADM/KYC previsti dalla normativa più che a un problema strutturale della piattaforma. Come per ogni operatore regolamentato, restare informati sulle tempistiche di verifica prima del primo deposito importante aiuta a gestire meglio le aspettative.")
body("Il rollover sul bonus senza deposito, sia nella versione SPID/CIE da 1.000€ sia in quella classica da 250€, è fissato a 4 volte l'importo di ogni tranche: una condizione nella media di settore, utile da conoscere prima di depositare.")
divider()

h1("PANORAMICA TRA EVENTI E STREAMING")
body("Il palinsesto sportivo di Betflag copre oltre 30 discipline e migliaia di eventi ogni settimana. Il calcio resta il prodotto principale, con copertura di Serie A, Serie B, Champions League, Europa League e dei principali campionati internazionali. Non manca l'offerta sui mercati minori (darts, snooker, sport americani) e sull'eSport, con tornei di League of Legends, CS:GO, Dota 2 e Valorant.")
body("Lo streaming live copre Bundesliga, Lega Pro e altri campionati esteri, oltre a tennis, basket e ippica. La copertura non raggiunge l'ampiezza dei leader di mercato sul fronte calcio internazionale, ma resta solida per chi segue le corse in diretta o i campionati minori europei.")
divider()

h1("TIPOLOGIA DI GIOCHI DISPONIBILI")
body("<b>Scommesse sportive</b>: oltre 30 discipline, dai grandi campionati agli eSport, con quote pre-match, live e multiple.")
body("<b>Exchange</b>: betting exchange con quote fissate dagli scommettitori, funzionalità Moneyback per gestire l'esposizione prima della fine dell'evento. Esclude Cashout tradizionale e non concorre alla validazione del bonus di benvenuto sport.")
body("<b>Ippica</b>: sezione dedicata con streaming live delle corse, tra i punti di forza più citati dagli utenti.")
body("<b>Casinò online</b>: catalogo tra i più ampi del mercato ADM, oltre 5.500 titoli, distribuiti su 60+ provider certificati.")
body("<b>Casinò live</b>: oltre 900 tavoli, disponibili 24 ore su 24.")
body("<b>Bingo, Poker, Lotterie</b>: sezioni presenti nell'app, a completamento dell'offerta.")
divider()

h1("PROMOZIONI")
h2("Bonus di benvenuto Sport")
body("Il pilastro dell'offerta è il 100% sul primo deposito fino a 5.000€.")
info_table([
    ("Massimale", "5.000€"),
    ("Deposito minimo qualificante", "5€"),
    ("Quota minima", "3,50 per evento, su scommesse pre-match, live o multiple"),
    ("Esclusioni", "Exchange e Cashout non concorrono alla validazione"),
    ("Finestra temporale", "90 giorni per completare gli obiettivi"),
    ("Erogazione", "A scaglioni progressivi"),
])
body("A questo si aggiunge un pacchetto di benvenuto immediato: 10€ senza deposito, utilizzabili da subito sulle scommesse sportive, più 200 Fun Flag erogati in 4 tranche da 50, ogni due giorni a partire dall'assegnazione del primo bonus. In fase di registrazione va selezionata l'opzione «10€ e 200 Fun Flag Sport» per attivarlo.")
h2("Bonus di benvenuto Casinò")
body("100% sul primo versamento fino a 3.000€ per il casinò, più un'offerta parallela fino a 3.000€ dedicata al casinò live.")
h2("Bonus senza deposito: Registrazione SPID/CIE")
body("1.000€, erogati in 5 tranche da 200€ ciascuna. Rollover di 1.000€ per tranche, con un massimo di 500€ convertibili in saldo prelevabile.")
h2("Bonus senza deposito: Registrazione classica")
body("250€, erogati in 5 tranche da 50€ ciascuna. Rollover di 250€, massimo 125€ convertibili.")
note_box("Nota importante", "tutte le condizioni (rollover, tempistiche, soglie) sono soggette ad aggiornamento da parte di Betflag. Verificare sempre i T&amp;C ufficiali prima dell'attivazione di qualsiasi bonus.")
divider()

h1("INFO SULLE QUOTE, MERCATI E FUNZIONALITÀ")
body("Il tratto distintivo dell'offerta Betflag non è la profondità dei singoli mercati calcistici, in linea con la media di settore, ma la presenza dell'Exchange accanto alle scommesse tradizionali. Nell'exchange le quote nascono dall'incontro tra chi punta e chi banca un esito: il bookmaker si limita a intermediare e a trattenere una commissione sulle giocate abbinate. È un meccanismo diverso da quello delle quote fisse, pensato per chi vuole intervenire sull'esposizione durante l'evento, non solo scommettere sull'esito finale.")
body("La funzionalità Moneyback lavora su questo stesso principio: permette di incassare parte di una vincita potenziale o di limitare una perdita prima che l'evento sia concluso, ribilanciando la posizione in corso.")
h2("Come piazzare una scommessa su Betflag")
body("<b>STEP 1: Scegli l'evento</b> — Naviga il palinsesto o usa la ricerca rapida. Seleziona il mercato e la quota desiderata.")
body("<b>STEP 2: Componi la giocata</b> — Inserisci l'importo. Aggiungi altri eventi per una multipla, oppure passa alla sezione Exchange per puntare o bancare una quota.")
body("<b>STEP 3: Conferma</b> — Conferma la giocata. La ricevuta appare in tempo reale nella cronologia del conto.")
divider()

h1("CONTO DI SCOMMESSA E REGISTRAZIONE")
body("<b>Registrazione classica</b>: compilazione del modulo con dati anagrafici, codice fiscale, email e numero di telefono, seguita dall'invio del documento d'identità per la verifica. All'esito positivo, il sistema eroga il bonus senza deposito da 250€.")
body("<b>Registrazione SPID/CIE</b>: percorso accelerato tramite identità digitale, che elimina la fase di verifica documentale manuale e sblocca il bonus senza deposito maggiorato da 1.000€.")
body("<b>Requisiti di base</b>: maggiore età (18 anni), residenza in Italia, codice fiscale italiano, documento d'identità in corso di validità.")
divider()

h1("METODI DI PAGAMENTO")
body("Betflag mette a disposizione 13 modalità di deposito, tra le più ampie del mercato ADM: Visa, Visa Electron, Maestro, Mastercard, PayPal, Skrill, Neteller, PostePay, bonifico bancario, Paysafecard e OnShop.")
data_table(
    ["Metodo", "Deposito minimo", "Prelievo"],
    [
        ["Carte (Visa/Mastercard/Maestro)", "5€", "Sì"],
        ["PayPal", "5€", "Sì"],
        ["Skrill / Neteller", "5€", "Sì"],
        ["PostePay", "5€", "Solo deposito"],
        ["Bonifico bancario", "0,50€", "Sì"],
        ["Paysafecard", "10€", "Solo deposito"],
        ["OnShop", "5€", "Sì"],
    ],
)
body("I tempi di accredito sono istantanei per la quasi totalità dei metodi, a eccezione del bonifico bancario. Non risultano commissioni sui prelievi, qualunque sia il metodo scelto: un vantaggio concreto rispetto a operatori che applicano costi oltre una certa soglia di operazioni.")
divider()

h1("SICUREZZA")
body("<b>Licenza ADM</b>: concessione n. 16008, subentrata alla precedente GAD 15007 con il nuovo bando ADM per la raccolta a distanza. Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana.")
body("<b>Garanzia patrimoniale</b>: dal novembre 2022 Betflag fa parte del Gruppo Lottomatica, uno dei maggiori operatori regolamentati in Italia, il che rafforza la solidità economica dietro il brand.")
body("<b>Gioco responsabile</b>: come tutti gli operatori ADM, Betflag mette a disposizione strumenti di auto-limitazione dei depositi e auto-esclusione dal gioco, in conformità con le normative italiane.")
divider()

h1("SERVE AIUTO? CUSTOMER SUPPORT")
body("Il servizio clienti è raggiungibile tramite Numero Verde 800.900.333 (da rete fissa, 8:00-22:00), il numero 02-91645111 per chi chiama da cellulare, ed email attraverso la sezione Aiuto del sito.")
body("Il canale telefonico è apprezzato da una parte degli utenti. Per le dispute più complesse, spesso legate a verifiche ADM/KYC, il contatto diretto con un operatore resta il percorso più efficace rispetto ai canali self-service.")
divider()

h1("ALTRI PRODOTTI NELL'OFFERTA")
body("<b>Bingo online</b>: sezione presente nell'app, a completamento dell'offerta di intrattenimento.")
body("<b>Poker</b>: tornei e tavoli cash, integrati nella suite Betflag.")
body("<b>Lotterie</b>: sezione dedicata alle lotterie online.")
divider()

h1("FEEDBACK E RECENSIONI")
body("Sull'App Store, BetFlag: Scommesse, l'app più utilizzata e recensita della suite, raccoglie una valutazione di 4,8/5 su circa 3.200 recensioni: tra i punteggi più solidi del comparto app di betting in Italia. Gli utenti apprezzano interfaccia e copertura sportiva.")
body("L'app dedicata al casinò, BetFlag: Casinò e Slot Machine, ha un volume di recensioni ancora contenuto (47) e un punteggio più altalenante, con alcune segnalazioni su tempi di prelievo. Un campione piccolo, da guardare più come segnale da monitorare che come giudizio consolidato: la stessa dinamica, tempi di prelievo legati alle verifiche ADM/KYC, emerge anche su altre piattaforme di recensioni indipendenti.")
divider()

h1("TABELLA COMPARATIVA: BETFLAG VS SNAI VS SISAL")
data_table(
    ["Caratteristica", "Betflag", "SNAI", "Sisal"],
    [
        ["Bonus sport", "100% fino a 5.000€ + 10€ no deposit + 200 Fun Flag = ~5.010€ (quota min. 3,50)", "500€ Gold (x6) + 500€ Game Bonus + 15€ free + 9€ extra = ~1.500€", "50-200€ Real + 1.500€ Fun"],
        ["Bonus no deposit", "1.000€ (SPID/CIE) / 250€ (classica)", "15€ sport / 1.000€ Play (casinò, percorso separato)", "Fino a 5.000€ (Salva il Bottino)"],
        ["Proprietà", "Gruppo Lottomatica (dal 2022)", "Gruppo Flutter Entertainment (dal 2025)", "Gruppo Flutter Entertainment (dal 2022)"],
        ["Prodotto distintivo", "Betting Exchange + Moneyback", "Ippica, Snaipay, integrazione fisico-digitale", "Gamification"],
        ["Discipline sportive", "30+", "25+", "25+"],
        ["Live streaming", "Bundesliga, Lega Pro e altri", "Eccellente (Bundesliga, Ligue 1, FA Cup, Liga, Serie A dedicata)", "Buono"],
        ["Login SPID/CIE", "Sì", "Sì", "Sì"],
    ],
)
body("<b>Nota</b>: le cifre di tutti gli operatori rappresentano valori nominali massimi, soggetti a rollover e condizioni di sblocco spesso complesse. Il valore effettivo percepito dall'utente può essere molto inferiore al valore headline della promozione.", size=9)
divider()

h1("IL NOSTRO GIUDIZIO")
body("Betflag arriva al 2026 con due identità che convivono: da un lato lo storico del bookmaker online nato nel 2004, dall'altro la nuova appartenenza al Gruppo Lottomatica, che dal 2022 ne garantisce la solidità patrimoniale mantenendone però l'autonomia di brand e prodotto.")
body("L'Exchange resta una delle poche concessioni ADM a offrirlo, un tratto che nel mercato italiano è tradizionalmente associato a Betfair. Su Betflag la funzionalità è presente ma non è valorizzata e promossa con la stessa intensità: resta più una carta in più nel mazzo che il motivo principale per cui un giocatore sceglie l'operatore. Restano invece solidi il bonus di benvenuto tra i più alti del mercato, un catalogo casinò tra i più ampi del comparto ADM e una sezione ippica ben curata.")
body("Chi punta solo sull'esito troverà in Betflag un bonus tra i più generosi del mercato e un catalogo ampio su casinò e ippica. Chi cerca l'Exchange lo trova anche qui, ma non è il terreno su cui Betflag gioca la sua partita migliore.")
final_score_box("VOTO FINALE: 4.5 SU 5")
divider()

h1("FAQ")
h2("Cos'è l'Exchange di Betflag e come funziona?")
body("È un betting exchange: le quote non sono fissate dal bookmaker ma nascono dall'incontro tra chi punta e chi banca un esito. Betflag intermedia le giocate e trattiene una commissione su quelle abbinate. La funzionalità Moneyback permette di ribilanciare l'esposizione prima della fine dell'evento.")
h2("Qual è la differenza tra registrazione classica e SPID/CIE?")
body("La registrazione classica richiede l'invio del documento d'identità per la verifica e dà accesso a un bonus senza deposito di 250€. La registrazione tramite SPID o CIE elimina la verifica manuale e sblocca un bonus senza deposito maggiorato di 1.000€.")
h2("Il bonus Exchange conta per il bonus di benvenuto sport?")
body("No. Le giocate su Exchange e il Cashout sono escluse dalla validazione del bonus di benvenuto sport, che richiede scommesse pre-match, live o multiple con quota minima 3,50.")
h2("Betflag è sicuro?")
body("Opera sotto concessione ADM n. 16008 ed è controllato al 100% dal Gruppo Lottomatica dal 2022, uno degli operatori regolamentati più solidi del mercato italiano.")
divider()

h1("LE MIGLIORI ALTERNATIVE")
body("<b>SNAI</b>: leadership storica nell'ippica, integrazione fisico-digitale con Snaipay, rollover x6 sul Bonus Gold tra i più accessibili del mercato.")
body("<b>Sisal</b>: bonus senza deposito fino a 5.000€ tramite il quiz sportivo «Salva il Bottino», meccanismo unico nel panorama italiano.")
body("<b>Lottomatica (Better)</b>: stesso gruppo proprietario di Betflag, con un'offerta bonus tra le più alte del mercato e un catalogo slot tra i più ampi.")
body("<b>Goldbet</b>: operatore in crescita, quote competitive e interfaccia mobile apprezzata dalla fascia più giovane dell'utenza.")

plain_note("Contenuto editoriale indipendente • Dati verificati a luglio 2026 • Il gioco è vietato ai minori di 18 anni • Bonus e T&amp;C soggetti a modifica: verificare sempre su betflag.it")

html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Recensione Betflag 2026</title>
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Salvato:", OUT_HTML)
