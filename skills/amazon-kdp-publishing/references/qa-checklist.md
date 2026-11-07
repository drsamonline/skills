# Pre-upload QA gate

Run every line against the built files. Fix each failure and re-run — a partial
pass is a rejection waiting to happen. Each check names the command or the
observation that settles it, so the answer is evidence rather than opinion.

## 1. Print format decided and consistent

- [ ] Trim, binding, ink and paper chosen and written down
- [ ] Page count is inside the range for **that exact combination**
- [ ] If binding is hardcover: the trim is one of the five hardcover trims
      (5.5×8.5, 6×9, 6.14×9.21, 7×10, 8.25×11), not a paperback-only size
- [ ] If ink is standard colour: binding is paperback (hardcover has none)
- [ ] Paper type recorded, because the spine depends on it

## 2. Interior geometry

- [ ] `pdfinfo interior.pdf` reports the trim size in points, e.g. `432 x 648`
- [ ] Page count in `pdfinfo` matches the count used for the cover
- [ ] Gutter matches the band for the final page count
      (0.375 / 0.5 / 0.625 / 0.75 / 0.875 in for the five bands)
- [ ] Layout is mirrored: gutter left on recto, right on verso
- [ ] Top, bottom and outside margins each clear their minimum
- [ ] No content inside the trim variance (0.25 in clear of every cut edge)
- [ ] Headings are not orphaned at the foot of a page
- [ ] Contents page numbers match the actual pages
- [ ] Index page references resolve to real pages

## 3. Interior content integrity

- [ ] Every chapter present — count them, do not assume
- [ ] No placeholder text anywhere (`TBD`, `TODO`, `lorem`)
- [ ] Every table fully populated — no empty cells
- [ ] Every figure rendered, not a broken image box
- [ ] Front matter order is right: title, copyright, dedication, contents
- [ ] Copyright page states what is and is not claimed (especially if the source
      material is public domain)
- [ ] No ISBN printed in the interior
- [ ] Watermark: present if the author asked for one, **absent if they asked for
      it removed** — verify by rendering a page and checking the centre band

## 4. Cover

- [ ] `pdfinfo cover.pdf` reports exactly one page
- [ ] Cover width = bleed + back + spine + front + bleed for this page count
- [ ] Cover height = bleed + trim height + bleed
- [ ] Spine computed with the correct paper thickness
- [ ] Background extends into the bleed on all four edges
- [ ] Nothing critical within 0.25 in of the trim line
- [ ] Spine text present only if > 79 pages, with 0.0625 in fold clearance
- [ ] Barcode area clear: 2 × 1.2 in, lower-right of the back cover (LTR)
- [ ] Front, spine and back all carry the correct title and author
- [ ] Text on the spine reads the right way round (top-to-bottom, not mirrored)

## 5. DOCX master

- [ ] Page size set to the trim, mirror margins on
- [ ] Contents is a live `TOC` field, not typed text
      (`unzip -p file.docx word/document.xml | grep "TOC \\\\o"`)
- [ ] `w:updateFields` set so Word refreshes on open
- [ ] Headings use built-in Heading 1/2 styles
- [ ] Fonts are ones the reader will have (Georgia / Times / Arial)
- [ ] No watermark if the print edition has none

## 6. Metadata

- [ ] Title and subtitle do not repeat each other's keywords
- [ ] Blurb under 4,000 characters, no health or legal claims
- [ ] Exactly three categories, real BISAC paths
- [ ] Seven keywords, no title repeats, no competitor names
- [ ] ISBN decision recorded
- [ ] List price above the print-cost floor for this page count

## 7. Package

- [ ] One zip, containing interior, colour copy, cover, DOCX, metadata, spec and
      this QA report
- [ ] Filenames carry the title, trim and binding so two editions cannot be
      confused
- [ ] The HTML or source master is included so the book can be reprinted
- [ ] Spec sheet records the page count, spine width and paper type used
- [ ] Limitations stated to the user: DOCX reflow, greyscale rasterisation if
      used, hardcover spine being approximate

## 8. What cannot be checked here

Be honest about these rather than implying they passed:

- **The Print Previewer** is KDP's own check and is more reliable than any
  static test. It must be run before publishing.
- **A physical proof** is the only way to confirm colour, paper and binding.
- **Hardcover spine width** is not published by KDP; it is confirmed by
  generating KDP's template, not by arithmetic.
- **Screen-reader and keyboard accessibility** of a PDF needs manual testing.
