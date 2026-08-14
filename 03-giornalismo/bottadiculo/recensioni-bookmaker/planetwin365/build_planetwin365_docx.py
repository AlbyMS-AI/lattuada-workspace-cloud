import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_template"))
import review_docx_builder as b

OUT = os.path.join(os.path.dirname(__file__), "recensione-planetwin365-2026.docx")

doc = b.new_document()
b.set_header_footer(doc, "Recensione Planetwin365 2026  |  Aggiornamento: Agosto 2026")

b.add_title(doc, "RECENSIONE PLANETWIN365 2026", "Analisi completa dell'operatore")

b.add_rating_box(
    doc,
    "⭐ 4.5/5",
    "Fino a 2.100€",
    "Tra bonus sport e slot",
    "Rimborso 50%",
    "Fino a 10€/settimana per 10 settimane",
)
b.add_cta_bar(doc, "VAI SU PLANETWIN365")
b.add_divider(doc)

b.add_h1(doc, "INFORMAZIONI ESSENZIALI")
b.add_info_table(doc, [
    ("Licenza operativa", "ADM, concessione n. 15242 per le scommesse (PWO S.p.A., Roma), concessione n. 16007 per il casinò online"),
    ("Proprietà", "PWO S.p.A. (già SKS365 Italia), parte di SKS365 Group, fondato nel 2009 a Innsbruck. Dal novembre 2023 Lottomatica Group ha in corso l'acquisizione del 100% del gruppo per 639 milioni di euro, completata nell'aprile 2024. Planetwin365 è oggi nello stesso portafoglio di Betflag e Goldbet"),
    ("Bonus sport", "50% sul primo deposito fino a 100€ (deposito minimo 20€ entro 7 giorni, quota minima 1,50 su almeno 4 eventi, quota totale minima 5,00)"),
    ("Bonus slot", "100% sul primo deposito fino a 2.000€, erogato in 4 tranche da 500€ ciascuna, rollover 30 volte l'importo per tranche da completare entro 3 giorni"),
    ("Bonus aggiuntivo", "Rimborso settimanale del 50% fino a 10€, su multiple da almeno 3 eventi a quota minima 1,50, per 10 settimane"),
    ("App disponibili", "iOS (App Store) come Planetwin365 Scommesse Sport; su Android non è distribuita tramite Google Play, si scarica come APK dal sito ufficiale"),
    ("Metodi di pagamento", "Visa, Mastercard, PostePay, PayPal, Skrill, Neteller, Paysafecard, bonifico bancario"),
    ("Servizio clienti", "Telefono a tariffa ordinaria 06 9480 0931 (11:00-19:00), live chat nello stesso orario, email info@planetwin365.it"),
    ("Deposito minimo", "5€ per la maggior parte dei metodi"),
    ("Registrazione rapida", "SPID e CIE non disponibili al momento: la registrazione richiede l'inserimento manuale dei dati e il caricamento di un documento entro 30 giorni"),
])

b.add_callout_box(doc, "PERCHÉ PLANETWIN365 POTREBBE NON FARE AL CASO TUO", [
    "Le multiple richieste per validare i bonus (almeno 4 eventi per la componente sport, almeno 3 per quella slot) spingono spesso a completare la giocata con sport o categorie minori, solo per raggiungere la soglia di eventi",
    "Registrazione SPID/CIE non disponibile al momento: chi cerca l'accesso rapido tramite identità digitale non lo trova, a differenza di altri operatori dello stesso gruppo",
    "Orario del servizio clienti (11:00-19:00) più stretto della media di settore, anche se la qualità del supporto resta tra le più apprezzate del comparto",
])
b.add_divider(doc)

b.add_h1(doc, "PREFAZIONE")
b.add_body(doc, "Planetwin365 nasce come costola italiana di SKS365 Group, fondato nel 2009 a Innsbruck, in Austria. Il brand sbarca sul mercato regolamentato italiano nel 2017, sotto la concessione ADM n. 15242, a cui si affianca la concessione n. 16007 per l'offerta di casinò online.")
b.add_body(doc, "Diciassette anni dopo la fondazione del gruppo, la proprietà è cambiata. A novembre 2023 Lottomatica Group ha annunciato l'acquisizione del 100% di SKS365 per 639 milioni di euro, operazione completata nell'aprile 2024. Planetwin365 si trova oggi nello stesso portafoglio di Betflag e Goldbet: tre brand che in vetrina competono per lo stesso giocatore, ma che condividono la stessa proprietà.")
b.add_body(doc, "Per chi scommette la distinzione conta relativamente poco: quello che interessa è cosa cambia nell'offerta concreta. Questa recensione analizza bonus, palinsesto, casinò e sicurezza di un operatore che, dopo il passaggio di proprietà, si trova a difendere un'identità di prodotto autonoma dentro un gruppo che possiede già altri due concessionari diretti concorrenti.")
b.add_divider(doc)

