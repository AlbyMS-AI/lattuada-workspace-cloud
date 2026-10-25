# -*- coding: utf-8 -*-
# Genera il .md sorgente dal contenuto condiviso e ci aggiunge le note fact-check,
# che restano solo qui: sono per Alberto e il caporedattore, non vanno nel docx/pdf.
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
import content as c

OUT = os.path.join(HERE, "recensione-sisal-2026.md")

FACT_CHECK = """## Note interne (non vanno nel docx/pdf)

Versione del 25/10/2026, metodo prova sul campo sul modello MyLotteries. Fonti e decisioni di Alberto in `prova-sul-campo-2026-10.md`.

- **Fonti**: sisal.it blocca gli accessi automatici (Akamai): T&C, contratto, concessione, FAQ e pagine bonus salvati in PDF da Alberto il 24-25/10/2026, in questa cartella.
- **Check**: verificatore-fatti su elenco chiuso; revisore-astra 6/10 e revisore-codex 6,5/10 (locali, Codex e Astra senza crediti fino al 01/11); check esterno di Alberto. Correzioni applicate.
- **Decisioni di Alberto**: voto 4,5/5; tutti sullo stesso piano, niente classifica né voti delle app affiancati; formato MyLotteries; massimale casinò 7.000€ non commentato; Sicurezza 9/10; osservazioni dal campo marcate "nella nostra esperienza".
- **Da rimisurare il giorno dell'invio**: rating App Store, bonus.
- **Fuori dal pezzo**: il Sitiscommesse del 09/09 su Win for Italia Team ("solo nei punti vendita") risulta impreciso; Alberto ha deciso di non segnalarlo.
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
