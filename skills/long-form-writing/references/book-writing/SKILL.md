---
name: book-writing
description: Produce a designed, multi-language book or series end to end — source-grounded drafting with an adversarial fact-audit and a cross-book deduplication registry, then a fixed-page A4 HTML master, a designed DOCX, PDF exports, and a combined all-languages HTML with a language switcher. Use when the user wants to write, build, translate, restyle, or package a book or series in one or more languages (English, Hindi, Gujarati, and other Indic scripts), to update an existing edition or its author bio, or to publish to KDP. Runs in phases, not one micro-step at a time.
---

# Book writing and multi-language edition production

Turn source files into a finished, publishable set of files: a source-grounded
manuscript, a fixed-page HTML master, a designed DOCX, PDFs, and one combined
file carrying every language behind a switcher. This is the workflow used to
build the Unlearning Series and *A Borrowed Light* (three languages, many
editions each).

## When to use it

- Writing or assembling a book or a series, in one language or several.
- Producing editions in a non-Latin script (Devanagari, Gujarati, and similar).
- Restyling, re-exporting, or updating an edition, including its author bio.
- Packaging a title for KDP or a similar storefront.

Do not use it for a one-off PDF or a slide deck. Use the PDF, DOCX, or slides
skills for those.

## How work is executed: phases, not steps

The book is built in **five phases**. A "continue" (`c`) runs the current phase
to completion and stops only at a **phase boundary** — not after each task.

- Inside a phase, execute every task the phase lists. Do not stop between them,
  and do not narrate what comes next. No conversational filler.
- When a phase is finished, reply with exactly one line:
  `Phase N ([name]) complete. Ready for 'c'.`
- A very long phase (Manuscript, Design) may span more than one turn for a big
  book. In that case a turn covers a **coherent group** of chapters (three to
  five, or whatever fits), and reports `Phase 2: chapters 1–5 done. Ready for 'c'.`
  Prefer fewer, larger turns over many tiny ones.
- **Nothing reaches the user until Phase 5 QA passes.** Working files stay in the
  project; only the finished, corrected, publication-ready files are delivered.

The phases:

1. **Foundation** — intake; read every source file; build the blueprint, the
   manifest, the claim ledger, the author bio, and the style guide.
2. **Manuscript** — every chapter: draft → adversarial audit.
3. **Design** — every chapter: fully-populated tables, SVG figures, keywords.
4. **Assembly and back matter** — compile the manuscript; glossary, index,
   conclusion, corrections appendix, acknowledgments, bio page, poem; KDP metadata.
5. **Build, QA, delivery** — HTML master, verify, DOCX, PDFs, combined file,
   supporting files, package; run the QA gate; deliver.

## The shape of the work

Every book is built from content modules plus shared building blocks, then
rendered by a script. Nothing is hand-laid-out.

```
work/
  00_BLUEPRINT.md          outline, chapter list, word targets, per-chapter source map
  00_MANIFEST.md           the master checklist, one [ ] row per task, in order
  01_AUTHOR_BIO.md         generated once, reused everywhere
  01_STYLE_GUIDE.md        generated once, reused everywhere
  02_RESEARCH_EXTRACTS.md  hard data pulled from the source files
  99_DEDUP_REGISTRY.md     phrases/concepts already used, updated every chapter
  99_SERIES_DEDUP_REGISTRY.md  (series only) phrases/concepts used across books
  99_AUDIT_LOG.md          claim → source-file map; unsourced claims deleted here
  CH{n}_01_RAW.md          chapter, drafted (voice + dedup applied)
  CH{n}_02_VERIFIED.md     chapter, audited
  CH{n}_03_FINAL.md        chapter, designed (tables + SVG)
  CH{n}_INDEX.md           chapter keywords
  99_MANUSCRIPT.md         full compiled book, before DOCX conversion
  KDP_METADATA.md          title, blurb, categories, keywords — never merged in
  <lang>kit.py             front/back matter (cover, copyright, foreword, series page)
  content_<book>_<lang>.py META, INTRO, CHAPTERS, CLOSING, GLOSSARY, BIBLIOGRAPHY, POEM, INDEX_TERMS
  figures_<lang>*.py       figures as inline SVG
  book.css                 the ONE stylesheet, byte-identical across all languages
  fonts/fonts.css          base64-embedded fonts
  build_*.py               the paginating builder
  make_docx_designed.py    the designed DOCX generator
  combine_langs.py         merges languages into one file with a switcher
  verify_*.py              layout + watermark checks
  rasterize_all.py         SVG → PNG for DOCX embedding
  pdf_export.py            colour + grayscale PDFs, plus the mobile PDF

  -- the ornamental pack (vines, runes, borders; A4 + mobile) --
  ornaments.py             vine / rune / marigold / border / medallion SVG library
  book_ornamental.css      the ornamental + responsive stylesheet
  bookkit_ornamental.py    cover / title / copyright / epigraph templates
  parse_manuscript.py      manuscript → content module (run first; re-run after ornaments.py)
  build_a4.py              A4 master builder (ornamental, part-per-page, balanced)
  build_mobile.py          reflowable mobile / eBook builder (body.is-mobile)
  make_docx.py             designed DOCX for the ornamental pack
  fetch_fonts.py           downloads + base64-embeds the webfonts
  verify_a4.py             layout + watermark checks for build_a4
  measure_fill.py          reports the real text fill of every A4 page
  poster.py                one-page A4 launch poster (HTML -> PDF)
```