b.add_h1(doc, "VALUTAZIONI")
b.add_data_table(
    doc,
    ["Categoria", "Voto", "Nota sintetica"],
    [
        ["Palinsesto sportivo", "8/10", "Oltre 25 discipline, più di 200 eventi live giornalieri"],
        ["Quote e payout", "7.5/10", "Quota minima 1,50 su almeno 4 eventi per il bonus sport"],
        ["Bonus e promozioni", "8.5/10", "Offerta generosa e spesso personalizzata, multiple obbligatorie per validare"],
        ["App e mobile", "7.5/10", "App Scommesse solida su App Store, assente da Google Play"],
        ["Live streaming", "7/10", "Copertura su calcio, tennis, basket, hockey su ghiaccio"],
        ["Casinò e slot", "8.5/10", "Oltre 4.700 giochi, tavoli live esclusivi Evolution"],
        ["Metodi di pagamento", "8/10", "8 metodi disponibili, nessuna commissione dichiarata sui prelievi"],
        ["Assistenza clienti", "8.5/10", "Orario ristretto, ma tra i canali più apprezzati del comparto"],
        ["Sicurezza e compliance", "8.5/10", "Doppia concessione ADM, garanzia patrimoniale del Gruppo Lottomatica"],
    ],
    highlight_col=1,
    col_widths=None,
)
b.add_average_score(doc, "Valutazione media complessiva: 8/10")
b.add_divider(doc)

b.add_h1(doc, "PRO & CONTRO")
b.add_h2(doc, "Perché scegliere Planetwin365 (Pro)")
b.add_body(doc, "Il casinò è il vero terreno di forza dell'operatore: oltre 4.700 giochi, di cui più di 4.000 slot, e una sezione live con circa 200 titoli distribuiti su 7 provider (Evolution, MediaLive, Authentic Gaming, Playtech Live, Pragmatic Play Live, LiveG24, Microgaming). Evolution ha realizzato per Planetwin365 due tavoli in esclusiva, Blackjack Planetwin365 e Planetwin365 Roulette Live: un dettaglio che pochi concessionari ADM possono vantare, perché le esclusive dei grandi provider live si contano sulle dita di una mano nel mercato italiano.")
b.add_body(doc, "Il bonus di benvenuto copre due componenti in parallelo, entrambe sportive, per un valore complessivo dichiarato fino a 2.100€. La parte più corposa, 2.000€ in 4 tranche da 500€ ciascuna, si affianca a un rimborso settimanale del 50% fino a 10€ per 10 settimane: un pacchetto costruito attorno alla campagna Mondiali 2026, non un bonus generico valido tutto l'anno.")
b.add_body(doc, "Il palinsesto sportivo supera le 25 discipline, con oltre 200 eventi in diretta ogni giorno tra calcio, tennis, basket, hockey su ghiaccio e pallavolo. Non manca l'eSport, con League of Legends tra i tornei coperti.")
b.add_body(doc, "Il ventaglio di prodotti va oltre scommesse e casinò: poker, bingo, ippica con diretta video e una suite di virtual sports, PGVirtual, che Planetwin365 è stato tra i primi grandi operatori italiani a introdurre.")
b.add_body(doc, "Tra chi scommette con regolarità, Planetwin365 gode di una reputazione che va oltre la scheda tecnica: non ricorre con facilità a limitazioni o chiusure di conto per i giocatori vincenti o per chi sfrutta sistematicamente le promozioni, un comportamento che nel mercato ADM non è affatto scontato. A questo si accompagna una gestione dei bonus spesso più generosa e personalizzata rispetto al solo pacchetto di benvenuto, un dettaglio che pesa nel tempo per chi gioca con continuità.")

