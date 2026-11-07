# Cover geometry

A cover is one file: back, spine and front on a single page. Two different
geometries, depending on binding.

**Everything here depends on the final page count.** Change the interior, and the
spine — and therefore the whole cover — changes. Rebuild the cover whenever the
interior page count moves.

---

## Paperback

```
cover width  = bleed + back + spine + front + bleed
cover height = bleed + trim height + bleed

bleed        = 0.125 in
back, front  = trim width
spine        = pages × thickness per page
```

Thickness per page: white/standard colour `0.002252`, cream `0.0025`,
premium colour `0.002347`.

**Worked example — 6 × 9 in, 752 pages, black ink on white:**

```
spine  = 752 × 0.002252          = 1.6935 in  (43.0 mm)
width  = 0.125 + 6 + 1.6935 + 6 + 0.125 = 13.9435 in
height = 0.125 + 9 + 0.125       = 9.2500 in
```

Those are the numbers to check against KDP's cover calculator before uploading.

### Zones on the paperback spread

| Zone | Rule |
|---|---|
| Bleed | 0.125 in on top, bottom and outside edges. Background must extend into it. |
| Safe area | Keep text and critical images ≥ 0.25 in inside the trim line. |
| Spine text | Only on books > 79 pages. ≥ 0.0625 in clear of both fold lines. Allow ±0.0625 in fold variance. |
| Barcode | Reserve a clear 2 × 1.2 in box in the lower-right of the back cover (LTR books), ≥ 0.25 in clear of the trim edges and the spine. KDP prints the barcode; do not place your own. |
| File | One PDF, back+spine+front. Under 650 MB converts; keep it under 40 MB for print speed. |

For right-to-left books, mirror the whole layout: front cover to the left of the
spine, back cover to the right, barcode bottom-left.

---

## Hardcover (case laminate)

A hardcover cover is a **wrap**, not a page. It has three extra features a
paperback does not:

- **Wrap** — the strip beyond the trim that folds around the board and glues to
  the inside of the case.
- **Hinge** — the groove where the case bends when the book opens, one on each
  side of the spine.
- **Board overhang** — the case boards are slightly larger than the text block,
  which adds to the height.

```
height = wrap + trim height + overhang + wrap
width  = wrap + back + hinge + spine + hinge + front + wrap
spine  = (pages × thickness per page) + board allowance
```

Constants that reproduce KDP's published example:

| Constant | Value |
|---|---|
| wrap | 0.591 in |
| hinge (each side) | 0.197 in |
| board overhang (height) | 0.236 in |
| board allowance (spine) | 0.189 in |

**Worked example — 6 × 9 in, 300 pages, black ink on white** (KDP's own sample
output is 14.439 × 10.417 in):

```
spine  = 300 × 0.002252 + 0.189 = 0.8646 in
width  = 0.591 + 6 + 0.197 + 0.8646 + 0.197 + 6 + 0.591 = 14.4406 in
height = 0.591 + 9 + 0.236 + 0.591 = 10.4180 in
```

Matches to within a thousandth of an inch.

### The honest caveat

**KDP does not publish a hardcover spine formula.** Unlike the paperback, where
the formula is printed in the help pages, the hardcover figures above are
reverse-engineered from KDP's own worked example and the constants used by
public cover calculators. They reproduce that example, but they are not
guaranteed by Amazon.

For a real hardcover, do this:

1. Compute the geometry here to design against.
2. Generate KDP's own template at
   `kdp.amazon.com/en_US/cover-templates` with the exact trim and page count.
3. Overlay your design on that template and confirm the spine band and hinge
   lines sit where you assumed.
4. Upload and let the Print Previewer check it before ordering a proof.

If the numbers disagree, **trust KDP's template**, not this file.

### Zones on the hardcover spread

| Zone | Rule |
|---|---|
| Wrap | All four edges. Background must extend into it — it becomes the inside cover. |
| Safe margin | Keep all text ≥ 0.635 in (16 mm) inside the book edge. |
| Hinge | 0.4 in total band each side of the spine. Nothing important here — it bends. |
| Spine safe area | Spine text must clear the hinge bands. |
| Headband | Black-and-white headband is added top and bottom of the spine above 120 pages. |

---

## Debugging a rejected cover

| Symptom | Cause |
|---|---|
| "Cover dimensions are incorrect" | Width/height do not match the calculator for your page count and paper. Recompute the spine with the *current* page count. |
| Spine text cut off or wrapped around | Text too close to the fold, or the book is under 79 pages. |
| White border at the edge | Background does not extend into the bleed. |
| Barcode unreadable | Content inside the 2 × 1.2 in barcode box, or too close to the edge. |
| Cover looks wrong on the preview | Paper type differs from the one the spine was cut for — cream is thicker than white. |

---

## Checking the rendered file

Never trust the design source; check the PDF:

```bash
pdfinfo Cover.pdf | grep "Page size"
```

For 6 × 9 paperback at 752 pages the answer must be `1003.92 x 666 pts`
(13.9435 × 9.25 in × 72). If it says `612 x 792` you have silently exported a
US Letter page — usually because the HTML had no `@page` rule.
