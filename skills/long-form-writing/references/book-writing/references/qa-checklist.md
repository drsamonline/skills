# Pre-delivery QA gate

Run this against the built files at the end of Phase 5. Fix every failure and
re-check. Never deliver on a partial pass. Nothing reaches the user until this
gate passes.

## 1. Fact audit closed

- [ ] Every substantive claim in the manuscript appears in `99_AUDIT_LOG.md`
      with an exact source file.
- [ ] No claim survives without a source (unsourced claims were deleted, not
      softened).
- [ ] No "research shows", "studies say", or "science tells us" without a named
      study or author in the same sentence.
- [ ] Contested claims are attributed to whoever makes them, not asserted in the
      book's own voice.
- [ ] Folklore is flagged as folklore, with its origin stated.
- [ ] No invented studies, authors, dates, or statistics.

## 2. Deduplication closed

- [ ] `99_DEDUP_REGISTRY.md` was updated for every chapter.
- [ ] No phrase or concept repeats across chapters in a way the registry should
      have caught.
- [ ] Repeated structural sentences (chapter openers, callout leads) vary.

## 3. Voice and banned words

- [ ] The banned-word/AI-tell list is absent (canonical list: `content-rules.md`, section "Language").
- [ ] No em-dash overuse (at most about six per thousand words).
- [ ] Sentence length varies within each section (at least one short sentence and
      one long one).
- [ ] No filler sentences that can be deleted without loss.
- [ ] Concrete nouns over abstractions.

## 4. Structure and content rules

- [ ] Every chapter has: a `lead` opener, `h2` sections, at least one callout,
      at least one labelled composite case, an honest-limit section, and a short
      "your one move this chapter".
- [ ] Every composite case is labelled as illustrative.
- [ ] Honest-limit sections are present, and health-adjacent topics point to a
      qualified professional.
- [ ] The note on sources is present at the end of the bibliography.

## 5. Visuals and tables

- [ ] Every table is fully populated — no "TBD", no empty or placeholder rows.
- [ ] Every figure is an SVG embedded in the DOCX, not an external link or a
      bitmap (unless the source material is a photo).
- [ ] `verify_figures.py` passes on every content module — no figure with a fixed
      width/height, type below 14 units, a cramped canvas, or an extreme aspect
      ratio.
- [ ] Figures are large and legible at print size (640-unit canvas, `viewBox`
      only, type ≥ 14 units).
- [ ] SVGs are print-safe: single colour scheme, no low-contrast text.
- [ ] Every process, comparison, hierarchy, or classification in prose has a
      matching figure.

## 6. Layout, watermark, parity

- [ ] `verify_any.py` on each HTML master: `max sheet height: 1123`, empty
      `v-overflow pages` and `h-overflow pages`.
- [ ] The footer watermark box (small boxed author name) appears on every
      interior page — cover and back cover excepted.
- [ ] DOCX footer watermark present: `unzip -p <out.docx> word/footer1.xml | grep -c Sohil`.
- [ ] The stylesheet is byte-identical across languages (md5 of the `<style>` block).
- [ ] Every glossary and index entry is localised in every language — no English
      term left in an Indic glossary or index.
- [ ] No ISBN printed anywhere.
- [ ] The author bio uses only supplied facts and keeps the ordering rule.

## 7. Deliverable set

- [ ] The built editions (HTML master, DOCX, PDFs, combined file) and the package
      are present and current.
- [ ] `KDP_METADATA.md` is separate from the manuscript.
- [ ] `99_AUDIT_LOG.md` is delivered alongside.
- [ ] Working files (`00_*`, `01_*`, `CH{n}_*`, `99_DEDUP_REGISTRY.md`,
      `99_MANUSCRIPT.md`) are NOT surfaced.
- [ ] Known limitations are stated to the user: DOCX reflow, grayscale PDF text
      not selectable, font substitution on machines without the script fonts.

## Pagination and completeness gate (ornamental pack)

- Run `python3 measure_fill.py <a4.html>` (with `BOOK_DIR` set). **No interior
  page under ~60% full**, except the About-the-Author page and a deliberately
  short epigraph/title page.
- **No ornament-only pages**: no page carries just a scene-break. No part begins
  or ends with a scene-break ornament.
- Every part starts on a fresh page; no chapter ends with a single stray line.
- The contents page and index carry page numbers that match the fixed A4 edition.
- Grep the built HTML for unresolved placeholders (`__INDEX__`, `{PG}`,
  `__FIG_`) — expect none.
- **Completeness**: confirm every file exists before delivering — HTML master,
  mobile HTML, colour + grayscale PDFs, mobile PDF, DOCX, KDP metadata, author
  instructions, marketing kit, poster, and the zip. A missing one is a failure.

## Mobile checks (when the mobile edition is built)

- The mobile HTML opens at 360–430 px with no horizontal scroll and no clipped
  ornament (the cover garland scales to the viewport width).
- The phone-sized PDF paginates at roughly 390×844 px and no text is cut off.
- The DOCX opens without a repair prompt and its footer still carries the
  watermark (`unzip -p book.docx word/footer1.xml | grep -c "<Author>"`).

## Extra verification (any book)

These catch defects a visual skim misses; they apply to every book.

- **Figure containment.** A label can overflow its own shape invisibly — a
  circle whose third line of text is wider than the circle reads as "text near
  the middle". For every `<text>` in a figure, confirm its *bounding box* — not
  just its anchor — sits inside the smallest enclosing filled shape.
  `verify_figures.py` covers canvas and type size; check containment separately
  for shape-heavy SVGs.
- **Markup typo class.** Grep the whole corpus for `</[a-z]+ [a-z]` — a stray
  space after a closing tag (e.g. `</span onsistent`) is valid-looking but
  silently turns the rest of the sentence into a malformed attribute and deletes
  it from render.
- **Supplied-HTML overflow.** A page with `min-height` (not a fixed height) grows
  to fit, so comparing a child's `scrollHeight` to its own `clientHeight` can
  never detect a page taller than one sheet. Measure the outer page element's
  rendered height against 1123 px. (The skill's own builders pack to a fixed
  sheet, so this matters for supplied HTML manuscripts.)
- **True output page count.** Export an actual PDF and confirm `pdfinfo` matches.
  A page can pass the height check yet split in print from sub-pixel rounding —
  if so, trim a little more margin.
- **Stated facts.** Verify author names and initials (Coulter CR, not Coulter
  HL), historical timelines and institution names before shipping.