b.add_h2(doc, "Dove Planetwin365 può migliorare (Contro)")
b.add_body(doc, "Il vincolo più segnalato da chi usa l'operatore con regolarità riguarda la struttura della multipla richiesta per validare i bonus: almeno 4 eventi per la componente sport, almeno 3 per quella slot, con quota minima per singolo evento. Per raggiungere la soglia capita di dover completare la giocata includendo sport o categorie minori, solo per arrivare al numero di eventi richiesto. Non è un vincolo esclusivo di Planetwin365, ma resta il più citato da chi lo utilizza abitualmente.")
b.add_body(doc, "La registrazione tramite SPID o CIE non è al momento disponibile: chi vuole aprire il conto con l'identità digitale deve procedere con l'inserimento manuale dei dati e il caricamento del documento entro 30 giorni, come da normativa ADM. Un limite che pesa nel confronto diretto con altri operatori del settore, incluso qualche marchio dello stesso gruppo proprietario.")
b.add_body(doc, "L'assistenza risponde a tariffa ordinaria, non su numero verde, con una finestra oraria (11:00-19:00) più stretta rispetto alla media degli operatori ADM. Sulla qualità del servizio, però, il canale è tra i più apprezzati del comparto: chi lo contatta segnala tempi di risposta rapidi, un bilanciamento da tenere presente prima di scartare l'operatore solo sulla base degli orari.")
b.add_divider(doc)

b.add_h1(doc, "PANORAMICA TRA EVENTI E STREAMING")
b.add_body(doc, "Il palinsesto di Planetwin365 copre oltre 25 discipline sportive, con più di 20 sport disponibili in pre-match e 7 sport nel comparto live ogni giorno, per oltre 200 eventi live complessivi. Il calcio resta il prodotto principale, con copertura di Serie A, Serie B, Coppa Italia e Champions League. Il tennis segue con i grandi tornei del circuito, Wimbledon e Coppa Davis tra questi, mentre Formula 1 e MotoGP completano l'offerta sui motori.")
b.add_body(doc, "Lo streaming live copre calcio, tennis, basket, hockey su ghiaccio e pallavolo. La profondità della copertura non emerge da fonti verificabili con la stessa precisione di altri comparti dell'offerta: resta un punto su cui l'operatore comunica meno rispetto, per esempio, al casinò live.")
b.add_divider(doc)

b.add_h1(doc, "TIPOLOGIA DI GIOCHI DISPONIBILI")
b.add_body(doc, "**Scommesse sportive**: oltre 25 discipline, dai grandi campionati all'eSport (League of Legends tra i tornei coperti), con quote pre-match, live e multiple.")
b.add_body(doc, "**Casinò online**: oltre 4.700 giochi, di cui più di 4.000 slot, distribuiti su un ampio ventaglio di provider. Titoli esclusivi del brand come Scarab Cash Megaways, PlanetWin Bonanza e Gold Blitz Ultimate.")
b.add_body(doc, "**Casinò live**: circa 200 titoli su 7 provider (Evolution, MediaLive, Authentic Gaming, Playtech Live, Pragmatic Play Live, LiveG24, Microgaming), con puntate da 0,50€ a 1.000€. Game show come Monopoly Live, Sweet Bonanza Candyland, Gonzo's Treasure Hunt e Crazy Time in versione italiana con host madrelingua.")
b.add_body(doc, "**Ippica**: sezione scommesse ippiche con diretta video degli eventi.")
b.add_body(doc, "**Virtual sports**: suite PGVirtual, corse di cavalli e cani preregistrate in alta definizione. Planetwin365 è stato tra i primi grandi operatori italiani a introdurla.")
b.add_body(doc, "**Poker, Bingo**: sezioni dedicate presenti nella piattaforma.")
b.add_divider(doc)

b.add_h1(doc, "PROMOZIONI")
b.add_h2(doc, "Bonus di benvenuto Sport")
b.add_info_table(doc, [
    ("Percentuale e massimale", "50% sul primo deposito, fino a 100€"),
    ("Deposito minimo qualificante", "20€, entro 7 giorni dalla registrazione"),
    ("Requisito di puntata", "Almeno 4 eventi, quota minima 1,50 per evento, quota totale minima 5,00"),
])
b.add_h2(doc, "Bonus di benvenuto Slot")
b.add_body(doc, "100% sul primo deposito, fino a 2.000€, erogato in 4 tranche da 500€ ciascuna.")
b.add_info_table(doc, [
    ("Rollover", "30 volte l'importo per ciascuna delle 4 tranche da 500€"),
    ("Finestra temporale", "3 giorni dall'accredito per completare il rollover di ciascuna tranche"),
])
b.add_h2(doc, "Rimborso settimanale")
b.add_body(doc, "50% fino a 10€ a settimana, su giocate multiple da almeno 3 eventi a quota minima 1,50 per evento. Promozione valida per 10 settimane, parte della stessa campagna legata ai Mondiali 2026.")
b.add_note_box(doc, "Nota importante", "tutte le condizioni (rollover, tempistiche, soglie) sono soggette ad aggiornamento da parte di Planetwin365. Verificare sempre i T&C ufficiali prima dell'attivazione di qualsiasi bonus.")
b.add_divider(doc)

