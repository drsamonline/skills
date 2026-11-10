---
name: amazon-kdp-publishing
description: Produce a print-ready Amazon KDP book — interior PDF, full cover spread (paperback and case-laminate hardcover), editable DOCX with a live table of contents, metadata sheet and a pre-upload QA report — all in one zip. Use this whenever a book is headed for Amazon, KDP, self-publishing or print-on-demand, including choosing a trim size, fixing "KDP rejected my file for page count", working out spine width or cover size, making a paperback cover that wraps correctly, making a hardcover case wrap with hinges, setting gutter margins, adding bleed, preparing a manuscript for paperback or hardcover, or packaging a publication set. Trigger on KDP, Kindle Direct Publishing, paperback, hardcover, case laminate, trim size, spine width, gutter, bleed, print-ready PDF, ISBN, or "publish my book on Amazon".
metadata:
  title: "Amazon KDP publishing"
---

# Amazon KDP publishing

KDP rejects a file for arithmetic, not for taste. Almost every rejection is one
of four things: the page count is outside the range for the chosen trim, the
gutter is too narrow for the page count, the cover is the wrong size for the
spine, or something sits inside the trim/bleed/safe area. All four are
computable before upload — that is what this skill does.

**The one rule that saves the most pain: settle the trim size before you lay out
a single page.** Trim determines the page limit; the page limit determines the
gutter; the page count determines the spine; the spine determines the cover
size. Every number downstream moves if you change the trim, so changing it late
means rebuilding the interior, the cover and the DOCX together.

## The pipeline

Run it in this order. `scripts/kdp_build.py` does all of it in one command, but
understand the steps because you will debug them individually.

1. **Choose the print format** — binding, trim, ink, paper. Check the page
   budget with `kdp_specs.check_pages()`. If the manuscript does not fit, change
   density or trim *now*, not later.
2. **Build the interior** at the trim size with a mirrored gutter
   (`scripts/build_interior.py`). Verify: sheet geometry exact, no overflow, no
   content inside the margin bands.
2b. **Verify the fonts.** Print engines reject **Type 3** fonts, and a PDF can
   report every font as embedded and still be rejected. Chromium writes Type 3
   for any *variable* font and exits 0 while doing it. `kdp_build.py` now gates
   on this and reports it in the QA sheet; see `references/font-embedding.md`.
3. **Compute the cover geometry** from the final page count
   (`kdp_specs.paperback_cover()` or `kdp_specs.hardcover_cover()`).
4. **Build the cover** as one spread — back, spine, front
   (`scripts/build_cover.py`).
5. **Build the DOCX** with a live TOC field (`scripts/build_docx.py`).
6. **Write the metadata sheet** — title, subtitle, blurb, categories, keywords,
   ISBN, pricing.
7. **Run the QA gate** (`references/qa-checklist.md`) and fix every failure.
8. **Package** — one zip containing every file above plus the spec sheet.

## Deciding the print format

Read `references/kdp-specifications.md` for the full tables. The decision that
catches people out:

| Trim | Max pages, B&W white paper |
|---|---|
| 5×8 through 8×10 (incl. 5.5×8.5, 6×9, 7×10) | **828** |
| 8.25×6, 8.25×8.25 | 800 |
| A4 (8.27×11.69) | 780 |
| **8.5×11, 8.5×8.5** | **590** |
| Hardcover (any of its five trims) | **550** |

A long book that fits at 6×9 will not fit at 8.5×11. If a manuscript is rejected
for page count, the fix is usually a *smaller* trim, not a larger one — 6×9
carries 828 pages where 8.5×11 stops at 590.

Cream paper caps lower than white (776 vs 828) because it is thicker; the page
block would otherwise be too thick to bind. Groundwood is 812.

## Interior geometry

The gutter grows with page count — 0.375 in at 24–150 pages up to 0.875 in at
701–828. Set a mirrored layout: odd (recto) pages carry the gutter on the left,
even (verso) pages on the right. Top, bottom and outside stay at 0.25 in minimum
(0.375 in with bleed) at every page count.

**The circular trap:** widening the gutter narrows the text block, which
lengthens the book, which can push it into a band requiring a wider gutter
still. Always re-check the page count *after* setting the gutter, and re-run if
the band changed.

Bleed adds 0.125 in to the top, bottom and outside edges only — never the
binding edge. A 6×9 page with bleed is 6.125 × 9.25 in.

## Cover geometry

A paperback cover is one file: `bleed + back + spine + front + bleed` wide and
`bleed + trim height + bleed` tall. Spine is `pages × paper thickness`:

