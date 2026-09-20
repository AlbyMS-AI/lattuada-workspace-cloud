# Workflow Grafiche — Newsletter Bottadiculo.it
# 1 main image + 2 infografiche interne

**Sempre, non su richiesta (dal 20/09/2026).** Appena il testo finale della newsletter è pronto,
questo workflow si esegue nella stessa sessione, tutti e tre gli output. Non è un passo che
aspetta un "prepara le grafiche" separato — vedi `../piano-newsletter-linkedin-2026.md`,
sezione "Output per edizione".

**Tutto quello che è di Bottadiculo vive in `bottadiculo/grafiche/` (dal 20/09/2026),
non in `04-linkedin/grafiche/`.** Quella cartella è riservata alle grafiche personali di
Alberto (The Betting Edge, post personali). Struttura, identica a quella personale:

```
03-giornalismo/bottadiculo/grafiche/
├── src/
│   ├── templates/   ← i due template fissi (newsletter, post singolo)
│   └── [data]-[slug]-*.html   ← sorgenti compilati per edizione
└── [data]-[slug]-*.png   ← output finali
```

Il solo elemento condiviso resta lo script `render.sh`, in `04-linkedin/grafiche/render.sh`
(utility di rendering generica, non una grafica) — richiamato con percorso relativo.

**Palette:** quella reale di Bottadiculo.it, estratta dal sito live il 13/07/2026 e
documentata in `../../../04-linkedin/palette-brand.md`. Sfondo indigo `#1C0F3A`, accento
unico arancio `#F9511F`, secondario viola `#6330C7`, testo bianco `#FFFFFF`.

**Niente giorno/orario di pubblicazione nelle grafiche (dal 20/09/2026).** Non un sub-label
"lunedì 7:30", non altrove: cambia troppo spesso ed è informazione di servizio, non
editoriale. La data dell'edizione (kicker "#N · GG mese AAAA") resta, è identità
dell'edizione, non un orario.

**Main image standardizzata il 06/09/2026** (vedi sezione dedicata sotto): niente più
Canva/Gemini per-edizione. Un formato fisso rende Gambling Insights riconoscibile a colpo
d'occhio nel feed, sullo stesso modello di "The Betting Edge": cambia solo il testo,
l'identità visiva resta.

---

## 3 output per ogni edizione — tutti fatti da Claude

**Corretto il 20/09/2026:** le infografiche non passano più da NotebookLM. Il tentativo con
la sola tipografia (nessuna icona, nessuna illustrazione) produceva card leggibili ma che
non aggiungevano niente al testo — non spiegavano il meccanismo, lo ripetevano in un altro
carattere. Ora tutti e tre gli output usano la stessa pipeline HTML/SVG della main image,
con controllo diretto su diagrammi e icone disegnate ad hoc (mai icone stock/generiche).

| Output | Formato | Cosa deve fare |
|---|---|---|
| Main image | 1280×720px (16:9) | Identità dell'edizione: kicker, H1, sub — template fisso, non cambia mai il pannello sinistro |
| Infografica 1 | 1080×1350px (4:5) | **Un diagramma** che spiega il meccanismo del pezzo (flusso, confronto, causa/effetto) — non una frase isolata |
| Infografica 2 | 1080×1350px (4:5) | La sezione più strutturata (di solito "Cosa cambia da domani"), **un'icona propria per ogni punto**, coerente col contenuto di quel punto |

Le due infografiche non sono intercambiabili: la 1 spiega perché il fatto funziona come
funziona, la 2 traduce in azioni. Se il pezzo non ha un meccanismo diagrammabile,
l'infografica 1 diventa un confronto (before/after, due colonne) invece di una quote card
vuota — mai testo isolato senza un elemento visivo che lo sostenga.

---

## MAIN IMAGE — template fisso

### Come si usa
Sorgente: `src/templates/gambling-insights-cover-template.html`.
Per ogni edizione: copiarlo in `src/[data]-[slug]-cover.html`, compilare solo tre campi
nella sezione `.box` (kicker `#N · data`, h1, sub — una frase che riprende l'angolo, non
riassume la newsletter), poi:

