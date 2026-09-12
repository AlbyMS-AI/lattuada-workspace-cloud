import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_template"))
import review_docx_builder as b

OUT = os.path.join(os.path.dirname(__file__), "recensione-goldbet-2026.docx")

doc = b.new_document()
b.set_header_footer(doc, "Recensione Goldbet 2026  |  Aggiornamento: Settembre 2026")

b.add_title(doc, "RECENSIONE GOLDBET 2026", "Analisi completa dell'operatore")

b.add_rating_box(
    doc,
    "⭐ 4/5",
    "Fino a 2.050€ di benvenuto", "Sport (100% fino a 50€ + 100% fino a 2.000€)",
    "App 4,8/5", "circa 25.000 recensioni",
)
b.add_cta_bar(doc, "VAI SU GOLDBET")
b.add_divider(doc)

b.add_h1(doc, "INFORMAZIONI ESSENZIALI")
b.add_info_table(doc, [
    ("Licenza operativa", "ADM, concessione n. 16009 (subentrata alla precedente GAD 15226 con il nuovo bando ADM)"),
    ("Proprietà", "GBO Italy S.p.A., nata a metà giugno 2022 dalla fusione per incorporazione di Lottomatica Scommesse in Goldbet, parte del Gruppo Lottomatica, quotato su Euronext Milan e nel FTSE MIB. Stesso gruppo di Betflag, Planetwin365 e Lottomatica"),
    ("Bonus benvenuto", "100% sul primo deposito fino a 50€, più un secondo 100% fino a 2.000€ (Multi Chance): totale nominale fino a 2.050€"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento, rollover 6 volte l'importo su entrambe le componenti"),
    ("App disponibili", "iOS su App Store, Android via APK diretto dal sito (non presente su Google Play per policy sul gioco d'azzardo)"),
    ("Metodi di pagamento", "Carte Visa e Mastercard, PostePay, Apple Pay, PayPal, Skrill, Neteller, bonifico bancario, MyBank, OnShop, Ricarica Voucher"),
    ("Servizio clienti", "Telefono 02 30453039 (feriali 9:00-20:00) o 06 40400860 (7 giorni su 7, 9:00-22:00), live chat, email assistenza@goldbet.it"),
    ("Deposito minimo", "2€ su OnShop e Ricarica Voucher, 20€ per la maggior parte degli altri metodi e per l'attivazione del bonus"),
    ("Registrazione rapida", "SPID e CIE non più disponibili dal 13 novembre 2025"),
])

b.add_callout_box(doc, "PERCHÉ GOLDBET POTREBBE NON FARE AL CASO TUO", [
    "SPID e CIE non più utilizzabili per la registrazione dal 13 novembre 2025: l'accesso rapido via identità digitale non è più un'opzione",
    "L'app non è disponibile su Google Play: su Android richiede il download di un APK direttamente dal sito",
    "L'assistenza clienti resta l'area con più margine di miglioramento del gruppo: il dato Trustpilot lo conferma",
])
b.add_divider(doc)

b.add_h1(doc, "PREFAZIONE")
b.add_body(doc, "Goldbet nasce in Austria nel 2000 come operatore specializzato in scommesse sportive, e nel 2015 sbarca in Italia ottenendo la concessione ADM per il gioco a distanza. Nove anni dopo, a metà giugno 2022, il marchio cambia pelle: la fusione per incorporazione di Lottomatica Scommesse in Goldbet dà vita a GBO Italy S.p.A., con sede a Roma, saldamente dentro il Gruppo Lottomatica.")
b.add_body(doc, "Da quel momento Goldbet condivide la proprietà con Betflag, Planetwin365 e Lottomatica, tre marchi che il giocatore incontra come alternative distinte ma che rispondono allo stesso gruppo, oggi quotato su Euronext Milan e nel FTSE MIB. Rispetto ai fratelli di portafoglio, Goldbet si è costruita negli anni la reputazione di prodotto solido e giocabile, con un'app tra le più apprezzate della categoria. Questa recensione analizza bonus, palinsesto, casinò e sicurezza di un operatore che il mercato conosce bene, insieme al punto su cui il gruppo ha ancora del lavoro da fare.")
b.add_divider(doc)

b.add_h1(doc, "VALUTAZIONI")
b.add_data_table(
    doc,
    ["Categoria", "Voto", "Nota sintetica"],
    [
        ["Palinsesto sportivo", "7.5/10", "Oltre 40 discipline, fino a 600 mercati sui grandi match"],
        ["Quote e payout", "7/10", "Nella media del mercato ADM"],
        ["Bonus e promozioni", "7/10", "Fino a 2.050€ nominali, struttura standard di gruppo"],
        ["App e mobile", "8.5/10", "4,8/5 su circa 25.000 recensioni, tra le migliori della categoria"],
        ["Live streaming", "6.5/10", "Copertura non sistematica, concentrata sui campionati minori"],
        ["Casinò e slot", "8/10", "Oltre 3.000 giochi, 18+ provider, live con Evolution, Playtech Live e MediaLive"],
        ["Metodi di pagamento", "8/10", "Ventaglio ampio, deposito minimo di 2€ su OnShop e voucher"],
        ["Assistenza clienti", "5.5/10", "Trustpilot 2,1/5, criticità che secondo chi opera nel settore riflette un problema reale"],
        ["Sicurezza e compliance", "8.5/10", "Licenza ADM, gruppo quotato su Euronext Milan e nel FTSE MIB"],
    ],
    highlight_col=1,
    col_widths=None,
)
b.add_average_score(doc, "Valutazione media complessiva: 7.4/10")
b.add_divider(doc)

b.add_h1(doc, "PRO & CONTRO")
b.add_h2(doc, "Perché scegliere Goldbet (Pro)")
b.add_body(doc, "Tra gli scommettitori, Goldbet gode di una buona reputazione: viene considerato un prodotto solido su piazzabilità, giocabilità e affidabilità generale, un giudizio che si appoggia anche al fatto di essere legato a uno dei gruppi più importanti del mercato italiano. Il legame con Lottomatica Group, quotato su Euronext Milan e nel FTSE MIB, offre una garanzia patrimoniale che pochi concessionari indipendenti possono vantare.")
b.add_body(doc, "Sul trattamento dei giocatori vincenti e dei bonus abuser, Goldbet si colloca sulla stessa linea degli altri brand del gruppo già passati sotto questa lente (Betflag, Planetwin365, Lottomatica): nessuna limitazione facile, un comportamento coerente con lo standard che il gruppo si è dato.")
b.add_body(doc, "L'app, disponibile su App Store, raccoglie una valutazione media di 4,8/5 su circa 25.000 recensioni: un risultato tra i migliori dell'intera serie, che conferma la reputazione del prodotto tra gli utenti più attivi.")
b.add_body(doc, "Il casinò online supera i 3.000 giochi distribuiti su oltre 18 provider, tra cui Playtech, NetEnt, Spribe e Nolimit City. La sezione live, con oltre 100 tavoli attivi 24 ore su 24, si appoggia a Evolution Gaming, Playtech Live e MediaLive Casino, e include tavoli brandizzati in esclusiva per Goldbet: Goldbet 21, Goldbet 21 VIP e Goldbet Sport Roulette.")
b.add_body(doc, "Il bonus di benvenuto arriva fino a 2.050€ nominali, con la stessa struttura in due componenti già vista su Lottomatica: un primo 100% fino a 50€ e un secondo 100% fino a 2.000€, entrambi attivabili con un deposito minimo di 20€.")

b.add_h2(doc, "Dove Goldbet può migliorare (Contro)")
b.add_body(doc, "Il dato più critico riguarda ancora una volta l'assistenza, ma qui il quadro pesa più che altrove nella serie: su Trustpilot, Goldbet raccoglie un punteggio di 2,1/5 su 1.129 recensioni, con l'82% dei giudizi a una stella. A differenza di quanto osservato su altri brand dello stesso gruppo, questo non è un dato che chi lavora nel settore derubrica a percezione distorta: riflette una superficialità reale nella gestione del cliente, che rende difficile interfacciarsi con l'operatore, anche per chi opera all'interno del suo stesso ecosistema. Una struttura troppo rigida per essere davvero flessibile sul problem solving, quando servirebbe il contrario.")
b.add_body(doc, "Negli ultimi mesi, inoltre, l'operatore ha intensificato le procedure di verifica e blocco sui conti con attività ritenute sospette: una linea più rigorosa che si inserisce in una tendenza più ampia del comparto regolamentato, ma che pesa sulla percezione complessiva del servizio.")
b.add_body(doc, "La registrazione tramite SPID non è più disponibile dal 13 novembre 2025, in coincidenza con il nuovo regime di rilascio delle concessioni online varato da ADM, e la CIE non è un'alternativa attiva: chi cerca l'accesso più rapido tramite identità digitale deve procedere con l'inserimento manuale dei dati. L'app, infine, non è disponibile su Google Play: su Android l'unica via è il download diretto di un APK dal sito.")
b.add_divider(doc)

b.add_h1(doc, "PANORAMICA TRA EVENTI E STREAMING")
b.add_body(doc, "Il palinsesto di Goldbet copre oltre 40 discipline sportive: dal calcio, sempre il prodotto trainante, a basket, tennis, pallavolo, hockey su ghiaccio e rugby, fino a discipline meno centrali nel mercato ADM come scacchi, freccette e surf. Sui grandi match il ventaglio di mercati arriva fino a 600, mentre anche sugli eventi minori la soglia supera regolarmente i 200 mercati, per un totale di circa 200 eventi coperti ogni giorno.")
b.add_body(doc, "Lo streaming live non è sistematico e resta concentrato soprattutto sui campionati minori, con una presenza comunque su alcuni grandi tornei: Serie A, Serie B, Bundesliga e basket NBA compaiono nella copertura, ma non su ogni singolo evento delle rispettive competizioni.")
b.add_divider(doc)

b.add_h1(doc, "TIPOLOGIA DI GIOCHI DISPONIBILI")
b.add_body(doc, "**Scommesse sportive**: pre-match e live, oltre 40 discipline, fino a 600 mercati sui grandi match.")
b.add_body(doc, "**Casinò online**: oltre 3.000 giochi distribuiti su più di 18 provider, tra cui Playtech, NetEnt, Spribe, ELK, Nolimit City, Inspired e WorldMatch.")
b.add_body(doc, "**Casinò live**: oltre 100 tavoli attivi 24 ore su 24, con Evolution Gaming, Playtech Live e MediaLive Casino, inclusi i tavoli esclusivi Goldbet 21, Goldbet 21 VIP e Goldbet Sport Roulette.")
b.add_body(doc, "**Poker**: tavoli cash e tornei, accessibili via software dedicato e app.")
b.add_body(doc, "**Bingo e lotterie**: sezione dedicata con montepremi settimanali, supportata da un'app Bingo separata.")
b.add_divider(doc)

b.add_h1(doc, "PROMOZIONI")
b.add_h2(doc, "Bonus di benvenuto — prima componente")
b.add_info_table(doc, [
    ("Percentuale e massimale", "100% sul primo deposito, fino a 50€"),
    ("Deposito minimo qualificante", "20€, entro 7 giorni dalla registrazione"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento"),
])
b.add_h2(doc, "Bonus di benvenuto — seconda componente (Multi Chance)")
b.add_info_table(doc, [
    ("Percentuale e massimale", "Ulteriore 100% sul primo deposito, fino a 2.000€"),
    ("Rollover", "6 volte l'importo, su multiple da almeno 3 eventi a quota minima 1,50"),
    ("Finestra temporale", "Da completare entro 30 giorni dalla registrazione"),
])
b.add_note_box(doc, "Nota importante", "Metodi di ricarica esclusi dall'attivazione del bonus: Skrill, Neteller, OnShop, MyBank, Ricarica Voucher. Tutte le condizioni sono soggette ad aggiornamento da parte dell'operatore: verificare sempre i T&C ufficiali prima dell'attivazione.")
b.add_divider(doc)

b.add_h1(doc, "INFO SULLE QUOTE, MERCATI E FUNZIONALITÀ")
b.add_body(doc, "Goldbet costruisce l'offerta scommesse su un palinsesto ampio, oltre 40 discipline con calcio, basket e tennis a fare da traino, ma con una copertura che si estende fino a sport di nicchia come scacchi e freccette. Sui grandi appuntamenti il numero di mercati disponibili, fino a 600, è tra i più alti della categoria.")

b.add_h2(doc, "Come piazzare una scommessa su Goldbet")
b.add_body(doc, "**STEP 1: Scegli l'evento** — Naviga il palinsesto sportivo online o da app. Seleziona il mercato e la quota desiderata.")
b.add_body(doc, "**STEP 2: Componi la giocata** — Inserisci l'importo. Aggiungi altri eventi per una multipla, verificando che la quota totale rispetti eventuali requisiti bonus attivi.")
b.add_body(doc, "**STEP 3: Conferma** — Conferma la giocata. La ricevuta appare in tempo reale nella cronologia del conto gioco.")
b.add_divider(doc)

b.add_h1(doc, "CONTO DI SCOMMESSA E REGISTRAZIONE")
b.add_body(doc, "**Registrazione**: compilazione del modulo con dati anagrafici, codice fiscale, email e numero di telefono, seguita dal caricamento di un documento d'identità valido. Dal 13 novembre 2025 non è più possibile registrarsi tramite SPID; la CIE non è al momento un'alternativa disponibile.")
b.add_body(doc, "**Requisiti di base**: maggiore età (18 anni), residenza in Italia, documento d'identità in corso di validità. Il conto gioco è infruttifero e personale: un solo conto per numero di concessione per ciascun cliente.")
b.add_divider(doc)

b.add_h1(doc, "METODI DI PAGAMENTO")
b.add_data_table(
    doc,
    ["Metodo", "Deposito minimo", "Prelievo"],
    [
        ["Carte Visa / Mastercard", "20€", "Sì, fino a 2.000€ per operazione"],
        ["PostePay", "20€", "Sì"],
        ["Apple Pay", "20€", "Sì"],
        ["PayPal", "20€", "Sì, fino a 5.000€"],
        ["Skrill / Neteller", "10€", "Sì, fino a 5.000€ (non attivano il bonus)"],
        ["Bonifico bancario", "5€", "Sì"],
        ["MyBank", "10€", "Sì (non attiva il bonus)"],
        ["OnShop / Ricarica Voucher", "2€", "Solo deposito (non attivano il bonus)"],
    ],
    highlight_col=None,
)
b.add_body(doc, "I prelievi vengono generalmente elaborati in 24-48 ore, con tempistiche che possono variare in base al metodo scelto e ai controlli antifrode.")
b.add_divider(doc)

b.add_h1(doc, "SICUREZZA")
b.add_body(doc, "**Licenza ADM**: concessione n. 16009, in capo a GBO Italy S.p.A. Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana.")
b.add_body(doc, "**Garanzia patrimoniale**: GBO Italy S.p.A. è parte del Gruppo Lottomatica, quotato su Euronext Milan dal maggio 2023 ed entrato nel FTSE MIB da settembre 2025, uno dei 40 titoli più liquidi e capitalizzati della Borsa italiana.")
b.add_body(doc, "**Gioco responsabile**: strumenti di auto-limitazione dei depositi, autoesclusione temporanea o permanente, limiti di durata delle sessioni e test di autovalutazione, in conformità con le normative ADM.")
b.add_divider(doc)

b.add_h1(doc, "SERVE AIUTO? CUSTOMER SUPPORT")
b.add_body(doc, "Il servizio clienti è raggiungibile tramite telefono (02 30453039 nei giorni feriali dalle 9:00 alle 20:00, oppure 06 40400860 tutti i giorni dalle 9:00 alle 22:00), live chat sul sito ed email (assistenza@goldbet.it, oltre a indirizzi dedicati per contratti e reclami).")
b.add_body(doc, "Su Trustpilot l'operatore raccoglie un punteggio di 2,1/5 su 1.129 recensioni, con l'82% dei giudizi a una stella. A differenza di quanto emerso su altri brand della stessa serie, qui il dato non va derubricato a percezione distorta: chi lavora nel settore conferma che interfacciarsi con Goldbet, anche dall'interno del suo stesso ecosistema, è più complicato del dovuto, con una struttura poco flessibile nella risoluzione dei problemi. Per colmare davvero il divario servirebbe un investimento serio in fidelizzazione, con il giocatore al centro del servizio, non solo del prodotto.")
b.add_divider(doc)

b.add_h1(doc, "ALTRI PRODOTTI NELL'OFFERTA")
b.add_body(doc, "**Poker**: tavoli cash e tornei, via software dedicato e app.")
b.add_body(doc, "**Bingo e lotterie**: sezione con montepremi settimanali, supportata da un'app Bingo separata da quella scommesse.")
b.add_divider(doc)

b.add_h1(doc, "FEEDBACK E RECENSIONI")
b.add_body(doc, "Sull'App Store, l'app Goldbet raggiunge una valutazione media di 4,8/5 su circa 25.000 recensioni: uno dei risultati migliori tra tutti gli operatori passati sotto questa lente.")
b.add_body(doc, "Il quadro cambia radicalmente su Trustpilot, dove Goldbet registra un punteggio di 2,1/5 su 1.129 recensioni, con l'82% dei giudizi a una stella. La divaricazione tra i due canali è ampia quanto quella già vista su altri brand del gruppo, ma qui il rilievo ha più sostanza: riflette un problema reale di gestione del cliente più che una distorsione del canale.")
b.add_divider(doc)

b.add_h1(doc, "TABELLA COMPARATIVA: GOLDBET VS SNAI VS LOTTOMATICA")
b.add_data_table(
    doc,
    ["Caratteristica", "Goldbet", "SNAI", "Lottomatica"],
    [
        ["Bonus sport", "100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (rollover x6)", "500€ Gold (x6) + 500€ Game Bonus + 15€ free + 9€ extra = ~1.500€", "100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (rollover x6)"],
        ["Deposito minimo bonus", "20€", "Non specificato in questa serie", "20€"],
        ["Proprietà", "GBO Italy S.p.A. (Gruppo Lottomatica)", "Gruppo Flutter Entertainment (dal 2025)", "Lottomatica Group (capofila)"],
        ["Prodotto distintivo", "App tra le più valutate della categoria (4,8/5)", "Ippica, Snaipay, integrazione fisico-digitale", "Rete fisica: 4.000+ agenzie, 1.100 sale gioco"],
        ["Registrazione SPID/CIE", "Non disponibile dal 13/11/2025", "Sì", "Non disponibile dal 13/11/2025"],
        ["Licenza ADM", "16009", "Non riportata in questa serie", "16010"],
    ],
    highlight_col=None,
    col_widths=None,
)
b.add_body(doc, "**Nota**: le cifre di tutti gli operatori rappresentano valori nominali massimi, soggetti a rollover e condizioni di sblocco spesso complesse. Goldbet e Lottomatica condividono oggi la stessa proprietà: la tabella li mette a confronto come prodotti distinti, non come alternative indipendenti.", size=9)
b.add_divider(doc)

b.add_h1(doc, "IL NOSTRO GIUDIZIO")
b.add_body(doc, "Goldbet nasce in Austria nel 2000 come specialista di scommesse sportive, sbarca in Italia nel 2015 con la propria concessione ADM, e a metà giugno 2022 la fusione con Lottomatica Scommesse la porta dentro GBO Italy S.p.A., saldamente nel Gruppo Lottomatica, quotato su Euronext Milan e nel FTSE MIB. Oggi condivide il portafoglio con Betflag, Planetwin365 e Lottomatica, gli altri tre brand già passati sotto questa lente.")
b.add_body(doc, "Tra gli scommettitori, Goldbet mantiene una buona reputazione: prodotto solido su piazzabilità e giocabilità, trattamento dei vincenti e dei bonus abuser in linea con gli altri fratelli di gruppo, e un'app che con 4,8/5 su circa 25.000 recensioni è tra le meglio valutate dell'intera serie. Il bonus di 2.050€ nominali segue la stessa struttura già vista su Lottomatica, e il casinò online, con oltre 3.000 giochi e i tavoli esclusivi firmati Evolution, tiene il passo dei concorrenti diretti.")
b.add_body(doc, "Il punto debole, però, qui pesa più che altrove nella serie. Il punteggio Trustpilot di 2,1/5, con l'82% delle recensioni a una stella, non è liquidabile come un quadro distorto: secondo chi opera nel settore, riflette una superficialità reale nella gestione del cliente, con una struttura che resta difficile da interfacciare anche per chi lavora all'interno dello stesso ecosistema Goldbet. A questo si aggiunge un irrigidimento recente nelle procedure di verifica sui conti, coerente con una tendenza di comparto ma percepito come un ulteriore ostacolo. Per colmare davvero il divario, servirebbe un investimento serio sulla fidelizzazione, che metta il giocatore al centro tanto quanto lo è oggi il prodotto.")
b.add_body(doc, "Chi cerca un'app solida, un gruppo affidabile alle spalle e un trattamento corretto sulle vincite trova in Goldbet una scelta valida. Chi mette l'assistenza e la rapidità nella risoluzione dei problemi tra i criteri decisivi farebbe bene a considerare che qui il margine di miglioramento resta più ampio che sugli altri brand dello stesso gruppo.")
b.add_final_score_box(doc, "VOTO FINALE: 4 SU 5")
b.add_divider(doc)

b.add_h1(doc, "FAQ")
b.add_h2(doc, "Goldbet è sicuro?")
b.add_body(doc, "Opera sotto concessione ADM n. 16009, in capo a GBO Italy S.p.A., parte del Gruppo Lottomatica, quotato su Euronext Milan e nel FTSE MIB: un gruppo tra i più solidi del mercato italiano regolamentato.")
b.add_h2(doc, "È possibile registrarsi con SPID o CIE su Goldbet?")
b.add_body(doc, "No. Dal 13 novembre 2025 nessuna delle due opzioni è più disponibile. La registrazione richiede l'inserimento manuale dei dati e il caricamento di un documento d'identità.")
b.add_h2(doc, "In cosa Goldbet è diverso dagli altri brand del gruppo (Betflag, Planetwin365, Lottomatica)?")
b.add_body(doc, "Stessa proprietà, ma un'app tra le più apprezzate della categoria e un pubblico più giovane. A differenza di Lottomatica, non ha una rete fisica di punti vendita.")
b.add_h2(doc, "Qual è il punto debole principale di Goldbet?")
b.add_body(doc, "L'assistenza clienti: Trustpilot assegna un punteggio di 2,1/5, e chi opera nel settore conferma una struttura poco flessibile nella gestione dei problemi, anche per chi lavora all'interno dello stesso ecosistema.")
b.add_divider(doc)

b.add_h1(doc, "LE MIGLIORI ALTERNATIVE")
b.add_body(doc, "**Lottomatica**: stesso gruppo proprietario, unico brand con rete fisica capillare (oltre 4.000 agenzie, 1.100 sale gioco), bonus fino a 2.050€.")
b.add_body(doc, "**Planetwin365**: stesso gruppo dal 2024, casinò live con tavoli esclusivi Evolution, bonus fino a 2.100€ tra sport e slot.")
b.add_body(doc, "**SNAI**: leadership storica nell'ippica, integrazione fisico-digitale con Snaipay, rollover x6 sul Bonus Gold tra i più accessibili del mercato.")

footer_p = doc.add_paragraph()
from docx.enum.text import WD_ALIGN_PARAGRAPH
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer_p.paragraph_format.space_before = b.Pt(14)
b._add_run(footer_p, "Il gioco è vietato ai minori di 18 anni • Bonus e T&C soggetti a modifica: verificare sempre su goldbet.it", italic=True, color=b.GRAY, size=8)

doc.save(OUT)
print("Salvato:", OUT)
