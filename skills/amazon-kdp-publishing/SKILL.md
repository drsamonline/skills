---
name: amazon-kdp-publishing
description: Produce a print-ready Amazon KDP book — interior PDF, full cover spread for paperback or case-laminate hardcover, editable DOCX with a live table of contents, metadata sheet and a pre-upload QA report — all in one zip. Use whenever a book is headed for Amazon, KDP, self-publishing or print-on-demand, including choosing a trim size, fixing a "KDP rejected my file for page count" error, working out spine width or cover size, making a paperback cover that wraps correctly, making a hardcover case wrap with hinges, setting gutter margins, adding bleed, preparing a manuscript for paperback or hardcover, or packaging a publication set. Trigger on KDP, Kindle Direct Publishing, paperback, hardcover, case laminate, trim size, spine width, gutter, bleed, print-ready PDF, ISBN, or "publish my book on Amazon".
metadata:
  title: "Amazon KDP publishing"
---

# Amazon KDP publishing

KDP rejects a file for arithmetic, not for taste. Almost every rejection is one
of four things: the page count is outside the range for the chosen trim, the
gutter is too narrow for the page count, the cover is the wrong size for the
spine, or something sits inside the trim/bleed/safe area. All four are
computable before upload — that is what this skill does.

The one rule that saves the most pain: **settle the trim size before you lay out
a single page.** Trim determines the page limit; the page limit determines the
gutter; the page count determines the spine; the spine determines the cover
size. Every number downstream moves if you change the trim, so changing it late
means rebuilding the interior, the cover and the DOCX together.

## When to use

- A manuscript is going to Amazon KDP, or to any print-on-demand printer that
  wants a fixed-trim PDF and a cover spread.
- KDP rejected an upload and you need to know which number is wrong.
- You need a spine width, a cover size, a gutter, or a bleed allowance.
- You are producing paperback and/or case-laminate hardcover editions of the
  same book.
- You want the whole publication set — interior, cover, DOCX, metadata, QA
  report — produced in one pass instead of assembled by hand.

## Method

Run the steps in this order. `scripts/kdp_build.py` does all of them in one
command, but understand each one, because you will debug them individually.

1. **Choose the print format** — binding, trim, ink, paper. Check the page
   budget with `kdp_specs.check_pages()`. If the manuscript does not fit, change
   density or trim *now*, not later.
2. **Build the interior** at the trim size with a mirrored gutter
   (`scripts/build_interior.py`). Verify the sheet geometry is exact and nothing
   overflows.
3. **Compute the cover geometry** from the final page count
   (`kdp_specs.paperback_cover()` or `kdp_specs.hardcover_cover()`).
4. **Build the cover** as one spread — back, spine, front
   (`scripts/build_cover.py`).
5. **Build the DOCX** with a live TOC field (`scripts/build_docx.py`).
6. **Write the metadata sheet** — title, subtitle, blurb, categories, keywords,
   ISBN, pricing.
7. **Run the QA gate** (`references/qa-checklist.md`) and fix every failure.
8. **Package** — one zip with every file above plus the specification sheet.

### The page-limit table that decides everything

| Trim | Max pages, B&W white paper |
|---|---|
| 5×8 through 8×10 (incl. 5.5×8.5, 6×9, 7×10) | **828** |
| 8.25×6, 8.25×8.25 | 800 |
| A4 (8.27×11.69) | 780 |
| **8.5×11, 8.5×8.5** | **590** |
| Hardcover (any of its five trims) | **550** |

A long book that fits at 6×9 will not fit at 8.5×11. If a manuscript is rejected
for page count, the fix is usually a *smaller* trim, not a larger one. Cream
paper caps lower than white (776 vs 828) because it is thicker.

### Interior geometry

The gutter grows with page count — 0.375 in at 24–150 pages up to 0.875 in at
701–828. Use a mirrored layout: odd (recto) pages carry the gutter on the left,
even (verso) pages on the right. Top, bottom and outside stay at 0.25 in minimum
(0.375 in with bleed) at every page count.

### Cover geometry

A paperback cover is one file: `bleed + back + spine + front + bleed` wide and
`bleed + trim height + bleed` tall. Spine is `pages × paper thickness`, where
white is 0.002252 in, cream 0.0025, premium colour 0.002347. Spine text needs
79+ pages and 0.0625 in clearance from both fold lines.

A hardcover case wrap adds wrap, hinges and board overhang. KDP publishes no
spine formula for it — read `references/cover-geometry.md` before attempting one.

## Key files

| File | What it is |
|---|---|
| `scripts/kdp_specs.py` | Every KDP constant and the geometry maths. Import it; never hardcode. |
| `scripts/build_interior.py` | Paginates a block-based HTML master into a fixed-trim PDF. |
| `scripts/build_cover.py` | Builds a paperback or hardcover spread as one PDF. |
| `scripts/build_docx.py` | DOCX with a live `TOC` field and mirrored margins. |
| `scripts/kdp_build.py` | Orchestrates everything into the single zip. |
| `references/kdp-specifications.md` | Trim/page tables, margins, bleed, spine, ink and paper. |
| `references/cover-geometry.md` | Paperback and hardcover cover maths, with the caveat stated. |
| `references/metadata-and-rights.md` | Blurb, categories, keywords, ISBN, royalty. |
| `references/file-formats-and-preflight.md` | Fonts, images, colour, PDF requirements. |
| `references/qa-checklist.md` | The pre-upload gate. |
| `assets/book.css` | A default interior stylesheet so any book builds out of the box. |
| `assets/example-book.json` | A complete spec file to copy and edit. |

Start with `kdp_build.py --spec book.json`. It validates the spec, refuses a page
count outside the trim's range, and tells you what to change.

## Gotchas

These are traps we actually hit, each one silent until a file was inspected.

- **A relative `file://` URL makes Chromium write nothing and exit 0.** Always
  pass an absolute path, and treat the existence and size of the output PDF as
  the only proof the render worked.
- **The page count must be the number of sheets actually written, not an
  arithmetic projection.** Ours diverged by two, and the cover spine was cut from
  the wrong number.
- **Never use `html{filter:grayscale(1)}` for a greyscale interior.** A CSS
  filter forces rasterisation: a 700-page file goes from ~10 MB to ~250 MB,
  renders 20× slower, and loses selectable text. Override the palette variables
  to greys instead.
- **Without an `@page` rule the PDF is Letter or A4, not your trim.** Chromium
  sizes the page from the CSS. Check `pdfinfo` reports the trim in points — 6×9
  in must be `432 x 648`.
- **The gutter/page-count dependency is circular.** Widening the gutter narrows
  the text block, which lengthens the book, which can push it into a band needing
  a wider gutter. Iterate until the band stops moving.
- **The cover must be rebuilt whenever the page count changes.** A cover cut for
  a different extent will not wrap, and the spine text will sit off-centre.
- **KDP's own frontmatter parsers are line-based, not YAML.** A `>-` block scalar
  for `description` is valid YAML but reads as the literal string `>-` to a naive
  parser. Keep `description` on one line.

## Source projects

Distilled from the **Open Materia Medica** book build (`open-materia-medica`),
a 344-chapter reference volume that had to move from 8.5 × 11 (where 800 pages
exceeds the 590-page cap) to 6 × 9, then be given a wrap-around cover, an
editable DOCX and a KDP-ready package. Every constant in `kdp_specs.py` was
checked against KDP's published help pages during that build, and the hardcover
constants were validated against KDP's own worked example.