A content module exposes exactly this interface, so every builder works on any
book:

```python
META = {"num": 3, "word": "Three", "title": "...", "subtitle": "...",
        "title_html": "...", "imprint": "...", "dedication": "...",
        "foreword_head": "...", "foreword_pre": [...], "foreword_post": [...],
        "back_paras": [...]}
INTRO    = {"key": "introduction", "title": "...", "kind": "flow", "blocks": [<html strings>]}
CHAPTERS = [ {"key": "chapter-1", "title": "...", "kind": "flow", "blocks": [...]}, ... ]
CLOSING  = {...}
GLOSSARY     = [("Term", "definition"), ...]
BIBLIOGRAPHY = ["Author (Year). ...", ...]
POEM         = {"key": "poem", "title": "...", "kind": "flow", "blocks": [...]}
INDEX_TERMS  = [("Term", ["chapter-1", "chapter-4"]), ...]
FIGURES      = {"__FIG_KEY__": "<svg ...>", ...}   # optional; inline SVGs
L10N         = {"font": "...", ...}                # optional; DOCX labels
```

The module is the **single source of truth**: every builder, verifier, rasteriser
and packager reads its book-specific content from it, so the same scripts build
any book in any language. `FIGURES` holds the inline SVGs a block references as
`__FIG_KEY__` placeholders, and `L10N` (usually on the language kit) holds the
localised labels the designed DOCX needs. The full contract is in
`references/content-module.md`.

Block kinds the builders understand: `chapter-open` div, `h2`/`h3`, `p` (with
`class="lead"` for the opener), `figure.fig` with a `__FIG_KEY__` placeholder,
`table.data`, `div.callout`, `div.vignette`, and the poem's `stanza`/`line` divs.

## Design systems

Two house styles ship with this skill. Pick one per book and keep it consistent
across every format.

- **The Unlearning style** (`assets/book.css`, `build_any.py`): warm maroon/gold,
  tables, callouts, case boxes, SVG figures. For non-fiction and series work.
- **The ornamental pack** (`assets/book_ornamental.css`, `ornaments.py`,
  `build_a4.py` + `build_mobile.py` + `make_docx.py`): for literary books, memoir
  and poetry. It adds a **cover design** (full-bleed ground, a marigold-garland
  crown, vine corners, an inscriptional display face, an imprint line);
  **page-border designs** (a fine double rule on every page with edge diamonds,
  and vine-cornered borders on every part opener); **vines and runes** (a
  `rune_divider` scene-break of mirrored runes, vine sprigs and a marigold, a
  `rune_medallion` chapter number, and a rune-framed monogram); and **drop caps**
  on each part's opening paragraph. The **mobile edition** is one reflowable,
  responsive HTML (`body.is-mobile`) plus a phone-sized PDF.

The ornamental pack starts every part on a fresh page and numbers the front
matter cover · title · copyright · epigraph · contents, so flow begins at page 6.
The full pagination, ornament and toolchain rules are in
`references/lessons-and-gotchas.md` — read it before building.

### Colour themes

Both house styles draw every colour from CSS custom properties, so a book's
whole palette is set by one **theme** — cover, rules, headings, tables, panels,
the page surround and the watermark all change together, across HTML, PDF and
DOCX. Seven themes ship in `scripts/themes.py`: `ember` (the original
maroon/gold), `sage`, `indigo`, `slate`, `plum`, `terracotta` and `midnight`.
Pick one with the `BOOK_THEME` environment variable, or set `theme` on the
content module's `META` (the env var wins); the default is `ember`.

