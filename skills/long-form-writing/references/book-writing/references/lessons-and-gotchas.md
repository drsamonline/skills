# Lessons and gotchas — the ornamental pack

Hard-won rules from building *Life Is a Comedy* (a 22,000-word literary memoir,
English, A4 + mobile). Read this before building an ornamental-pack book. Every
rule here cost real time to learn; skipping one produces a visible defect.

---

## 1. Delivery is the whole set, or it is not done

The single most expensive mistake: building the book beautifully and stopping
before the supporting files and the package. A finished delivery is **all** of:

1. the A4 HTML master,
2. the reflowable mobile HTML,
3. the A4 colour PDF,
4. the A4 grayscale PDF,
5. the phone-sized mobile PDF,
6. the designed DOCX,
7. `KDP_Metadata.md`,
8. `Author_Instructions.md`,
9. a marketing kit (`Instagram_Marketing.md`),
10. a one-page poster (`poster.py`),
11. a zip of the whole set, grouped `01_English/` + `Supporting/`.

Confirm each file exists before you write the delivery message. A missing poster
or zip is a failed delivery, not a rounding error.

---

## 2. A user-supplied manuscript is the source, not a draft

When the user hands over a finished manuscript, do **not** rewrite the prose.
The work becomes: parse → design → assemble → build, plus the front/back matter
every book needs (copyright, epigraph/dedication, glossary, index, About the
Author, back-cover copy). Keep the author's words exactly.

Front/back matter that must be *authored* should be minimal and drawn from the
book or the author's own notes — never invented facts, never a borrowed blurb.

---

## 3. Turning a manuscript into a content module (the parser)

Split on `## ` headings; convert to blocks:

- `---` → `ornaments.rune_divider()` (a scene break).
- a bold-only paragraph (`**Exhibit One: The Astronaut.**`) → a `div.exhibit`
  sub-head with an `ex-label`.
- the section's first paragraph → `p.lead` with a drop-cap span.
- inline `*x*` → `<em>`, `**x**` → `<strong>`.

**Strip the leading and trailing `---` of every section.** A manuscript usually
wraps each chapter's `*(Chapter N — end)*` marker in `---`, and those are
structural, not scene breaks. Left in, they render as ornament-only pages — a
page carrying nothing but a border and a rune divider. This was the exact
"empty pages with chapter ending lines and designs" defect.

Also drop the manuscript's own end markers (`*(Chapter N — end)*`) and any
trailing contents list the author typed.

**Re-run the parser after editing `ornaments.py`.** The divider SVGs are baked
into the content module at parse time, so a design change does not reach the book
until you re-parse.

---

## 4. Pagination: no orphaned ornaments, no sparse chapter ends

The A4 builder packs measured blocks into fixed sheets. Rules it must enforce:

- **Every part starts on a fresh page.**
- **Never emit a page that carries only an ornament.** Filter out any packed page
  whose every block is a `rune_divider`.
- **Keep a heading with the text that follows it** (move a trailing heading to
  the next page).
- **Balance a part across its pages.** If the last page comes out sparse
  (under ~60% full), search a range of per-page fill targets and pick the one
  that yields the **fullest last page at the same page count**. Without this, a
  chapter's closing couplet sits alone on an otherwise blank page. Pseudo-code:

  ```python
  naive = pack_pairs(pairs, AVAIL_H)
  if last_fill(naive) < 0.60 * AVAIL_H:
      total = sum(h for _, h in pairs); n = len(naive)
      lo = total / n
      for t in [lo + (AVAIL_H - lo) * i / 16 for i in range(17)]:
          bal = pack_pairs(pairs, t)
          if 1 < len(bal) <= n and last_fill(bal) > best:
              best = bal
  ```

- **Gate on real fill.** No interior page should be under ~60% full, except the
  About-the-Author page and a deliberately short epigraph/title page.

Give the page a little usable height back by trimming the bottom padding
(72 px top / 78 px bottom, `AVAIL_H ≈ 966`) — this alone pulls many short tails
back onto the previous page.

---

## 5. Measuring page fill correctly

`getBoundingClientRect().height` **excludes margins**, so summing child rects
under-counts by every paragraph's bottom margin (13 px each) and makes a full
page look half empty. Measure the used height as:

```js
var b = c.offsetTop + c.offsetHeight
      + parseFloat(getComputedStyle(c).marginTop || 0)
      + parseFloat(getComputedStyle(c).marginBottom || 0);
```

`measure_fill.py` does this and reports every page under 60%.

---

## 6. Ornament rules

- **Symmetry, always.** An asymmetric row of rune glyphs reads as a word — the
  first divider spelled *KPAXA*. Mirror the runes about the centre and put a
  marigold in the middle: sprig · rune · ◆ · marigold · ◆ · rune(mirrored) ·
  sprig(mirrored).
