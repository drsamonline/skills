# The pipeline, phase by phase

Work runs in five phases. A "continue" (`c`) completes the current phase and
stops only at a phase boundary. Inside a phase, do every task without stopping
and without narration. A long phase may span several turns; then a turn covers a
coherent group of chapters and reports at that boundary.

The working-file map is in `SKILL.md`. The honesty rules are in
`content-rules.md`. The pre-delivery gate is in `qa-checklist.md`.

---

## Phase 1 — Foundation

Set up one working folder; copy the skill's `scripts/` and
`scripts/assets/book.css` into it. Build the embedded-font CSS once
(`fonts/fonts.css`) and keep it stable.

Then, in one phase:

1. Ask for topic and title only if not already given.
2. Read every uploaded `.txt`/`.md` source file in full; extract hard data to
   `02_RESEARCH_EXTRACTS.md`.
3. Write `00_BLUEPRINT.md`: outline, chapter list, word-count targets, per-chapter
   source-file mapping, and the claim ledger (every claim → a named source, a
   classical/observational finding, or marked for removal). For a series, also
   fix how each book stands alone and each book's arc.
4. Write `00_MANIFEST.md`: one atomic `[ ]` row per task across all five phases,
   in execution order.
5. Generate `01_AUTHOR_BIO.md` from `assets/author-bio-template.md` (keep the
   ordering rule; invent nothing).
6. Generate `01_STYLE_GUIDE.md`: structured, systematic, compliance-flavoured
   prose, with a philosophical/narrative register for poetry and reflection.

Report: `Phase 1 (Foundation) complete. Ready for 'c'.`

---

## Phase 2 — Manuscript (per chapter, run across all chapters)

For each chapter, in order, do both steps before moving on:

1. **Draft** — write from the mapped source file(s) only, in the book's voice.
   Read `99_DEDUP_REGISTRY.md` first and write around anything already logged
   (across the whole book), then append this chapter's new phrases/concepts as
   you go. Apply the style guide and the banned-word list while writing: vary
   sentence length, add concrete examples, allow small natural imperfections,
   never a factual error. `CH{n}_01_RAW.md`.
2. **Adversarial audit** — line-by-line table into `99_AUDIT_LOG.md`: claim →
   exact source file. Delete unsourced claims (do not soften). Inject
   `[Source_File]` markers inline. `CH{n}_02_VERIFIED.md`.

A big book may take several turns; cover three to five chapters per turn and
report `Phase 2: chapters 1–5 done. Ready for 'c'.`

---

## Phase 3 — Design (per chapter)

For each chapter:

- Build every table the chapter needs, fully populated.
- For any process, comparison, hierarchy, or classification, build a figure with
  `scripts/figlib.py` — a flowchart, cycle, tree, timeline, matrix, comparison or
  chart — and embed it. Figures must be large and legible (640-unit canvas,
  `viewBox` only, type ≥ 14 units); see `references/figures.md`.
- Save `CH{n}_03_FINAL.md`; extract keywords to `CH{n}_INDEX.md`.

Report at the boundary, as in Phase 2.

---

## Phase 4 — Assembly and back matter

- Concatenate every `CH{n}_03_FINAL.md`, in order, into `99_MANUSCRIPT.md`.
- Generate: glossary, book review/conclusion, corrections appendix (summarised
  from `99_AUDIT_LOG.md`), index (from the `CH{n}_INDEX.md` files),
  acknowledgments, about-the-author page (from `01_AUTHOR_BIO.md`), and an
  opening/closing poem if the style guide calls for one.
- Generate `KDP_METADATA.md` separately: title, subtitle, back-cover blurb,
  category paths, keywords, pricing notes. Never merge it into the manuscript.
- Write the manuscript into content modules (`content_<book>_<lang>.py`), keeping
  the interface in `SKILL.md`. Split large modules: `<book>_<lang>_a.py` (META,
  foreword, INTRO, chapters 1–5) and `<book>_<lang>_b.py` (chapters 6+, CLOSING,
  GLOSSARY, BIBLIOGRAPHY, POEM, INDEX_TERMS), with a thin `<book>_<lang>.py` that
  re-exports both.

