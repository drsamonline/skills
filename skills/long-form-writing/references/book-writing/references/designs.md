# Designs — more than vines, runes and sigils

A designed book should not look like every other book from this skill. The
ornamental pack ships vines, runes, marigolds and medallions; the Unlearning pack
ships tables, callouts and diagrams. Neither is the whole vocabulary. This file
is how to give a book its **own** visual identity.

## The layers of a designed page

Work through these layers; a book needs the first four and benefits from the rest:

1. **Palette (theme).** One theme recolours everything — cover, rules, headings,
   tables, panels, the page surround, the watermark. See `references/themes.md`.
   Never leave a book on the default theme if the author gave a colour.
2. **Cover.** The single most important designed page. It may use: a full-bleed
   ground, a corner filigree frame, a crown/garland, a large central emblem, an
   inscriptional display face, and an imprint line. Or go minimal: a deep ground,
   one fine double-rule frame, a stacked title, the author at the foot.
3. **A motif per chapter.** A distinct emblem above each chapter title. This is
   what makes a book read as *designed* rather than *typeset*.
4. **Page frame.** A fine double rule inset on every interior page (CSS
   `::before`/`::after` on `.sheet-a4`), excluded from the cover and back cover.
5. **Section flourishes.** A rule flourish under a chapter title, a scene-break
   divider between sections, a drop cap on each part opener.
6. **Figure style.** A consistent diagram look (clean or sketch). See
   `references/figures.md`.

## The motif families (`scripts/motifs.py`)

`motifs.py` is a library of 26 emblems in five families. Every one is a bare
`<svg viewBox>` string with **explicit palette colours** (so it rasterises in
colour for the DOCX and EPUB), strokes ≥ 1.6, and type ≥ 14.

| Family | Keys | Good for |
|---|---|---|
| **emblems** | eye, loop, spiral, seed, mask, vortex, vesica, compass, lantern, peak, lyre, cover | one per chapter |
| **celestial** | sun, moon, star, orbit, constellation | spirituality, cosmology, wonder |
| **botanical** | leaf, blossom | nature, growth, memoir, food |
| **geometric** | rings, chevron, fan, sunburst | modern, business, design, technology |
| **line** | flourish, wave, knot | literary, classical, calm |

```python
import motifs
motifs.set_palette(primary="#3b2f63", accent="#c08a2b", light="#9a8fc4")  # match the theme
FIGURES = {
    "__FIG_SIGIL_CH1__": motifs.render("sunburst"),
    "__FIG_SIGIL_CH2__": motifs.render("leaf"),
}
# chapter opener:
#   <div class="chapter-open"><span class="chapter-sigil">__FIG_SIGIL_CH1__</span>
#     <span class="chap-num">Chapter 1</span><h1>...</h1></div>
```

CSS (add to the stylesheet once):

```css
.chapter-sigil{ display:block; text-align:center; margin:0 auto 12px; color:var(--maroon); }
.chapter-sigil svg{ width:78px; height:auto; display:inline-block; }
```

## Choosing emblems that mean something

Do not decorate at random. Pick an emblem whose **shape carries the chapter's
idea**, so the design reads as considered:

| Chapter is about… | Motif |
|---|---|
| seeing, attention, awareness | eye |
| a trap, a loop, repetition | loop, rings |
| change, process, growth | spiral, leaf, seed |
| the body, breath | wave, blossom |
| identity, the mask | mask |
| impermanence, the self | vortex, knot |
| connection, duality | vesica, orbit |
| direction, a journey | compass, star |
| illumination, teaching | lantern, sun |
| peaks and valleys, effort | peak, chevron |
| music, art, play | lyre, fan, sunburst |
| mystery, the night | moon, constellation |

Give each chapter a **different** emblem. Repeating one emblem across every
chapter is the visual equivalent of a repeated sentence.

## Rules that keep a motif from looking broken

- **Explicit colours, never `currentColor`** — or the DOCX/EPUB raster is black.
- **Fixed `viewBox`, no `width`/`height` on the `<svg>`** — the stylesheet sets
  the display size, so it stays crisp at any zoom.
- **Strokes ≥ 1.6 units, type ≥ 14 units** — below that, a 78 px motif blurs.
- **Keep it symmetric** unless the asymmetry is meaningful; an asymmetric glyph
  row reads as letters.
- **`figcheck.py`** flags thin strokes, tiny type, fixed sizes and a title
  colliding with a top node. Run it.
- **`verify_figures.py` flags small motif canvases** (a 160-unit sigil fails its
  500-unit minimum). That is expected for motifs — run it for the *diagrams*.

## Adding a new motif

Add a function to `motifs.py` that returns `_svg(body)`, register it in `MOTIFS`
and in the right `FAMILY` list. Reuse the helpers (`_ring`, `_rays`, `_spiral`,
`_diamond`). Then `figcheck.py` it.
