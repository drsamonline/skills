# -*- coding: utf-8 -*-
"""A4 builder for the ornamental pack.

Packs measured blocks into fixed A4 sheets, starts every part on a fresh
page, builds a contents page and a page-accurate index, and stamps the
ornamental page border and the footer watermark (a small boxed author name)
on every interior sheet.

Usage:
    BOOK_DIR=/path/to/project python3 build_a4.py <content_module> <out.html>
"""
import os, sys, json, re, html, subprocess, importlib
import booklib, themes
BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
sys.path.insert(0, BOOK)
import ornaments, bookkit_ornamental as kit

CHROMIUM = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")

CONTENT_W = 625.7
AVAIL_H = 966.0


def css(theme=None):
    return (open(os.path.join(BOOK, "fonts/fonts.css")).read() + "\n"
            + open(os.path.join(BOOK, "book.css")).read() + "\n"
            + themes.css_vars(theme or themes.DEFAULT))


def measure_blocks(blocks, css_text):
    css_path = os.path.join(BOOK, "book_full.css")
    open(css_path, "w").write(css_text + "\n.mwrap{display:flow-root;width:%.1fpx;}\n" % CONTENT_W)
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
                        "--hide-scrollbars", "--virtual-time-budget=15000", "--dump-dom",
                        "file://" + os.path.join(BOOK, "measure.html")],
                       capture_output=True, text=True, timeout=200)
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    if not m:
        raise RuntimeError("measurement failed: " + r.stdout[:400] + r.stderr[:400])
    return json.loads(html.unescape(m.group(1)))


def is_heading(b):
    s = b.lstrip()
    return s.startswith("<h2") or s.startswith("<h3") or "chapter-open" in s[:60]


def is_divider(b):
    return b.lstrip().startswith('<div class="rune-divider"')


def pack_pairs(pairs, avail):
    """Pack (block, height) pairs into pages of at most `avail` px."""
    pages, cur, curh = [], [], 0.0
    for blk, h in pairs:
        if cur and curh + h > avail:
            pages.append(cur); cur, curh = [], 0.0
        cur.append((blk, h)); curh += h
    if cur:
        pages.append(cur)
    ch = True
    while ch:
        ch = False
        for i in range(len(pages) - 1):
            if pages[i] and is_heading(pages[i][-1][0]):
                pages[i + 1].insert(0, pages[i].pop()); ch = True
    pages = [p for p in pages if p]
    # never emit a page that carries only an ornament (an orphaned scene-break)
    pages = [p for p in pages if not all(is_divider(b) for b, h in p)]
    return pages


def pack_section(pairs):
    """Pack one part. If the last page comes out sparse, search per-page fill
    targets so the part's blocks spread evenly and no chapter ending sits alone
    on a page."""
    naive = pack_pairs(pairs, AVAIL_H)
    if len(naive) <= 1:
        return naive
    last_fill = sum(h for _, h in naive[-1])
    if last_fill >= 0.60 * AVAIL_H:
        return naive
    total = sum(h for _, h in pairs)
    n = len(naive)
    lo = total / float(n)
    best, best_last = naive, last_fill
    steps = 16
    if os.environ.get("PACK_DEBUG"):
        print("[pack] n=%d total=%.0f lo=%.0f last_fill=%.0f" % (n, total, lo, last_fill))
    for i in range(steps + 1):
        t = lo + (AVAIL_H - lo) * i / float(steps)
        bal = pack_pairs(pairs, t)
        lf = sum(h for _, h in bal[-1]) if bal else 0
        if os.environ.get("PACK_DEBUG"):
            print("   t=%.0f -> pages=%d lastfill=%.0f" % (t, len(bal), lf))
        if 1 < len(bal) <= n and lf > best_last:
            best, best_last = bal, lf
    return best


