# -*- coding: utf-8 -*-
"""Designed DOCX for any book: full-bleed cover, styled headings/tables/boxes,
embedded figures, and a small boxed author-name watermark in the page footer
that repeats on every page.

Everything book-specific is read from the content module and its language kit:
  * figures come from the module's FIGURES map (rasterize_all.py writes them to
    <lang>_<name>.png, the filenames used here);
  * the localised labels (copyright lines, series line, section headings, the
    safety note, the About-the-Author paragraphs) come from the kit's L10N dict
    (or the module's L10N), with generic English defaults as a fallback.

Usage:
    BOOK_DIR=/path/to/project python3 make_docx_designed.py <content_module> <out.docx> [<lang>]

DOCX reflows, so its pagination will not match the fixed A4 HTML - say so.
"""
import os, sys, re, html as _html, importlib
import booklib, themes

BOOK = booklib.book_dir()
sys.path.insert(0, BOOK)
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import qn

MAROON = RGBColor(0x6e, 0x1f, 0x2a); DEEP = RGBColor(0x57, 0x17, 0x22)
GOLD = RGBColor(0xb8, 0x86, 0x2b); INK = RGBColor(0x24, 0x1c, 0x14)
CREAM = RGBColor(0xfb, 0xf3, 0xe6); CREAM2 = RGBColor(0xf0, 0xe2, 0xc8); GOLD_L = RGBColor(0xd8, 0xb4, 0x5c)

# Generic fallback labels. A book overrides any of these through its kit's L10N
# dict (or the module's L10N). {w} in "series" is filled with META["word"].
DEFAULTS = {
    "series": "", "author": "",
    "c_rights": "All rights reserved.", "c_ed": "", "c_no": "",
    "c_disc": "This book presents general information. It is not a substitute for advice from a qualified professional.",
    "c_case": "The case material in this book is illustrative and composite.",
    "contact": "", "about_h": "About the Author", "fore_h": "Foreword",
    "safety_l": "", "safety_p": "",
    "toc_h": "Contents", "gloss_h": "Glossary", "idx_h": "Index", "bib_h": "Bibliography",
    "font": "Georgia",
}

WM = ('<w:r %s><w:rPr><w:noProof/></w:rPr><w:pict>'
      '<v:shapetype id="_x0000_t136" coordsize="21600,21600" o:spt="136" adj="10800" path="m@7,l@8,m@5,21600l@6,21600e">'
      '<v:formulas><v:f eqn="sum #0 0 10800"/><v:f eqn="prod #0 2 1"/><v:f eqn="sum 21600 0 @1"/><v:f eqn="sum 0 0 @2"/>'
      '<v:f eqn="sum 21600 0 @3"/><v:f eqn="if @0 @3 0"/><v:f eqn="if @0 21600 @1"/><v:f eqn="if @0 0 @2"/>'
      '<v:f eqn="if @0 @4 21600"/><v:f eqn="mid @5 @6"/><v:f eqn="mid @8 @5"/><v:f eqn="mid @7 @8"/><v:f eqn="mid @6 @7"/>'
      '<v:f eqn="sum @6 0 @5"/></v:formulas>'
      '<v:path textpathok="t" o:connecttype="custom" o:connectlocs="@9,0;@10,10800;@11,21600;@12,10800" o:connectangles="270,180,90,0"/>'
      '<v:textpath on="t" fitshape="t"/></v:shapetype>'
      '<v:shape id="PowerPlusWaterMarkObject" o:spid="_x0000_s2049" type="#_x0000_t136" '
      'style="position:absolute;margin-left:0;margin-top:0;width:480pt;height:120pt;rotation:-32;z-index:-251658752;'
      'mso-position-horizontal:center;mso-position-horizontal-relative:margin;mso-position-vertical:center;'
      'mso-position-vertical-relative:margin" o:allowincell="f" fillcolor="#241c14" stroked="f">'
      '<v:fill opacity=".055"/><v:textpath style="font-family:\'Inter\';font-size:1pt" string="%s"/>'
      '</v:shape></w:pict></w:r>')

