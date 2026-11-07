# -*- coding: utf-8 -*-
"""Paginate a block-based book module into a fixed-trim interior, then render it.

The engine measures every block in headless Chromium and packs blocks into
sheets of an exact height, keeping a heading with the text that follows it.
That is what makes a fixed-page PDF possible from flowing HTML.

A "book module" is any Python module exposing:

    META, INTRO, CHAPTERS, CLOSING, GLOSSARY, BIBLIOGRAPHY, POEM, INDEX_TERMS

Blocks are HTML strings. The kinds understood are chapter-open divs, h2/h3,
p, table.data, div.callout, div.vignette, figure.fig and the poem's stanza/line.
"""

from __future__ import annotations
import importlib, json, os, re, subprocess, sys, html as _html

CHROMIUM = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")
DPI = 96.0


# ---------------------------------------------------------------- measuring
def measure(blocks, css, content_w, workdir, timeout=280):
    """Return the rendered height of each block, in px."""
    css_path = os.path.join(workdir, "_measure.css")
    with open(css_path, "w", encoding="utf-8") as fh:
        fh.write(css + "\n.mwrap{display:flow-root;width:%.2fpx;}\n" % content_w)
    parts = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
             '<link rel="stylesheet" href="file://%s">' % css_path, '</head><body>']
    for i, b in enumerate(blocks):
        parts.append('<div class="mwrap" data-i="%d">%s</div>' % (i, b))
    parts.append('<script>window.addEventListener("load",function(){var a=[];'
                 'document.querySelectorAll(".mwrap").forEach(function(w){a.push(w.getBoundingClientRect().height);});'
                 'document.documentElement.innerHTML="<body><pre id=\\"out\\">"+JSON.stringify(a)+"</pre></body>";});</script>'
                 '</body></html>')
    page = os.path.join(workdir, "_measure.html")
    with open(page, "w", encoding="utf-8") as fh:
        fh.write("".join(parts))
    r = subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--virtual-time-budget=25000", "--dump-dom",
                        "file://" + page], capture_output=True, text=True, timeout=timeout)
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    if not m:
        raise RuntimeError("block measurement failed:\n" + (r.stdout or r.stderr)[:600])
    return json.loads(_html.unescape(m.group(1)))


def is_heading(b):
    s = b.lstrip()
    return s.startswith('<h2') or s.startswith('<h3') or 'chapter-open' in s[:40]


def pack(blocks, heights, avail):
    pages, cur, curh = [], [], 0.0
    for blk, h in zip(blocks, heights):
        if cur and curh + h > avail:
            pages.append(cur); cur, curh = [], 0.0
        cur.append(blk); curh += h
    if cur:
        pages.append(cur)
    # never leave a heading stranded at the foot of a page
    moved = True
    while moved:
        moved = False
        for i in range(len(pages) - 1):
            if pages[i] and is_heading(pages[i][-1]):
                pages[i + 1].insert(0, pages[i].pop()); moved = True
    return [p for p in pages if p]


# ---------------------------------------------------------------- geometry
def geometry(trim, inside, outside, top, bottom):
    """Content box in px, and the sheet in px, from inches."""
    w, h = trim
    return {
        "sheet_w": round(w * DPI, 2), "sheet_h": round(h * DPI, 2),
        "content_w": round((w - inside - outside) * DPI, 2),
        "content_h": round((h - top - bottom) * DPI, 2),
        "inside": inside, "outside": outside, "top": top, "bottom": bottom,
    }


def trim_css(g, bleed=0.0):
    """The @page rule and the mirrored padding. Without @page the PDF is Letter."""
    return f"""
@page {{ size: {g['sheet_w'] / DPI:.4f}in {g['sheet_h'] / DPI:.4f}in; margin: 0; }}
.sheet{{ position:relative; width:{g['sheet_w']}px; height:{g['sheet_h']}px;
        background:#fff; overflow:hidden; margin:0 auto; }}
.book > .sheet:nth-child(odd)  > .page-content{{ padding:{g['top']*DPI:.1f}px {g['outside']*DPI:.1f}px {g['bottom']*DPI:.1f}px {g['inside']*DPI:.1f}px; }}
.book > .sheet:nth-child(even) > .page-content{{ padding:{g['top']*DPI:.1f}px {g['inside']*DPI:.1f}px {g['bottom']*DPI:.1f}px {g['outside']*DPI:.1f}px; }}
.book > .sheet:nth-child(odd)  .page-foot{{ left:{g['inside']*DPI:.1f}px; right:{g['outside']*DPI:.1f}px; }}
.book > .sheet:nth-child(even) .page-foot{{ left:{g['outside']*DPI:.1f}px; right:{g['inside']*DPI:.1f}px; }}
.page-content{{ height:100%; position:relative; }}
.page-foot{{ position:absolute; bottom:0.36in; display:flex; align-items:center;
            font-size:7.5pt; letter-spacing:0.12em; text-transform:uppercase; }}
.page-foot .rule{{ flex:1; height:1px; background:#ddd; margin:0 10px; }}
"""


