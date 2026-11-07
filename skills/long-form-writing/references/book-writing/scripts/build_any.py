# -*- coding: utf-8 -*-
"""Generic builder: assemble a book from a content module plus a language kit.

Reads everything book-specific from the content module (META, the section lists,
and the FIGURES map) and picks the front/back-matter kit by the module's
META["lang"] (`bookkit_<lang>`, falling back to `bookkit`). Paginates with
headless Chromium. Works for any book, in any language, with no per-book edits.

Usage:
    BOOK_DIR=/path/to/project python3 build_any.py <content_module> <out.html>
"""
import os, sys, json, re, html, subprocess, importlib
import booklib, themes

BOOK = booklib.book_dir()
CHROMIUM = booklib.chromium()
CONTENT_W = 649.7
AVAIL_H = 958.0


def measure_blocks(blocks, css):
    css_path = os.path.join(BOOK, "book_full.css")
    open(css_path, "w").write(css + "\n.mwrap{display:flow-root;width:%.1fpx;}\n" % CONTENT_W)
    parts = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
             '<link rel="stylesheet" href="file://%s">' % css_path, '</head><body>']
    for i, b in enumerate(blocks):
        parts.append('<div class="mwrap" data-i="%d">%s</div>' % (i, b))
    parts.append('<script>window.addEventListener("load",function(){var a=[];'
                 'document.querySelectorAll(".mwrap").forEach(function(w){a.push(w.getBoundingClientRect().height);});'
                 'document.documentElement.innerHTML="<body><pre id=\\"out\\">"+JSON.stringify(a)+"</pre></body>";});</script>'
                 '</body></html>')
    open(os.path.join(BOOK, "measure.html"), "w").write("".join(parts))
    r = subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--virtual-time-budget=12000", "--dump-dom",
                        "file://" + os.path.join(BOOK, "measure.html")],
                       capture_output=True, text=True, timeout=150)
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    if not m:
        raise RuntimeError("measurement failed: " + r.stdout[:300])
    return json.loads(html.unescape(m.group(1)))


def is_heading(b):
    s = b.lstrip()
    return s.startswith('<h2') or s.startswith('<h3') or 'chapter-open' in s[:40]


def pack(blocks, heights, avail=AVAIL_H):
    pages, cur, curh = [], [], 0.0
    for blk, h in zip(blocks, heights):
        if cur and curh + h > avail:
            pages.append(cur); cur, curh = [], 0.0
        cur.append(blk); curh += h
    if cur:
        pages.append(cur)
    ch = True
    while ch:
        ch = False
        for i in range(len(pages) - 1):
            if pages[i] and is_heading(pages[i][-1]):
                pages[i + 1].insert(0, pages[i].pop()); ch = True
    return [p for p in pages if p]