```
BOOK_THEME=sage python3 build_any.py content_book_en out.html
```

Give each book (and each book in a series) its own theme so a shelf of titles
does not read as one colour. The theme also drives the ornaments' border and
vine colours and the designed DOCX. Add a theme by adding an entry to
`THEMES` in `themes.py` — name the paper, ink, primary, deep, two accents and
the three cover stops; the rules, panels and on-dark text are derived from
them. See `references/themes.md`.

## The five phases in detail

### Phase 1 — Foundation

1. Confirm intake only if not already given: topic and title, target audience,
   rough length, tone/register, the languages wanted, and the delivery target
   (KDP eBook, print, or both). Read every uploaded `.txt`/`.md` source file in
   full; extract hard data to `02_RESEARCH_EXTRACTS.md`.
2. Build `00_BLUEPRINT.md`: outline, chapter list, word-count targets, and a
   per-chapter source-file mapping.
3. Build `00_MANIFEST.md`: the master checklist, one atomic `[ ]` row per task
   across all five phases, in execution order.
4. Generate `01_AUTHOR_BIO.md` from `assets/author-bio-template.md` — do not
   alter the ordering rule in that file, and do not invent facts.
5. Generate `01_STYLE_GUIDE.md`: structured, systematic, compliance-flavoured
   prose, with a philosophical/narrative register available for poetry and
   reflective passages.
6. Reply `Phase 1 (Foundation) complete. Ready for 'c'.`

### Phase 2 — Manuscript (per chapter: draft → adversarial audit)

- **Draft** — write from the mapped source file(s) only, in the book's voice.
  Read `99_DEDUP_REGISTRY.md` first and write around anything already logged
  (across the whole book, not just this chapter), then append this chapter's new
  phrases and concepts as you go. Apply `01_STYLE_GUIDE.md` and the
  banned-word/AI-tell list in `references/qa-checklist.md` while writing: vary
  sentence length, add one or two concrete examples, and allow small natural
  imperfections (a colloquial turn, a sentence starting with "And"/"But") —
  never a factual error. Save `CH{n}_01_RAW.md`.
- **Adversarial audit** — build a line-by-line table in `99_AUDIT_LOG.md`:
  claim → exact source file. Any claim without a source is **deleted, not
  softened**. Inject `[Source_File]` citation markers inline. Save
  `CH{n}_02_VERIFIED.md`.

### Phase 3 — Design (per chapter)