- **Minimum stroke width.** At small sizes a stroke scaled by radius vanishes.
  Use `max(1.15, r * 0.08)` in the marigold generator, or the 28 px bloom is
  invisible.
- **Inline SVG only**, so the same ornament embeds in HTML, PDF and DOCX.
- The set that works: a `rune_divider` scene-break, a `rune_medallion` chapter
  number, a rune-framed `monogram`, `corner_frame` vine corners, a
  `page_border` (fine double rule + edge diamonds; vine corners on openers), a
  `marigold_garland` cover crown, a `marigold_motif`, and a `rule_flourish`.
- Palette: ivory `#fbf7f0`, maroon `#6e1f2a`, gold `#b8862b`, marigold `#dd8a1c`.
  Type: EB Garamond body, Cinzel display, Inter labels. (Any of these can be
  overridden by a theme — see `references/themes.md`.)

---

## 7. Toolchain gotchas

- **Chromium `--default-background-color` takes ARGB hex**, not CSS: use
  `FFFBF7F0`, not `#fbf7f0`, or the screenshot is never written. `00000000` does
  **not** produce a transparent PNG — render the element on white instead.
- **Headless Chromium flags**: `--dump-dom` to measure, `--print-to-pdf` (add
  `--no-pdf-header-footer` for clean output), `--screenshot` with `--window-size`.
- **Fonts**: fetch from Google Fonts with a desktop Chrome UA and keep **only the
  basic-latin subset** (`unicode-range` starting `U+0000-00FF`), or the CSS
  bloats with duplicated subsets (1.8 MB → 0.64 MB). Base64-embed as woff2.
- **Phone-sized PDF**: inject `@page{size:390px 844px;margin:0}` plus
  `*{print-color-adjust:exact}` before printing the mobile HTML.
- **DOCX → PDF for a visual check**: `libreoffice --headless --convert-to pdf`.
- **Verify no unresolved placeholders**: grep the built HTML for `__INDEX__`,
  `{PG}`, `__FIG_`.
- **The skill sandbox tree is session-local.** `/scratch/skills/<name>/` is
  re-materialised from the canonical skill between sessions, so edits there may
  not persist. Keep the working copy and offer the user a packaged (tar.gz) copy
  of the updated skill.

---

## 8. Build order (rebuild everything after any change)

```
parse_manuscript.py manuscript.md <slug> en  -> content module (re-run after ornaments.py)
build_a4.py    <mod> <a4.html> -> A4 master
build_mobile.py <mod> <m.html> -> mobile HTML
verify_a4.py   <a4.html>       -> height / overflow / watermark
measure_fill.py <a4.html>      -> page-fill gate
pdf_export.py  <a4.html> <base> <m.html> <m.pdf>
make_docx.py   <mod> <out.docx>
poster.py                      -> A4 poster
zip            -> 01_English/ + Supporting/
```

Watermark: a small boxed author name in the footer of every interior page (the
old ~0.035-opacity diagonal background mark was retired); exempt the cover and
back cover. The DOCX uses Georgia (Cinzel/EB Garamond are usually absent) and
reflows, so its pagination will not match the fixed HTML — say so in the
instructions.

---

## 9. Supplied HTML manuscripts, and what the *READ. LIVE. TRANSFORM.* run taught

That book arrived not as markdown but as a **finished A4 HTML** (97 `<section>`
pages, 74 chapters, 12 parts), and the ornamental builders had to be re-pointed
at it. Everything below is reusable.

### 9.1 Parsing HTML, not markdown

`parse_manuscript.py` splits on `## `. For an HTML source, split on
`//section` (lxml) and map the source's own classes to the ornamental block
vocabulary instead of inventing one:

| Source element | Ornamental block |
|---|---|
| `p.lead` | `p.lead` (+ drop-cap span on the first letter) |
| `div.verse-card` | a kept `div.verse-card` (styled in the book CSS) |
| `div.check` / `div.read-carefully` | `div.callout` with a `clabel` |
| `div.practice` / `div.practice-box` | `div.vignette` with a `vlabel` |
| `div.takeaway` | a `div.takeaway` band |
| `div.quote` | `div.pullquote` |
| `div.grid` of `div.card` | `div.grid2` of `div.card` |
| `table` | `table.data` (fully populated) |
| `ul` / `ol` | kept as-is |
| `div.visual` (an inline SVG) | dropped — see 9.3 |

Add CSS for any new block class (`.verse-card`, `.takeaway`, `.grid2`,
`table.data`, list markers) to the one stylesheet, and teach `make_docx.py` the
same blocks, or the DOCX flattens them to plain paragraphs.

### 9.2 The lxml tail trap (silent text duplication)