b.add_h1(doc, "INFO SULLE QUOTE, MERCATI E FUNZIONALITÀ")
b.add_body(doc, "Planetwin365 costruisce l'offerta scommesse su un palinsesto ampio più che su una profondità di mercato fuori dalla media: calcio, tennis e basket restano i tre pilastri, affiancati da un comparto eSport che include League of Legends. Il vero terreno differenziante dell'operatore, però, non è la scommessa sportiva: è il casinò live, dove le esclusive Evolution (Blackjack Planetwin365, Planetwin365 Roulette Live) offrono qualcosa che il resto del mercato ADM non replica.")

b.add_h2(doc, "Come piazzare una scommessa su Planetwin365")
b.add_body(doc, "**STEP 1: Scegli l'evento** — Naviga il palinsesto o usa la ricerca rapida. Seleziona il mercato e la quota desiderata.")
b.add_body(doc, "**STEP 2: Componi la giocata** — Inserisci l'importo. Aggiungi altri eventi per una multipla, verificando che la quota totale rispetti eventuali requisiti bonus attivi.")
b.add_body(doc, "**STEP 3: Conferma** — Conferma la giocata. La ricevuta appare in tempo reale nella cronologia del conto.")
b.add_divider(doc)

b.add_h1(doc, "CONTO DI SCOMMESSA E REGISTRAZIONE")
b.add_body(doc, "**Registrazione**: compilazione del modulo con dati anagrafici, codice fiscale, email e numero di telefono, seguita dal caricamento di un documento d'identità valido entro 30 giorni dall'apertura del conto. Non è prevista, al momento, una via di accesso semplificata tramite SPID o CIE.")
b.add_body(doc, "**Requisiti di base**: maggiore età (18 anni), residenza in Italia, codice fiscale italiano, documento d'identità in corso di validità.")
b.add_divider(doc)

b.add_h1(doc, "METODI DI PAGAMENTO")
b.add_body(doc, "Planetwin365 mette a disposizione 8 modalità di deposito: Visa, Mastercard, PostePay, PayPal, Skrill, Neteller, Paysafecard e bonifico bancario.")
b.add_data_table(
    doc,
    ["Metodo", "Deposito minimo", "Prelievo"],
    [
        ["Carte (Visa/Mastercard)", "5€", "Sì"],
        ["PostePay", "5€", "Solo deposito"],
        ["PayPal", "5€", "Sì"],
        ["Skrill / Neteller", "5€", "Sì"],
        ["Paysafecard", "5€", "Solo deposito"],
        ["Bonifico bancario", "5€", "Sì"],
    ],
    highlight_col=None,
)
b.add_body(doc, "Nessuna commissione risulta applicata dall'operatore sui prelievi. I tempi di accredito indicati dalle fonti disponibili si aggirano sui 2-3 giorni lavorativi, in linea con la media degli operatori ADM soggetti ai controlli KYC previsti dalla normativa.")
b.add_divider(doc)

b.add_h1(doc, "SICUREZZA")
b.add_body(doc, "**Licenza ADM**: doppia concessione, n. 15242 per le scommesse e n. 16007 per il casinò online, entrambe in capo a PWO S.p.A. (Roma). Garanzia di legalità e tracciabilità delle operazioni secondo la normativa italiana.")
b.add_body(doc, "**Garanzia patrimoniale**: dall'aprile 2024 Planetwin365 fa parte del Gruppo Lottomatica, quotato su Euronext Milan e incluso nel FTSE MIB, il che rafforza la solidità economica dietro il brand.")
b.add_body(doc, "**Gioco responsabile**: strumenti di auto-limitazione dei depositi (con periodo di riflessione di 7 giorni per gli aumenti), autoesclusione temporanea o permanente, limiti di durata delle sessioni e test di autovalutazione, in conformità con le normative ADM.")
b.add_divider(doc)