WM_NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
         'xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"')


def strip_tags(s):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


# Theme fills (hex, no '#'), set in main() from the chosen theme.
T = {}


def _fill(key):
    return T.get(key, "#000000").lstrip("#").upper()


def resolve_labels(kit, mod):
    g = dict(DEFAULTS)
    g.update(getattr(kit, "L10N", {}) or {})
    g.update(getattr(mod, "L10N", {}) or {})
    meta = getattr(mod, "META", {}) or {}
    if not g.get("author"):
        g["author"] = getattr(kit, "AUTHOR", "") or meta.get("author", "")
    if not g.get("contact"):
        g["contact"] = getattr(kit, "CONTACT", "")
    if "about_p" not in g:
        about = getattr(kit, "ABOUT_HTML", "")
        g["about_p"] = [strip_tags(x) for x in re.findall(r"<p>(.*?)</p>", about, re.S)] \
            or [strip_tags(x) for x in meta.get("about_paras", [])]
    return g


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:fill'), fill); tcPr.append(shd)


def add_watermark(section, author, font="Georgia"):
    """The watermark is a small boxed author name in the footer (plus the page
    number) — not a header mark."""
    from docx.enum.table import WD_TABLE_ALIGNMENT
    f = section.footer; f.is_linked_to_previous = False
    p = f.paragraphs[0]; p.text = ""; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t = f.add_table(rows=1, cols=1, width=Cm(4.8))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0); cell.text = ""
    cp = cell.paragraphs[0]; cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = cp.add_run((author or "").upper())
    r.font.name = font; r.font.size = Pt(7); r.font.color.rgb = MAROON
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement("w:" + edge); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "6")
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), "b38b4d"); borders.append(e)
    t._tbl.tblPr.append(borders)
    p2 = f.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rr = p2.add_run(); rr.font.name = font; rr.font.size = Pt(9); rr.font.color.rgb = GOLD
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE"); rr._r.append(fld)


def para(doc, text, align=None, italic=False, color=None, size=None):
    if not text: return
    p = doc.add_paragraph(); r = p.add_run(text)
    if italic: r.italic = True
    if color is not None: r.font.color.rgb = color
    if size is not None: r.font.size = Pt(size)
    if align is not None: p.alignment = align


def cover(doc, M, g):
    t = doc.add_table(rows=1, cols=1); t.autofit = False; t.columns[0].width = Cm(21)
    c = t.cell(0, 0); shade(c, _fill("maroon")); c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    tr = t.rows[0]; tr.height = Cm(29.7); tr.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    c.paragraphs[0].text = ""
    def cp(text, size, color, italic=False, bold=False, after=8):
        p = c.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(after)
        r = p.add_run(text); r.font.size = Pt(size); r.font.color.rgb = color; r.italic = italic; r.bold = bold
    if g.get("series"):
        cp(g["series"].format(w=M.get("word", "")), 11, GOLD_L, after=20)
    cp(M["title"], 40, CREAM, bold=True, after=14)
    cp(M.get("subtitle", ""), 16, CREAM2, italic=True, after=26)
    cp(g.get("author", ""), 13, RGBColor(0xf6, 0xec, 0xd8), after=6)
    cp(M.get("imprint", ""), 9, GOLD_L)


def box(doc, label, paras, fill):
    t = doc.add_table(rows=1, cols=1); c = t.cell(0, 0); shade(c, fill); c.paragraphs[0].text = ""
    if label:
        r = c.paragraphs[0].add_run(label); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = MAROON
    for x in paras:
        p = c.add_paragraph(x); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_paragraph()