- Read `CH{n}_02_VERIFIED.md`.
- Build every table the chapter needs, fully populated — no "TBD", no empty rows.
- For any process, comparison, hierarchy, or classification, build a figure with
  `scripts/figlib.py` — a flowchart, cycle, tree, timeline, matrix, comparison or
  chart — and embed it (no external image links; no bitmaps unless it is the
  author's own artwork). Figures must be large and legible: a 640-unit canvas,
  `viewBox` only, type ≥ 14 units, aspect ratio between ~0.2 and 1.15. Aim for at
  least one figure per chapter. See `references/figures.md`.
- For a hand-drawn look, call `figlib.set_style("sketch")` before building the
  figures. To include the author's own scanned sketch, clean it with
  `prep_sketch.py` and place it with `booklib.sketch_block()` — see
  `references/sketches.md`.
- Save the visual-enhanced chapter as `CH{n}_03_FINAL.md`; extract keywords to
  `CH{n}_INDEX.md`.

### Phase 4 — Assembly and back matter

- Concatenate every `CH{n}_03_FINAL.md`, in order, into `99_MANUSCRIPT.md`.
- Generate: glossary, book review/conclusion, corrections appendix (summarised
  from `99_AUDIT_LOG.md`), index (from the `CH{n}_INDEX.md` files),
  acknowledgments, about-the-author page (from `01_AUTHOR_BIO.md`), and an
  opening/closing poem if the style guide calls for one.
- Generate `KDP_METADATA.md` separately: title, subtitle, back-cover blurb,
  category paths, keywords, pricing notes. Never merge it into the manuscript.

### Phase 5 — Build, QA, delivery

1. **Content first.** Write the manuscript into content modules. See
   `references/content-rules.md` — the honesty rules are not optional.
2. **HTML master.** `python3 build_any.py <module> <out.html>` — one builder for
   every language: it reads `META["lang"]`, loads the matching kit
   (`bookkit_<lang>`, falling back to `bookkit`), and substitutes the module's
   `FIGURES`. The builder
   measures each block in headless Chromium, packs blocks into fixed A4 sheets
   (1123 px tall), keeps headings with their text, builds the table of contents,
   resolves a page-accurate index, and stamps a small boxed author-name
   watermark and the page number in the footer of every sheet.
3. **Verify.** `python3 verify_any.py <file.html>` — expect `max sheet height:
   1123`, empty overflow lists, the footer watermark box on every interior page.
4. **DOCX.** Rasterise figures (`rasterize_all.py`), then
   `python3 make_docx_designed.py <module> <out.docx> <en|hi|gu>`. Full-bleed
   cover, maroon headings, styled tables and boxes, embedded figures, and a small
   boxed author-name watermark in the DOCX footer.
5. **Mobile edition (when asked).** `python3 build_mobile.py <module> <out.html>`
   — one reflowable, responsive document (`body.is-mobile`) that adapts to any
   phone or e-reader width, using the same content module, stylesheet and
   ornaments as the A4 master.
6. **PDF.** `python3 pdf_export.py <a4.html> <out_base> [<mobile.html> <mobile.pdf>]`
   — colour + grayscale A4, and a phone-sized PDF when a mobile HTML is given.
   Grayscale is a CSS `filter: grayscale(1)` pass (rendered, not selectable).
7. **Combined all-languages file.** `python3 combine_langs.py`; verify with
   `verify_combined.py`.
8. **Supporting files — build ALL of them.** KDP metadata, author instructions,
   a marketing kit (e.g. `Instagram_Marketing.md`), and a one-page poster
   (`poster.py`). Never ship the book without these. For a KDP eBook, also
   produce an EPUB — it is KDP's native eBook format and the reflowable mobile
   HTML is the right source. No EPUB converter is guaranteed in the sandbox, so
   package the mobile HTML as a minimal EPUB (an uncompressed `mimetype` entry
   first, then `META-INF/container.xml` and `OEBPS/content.opf` plus one XHTML
   document), or use a converter if one is installed. Confirm it opens.
9. **Package.** Group by language (`01_English/`, `02_Hindi/`, …) plus
   `Supporting/`, then zip the whole set. Confirm the zip exists before delivery.
10. **QA gate.** Run `references/qa-checklist.md` against the built files. Fix
    every failure and re-check — never deliver on a partial pass.
11. **Deliver** the built editions plus `KDP_METADATA.md` and `99_AUDIT_LOG.md`.
    Working files (`00_*`, `01_*`, `CH{n}_*`, `99_DEDUP_REGISTRY.md`,
    `99_MANUSCRIPT.md`) stay hidden unless the user asks for them.

## Hard rules

- **Zero hallucination.** Every substantive claim is attributed to a named
  source, presented as a classical/observational finding, or removed. No source,
  no claim. Never write "research shows" without a name in the same breath. Mark
  popular figures as folklore. See `references/content-rules.md`.
- **No skip, no filler.** Do not re-summarise prior chapters, restate the plan,
  or pad. Read only the files a task needs.
- **Deduplicate across the whole book**, not just within a chapter, via
  `99_DEDUP_REGISTRY.md`.
- **In a series, deduplicate across books too**, via
  `99_SERIES_DEDUP_REGISTRY.md`: a phrase, framing or example already used in an
  earlier book must not repeat in a later one, and each book must still stand
  alone for a reader who starts with it.
- **Every visual is SVG, embedded** in the DOCX — no external links, no bitmaps
  unless it is the author's own artwork (a scanned sketch or a photograph; see
  `references/sketches.md`). **Every table is fully populated.**
- **Human voice, not AI voice.** Variable sentence length, plain words, concrete
  examples, no banned AI-tell phrases. See `references/qa-checklist.md`.
- **The author bio comes from the user, never invented.** Keep one canonical bio
  (from `assets/author-bio-template.md`) and reuse it in every edition and
  language. Check Notion Memory for a stored "Author biography" memory before
  writing or changing a bio.
- **Watermark on every interior page**, every edition, every format, as a
  **small boxed author name in the page footer** — never a large diagonal
  background mark across the page. In DOCX it lives in the page footer, so it
  repeats and survives edits.
