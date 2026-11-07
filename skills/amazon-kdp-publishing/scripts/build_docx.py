# -*- coding: utf-8 -*-
"""Build the editable DOCX master: trim size, mirrored margins, live TOC field.

The contents is a Word `TOC` field, not a typed list. Word rebuilds it from the
Heading styles, so the page numbers stay correct after the author edits — which
is the whole reason to ship a DOCX alongside the fixed PDF.

`w:updateFields` is set, so Word offers to refresh the field when the file is
opened.
"""

from __future__ import annotations
import importlib, os, re, sys, html as _html

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kdp_specs as S

BODY_FONT = "Georgia"       # on every Windows and Mac; will not silently substitute
INK = RGBColor(0x1b, 0x1b, 0x1b)
ACCENT = RGBColor(0x3a, 0x3a, 0x3a)
FAINT = RGBColor(0x6a, 0x6a, 0x6a)


def strip_tags(s):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def add_toc_field(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    begin = OxmlElement('w:fldChar'); begin.set(qn('w:fldCharType'), 'begin')
    begin.set(qn('w:dirty'), 'true'); r._r.append(begin)
    instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve')
    instr.text = ' TOC \\o "1-2" \\h \\z \\u '; r._r.append(instr)
    sep = OxmlElement('w:fldChar'); sep.set(qn('w:fldCharType'), 'separate'); r._r.append(sep)
    t = OxmlElement('w:t')
    t.text = "Contents is a Word field. Right-click and choose “Update Field” to build it."
    r._r.append(t)
    end = OxmlElement('w:fldChar'); end.set(qn('w:fldCharType'), 'end'); r._r.append(end)


def update_fields_on_open(doc):
    el = OxmlElement('w:updateFields'); el.set(qn('w:val'), 'true')
    doc.settings.element.append(el)


def mirror_margins(doc):
    doc.settings.element.append(OxmlElement('w:mirrorMargins'))


def para(doc, text, align=None, italic=False, color=None, size=None, bold=False, after=None):
    if not text:
        return
    p = doc.add_paragraph(); r = p.add_run(text)
    if italic: r.italic = True
    if bold: r.bold = True
    if color is not None: r.font.color.rgb = color
    if size is not None: r.font.size = Pt(size)
    if align is not None: p.alignment = align
    if after is not None: p.paragraph_format.space_after = Pt(after)
    return p


def box(doc, label, paras, fill="F2F2F2"):
    t = doc.add_table(rows=1, cols=1); c = t.cell(0, 0)
    shade(c, fill); c.paragraphs[0].text = ""
    if label:
        r = c.paragraphs[0].add_run(label); r.bold = True; r.font.size = Pt(7.5)
    for x in paras:
        p = c.add_paragraph(x); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(2)
    doc.add_paragraph()


def data_table(doc, block):
    head = [strip_tags(c) for c in re.findall(r'<th[^>]*>(.*?)</th>', block, re.S)]
    rows = []
    for tr in re.findall(r'<tr>(.*?)</tr>', block, re.S):
        tds = [strip_tags(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
        if tds:
            rows.append(tds)
    n = len(head) if head else (len(rows[0]) if rows else 0)
    if not n:
        return
    t = doc.add_table(rows=(1 if head else 0) + len(rows), cols=n); t.style = 'Table Grid'
    if head:
        for j, h in enumerate(head):
            c = t.cell(0, j); shade(c, "3A3A3A"); c.paragraphs[0].text = ""
            r = c.paragraphs[0].add_run(h); r.bold = True
            r.font.color.rgb = RGBColor(0xff, 0xff, 0xff); r.font.size = Pt(7.5)
    off = 1 if head else 0
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i + off, j); c.paragraphs[0].text = ""
            c.paragraphs[0].add_run(val).font.size = Pt(8)
            if i % 2 == 1:
                shade(c, "F4F4F4")
    doc.add_paragraph()


def emit(doc, blocks, motif_dir=None):
    for b in blocks:
        bs = b.strip()
        if bs.startswith('<figure'):
            n = re.search(r'fig-n">(.*?)</span>', b, re.S)
            if motif_dir and n:
                key = re.sub(r'[^a-z0-9]+', '-', n.group(1).lower()).strip("-")
                png = os.path.join(motif_dir, key + ".png")
                if os.path.exists(png):
                    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p.add_run().add_picture(png, width=Cm(1.0))
            if n:
                para(doc, strip_tags(n.group(1)), align=WD_ALIGN_PARAGRAPH.CENTER,
                     italic=True, color=FAINT, size=7.5, after=4)
            continue
        if bs.startswith('<table'):
            data_table(doc, b); continue
        if bs.startswith('<div class="chapter-open"'):
            m = re.search(r'<h1>(.*?)</h1>', b, re.S)
            if m:
                doc.add_heading(strip_tags(m.group(1)), level=1)
            continue
        if bs.startswith('<h2'):
            doc.add_heading(strip_tags(b), level=2); continue
        if bs.startswith('<h3'):
            doc.add_heading(strip_tags(b), level=3); continue
        if bs.startswith('<div class="vignette"') or bs.startswith('<div class="callout"'):
            lbl = re.search(r'class="(?:vlabel|clabel)">(.*?)</div>', b, re.S)
            box(doc, strip_tags(lbl.group(1)) if lbl else "",
                [strip_tags(x) for x in re.findall(r'<p>(.*?)</p>', b, re.S)])
            continue
        para(doc, strip_tags(b), align=WD_ALIGN_PARAGRAPH.JUSTIFY)


def build(modname, out_docx, trim, gutter, outside, top, bottom, motif_dir=None, title_meta=None):
    B = importlib.import_module(modname)
    M = B.META
    doc = Document()

    st = doc.styles["Normal"]; st.font.name = BODY_FONT; st.font.size = Pt(10.5)
    st.font.color.rgb = INK
    rf = st.element.get_or_add_rPr().get_or_add_rFonts()
    for a in ('ascii', 'hAnsi', 'cs'):
        rf.set(qn('w:' + a), BODY_FONT)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.line_spacing = 1.12
    for h, sz in (("Heading 1", 18), ("Heading 2", 12), ("Heading 3", 10.5)):
        s = doc.styles[h]; s.font.name = BODY_FONT; s.font.size = Pt(sz)
        s.font.color.rgb = ACCENT; s.font.bold = True

    update_fields_on_open(doc); mirror_margins(doc)
    sec = doc.sections[0]
    sec.page_width = Cm(trim[0] * 2.54); sec.page_height = Cm(trim[1] * 2.54)
    sec.left_margin = Cm(gutter * 2.54); sec.right_margin = Cm(outside * 2.54)
    sec.top_margin = Cm(top * 2.54); sec.bottom_margin = Cm(bottom * 2.54)

    # front matter
    para(doc, M["title"], align=WD_ALIGN_PARAGRAPH.CENTER, size=26, bold=True)
    para(doc, M.get("subtitle", ""), align=WD_ALIGN_PARAGRAPH.CENTER, italic=True,
         size=13, color=FAINT)
    para(doc, "", after=18)
    para(doc, M.get("imprint", ""), align=WD_ALIGN_PARAGRAPH.CENTER, size=9, color=FAINT)
    doc.add_page_break()
    if M.get("dedication"):
        para(doc, strip_tags(M["dedication"]), align=WD_ALIGN_PARAGRAPH.CENTER,
             italic=True, size=11)
        doc.add_page_break()

    doc.add_heading("Contents", level=1)
    para(doc, "This contents is a Word field and rebuilds itself from the chapter headings.",
         italic=True, size=9, color=FAINT)
    add_toc_field(doc)
    doc.add_page_break()

    emit(doc, B.INTRO["blocks"], motif_dir)
    for ch in B.CHAPTERS:
        doc.add_page_break(); emit(doc, ch["blocks"], motif_dir)
    doc.add_page_break(); emit(doc, B.CLOSING["blocks"], motif_dir)

    doc.add_page_break(); doc.add_heading("Glossary", level=1)
    for t, d in B.GLOSSARY:
        para(doc, f"{t}. {d}", align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    doc.add_page_break(); doc.add_heading("Index", level=1)
    para(doc, "Page numbers appear in the printed edition; this file reflows, so the index "
              "lists terms only.", italic=True, size=9, color=FAINT)
    for t, _ in B.INDEX_TERMS:
        para(doc, t, size=9.5)
    doc.add_page_break(); doc.add_heading("Bibliography", level=1)
    for r in B.BIBLIOGRAPHY:
        para(doc, strip_tags(r))
    doc.add_page_break(); doc.add_heading(B.POEM["title"], level=1)
    for b in B.POEM["blocks"]:
        for ln in re.findall(r'<div class="line">(.*?)</div>', b, re.S):
            para(doc, strip_tags(ln), align=WD_ALIGN_PARAGRAPH.CENTER, italic=True)

    doc.save(out_docx)
    return out_docx