def opener(sec):
    cls = "chapter-open" if sec.get("num") else "chapter-open part-open"
    p = ['<div class="%s">' % cls]
    if sec.get("num"):
        p.append(ornaments.rune_medallion(sec["num"]))
    if sec.get("kicker"):
        p.append('<div class="chapter-kicker">%s</div>' % sec["kicker"].upper())
    p.append("<h1>%s</h1>" % sec["title"])
    p.append(ornaments.rule_flourish())
    p.append("</div>")
    return "".join(p)


def build(modname, outname):
    mod = importlib.import_module(modname)
    meta = dict(mod.META)
    theme = themes.pick(meta)
    ornaments.set_palette(themes.resolve(theme))
    C = css(theme)

    # ---- assemble flow sections ----
    flows = [dict(mod.INTRO)] + [dict(c) for c in mod.CHAPTERS] + [dict(mod.CLOSING)]

    gl = {"key": "glossary", "title": "A Glossary of Terms", "kicker": "Glossary", "num": "",
          "blocks": ['<div class="chapter-open"><div class="chapter-kicker">GLOSSARY</div>'
                     '<h1>A Glossary of Terms</h1>' + ornaments.rule_flourish() + '</div>'] +
                    ['<div class="entry"><span class="term">%s.</span> %s</div>' % (t, d)
                     for t, d in mod.GLOSSARY]}
    ix = {"key": "index", "title": "Index", "kicker": "Index", "num": "",
          "blocks": ['<div class="chapter-open"><div class="chapter-kicker">INDEX</div>'
                     '<h1>Index</h1>' + ornaments.rule_flourish() + '</div>', "__INDEX__"]}
    flows += [gl, ix]

    # prepend opener to each section's blocks
    for s in flows:
        if s["key"] != "index":
            s["blocks"] = [opener(s)] + list(s["blocks"])
        else:
            s["blocks"] = [opener(s), "__INDEX__"]

    # ---- measure & pack ----
    all_blocks, index_pos = [], {}
    for s in flows:
        for b in s["blocks"]:
            index_pos[len(all_blocks)] = s["key"]
            all_blocks.append('<div class="idx" style="visibility:hidden">placeholder</div>'
                              if b == "__INDEX__" else b)
    heights = measure_blocks(all_blocks, C)

    hi, pages_by_sec, order = 0, {}, []
    for s in flows:
        k = s["key"]; n = len(s["blocks"]); hh = heights[hi:hi + n]; hi += n
        pgs = pack_section(list(zip(s["blocks"], hh)))
        pages_by_sec[k] = [[b for b, _h in p] for p in pgs]
        order.append(k)

    # ---- page numbering ----
    front = ["cover", "title", "copyright", "epigraph"]
    n_front = len(front)
    pageno = n_front + 1
    toc_page = pageno; pageno += 1
    start_page = {}
    for k in order:
        start_page[k] = pageno; pageno += len(pages_by_sec[k])
    # back matter sheets
    about_page = pageno; pageno += 1
    backcover_page = pageno; pageno += 1
    total = pageno - 1

    titles = {s["key"]: s["title"] for s in flows}
    kicks = {s["key"]: s["kicker"] for s in flows}

    # ---- contents (parts and front/back matter; chapters sit under their part) ----
    # Listing every chapter overflows a single fixed sheet for a many-part book,
    # so list the parts (with their chapter ranges) and the front/back matter.
    def _cnum(k):
        m = re.match(r"chapter-(\d+)$", k)
        return int(m.group(1)) if m else None
    part_range, cur = {}, None
    for k in order:
        if k.startswith("part-"):
            cur = k; part_range[k] = [None, None]
        elif _cnum(k) is not None and cur:
            n = _cnum(k)
            if part_range[cur][0] is None:
                part_range[cur][0] = n
            part_range[cur][1] = n
    toc_rows = []
    for k in order:
        if _cnum(k) is not None:
            continue
        if k.startswith("part-") and part_range.get(k, [None, None])[0]:
            a, b = part_range[k]
            label = "%s &middot; %s &mdash; Chapters %d&ndash;%d" % (kicks[k], titles[k], a, b)
        elif kicks[k] and kicks[k] not in ("Glossary", "Index"):
            label = "%s &middot; %s" % (kicks[k], titles[k])
        else:
            label = titles[k]
        toc_rows.append('<li><span class="t">%s</span><span class="dots"></span><span class="pg">%d</span></li>'
                        % (label, start_page[k]))
    toc_html = ('<div class="page-content"><div class="center-page"><div class="toc"><h1>Contents</h1>'
                + ornaments.rule_flourish() + '<ul class="toc-list">' + "".join(toc_rows)
                + '</ul></div></div></div>')

    # ---- sheets ----
    _wm_name = (meta.get("author") or "Author").upper()

    def sheet(inner, cls="", foot=None, frame=None, watermark=True):
        wm = "" if watermark else " no-watermark"
        fr = frame or ""
        f = ""
        if watermark:
            # the watermark is a small boxed author name in the footer, on every
            # interior sheet (cover and back cover carry no footer)
            f = ('<div class="page-foot"><span>%s</span><span class="rule"></span>'
                 '<span class="wm">%s</span><span class="pg">{PG}</span></div>'
                 % (foot or "", _wm_name))
        return '<section class="sheet-a4 %s%s">%s%s%s</section>' % (cls, wm, fr, inner, f)

    sheets = []
    # front matter
    sheets.append(sheet(kit.cover(meta), cls="cover", frame=ornaments.corner_frame(), watermark=False))
    sheets.append(sheet(kit.title_page(meta), cls="title", frame=ornaments.page_border()))
    sheets.append(sheet(kit.copyright_page(meta), cls="copyright", frame=ornaments.page_border()))
    sheets.append(sheet(kit.epigraph(meta), cls="epigraph-page", frame=ornaments.page_border()))
    sheets.append(sheet(toc_html, cls="toc-page", frame=ornaments.page_border()))
    # flow
    for k in order:
        for pi, pg in enumerate(pages_by_sec[k]):
            inner = '<div class="page-content">' + "".join(pg) + '</div>'
            frame = ornaments.page_border(opener=(pi == 0))
            foot = titles[k]
            sheets.append(sheet(inner, foot=foot, frame=frame))
    # back matter
    sheets.append(sheet(mod.ABOUT_HTML, cls="about-page", foot="About the Author", frame=ornaments.page_border()))
    sheets.append(sheet(mod.BACK_HTML, cls="backcover", frame=ornaments.corner_frame(), watermark=False))

    # ---- index resolution ----
    def text_of(sec_html):
        t = re.sub(r"<[^>]+>", " ", sec_html)
        t = re.sub(r"&[a-z]+;", " ", t)
        return re.sub(r"\s+", " ", t).lower()

    page_text = {i + 1: text_of(s) for i, s in enumerate(sheets)}
    page_ranges = {k: (start_page[k], start_page[k] + len(pages_by_sec[k]) - 1) for k in order}
    entries = []
    for term, keys in mod.INDEX_TERMS:
        key = term.split(",")[0].strip().lower()
        pgs = []
        for k in keys:
            if k not in page_ranges:
                continue
            lo, hi = page_ranges[k]
            hit = None
            for p in range(lo, hi + 1):
                if key and key in page_text.get(p, ""):
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
    ih.append("</div>")
    idx_block = "".join(ih)

    for i in range(len(sheets)):
        sheets[i] = sheets[i].replace("{PG}", str(i + 1))
    body = booklib.inline_images("".join(sheets).replace("__INDEX__", idx_block))

    doc = ('<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width, initial-scale=1">'
           '<title>%s</title>'
           '<style>%s</style></head><body><div class="book">%s</div></body></html>'
           % (meta.get("lang", "en"), meta.get("title", ""), C, body))
    open(os.path.join(BOOK, outname), "w").write(doc)
    print(json.dumps({"total_pages": total, "toc_page": toc_page,
                      "start_page": start_page, "about_page": about_page,
                      "flow_pages": {k: len(pages_by_sec[k]) for k in order},
                      "index_entries": len(entries), "html_bytes": len(doc)}, indent=1))


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
