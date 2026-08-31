# -*- coding: utf-8 -*-
import os

HERE = os.path.dirname(__file__)
CSS_PATH = os.path.join(HERE, "..", "_template", "review_style.css")
OUT_HTML = os.path.join(HERE, "recensione-lottomatica-2026.html")

with open(CSS_PATH, "r", encoding="utf-8") as f:
    CSS = f.read()

parts = []


def top_note():
    parts.append('<div class="doc-top-note">Recensione Lottomatica 2026&nbsp;&nbsp;|&nbsp;&nbsp;Aggiornamento: Agosto 2026</div>')


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
title("RECENSIONE LOTTOMATICA 2026", "Analisi completa dell'operatore")
rating_box(
    "⭐ 4/5",
    "Fino a 2.050€ di benvenuto", "Sport (100% fino a 50€ + 100% fino a 2.000€)",
    "4.000+ agenzie", "1.100 sale gioco",
)
cta("VAI SU LOTTOMATICA")
divider()

h1("INFORMAZIONI ESSENZIALI")
info_table([
    ("Licenza operativa", "ADM, concessione n. 16010 (Lottomatica Scommesse S.r.l.)"),
    ("Proprietà", "Lottomatica Group S.p.A. (ex Gamenet Group, rinominata nel 2020), quotata su Euronext Milan dal maggio 2023, nel FTSE MIB dal settembre 2025. Stesso gruppo di Betflag, Planetwin365 e Goldbet"),
    ("Bonus benvenuto", "100% sul primo deposito fino a 50€, più un secondo 100% fino a 2.000€: totale nominale fino a 2.050€"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento, su entrambe le componenti"),
    ("App disponibili", "iOS e Android, valutazione media 4,7/5 su oltre 11.500 recensioni"),
    ("Metodi di pagamento", "Carte, PostePay, Apple Pay, Google Pay, PayPal, Skrill, Neteller, MuchBetter, bonifico, MyBank, voucher Lottomatica"),
    ("Servizio clienti", "Telefono 800 900 009 (fisso) o 06 2929 (cellulare), live chat, email supporto@lottomatica.it, tutti i giorni 9:00-22:00"),
    ("Deposito minimo", "20€ per la maggior parte dei metodi, 2€ solo con voucher Lottomatica"),
    ("Registrazione rapida", "SPID non più disponibile dal 13 novembre 2025, CIE non disponibile"),
])

callout_box("PERCHÉ LOTTOMATICA POTREBBE NON FARE AL CASO TUO", [
    "Skrill, Neteller, MyBank e voucher Lottomatica sono esclusi dai metodi che attivano il bonus di benvenuto",
    "Registrazione SPID sospesa dal 13 novembre 2025, CIE non ancora disponibile: chi cerca l'accesso via identità digitale non lo trova",
    "Le multiple minime da 3 eventi richieste per validare entrambe le componenti del bonus spingono spesso a completare la giocata con eventi minori solo per raggiungere la soglia",
])
divider()

h1("PREFAZIONE")
body("Lottomatica nasce nel dicembre 1990 a Roma come consorzio per la gestione del Lotto, tra soci come BNL, Olivetti e Sogei. Nel 2006 acquisisce l'americana GTECH per 4 miliardi di euro, diventando il più grande gruppo al mondo nel settore dei giochi. Nel 2015 la fusione con IGT porta alla nascita di International Game Technology PLC, e per alcuni anni il marchio italiano delle scommesse opera come costola di un colosso quotato a Wall Street.")
body("Nel 2021 la direzione si inverte: Gamenet Group acquisisce da IGT le quote di Lottomatica Scommesse S.r.l. e Lottomatica Videolot Rete S.p.A., e l'anno seguente adotta il nome Lottomatica per l'intero gruppo. Da maggio 2023 Lottomatica Group è quotata su Euronext Milan, e da settembre 2025 fa parte del FTSE MIB. Nello stesso portafoglio siedono oggi Betflag, Planetwin365 e Goldbet, tutti già passati sotto la lente di questa serie.")
body("A differenza dei tre brand fratelli, però, Lottomatica non è un prodotto nato online: eredita da oltre trent'anni di storia una rete fisica che nessun altro concessionario del gruppo possiede, oltre 4.000 agenzie scommesse e 1.100 sale gioco. Questa recensione analizza bonus, palinsesto, casinò e sicurezza di un operatore che gioca una partita diversa dagli altri tre: non solo online, ma davvero omnicanale.")
divider()

h1("VALUTAZIONI")
data_table(
    ["Categoria", "Voto", "Nota sintetica"],
    [
        ["Palinsesto sportivo", "8/10", "Ampio ventaglio di discipline, dal calcio agli sport USA, streaming su eventi selezionati"],
        ["Quote e payout", "7/10", "Nella media del mercato ADM"],
        ["Bonus e promozioni", "7.5/10", "Fino a 2.050€ nominali, ma multiple minime su entrambe le componenti"],
        ["App e mobile", "8.5/10", "4,7/5 su oltre 11.500 recensioni, disponibile su iOS e Android"],
        ["Live streaming", "7/10", "Copertura su calcio, basket, tennis, eventi selezionati"],
        ["Casinò e slot", "8/10", "Oltre 3.000 slot, 30+ provider incluso IGT, live casinò con Evolution"],
        ["Metodi di pagamento", "8.5/10", "Tra i ventagli più ampi della categoria"],
        ["Assistenza clienti", "6.5/10", "Trustpilot molto negativo, esperienza diretta più sfumata ma margine di miglioramento reale"],
        ["Sicurezza e compliance", "8.5/10", "Licenza ADM storica, gruppo quotato e nel FTSE MIB"],
    ],
    highlight_col=1,
)
average_score("Valutazione media complessiva: 7.5/10")
divider()

h1("PRO &amp; CONTRO")
h2("Perché scegliere Lottomatica (Pro)")
body("Il tratto che distingue davvero Lottomatica dagli altri tre brand del gruppo non è nel palinsesto o nel casinò, ma nella rete fisica: oltre 4.000 agenzie scommesse e 1.100 sale gioco, ereditate da oltre trent'anni di storia che parte dalla gestione del Lotto nel 1990. Nessun altro concessionario del portafoglio Lottomatica Group ha un'infrastruttura fisica paragonabile: chi vuole passare dal punto vendita sotto casa al conto online, o viceversa, trova un'omnicanalità che Betflag, Planetwin365 e Goldbet non possono offrire.")
body("Il bonus di benvenuto arriva fino a 2.050€ nominali, diviso in due componenti da 50€ e 2.000€ sul primo deposito, entrambe attivabili con un deposito minimo di 20€. Il ventaglio di metodi di pagamento è tra i più ampi della categoria: oltre alle carte e ai principali e-wallet, sono disponibili Apple Pay, Google Pay, MyBank e un voucher proprietario che scende fino a 2€ di deposito minimo.")
body("Il casinò online supera i 3.000 giochi distribuiti su oltre 30 provider, con una sezione live firmata Evolution che include Crazy Time, Blackjack e Venezia Roulette. Tra i fornitori di slot compare anche IGT, la società con cui il gruppo ha condiviso vent'anni di storia societaria prima della separazione del 2021: un dettaglio che chiude idealmente il cerchio con le origini del marchio.")
body("Tra chi scommette con regolarità, Lottomatica si colloca alla pari con gli altri brand del gruppo già passati sotto questa lente: non ricorre con facilità a limitazioni o chiusure di conto per i giocatori vincenti o per chi sfrutta sistematicamente le promozioni, un comportamento tutt'altro che scontato nel mercato ADM.")
body("L'app, disponibile su iOS e Android, raccoglie una valutazione media di 4,7/5 su oltre 11.500 recensioni: un riscontro solido, in linea con i migliori risultati della categoria.")
h2("Dove Lottomatica può migliorare (Contro)")
body("Il dato più critico riguarda l'assistenza: su Trustpilot, Lottomatica raccoglie un punteggio di 1,2/5 su 1.182 recensioni, con il 92% delle valutazioni a una stella, in gran parte legate a lamentele su tempi di prelievo e qualità del supporto. È un quadro parzialmente distorto rispetto all'esperienza di chi lavora nel settore, ma il margine di miglioramento è reale: da leader di mercato con una storia di oltre trent'anni, l'attenzione all'esperienza del cliente e alla qualità dell'assistenza non è sempre all'altezza della posizione che l'operatore occupa.")
body("La registrazione tramite SPID non è più disponibile dal 13 novembre 2025, in coincidenza con il nuovo regime di rilascio delle concessioni online varato da ADM, e la CIE non è ancora un'alternativa attiva: chi cerca l'accesso più rapido tramite identità digitale deve procedere con l'inserimento manuale dei dati.")
body("Entrambe le componenti del bonus di benvenuto richiedono multiple da almeno 3 eventi con quota minima 1,50: un vincolo comune al settore, ma che nella pratica spinge spesso a completare la giocata con eventi minori solo per raggiungere la soglia richiesta.")
divider()

h1("PANORAMICA TRA EVENTI E STREAMING")
body("Il palinsesto di Lottomatica copre un ampio ventaglio di discipline: calcio, basket, tennis, pallavolo, motori (Formula 1 e MotoGP), ciclismo, pugilato, golf e i principali sport americani come football e baseball, oltre a hockey su ghiaccio, calcio a 5 e pallamano. Il calcio resta il prodotto trainante, con copertura di Serie A, Coppa Italia e dei principali campionati esteri.")
body("Lo streaming live copre una selezione di eventi tra cui Bundesliga, Coppa di Francia, FA Cup, Coppa America, Lega Pro, NBA, Serie A2 di basket e i grandi tornei del tennis, dai major ATP 1000 e 500. Sul calcio la copertura include alcune partite di Premier League, La Liga e Bundesliga: una selezione più ampia della media, anche se non sistematica su ogni competizione.")
divider()

h1("TIPOLOGIA DI GIOCHI DISPONIBILI")
body("<b>Scommesse sportive</b>: ampio ventaglio di discipline, dai grandi campionati europei agli sport americani, con quote pre-match, live e multiple.")
body("<b>Casinò online</b>: oltre 3.000 slot distribuite su più di 30 provider, tra cui IGT, NetEnt, Play'n GO, Pragmatic Play e Red Tiger Gaming.")
body("<b>Casinò live</b>: tavoli con dealer italiani firmati Evolution, tra cui Crazy Time, Blackjack live e Venezia Roulette.")
body("<b>Poker</b>: sezione dedicata con bonus specifico del 300% sul primo versamento fino a 1.200€ (deposito minimo 10€), sbloccato con 10€ di bonus ogni 30€ di rake generata entro 30 giorni.")
divider()

h1("PROMOZIONI")
h2("Bonus di benvenuto — prima componente")
info_table([
    ("Percentuale e massimale", "100% sul primo deposito, fino a 50€"),
    ("Deposito minimo qualificante", "20€, entro 7 giorni dalla registrazione"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento"),
])
h2("Bonus di benvenuto — seconda componente")
info_table([
    ("Percentuale e massimale", "Ulteriore 100% sul primo deposito, fino a 2.000€"),
    ("Rollover", "6 volte l'importo, su multiple da almeno 3 eventi a quota minima 1,50"),
    ("Finestra temporale", "Da completare entro 30 giorni dalla registrazione"),
])
h2("Bonus poker")
body("300% sul primo versamento fino a 1.200€ (deposito minimo 10€), sbloccato progressivamente con 10€ di bonus ogni 30€ di rake generata, validità 30 giorni dall'erogazione.")
note_box("Nota importante", "Skrill, Neteller, MyBank e voucher Lottomatica sono esclusi dai metodi che attivano il bonus di benvenuto. Tutte le condizioni sono soggette ad aggiornamento da parte dell'operatore: verificare sempre i T&amp;C ufficiali prima dell'attivazione.")
divider()

h1("INFO SULLE QUOTE, MERCATI E FUNZIONALITÀ")
body("Lottomatica costruisce l'offerta scommesse su un palinsesto ampio quanto trasversale: calcio, basket e tennis restano i pilastri, ma la copertura si estende a discipline meno centrali nel mercato ADM come pugilato, golf e sport americani. Il vero terreno differenziante dell'operatore, però, resta fuori dal palinsesto: è la rete fisica di oltre 4.000 agenzie e 1.100 sale gioco, un'infrastruttura che nessun altro brand del gruppo Lottomatica può vantare.")
h2("Come piazzare una scommessa su Lottomatica")
body("<b>STEP 1: Scegli l'evento</b> — Naviga il palinsesto online o passa dal punto vendita fisico. Seleziona il mercato e la quota desiderata.")
body("<b>STEP 2: Componi la giocata</b> — Inserisci l'importo. Aggiungi altri eventi per una multipla, verificando che la quota totale rispetti eventuali requisiti bonus attivi.")
body("<b>STEP 3: Conferma</b> — Conferma la giocata online o al banco. La ricevuta appare in tempo reale nella cronologia del conto, o viene stampata al punto vendita.")
divider()

h1("CONTO DI SCOMMESSA E REGISTRAZIONE")
body("<b>Registrazione</b>: compilazione del modulo con dati anagrafici, codice fiscale, email e numero di telefono, seguita dal caricamento di un documento d'identità valido in fase di apertura del conto. Dal 13 novembre 2025 non è più possibile registrarsi tramite SPID; la CIE non è al momento un'alternativa disponibile.")
body("<b>Requisiti di base</b>: maggiore età (18 anni), residenza in Italia, codice fiscale italiano, documento d'identità in corso di validità.")
divider()

h1("METODI DI PAGAMENTO")
body("Lottomatica mette a disposizione uno dei ventagli di pagamento più ampi della categoria: carte di credito, PostePay, Apple Pay, Google Pay, PayPal, Skrill, Neteller, MuchBetter, bonifico bancario, MyBank e un voucher proprietario Lottomatica.")
data_table(
    ["Metodo", "Deposito minimo", "Prelievo"],
    [
        ["Carte / PostePay", "20€", "Sì"],
        ["Apple Pay / Google Pay", "20€", "Sì"],
        ["PayPal", "20€", "Sì"],
        ["Skrill / Neteller", "10€", "Sì (non attiva il bonus)"],
        ["Voucher Lottomatica", "2€", "Solo deposito"],
        ["Bonifico bancario", "20€", "Sì"],
    ],
)
body("I prelievi tramite e-wallet (PayPal, Skrill, Neteller) richiedono generalmente 24 ore di lavorazione, con un range che va da un minimo di 10€ a un massimo di 5.000€ per operazione.")
divider()

h1("SICUREZZA")
body("<b>Licenza ADM</b>: concessione n. 16010, in capo a Lottomatica Scommesse S.r.l. Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana.")
body("<b>Garanzia patrimoniale</b>: Lottomatica Group S.p.A. è quotata su Euronext Milan dal maggio 2023 ed è entrata nel FTSE MIB da settembre 2025, uno dei 40 titoli più liquidi e capitalizzati della Borsa italiana: una solidità finanziaria che rafforza le garanzie dietro il brand.")
body("<b>Gioco responsabile</b>: strumenti di auto-limitazione dei depositi, autoesclusione temporanea o permanente, limiti di durata delle sessioni e test di autovalutazione, in conformità con le normative ADM.")
divider()

h1("SERVE AIUTO? CUSTOMER SUPPORT")
body("Il servizio clienti è raggiungibile tramite telefono (800 900 009 da rete fissa, 06 2929 da cellulare), live chat nell'area riservata ed email (supporto@lottomatica.it), tutti i giorni dalle 9:00 alle 22:00.")
body("Su Trustpilot l'operatore raccoglie un punteggio molto basso, 1,2/5 su 1.182 recensioni, in gran parte legato a lamentele su tempi di prelievo e qualità del supporto. Un quadro che, nell'esperienza di chi lavora nel settore, appare parzialmente distorto rispetto alla realtà del servizio, ma che segnala comunque un margine di miglioramento reale sull'esperienza del cliente, specie per un operatore che occupa una posizione di leadership nel mercato ADM.")
divider()

h1("ALTRI PRODOTTI NELL'OFFERTA")
body("<b>Poker</b>: sezione dedicata con bonus specifico del 300% sul primo versamento fino a 1.200€.")
body("<b>Rete fisica</b>: oltre 4.000 agenzie scommesse e 1.100 sale gioco, un'infrastruttura omnicanale che accompagna l'offerta online e che nessun altro brand del gruppo Lottomatica possiede.")
divider()

h1("FEEDBACK E RECENSIONI")
body("Sull'App Store e Google Play, l'app Lottomatica raggiunge una valutazione media di 4,7/5 su oltre 11.500 recensioni complessive: un punteggio solido, in linea con i migliori risultati della categoria.")
body("Il quadro cambia su Trustpilot, dove Lottomatica registra un punteggio di 1,2/5 su 1.182 recensioni, con il 92% dei giudizi a una stella, concentrati su lamentele relative a prelievi e assistenza. Una divaricazione così ampia tra i due canali non è rara nel settore, ma resta un punto su cui l'operatore ha margine di miglioramento.")
divider()

h1("TABELLA COMPARATIVA: LOTTOMATICA VS SNAI VS GOLDBET")
data_table(
    ["Caratteristica", "Lottomatica", "SNAI", "Goldbet"],
    [
        ["Bonus sport", "100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (quota min. 1,50)", "500€ Gold (x6) + 500€ Game Bonus + 15€ free + 9€ extra = ~1.500€", "100% fino a 2.000€ (rollover x6)"],
        ["Deposito minimo bonus", "20€", "Non specificato in questa serie", "20€"],
        ["Proprietà", "Lottomatica Group (capofila del gruppo)", "Gruppo Flutter Entertainment (dal 2025)", "Gruppo Lottomatica"],
        ["Prodotto distintivo", "Rete fisica: 4.000+ agenzie, 1.100 sale gioco", "Ippica, Snaipay, integrazione fisico-digitale", "Interfaccia mobile, quote competitive"],
        ["Registrazione SPID/CIE", "Non disponibile dal 13/11/2025", "Sì", "Non verificato in questa serie"],
        ["Licenza ADM", "16010", "Non riportata in questa serie", "16009"],
    ],
)
body("<b>Nota</b>: le cifre di tutti gli operatori rappresentano valori nominali massimi, soggetti a rollover e condizioni di sblocco spesso complesse. Lottomatica è il concessionario capofila dello stesso gruppo proprietario di Goldbet: la tabella li mette a confronto come prodotti distinti, non come alternative indipendenti.", size=9)
divider()

h1("IL NOSTRO GIUDIZIO")
body("Lottomatica arriva al 2026 con una storia che nessun altro brand di questa serie può vantare: nasce nel 1990 come consorzio per la gestione del Lotto, attraversa vent'anni sotto il controllo di IGT dopo la fusione del 2015, e nel 2021 torna sotto controllo italiano quando Gamenet Group ne rileva le quote scommesse, adottandone poi il nome. Oggi Lottomatica Group è quotata su Euronext Milan e nel FTSE MIB, capofila dello stesso portafoglio che include Betflag, Planetwin365 e Goldbet.")
body("Quello che distingue davvero Lottomatica dai tre fratelli online, però, non sta nella scheda tecnica del prodotto digitale: è la rete fisica, oltre 4.000 agenzie scommesse e 1.100 sale gioco, un'infrastruttura omnicanale unica nel gruppo. A questo si aggiunge un comportamento verso i giocatori vincenti e i bonus abuser che, secondo chi opera nel settore, si colloca alla pari con gli altri brand già passati sotto questa lente: nessuna limitazione facile, un trattamento corretto.")
body("Il bonus di benvenuto arriva a 2.050€ nominali su due componenti, il casinò supera i 3.000 giochi con un live curato da Evolution, e l'app raccoglie un solido 4,7/5. Il punto su cui l'operatore ha davvero margine di miglioramento è l'esperienza del cliente lato assistenza: il punteggio Trustpilot di 1,2/5 racconta un quadro più duro della realtà percepita da chi lavora nel settore, ma la sostanza del rilievo regge. Da leader di mercato con oltre trent'anni di storia, l'attenzione alla UX e alla qualità del supporto non è sempre coerente con la posizione che l'operatore occupa: è l'area dove Lottomatica ha più da guadagnare rispetto agli altri brand dello stesso gruppo.")
body("Chi cerca un operatore omnicanale, con una rete fisica capillare alle spalle e un trattamento corretto verso chi vince con regolarità, trova in Lottomatica una scelta solida. Chi valuta l'assistenza come criterio decisivo farebbe bene a verificare i canali disponibili prima di scegliere, tenendo presente che il dato più critico riguarda l'esperienza online più che il servizio in agenzia.")
final_score_box("VOTO FINALE: 4 SU 5")
divider()

h1("FAQ")
h2("Lottomatica è sicuro?")
body("Opera sotto concessione ADM n. 16010 ed è controllato da Lottomatica Group S.p.A., quotata su Euronext Milan e nel FTSE MIB dal settembre 2025: tra gli operatori regolamentati più solidi del mercato italiano.")
h2("È possibile registrarsi con SPID o CIE su Lottomatica?")
body("No. La registrazione tramite SPID non è più disponibile dal 13 novembre 2025, e la CIE non è al momento un'alternativa attiva. La registrazione richiede l'inserimento manuale dei dati e il caricamento di un documento d'identità.")
h2("In cosa Lottomatica è diverso dagli altri brand del gruppo (Betflag, Planetwin365, Goldbet)?")
body("È l'unico con una rete fisica: oltre 4.000 agenzie scommesse e 1.100 sale gioco, ereditate da una storia che parte dalla gestione del Lotto nel 1990. Gli altri tre brand del gruppo sono prodotti nati online.")
h2("Quali metodi di pagamento non attivano il bonus di benvenuto?")
body("Skrill, Neteller, MyBank e il voucher Lottomatica sono esclusi dai metodi che permettono di ricevere il bonus.")
divider()

h1("LE MIGLIORI ALTERNATIVE")
body("<b>Goldbet</b>: stesso gruppo proprietario di Lottomatica, bonus sport 100% fino a 2.000€ con rollover x6, interfaccia mobile apprezzata dalla fascia più giovane dell'utenza.")
body("<b>Planetwin365</b>: terzo brand del gruppo, casinò live con tavoli esclusivi Evolution, bonus fino a 2.100€ tra sport e slot.")
body("<b>SNAI</b>: leadership storica nell'ippica, integrazione fisico-digitale con Snaipay, rollover x6 sul Bonus Gold tra i più accessibili del mercato.")

plain_note("Il gioco è vietato ai minori di 18 anni • Bonus e T&amp;C soggetti a modifica: verificare sempre su lottomatica.it")

html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Recensione Lottomatica 2026</title>
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Salvato:", OUT_HTML)