- **One stylesheet, byte-identical across languages.** Verify with an md5 of the
  `<style>` block.
- **No ISBN** printed anywhere. Indic editions are eBook-only unless the user
  says otherwise.
- **Nothing hits the user until QA passes.**
- **State the honest limitations** in the user-facing instructions (DOCX reflows
  so pagination differs from the fixed HTML; grayscale PDFs are a rendered pass
  without selectable text).
- **Deliver the complete set, every time.** A book is not done until the user has
  the HTML master, the mobile edition, the colour and grayscale PDFs, the DOCX,
  the KDP metadata, the author instructions, the marketing kit, the poster, AND
  the zip. Do not stop at a subset — a missing poster or zip is a failed delivery.
- **No orphaned ornament pages.** A part must not begin or end with a scene-break
  ornament, and no page may carry only an ornament. See
  `references/lessons-and-gotchas.md`.
- **Rebuild everything after any change.** A change to the parser, the
  stylesheet, the ornaments or the bio invalidates every downstream file: re-run
  parse → A4 → mobile → PDFs → DOCX → package, and re-verify.
- **When the user supplies a finished manuscript, it IS the source.** Do not
  rewrite the prose; the work is parse → design → assemble → build, plus the
  front/back matter every book needs.
- **Strip the manuscript's working notes.** A supplied manuscript often carries
  notes addressed to the author (source/verification registers, per-quote
  "check before publication" lines, editorial to-do lists). Remove them from the
  book; keep the reader-relevant part as one clean "A Note on the Text" and move
  the author checklist to `KDP_Metadata.md` / `99_AUDIT_LOG.md`. See
  `references/lessons-and-gotchas.md` §9.6.

## Gotchas that will cost you an hour if forgotten

- **Headless Chromium, not Playwright.** Playwright's driver is unreliable in
  the sandbox. Use `chromium --headless=new --no-sandbox --disable-gpu` with
  `--dump-dom` (measure), `--print-to-pdf`, or `--screenshot`. Every script
  reads the browser from `CHROMIUM` (default `/usr/local/bin/chromium`) and the
  project from `BOOK_DIR` — set both instead of editing paths.
- **Indic scripts need a font.** Devanagari and Gujarati render because Noto
  Sans/Serif Devanagari and Gujarati are installed system-wide. Check with
  `fc-list | grep -i gujarati` before promising an edition, and name the script
  font explicitly in each figure's `font-family`.
- **Ghostscript is usually absent**, so do not plan a colour-to-gray PDF
  conversion through it.
- **The index is page-accurate by substring search.** Each index term's key (the
  text before the first comma) must actually appear in the mapped chapter, or the
  builder falls back to the chapter's first page.
- **Front matter differs by pack.** The Unlearning pack has six fixed sheets
  (cover, title, copyright, dedication, about, foreword) plus the contents
  sheet, so flow content starts at page 8. The ornamental pack has four fixed
  sheets (cover, title, copyright, epigraph) plus contents, so flow begins at
  page 6. The poem goes on the very last page, after the series page.
- **Keep long content out of the About page's flow** — it is a single fixed
  sheet, so a long bio can overflow it. Verify after any bio change.
- **Localise every list, not just the prose.** When adding entries to a
  glossary or index, translate them in every edition; an English term left in an
  Indic index reads as a bug. Translate glossary terms and definitions, and
  transliterate index terms (an index finds the word as it appears in the text).
- **A batch translation tool may time out on large inputs.** Keep calls to about
  two chapters (roughly 4,000 words); copy each result to a unique path
  immediately, because the sandbox filename is reused.
- **`--default-background-color` takes ARGB hex, not CSS.** Use `FFFBF7F0`, not
  `#fbf7f0`, or Chromium silently produces no screenshot. `00000000` does not
  give you a transparent PNG — render the element on white instead.
- **`getBoundingClientRect()` excludes margins.** To measure real page fill, sum
  `offsetTop + offsetHeight + marginTop + marginBottom` per child, or you will
  under-count and mistake a full page for an empty one.
- **A figure renders small if it has a fixed width/height or tiny type.** Author
  every figure on a 640-unit canvas with a `viewBox` only, type ≥ 14 units and
  strokes ≥ 1.6; build them with `figlib`. `verify_figures.py` catches
  violations. See `references/figures.md`.
