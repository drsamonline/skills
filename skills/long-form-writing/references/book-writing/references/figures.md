# Figures — making diagrams large, clear and legible

Figures are the part of a book most likely to come out wrong. A hand-drawn SVG
with a big empty viewBox and 8-unit type renders as a faint scribble, and a wide,
short drawing renders as a thin strip. This file is how to avoid both, and what
to use instead of hand-drawing when you can.

## The rules

1. **Draw at the real size.** Use a canvas **640 units wide** — about the width of
   the A4 text column. One unit is roughly one pixel at print size, so a figure
   drawn 640 wide prints 640 wide. Never draw a large scene on a small viewBox and
   scale it up, or a small scene on a large viewBox and let it shrink.
2. **`viewBox` only, never `width`/`height` on the `<svg>`.** A fixed width/height
   makes the figure render at that pixel size and no larger. The stylesheets set
   `figure.fig svg{ width:100% }`, so a viewBox SVG fills the column.
3. **Type no smaller than 14 units; strokes no thinner than 1.6.** Below that,
   text and hairlines vanish at print scale. `figlib` enforces both.
4. **Keep the aspect ratio between about 0.2 and 1.15** (height ÷ width). Taller
   than wide overflows a page; thinner than 0.2 is a strip. If a diagram is
   naturally wide, split it or stack it.
5. **One colour scheme, real contrast.** Use the book's theme colours (paper,
   panel, ink, accent). Never light-on-light.
6. **Leave breathing room but not dead space.** ~16–24 units of padding, not a
   third of the canvas.

`figlib.audit(svg)` checks rules 2–3 mechanically; `verify_figures.py` checks the
canvas and aspect too.

## Use the figure library

`scripts/figlib.py` builds the common diagrams at the right size and with legible
type, so you do not hand-draw them. It returns a bare `<svg>` for a content
module's `FIGURES` map.

```python
import figlib, themes
P = themes.resolve("sage")          # optional: match the book's theme

FIGURES = {
  "__FIG_LOOP__":  figlib.flowchart(["Notice the cue", "Name the story",
                                     "Choose one move", "Repeat"], pal_=P,
                                    title="The change loop"),
  "__FIG_ROOTS__": figlib.tree("A stuck pattern", ["Fear", "Habit", "Story"], pal_=P),
  "__FIG_WHERE__": figlib.matrix("Effort", "Reward",
                                 ["Quick win", "Big bet", "Avoid", "Drudgery"], pal_=P),
  "__FIG_HOURS__": figlib.bars([("Sleep", 7), ("Work", 9), ("Rest", 2)], unit="h", pal_=P),
}
```

Then reference each one in a block, wrapped by `figlib.block`:

```python
CHAPTERS = [{"key": "chapter-1", "title": "The First Room", "blocks": [
    '<p class="lead">...</p>',
    figlib.block("__FIG_LOOP__", "Figure 1. The change loop."),
]}]
```

### Which diagram for which content

| The content is… | Use |
|---|---|
| A process or sequence of steps | `flowchart(steps, vertical=False)` |
| A cycle or loop that repeats | `cycle(steps)` |
| A category with sub-parts | `tree(root, branches)` |
| A sequence over time | `timeline([(when, what), …])` |
| A choice on two axes | `matrix(xlab, ylab, [tr, tl, bl, br])` |
| A comparison of options | `compare(cols, rows)` |
| Quantities to compare | `bars([(label, value), …])` |
| A trend | `line([(label, value), …])` |
| A simple table of numbers | a real `<table class="data">`, not a figure |

Anything else: compose `figlib.node()`, `figlib.arrow()` and `figlib.text()` on a
`figlib.wrap(...)` canvas.

## SVG in HTML and PDF, raster in DOCX

- **HTML and PDF keep the SVG** — vector, crisp at any zoom. Nothing to do.
- **DOCX needs a raster.** `python-docx` cannot embed SVG, so `rasterize_all.py`
  converts each figure to PNG at **3× (`FIG_SCALE`)** and the DOCX embeds it at
  the full text-column width (16.5 cm). That is why figures look sharp in the DOCX
  rather than pixelated.

So author once in SVG; the pipeline handles both.

## Alternative ways to make figures

Inline SVG by hand or via `figlib` is the default because it embeds in HTML, PDF
and DOCX alike and needs no extra tools. Two more options are useful:

- **Data charts: matplotlib.** For real charts (several series, axes, ticks),
  `matplotlib` is installed. Save as SVG so it stays vector:
  ```python
  import matplotlib; matplotlib.use("Agg")
  import matplotlib.pyplot as plt
  fig, ax = plt.subplots(figsize=(6.4, 3.2))
  ax.plot(xs, ys); ax.set_xlabel("Week"); ax.set_ylabel("Hours")
  fig.savefig("chart.svg", format="svg", bbox_inches="tight")
  ```
  Read the file back and use it as a FIGURES value (wrap its `<svg>` contents).
  Size the figure at ~6.4×3.2 in so it matches the 640-unit canvas, and set the
  font size to at least 11 pt so the rasterised type clears the legibility floor.
- **Auto-laid-out graphs: Graphviz.** `dot` is *not* installed in this sandbox, so
  it cannot be relied on. If you install it (`apt`/`brew graphviz`), `dot -Tsvg`
  gives clean auto-layout for larger node graphs; feed its `<svg>` in as a FIGURES
  value. For everything `figlib` covers, prefer `figlib` — it needs nothing extra
  and matches the house style.

Rasterising itself uses **CairoSVG** (`cairosvg.svg2png`), which is installed and
handles SVG→PNG cleanly at any scale; `rasterize_all.py` falls back to a headless
Chromium screenshot only if CairoSVG is missing.

## Before delivery

- Run `verify_figures.py` on every content module — expect no problems.
- Every process, comparison, hierarchy and classification in the prose has a
  matching figure.
- No figure is a thin strip or taller than the page.
- Figures read at print size: step back and squint; if the labels blur, the type
  is too small.
