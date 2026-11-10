# File formats and preflight

KDP takes a PDF for print. Most rejections and most ugly print results come from
the file, not the words.

## Interior PDF

| Requirement | Value |
|---|---|
| Page size | Exactly the trim (or trim + bleed). One size for the whole file. |
| Pages | One book page per PDF page. No spreads. |
| Fonts | Embedded, and **not Type 3** — see `font-embedding.md`. Check with `pdffonts`. |
| Images | 300 DPI at final printed size; 150 DPI absolute minimum. |
| Colour | RGB is accepted and converted; supply greyscale for B&W interiors. |
| Transparency | Flattened. Live transparency can drop shadows and blends. |
| File size | Large is tolerated, but slow to process; keep under ~400 MB. |
| Security | No passwords, no permissions, no encryption. |

### Check the page size, always

The most common silent failure: an HTML-to-PDF export with no `@page` rule falls
back to Letter or A4, and the file is wrong at every page.

```bash
pdfinfo interior.pdf | grep "Page size"
```

Expected, in points (inches × 72):

| Trim | Points |
|---|---|
| 5 × 8 | 360 × 576 |
| 5.5 × 8.5 | 396 × 612 |
| 6 × 9 | **432 × 648** |
| 7 × 10 | 504 × 720 |
| 8.5 × 11 | 612 × 792 |

`612 × 792` is US Letter — if a 6 × 9 book reports that, the export is wrong.

### Greyscale done properly

For a black-and-white interior, convert by **overriding the palette to greys**
in CSS before rendering:

```css
:root{ --ink:#1c1c1c; --accent:#3a3a3a; --rule:#dcdcdc; }
table th{ background:#3a3a3a !important; }
```

Do **not** use `html{filter:grayscale(1)}`. A CSS filter forces the renderer to
rasterise the page, which:

- inflates a 700-page file from ~10 MB to ~250 MB,
- makes rendering 20× slower,
- destroys selectable text.

Verify the result: render a page and count coloured pixels. Under 0.1% is clean.

### Fonts

- Embed every face actually used, including italic and semibold.
- A webfont loaded by URL will not embed unless the renderer has fetched it
  first — embed as base64 `@font-face` if you are generating from HTML.
- Word's DOCX is not the print file. Convert from the PDF, not from the DOCX.

## Cover PDF

| Requirement | Value |
|---|---|
| Pages | Exactly one. Back, spine and front on that single page. |
| Size | From the cover geometry for this page count and paper. |
| Bleed | 0.125 in on top, bottom and outside; none on the binding edge. |
| File size | Under 650 MB converts; keep under 40 MB for print speed. |
| Fonts | Embedded. |
| Barcode | Do not draw one. KDP prints it from your ISBN. |

## DOCX (the editable master)

Not a print file — it is what the author edits.

- Page size set to the trim, **mirror margins** on.
- Contents as a real `TOC` field, not a typed list, so page numbers rebuild
  after edits. Set `w:updateFields` so Word offers to refresh on open.
- Headings must use the built-in Heading 1/2 styles or the TOC field will not
  find them.
- Avoid fonts that may not exist on the reader's machine; Word substitutes
  silently and the layout shifts. Georgia, Times New Roman and Arial are safe
  everywhere.

## Preflight before upload

```bash
# page size and count
pdfinfo interior.pdf | grep -E "Pages|Page size"

# fonts embedded?
pdffonts interior.pdf | awk 'NR>2 && $(NF-4)!="yes" {print "NOT EMBEDDED:", $1}'

# any page a different size?
pdfinfo -f 1 -l 999 interior.pdf | grep "Page.*size" | sort -u
```

- [ ] Page size matches the trim exactly
- [ ] Page count is inside the range for trim + paper
- [ ] Every font reports `emb yes`
- [ ] No page reports a different size
- [ ] Images at 300 DPI at final size
- [ ] Greyscale interior if printing B&W
- [ ] No password or permissions on the file
- [ ] Cover size computed from *this* page count

## Common failures and their real cause

| Message | Cause |
|---|---|
| Page count out of range | Trim/paper combination caps lower than you assumed (8.5 × 11 = 590). |
| Margin violation | Gutter too narrow for the page count, or content in the bleed. |
| Cover dimensions incorrect | Spine computed from a stale page count, or wrong paper thickness. |
| Font not embedded | A webfont or a system font the renderer never fetched. |
| **Type 3 font** | A *variable* font flattened by the renderer. Pin a static instance and strip `@font-face` — see `font-embedding.md`. |
| Low-resolution images | Scaled up after placement; 300 DPI at final size is the test. |
| Text cut off at the edge | Content inside the trim variance — needs 0.25 in clear. |

## The one font failure that hides

A PDF can report every font as embedded and still be rejected, because
**Type 3 counts as embedded**. Chromium writes Type 3 for any *variable* font,
and it exits 0 while doing it. Check the type column, not just the `emb` column:

```bash
pdffonts interior.pdf     # type must be CID TrueType / TrueType / Type 1
```

Three things must all be true to avoid it: the font is a static instance, the
`@font-face` blocks are gone from the CSS, and `fc-match` resolves your family
rather than a fallback. Details and the fix are in `references/font-embedding.md`.