# ---------------------------------------------------------------- assembly
def open_head(kicker, title):
    return f'<div class="chapter-open"><span class="chap-num">{kicker}</span><h1>{title}</h1></div>'


def build_master(modname, css, g, out_html, extra_sections=None, front_sheets=None,
                 foot_titles=True, workdir="."):
    """Lay the book out and write a fixed-page HTML master. Returns a manifest."""
    mod = importlib.import_module(modname)
    meta = mod.META
    poem_key = mod.POEM["key"]

    def sheet(inner, cls="", foot=None):
        f = (f'<div class="page-foot"><span>{foot}</span><span class="rule"></span>'
             f'<span class="pg">{{PG}}</span></div>') if foot is not None else ""
        return f'<section class="sheet {cls}">{inner}{f}</section>'

    front = front_sheets or []
    n_front = len(front)

    glossary_sec = {"key": "glossary", "title": "Glossary", "blocks":
                    [open_head("Reference", "Glossary")]
                    + [f'<div class="entry"><span class="term">{t}.</span> {d}</div>'
                       for t, d in mod.GLOSSARY]}
    bib_sec = {"key": "bibliography", "title": "Bibliography", "blocks":
               [open_head("Reference", "Bibliography"), '<div class="biblio">']
               + [f'<div class="ref">{r}</div>' for r in mod.BIBLIOGRAPHY] + ['</div>']}

    PRE = [mod.INTRO] + list(mod.CHAPTERS) + [mod.CLOSING, glossary_sec]
    POST = [bib_sec] + list(extra_sections or [])
    titles = {s["key"]: s["title"] for s in PRE + POST + [mod.POEM]}
    titles["index"] = "Index"

    CHUNK = 24
    ROW = '<li><span class="t">{t}</span><span class="dots"></span><span class="pg">{p}</span></li>'

    def contents(rows):
        blocks = [open_head("Front", "Contents")]
        for i in range(0, len(rows), CHUNK):
            grp = rows[i:i + CHUNK]
            blocks.append('<ul class="toc-list">' + "".join(ROW.format(t=t, p=p) for t, p in grp) + '</ul>')
        return blocks

    listed = [s["key"] for s in PRE] + ["index"] + [s["key"] for s in POST] + [poem_key]
    toc_ph = contents([(titles[k], "000") for k in listed])

    layout, allb = [], []
    for s in PRE + POST:
        layout.append((s["key"], len(allb), len(s["blocks"]))); allb += s["blocks"]
    layout.append(("__contents__", len(allb), len(toc_ph))); allb += toc_ph
    layout.append((poem_key, len(allb), len(mod.POEM["blocks"]))); allb += mod.POEM["blocks"]

    hh = measure(allb, css, g["content_w"], workdir)
    H = {k: hh[i:i + n] for k, i, n in layout}

    pageno = n_front + 1
    start, pages = {}, {}
    toc_pages = pack(toc_ph, H["__contents__"], g["content_h"])
    pageno += len(toc_pages)
    for s in PRE:
        start[s["key"]] = pageno
        pages[s["key"]] = pack(s["blocks"], H[s["key"]], g["content_h"])
        pageno += len(pages[s["key"]])

    # index, now that the pages it points at exist
    start["index"] = pageno
    ranges = {k: (start[k], start[k] + len(pages[k]) - 1) for k in [s["key"] for s in PRE]}

    def txt(sec):
        t = re.sub(r'<[^>]+>', ' ', sec); t = re.sub(r'&[a-z]+;', ' ', t)
        return re.sub(r'\s+', ' ', t).lower()
    placed = list(front) + ["".join(p) for p in toc_pages]
    for s in PRE:
        placed += ["".join(p) for p in pages[s["key"]]]
    ptext = {i + 1: txt(s) for i, s in enumerate(placed)}

    entries = []
    for term, keys in mod.INDEX_TERMS:
        key = term.split(',')[0].strip().lower()
        got = []
        for k in keys:
            if k not in ranges:
                continue
            lo, hi = ranges[k]; hit = None
            for p in range(lo, hi + 1):
                if key and key in ptext.get(p, ""):
                    hit = p; break
            got.append(hit if hit else lo)
        entries.append((term, sorted(set(got))))
    entries.sort(key=lambda x: x[0].lower())
    letters = {}
    for term, pgs in entries:
        letters.setdefault(term[0].upper(), []).append((term, pgs))
    idx_blocks = [open_head("Reference", "Index")]
    for L in sorted(letters):
        items = "".join(f'<div class="item">{t}, {", ".join(map(str, p))}</div>' for t, p in letters[L])
        idx_blocks.append(f'<div class="idx"><div class="letter">{L}</div>{items}</div>')
    pages["index"] = pack(idx_blocks, measure(idx_blocks, css, g["content_w"], workdir), g["content_h"])
    pageno += len(pages["index"])

    for s in POST:
        start[s["key"]] = pageno
        pages[s["key"]] = pack(s["blocks"], H[s["key"]], g["content_h"])
        pageno += len(pages[s["key"]])
    start[poem_key] = pageno
    pages[poem_key] = pack(mod.POEM["blocks"], H[poem_key], g["content_h"])
    pageno += len(pages[poem_key])

    toc_pages = pack(contents([(titles[k], start[k]) for k in listed]), H["__contents__"], g["content_h"])

    sheets = list(front)
    for pg in toc_pages:
        sheets.append(sheet('<div class="page-content">' + "".join(pg) + '</div>', foot="Contents"))
    order = [s["key"] for s in PRE] + ["index"] + [s["key"] for s in POST] + [poem_key]
    for k in order:
        for pg in pages[k]:
            sheets.append(sheet('<div class="page-content">' + "".join(pg) + '</div>',
                                foot=titles[k] if foot_titles else None))
    for i in range(len(sheets)):
        sheets[i] = sheets[i].replace("{PG}", str(i + 1))
    # the page count is the number of sheets actually written, not an
    # arithmetic projection — they diverged once and the cover spine was cut
    # from the wrong number.
    total = len(sheets)

    doc = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
           f'<title>{meta["title"]}</title><style>{css}</style></head>'
           f'<body><div class="book">{"".join(sheets)}</div></body></html>')
    with open(out_html, "w", encoding="utf-8") as fh:
        fh.write(doc)
    return {"total_pages": total, "start": start, "contents_pages": len(toc_pages),
            "index_pages": len(pages["index"]), "html_bytes": len(doc)}