def build(modname, outname):
    mod = booklib.load_module(modname)
    meta = mod.META
    lang = meta.get("lang", "en")
    kit = booklib.load_kit(lang)
    figs = booklib.figures(mod)
    specials = kit.build_specials(meta)
    back = kit.build_back(meta)

    ref_head = lambda h, k: ('<div class="chapter-open"><span class="chap-num">Reference</span>'
                             '<h1>%s</h1></div>' % h)
    FLOWS = [mod.INTRO] + list(mod.CHAPTERS) + [
        mod.CLOSING,
        {"key": "glossary", "title": "Glossary", "kind": "flow",
         "blocks": [ref_head("Glossary", "glossary")]
         + ['<div class="entry"><span class="term">%s.</span> %s</div>' % (t, d)
            for t, d in mod.GLOSSARY]},
        {"key": "index", "title": "Index", "kind": "flow",
         "blocks": [ref_head("Index", "index"), "__INDEX__"]},
        {"key": "bibliography", "title": "Bibliography", "kind": "flow",
         "blocks": [ref_head("Bibliography", "bibliography")]
         + ['<div class="ref">%s</div>' % r for r in mod.BIBLIOGRAPHY]},
        mod.POEM,
    ]

    sec_blocks = {s["key"]: [booklib.sub_figs(b, figs) for b in s["blocks"]] for s in FLOWS}
    all_blocks = []
    for s in FLOWS:
        for b in sec_blocks[s["key"]]:
            all_blocks.append('<div class="idx" id="idxbox">placeholder</div>' if b == "__INDEX__" else b)
    C = _css(themes.pick(meta))
    heights = measure_blocks(all_blocks, C)

    hi = 0; pages_by_sec = {}; order = []
    for s in FLOWS:
        k = s["key"]; n = len(sec_blocks[k]); hh = heights[hi:hi + n]; hi += n
        pages_by_sec[k] = pack(sec_blocks[k], hh); order.append(k)

    front = ["cover", "title", "copyright", "dedication", "about", "foreword"]
    main_order = [k for k in order if k != "poem"]
    pageno = len(front) + 1
    toc_page = pageno; pageno += 1
    start_page = {}
    for k in main_order:
        start_page[k] = pageno; pageno += len(pages_by_sec[k])
    pageno += 2  # back cover + series page
    start_page["poem"] = pageno
    pageno += len(pages_by_sec["poem"])
    total = pageno - 1

    titles = {s["key"]: s["title"] for s in FLOWS}
    toc_order = main_order + ["poem"]
    toc_lis = "".join('<li><span class="t">%s</span><span class="dots"></span>'
                      '<span class="pg">%s</span></li>' % (titles[k], start_page[k]) for k in toc_order)
    toc_html = ('<div class="page-content"><div class="toc"><h1>Contents</h1>'
                '<ul class="toc-list">%s</ul></div></div>' % toc_lis)

    def build_idx(page_texts, page_ranges):
        entries = []
        for term, keys in mod.INDEX_TERMS:
            key = term.split(',')[0].strip().lower()
            pgs = []
            for k in keys:
                if k not in page_ranges:
                    continue
                lo, hi = page_ranges[k]
                hit = None
                for p in range(lo, hi + 1):
                    if key and key in page_texts.get(p, ""):
                        hit = p; break
                pgs.append(hit if hit else lo)
            entries.append((term, sorted(set(pgs))))
        entries.sort(key=lambda x: x[0].lower())
        letters = {}
        for term, pgs in entries:
            letters.setdefault(term[0].upper(), []).append((term, pgs))
        ih = ['<div class="idx">']
        for L in sorted(letters):
            ih.append('<div class="letter">%s</div>' % L)
            for term, pgs in letters[L]:
                ih.append('<div class="item">%s, %s</div>' % (term, ", ".join(map(str, pgs))))
        ih.append('</div>')
        return "".join(ih)

    _wm_name = (meta.get("author") or "Author").upper()

    def sheet(inner, cls="", foot=None, watermark=True):
        f = ""
        if watermark:
            f = ('<div class="page-foot"><span>%s</span><span class="rule"></span>'
                 '<span class="wm">%s</span><span class="pg">{PG}</span></div>'
                 % (foot or "", _wm_name))
        return '<section class="sheet-a4 %s">%s%s</section>' % (cls, inner, f)

    sheets = [sheet(specials["cover"], cls="cover", watermark=False),
              sheet(specials["title"], cls="title", foot=""),
              sheet(specials["copyright"], foot=""), sheet(specials["dedication"], foot=""),
              sheet(specials["about"], foot=""), sheet(specials["foreword"], foot=""),
              sheet(toc_html, cls="toc-page", foot="")]
    for k in main_order:
        for pg in pages_by_sec[k]:
            inner = '<div class="page-content">' + "".join(pg) + '</div>'
            if k == "index":
                inner = inner.replace("__INDEX__", "<!IDX!>")
            sheets.append(sheet(inner, foot=titles[k]))
    sheets += [sheet(back["backcover"], cls="backcover", watermark=False),
               sheet(back["series"], cls="series-page", foot="")]
    for pg in pages_by_sec["poem"]:
        sheets.append(sheet('<div class="page-content">' + "".join(pg) + '</div>', foot=titles["poem"]))

    def _sheet_text(sec):
        t = re.sub(r'<[^>]+>', ' ', sec); t = re.sub(r'&[a-z]+;', ' ', t)
        return re.sub(r'\s+', ' ', t).lower()
    page_texts = {i + 1: _sheet_text(s) for i, s in enumerate(sheets)}
    page_ranges = {}
    for k in main_order:
        if k in ("index", "bibliography"):
            continue
        page_ranges[k] = (start_page[k], start_page[k] + len(pages_by_sec[k]) - 1)
    idx_block = build_idx(page_texts, page_ranges)

    for i in range(len(sheets)):
        sheets[i] = sheets[i].replace("{PG}", str(i + 1))

    body = booklib.inline_images("".join(sheets).replace("<!IDX!>", idx_block))
    doc = ('<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width, initial-scale=1">'
           '<title>%s</title>'
           '<style>%s</style></head><body><div class="book">%s</div></body></html>'
           % (lang, meta["title"], C, body))
    open(os.path.join(BOOK, outname), "w").write(doc)
    print(json.dumps({"book": meta["title"], "lang": lang, "total_pages": total,
                      "toc_page": toc_page, "start_page": start_page,
                      "flow_pages": {k: len(pages_by_sec[k]) for k in order},
                      "figures": len(figs), "html_bytes": len(doc)}, indent=1))


def _css(theme=None):
    return (open(os.path.join(BOOK, "fonts/fonts.css")).read() + "\n"
            + open(os.path.join(BOOK, "book.css")).read() + "\n"
            + themes.css_vars(theme or themes.DEFAULT))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    CSS = _css()
    build(sys.argv[1], sys.argv[2])
