# -*- coding: utf-8 -*-
"""Reflowable eBook HTML + EPUB for *The Symphony of the Present*.
HTML keeps inline SVG (crisp in browsers). The EPUB embeds rasterised PNG
figures, because some e-readers do not render inline SVG.
"""
import os, sys, re, zipfile, uuid, glob
import booklib, themes

BOOK = booklib.book_dir()


def sub_figs(block, figs):
    for k, v in figs.items():
        if k in block:
            return block.replace(k, v)
    return block


def build_body(mod, figs):
    meta = mod.META
    lang = meta.get("lang", "en")
    kit = booklib.load_kit(lang)
    g = dict(getattr(kit, "L10N", {}) or {})

    parts = []
    parts.append('<section class="fm"><h1>%s</h1><p class="sub">%s</p><p class="by">%s</p><p class="imp">%s</p></section>'
                 % (meta["title"], meta.get("subtitle", ""), meta.get("author", ""), meta.get("imprint", "")))
    parts.append('<section class="fm"><h2>%s: %s</h2>%s</section>'
                 % (meta["title"], meta.get("subtitle", ""),
                    "".join("<p>%s</p>" % x for x in [g.get("c_rights", ""), g.get("c_ed", ""),
                                                      g.get("c_no", ""), g.get("c_disc", ""),
                                                      g.get("c_case", ""), g.get("contact", "")])))
    parts.append('<section class="fm"><h2>About the Author</h2>%s</section>'
                 % "".join("<p>%s</p>" % x for x in g.get("about_p", [])))
    fw = ['<section class="fm"><h2>%s</h2>' % g.get("fore_h", "Foreword")]
    fw.append("<h3>%s</h3>" % meta.get("foreword_head", ""))
    fw += ["<p>%s</p>" % x for x in meta.get("foreword_pre", [])]
    fw.append('<div class="callout"><div class="clabel">%s</div><p>%s</p></div>' % (g.get("safety_l", "A note"), g.get("safety_p", "")))
    fw += ["<p>%s</p>" % x for x in meta.get("foreword_post", [])]
    fw.append("</section>")
    parts.append("".join(fw))

    secs = [mod.INTRO] + list(mod.CHAPTERS) + [mod.CLOSING]
    toc = "".join("<li>%s</li>" % s["title"] for s in secs)
    toc += "".join("<li>%s</li>" % t for t in ["Glossary", "Index", "Bibliography", mod.POEM["title"]])
    parts.append('<section class="fm"><h2>Contents</h2><ul class="toc-ebook">%s</ul></section>' % toc)

    for s in secs:
        parts.append('<section class="ch">%s</section>'
                     % "".join(sub_figs(b, figs) for b in s["blocks"]))
    parts.append('<section class="ch"><h2>Glossary</h2>%s</section>'
                 % "".join('<p><strong>%s.</strong> %s</p>' % (t, d) for t, d in mod.GLOSSARY))
    parts.append('<section class="ch"><h2>Index</h2><ul>%s</ul></section>'
                 % "".join("<li>%s</li>" % t for t, _ in mod.INDEX_TERMS))
    parts.append('<section class="ch"><h2>Bibliography</h2>%s</section>'
                 % "".join('<p class="ref">%s</p>' % r for r in mod.BIBLIOGRAPHY))
    parts.append('<section class="ch">%s</section>' % "".join(sub_figs(b, figs) for b in mod.POEM["blocks"]))
    parts.append('<section class="fm back"><h2>%s</h2>%s<p class="imp">%s</p></section>'
                 % (meta["title"], "".join("<p>%s</p>" % x for x in meta.get("back_paras", [])),
                    meta.get("imprint", "")))
    return "".join(parts)


EBOOK_CSS = """
.ebook{ max-width:720px; margin:0 auto; padding:28px 22px 60px; }
.ebook section.fm{ text-align:center; margin:0 0 34px; }
.ebook section.fm h1{ font-size:40px; line-height:1.05; }
.ebook section.fm h2{ font-size:26px; }
.ebook section.fm p.sub{ font-style:italic; color:var(--ink-soft); font-size:18px; }
.ebook section.fm p.by{ font-family:var(--font-label); letter-spacing:.3em; text-transform:uppercase; color:var(--maroon); }
.ebook section.fm p.imp{ font-family:var(--font-label); letter-spacing:.3em; text-transform:uppercase; color:var(--ink-faint); font-size:11px; }
.ebook section.fm.back{ text-align:left; }
.ebook section.ch{ margin:0 0 40px; }
.ebook section.fm p{ text-align:center; }
.ebook ul.toc-ebook{ list-style:none; padding:0; }
.ebook ul.toc-ebook li{ padding:6px 0; border-bottom:1px dotted var(--rule); }
.ebook .chapter-sigil svg, .ebook .chapter-sigil img{ width:74px; height:auto; }
.ebook figure.fig img{ width:100%; height:auto; }
body{ background:var(--mobile-bg); }
"""