- **Runes read as words.** An asymmetric row of rune glyphs reads as letters
  (KPAXA). Keep every ornament symmetric; mirror the runes about the centre.
- **Thin ornament strokes vanish.** Give small ornaments a minimum stroke width
  (`max(1.15, r*0.08)`) or the marigold disappears at 28 px.
- **Divider SVGs are baked in at parse time.** After editing `ornaments.py`,
  re-run the manuscript parser or the built book keeps the old ornaments.
- **Verify the built HTML has no unresolved placeholders** — grep for
  `__INDEX__`, `{PG}` and `__FIG_`.
- **A skill's sandbox tree is session-local.** Writing to
  `/scratch/skills/<name>/` does not always persist to the canonical skill; keep
  the working copy and offer the user a packaged copy of the updated skill.

## Supporting files

- `references/workflow.md` — the full pipeline with commands, plus the file map
  and the rebuild order.
- `references/content-rules.md` — the writing and honesty rules.
- `references/qa-checklist.md` — the pre-delivery QA gate.
- `assets/author-bio-template.md` — the canonical bio facts and ordering rule.
- `scripts/` — the working builders and generators, ready to copy into a new project.
- `scripts/kits/` — the per-language front/back-matter kits.
- `scripts/assets/book.css` — the Unlearning stylesheet.
- `scripts/ornaments.py` — the vine/rune/marigold/border SVG library (ornamental pack).
- `scripts/assets/book_ornamental.css` — the ornamental + responsive stylesheet.
- `scripts/kits/bookkit_ornamental.py` — cover/title/copyright/epigraph templates.
- `scripts/build_a4.py`, `scripts/build_mobile.py`, `scripts/make_docx.py` —
  A4 master, reflowable mobile edition, and designed DOCX for the ornamental pack.
- `scripts/fetch_fonts.py` — downloads and base64-embeds the webfonts (run once).
- `scripts/verify_a4.py`, `scripts/measure_fill.py` — layout, watermark and
  page-fill checks for the A4 build.
- `scripts/poster.py` — one-page A4 launch poster.
- `scripts/parse_manuscript.py` — turns a supplied manuscript into an
  ornamental-pack content module (splits on `## `, applies the scene-break,
  drop-cap and exhibit rules, strips the `*(Chapter N — end)*` markers).
- `scripts/update_bio.py` — rewrites the about-the-author block in the kits and
  the DOCX label dicts from the canonical bio; run after any bio change.
- `scripts/booklib.py` — the shared helpers every tool uses (`BOOK_DIR`,
  `CHROMIUM`, module/kit loading, figure substitution and naming). Copy it
  alongside the scripts into any project.
- `scripts/combine_langs.py`, `verify_combined.py`, `rasterize_all.py`,
  `poster.py`, `make_docx_designed.py` — driven entirely by the content module
  and their command-line arguments, so they build any book with no edits.
- `scripts/themes.py` — the named colour themes and the palette resolver that
  every builder, the ornaments and the DOCX generators read.
- `references/themes.md` — the shipped themes and how to add one.
- `scripts/figlib.py` — the inline-SVG diagram builders (flowchart, tree, cycle,
  timeline, matrix, comparison, bars, line) sized for legibility.
- `scripts/verify_figures.py` — checks every figure is large enough and legible.
- `references/figures.md` — how to make figures large, clear and legible, and the
  alternative ways to draw them (matplotlib charts, Graphviz if installed).
- `scripts/prep_sketch.py` — cleans a scanned sketch into a print-ready PNG.
- `references/sketches.md` — the hand-drawn figure style, and how to include the
  author's own drawings and photographs.
- `references/content-module.md` — the module contract every tool shares.
- `references/lessons-and-gotchas.md` — the pagination, ornament and toolchain
  rules learned building *Life Is a Comedy*. **§9** adds the rules from the
  *READ. LIVE. TRANSFORM.* run: parsing a supplied HTML manuscript, the lxml
  tail trap, mismatched part dividers, the footer watermark, the non-AI cleanup
  pass, the minimal cover, and EPUB packaging without a converter.
- `references/clinical-safety.md` — **medical, clinical and homeopathy books
  only** (ignore it for any general title): the safety framing and voice —
  emergency-referral boxes, crisis-line verification, contested-claim reframing,
  the four-audience badges.
- `references/full-book-prompt.md` — the one-shot full-book generation prompt,
  kept as a template.
