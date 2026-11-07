# Changelog

## 2026-10 — trimmed the per-chapter passes and the redundant builder aliases

**Changed**
- Phase 2 is now two passes, not four: **draft** (source-grounded, dedup-checked
  against `99_DEDUP_REGISTRY.md`, and written in the book's voice) followed by
  the **adversarial audit**. The separate *dedup* and *humanize* passes were
  folded into drafting — both are writing-time concerns, and keeping them as
  standalone steps only added intermediate files and hand-offs.
- Intermediate chapter files renumbered to match: `CH{n}_01_RAW.md` →
  `CH{n}_02_VERIFIED.md` → `CH{n}_03_FINAL.md` (the `_02_UNIQUE` and `_04_FINAL`
  stages are gone).
- Removed the per-language builder aliases `build_hi.py` / `build_gu.py`;
  `build_any.py` builds every language (it reads `META["lang"]`).

## 2026-10 — consolidation: merged the updated export, the drbooks notes, and the full-book prompt

**Changed**
- Merged the *Book Writing Skill Updated* export: adopted the footer-box
  watermark (docs + code), `lessons-and-gotchas.md` §9, and its changelog entry,
  while keeping this skill's newer `figlib` Phase-3 wording and the sketches
  bitmap rule that the export had dropped.
- Extended the footer-box watermark to the **Unlearning pack** too (`book.css`,
  `build_any.py`, `verify_any.py`, `make_docx_designed.py`), which the export had
  left on the old diagonal mark, so the skill's own rule now holds for both packs.
- Added `references/clinical-safety.md` — the clinical/homeopathy safety framing
  and voice from the `drbooks` notes (emergency-referral boxes, crisis-line
  verification, contested-claim reframing, the four-audience badges). It is
  scoped to **medical/clinical books only**; the general parts of those notes —
  the extra verification checks, the AI-tell heuristic, the KDP limits — were
  moved out into `qa-checklist.md`, `content-rules.md` and `workflow.md`. The
  voice rules are written generically ("label each chapter for its reader"), with
  the homeopathy four-audience set kept as the worked example.
- Added `references/full-book-prompt.md` — the one-shot full-book generation
  prompt, kept as a template.
- Cross-linked the duplicated rules (figures, themes, sketches, EPUB, watermark)
  instead of repeating them.

**Fixed**
- `lessons-and-gotchas.md` §8's watermark note now matches §9.12 (the footer box).

## 2026-10 — footer watermark, and lessons from READ. LIVE. TRANSFORM.

**Changed**
- **The watermark is now a small boxed author name in the page footer**, not a
  large diagonal background mark. `build_a4.py` writes `meta["author"]` into a
  `.page-foot .wm` span on every interior sheet; `book_ornamental.css` styles the
  box; `verify_a4.py` recolours it red and counts the pixels; `make_docx.py` uses
  a 1-cell bordered table in the footer (the header VML watermark is gone). Cover
  and back cover carry no footer. Rules updated in `SKILL.md`,
  `content-rules.md`, `qa-checklist.md`, `workflow.md` and
  `lessons-and-gotchas.md`.

**Added**
- `references/lessons-and-gotchas.md` **§9** — what the *READ. LIVE. TRANSFORM.*
  run taught: parsing a supplied HTML manuscript (not markdown) by mapping its
  classes to the ornamental blocks; the lxml `with_tail=False` trap and the
  `<strong>`-tail box-body bug; deduplicating a figure repeated 74 times;
  title-keyed part mapping when the source's dividers are mismatched; the
  "In this part" list for sparse part openers; stripping the manuscript's
  working/editorial notes into a single clean "A Note on the Text"; making the
  kit and builders meta-driven; a theme from a supplied palette; a parts-level
  Contents for a many-part book; a minimal double-rule cover; packaging an EPUB
  with no converter; and knowing what NOT to "fix" in a spell-check pass.

## 2026-10 — sketches

**Added**
- A hand-drawn figure style: `figlib.set_style("sketch")` draws every box, arrow
  and axis with a deterministic pencil wobble. It is pure geometry, so it
  rasterises cleanly for the DOCX; the type stays crisp.
- `scripts/prep_sketch.py` — cleans a scanned or photographed sketch into a
  print-ready PNG (autocrop, contrast, threshold, resize, optional theme tint).
- `references/sketches.md` — the sketch style, and how to include the author's
  own drawings and photographs.

**Changed**
- The author's own artwork is now an allowed bitmap: `booklib.sketch_block()`
  places it, the HTML builders inline it as a data URI, and the designed DOCX
  embeds the file. `figure.fig img` fills the text column.
- Fixed a stray `→` glyph in the matrix figure that rendered as a tofu box in
  fonts without it.

## 2026-10 — figures: large, legible, and built from a library

Figures used to be hand-drawn SVGs with no size discipline, so they often came
out small and faint.

**Added**
- `scripts/figlib.py` — inline-SVG diagram builders (flowchart, tree, cycle,
  timeline, matrix, comparison, bars, line) drawn on a 640-unit canvas with a
  14-unit type floor and a 1.6 stroke floor, so figures are always large and
  legible. Takes the book theme's palette.
- `scripts/verify_figures.py` — audits every figure (canvas size, viewBox, type
  size, aspect ratio) and exits non-zero on a problem.
- `references/figures.md` — the figure authoring rules, and the alternative ways
  to draw them (matplotlib charts; Graphviz if it is installed).

**Changed**
- `rasterize_all.py` rasterises at 3× via CairoSVG (`FIG_SCALE` / `FIG_WIDTH`),
  with a Chromium fallback, so DOCX figures are crisp; the designed DOCX embeds
  figures at the full text-column width (16.5 cm).
- The writing rules and the QA gate now require large, legible figures and at
  least one figure per chapter, and point at `figlib`.

## 2026-10 — colour themes

Every book used to come out in the same maroon/gold palette. Colour is now
themed, so a shelf of titles can look different.

**Added**
- `scripts/themes.py` — seven named palettes (`ember`, `sage`, `indigo`,
  `slate`, `plum`, `terracotta`, `midnight`) with a resolver that derives the
  rules, panels, surround and on-dark text from a handful of core colours.
- `references/themes.md` — the theme list and how to add one.
- A `BOOK_THEME` environment variable (or `META["theme"]`) to pick a theme.

**Changed**
- Both stylesheets route every colour through CSS custom properties, so one
  theme recolours the cover, rules, headings, tables, panels, page surround and
  watermark together, across HTML, PDF and DOCX.
- `build_any.py`, `build_a4.py`, `build_mobile.py`, `make_docx.py`,
  `make_docx_designed.py` and `poster.py` read the theme; `ornaments.page_border`
  takes its rule/accent/vine colours from the theme palette.
- `build_mobile.py` no longer hardcodes the book title, subtitle, footer or
  theme-color (it reads META); `build_a4.py` reads `CHROMIUM` from the
  environment.

## 2026-10 — the tools are now generic (any book, any language)

The per-book scripts became tools driven entirely by the content module and their
command-line arguments, so the same scripts build any book with no edits.

**Added**
- `scripts/booklib.py` — shared helpers (`BOOK_DIR`, `CHROMIUM`, module/kit
  loading, figure substitution and naming) used by every tool.
- `references/content-module.md` — the module contract every tool shares.
- `FIGURES` (inline SVGs) on the content module and `L10N` (localised DOCX
  labels) on the module or its language kit.

**Changed**
- `build_any.py` is the one generic builder: it reads `META["lang"]`, loads the
  matching kit (`bookkit_<lang>`, falling back to `bookkit`), and substitutes the
  module's `FIGURES`. `build_hi.py` / `build_gu.py` are thin aliases.
- `make_docx_designed.py` derives its figures from `FIGURES` and its labels from
  the kit's `L10N` (generic defaults as fallback); the Unlearning label text moved
  into the kits' `L10N`.
- `combine_langs.py`, `verify_combined.py`, `rasterize_all.py` and `poster.py` now
  take their inputs on the command line, with no hardcoded book or series lists.

**Fixed**
- `rasterize_all.py` and `verify_combined.py` used `sys.argv` without importing
  `sys`.
- `rasterize_all.py` appended `.png` to an already-suffixed name, writing
  `en_light.png.png` and breaking DOCX figure embedding.

**Verified** end to end on a synthetic two-language book: build, rasterise,
poster, designed DOCX, combine and verify all pass.

## 2026-10 — toolchain config and doc alignment

**Fixed**
- `pdf_export.py` rewritten to take the documented CLI arguments
  (`<src.html> <out_base> [<mobile.html> <mobile.pdf>]`). It no longer ignores
  argv in favour of a hardcoded Unlearning job list; it now writes colour and
  grayscale A4 PDFs plus an optional phone-sized PDF.
- `build_hi.py`, `build_gu.py`, `make_docx_designed.py`, `combine_langs.py`,
  `verify_combined.py`, `rasterize_all.py`, `poster.py` and `make_docx.py` now
  read `BOOK_DIR` and `CHROMIUM` instead of hardcoding paths.
- The shipped author-bio defaults in `kits/bookkit.py`, `bookkit_hi.py`,
  `bookkit_gu.py` and `make_docx_designed.py` now match the canonical ordering
  (practice and service lead, job titles last).

**Docs**
- The per-book scripts are labelled as templates, and the `CHROMIUM` / `BOOK_DIR`
  overrides are documented in SKILL.md.

## 2026-10 — parser, bio and consistency fixes

**Added**
- `scripts/parse_manuscript.py` — the manuscript → content-module parser the
  ornamental-pack docs referenced but never shipped. Splits on `## `, applies the
  scene-break / drop-cap / exhibit rules, strips the `*(Chapter N — end)*`
  markers and the leading/trailing `---`, and drops a trailing contents list.
- `99_SERIES_DEDUP_REGISTRY.md` — series-level dedup across books.

**Fixed**
- `scripts/update_bio.py` reordered the EN/HI/GU bios to obey the canonical
  ordering rule in `assets/author-bio-template.md` (practice and service lead,
  job titles last), and now reads `BOOK_DIR`.
- Front-matter page numbering disambiguated: the Unlearning pack flows from page
  8, the ornamental pack from page 6.
- `build_any.py`, `verify_any.py`, `update_bio.py` read `BOOK_DIR` instead of
  hardcoding `/scratch/work/book`; `build_any.py` is marked a per-book template.

**Docs**
- Phase 1 intake widened (audience, length, tone, languages, delivery target).
- EPUB guidance added to Phase 5 for KDP eBooks.
- `parse_manuscript.py` and `update_bio.py` documented in SKILL.md.

## 2026-10 — ornamental pack, mobile edition, and pagination rules

Learned building *Life Is a Comedy* (literary memoir, A4 + mobile).

**Added**
- The ornamental design system: `scripts/ornaments.py`,
  `scripts/assets/book_ornamental.css`, `scripts/kits/bookkit_ornamental.py`.
- Builders: `scripts/build_a4.py` (A4 master), `scripts/build_mobile.py`
  (reflowable mobile edition), `scripts/make_docx.py` (designed DOCX).
- Tools: `scripts/fetch_fonts.py`, `scripts/verify_a4.py`,
  `scripts/measure_fill.py`, `scripts/poster.py`.
- Reference: `references/lessons-and-gotchas.md` — the pagination, ornament,
  toolchain and delivery rules.

**Rules**
- Deliver the complete set every time (HTML, mobile, colour + grayscale PDFs,
  mobile PDF, DOCX, KDP metadata, author instructions, marketing kit, poster,
  zip). A subset is a failed delivery.
- Strip the leading/trailing `---` around a chapter's end marker at parse time;
  never emit an ornament-only page; balance each part across its pages so no
  chapter ends on a sparse page.
- Keep ornaments symmetric; give small ornaments a minimum stroke width.
- Measure page fill including margins (`getBoundingClientRect` excludes them).
- When the user supplies a finished manuscript, it is the source — parse, design,
  assemble and build; do not rewrite the prose.