def css_text(theme):
    return (open(os.path.join(BOOK, "fonts/fonts.css")).read() + "\n"
            + open(os.path.join(BOOK, "book.css")).read() + "\n"
            + themes.css_vars(theme) + "\n" + EBOOK_CSS)


def main(modname, out_html, out_epub):
    mod = booklib.load_module(modname)
    meta = mod.META
    lang = meta.get("lang", "en")
    theme = themes.pick(meta)
    figs_svg = booklib.figures(mod)
    figs_png = {k: '<img src="img/%s" alt=""/>' % booklib.fig_name(lang, k) for k in figs_svg}

    # --- reflowable HTML (inline SVG) ---
    css = css_text(theme)
    html = ('<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body>'
            '<div class="ebook">%s</div></body></html>'
            % (lang, meta["title"], css, build_body(mod, figs_svg)))
    open(os.path.join(BOOK, out_html), "w").write(html)
    print("ebook html:", os.path.getsize(os.path.join(BOOK, out_html)), "bytes")

    # --- EPUB (rasterised figures) ---
    import lxml.html, lxml.etree as ET
    epub_body = build_body(mod, figs_png)
    doc = lxml.html.fromstring('<div class="ebook">%s</div>' % epub_body)
    ebook_div = doc.xpath("//div[@class='ebook']")[0]
    xbody = "".join(ET.tostring(c, method="xml", encoding="unicode") for c in ebook_div)
    xhtml = ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
             '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="%s" lang="%s">'
             '<head><meta charset="utf-8"/><title>%s</title>'
             '<link rel="stylesheet" type="text/css" href="style.css"/></head>'
             '<body><div class="ebook">%s</div></body></html>' % (lang, lang, meta["title"], xbody))
    ET.fromstring(xhtml.encode("utf-8"))

    uid = "urn:uuid:" + str(uuid.uuid4())
    manifest_imgs = "".join('<item id="i%d" href="img/%s" media-type="image/png"/>' % (i, os.path.basename(p))
                            for i, p in enumerate(sorted(glob.glob(os.path.join(BOOK, "en_*.png")))))
    opf = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           '<dc:identifier id="bookid">%s</dc:identifier><dc:title>%s</dc:title>'
           '<dc:language>%s</dc:language><dc:creator>%s</dc:creator>'
           '<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta></metadata><manifest>'
           '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
           '<item id="book" href="book.xhtml" media-type="application/xhtml+xml"/>'
           '<item id="css" href="style.css" media-type="text/css"/>%s</manifest>'
           '<spine><itemref idref="book"/></spine></package>'
           % (uid, meta["title"], lang, meta.get("author", ""), manifest_imgs))
    nav = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">'
           '<head><title>Contents</title></head><body><nav epub:type="toc" id="toc"><h1>Contents</h1><ol>'
           + "".join("<li><a href='book.xhtml'>%s</a></li>" % s["title"]
                     for s in [mod.INTRO] + list(mod.CHAPTERS) + [mod.CLOSING])
           + '</ol></nav></body></html>')
    container = ('<?xml version="1.0" encoding="utf-8"?>\n'
                 '<container version="1.0" xmlns="http://www.idpf.org/2007/opf">'
                 '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                 'media-type="application/oebps-package+xml"/></rootfiles></container>')

    with zipfile.ZipFile(os.path.join(BOOK, out_epub), "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/book.xhtml", xhtml, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", css, compress_type=zipfile.ZIP_DEFLATED)
        for p in sorted(glob.glob(os.path.join(BOOK, "en_*.png"))):
            z.write(p, "OEBPS/img/" + os.path.basename(p), compress_type=zipfile.ZIP_DEFLATED)
    print("epub:", os.path.getsize(os.path.join(BOOK, out_epub)), "bytes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
