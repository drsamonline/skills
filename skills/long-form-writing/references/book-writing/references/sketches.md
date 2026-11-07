# Sketches

There are two kinds of sketch, and the skill supports both.

## 1. A hand-drawn *style* for the generated diagrams

Turn it on for a whole book with one call, before building the figures:

```python
import figlib
figlib.set_style("sketch")     # or set_style("clean") to go back
```

Every box, arrow, axis and gridline is then drawn with a hand-drawn wobble in
pencil grey, so the flowcharts, trees, cycles and matrices read as sketched
rather than drafted. Details that matter:

- **Deterministic.** The wobble is a hash of the coordinates, not a random
  number, so the same figure looks identical on every build — no churn in diffs,
  no surprise changes between editions.
- **Rasterises cleanly.** The rough look is pure geometry (wobbly paths), not an
  SVG filter, so CairoSVG converts it for the DOCX without loss. Filters such as
  `feTurbulence` look nice in a browser but do **not** survive rasterisation — do
  not use them.
- **Type stays crisp.** Only the strokes are rough; the labels are drawn as
  normal text, so the legibility floor (≥ 14 units) still holds. Never
  hand-draw the lettering.
- **Tune the pencil.** `figlib.set_style("sketch", pencil="#2f2f2f")` sets the
  stroke colour; the fills still come from the book's theme, so a sketch can be
  warm-toned (marigold fills) or cool.

A sketchy figure passes `verify_figures.py` exactly like a clean one.

## 2. The author's own drawings and photographs

A scanned pencil sketch, a handwritten diagram, a photo — these are bitmaps, and
they are allowed as *author-supplied artwork* (the general rule against bitmaps
is about substituting raster for what should be a crisp SVG diagram).

### Clean the scan first

Scans arrive grey, unevenly lit, bordered by desk and softened by JPEG. Run each
through `prep_sketch.py`, which crops to the drawing, lifts contrast, thresholds
to clean line art, resizes, and can recolour it to the book's paper and ink:

```
python3 prep_sketch.py scan.jpg sketches/fig-01.png --width 1600 \
        --tint FBF7F0 --ink 241C14
```

- `--width` sets the print width in pixels — **1600 is the target** (2× the
  column at print size); below ~1000 the sketch looks soft in the DOCX.
- `--tint` / `--ink` lay the drawing on the theme's paper and ink, so it sits on
  the page instead of on a white rectangle. Use the theme's `paper` and `ink`
  (see `themes.resolve(name)`); omit both for a pure white background.
- `--threshold` (default 165) sets how dark a pixel must be to count as ink;
  raise it for a faint pencil, lower it for a dark pen.

### Put it in the book

Keep cleaned sketches in a `sketches/` folder in the project, then reference one
with `booklib.sketch_block()`:

```python
import booklib
CHAPTERS = [{"key": "chapter-1", "title": "The First Room", "blocks": [
    '<p class="lead">...</p>',
    booklib.sketch_block("sketches/fig-01.png", "Figure 1. The kitchen table, from memory."),
]}]
```

The pipeline then handles each format correctly, with no extra work:

- **HTML / PDF** — `build_any.py` (and the ornamental builders) inline the image
  as a base64 data URI, so the eBook HTML stays a single self-contained file.
- **DOCX** — `make_docx_designed.py` finds the `<img>` and embeds the file at the
  full column width (16.5 cm).

### Sizing and placement

- `figure.fig img` fills the text column, so a sketch is as wide as the prose —
  no fixed pixel size to set.
- A sketch is centred and captioned like any other figure; keep captions in the
  same voice as the diagrams.
- Very tall sketches (taller than wide) will run long on the page — crop them
  closer, or split into two.
- Mixing is fine: a chapter can carry a clean diagram, a sketchy one, and a
  scanned drawing, as long as the captions are consistent.

## Before delivery

- Run `verify_figures.py` for the SVG diagrams (unchanged).
- For scanned sketches, check each one at print size: is it sharp, is the paper
  tone the book's, is it cropped tight?
- Confirm the DOCX embeds every sketch (the build prints no `[missing image]`),
  and that the eBook HTML carries the image inline (no broken `<img>`).