# ---------------------------------------------------------------- rendering
def render_pdf(html_path, out_pdf, gray=False, palette_css="", timeout=290):
    """Print the master to PDF. gray=True swaps the palette to greys.

    Palette substitution, not a CSS filter: a filter forces rasterisation and
    inflates the file roughly twentyfold while killing text selection.
    """
    src = open(html_path, encoding="utf-8").read()
    if gray and palette_css:
        src = src.replace("</head>", "<style>" + palette_css + "</style></head>")
    tmp = os.path.abspath(html_path.replace(".html", "_render.html"))
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(src)
    if os.path.exists(out_pdf):
        os.remove(out_pdf)
    r = subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--no-pdf-header-footer", "--virtual-time-budget=40000",
                        "--print-to-pdf=" + os.path.abspath(out_pdf), "file://" + tmp],
                       capture_output=True, timeout=timeout)
    os.remove(tmp)
    # Chromium exits 0 even when it fails to write; the file is the only proof
    if not os.path.exists(out_pdf) or os.path.getsize(out_pdf) < 2000:
        raise RuntimeError("PDF render produced nothing for " + out_pdf +
                           "\n" + (r.stdout or b"").decode("utf-8", "replace")[:400] +
                           (r.stderr or b"").decode("utf-8", "replace")[:400])
    return out_pdf


def pdf_info(path):
    r = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60)
    d = {}
    for ln in r.stdout.splitlines():
        if ":" in ln:
            k, v = ln.split(":", 1); d[k.strip()] = v.strip()
    return d


GRAY_PALETTE = """
:root{--paper:#f7f7f7;--paper-edge:#ededed;--ink:#1b1b1b;--ink-soft:#3b3b3b;
--ink-faint:#6a6a6a;--accent:#3a3a3a;--accent-deep:#2a2a2a;--gold:#6e6e6e;
--rule:#dbdbdb;--rule-strong:#b8b8b8;--zebra:#eeeeee;}
table.data th, table th{background:#3a3a3a !important;color:#fff !important;}
.vignette,.callout,.box{background:#f1f1f1 !important;}
"""