def data_table(doc, block):
    head = [strip_tags(c) for c in re.findall(r'<th[^>]*>(.*?)</th>', block, re.S)]
    rows = []
    for tr in re.findall(r'<tr>(.*?)</tr>', block, re.S):
        tds = [strip_tags(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
        if tds: rows.append(tds)
    cap = re.search(r'<caption>(.*?)</caption>', block, re.S)
    if cap: para(doc, strip_tags(cap.group(1)), italic=True, color=GOLD, size=9)
    n = len(head) if head else (len(rows[0]) if rows else 0)
    t = doc.add_table(rows=(1 if head else 0) + len(rows), cols=n); t.style = 'Table Grid'
    if head:
        for j, h in enumerate(head):
            c = t.cell(0, j); shade(c, _fill("maroon")); c.paragraphs[0].text = ""
            r = c.paragraphs[0].add_run(h); r.bold = True; r.font.color.rgb = RGBColor(0xff, 0xff, 0xff); r.font.size = Pt(9)
    off = 1 if head else 0
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i + off, j); c.paragraphs[0].text = ""; c.paragraphs[0].add_run(val).font.size = Pt(9.5)
            if i % 2 == 1: shade(c, _fill("zebra"))
    doc.add_paragraph()


def emit(doc, blocks, figs):
    for b in blocks:
        bs = b.strip()
        if bs.startswith('<figure'):
            im = re.search(r'<img[^>]*\bsrc="([^"]+)"', b)
            if im:
                src = im.group(1)
                path = src if os.path.isabs(src) else os.path.join(BOOK, src)
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                try:
                    p.add_run().add_picture(path, width=Cm(16.5))
                except Exception:
                    para(doc, "[missing image: %s]" % src, align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=GOLD, size=9)
            else:
                for key, png in figs.items():
                    if key in b:
                        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.add_run().add_picture(f"{BOOK}/{png}", width=Cm(16.5))
            cap = re.search(r'<figcaption>(.*?)</figcaption>', b, re.S)
            if cap: para(doc, strip_tags(cap.group(1)), align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=GOLD, size=9)
            continue
        if bs.startswith('<table'): data_table(doc, b); continue
        if bs.startswith('<div class="chapter-open"'):
            m = re.search(r'<h1>(.*?)</h1>', b, re.S)
            if m: doc.add_heading(strip_tags(m.group(1)), level=1)
            continue
        if bs.startswith('<h2'): doc.add_heading(strip_tags(b), level=2); continue
        if bs.startswith('<h3'): doc.add_heading(strip_tags(b), level=3); continue
        if bs.startswith('<div class="vignette"') or bs.startswith('<div class="callout"'):
            lbl = re.search(r'class="(?:vlabel|clabel)">(.*?)</div>', b, re.S)
            box(doc, strip_tags(lbl.group(1)) if lbl else "", [strip_tags(x) for x in re.findall(r'<p>(.*?)</p>', b, re.S)],
                _fill("panel") if 'vignette' in bs else _fill("panel-2"))
            continue
        para(doc, strip_tags(b), align=WD_ALIGN_PARAGRAPH.JUSTIFY)


def style_doc(doc, font):
    st = doc.styles["Normal"]; st.font.name = font; st.font.size = Pt(11.5); st.font.color.rgb = INK
    rf = st.element.get_or_add_rPr().get_or_add_rFonts()
    for a in ('ascii', 'hAnsi', 'cs'): rf.set(qn('w:' + a), font)
    for h, sz in (("Heading 1", 22), ("Heading 2", 14), ("Heading 3", 12)):
        s = doc.styles[h]; s.font.name = font; s.font.size = Pt(sz); s.font.color.rgb = MAROON


def main(modname, out, lang):
    global MAROON, DEEP, GOLD, INK, CREAM, CREAM2, GOLD_L
    B = booklib.load_module(modname)
    M = B.META
    lang = lang or booklib.module_lang(B)
    theme = themes.pick(M)
    MAROON = RGBColor(*themes.rgb(theme, "maroon"))
    DEEP = RGBColor(*themes.rgb(theme, "maroon-deep"))
    GOLD = RGBColor(*themes.rgb(theme, "gold"))
    INK = RGBColor(*themes.rgb(theme, "ink"))
    CREAM = RGBColor(*themes.rgb(theme, "paper"))
    CREAM2 = RGBColor(*themes.rgb(theme, "on-dark-sub"))
    GOLD_L = RGBColor(*themes.rgb(theme, "gold-soft"))
    T.clear(); T.update(themes.resolve(theme))
    kit = booklib.load_kit(lang)
    g = resolve_labels(kit, B)
    figs = {key: booklib.fig_name(lang, key) for key in booklib.figures(B)}

    doc = Document(); style_doc(doc, g["font"])
    s0 = doc.sections[0]
    s0.page_width = Cm(21); s0.page_height = Cm(29.7)
    s0.top_margin = s0.bottom_margin = s0.left_margin = s0.right_margin = Cm(0)
    add_watermark(s0, g.get("author", ""), g["font"]); cover(doc, M, g)
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.page_width = Cm(21); s.page_height = Cm(29.7)
    s.top_margin = s.bottom_margin = Cm(2); s.left_margin = s.right_margin = Cm(2)
    add_watermark(s, g.get("author", ""), g["font"])
    para(doc, "%s: %s" % (M["title"], M.get("subtitle", "")))
    para(doc, g["c_rights"]); para(doc, g["c_ed"]); para(doc, g["c_no"]); para(doc, g["c_disc"]); para(doc, g["c_case"]); para(doc, g["contact"])
    doc.add_page_break()
    para(doc, strip_tags(M.get("dedication", "")), align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, size=14, color=DEEP)
    doc.add_page_break()
    doc.add_heading(g["about_h"], level=2)
    for x in g["about_p"]: para(doc, x, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    doc.add_page_break()
    doc.add_heading(g["fore_h"], level=2)
    for x in M.get("foreword_pre", []): para(doc, x, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    if g.get("safety_p"):
        box(doc, g.get("safety_l", ""), [g["safety_p"]], _fill("panel-2"))
    for x in M.get("foreword_post", []): para(doc, x, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    doc.add_page_break()
    doc.add_heading(g["toc_h"], level=2)
    for sec in [B.INTRO] + list(B.CHAPTERS) + [B.CLOSING]: para(doc, sec["title"])
    for t in [g["gloss_h"], g["idx_h"], g["bib_h"], B.POEM["title"]]: para(doc, t)
    doc.add_page_break()
    emit(doc, B.INTRO["blocks"], figs)
    for ch in B.CHAPTERS:
        doc.add_page_break(); emit(doc, ch["blocks"], figs)
    doc.add_page_break(); emit(doc, B.CLOSING["blocks"], figs)
    doc.add_page_break(); doc.add_heading(g["gloss_h"], level=1)
    for t, d in B.GLOSSARY: para(doc, "%s. %s" % (t, d), align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    doc.add_page_break(); doc.add_heading(g["idx_h"], level=1)
    for t, keys in B.INDEX_TERMS: para(doc, t)
    doc.add_page_break(); doc.add_heading(g["bib_h"], level=1)
    for r in B.BIBLIOGRAPHY: para(doc, strip_tags(r))
    doc.add_page_break(); doc.add_heading(B.POEM["title"], level=1)
    for b in B.POEM["blocks"]:
        for ln in re.findall(r'<div class="line">(.*?)</div>', b, re.S):
            para(doc, strip_tags(ln), align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=DEEP)
        if '<div class="stanza"' in b: doc.add_paragraph()
    doc.add_page_break(); doc.add_heading(M["title"], level=2)
    for x in M.get("back_paras", []): para(doc, strip_tags(x), align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    if g.get("series"):
        para(doc, g["series"].format(w=M.get("word", "")), color=GOLD, size=10)
    doc.save(out); print("saved", out)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    lang = sys.argv[3] if len(sys.argv) > 3 else None
    main(sys.argv[1], sys.argv[2], lang)