| Paper | Thickness per page |
|---|---|
| B&W white | 0.002252 in |
| B&W cream | 0.0025 in |
| Standard colour | 0.002252 in |
| Premium colour | 0.002347 in |

Spine text needs **79+ pages** and 0.0625 in clearance from both fold lines.

A **hardcover case wrap** is a different animal: it adds wrap, hinges and board
overhang, and KDP does not publish a spine formula for it. Read
`references/cover-geometry.md` before attempting one — the geometry is in there,
with the caveat stated plainly.

## The deliverables

`scripts/kdp_build.py` writes one zip containing:

```
<Book>_KDP/
  01_Interior_<trim>_<paper>.pdf        print interior, grayscale for B&W
  02_Interior_<trim>_<paper>_colour.pdf reading copy
  03_Cover_<binding>_<trim>.pdf         one spread: back + spine + front
  04_Manuscript_<trim>.docx             editable, live TOC field
  05_KDP_Metadata.md                    title, blurb, categories, keywords, ISBN, pricing
  06_KDP_Specification.md               every measured number, and why
  07_QA_Report.md                       the gate, pass/fail per check
  source/                               the HTML master, for reprints
```

Ship all of it. The spec sheet is what lets the author or a future run
reproduce the book exactly; the QA report is what stops a file being uploaded
that will bounce.

## Fonts — the silent rejection

A file can pass every geometric check and still be refused for fonts. **Type 3**
glyphs are drawing procedures, not a font program, and printers reject them. It
is invisible: the PDF opens, looks correct, and fails at the printer.

Chromium produces Type 3 for any **variable** font — which is what Google Fonts
serves for most families. Installing the font is not enough; the axis must be
pinned to a static instance, the `@font-face` blocks must be removed from the
CSS, and `fc-match` must resolve your family rather than a fallback.

```bash
python3 scripts/fontaudit.py build/          # audit every PDF in a folder
python3 scripts/fontfix.py --css book.css    # pin static instances, strip @font-face
python3 scripts/printrender.py --html book.html --out book.pdf
```

Full method in `references/font-embedding.md`. The companion skill
**`print-font-safety`** automates the repair.

## Working rules

- **Measure, never estimate.** Page counts, spine widths and margins are
  arithmetic on real files. `kdp_specs.py` is the single source of truth for
  every constant; do not retype numbers into a script.
- **The cover must be rebuilt whenever the interior page count changes.** The
  spine is a function of it. A cover built for 700 pages will not wrap a
  752-page book.
- **Verify the rendered PDF, not the source HTML.** Chromium sizes a PDF from
  the `@page` rule; without one it silently falls back to Letter or A4. Read
  `pdfinfo` and confirm the page size in points (6×9 in = 432 × 648 pt).
- **Grayscale interiors for B&W printing.** Convert by overriding the palette to
  greys, not with a CSS `filter: grayscale()` — the filter forces rasterisation,
  which balloons the file and kills text selection.
- **State the limitations in the deliverable.** DOCX reflows and will not match
  the PDF's pagination; that is why its contents is a field, not fixed numbers.

## References

| File | Read it when |
|---|---|
| `references/kdp-specifications.md` | choosing trim/ink/paper, checking page limits, margins, bleed |
| `references/cover-geometry.md` | building or debugging a cover, paperback or hardcover |
| `references/metadata-and-rights.md` | writing the blurb, categories, keywords, ISBN, pricing |
| `references/file-formats-and-preflight.md` | fonts, images, colour, PDF requirements |
| `references/qa-checklist.md` | before declaring the package ready |

## Scripts

| Script | What it does |
|---|---|
| `scripts/kdp_specs.py` | All KDP constants and the geometry maths. Import it; never hardcode. |
| `scripts/build_interior.py` | Paginates a block-based HTML master into a fixed-trim PDF. |
| `scripts/build_cover.py` | Builds a paperback or hardcover spread as one PDF. |
| `scripts/build_docx.py` | DOCX with a live `TOC` field and mirrored margins. |
| `scripts/kdp_build.py` | Orchestrates everything into the single zip, and gates on fonts. |
| `scripts/fontaudit.py` | Reads a PDF's fonts; exits non-zero on Type 3 or missing embedding. |
| `scripts/fontfix.py` | Pins variable fonts to static instances, installs them, strips `@font-face`. |
| `scripts/printrender.py` | HTML to PDF with the font environment, verified before it exits. |
| `scripts/inkcheck.py` | Measures where ink actually lands on the page and compares it with the trim. |
| `assets/fonts.conf` | Minimal fontconfig pointing at a font directory. |

Start with `kdp_build.py --spec book.json`. It validates the spec, refuses a
page count outside the trim's range, and tells you what to change.
