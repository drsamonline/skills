#!/usr/bin/env python3
"""Renderer toolkit for the audit report (.docx) — the plumbing, not the argument.

    from docx_kit import Report
    r = Report('Fleet audit', owner='Dr Sohil Momin', date='3 November 2026')
    r.cover(title, subtitle, stats=[('100','repositories'), ...], evidence='...')
    r.toc()
    r.h1('1. What this audit is'); r.p('...'); r.bullet('...')
    r.table(['a','b'], rows, widths=[2,3], caption='Table 1 — ...')
    r.save('report.docx')

Write the narrative yourself. This module exists so that headings, tables, callouts and page
numbers are consistent across reports and so that no one re-derives the TOC field from scratch.
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x1F, 0x33, 0x52)
ACCENT = RGBColor(0x2E, 0x5A, 0x88)
GREY = RGBColor(0x55, 0x60, 0x6E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


class Report:
    def __init__(self, title, owner='', date='', page='A4', body_pt=10.5):
        self.doc = Document()
        self.title = title
        sec = self.doc.sections[0]
        if page.upper() == 'A4':
            sec.page_width, sec.page_height = Inches(8.27), Inches(11.69)
        else:
            sec.page_width, sec.page_height = Inches(8.5), Inches(11.0)
        sec.left_margin = sec.right_margin = Inches(0.95)
        sec.top_margin = Inches(0.9)
        sec.bottom_margin = Inches(0.85)

        st = self.doc.styles['Normal']
        st.font.name = 'Calibri'
        st.font.size = Pt(body_pt)
        st.paragraph_format.space_after = Pt(7)
        st.paragraph_format.line_spacing = 1.16
        st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')

        for name, size, colour, before, after in [
                ('Heading 1', 20, NAVY, 0, 10),
                ('Heading 2', 14, ACCENT, 18, 6),
                ('Heading 3', 11.5, NAVY, 12, 4)]:
            s = self.doc.styles[name]
            s.font.name = 'Calibri'
            s.font.size = Pt(size)
            s.font.bold = True
            s.font.color.rgb = colour
            s.paragraph_format.space_before = Pt(before)
            s.paragraph_format.space_after = Pt(after)
            s.paragraph_format.keep_with_next = True
        self.owner, self.date = owner, date

    # ---------------------------------------------------------------- text
    def p(self, text='', size=None, bold=False, italic=False, colour=None, align=None,
          before=0, after=7):
        par = self.doc.add_paragraph()
        r = par.add_run(text)
        r.font.size = Pt(size or 10.5)
        r.bold, r.italic = bold, italic
        if colour is not None:
            r.font.color.rgb = colour
        if align is not None:
            par.alignment = align
        par.paragraph_format.space_before = Pt(before)
        par.paragraph_format.space_after = Pt(after)
        return par

    def rich(self, parts, size=10.5, after=7, before=0):
        """parts: [(text, bold, italic), ...] — use for '**claim** then the evidence' sentences."""
        par = self.doc.add_paragraph()
        for t, b, i in parts:
            r = par.add_run(t)
            r.font.size = Pt(size)
            r.bold, r.italic = b, i
        par.paragraph_format.space_after = Pt(after)
        par.paragraph_format.space_before = Pt(before)
        return par

    def bullet(self, text, size=10.5, level=0):
        par = self.doc.add_paragraph(style='List Bullet' if level == 0 else 'List Bullet 2')
        r = par.add_run(text)
        r.font.size = Pt(size)
        par.paragraph_format.space_after = Pt(3)
        return par

    def h1(self, text):
        self.doc.add_heading(text, 1)

    def h2(self, text):
        self.doc.add_heading(text, 2)

    def h3(self, text):
        self.doc.add_heading(text, 3)

    def pagebreak(self):
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def rule(self, before=6, after=10):
        par = self.doc.add_paragraph()
        par.paragraph_format.space_before = Pt(before)
        par.paragraph_format.space_after = Pt(after)
        pPr = par._p.get_or_add_pPr()
        b = OxmlElement('w:pBdr')
        bot = OxmlElement('w:bottom')
        bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '6')
        bot.set(qn('w:space'), '1'); bot.set(qn('w:color'), 'C9D3E0')
        b.append(bot); pPr.append(b)

    # ---------------------------------------------------------------- tables
    @staticmethod
    def _shade(cell, hexcol):
        tcPr = cell._tc.get_or_add_tcPr()
        sh = OxmlElement('w:shd')
        sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexcol)
        tcPr.append(sh)

    @staticmethod
    def _cell(cell, text, size=8.6, bold=False, colour=None):
        cell.text = ''
        par = cell.paragraphs[0]
        r = par.add_run(str(text))
        r.font.size = Pt(size); r.bold = bold
        if colour is not None:
            r.font.color.rgb = colour
        par.paragraph_format.space_after = Pt(1.5)
        par.paragraph_format.space_before = Pt(1.5)
        par.paragraph_format.line_spacing = 1.06

    def table(self, headers, rows, widths, size=8.6, caption=None, zebra=True):
        if caption:
            cp = self.doc.add_paragraph()
            cr = cp.add_run(caption)
            cr.font.size = Pt(8.8); cr.italic = True; cr.font.color.rgb = GREY
            cp.paragraph_format.space_before = Pt(8)
            cp.paragraph_format.space_after = Pt(3)
            cp.paragraph_format.keep_with_next = True
        t = self.doc.add_table(rows=1, cols=len(headers))
        t.style = 'Table Grid'
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        for i, h in enumerate(headers):
            c = t.rows[0].cells[i]
            self._cell(c, h, size=size, bold=True, colour=WHITE)
            self._shade(c, '1F3352')
        for ri, row in enumerate(rows):
            cells = t.add_row().cells
            for i, v in enumerate(row):
                self._cell(cells[i], v, size=size)
                if zebra and ri % 2 == 1:
                    self._shade(cells[i], 'F4F7FB')
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
        return t

    # ---------------------------------------------------------------- front matter
    def cover(self, title, subtitle, stats=(), evidence=''):
        par = self.doc.add_paragraph()
        par.paragraph_format.space_before = Pt(70)
        r = par.add_run(title)
        r.font.size = Pt(38); r.bold = True; r.font.color.rgb = NAVY
        par.paragraph_format.space_after = Pt(2)
        self.p(subtitle, size=13, colour=ACCENT, after=18)
        self.rule(2, 16)
        if stats:
            t = self.doc.add_table(rows=1, cols=len(stats))
            t.autofit = False
            for i, (n, l) in enumerate(stats):
                c = t.rows[0].cells[i]
                c.width = Inches(6.3 / len(stats))
                c.text = ''
                pp = c.paragraphs[0]
                rr = pp.add_run(n); rr.font.size = Pt(19); rr.bold = True; rr.font.color.rgb = NAVY
                pp.paragraph_format.space_after = Pt(0)
                p2 = c.add_paragraph()
                r2 = p2.add_run(l); r2.font.size = Pt(7.6); r2.font.color.rgb = GREY
                p2.paragraph_format.space_after = Pt(0)
            self.p('', after=24)
        self.rule(2, 14)
        if self.owner:
            self.p(f'Prepared for {self.owner}', size=10.5, bold=True, colour=NAVY, after=2)
        if self.date:
            self.p(self.date, size=9.5, colour=GREY, after=2)
        if evidence:
            self.p(evidence, size=9, italic=True, colour=GREY, after=0)
        self.pagebreak()

    def toc(self, heading='Contents'):
        self.h1(heading)
        par = self.doc.add_paragraph()
        r = par.add_run()
        fld = OxmlElement('w:fldChar'); fld.set(qn('w:fldCharType'), 'begin')
        instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve')
        instr.text = 'TOC \\o "1-2" \\h \\z \\u'
        sep = OxmlElement('w:fldChar'); sep.set(qn('w:fldCharType'), 'separate')
        txt = OxmlElement('w:t')
        txt.text = 'Right-click and choose Update Field to build the contents.'
        end = OxmlElement('w:fldChar'); end.set(qn('w:fldCharType'), 'end')
        for el in (fld, instr, sep, txt, end):
            r._r.append(el)
        self.p('', after=6)
        self.p('The contents list is a Word field: right-click it and choose Update Field, or press F9.',
               size=8.5, italic=True, colour=GREY)
        self.pagebreak()

    def footer(self, left_text=''):
        for s in self.doc.sections:
            par = s.footer.paragraphs[0]
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = par.add_run((left_text or self.title) + ' · ')
            r.font.size = Pt(8); r.font.color.rgb = GREY
            fld = OxmlElement('w:fldChar'); fld.set(qn('w:fldCharType'), 'begin')
            instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve')
            instr.text = 'PAGE'
            end = OxmlElement('w:fldChar'); end.set(qn('w:fldCharType'), 'end')
            r2 = par.add_run(); r2.font.size = Pt(8); r2.font.color.rgb = GREY
            for el in (fld, instr, end):
                r2._r.append(el)

    def save(self, path):
        self.footer()
        self.doc.save(path)
        return path
