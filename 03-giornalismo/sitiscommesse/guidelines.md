# Linee Guida Editoriali — Sitiscommesse.com

## Identità della testata
Sitiscommesse.com è un portale di news e informazioni sul mondo delle scommesse sportive online in Italia. Lettore tipo: appassionato di scommesse che vuole essere aggiornato su notizie, operatori, promozioni, normative. Audience B2C.

## Tono
- Informativo e pratico, mai opinionistico
- **Zero opinioni o commenti personali** — solo fatti
- Chiaro e diretto, senza gergo tecnico B2B
- Neutrale: non prendere posizioni, riportare i fatti

## Specifiche SEO e metadati

| Campo | Specifica |
|---|---|
| SEO Title | 60-65 caratteri max |
| Meta description | 150-155 caratteri max — includere sempre una **CTA** |
| Caption (didascalia foto) | Max 10 parole — descrive il topic principale dell'articolo |

## Struttura articolo news standard (6 paragrafi + intro, blocco unico)

```html
<!-- METADATI -->
SEO Title: [60-65 caratteri]
Meta description: [150-155 caratteri — con CTA]
Caption: [max 10 parole]

<!-- CORPO ARTICOLO -->
<strong>INTRO</strong> — 35-40 parole

Paragrafo 1 — 50-60 parole — <strong>bold su topic principale (3-8 parole)</strong>
Paragrafo 2 — 50-60 parole — <strong>bold su topic principale (3-8 parole)</strong>
Paragrafo 3 — 50-60 parole — <strong>bold su topic principale (3-8 parole)</strong>
Paragrafo 4 — 50-60 parole — <strong>bold su topic principale (3-8 parole)</strong>
Paragrafo 5 — 50-60 parole — <strong>bold su topic principale (3-8 parole)</strong>
Paragrafo 6 — 50-60 parole — <strong>bold su topic principale (3-8 parole)</strong>
             ↑ in uno dei par. 4-6 inserire il trust link: <a href="url" target="_blank">anchor</a>
```

**Niente `<h2>`**: il corpo va sempre scritto come blocco unico di paragrafi, senza sottotitoli. Non è una scelta caso per caso: gli h2 non vanno mai usati (confermato 07/07/2026).

Lunghezza corpo (intro + paragrafi, esclusi metadati): **450-550 parole di default**. Per notizie con più angoli fattuali da spiegare (es. soglie diverse per casistica, confronto prima/dopo, aliquote, dati tecnici) si può estendere fino a **550-650 parole**, aggiungendo paragrafi extra allo stesso blocco unico — mai un nuovo `<h2>`. Se in dubbio su quale range usare, chiedere.

## Articolo esteso (solo per notizie più complesse)

Aggiungere 3-4 paragrafi extra da ~50-60 parole ciascuno all'unico blocco di testo (non un `<h2>` aggiuntivo). Usare solo se la notizia lo richiede davvero — non allungare per allungare.

## Regole sui link

### Link interni
- Formato: `<a href="/slug-pagina">anchor text</a>` — **senza** `target="_blank"`
- Anchor text: descrittivo e rilevante per la pagina di destinazione
- Non linkare a siti concorrenti di sitiscommesse.com
- Seguire gli esempi in `../archive/` per stile di anchor interni ed esterni

### Trust link (link esterni a fonti autorevoli)
- Formato: `<a href="https://url-fonte" target="_blank">anchor text</a>` — **con** `target="_blank"`
- Inserire **uno** per articolo, in uno dei paragrafi del secondo blocco
- Fonti accettabili: ADM, AGIPRO, AGIMEG, siti istituzionali, operatori con licenza ADM

### Verifica link
- **I link devono essere testati e funzionanti** prima dell'invio
- Nessun link a pagine 404 o redirect non pertinenti

## Regole su citazioni e dichiarazioni
- **Nessuna dichiarazione virgolettata diretta** — se non si può linkare la fonte, non si cita testualmente
- Usa sempre il **discorso indiretto**: "secondo X", "come ha dichiarato Y a [testata]", "stando a quanto riportato da..."

## Regole sul grassetto
- Bold (`<strong>`) solo sul topic principale del paragrafo
- 3-8 parole per volta, massimo
- Non usare il bold per decorazione o enfasi generica

## Cose da evitare
- Opinioni, commenti, punti di vista personali
- Titoli clickbait
- Paragrafi senza una conclusione del pensiero
- Link non testati o a siti concorrenti
- Citazioni dirette senza link alla fonte
- Testo sopra le 65 parole per paragrafo (rimani nei range)

## Checklist anti-AI
Vale anche per Sitiscommesse la checklist in `../../01-tono-di-voce/anti-ai-checklist.md`
(trattino lungo, aperture da formula, pattern "Non è X. È Y.", lessico da evitare, ritmo
delle frasi). **Eccezione**: il punto 7 (presa di posizione) non si applica — la testata
resta strutturalmente neutra, zero opinioni.
