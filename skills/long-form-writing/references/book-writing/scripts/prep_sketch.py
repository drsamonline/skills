# -*- coding: utf-8 -*-
"""Turn a scanned or photographed sketch into a clean, print-ready PNG.

Scans arrive with grey paper, uneven light, a border of desk around the page,
and a JPEG haze. This crops to the paper (dropping the desk surround), lifts the
contrast, thresholds to clean line art, resizes to a print width, and
(optionally) recolours to the book's paper and ink so the sketch sits on the page
rather than on a white rectangle.

Usage:
    python3 prep_sketch.py <input> <out.png> [--width 1600] [--threshold 165]
                           [--tol 45] [--ink 241c14] [--tint FBF7F0]

--tint sets the paper colour the sketch is laid on (use the theme's paper);
omit it for a pure white background. --ink sets the line colour. --tol is how
far from the paper tone a pixel may be and still count as paper. Feed the result
to booklib.sketch_block() and it flows through HTML, PDF and DOCX unchanged.
"""
import argparse, os, sys


def _crop_to_paper(im, tol):
    """Crop to the paper region, dropping any desk/background surround."""
    try:
        import numpy as np
    except ImportError:
        from PIL import ImageChops
        bbox = ImageChops.difference(im, im.__class__.new("L", im.size, 255)).getbbox()
        return im.crop(bbox) if bbox else im
    arr = np.asarray(im)
    paper = int(np.median(arr))
    mask = np.abs(arr.astype(int) - paper) < tol
    ys, xs = np.where(mask)
    if not len(xs):
        return im
    x0, y0, x1, y1 = int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1
    # only crop when the paper is smaller than the frame (i.e. there is a surround)
    if (x1 - x0) >= im.width - 4 and (y1 - y0) >= im.height - 4:
        return im
    inset = 2   # trim the paper's outer edge so no surround bleeds in
    return im.crop((min(im.width, x0 + inset), min(im.height, y0 + inset),
                    max(0, x1 - inset), max(0, y1 - inset)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--width", type=int, default=1600)
    ap.add_argument("--threshold", type=int, default=165)
    ap.add_argument("--tol", type=int, default=45)
    ap.add_argument("--ink", default=None)
    ap.add_argument("--tint", default=None)
    a = ap.parse_args()
    try:
        from PIL import Image, ImageOps
    except ImportError:
        sys.exit("Pillow is required: pip install pillow")

    im = Image.open(a.inp).convert("L")
    im = _crop_to_paper(im, a.tol)
    im = ImageOps.autocontrast(im, cutoff=1)
    im = im.point(lambda v: 0 if v < a.threshold else 255)      # clean line art
    if a.width and im.width != a.width:
        im = im.resize((a.width, max(1, round(im.height * a.width / im.width))), Image.LANCZOS)
    if a.tint and a.ink:
        im = ImageOps.colorize(im, black="#" + a.ink.lstrip("#"), white="#" + a.tint.lstrip("#"))
    else:
        im = im.convert("RGB")
    im.save(a.out, "PNG", optimize=True)
    print("wrote %s  %dx%d  %d bytes" % (a.out, im.width, im.height, os.path.getsize(a.out)))


if __name__ == "__main__":
    main()
