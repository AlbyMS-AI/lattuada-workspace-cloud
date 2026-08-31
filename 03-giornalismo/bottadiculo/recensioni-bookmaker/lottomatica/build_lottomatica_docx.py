import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_template"))
import review_docx_builder as b

OUT = os.path.join(os.path.dirname(__file__), "recensione-lottomatica-2026.docx")

doc = b.new_document()
b.set_header_footer(doc, "Recensione Lottomatica 2026  |  Aggiornamento: Agosto 2026")

b.add_title(doc, "RECENSIONE LOTTOMATICA 2026", "Analisi completa dell'operatore")

b.add_rating_box(
    doc,
    "⭐ 4/5",
    "Fino a 2.050€ di benvenuto", "Sport (100% fino a 50€ + 100% fino a 2.000€)",
    "4.000+ agenzie", "1.100 sale gioco",
)
b.add_cta_bar(doc, "VAI SU LOTTOMATICA")
b.add_divider(doc)

b.add_h1(doc, "INFORMAZIONI ESSENZIALI")
b.add_info_table(doc, [
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

b.add_callout_box(doc, "PERCHÉ LOTTOMATICA POTREBBE NON FARE AL CASO TUO", [
    "Skrill, Neteller, MyBank e voucher Lottomatica sono esclusi dai metodi che attivano il bonus di benvenuto",
    "Registrazione SPID sospesa dal 13 novembre 2025, CIE non ancora disponibile: chi cerca l'accesso via identità digitale non lo trova",
    "Le multiple minime da 3 eventi richieste per validare entrambe le componenti del bonus spingono spesso a completare la giocata con eventi minori solo per raggiungere la soglia",
])
b.add_divider(doc)

b.add_h1(doc, "PREFAZIONE")
b.add_body(doc, "Lottomatica nasce nel dicembre 1990 a Roma come consorzio per la gestione del Lotto, tra soci come BNL, Olivetti e Sogei. Nel 2006 acquisisce l'americana GTECH per 4 miliardi di euro, diventando il più grande gruppo al mondo nel settore dei giochi. Nel 2015 la fusione con IGT porta alla nascita di International Game Technology PLC, e per alcuni anni il marchio italiano delle scommesse opera come costola di un colosso quotato a Wall Street.")
b.add_body(doc, "Nel 2021 la direzione si inverte: Gamenet Group acquisisce da IGT le quote di Lottomatica Scommesse S.r.l. e Lottomatica Videolot Rete S.p.A., e l'anno seguente adotta il nome Lottomatica per l'intero gruppo. Da maggio 2023 Lottomatica Group è quotata su Euronext Milan, e da settembre 2025 fa parte del FTSE MIB. Nello stesso portafoglio siedono oggi Betflag, Planetwin365 e Goldbet, tutti già passati sotto la lente di questa serie.")
b.add_body(doc, "A differenza dei tre brand fratelli, però, Lottomatica non è un prodotto nato online: eredita da oltre trent'anni di storia una rete fisica che nessun altro concessionario del gruppo possiede, oltre 4.000 agenzie scommesse e 1.100 sale gioco. Questa recensione analizza bonus, palinsesto, casinò e sicurezza di un operatore che gioca una partita diversa dagli altri tre: non solo online, ma davvero omnicanale.")
b.add_divider(doc)

b.add_h1(doc, "VALUTAZIONI")
b.add_data_table(
    doc,
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
    col_widths=None,
)
b.add_average_score(doc, "Valutazione media complessiva: 7.5/10")
b.add_divider(doc)

b.add_h1(doc, "PRO & CONTRO")
b.add_h2(doc, "Perché scegliere Lottomatica (Pro)")
b.add_body(doc, "Il tratto che distingue davvero Lottomatica dagli altri tre brand del gruppo non è nel palinsesto o nel casinò, ma nella rete fisica: oltre 4.000 agenzie scommesse e 1.100 sale gioco, ereditate da oltre trent'anni di storia che parte dalla gestione del Lotto nel 1990. Nessun altro concessionario del portafoglio Lottomatica Group ha un'infrastruttura fisica paragonabile: chi vuole passare dal punto vendita sotto casa al conto online, o viceversa, trova un'omnicanalità che Betflag, Planetwin365 e Goldbet non possono offrire.")
b.add_body(doc, "Il bonus di benvenuto arriva fino a 2.050€ nominali, diviso in due componenti da 50€ e 2.000€ sul primo deposito, entrambe attivabili con un deposito minimo di 20€. Il ventaglio di metodi di pagamento è tra i più ampi della categoria: oltre alle carte e ai principali e-wallet, sono disponibili Apple Pay, Google Pay, MyBank e un voucher proprietario che scende fino a 2€ di deposito minimo.")
b.add_body(doc, "Il casinò online supera i 3.000 giochi distribuiti su oltre 30 provider, con una sezione live firmata Evolution che include Crazy Time, Blackjack e Venezia Roulette. Tra i fornitori di slot compare anche IGT, la società con cui il gruppo ha condiviso vent'anni di storia societaria prima della separazione del 2021: un dettaglio che chiude idealmente il cerchio con le origini del marchio.")
b.add_body(doc, "Tra chi scommette con regolarità, Lottomatica si colloca alla pari con gli altri brand del gruppo già passati sotto questa lente: non ricorre con facilità a limitazioni o chiusure di conto per i giocatori vincenti o per chi sfrutta sistematicamente le promozioni, un comportamento tutt'altro che scontato nel mercato ADM.")
b.add_body(doc, "L'app, disponibile su iOS e Android, raccoglie una valutazione media di 4,7/5 su oltre 11.500 recensioni: un riscontro solido, in linea con i migliori risultati della categoria.")

b.add_h2(doc, "Dove Lottomatica può migliorare (Contro)")
b.add_body(doc, "Il dato più critico riguarda l'assistenza: su Trustpilot, Lottomatica raccoglie un punteggio di 1,2/5 su 1.182 recensioni, con il 92% delle valutazioni a una stella, in gran parte legate a lamentele su tempi di prelievo e qualità del supporto. È un quadro parzialmente distorto rispetto all'esperienza di chi lavora nel settore, ma il margine di miglioramento è reale: da leader di mercato con una storia di oltre trent'anni, l'attenzione all'esperienza del cliente e alla qualità dell'assistenza non è sempre all'altezza della posizione che l'operatore occupa.")
b.add_body(doc, "La registrazione tramite SPID non è più disponibile dal 13 novembre 2025, in coincidenza con il nuovo regime di rilascio delle concessioni online varato da ADM, e la CIE non è ancora un'alternativa attiva: chi cerca l'accesso più rapido tramite identità digitale deve procedere con l'inserimento manuale dei dati.")
b.add_body(doc, "Entrambe le componenti del bonus di benvenuto richiedono multiple da almeno 3 eventi con quota minima 1,50: un vincolo comune al settore, ma che nella pratica spinge spesso a completare la giocata con eventi minori solo per raggiungere la soglia richiesta.")
b.add_divider(doc)

b.add_h1(doc, "PANORAMICA TRA EVENTI E STREAMING")
b.add_body(doc, "Il palinsesto di Lottomatica copre un ampio ventaglio di discipline: calcio, basket, tennis, pallavolo, motori (Formula 1 e MotoGP), ciclismo, pugilato, golf e i principali sport americani come football e baseball, oltre a hockey su ghiaccio, calcio a 5 e pallamano. Il calcio resta il prodotto trainante, con copertura di Serie A, Coppa Italia e dei principali campionati esteri.")
b.add_body(doc, "Lo streaming live copre una selezione di eventi tra cui Bundesliga, Coppa di Francia, FA Cup, Coppa America, Lega Pro, NBA, Serie A2 di basket e i grandi tornei del tennis, dai major ATP 1000 e 500. Sul calcio la copertura include alcune partite di Premier League, La Liga e Bundesliga: una selezione più ampia della media, anche se non sistematica su ogni competizione.")
b.add_divider(doc)

b.add_h1(doc, "TIPOLOGIA DI GIOCHI DISPONIBILI")
b.add_body(doc, "**Scommesse sportive**: ampio ventaglio di discipline, dai grandi campionati europei agli sport americani, con quote pre-match, live e multiple.")
b.add_body(doc, "**Casinò online**: oltre 3.000 slot distribuite su più di 30 provider, tra cui IGT, NetEnt, Play'n GO, Pragmatic Play e Red Tiger Gaming.")
b.add_body(doc, "**Casinò live**: tavoli con dealer italiani firmati Evolution, tra cui Crazy Time, Blackjack live e Venezia Roulette.")
b.add_body(doc, "**Poker**: sezione dedicata con bonus specifico del 300% sul primo versamento fino a 1.200€ (deposito minimo 10€), sbloccato con 10€ di bonus ogni 30€ di rake generata entro 30 giorni.")
b.add_divider(doc)

b.add_h1(doc, "PROMOZIONI")
b.add_h2(doc, "Bonus di benvenuto — prima componente")
b.add_info_table(doc, [
    ("Percentuale e massimale", "100% sul primo deposito, fino a 50€"),
    ("Deposito minimo qualificante", "20€, entro 7 giorni dalla registrazione"),
    ("Requisito di puntata", "Multiple da almeno 3 eventi, quota minima 1,50 per evento"),
])
b.add_h2(doc, "Bonus di benvenuto — seconda componente")
b.add_info_table(doc, [
    ("Percentuale e massimale", "Ulteriore 100% sul primo deposito, fino a 2.000€"),
    ("Rollover", "6 volte l'importo, su multiple da almeno 3 eventi a quota minima 1,50"),
    ("Finestra temporale", "Da completare entro 30 giorni dalla registrazione"),
])
b.add_h2(doc, "Bonus poker")
b.add_body(doc, "300% sul primo versamento fino a 1.200€ (deposito minimo 10€), sbloccato progressivamente con 10€ di bonus ogni 30€ di rake generata, validità 30 giorni dall'erogazione.")
b.add_note_box(doc, "Nota importante", "Skrill, Neteller, MyBank e voucher Lottomatica sono esclusi dai metodi che attivano il bonus di benvenuto. Tutte le condizioni sono soggette ad aggiornamento da parte dell'operatore: verificare sempre i T&C ufficiali prima dell'attivazione.")
b.add_divider(doc)

b.add_h1(doc, "INFO SULLE QUOTE, MERCATI E FUNZIONALITÀ")
b.add_body(doc, "Lottomatica costruisce l'offerta scommesse su un palinsesto ampio quanto trasversale: calcio, basket e tennis restano i pilastri, ma la copertura si estende a discipline meno centrali nel mercato ADM come pugilato, golf e sport americani. Il vero terreno differenziante dell'operatore, però, resta fuori dal palinsesto: è la rete fisica di oltre 4.000 agenzie e 1.100 sale gioco, un'infrastruttura che nessun altro brand del gruppo Lottomatica può vantare.")

b.add_h2(doc, "Come piazzare una scommessa su Lottomatica")
b.add_body(doc, "**STEP 1: Scegli l'evento** — Naviga il palinsesto online o passa dal punto vendita fisico. Seleziona il mercato e la quota desiderata.")
b.add_body(doc, "**STEP 2: Componi la giocata** — Inserisci l'importo. Aggiungi altri eventi per una multipla, verificando che la quota totale rispetti eventuali requisiti bonus attivi.")
b.add_body(doc, "**STEP 3: Conferma** — Conferma la giocata online o al banco. La ricevuta appare in tempo reale nella cronologia del conto, o viene stampata al punto vendita.")
b.add_divider(doc)

b.add_h1(doc, "CONTO DI SCOMMESSA E REGISTRAZIONE")
b.add_body(doc, "**Registrazione**: compilazione del modulo con dati anagrafici, codice fiscale, email e numero di telefono, seguita dal caricamento di un documento d'identità valido in fase di apertura del conto. Dal 13 novembre 2025 non è più possibile registrarsi tramite SPID; la CIE non è al momento un'alternativa disponibile.")
b.add_body(doc, "**Requisiti di base**: maggiore età (18 anni), residenza in Italia, codice fiscale italiano, documento d'identità in corso di validità.")
b.add_divider(doc)

b.add_h1(doc, "METODI DI PAGAMENTO")
b.add_body(doc, "Lottomatica mette a disposizione uno dei ventagli di pagamento più ampi della categoria: carte di credito, PostePay, Apple Pay, Google Pay, PayPal, Skrill, Neteller, MuchBetter, bonifico bancario, MyBank e un voucher proprietario Lottomatica.")
b.add_data_table(
    doc,
    ["Metodo", "Deposito minimo", "Prelievo"],
    [
        ["Carte / PostePay", "20€", "Sì"],
        ["Apple Pay / Google Pay", "20€", "Sì"],
        ["PayPal", "20€", "Sì"],
        ["Skrill / Neteller", "10€", "Sì (non attiva il bonus)"],
        ["Voucher Lottomatica", "2€", "Solo deposito"],
        ["Bonifico bancario", "20€", "Sì"],
    ],
    highlight_col=None,
)
b.add_body(doc, "I prelievi tramite e-wallet (PayPal, Skrill, Neteller) richiedono generalmente 24 ore di lavorazione, con un range che va da un minimo di 10€ a un massimo di 5.000€ per operazione.")
b.add_divider(doc)

b.add_h1(doc, "SICUREZZA")
b.add_body(doc, "**Licenza ADM**: concessione n. 16010, in capo a Lottomatica Scommesse S.r.l. Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana.")
b.add_body(doc, "**Garanzia patrimoniale**: Lottomatica Group S.p.A. è quotata su Euronext Milan dal maggio 2023 ed è entrata nel FTSE MIB da settembre 2025, uno dei 40 titoli più liquidi e capitalizzati della Borsa italiana: una solidità finanziaria che rafforza le garanzie dietro il brand.")
b.add_body(doc, "**Gioco responsabile**: strumenti di auto-limitazione dei depositi, autoesclusione temporanea o permanente, limiti di durata delle sessioni e test di autovalutazione, in conformità con le normative ADM.")
b.add_divider(doc)

b.add_h1(doc, "SERVE AIUTO? CUSTOMER SUPPORT")
b.add_body(doc, "Il servizio clienti è raggiungibile tramite telefono (800 900 009 da rete fissa, 06 2929 da cellulare), live chat nell'area riservata ed email (supporto@lottomatica.it), tutti i giorni dalle 9:00 alle 22:00.")
b.add_body(doc, "Su Trustpilot l'operatore raccoglie un punteggio molto basso, 1,2/5 su 1.182 recensioni, in gran parte legato a lamentele su tempi di prelievo e qualità del supporto. Un quadro che, nell'esperienza di chi lavora nel settore, appare parzialmente distorto rispetto alla realtà del servizio, ma che segnala comunque un margine di miglioramento reale sull'esperienza del cliente, specie per un operatore che occupa una posizione di leadership nel mercato ADM.")
b.add_divider(doc)

b.add_h1(doc, "ALTRI PRODOTTI NELL'OFFERTA")
b.add_body(doc, "**Poker**: sezione dedicata con bonus specifico del 300% sul primo versamento fino a 1.200€.")
b.add_body(doc, "**Rete fisica**: oltre 4.000 agenzie scommesse e 1.100 sale gioco, un'infrastruttura omnicanale che accompagna l'offerta online e che nessun altro brand del gruppo Lottomatica possiede.")
b.add_divider(doc)

b.add_h1(doc, "FEEDBACK E RECENSIONI")
b.add_body(doc, "Sull'App Store e Google Play, l'app Lottomatica raggiunge una valutazione media di 4,7/5 su oltre 11.500 recensioni complessive: un punteggio solido, in linea con i migliori risultati della categoria.")
b.add_body(doc, "Il quadro cambia su Trustpilot, dove Lottomatica registra un punteggio di 1,2/5 su 1.182 recensioni, con il 92% dei giudizi a una stella, concentrati su lamentele relative a prelievi e assistenza. Una divaricazione così ampia tra i due canali non è rara nel settore, ma resta un punto su cui l'operatore ha margine di miglioramento.")
b.add_divider(doc)

b.add_h1(doc, "TABELLA COMPARATIVA: LOTTOMATICA VS SNAI VS GOLDBET")
b.add_data_table(
    doc,
    ["Caratteristica", "Lottomatica", "SNAI", "Goldbet"],
    [
        ["Bonus sport", "100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (quota min. 1,50)", "500€ Gold (x6) + 500€ Game Bonus + 15€ free + 9€ extra = ~1.500€", "100% fino a 2.000€ (rollover x6)"],
        ["Deposito minimo bonus", "20€", "Non specificato in questa serie", "20€"],
        ["Proprietà", "Lottomatica Group (capofila del gruppo)", "Gruppo Flutter Entertainment (dal 2025)", "Gruppo Lottomatica"],
        ["Prodotto distintivo", "Rete fisica: 4.000+ agenzie, 1.100 sale gioco", "Ippica, Snaipay, integrazione fisico-digitale", "Interfaccia mobile, quote competitive"],
        ["Registrazione SPID/CIE", "Non disponibile dal 13/11/2025", "Sì", "Non verificato in questa serie"],
        ["Licenza ADM", "16010", "Non riportata in questa serie", "16009"],
    ],
    highlight_col=None,
    col_widths=None,
)
b.add_body(doc, "**Nota**: le cifre di tutti gli operatori rappresentano valori nominali massimi, soggetti a rollover e condizioni di sblocco spesso complesse. Lottomatica è il concessionario capofila dello stesso gruppo proprietario di Goldbet: la tabella li mette a confronto come prodotti distinti, non come alternative indipendenti.", size=9)
b.add_divider(doc)

b.add_h1(doc, "IL NOSTRO GIUDIZIO")
b.add_body(doc, "Lottomatica arriva al 2026 con una storia che nessun altro brand di questa serie può vantare: nasce nel 1990 come consorzio per la gestione del Lotto, attraversa vent'anni sotto il controllo di IGT dopo la fusione del 2015, e nel 2021 torna sotto controllo italiano quando Gamenet Group ne rileva le quote scommesse, adottandone poi il nome. Oggi Lottomatica Group è quotata su Euronext Milan e nel FTSE MIB, capofila dello stesso portafoglio che include Betflag, Planetwin365 e Goldbet.")
b.add_body(doc, "Quello che distingue davvero Lottomatica dai tre fratelli online, però, non sta nella scheda tecnica del prodotto digitale: è la rete fisica, oltre 4.000 agenzie scommesse e 1.100 sale gioco, un'infrastruttura omnicanale unica nel gruppo. A questo si aggiunge un comportamento verso i giocatori vincenti e i bonus abuser che, secondo chi opera nel settore, si colloca alla pari con gli altri brand già passati sotto questa lente: nessuna limitazione facile, un trattamento corretto.")
b.add_body(doc, "Il bonus di benvenuto arriva a 2.050€ nominali su due componenti, il casinò supera i 3.000 giochi con un live curato da Evolution, e l'app raccoglie un solido 4,7/5. Il punto su cui l'operatore ha davvero margine di miglioramento è l'esperienza del cliente lato assistenza: il punteggio Trustpilot di 1,2/5 racconta un quadro più duro della realtà percepita da chi lavora nel settore, ma la sostanza del rilievo regge. Da leader di mercato con oltre trent'anni di storia, l'attenzione alla UX e alla qualità del supporto non è sempre coerente con la posizione che l'operatore occupa: è l'area dove Lottomatica ha più da guadagnare rispetto agli altri brand dello stesso gruppo.")
b.add_body(doc, "Chi cerca un operatore omnicanale, con una rete fisica capillare alle spalle e un trattamento corretto verso chi vince con regolarità, trova in Lottomatica una scelta solida. Chi valuta l'assistenza come criterio decisivo farebbe bene a verificare i canali disponibili prima di scegliere, tenendo presente che il dato più critico riguarda l'esperienza online più che il servizio in agenzia.")
b.add_final_score_box(doc, "VOTO FINALE: 4 SU 5")
b.add_divider(doc)

b.add_h1(doc, "FAQ")
b.add_h2(doc, "Lottomatica è sicuro?")
b.add_body(doc, "Opera sotto concessione ADM n. 16010 ed è controllato da Lottomatica Group S.p.A., quotata su Euronext Milan e nel FTSE MIB dal settembre 2025: tra gli operatori regolamentati più solidi del mercato italiano.")
b.add_h2(doc, "È possibile registrarsi con SPID o CIE su Lottomatica?")
b.add_body(doc, "No. La registrazione tramite SPID non è più disponibile dal 13 novembre 2025, e la CIE non è al momento un'alternativa attiva. La registrazione richiede l'inserimento manuale dei dati e il caricamento di un documento d'identità.")
b.add_h2(doc, "In cosa Lottomatica è diverso dagli altri brand del gruppo (Betflag, Planetwin365, Goldbet)?")
b.add_body(doc, "È l'unico con una rete fisica: oltre 4.000 agenzie scommesse e 1.100 sale gioco, ereditate da una storia che parte dalla gestione del Lotto nel 1990. Gli altri tre brand del gruppo sono prodotti nati online.")
b.add_h2(doc, "Quali metodi di pagamento non attivano il bonus di benvenuto?")
b.add_body(doc, "Skrill, Neteller, MyBank e il voucher Lottomatica sono esclusi dai metodi che permettono di ricevere il bonus.")
b.add_divider(doc)

b.add_h1(doc, "LE MIGLIORI ALTERNATIVE")
b.add_body(doc, "**Goldbet**: stesso gruppo proprietario di Lottomatica, bonus sport 100% fino a 2.000€ con rollover x6, interfaccia mobile apprezzata dalla fascia più giovane dell'utenza.")
b.add_body(doc, "**Planetwin365**: terzo brand del gruppo, casinò live con tavoli esclusivi Evolution, bonus fino a 2.100€ tra sport e slot.")
b.add_body(doc, "**SNAI**: leadership storica nell'ippica, integrazione fisico-digitale con Snaipay, rollover x6 sul Bonus Gold tra i più accessibili del mercato.")

footer_p = doc.add_paragraph()
from docx.enum.text import WD_ALIGN_PARAGRAPH
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer_p.paragraph_format.space_before = b.Pt(14)
b._add_run(footer_p, "Il gioco è vietato ai minori di 18 anni • Bonus e T&C soggetti a modifica: verificare sempre su lottomatica.it", italic=True, color=b.GRAY, size=8)

doc.save(OUT)
print("Salvato:", OUT)
