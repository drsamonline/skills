# -*- coding: utf-8 -*-
"""Designed DOCX for the ornamental pack.

Full-bleed rasterised cover, maroon headings, drop-cap leads, rune-divider
images, glossary/index, and a small boxed author-name watermark in the page
footer that repeats on every page. DOCX reflows, so pagination differs from the
fixed A4 HTML — stated to the user. Fonts: Georgia (universally available) since
Cinzel/EB Garamond are not installed for Word.
"""
import os, sys, re, html as _html, subprocess, importlib
import themes
BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
sys.path.insert(0, BOOK)
import ornaments, bookkit_ornamental as kit
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_ROW_HEIGHT_RULE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement, parse_xml

CH = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")
MAROON = RGBColor(0x6e, 0x1f, 0x2a)
MAROON_D = RGBColor(0x4c, 0x10, 0x19)
INK = RGBColor(0x24, 0x1c, 0x14)
GOLD = RGBColor(0xb8, 0x86, 0x2b)
FONT = "Georgia"


def css(theme=None):
    return (open(os.path.join(BOOK, "fonts/fonts.css")).read() + "\n"
            + open(os.path.join(BOOK, "book.css")).read() + "\n"
            + themes.css_vars(theme or themes.DEFAULT))


def shot(html, out, w, h, bg="FFFBF7F0"):
    tmp = os.path.join(BOOK, "_shot.html"); open(tmp, "w").write(html)
    subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={out}", f"--window-size={w},{h}", f"--default-background-color={bg}",
                    "--virtual-time-budget=8000", "file://" + tmp], capture_output=True, timeout=120)


def make_images(meta):
    C = css(themes.pick(meta))
    cover = ('<section class="sheet-a4 cover no-watermark">' + ornaments.corner_frame()
             + kit.cover(meta) + '</section>')
    shot('<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + C + '</style></head>'
         '<body style="margin:0">' + cover + '</body></html>',
         os.path.join(BOOK, "docx_cover.png"), 794, 1123)
    div = ornaments.rune_divider()
    shot('<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + C + '</style></head>'
         '<body style="margin:0;background:#ffffff"><div style="padding:6px 0">' + div + '</div></body></html>',
         os.path.join(BOOK, "docx_divider.png"), 720, 70, bg="FFFFFFFF")
    print("images:", os.path.getsize(os.path.join(BOOK, "docx_cover.png")),
          os.path.getsize(os.path.join(BOOK, "docx_divider.png")))


def _box_borders(table, color):
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "6")
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), color)
        borders.append(e)
    table._tbl.tblPr.append(borders)


def add_footer(section, author):
    """The watermark is a small boxed author name in the footer (plus the page
    number) — not a large background mark in the page header."""
    from docx.enum.table import WD_TABLE_ALIGNMENT
    f = section.footer; f.is_linked_to_previous = False
    p = f.paragraphs[0]; p.text = ""; p.alignment = AL.CENTER
    t = f.add_table(rows=1, cols=1, width=Cm(4.8))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0); cell.text = ""
    cp = cell.paragraphs[0]; cp.alignment = AL.CENTER
    r = cp.add_run(author.upper())
    r.font.name = FONT; r.font.size = Pt(7); r.font.color.rgb = MAROON
    _box_borders(t, "b38b4d")
    p2 = f.add_paragraph(); p2.alignment = AL.CENTER
    rr = p2.add_run(); rr.font.size = Pt(9); rr.font.name = FONT; rr.font.color.rgb = GOLD
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
    rr._r.append(fld)


def parse_inline(s):
    toks, i = [], 0
    b = it = False
    while i < len(s):
        if s.startswith("<em>", i): it = True; i += 4; continue
        if s.startswith("</em>", i): it = False; i += 5; continue
        if s.startswith("<strong>", i): b = True; i += 8; continue
        if s.startswith("</strong>", i): b = False; i += 9; continue
        m = re.match(r'<span class="dropcap">(.*?)</span>', s[i:], re.S)
        if m:
            toks.append((_html.unescape(m.group(1)), b, it, True)); i += m.end(); continue
        if s[i] == "<":
            i = s.find(">", i) + 1; continue
        j = s.find("<", i)
        if j == -1: j = len(s)
        toks.append((_html.unescape(s[i:j]), b, it, False)); i = j
    return toks