Report: `Phase 4 (Assembly) complete. Ready for 'c'.`

---

## Phase 5 — Build, QA, delivery

Do the whole phase, then run the gate, then deliver.

### Build the HTML master

```
python3 build_any.py <module> <out.html>      # any language (reads META["lang"])
```

The builder assembles front matter (cover, title, copyright, dedication, about,
foreword) and back matter from the language kit; measures every flow block in
headless Chromium; packs blocks into A4 sheets up to 958 px of content, never
leaving a heading as the last block on a page; computes the contents and a
page-accurate index (searching each mapped chapter's rendered text for the index
key); places the poem on the final page, after the series page; and stamps the
small boxed author-name watermark and page number in the footer of every sheet.

### Verify the HTML

```
python3 verify_any.py <file.html>
```

Expect `max sheet height: 1123`, empty `v-overflow pages` and `h-overflow pages`,
and `watermark: N/N pages carry the mark` (the footer box; cover and back cover
excepted).

### Build the designed DOCX

```
python3 rasterize_all.py <module> [<module> ...]
python3 make_docx_designed.py <module> <out.docx> [<en|hi|gu>]
```

Full-bleed maroon cover, styled headings, tables, callouts and case boxes,
embedded figures, and a small boxed author-name watermark in the DOCX footer so
it repeats on every page and survives editing. Verify:

```
unzip -p <out.docx> word/footer1.xml | grep -c Sohil
```

### Export PDFs (usually English only)

```
python3 pdf_export.py <a4.html> <out_base> [<mobile.html> <mobile.pdf>]
```

Colour via Chromium `--print-to-pdf`; grayscale by injecting
`html{filter:grayscale(1)}` before printing. The grayscale pass rasterises, so
its text is not selectable — state this.

### Build the combined all-languages file

```
python3 combine_langs.py <slug> <title> en=a.html hi=b.html gu=c.html
python3 verify_combined.py <slug>_-_All_Languages.html
```

The merged file carries the stylesheet once, a top-right switcher, and
`#en`/`#hi`/`#gu` deep links. Printing hides the switcher and prints only the
active language.

### Author bio

- Fetch the canonical bio from `assets/author-bio-template.md`, or from Notion
  Memory (a Profile memory titled "Author biography") if one exists; otherwise
  draft from supplied material and save it there.
- Write the matching language version for each edition.
- Update it in the kits and the DOCX label dicts, then rebuild everything that
  contains it.

### Supporting files

- `KDP_Metadata.md` — title, subtitle, author, language, series, description,
  keywords, categories per edition. No ISBN. Note which languages are eBook-only.
  **Validate the limits in code, not by eye:** title + subtitle ≤ 200 characters;
  description ≤ 4,000 (HTML tags count); exactly 7 keywords, each ≤ 50 characters
  and non-duplicated; an author bio; 2–3 category paths. Paperback minimum is 24
  pages (A4 is a supported trim); print interiors are grayscale by default —
  colour costs far more, so confirm before assuming it. Check the current limits
  with a search, as KDP changes them. The AI-content declaration is the user's to
  make: tell them what KDP's "AI-generated" vs "AI-assisted" definitions are so
  they can answer accurately.
- `Author_Instructions.md` — what each file is, how to open and edit it, the
  honest limitations.
- `Instagram_Marketing.md` — post ideas, captions, hashtags, a posting rhythm.
- A one-page series poster, rendered from HTML to PDF.

### Package

Title-based filenames, grouped by language:

```
00_All_Languages/   the combined files
01_English/         eBook HTML, DOCX, colour + grayscale PDF
02_Hindi/           eBook HTML, DOCX
03_Gujarati/        eBook HTML, DOCX
Supporting/         KDP metadata, instructions, marketing, poster
```