`lxml.html.tostring(el)` **includes the element's tail text by default**. Building
an inner-HTML helper as `tostring(child) + child.tail` therefore emits every
tail twice. In a list item `<li><strong>Day 1 — Read:</strong> choose…</li>` the
body came out doubled. Fix: `tostring(child, with_tail=False)`, then append the
tail yourself.

Related: a box like `<div class="check"><strong>READ CAREFULLY</strong><br/>body</div>`
hides its body in the **`<strong>` element's tail**, not in a child. A splitter
that only reads `el.text` and child elements returns an empty body — all 74
callouts and takeaways came out blank until the tail was captured. Read
`el.text`, each child, **and each child's tail**.

### 9.3 Deduplicate repeated figures

The manuscript carried one identical "VERSE → UNDERSTAND → APPLY → PRACTICE" SVG
inside all 74 chapters. Repeating it 74 times is the visual version of a repeated
sentence. Drop the per-chapter copy and ship a **curated** figure set (one per
part opener, plus the method and the seven-day practice), built with `figlib`.

### 9.4 Mismatched part dividers

The source had **13 part dividers for a 12-part structure** (a stray "BECOMING"
divider printed as a second "Part VII"). Map parts **by title**, not by document
order, and cross-check against the author's own Contents page. Also: in the
second half the part openers sit consecutively with no chapters between them, so
document order cannot assign chapters to parts — use the author's stated chapter
ranges.

### 9.5 Sparse divider pages

A part opener of just a lead line and a figure measured ~35% full and failed the
page-fill gate. Add an **"In this part"** list of the part's chapter titles to
each opener — it fills the page and is genuinely useful.

### 9.6 Strip the manuscript's working notes

A supplied manuscript often carries **notes addressed to the author**, not to the
reader: source/verification registers, a per-quote line like "…platform-specific
publishing requirements should still be checked", "final editorial audit before
publication" to-do lists, "restore the remaining chapters…" asides. Remove them
from the book. Keep the reader-relevant part as **one clean, human page** — here,
"A Note on the Text" — and move the author-facing checklist into
`KDP_Metadata.md` / `99_AUDIT_LOG.md`. This is the "strictly non-AI" pass: no
working note, no to-do, no meta commentary survives inside the book.

### 9.7 Make the kit and builders meta-driven

`bookkit_ornamental.py`, `build_a4.py`, `build_mobile.py` and `make_docx.py`
shipped hardcoded to the demo book (title, subtitle, "A Memoir", copyright text,
the `<title>` tag). For any new book: read every string from `META`, and add a
theme. The cover, title page, copyright and epigraph must all be template
functions of `META`.

### 9.8 A theme from a supplied palette

When the author supplies a palette (here green/gold/cream), add one entry to
`THEMES` in `themes.py` — `paper`, `ink`, `maroon`/`maroon_deep` (the primary),
`gold`/`gold_soft`, `marigold`/`marigold_soft`, `cover1..3` — and set
`META["theme"]`. Everything else is derived. See `references/themes.md`.

### 9.9 A many-part book's Contents must list parts

An 89-row TOC overflows one fixed sheet. List the **parts** (with their chapter
ranges) and the front/back matter, not every chapter. Compute each part's range
from the chapter keys that follow it.

### 9.10 A minimal cover option

For "less designer, minimalistic but impressive": a deep ground, a **single fine
double-rule frame** (`ornaments.plain_frame()`), the title set large and stacked
(`title_html` with `<br>`), the subtitle, and the author resting at the foot. No
garland, no vine corners, no marigold. Typography does the work.

### 9.11 EPUB without a converter

No `pandoc`/`ebook-convert` in the sandbox. Build the container by hand: an
**uncompressed `mimetype` entry first**, then `META-INF/container.xml`,
`OEBPS/content.opf`, a `nav.xhtml`, and one XHTML document made by serialising
the mobile HTML's body with `lxml` `method="xml"` and inlining the stylesheet.
Validate that the XHTML parses as XML before packing.

### 9.12 The watermark is a footer box

The old large diagonal background mark is retired. The watermark is a **small
boxed author name in the page footer** (`build_a4.py` puts `meta["author"]` in a
`.page-foot .wm` span; the DOCX uses a 1-cell bordered table in the footer). The
cover and back cover carry no footer. `verify_a4.py` recolours `.page-foot .wm`
red and counts the pixels (threshold ~60).

### 9.13 The spell-check pass: know what NOT to "fix"

Running a spellchecker over a Qur'an book flags a lot that is correct. Do not
"correct": **archaic translation forms** (admonisheth, knoweth, maketh, pardoneth
— they are Pickthall's 1930 wording), **British spellings** (apologise, behaviour,
recognise, programme — correct for Indian English), proper nouns and
transliterations (Qur'an, tawakkul, surah, ayah), and **drop-cap extraction
artifacts** (a checker sees "P" + "urpose" and reports "urpose"). Fix only real
typos, and never rewrite the author's prose.
