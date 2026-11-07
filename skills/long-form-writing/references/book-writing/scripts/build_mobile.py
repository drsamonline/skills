# -*- coding: utf-8 -*-
"""Reflowable mobile/eBook builder for *Life Is a Comedy*.

One scrolling, responsive document (body.is-mobile) that adapts to any phone
or tablet width and reflows cleanly for e-readers. Same content module, same
stylesheet, same ornaments as the A4 master.
"""
import os, sys, importlib, html
import booklib, themes
BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
sys.path.insert(0, BOOK)
import ornaments, bookkit_ornamental as kit



def css(theme=None):
    return (open(os.path.join(BOOK, "fonts/fonts.css")).read() + "\n"
            + open(os.path.join(BOOK, "book.css")).read() + "\n"
            + themes.css_vars(theme or themes.DEFAULT))


def opener(sec):
    p = ['<div class="chapter-open">']
    if sec.get("num"):
        p.append(ornaments.rune_medallion(sec["num"], size=64))
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

    flows = [dict(mod.INTRO)] + [dict(c) for c in mod.CHAPTERS] + [dict(mod.CLOSING)]
    gl = {"key": "glossary", "title": "A Glossary of Terms", "kicker": "Glossary", "num": "",
          "blocks": ['<p class="lead">Words in Hindi and Urdu that appear in these pages, for readers meeting them for the first time.</p>'] +
                    ['<div class="entry"><span class="term">%s.</span> %s</div>' % (t, d) for t, d in mod.GLOSSARY]}
    ix = {"key": "index", "title": "Index", "kicker": "Index", "num": "", "blocks": ["__INDEX__"]}
    flows += [gl, ix]

    # TOC
    toc_rows = []
    for s in flows:
        label = ("%s &middot; %s" % (s["kicker"], s["title"])) if s["kicker"] and s["kicker"] not in ("Glossary", "Index") else s["title"]
        toc_rows.append('<li><a href="#%s"><span class="t">%s</span></a></li>' % (s["key"], label))
    toc = ('<section class="m-page toc-page" id="contents"><div class="page-content"><div class="toc">'
           '<h1>Contents</h1>' + ornaments.rule_flourish() +
           '<ul class="toc-list">' + "".join(toc_rows) + '</ul></div></div></section>')

    # masthead
    masthead = ('<header class="masthead"><div class="orn-marigold">%s</div>'
                '<div class="mh-title">%s</div>'
                '<div class="mh-sub">%s</div></header>'
                % (ornaments.marigold_motif(size=40), meta.get("title", ""),
                   meta.get("subtitle", "")))

    parts = []
    parts.append('<section class="m-page cover-hero" id="cover"><div class="cover">' + kit.cover(meta) + '</div></section>')
    parts.append('<section class="m-page" id="title">' + kit.title_page(meta) + '</section>')
    parts.append('<section class="m-page" id="copyright">' + kit.copyright_page(meta) + '</section>')
    parts.append('<section class="m-page" id="epigraph">' + kit.epigraph(meta) + '</section>')
    parts.append(toc)

    # index grouped by letter
    letters = {}
    for term, keys in mod.INDEX_TERMS:
        letters.setdefault(term[0].upper(), []).append((term, keys))
    ih = ['<div class="idx">']
    for L in sorted(letters):
        ih.append('<div class="letter">%s</div>' % L)
        for term, keys in letters[L]:
            ih.append('<div class="item">%s, %s</div>'
                      % (term, ", ".join(k.replace("chapter-", "ch. ") for k in keys)))
    ih.append('</div>')
    idx_html = "".join(ih)

    for s in flows:
        parts.append('<article class="m-page" id="%s">%s%s</article>'
                     % (s["key"], opener(s) if s["key"] != "index" else "",
                        "".join(s["blocks"]).replace("__INDEX__", idx_html)))

    parts.append('<section class="m-page" id="about">' + mod.ABOUT_HTML + '</section>')
    parts.append('<section class="m-page backcover-wrap" id="backcover"><div class="backcover">' + mod.BACK_HTML + '</div></section>')
    parts.append('<footer class="masthead"><div class="orn-marigold">%s</div>'
                 '<div class="mh-sub">%s</div></footer>'
                 % (ornaments.marigold_motif(size=34), meta.get("imprint", "")))

    doc = ('<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
           '<meta name="theme-color" content="%s">'
           '<title>%s</title>'
           '<style>%s</style></head><body class="is-mobile"><div class="book">%s</div></body></html>'
           % (meta.get("lang", "en"), themes.resolve(theme)["cover-2"],
              meta.get("title", ""), C, booklib.inline_images("".join(parts))))
    open(os.path.join(BOOK, outname), "w").write(doc)
    print("wrote", outname, len(doc), "bytes")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
