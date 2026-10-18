# -*- coding: utf-8 -*-
# Genera il .md sorgente dal contenuto condiviso e ci aggiunge le note fact-check,
# che restano solo qui: sono per Alberto e il caporedattore, non vanno nel docx/pdf.
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
import content as c

OUT = os.path.join(HERE, "recensione-mylotteriesplay-2026.md")

FACT_CHECK = """## Note interne (non vanno nel docx/pdf)

Versione del 16/10/2026: rifatta col metodo "prova sul campo" (`../_template/prova-sul-campo.md`). Risposte di Alberto e fonti incrociate in `prova-sul-campo-2026-10.md`. Sostituisce la bozza del 28-29/09/2026 (check Codex 5,5/10 e Astra #527 sulla vecchia stesura).

- **Check fatti (17/10/2026)**: verificatore-fatti, Codex, Astra (#106, voto 7/10). Correzioni applicate con Alberto una alla volta; dettaglio in `prova-sul-campo-2026-10.md`.
- **Pagine ufficiali discordanti**: prelievi (tabella generale 24-48 ore carta / 24 ore PayPal; pagine dedicate 3-5 giorni lavorativi carta / evasione entro 3 PayPal): scelta di Alberto, valgono le pagine dedicate. Ricarica massima carta: 1.000€ tabella generale, 950€ pagina dedicata: scritte entrambe.
- **Affiliazione**: Bottadiculo è in affiliazione (Alberto, 17/10). Tolti il pulsante "VAI SU" e il bonus in copertina, formule descrittive al posto degli inviti alla scelta (rischio AGCOM 132/19/CONS). Da segnalare a Francesco per le cinque recensioni già uscite.
- **Bonus di benvenuto e Bonus Multipla**: riverificati il 17/10/2026 sulle pagine ufficiali (validi fino al 31/12/2026).
- **Dati di reputazione**: App Store 3,3 su 27 (API iTunes, 16/10); Trustpilot 1,7 su 23 (16/10); Goldbet 25.766 valutazioni (API, 17/10). Rimisurare il giorno dell'invio.
- **Voti**: decisi con Alberto il 17/10 (lotterie 8, il resto confermato); media 7/10 = 3,5/5.
- **Android**: app distribuita come APK dal sito ufficiale.
- **Detector**: Pangram 39-81% AI secondo il testo, QuillBot 100% umano; non si insegue il punteggio (vedi video Gaito del 07/10/2026).
- **Avvertenza**: "può causare dipendenza patologica" nel footer; da estendere alle altre recensioni.
"""


def bullet(text):
    return f"- {text}"


lines = [f"# {c.HEADER.replace('  ', ' ')}", "", f"**{c.TITLE}**", c.SUBTITLE, ""] + ([c.CTA, ""] if c.CTA else []) + ["---", ""]
stars, t2, s2, t3, s3 = c.RATING
lines += [f"{stars} | {t2}: {s2} | {t3}: {s3}", ""]

for block in c.BLOCKS:
    kind, args = block[0], block[1:]
    if kind == "h1":
        lines += [f"## {args[0]}", ""]
    elif kind == "h2":
        lines += [f"### {args[0]}", ""]
    elif kind in ("body", "small"):
        lines += [args[0], ""]
    elif kind == "info":
        lines += ["| Campo | Dettaglio |", "|---|---|"] + [f"| {k} | {v} |" for k, v in args[0]] + [""]
    elif kind == "callout":
        lines += [f"### {args[0]}", ""] + [bullet(x) for x in args[1]] + [""]
    elif kind == "table":
        headers, rows = args[0], args[1]
        lines += ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
        lines += ["| " + " | ".join(r) + " |" for r in rows] + [""]
    elif kind == "avg":
        lines += [f"**{args[0]}**", ""]
    elif kind == "note":
        lines += [f"**{args[0]}**: {args[1]}", ""]
    elif kind == "final":
        lines += [f"## {args[0]}", ""]
    elif kind == "divider":
        lines += ["---", ""]

lines += [c.FOOTER, "", "---", "", FACT_CHECK]

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Salvato:", OUT)