Then `zip -r <Series>_-_Complete.zip 00_All_Languages 01_English 02_Hindi 03_Gujarati Supporting`.

### QA gate

Run `references/qa-checklist.md` against the built files. Fix every failure and
re-check.

### Deliver

Present the built editions plus `KDP_METADATA.md` and `99_AUDIT_LOG.md`. Working
files stay hidden unless the user asks for them.

---

## Rebuild discipline

When one shared thing changes (the stylesheet, the kit, the author bio,
translations), everything downstream changes. Rebuild in this order: HTML
masters, then DOCX, then combined files, then PDFs, then the package. Re-verify
after each stage. Save a file again under the same name to publish a new version;
never invent `_v2` names.

## Translation gotchas (multi-language editions)

- **Localise every list.** When you add glossary or index entries, translate them
  in every edition. Translate glossary terms and definitions; transliterate index
  terms (an index finds the word as it appears in the text). An English term left
  in an Indic index reads as a bug.
- **Keep batch calls to about two chapters** (roughly 4,000 words) or the
  translation tool times out.
- **Copy each translation result to a unique path immediately** — the sandbox
  filename is reused and the next call overwrites it.
- **Check the whole figure set**, not just the prose: figure labels, table cells,
  and SVG text nodes are easy to leave in English.

---

## The ornamental pack and the mobile edition

For literary books, memoir and poetry, the **ornamental pack** replaces the
Unlearning builders. Copy `ornaments.py`, `build_a4.py`, `build_mobile.py`,
`make_docx.py`, `verify_a4.py`, `measure_fill.py`, `poster.py`, `fetch_fonts.py`,
`kits/bookkit_ornamental.py` and `assets/book_ornamental.css` into the project,
then:

```
export BOOK_DIR=/scratch/work/<project>          # every script reads this
python3 fetch_fonts.py                            # once: download + embed webfonts
python3 parse_manuscript.py manuscript.md <slug> en   # manuscript -> content module
python3 build_a4.py     content_<book>_en "Book_-_A4_eBook.html"
python3 build_mobile.py content_<book>_en "Book_-_Mobile_eBook.html"
python3 verify_a4.py    "Book_-_A4_eBook.html"    # max height 1123, no overflow, watermark
python3 measure_fill.py "Book_-_A4_eBook.html"    # page-fill gate: nothing under ~60%
python3 make_docx.py    content_<book>_en "Book_-_Designed.docx"
python3 pdf_export.py   "Book_-_A4_eBook.html" "Book_-_A4" \
                        "Book_-_Mobile_eBook.html" "Book_-_Mobile.pdf"
python3 poster.py                                 # one-page A4 poster
```

The A4 master starts every part on a fresh page, balances each part across its
pages so no chapter ends on a sparse page, and stamps the ornamental page border
(vine corners on openers) and the small boxed author-name watermark and page
number in the footer. The mobile master is one reflowable document
(`body.is-mobile`) with no fixed pages. `make_docx.py` rasterises the cover to a
full-bleed image, embeds a rune-divider PNG between parts, and injects the footer
watermark box.

### Parsing a manuscript into a content module

Split on `## ` headings. Turn `---` into `ornaments.rune_divider()`, bold-only
paragraphs into `div.exhibit` labels, and give each part's first paragraph
`class="lead"` for the drop cap. **Strip the leading and trailing `---` of every
section** (the manuscript wraps each `*(Chapter N — end)*` marker in them; left
in, they become ornament-only pages). Drop the end markers and any trailing
contents list the author typed. Re-run the parser after any change to
`ornaments.py`, because the divider SVGs are baked in at parse time.

### Supporting files and the package

Build **all** of them, then zip:

```
01_English/   eBook HTML, mobile HTML, colour + grayscale PDF, mobile PDF, DOCX
Supporting/   KDP metadata, author instructions, marketing kit, poster
```

A delivery without the poster, the marketing kit or the zip is incomplete.

The full rule set — pagination, ornament, toolchain and delivery — is in
`references/lessons-and-gotchas.md`.
