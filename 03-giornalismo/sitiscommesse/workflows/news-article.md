# Workflow — Articolo News (Sitiscommesse.com)

## Format
- Struttura: intro + 6 paragrafi da ~50 parole (standard) — vedi `../guidelines.md` per struttura completa
- Audience: scommettitori italiani (B2C)
- Tono: informativo, neutrale, zero opinioni

## Input necessari
- [ ] Notizia / tema di partenza
- [ ] Fonti disponibili (link, comunicati, AGIPRO, AGIMEG, ADM)
- [ ] Keyword SEO principale
- [ ] Link interno da inserire (se disponibile)
- [ ] Trust link (fonte autorevole esterna) da inserire

## Step del flusso

### Step 1 — Valutazione notizia
- È rilevante per uno scommettitore italiano?
- Ha impatto pratico per il lettore o è solo tecnico/industriale (→ Jamma)?
- La notizia è verificabile con fonti primarie?

### Step 2 — Ricerca e verifica fatti
- Verifica su fonti primarie: ADM, comunicati operatori, AGIPRO, AGIMEG
- Raccogli: chi, cosa, quando, impatto pratico per il lettore
- **Nessuna citazione diretta** senza link alla fonte — usa discorso indiretto
- Identifica un trust link (fonte istituzionale o autorevole) da inserire nel testo

### Step 3 — Scrittura

Produci nell'ordine:

```
SEO Title: [60-65 caratteri — keyword principale inclusa]
Meta description: [150-155 caratteri — keyword + CTA]
Caption: [max 10 parole — descrive il topic principale]

<strong>INTRO</strong>
[35-40 parole — Chi/Cosa/Quando, subito al punto]

<h2>[30-50 caratteri]</h2>
[Paragrafo 1 — 50-60 parole — <strong>bold 3-8 parole sul topic principale</strong>]
[Paragrafo 2 — 50-60 parole — <strong>bold 3-8 parole sul topic principale</strong>]
[Paragrafo 3 — 50-60 parole — <strong>bold 3-8 parole sul topic principale</strong>]

<h2>[30-50 caratteri]</h2>
[Paragrafo 4 — 50-60 parole — <strong>bold 3-8 parole</strong>]
[Paragrafo 5 — 50-60 parole — <strong>bold 3-8 parole</strong>]
[Paragrafo 6 — 50-60 parole — <strong>bold 3-8 parole</strong> — inserire trust link qui]
```

**Nota 2026**: se gli h2 non aggiungono valore alla notizia, omettili e scrivi il testo come blocco unico.

### Step 4 — Gestione link

**Link interni** (senza target blank):
- Formato: `<a href="/slug">anchor</a>`
- Consulta `../archive/` per esempi di anchor interni corretti
- Non linkare a siti concorrenti di sitiscommesse.com

**Trust link** (con target blank):
- Formato: `<a href="https://fonte.it" target="_blank">anchor</a>`
- Uno per articolo, in uno dei paragrafi del secondo blocco
- Fonti: ADM, AGIPRO, AGIMEG, operatori ADM, siti istituzionali

### Step 5 — Conteggio e verifica struttura
Controlla prima di chiudere:
- [ ] SEO Title: 60-65 caratteri (conta!)
- [ ] Meta description: 150-155 caratteri (conta!) + CTA presente
- [ ] Caption: max 10 parole
- [ ] Intro: 35-40 parole
- [ ] Ogni paragrafo: 50-60 parole
- [ ] Bold presente in ogni paragrafo (3-8 parole)
- [ ] Trust link inserito (con target="_blank")
- [ ] Nessuna citazione diretta senza fonte
- [ ] Nessuna opinione o commento

### Step 6 — Verifica link
- Testa ogni link inserito (interno ed esterno) prima di dichiarare l'articolo pronto
- Segnala eventuali link che non riesci a verificare

### Step 7 — Umanizzazione
- Rimuovi strutture meccaniche
- Tono da giornalista pratico, non da comunicato stampa
- Nessuna frase da AI: "è importante sottolineare che", "vale la pena notare", ecc.

## Output
Articolo pronto in `../../archive/sitiscommesse/[slug]-[data].md`

Formato output:
```
# [SEO Title]
**Meta description**: [testo]
**Caption**: [testo]
---
[articolo in HTML inline: <strong>, <h2>, <a>]
```