def add_para(doc, inner, lead=False, align=AL.JUSTIFY, size=11, color=None, after=6, first_indent=True):
    p = doc.add_paragraph(); p.alignment = align
    pf = p.paragraph_format; pf.space_after = Pt(after); pf.line_spacing = 1.18
    for text, b, i, dc in parse_inline(inner):
        if not text:
            continue
        r = p.add_run(text); r.bold = b; r.italic = i; r.font.name = FONT
        r.font.size = Pt(size); r.font.color.rgb = color or INK
        if dc:
            r.font.size = Pt(30); r.font.color.rgb = MAROON; r.bold = False
    return p


def styled(doc, text, size, color, align=AL.CENTER, bold=False, italic=False, caps=False, after=8, space_before=0):
    p = doc.add_paragraph(); p.alignment = align
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(space_before)
    r = p.add_run(text.upper() if caps else text)
    r.bold = bold; r.italic = italic; r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = FONT
    return p


def add_divider(doc):
    p = doc.add_paragraph(); p.alignment = AL.CENTER
    p.paragraph_format.space_after = Pt(4); p.paragraph_format.space_before = Pt(4)
    p.add_run().add_picture(os.path.join(BOOK, "docx_divider.png"), width=Cm(11))


def main(modname, out):
    global MAROON, MAROON_D, INK, GOLD
    mod = importlib.import_module(modname)
    meta = dict(mod.META)
    theme = themes.pick(meta)
    ornaments.set_palette(themes.resolve(theme))
    MAROON = RGBColor(*themes.rgb(theme, "maroon"))
    MAROON_D = RGBColor(*themes.rgb(theme, "maroon-deep"))
    INK = RGBColor(*themes.rgb(theme, "ink"))
    GOLD = RGBColor(*themes.rgb(theme, "gold"))
    make_images(meta)

    doc = Document()
    st = doc.styles["Normal"]; st.font.name = FONT; st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)

    # ---- cover section (full bleed) ----
    s0 = doc.sections[0]
    s0.page_width, s0.page_height = Cm(21), Cm(29.7)
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(s0, m, 0)
    cp = doc.add_paragraph(); cp.alignment = AL.CENTER
    cp.paragraph_format.space_after = Pt(0)
    cp.add_run().add_picture(os.path.join(BOOK, "docx_cover.png"), width=Cm(21), height=Cm(29.7))

    # ---- body section ----
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.left_margin = s.right_margin = Cm(2.4); s.top_margin = Cm(2.2); s.bottom_margin = Cm(2.0)
    add_footer(s, meta.get("author", "Dr. Sohil Momin"))

    # title page
    styled(doc, "", 11, INK, after=60)
    styled(doc, meta.get("title", ""), 30, MAROON, bold=False, after=6)
    styled(doc, meta.get("subtitle", ""), 15, INK, italic=True, after=24)
    styled(doc, meta.get("author", ""), 12, MAROON, caps=True, after=6)
    styled(doc, meta.get("imprint", ""), 9, GOLD, caps=True)
    doc.add_page_break()

    # copyright
    for line in [
        "%s: %s" % (meta.get("title", ""), meta.get("subtitle", "")),
        "\u00a9 %s %s. All rights reserved." % (kit.YEAR, meta.get("author", "")),
        "First edition, %s." % kit.YEAR,
        "No part of this publication may be reproduced, stored in a retrieval system, or transmitted "
        "in any form or by any means — electronic, mechanical, photocopying, recording, or otherwise — "
        "without the prior written permission of the author, except for brief quotations in a review or "
        "scholarly work.",
        "This is a work of memoir. Scenes and conversations are rendered from memory, and memory is not "
        "a court of record.",
        "Contact: %s" % kit.CONTACT,
    ]:
        add_para(doc, _html.escape(line), align=AL.LEFT, size=10)
    doc.add_page_break()

    # epigraph (mirror the kit's epigraph page)
    _epi = re.search(r"<blockquote>(.*?)</blockquote>", kit.epigraph(meta), re.S)
    _epi_txt = _html.unescape(re.sub(r"<[^>]+>", "", _epi.group(1))).strip() if _epi else meta.get("epigraph", "")
    styled(doc, "", 11, INK, after=120)
    styled(doc, "Before the Curtain", 9, GOLD, caps=True, after=16)
    styled(doc, _epi_txt, 15, INK, italic=True, after=10)
    styled(doc, "From the Epilogue", 9, GOLD, caps=True)
    doc.add_page_break()

    # contents
    styled(doc, "Contents", 20, MAROON, after=16)
    flows = [dict(mod.INTRO)] + [dict(c) for c in mod.CHAPTERS] + [dict(mod.CLOSING)]
    for sec in flows:
        lab = ("%s · %s" % (sec["kicker"], sec["title"])) if sec["kicker"] else sec["title"]
        add_para(doc, _html.escape(lab), align=AL.LEFT, size=11)
    add_para(doc, "A Glossary of Terms", align=AL.LEFT, size=11)
    add_para(doc, "Index", align=AL.LEFT, size=11)
    add_para(doc, "About the Author", align=AL.LEFT, size=11)
    doc.add_page_break()

    # body
    def emit_section(sec, first=False):
        if not first:
            doc.add_page_break()
        styled(doc, sec["kicker"].upper(), 9, GOLD, caps=True, after=4, space_before=6)
        styled(doc, sec["title"], 22, MAROON, after=6)
        add_divider(doc)
        for blk in sec["blocks"]:
            if blk.startswith('<div class="rune-divider"'):
                add_divider(doc)
            elif blk.startswith('<div class="exhibit"'):
                m = re.search(r'ex-label">(.*?)</span>', blk, re.S)
                if m:
                    styled(doc, re.sub(r"<[^>]+>", "", m.group(1)), 12, MAROON_D, align=AL.LEFT, bold=True,
                           after=4, space_before=10)
            elif blk.startswith('<p class="lead"'):
                add_para(doc, blk[blk.find(">") + 1:blk.rfind("</p>")], lead=True)
            elif blk.startswith("<p>"):
                add_para(doc, blk[3:-4])
            else:
                txt = re.sub(r"<[^>]+>", " ", blk)
                txt = re.sub(r"\s+", " ", _html.unescape(txt)).strip()
                if txt:
                    add_para(doc, _html.escape(txt))

    for i, sec in enumerate(flows):
        emit_section(sec, first=(i == 0))

    # glossary
    doc.add_page_break()
    styled(doc, "A Glossary of Terms", 22, MAROON, after=6)
    add_divider(doc)
    for t, d in mod.GLOSSARY:
        add_para(doc, "<strong>%s.</strong> %s" % (_html.escape(t), d), align=AL.LEFT, size=10.5)

    # index
    doc.add_page_break()
    styled(doc, "Index", 22, MAROON, after=6)
    add_divider(doc)
    letters = {}
    for term, keys in mod.INDEX_TERMS:
        letters.setdefault(term[0].upper(), []).append((term, keys))
    for L in sorted(letters):
        styled(doc, L, 12, MAROON, align=AL.LEFT, bold=True, after=2, space_before=6)
        for term, keys in letters[L]:
            add_para(doc, "%s — %s" % (term, ", ".join(k.replace("chapter-", "ch. ") for k in keys)),
                     align=AL.LEFT, size=10.5)

    # about
    doc.add_page_break()
    styled(doc, "About the Author", 22, MAROON, after=6)
    add_divider(doc)
    for m in re.findall(r"<p>(.*?)</p>", mod.ABOUT_HTML, re.S):
        add_para(doc, m, align=AL.LEFT)

    doc.save(os.path.join(BOOK, out))
    print("saved", out, os.path.getsize(os.path.join(BOOK, out)), "bytes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
