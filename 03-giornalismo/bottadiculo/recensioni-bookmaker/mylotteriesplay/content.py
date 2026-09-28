# -*- coding: utf-8 -*-
# Contenuto unico della recensione My Lotteries Play 2026.
# Lo leggono build_mylotteriesplay_docx.py, build_mylotteriesplay_html.py e build_mylotteriesplay_md.py:
# si corregge qui, una volta sola, e le tre versioni restano allineate.
# Grassetto inline in stile markdown (**testo**), come in _template/review_docx_builder.add_body.

HEADER = "Recensione My Lotteries Play 2026  |  Aggiornamento: Settembre 2026"
TITLE = "RECENSIONE MY LOTTERIES PLAY 2026"
SUBTITLE = "Analisi completa dell'operatore"
RATING = (
    "⭐ 3,5/5",
    "Fino a 50€ di benvenuto", "Slot e Lotterie (100% della prima ricarica)",
    "Oltre 10 giochi di lotteria", "Lotto, Gratta e Vinci, SuperEnalotto, Lotteria Italia",
)
CTA = "VAI SU MY LOTTERIES PLAY"
FOOTER = "Il gioco è vietato ai minori di 18 anni • Bonus e T&C soggetti a modifica: verificare sempre su mylotteriesplay.it"

# Ogni blocco: (tipo, argomenti). Tipi: h1, h2, body, small, info, callout, table, avg, note, final, divider
BLOCKS = [
    ("h1", "INFORMAZIONI ESSENZIALI"),
    ("info", [
        ("Licenza operativa", "ADM, concessione n. 16049 (subentrata alla GAD n. 15478 con il nuovo regime delle concessioni online, in vigore dal 13 novembre 2025)"),
        ("Proprietà", "MyLotteries S.r.l., Roma, società a socio unico soggetta a direzione e coordinamento di Brightstar Lottery S.p.A., il gruppo che fino a giugno 2025 si chiamava IGT Lottery. Non fa parte del Gruppo Lottomatica"),
        ("Bonus benvenuto", "Tre offerte attive: Slot e Lotterie, 100% della prima ricarica fino a 50€; Lotterie, 100% fino a 25€; Lotterie in ricevitoria, 100% fino a 30€ per chi apre il conto in un punto vendita"),
        ("Requisito di puntata", "Fun Bonus Slot: rollover 10 volte, puntata da 0,10€ a 10€. Real Bonus Lotterie: nessun requisito di puntata indicato nelle condizioni, da usare entro 5 giorni"),
        ("App disponibili", "My Lotteries PLAY su App Store, con l'offerta completa; My Lotteries, app dedicata alle lotterie, per iOS e Android"),
        ("Metodi di pagamento", "Carte Visa e Mastercard, PayPal, bonifico ordinario e istantaneo, MyBank, OnShop nei punti LIS Carica"),
        ("Servizio clienti", "Numero verde 800.900.500, email supporto@mylotteriesplay.it e contogioco@mylotteriesplay.it"),
        ("Deposito minimo", "10€; 20€ per attivare il bonus Slot e Lotterie"),
        ("Registrazione rapida", "Foto del documento con compilazione automatica dei dati, in alternativa alla registrazione manuale"),
    ]),
    ("callout", "PERCHÉ MY LOTTERIES PLAY POTREBBE NON FARE AL CASO TUO", [
        "Le scommesse sportive sono arrivate a febbraio 2026: il sito non indica il numero di discipline né dei mercati, e alla data di verifica non risulta un bonus di benvenuto dedicato allo sport",
        "I bonus di benvenuto hanno massimali contenuti, fino a 50€: sono pensati per chi gioca a lotterie e slot con importi piccoli, non per chi cerca cifre alte",
        "Numero di titoli e fornitori del casinò non compaiono nelle pagine del sito: difficile confrontare il catalogo prima di aprire un conto",
    ]),
    ("divider",),

    ("h1", "PREFAZIONE"),
    ("body", "My Lotteries Play è la piattaforma di gioco online di MyLotteries S.r.l., società romana controllata da Brightstar Lottery S.p.A. Il nome della piattaforma può dire poco a chi scommette, quello del gruppo dice di più: Brightstar Lottery è la denominazione adottata a giugno 2025 da IGT Lottery, quando il gruppo IGT ha ceduto le attività gaming e digital a una società controllata da fondi Apollo per concentrarsi sulle lotterie. In Italia le società del gruppo sono concessionarie dello Stato per il Gioco del Lotto, il Gratta e Vinci e la Lotteria Italia."),
    ("body", "Da qui nasce l'identità del prodotto. My Lotteries Play parte dalle lotterie, che restano il cuore dell'offerta, e nel tempo ha aggiunto casinò, slot, giochi di carte e scommesse virtuali. Da febbraio 2026 ha aperto anche le scommesse sportive, pre-match e live. Questa recensione analizza un operatore diverso dai bookmaker tradizionali: un gruppo solido alle spalle, un'offerta ampia sulle lotterie, uno sport ancora giovane e un marchio che il pubblico online conosce poco."),
    ("divider",),

    ("h1", "VALUTAZIONI"),
    ("table", ["Categoria", "Voto", "Nota sintetica"], [
        ["Lotterie e Gratta e Vinci", "8.5/10", "Oltre 10 giochi, dal Lotto alla Lotteria Italia, più di 100 Gratta e Vinci online"],
        ["Scommesse sportive", "5.5/10", "Pre-match e live da febbraio 2026, discipline e mercati non dichiarati"],
        ["Casinò e slot", "6.5/10", "Slot, tavoli e live presenti, catalogo e fornitori non dichiarati"],
        ["Bonus e promozioni", "6.5/10", "Massimali contenuti, condizioni leggibili, programma fedeltà My Club"],
        ["App e mobile", "6/10", "App completa recente, 3,6/5 su 24 valutazioni"],
        ["Metodi di pagamento", "7/10", "Set essenziale, nessuna commissione sui prelievi"],
        ["Assistenza clienti", "6/10", "Numero verde ed email, nessuna live chat indicata"],
        ["Sicurezza e compliance", "8.5/10", "Licenza ADM 16049, gruppo concessionario di Lotto e Gratta e Vinci"],
    ], 1),
    ("avg", "Valutazione media complessiva: 6.8/10"),
    ("divider",),

    ("h1", "PRO & CONTRO"),
    ("h2", "Perché scegliere My Lotteries Play (Pro)"),
    ("body", "Il punto di forza sta nelle lotterie. My Lotteries Play fa capo al gruppo che in Italia gestisce in concessione Lotto, Gratta e Vinci e Lotteria Italia, e l'offerta lo riflette: accanto a Lotto e 10eLotto ci sono FAI3 FAI4, MillionDay, SuperEnalotto, Eurojackpot, Win for Life, VinciCasa, SiVinceTutto, oltre 100 Gratta e Vinci online e l'acquisto dei biglietti della Lotteria Italia. Chi gioca soprattutto a questi prodotti li trova tutti in un solo conto."),
    ("body", "La solidità societaria è l'altro elemento a favore: concessione ADM n. 16049 e un gruppo controllante che, per sua stessa presentazione, lavora nel settore delle lotterie da quasi cinquant'anni."),
    ("body", "I bonus di benvenuto hanno massimali bassi ma condizioni facili da leggere. Il bonus Slot e Lotterie restituisce il 100% della prima ricarica fino a 50€, diviso a metà: 25€ di Fun Bonus Slot con rollover 10 volte e 25€ di Real Bonus Lotterie, spendibile su Gratta e Vinci, Lotto, 10eLotto, FAI3 FAI4 e MillionDay senza requisiti di puntata indicati nelle condizioni. Sui prelievi con carta, PayPal e bonifico non si paga commissione."),
    ("h2", "Dove My Lotteries Play può migliorare (Contro)"),
    ("body", "Il limite principale, nel nostro giudizio editoriale (dettagliato in nota, in fondo), riguarda la notorietà più che il prodotto: My Lotteries Play è un marchio che deve ancora emergere online, poco presente nelle conversazioni dei giocatori e poco conosciuto fuori da chi cerca le lotterie. Per un operatore che ha appena aperto lo sport, farsi conoscere online è il passaggio da cui dipende il resto."),
    ("body", "Le scommesse sportive, pre-match e live, sono disponibili solo da febbraio 2026. Il sito non dichiara quante discipline copre né quanti mercati offre, e alla data di verifica non risulta un bonus di benvenuto dedicato allo sport: chi arriva per scommettere trova meno elementi per valutare l'offerta rispetto agli operatori con più storia su questo terreno."),
    ("body", "Anche i dati reputazionali riflettono la stessa distanza dal pubblico online: sono pochi e raccolti su campioni ridotti (dettaglio in Feedback e recensioni). La pagina contatti, infine, indica numero verde ed email ma nessuna live chat."),
    ("divider",),

    ("h1", "LOTTERIE, LOTTO E GRATTA E VINCI"),
    ("body", "È la sezione che distingue My Lotteries Play dagli operatori nati come bookmaker. L'offerta comprende Gioco del Lotto, 10eLotto, FAI3 FAI4, MillionDay, SuperEnalotto, Eurojackpot, Win for Life Classico, Super Win for Life, VinciCasa, SiVinceTutto e Play Your Date, oltre all'acquisto online dei biglietti della Lotteria Italia."),
    ("body", "I Gratta e Vinci online sono oltre 100, con giocate da 0,10€ a 25€. Per Lotto, 10eLotto, MillionDay e Gratta e Vinci il sito affianca ai giochi pagine dedicate a regolamenti, verifica delle vincite e modalità di riscossione. L'app My Lotteries, dedicata solo alle lotterie, permette anche di seguire le estrazioni e controllare i biglietti."),
    ("divider",),

    ("h1", "SCOMMESSE SPORTIVE E VIRTUAL"),
    ("body", "Le scommesse sportive sono l'aggiunta più recente: l'operatore le ha annunciate a febbraio 2026, in modalità pre-match e live, da desktop e da mobile, con il calcio in primo piano ma non come unica disciplina. Il sito non pubblica il numero di discipline, i mercati per evento né eventuali servizi di streaming: su questi aspetti la recensione non esprime un giudizio che non potrebbe verificare."),
    ("body", "**Scommesse virtuali**: calcio, corse di cavalli e di cani, biglie e auto, con esiti generati da un sistema di estrazione casuale certificato."),
    ("divider",),

    ("h1", "CASINÒ, SLOT E GIOCHI DI CARTE"),
    ("body", "**Casinò e slot**: la sezione comprende slot, giochi da tavolo e casinò live. Il sito non indica il numero di titoli né i fornitori."),
    ("body", "**Giochi di carte**: titoli della tradizione italiana come Briscola, Tresette e Scopa, disponibili anche in app."),
    ("divider",),

    ("h1", "PROMOZIONI"),
    ("h2", "Bonus Benvenuto Slot e Lotterie"),
    ("info", [
        ("Percentuale e massimale", "100% della prima ricarica, fino a 50€: metà Fun Bonus Slot (fino a 25€), metà Real Bonus Lotterie (fino a 25€)"),
        ("Deposito minimo qualificante", "20€, entro 7 giorni dall'apertura del conto"),
        ("Requisito di puntata", "Fun Bonus Slot: 10 volte, puntata da 0,10€ a 10€, su dieci slot indicate nel regolamento. Real Bonus Lotterie: nessun requisito indicato, su Gratta e Vinci, Lotto, 10eLotto, FAI3 FAI4 e MillionDay"),
        ("Validità", "Fun Bonus 2 giorni, Real Bonus 5 giorni. Iniziativa valida fino al 31/12/2026"),
    ]),
    ("h2", "Bonus Benvenuto Lotterie"),
    ("info", [
        ("Percentuale e massimale", "100% della prima ricarica, fino a 25€"),
        ("Deposito minimo qualificante", "10€, entro 7 giorni dall'apertura del conto"),
        ("Giochi", "Gratta e Vinci, Lotto, 10eLotto, FAI3 FAI4, MillionDay, SuperEnalotto, Win for Life, Eurojackpot, VinciCasa, SiVinceTutto e Play Your Date"),
        ("Validità", "5 giorni dall'accredito. Iniziativa valida fino al 31/12/2026"),
    ]),
    ("h2", "Bonus Benvenuto Lotterie in Ricevitoria"),
    ("info", [
        ("Percentuale e massimale", "100% della prima ricarica, fino a 30€, per chi apre il conto in un punto vendita"),
        ("Deposito minimo qualificante", "10€, entro 7 giorni dalla registrazione"),
        ("Giochi", "Gratta e Vinci, Lotto, 10eLotto, FAI3 FAI4, MillionDay e SuperEnalotto online"),
        ("Validità", "5 giorni dall'attivazione. Iniziativa valida fino al 31/12/2026"),
    ]),
    ("note", "Nota importante", "Le ricariche con bonifico bancario non attivano i bonus. I bonus non sono prelevabili né convertibili in denaro. Condizioni verificate il 28/09/2026 sulle pagine ufficiali dell'operatore e soggette a cambiamento: verificare sempre i T&C aggiornati prima dell'attivazione."),
    ("divider",),

    ("h1", "CONTO DI GIOCO E REGISTRAZIONE"),
    ("body", "**Registrazione**: due strade, la registrazione veloce con la foto del documento, che compila i dati in automatico, oppure quella manuale in sei passaggi (dati personali, accesso e contatti, bonus, limite di ricarica settimanale, condizioni, conferma). Documenti accettati: carta d'identità, passaporto, patente. Il documento va caricato subito: se entro 48 ore non risulta valido, il conto viene sospeso fino al caricamento di un documento corretto."),
    ("body", "**Requisiti di base**: maggiore età, residenza in Italia, codice fiscale, email e numero di cellulare italiano per la verifica via OTP. Il conto si può aprire anche in un punto vendita aderente, con un bonus di benvenuto dedicato."),
    ("divider",),

    ("h1", "METODI DI PAGAMENTO"),
    ("table", ["Metodo", "Ricarica", "Prelievo"], [
        ["Carte Visa / Mastercard", "Sì, senza costi, accredito immediato", "Da 10€ a 2.000€, da 24 a 48 ore, nessuna commissione"],
        ["PayPal", "Sì", "Da 10€ a 8.000€, nessuna commissione, dopo almeno una ricarica con lo stesso conto PayPal"],
        ["Bonifico ordinario e istantaneo", "Sì, accredito in 2 o 3 giorni lavorativi (non attiva i bonus)", "Da 10€, nessun massimo, entro 2 o 3 giorni lavorativi"],
        ["MyBank", "Sì", "Non indicato tra i metodi di prelievo"],
        ["OnShop (punti LIS Carica)", "Sì, costo di 1,20€ IVA inclusa", "Non indicato tra i metodi di prelievo"],
    ], None),
    ("body", "Per PayPal le pagine di assistenza riportano tempi diversi, da 24 ore fino a 3 giorni lavorativi previa verifica. Il tetto alle ricariche online è di 10.000€ a settimana, entro il limite che ogni giocatore sceglie in registrazione. I prelievi si bloccano se il documento d'identità risulta scaduto."),
    ("divider",),

    ("h1", "SICUREZZA"),
    ("body", "**Licenza ADM**: concessione n. 16049, in capo a MyLotteries S.r.l. Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana."),
    ("body", "**Struttura societaria**: MyLotteries S.r.l. è soggetta a direzione e coordinamento di Brightstar Lottery S.p.A. e fa parte del suo gruppo IVA. In Italia le società del gruppo sono concessionarie dello Stato per Lotto, Gratta e Vinci e Lotteria Italia: un profilo che colloca l'operatore dentro uno dei soggetti più strutturati del comparto."),
    ("body", "**Gioco responsabile**: limite di ricarica settimanale scelto in fase di registrazione, strumenti di autoesclusione e le altre misure di protezione previste da ADM, aggiornate con il nuovo contratto di conto gioco."),
    ("divider",),

    ("h1", "SERVE AIUTO? CUSTOMER SUPPORT"),
    ("body", "Il numero verde 800.900.500 copre richieste di informazioni, problemi tecnici e assistenza nel caricamento dei documenti. Per iscritto si scrive a supporto@mylotteriesplay.it dalla mail associata al conto, oppure a contogioco@mylotteriesplay.it per lo sblocco di conti sospesi e le richieste di chiusura. Gli orari del servizio non sono indicati nella pagina contatti, che non riporta una live chat."),
    ("divider",),

    ("h1", "ALTRI PRODOTTI NELL'OFFERTA"),
    ("body", "**Programma fedeltà My Club**: iscrizione automatica con la prima giocata in denaro reale, cinque livelli da Bronzo a Diamante. I punti si accumulano sulle giocate reali, 10 per euro sulle lotterie e 5 per euro su slot, casinò, giochi di carte e scommesse, e a fine mese si convertono in punti bonus con un moltiplicatore che sale con il livello, da 1 a 4 volte. Le giocate fatte con i bonus non generano punti."),
    ("divider",),

    ("h1", "FEEDBACK E RECENSIONI"),
    ("body", "Sull'App Store, My Lotteries PLAY raccoglie una valutazione media di 3,6/5 su 24 valutazioni (rilevazione del 28/09/2026): un'app recente, alla versione 1.0.1, con una base di giudizi ancora troppo piccola per dire qualcosa di stabile."),
    ("body", "Su Trustpilot il profilo non è gestito dall'operatore e registra 1,7/5 su 23 recensioni, quasi tutte a una stella (rilevazione del 28/09/2026). Su numeri così bassi, e su una piattaforma dove chi lascia un giudizio negativo è sempre sovrarappresentato, il punteggio non misura la qualità del servizio: indica soprattutto che la comunità di utenti che si esprime online è ancora ridotta."),
    ("divider",),

    ("h1", "TABELLA COMPARATIVA: MY LOTTERIES PLAY VS SISAL VS LOTTOMATICA"),
    ("table", ["Caratteristica", "My Lotteries Play", "Sisal", "Lottomatica"], [
        ["Proprietà", "MyLotteries S.r.l. (Brightstar Lottery)", "Flutter Entertainment (dal 4 agosto 2022)", "Lottomatica Group"],
        ["Prodotto distintivo", "Lotterie del gruppo concessionario di Lotto, Gratta e Vinci e Lotteria Italia", "Concessionario di SuperEnalotto e MillionDay", "Rete fisica: oltre 4.000 agenzie e 1.100 sale gioco"],
        ["Bonus di benvenuto principale", "Slot e Lotterie: 100% fino a 50€", "Dato non verificato alla data di aggiornamento", "Sport: 100% fino a 50€ + 100% fino a 2.000€ = 2.050€ (rollover x6)"],
        ["Scommesse sportive", "Da febbraio 2026", "Sì", "Sì"],
        ["Licenza ADM", "16049", "Dato non verificato alla data di aggiornamento", "16010"],
    ], None),
    ("small", "**Nota**: i tre operatori hanno un'origine diversa e il confronto va letto di conseguenza: My Lotteries Play e Sisal partono dalle lotterie, Lottomatica dalle scommesse e dalla rete fisica. I dati My Lotteries Play sono verificati il 28/09/2026; i dati Lottomatica vengono dalla nostra recensione di settembre 2026; per Sisal sono riportati solo proprietà e concessioni, riscontrate su fonti di stampa. Le cifre dei bonus sono valori nominali massimi, soggetti a condizioni di sblocco: un confronto indicativo, non un'istantanea unica."),
    ("divider",),

    ("h1", "IL NOSTRO GIUDIZIO"),
    ("body", "My Lotteries Play va letto per quello che è: una piattaforma nata dalle lotterie, che negli ultimi mesi ha allargato l'offerta fino alle scommesse sportive. Alle spalle ha il gruppo concessionario di Lotto, Gratta e Vinci e Lotteria Italia, e sulle lotterie raccoglie in un solo conto un'offerta ampia, dal Lotto alla Lotteria Italia."),
    ("body", "Il limite, nel nostro giudizio, sta nella visibilità più che nel prodotto: è un marchio che deve ancora farsi conoscere online e che oggi non è tra quelli di cui i giocatori parlano. Lo sport, arrivato a febbraio 2026, è la leva naturale per allargare il pubblico, ma alla data di verifica il sito non dichiara l'ampiezza del palinsesto né offre un bonus dedicato. L'apertura del conto in ricevitoria esiste, con un bonus fino a 30€, ma nella pratica conta poco: la partita della notorietà si gioca online."),
    ("body", "Chi gioca soprattutto a Lotto, 10eLotto, Gratta e Vinci e SuperEnalotto trova in My Lotteries Play un conto solido, con un gruppo affidabile alle spalle e bonus piccoli ma leggibili. Chi cerca un bookmaker con un palinsesto sportivo consolidato, per ora, ha alternative con più storia su quel terreno."),
    ("body", "Il voto finale è una sintesi editoriale e non una conversione della media per categoria (6,8/10, pari a 3,4 su 5 in scala lineare): premia la solidità del gruppo e l'ampiezza dell'offerta lotterie, e tiene conto di uno sport ancora giovane e di un marchio poco conosciuto."),
    ("final", "VOTO FINALE: 3,5 SU 5"),
    ("divider",),

    ("h1", "NOTA METODOLOGICA"),
    ("body", "Dati raccolti e verificati il 28 settembre 2026 da fonti pubbliche. Concessione, proprietà, bonus, pagamenti, registrazione, contatti, programma fedeltà e lancio delle scommesse sportive vengono dalle pagine ufficiali di mylotteriesplay.it; il rating dell'app dalla pagina App Store per iOS; il punteggio Trustpilot dal profilo ufficiale della piattaforma; le concessioni del gruppo dal sito di Brightstar Lottery; il cambio di denominazione da IGT Lottery a Brightstar Lottery da fonti di stampa. Non sono stati effettuati test diretti su conto di gioco, app o transazioni reali: i dati derivano da fonti documentali, non da verifica operativa sul campo. La disponibilità di My Lotteries PLAY su Android non è stata verificata. Bonus, condizioni di gioco, metodi di pagamento e limiti cambiano nel tempo: verificare sempre i T&C ufficiali aggiornati prima di ogni decisione di gioco."),
    ("divider",),

    ("h1", "FAQ"),
    ("h2", "My Lotteries Play è sicuro?"),
    ("body", "Opera con concessione ADM n. 16049, in capo a MyLotteries S.r.l., società soggetta a direzione e coordinamento di Brightstar Lottery S.p.A., il gruppo concessionario in Italia di Lotto, Gratta e Vinci e Lotteria Italia."),
    ("h2", "My Lotteries Play fa parte del Gruppo Lottomatica?"),
    ("body", "No. Il gruppo di riferimento è Brightstar Lottery, la denominazione assunta da IGT Lottery a giugno 2025, distinto da Lottomatica Group."),
    ("h2", "Su My Lotteries Play si può scommettere sullo sport?"),
    ("body", "Sì, da febbraio 2026, con scommesse pre-match e live da sito e da app. Sono disponibili anche le scommesse virtuali."),
    ("h2", "Si può aprire il conto in ricevitoria?"),
    ("body", "Sì, presso i punti vendita aderenti, con un bonus di benvenuto dedicato: 100% della prima ricarica fino a 30€, spendibile su lotterie e Gratta e Vinci online."),
    ("h2", "Qual è il punto debole principale di My Lotteries Play?"),
    ("body", "La notorietà online: è un marchio che deve ancora farsi conoscere dal pubblico che gioca in rete. Sul prodotto, l'area più giovane è lo sport, disponibile solo da febbraio 2026."),
    ("divider",),

    ("h1", "LE MIGLIORI ALTERNATIVE"),
    ("body", "**Sisal**: concessionario di SuperEnalotto e MillionDay, parte di Flutter Entertainment dal 2022, con un'offerta che unisce lotterie, scommesse e casinò."),
    ("body", "**Lottomatica**: la scelta omnicanale, con oltre 4.000 agenzie e 1.100 sale gioco e un bonus sport fino a 2.050€."),
    ("body", "**Goldbet**: per chi mette lo sport al centro, con un'app valutata 4,8/5 su circa 25.000 valutazioni sull'App Store (rilevazione dell'11/09/2026)."),
]