b.add_h1(doc, "SERVE AIUTO? CUSTOMER SUPPORT")
b.add_body(doc, "Il servizio clienti è raggiungibile tramite telefono a tariffa ordinaria (06 9480 0931), live chat ed email (info@planetwin365.it), tutti attivi nella fascia 11:00-19:00.")
b.add_body(doc, "L'assenza di un numero verde e la finestra oraria più contenuta rispetto alla media di settore sono elementi da considerare per chi cerca assistenza fuori da questa fascia, in particolare in tarda serata o nel weekend. Nella fascia coperta, però, il servizio è tra i meglio valutati della categoria: tempi di risposta rapidi e problemi risolti spesso alla prima interazione.")
b.add_divider(doc)

b.add_h1(doc, "ALTRI PRODOTTI NELL'OFFERTA")
b.add_body(doc, "**Poker**: sezione dedicata, integrata nella piattaforma principale.")
b.add_body(doc, "**Bingo**: sezione presente a completamento dell'offerta di intrattenimento.")
b.add_body(doc, "**Virtual sports**: suite PGVirtual, corse preregistrate in HD. Planetwin365 tra i primi grandi operatori italiani ad averla introdotta.")
b.add_divider(doc)

b.add_h1(doc, "FEEDBACK E RECENSIONI")
b.add_body(doc, "Sull'App Store, Planetwin365 Scommesse Sport raggiunge una valutazione di 4,7/5 su circa 7.500 recensioni: un punteggio solido, in linea con i migliori risultati registrati dagli operatori ADM su questo canale.")
b.add_body(doc, "L'app non è distribuita su Google Play, per policy dello store sui prodotti di gioco con denaro reale: chi usa Android scarica l'applicazione come file APK direttamente dal sito ufficiale, una prassi comune a diversi concessionari italiani ma non a tutti.")
b.add_divider(doc)

b.add_h1(doc, "TABELLA COMPARATIVA: PLANETWIN365 VS SNAI VS GOLDBET")
b.add_data_table(
    doc,
    ["Caratteristica", "Planetwin365", "SNAI", "Goldbet"],
    [
        ["Bonus sport", "50% fino a 100€ + 100% fino a 2.000€ slot = 2.100€ (quota min. 1,50)", "500€ Gold (x6) + 500€ Game Bonus + 15€ free + 9€ extra = ~1.500€", "100% fino a 2.000€ (rollover x6)"],
        ["Deposito minimo bonus", "20€", "Non specificato in questa serie", "20€"],
        ["Proprietà", "Gruppo Lottomatica (dal 2024)", "Gruppo Flutter Entertainment (dal 2025)", "Gruppo Lottomatica"],
        ["Prodotto distintivo", "Casinò live con tavoli esclusivi Evolution", "Ippica, Snaipay, integrazione fisico-digitale", "Interfaccia mobile, quote competitive"],
        ["Discipline sportive", "25+", "25+", "Non verificato in questa serie"],
        ["Registrazione SPID/CIE", "Non disponibile", "Sì", "Non verificato in questa serie"],
        ["Licenza ADM", "15242 (sport) / 16007 (casinò)", "Non riportata in questa serie", "16009"],
    ],
    highlight_col=None,
    col_widths=None,
)
b.add_body(doc, "**Nota**: le cifre di tutti gli operatori rappresentano valori nominali massimi, soggetti a rollover e condizioni di sblocco spesso complesse. Il valore effettivo percepito dall'utente può essere molto inferiore al valore headline della promozione. Planetwin365 e Goldbet condividono oggi la stessa proprietà: la tabella li mette a confronto come prodotti distinti, non come alternative indipendenti.", size=9)
b.add_divider(doc)