```
cd 03-giornalismo/bottadiculo/grafiche
../../../04-linkedin/grafiche/render.sh png src/[data]-[slug]-cover.html [data]-[slug]-cover.png 1280x720
```

Il pannello sinistro (identità fissa: tassello arancio spezzato su sfondo indigo, wordmark
"Bottadiculo.it") non si tocca mai. Palette e struttura: vedi commento in testa al file
template.

---

## INFOGRAFICA 1 — diagramma del meccanismo

### Cosa deve mostrare
Non la frase più citabile del pezzo isolata su sfondo colorato. Il meccanismo che il pezzo
spiega, reso visivamente: un flusso (A succede, poi B, poi C), un confronto (due strade che
partono uguali e arrivano diverse), una causa che produce due effetti diversi a seconda di
una variabile. Il lettore deve capire il meccanismo guardando l'immagine, anche senza aver
letto il testo.

### Come si costruisce
Copiare la struttura da un file già fatto come riferimento di layout (es.
`src/2026-09-19-adm-blocco-dns-provider-infografica-1.html`: nodo in alto, biforcazione,
due colonne di confronto con icona + esito, nota finale). Icone disegnate come SVG inline,
forme semplici (cerchi, linee, rettangoli arrotondati) nello stile flat già usato nel logo
Bottadiculo — mai icone stock scaricate, mai clipart, mai emoji.

```
cd 03-giornalismo/bottadiculo/grafiche
../../../04-linkedin/grafiche/render.sh png src/[data]-[slug]-infografica-1.html [data]-[slug]-infografica-1.png 1080x1350
```

---

## INFOGRAFICA 2 — sezione strutturata con icone

### Cosa deve mostrare
Di norma "Cosa cambia da domani": ogni punto ha un'icona propria coerente col contenuto
di quel punto specifico (una lente per "verifica", un fumetto per "comunicazione", un
cronometro per "tempi"), non un numero o un checkbox generico. Se la sezione è un
before/after o un profilo, stessa logica: ogni blocco ha un elemento visivo che lo
distingue dagli altri, non solo il testo.

### Come si costruisce
Riferimento di layout: `src/2026-09-19-adm-blocco-dns-provider-infografica-2.html` (lista
di card, ognuna con icon-box + testo). Stessa regola sulle icone dell'infografica 1: SVG
disegnate ad hoc, mai stock.

```
cd 03-giornalismo/bottadiculo/grafiche
../../../04-linkedin/grafiche/render.sh png src/[data]-[slug]-infografica-2.html [data]-[slug]-infografica-2.png 1080x1350
```

---

## Export e salvataggio

| File | Nome | Dove |
|---|---|---|
| Main image | `[data]-[slug]-cover.png` | `bottadiculo/grafiche/` |
| Infografica 1 | `[data]-[slug]-infografica-1.png` | `bottadiculo/grafiche/` |
| Infografica 2 | `[data]-[slug]-infografica-2.png` | `bottadiculo/grafiche/` |
| Nota di produzione (cosa mostra ciascuna, non un brief per tool esterno) | `[data]-[slug]-grafiche.md` | `bottadiculo/drafts/` |

---

## Checklist finale prima di usare le grafiche

- [ ] Main image leggibile a 300px di larghezza (anteprima mobile WordPress)
- [ ] Infografiche leggibili a 540px (feed LinkedIn mobile)
- [ ] Ogni infografica ha almeno un elemento grafico reale (diagramma o icona), non solo testo su sfondo colorato
- [ ] Nessuna icona stock, nessuna emoji, nessun logo di terzi
- [ ] Nessun giorno/orario di pubblicazione nel testo della grafica
- [ ] Nessun testo troncato o tagliato dai bordi
- [ ] Palette coerente tra i 3 output (stesso sfondo, stessi accenti)
- [ ] Alt text pronto per tutte e tre le grafiche (vedere SEO output)
