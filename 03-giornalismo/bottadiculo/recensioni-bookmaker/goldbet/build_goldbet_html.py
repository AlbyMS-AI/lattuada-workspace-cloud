# -*- coding: utf-8 -*-
import os

HERE = os.path.dirname(__file__)
CSS_PATH = os.path.join(HERE, "..", "_template", "review_style.css")
OUT_HTML = os.path.join(HERE, "recensione-goldbet-2026.html")

with open(CSS_PATH, "r", encoding="utf-8") as f:
    CSS = f.read()

parts = []


def top_note():
    parts.append('<div class="doc-top-note">Recensione Goldbet 2026&nbsp;&nbsp;|&nbsp;&nbsp;Aggiornamento: Settembre 2026</div>')


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
title("RECENSIONE GOLDBET 2026", "Analisi completa dell'operatore")
rating_box(
    "⭐ 4/5",
    "Fino a 2.050€ di benvenuto", "Sport (100% fino a 50€ + 100% fino a 2.000€)",
    "App 4,8/5", "circa 25.000 valutazioni",
)
cta("VAI SU GOLDBET")
divider()

h1("INFORMAZIONI ESSENZIALI")
info_table([
    ("Licenza operativa", "ADM, concessione n. 16009 (subentrata a una concessione precedente con il nuovo bando ADM)"),
    ("Proprietà", "GBO Italy S.p.A., nata a metà giugno 2022 dalla fusione per incorporazione di Lottomatica Scommesse in Goldbet, parte del Gruppo Lottomatica, quotato su Euronext Milan e nel FTSE MIB. Stesso gruppo di Betflag, Planetwin365 e Lottomatica"),
    ("Bonus benvenuto", "100% sul primo deposito fino a 50€, più un secondo 100% fino a 2.000€ (Multi Chance): totale nominale fino a 2.050€"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento, rollover 6 volte l'importo su entrambe le componenti"),
    ("App disponibili", "iOS su App Store, Android via APK diretto dal sito (non presente su Google Play)"),
    ("Metodi di pagamento", "Carte Visa e Mastercard, PostePay, Apple Pay, PayPal, Skrill, Neteller, bonifico bancario, MyBank, OnShop, Ricarica Voucher"),
    ("Servizio clienti", "Telefono 02 30453039 (feriali 9:00-20:00) o 06 40400860 (7 giorni su 7, 9:00-22:00), live chat, email assistenza@goldbet.it"),
    ("Deposito minimo", "2€ su OnShop e Ricarica Voucher, 20€ per la maggior parte degli altri metodi e per l'attivazione del bonus"),
    ("Registrazione rapida", "SPID e CIE non più disponibili dal 13 novembre 2025"),
])

callout_box("PERCHÉ GOLDBET POTREBBE NON FARE AL CASO TUO", [
    "SPID e CIE non più utilizzabili per la registrazione dal 13 novembre 2025: l'accesso rapido via identità digitale non è più un'opzione",
    "L'app non è disponibile su Google Play (motivo non dichiarato dall'operatore): su Android richiede il download di un APK direttamente dal sito",
    "L'assistenza clienti resta l'area con più margine di miglioramento del gruppo: il dato Trustpilot lo conferma",
])
divider()

h1("PREFAZIONE")
body("Goldbet nasce in Austria nel 2000 come operatore specializzato in scommesse sportive, e nel 2015 sbarca in Italia ottenendo la concessione ADM per il gioco a distanza. Sette anni dopo, a metà giugno 2022, il marchio cambia pelle: la fusione per incorporazione di Lottomatica Scommesse in Goldbet dà vita a GBO Italy S.p.A., con sede a Roma, saldamente dentro il Gruppo Lottomatica.")
body("Betflag entra nello stesso portafoglio nel novembre 2022, Planetwin365 con il completamento dell'acquisizione di SKS365 nell'aprile 2024: tre marchi arrivati in momenti diversi, che il giocatore incontra come alternative distinte ma che oggi rispondono alla stessa proprietà, quotata su Euronext Milan e nel FTSE MIB. Rispetto ai fratelli di portafoglio, Goldbet si è costruita negli anni la reputazione di prodotto solido e giocabile, con un'app tra le più apprezzate della categoria e, diversamente da quanto talvolta si legge, una rete di agenzie fisiche che affianca l'online. Questa recensione analizza bonus, palinsesto, casinò e sicurezza di un operatore che il mercato conosce bene, insieme al punto su cui il gruppo ha ancora del lavoro da fare.")
divider()

h1("VALUTAZIONI")
data_table(
    ["Categoria", "Voto", "Nota sintetica"],
    [
        ["Palinsesto sportivo", "7.5/10", "Oltre 40 discipline, fino a 600 mercati sui grandi match"],
        ["Quote e payout", "7/10", "Nella media del mercato ADM"],
        ["Bonus e promozioni", "7/10", "Fino a 2.050€ nominali, struttura standard di gruppo"],
        ["App e mobile", "8.5/10", "4,8/5 su circa 25.000 valutazioni, tra le migliori della categoria"],
        ["Live streaming", "6.5/10", "Copertura non sistematica, concentrata sui campionati minori"],
        ["Casinò e slot", "8/10", "Oltre 3.000 giochi, 18+ provider, live con Evolution, Playtech Live e MediaLive"],
        ["Metodi di pagamento", "8/10", "Ventaglio ampio, deposito minimo di 2€ su OnShop e voucher"],
        ["Assistenza clienti", "5.5/10", "Trustpilot 2,1/5, criticità che secondo chi opera nel settore riflette un problema reale"],
        ["Sicurezza e compliance", "8.5/10", "Licenza ADM, gruppo quotato su Euronext Milan e nel FTSE MIB"],
    ],
    highlight_col=1,
)
average_score("Valutazione media complessiva: 7.4/10")
divider()

h1("PRO &amp; CONTRO")
h2("Perché scegliere Goldbet (Pro)")
body("Tra gli scommettitori, Goldbet gode di una buona reputazione: nel giudizio di chi segue il settore da anni è un prodotto solido su piazzabilità, giocabilità e affidabilità generale, anche in virtù del legame con uno dei gruppi più importanti del mercato italiano. Il legame con Lottomatica Group, quotato su Euronext Milan e nel FTSE MIB, colloca Goldbet in una struttura societaria più solida di quella di molti concessionari indipendenti.")
body("Sul trattamento dei giocatori vincenti e dei bonus abuser, secondo la stessa fonte Goldbet si colloca sulla linea degli altri brand del gruppo già passati sotto questa lente (Betflag, Planetwin365, Lottomatica), senza differenze sostanziali segnalate.")
body("L'app, disponibile su App Store, raccoglie una valutazione media di 4,8/5 su circa 25.000 valutazioni: un risultato tra i migliori dell'intera serie, che conferma la reputazione del prodotto tra gli utenti più attivi.")
body("Il casinò online supera i 3.000 giochi distribuiti su oltre 18 provider, tra cui Playtech, NetEnt, Spribe e Nolimit City. La sezione live si appoggia a Evolution Gaming, Playtech Live e MediaLive Casino su oltre 100 tavoli, e include tavoli brandizzati in esclusiva per Goldbet: Goldbet 21, Goldbet 21 VIP e Goldbet Sport Roulette.")
body("Il bonus di benvenuto arriva fino a 2.050€ nominali, con la stessa struttura in due componenti già vista su Lottomatica: un primo 100% fino a 50€ e un secondo 100% fino a 2.000€, entrambi attivabili con un deposito minimo di 20€.")
h2("Dove Goldbet può migliorare (Contro)")
body("Il dato più critico riguarda ancora una volta l'assistenza, ma qui il quadro pesa più che altrove nella serie: su Trustpilot, Goldbet raccoglie un punteggio di 2,1/5 su 1.129 recensioni, con l'82% dei giudizi a una stella. Secondo il giudizio editoriale di chi segue il settore da anni, qui il dato non è solo la distorsione tipica delle piattaforme di recensioni negative: riflette una superficialità reale nella gestione del cliente, con una struttura difficile da interfacciare anche per chi lavora all'interno dello stesso ecosistema Goldbet.")
body("Sempre secondo questo giudizio, negli ultimi mesi l'operatore avrebbe intensificato le procedure di verifica e blocco sui conti con attività ritenute sospette: una linea più rigorosa, percepita come un ulteriore ostacolo anche se coerente con una tendenza più ampia del comparto regolamentato.")
body("La registrazione tramite SPID non è più disponibile dal 13 novembre 2025, in coincidenza con il nuovo regime di rilascio delle concessioni online varato da ADM, e la CIE non è un'alternativa attiva per la registrazione (resta valida come documento d'identità caricato a corredo). L'app, infine, non è disponibile su Google Play: su Android l'unica via è il download diretto di un APK dal sito.")
divider()

h1("PANORAMICA TRA EVENTI E STREAMING")
body("Il palinsesto di Goldbet copre oltre 40 discipline sportive: dal calcio, sempre il prodotto trainante, a basket, tennis, pallavolo, hockey su ghiaccio e rugby, fino a discipline meno centrali nel mercato ADM come scacchi, freccette e surf. Sui grandi match il ventaglio di mercati arriva fino a 600, mentre anche sugli eventi minori la soglia supera regolarmente i 200 mercati, per un totale di circa 200 eventi coperti ogni giorno.")
body("Lo streaming live non è sistematico e resta concentrato soprattutto sui campionati minori, con una presenza comunque su alcuni grandi tornei: Serie A, Serie B, Bundesliga e basket NBA compaiono nella copertura, ma non su ogni singolo evento delle rispettive competizioni.")
divider()

h1("TIPOLOGIA DI GIOCHI DISPONIBILI")
body("<b>Scommesse sportive</b>: pre-match e live, oltre 40 discipline, fino a 600 mercati sui grandi match.")
body("<b>Casinò online</b>: oltre 3.000 giochi distribuiti su più di 18 provider, tra cui Playtech, NetEnt, Spribe, ELK, Nolimit City, Inspired e WorldMatch.")
body("<b>Casinò live</b>: oltre 100 tavoli attivi 24 ore su 24, con Evolution Gaming, Playtech Live e MediaLive Casino, inclusi i tavoli esclusivi Goldbet 21, Goldbet 21 VIP e Goldbet Sport Roulette.")
body("<b>Poker</b>: tavoli cash e tornei, accessibili via software dedicato e app.")
body("<b>Bingo e lotterie</b>: sezione dedicata con montepremi settimanali, supportata da un'app Bingo separata.")
divider()

h1("PROMOZIONI")
h2("Bonus di benvenuto — prima componente")
info_table([
    ("Percentuale e massimale", "100% sul primo deposito, fino a 50€"),
    ("Deposito minimo qualificante", "20€, entro 7 giorni dalla registrazione"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento"),
])
h2("Bonus di benvenuto — seconda componente (Multi Chance)")
info_table([
    ("Percentuale e massimale", "Ulteriore 100% sul primo deposito, fino a 2.000€"),
    ("Rollover", "6 volte l'importo, su multiple da almeno 3 eventi a quota minima 1,50"),
    ("Finestra temporale", "Da completare entro 30 giorni dalla registrazione"),
])
note_box("Nota importante", "Metodi di ricarica esclusi dall'attivazione del bonus: Skrill, Neteller, OnShop, MyBank, Ricarica Voucher. Tutte le condizioni sono soggette ad aggiornamento da parte dell'operatore: verificare sempre i T&amp;C ufficiali prima dell'attivazione.")
divider()

h1("INFO SULLE QUOTE, MERCATI E FUNZIONALITÀ")
body("Goldbet costruisce l'offerta scommesse su un palinsesto ampio, oltre 40 discipline con calcio, basket e tennis a fare da traino, ma con una copertura che si estende fino a sport di nicchia come scacchi e freccette. Sui grandi appuntamenti il numero di mercati disponibili, fino a 600, è tra i più alti della categoria.")
h2("Come piazzare una scommessa su Goldbet")
body("<b>STEP 1: Scegli l'evento</b> — Naviga il palinsesto sportivo online o da app. Seleziona il mercato e la quota desiderata.")
body("<b>STEP 2: Componi la giocata</b> — Inserisci l'importo. Aggiungi altri eventi per una multipla, verificando che la quota totale rispetti eventuali requisiti bonus attivi.")
body("<b>STEP 3: Conferma</b> — Conferma la giocata. La ricevuta appare in tempo reale nella cronologia del conto gioco.")
divider()

h1("CONTO DI SCOMMESSA E REGISTRAZIONE")
body("<b>Registrazione</b>: compilazione del modulo con dati anagrafici, codice fiscale, email e numero di telefono, seguita dal caricamento di un documento d'identità valido. Dal 13 novembre 2025 non è più possibile registrarsi tramite SPID; la CIE non è al momento un'alternativa disponibile.")
body("<b>Requisiti di base</b>: maggiore età (18 anni), residenza in Italia, documento d'identità in corso di validità. Il conto gioco è infruttifero e personale: un solo conto per numero di concessione per ciascun cliente.")
divider()

h1("METODI DI PAGAMENTO")
data_table(
    ["Metodo", "Deposito minimo", "Prelievo"],
    [
        ["Carte Visa / Mastercard", "20€", "Sì, fino a 2.000€ per operazione"],
        ["PostePay", "20€", "Sì"],
        ["Apple Pay", "20€", "Sì, a determinate condizioni"],
        ["PayPal", "20€", "Sì, fino a 5.000€"],
        ["Skrill / Neteller", "10€", "Sì, fino a 5.000€ (non attivano il bonus)"],
        ["Bonifico bancario", "5€", "Sì"],
        ["MyBank", "10€", "Solo deposito (non attiva il bonus)"],
        ["OnShop / Ricarica Voucher", "2€", "Solo deposito (non attivano il bonus)"],
    ],
)
body("Per le carte, i prelievi vengono generalmente elaborati in 24-48 ore lavorative dalla conferma dell'operazione; per gli altri metodi le tempistiche possono variare in base ai controlli antifrode.")
divider()

h1("SICUREZZA")
body("<b>Licenza ADM</b>: concessione n. 16009, in capo a GBO Italy S.p.A. Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana.")
body("<b>Struttura societaria</b>: GBO Italy S.p.A. è parte del Gruppo Lottomatica, quotato su Euronext Milan dal maggio 2023 ed entrato nel FTSE MIB da settembre 2025, uno dei 40 titoli più liquidi e capitalizzati della Borsa italiana. La quotazione non costituisce di per sé una garanzia specifica per il cliente, ma colloca il gruppo controllante in una fascia di trasparenza societaria superiore a quella di un concessionario indipendente non quotato.")
body("<b>Gioco responsabile</b>: strumenti di auto-limitazione dei depositi, autoesclusione temporanea o permanente, limiti di durata delle sessioni e test di autovalutazione, in conformità con le normative ADM.")
divider()

h1("SERVE AIUTO? CUSTOMER SUPPORT")
body("Il servizio clienti è raggiungibile tramite telefono (02 30453039 nei giorni feriali dalle 9:00 alle 20:00, oppure 06 40400860 tutti i giorni dalle 9:00 alle 22:00), live chat sul sito ed email (assistenza@goldbet.it, oltre a indirizzi dedicati per contratti e reclami).")
body("Su Trustpilot l'operatore raccoglie un punteggio di 2,1/5 su 1.129 recensioni, con l'82% dei giudizi a una stella: il dato più critico dell'intera recensione, discusso nel dettaglio in Pro &amp; Contro.")
divider()

h1("ALTRI PRODOTTI NELL'OFFERTA")
body("<b>Poker</b>: tavoli cash e tornei, via software dedicato e app.")
body("<b>Bingo e lotterie</b>: sezione con montepremi settimanali, supportata da un'app Bingo separata da quella scommesse.")
divider()

h1("FEEDBACK E RECENSIONI")
body("Sull'App Store, l'app Goldbet raggiunge una valutazione media di 4,8/5 su circa 25.000 valutazioni: uno dei risultati migliori tra tutti gli operatori passati sotto questa lente.")
body("Il quadro cambia radicalmente su Trustpilot, dove Goldbet registra un punteggio di 2,1/5 su 1.129 recensioni, con l'82% dei giudizi a una stella. La divaricazione tra i due canali è ampia quanto quella già vista su altri brand del gruppo, ma qui il rilievo ha più sostanza: riflette un problema reale di gestione del cliente più che una distorsione del canale.")
divider()

h1("TABELLA COMPARATIVA: GOLDBET VS SNAI VS LOTTOMATICA")
data_table(
    ["Caratteristica", "Goldbet", "SNAI", "Lottomatica"],
    [
        ["Bonus sport", "100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (rollover x6)", "500€ Gold (x6) + 500€ Game Bonus + 15€ free + 9€ extra = 1.024€", "100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (rollover x6)"],
        ["Deposito minimo bonus", "20€", "Non specificato in questa serie", "20€"],
        ["Proprietà", "GBO Italy S.p.A. (Gruppo Lottomatica)", "Gruppo Flutter Entertainment (dal 2025)", "Lottomatica Group (capofila)"],
        ["Prodotto distintivo", "App tra le più valutate della categoria (4,8/5); rete di agenzie fisiche affiancata all'online", "Ippica, Snaipay, integrazione fisico-digitale", "Rete fisica capillare: oltre 4.000 agenzie, 1.100 sale gioco"],
        ["Registrazione SPID/CIE", "Non disponibile dal 13/11/2025", "Sì", "Non disponibile dal 13/11/2025"],
        ["Licenza ADM", "16009", "Non riportata in questa serie", "16010"],
    ],
)
body("<b>Nota</b>: le cifre di tutti gli operatori rappresentano valori nominali massimi, soggetti a rollover e condizioni di sblocco spesso complesse. Goldbet e Lottomatica condividono oggi la stessa proprietà: la tabella li mette a confronto come prodotti distinti, non come alternative indipendenti.", size=9)
divider()

h1("IL NOSTRO GIUDIZIO")
body("Goldbet arriva al 2026 con un percorso diverso dagli altri marchi già passati sotto questa lente: nasce online in Austria nel 2000, opera come concessionario indipendente in Italia dal 2015, e solo nel giugno 2022, con la fusione in GBO Italy S.p.A., entra nel Gruppo Lottomatica. Betflag la raggiunge a novembre dello stesso anno, Planetwin365 nel 2024.")
body("Sul prodotto, la sintesi di questa recensione è positiva: reputazione solida, app tra le meglio valutate della serie (4,8/5 su circa 25.000 valutazioni), trattamento dei vincenti in linea con gli altri brand del gruppo secondo il giudizio raccolto. Il vero scarto rispetto ai fratelli di portafoglio è sull'assistenza (dettagli in Pro &amp; Contro): qui il divario tra qualità del prodotto e qualità del servizio al cliente è il più ampio registrato finora nella serie, e richiederebbe un investimento reale in fidelizzazione più che un intervento cosmetico.")
body("Chi cerca un'app solida, un gruppo affidabile alle spalle e un trattamento corretto sulle vincite trova in Goldbet una scelta valida. Chi mette l'assistenza e la rapidità di risoluzione dei problemi tra i criteri decisivi farebbe bene a mettere in conto che qui il margine di miglioramento resta il più ampio del gruppo.")
body("Il voto finale è una sintesi editoriale e non una conversione meccanica della media delle valutazioni per categoria (7,4/10): pesa quanto l'assistenza incide sull'esperienza di chi scommette con regolarità, un fattore rilevante ma non tale da annullare la solidità del resto dell'offerta.")
final_score_box("VOTO FINALE: 4 SU 5")
divider()

h1("FAQ")
h2("Goldbet è sicuro?")
body("Opera sotto concessione ADM n. 16009, in capo a GBO Italy S.p.A., parte del Gruppo Lottomatica, quotato su Euronext Milan e nel FTSE MIB: un gruppo tra i più solidi del mercato italiano regolamentato.")
h2("È possibile registrarsi con SPID o CIE su Goldbet?")
body("No. Dal 13 novembre 2025 nessuna delle due opzioni è più disponibile. La registrazione richiede l'inserimento manuale dei dati e il caricamento di un documento d'identità.")
h2("In cosa Goldbet è diverso dagli altri brand del gruppo (Betflag, Planetwin365, Lottomatica)?")
body("Stessa proprietà, ma un'app tra le più apprezzate della categoria. Ha anche una propria rete di agenzie fisiche, più contenuta di quella di Lottomatica ma comunque presente.")
h2("Qual è il punto debole principale di Goldbet?")
body("L'assistenza clienti: Trustpilot assegna un punteggio di 2,1/5, e chi opera nel settore conferma una struttura poco flessibile nella gestione dei problemi, anche per chi lavora all'interno dello stesso ecosistema.")
divider()

h1("LE MIGLIORI ALTERNATIVE")
body("<b>Lottomatica</b>: stesso gruppo proprietario, unico brand con rete fisica capillare (oltre 4.000 agenzie, 1.100 sale gioco), bonus fino a 2.050€.")
body("<b>Planetwin365</b>: stesso gruppo dal 2024, casinò live con tavoli esclusivi Evolution, bonus fino a 2.100€ tra sport e slot.")
body("<b>SNAI</b>: leadership storica nell'ippica, integrazione fisico-digitale con Snaipay, rollover x6 sul Bonus Gold tra i più accessibili del mercato.")

plain_note("Il gioco è vietato ai minori di 18 anni • Bonus e T&amp;C soggetti a modifica: verificare sempre su goldbet.it")

html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Recensione Goldbet 2026</title>
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Salvato:", OUT_HTML)