b.add_h1(doc, "IL NOSTRO GIUDIZIO")
b.add_body(doc, "Planetwin365 arriva al 2026 con un'identità in trasformazione. Il brand nasce nel 2009 come costola italiana di un gruppo austriaco, SKS365, e per quindici anni cresce come concessionario indipendente. Dal 2024 è un tassello del Gruppo Lottomatica, nello stesso portafoglio di Betflag e Goldbet: tre marchi che il giocatore incontra come alternative diverse, ma che rispondono alla stessa proprietà.")
b.add_body(doc, "Il punto di forza reale dell'operatore, però, non si esaurisce nella scheda tecnica. Tra chi scommette con continuità, Planetwin365 ha costruito una reputazione specifica: non chiude né limita con facilità i conti dei giocatori vincenti o di chi sfrutta sistematicamente le promozioni, un comportamento raro nel mercato ADM, dove le limitazioni silenziose sono più la norma che l'eccezione. A questo si aggiunge una gestione dei bonus spesso più generosa e su misura rispetto al pacchetto di benvenuto standard, e un'assistenza clienti che, orari a parte, resta tra le più apprezzate del comparto.")
b.add_body(doc, "Sul fronte prodotto, la carta migliore è il casinò, in particolare la sezione live: sette provider, circa 200 titoli, e due tavoli realizzati da Evolution in esclusiva per il brand. Una caratteristica che nel mercato ADM pochi altri concessionari possono vantare.")
b.add_body(doc, "Il bonus di benvenuto tocca quota 2.100€ nominali, ma nasconde il vincolo più citato da chi lo usa con regolarità: la componente sport richiede multiple da almeno 4 eventi, quella slot da almeno 3, con quote minime per singolo evento. Per raggiungere la soglia capita di dover completare la giocata con sport o categorie minori, solo per arrivare al numero di eventi richiesto: un dettaglio strutturale più che una carenza, ma l'unico neo segnalato con costanza.")
b.add_body(doc, "Chi cerca un operatore che non intralcia chi vince, gestisce i bonus in modo personalizzato e offre un catalogo casinò tra i più profondi del mercato ADM, trova in Planetwin365 una delle scelte più solide della categoria. Chi cerca l'accesso più rapido possibile, via SPID o CIE, dovrà guardare altrove, almeno finché l'operatore non colma questo gap.")
b.add_final_score_box(doc, "VOTO FINALE: 4.5 SU 5")
b.add_divider(doc)

b.add_h1(doc, "FAQ")
b.add_h2(doc, "Planetwin365 è sicuro?")
b.add_body(doc, "Opera sotto doppia concessione ADM (n. 15242 per le scommesse, n. 16007 per il casinò) ed è controllato dal Gruppo Lottomatica dal 2024, uno degli operatori regolamentati più solidi del mercato italiano.")
b.add_h2(doc, "È possibile registrarsi con SPID o CIE su Planetwin365?")
b.add_body(doc, "No, non al momento. La registrazione richiede l'inserimento manuale dei dati anagrafici e il caricamento di un documento d'identità entro 30 giorni dall'apertura del conto.")
b.add_h2(doc, "Qual è la differenza tra bonus sport e bonus slot?")
b.add_body(doc, "Il bonus sport è il 50% del primo deposito fino a 100€, con requisito di puntata su almeno 4 eventi a quota minima 1,50. Il bonus slot è il 100% del primo deposito fino a 2.000€, erogato in 4 tranche da 500€, con un rollover di 30 volte l'importo per tranche da completare entro 3 giorni.")
b.add_h2(doc, "L'app Planetwin365 è disponibile su Android?")
b.add_body(doc, "Non tramite Google Play, per policy dello store sui prodotti di gioco con denaro reale. È scaricabile come file APK dal sito ufficiale dell'operatore.")
b.add_divider(doc)

b.add_h1(doc, "LE MIGLIORI ALTERNATIVE")
b.add_body(doc, "**Goldbet**: stesso gruppo proprietario di Planetwin365 dal 2024, bonus sport 100% fino a 2.000€ con rollover x6, interfaccia mobile apprezzata dalla fascia più giovane dell'utenza.")
b.add_body(doc, "**SNAI**: leadership storica nell'ippica, integrazione fisico-digitale con Snaipay, rollover x6 sul Bonus Gold tra i più accessibili del mercato.")
b.add_body(doc, "**Betflag**: terzo brand del Gruppo Lottomatica, unico insieme a Betfair a offrire il betting exchange tra i concessionari ADM, bonus sport tra i più alti del mercato.")

footer_p = doc.add_paragraph()
from docx.enum.text import WD_ALIGN_PARAGRAPH
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer_p.paragraph_format.space_before = b.Pt(14)
b._add_run(footer_p, "Il gioco è vietato ai minori di 18 anni • Bonus e T&C soggetti a modifica: verificare sempre su planetwin365.it", italic=True, color=b.GRAY, size=8)

doc.save(OUT)
print("Salvato:", OUT)
