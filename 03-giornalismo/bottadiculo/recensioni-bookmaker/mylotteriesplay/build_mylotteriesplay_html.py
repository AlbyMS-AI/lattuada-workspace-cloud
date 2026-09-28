# -*- coding: utf-8 -*-
import html as _html
import os
import re
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
import content as c

CSS_PATH = os.path.join(HERE, "..", "_template", "review_style.css")
OUT_HTML = os.path.join(HERE, "recensione-mylotteriesplay-2026.html")

with open(CSS_PATH, "r", encoding="utf-8") as f:
    CSS = f.read()

# Fix di impaginazione PDF solo per questa recensione (il template condiviso resta invariato):
# tabelle brevi non spezzate a cavallo di pagina, box del voto finale attaccato al giudizio.
CSS += """
.data-table, .info-table { break-inside: avoid; }
.final-score-box { break-before: avoid; }
.final-score-box + hr, p.body-text:has(+ .final-score-box) { break-before: avoid; }
"""


def fmt(text):
    """Escape HTML e converte il **grassetto** markdown in <b>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", _html.escape(text, quote=False))


parts = [f'<div class="doc-top-note">{fmt(c.HEADER)}</div>']
parts.append(f'<h1 class="doc-title">{fmt(c.TITLE)}</h1><p class="doc-subtitle">{fmt(c.SUBTITLE)}</p>')
stars, t2, s2, t3, s3 = (fmt(x) for x in c.RATING)
parts.append(f'''
<table class="rating-box"><tr>
  <td><span class="stars">{stars}</span></td>
  <td><span class="col-title">{t2}</span><span class="col-sub">{s2}</span></td>
  <td><span class="col-title">{t3}</span><span class="col-sub">{s3}</span></td>
</tr></table>''')
parts.append(f'<div class="cta-bar">{fmt(c.CTA)}</div>')
parts.append('<hr class="divider">')


def data_table(headers, rows, highlight_col):
    ths = "".join(f"<th>{fmt(h)}</th>" for h in headers)
    trs = ""
    for row in rows:
        tds = ""
        for i, val in enumerate(row):
            cls = ' class="highlight-col"' if i == highlight_col else (' class="label-col"' if i == 0 else "")
            tds += f"<td{cls}>{fmt(val)}</td>"
        trs += f"<tr>{tds}</tr>"
    return f'<table class="data-table"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'


for block in c.BLOCKS:
    kind, args = block[0], block[1:]
    if kind == "h1":
        parts.append(f'<h2 class="section avoid-break">{fmt(args[0])}</h2>')
    elif kind == "h2":
        parts.append(f'<h3 class="subsection avoid-break">{fmt(args[0])}</h3>')
    elif kind == "body":
        parts.append(f'<p class="body-text">{fmt(args[0])}</p>')
    elif kind == "small":
        parts.append(f'<p class="body-text" style="font-size:9pt">{fmt(args[0])}</p>')
    elif kind == "info":
        trs = "".join(f'<tr><td class="label">{fmt(k)}</td><td>{fmt(v)}</td></tr>' for k, v in args[0])
        parts.append(f'<table class="info-table">{trs}</table>')
    elif kind == "callout":
        lis = "".join(f"<li>{fmt(it)}</li>" for it in args[1])
        parts.append(f'<div class="callout-box avoid-break"><p class="callout-heading">{fmt(args[0])}</p><ul>{lis}</ul></div>')
    elif kind == "table":
        parts.append(data_table(*args))
    elif kind == "avg":
        parts.append(f'<p class="average-score">{fmt(args[0])}</p>')
    elif kind == "note":
        parts.append(f'<div class="note-box avoid-break"><span class="note-label">{fmt(args[0])}: </span>{fmt(args[1])}</div>')
    elif kind == "final":
        parts.append(f'<div class="final-score-box avoid-break">{fmt(args[0])}</div>')
    elif kind == "divider":
        parts.append('<hr class="divider">')

parts.append(f'<p class="body-text" style="text-align:center;color:#666666;font-size:8pt;font-style:italic;margin-top:18px">{fmt(c.FOOTER)}</p>')

page = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Recensione My Lotteries Play 2026</title>
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(page)

print("Salvato:", OUT_HTML)
