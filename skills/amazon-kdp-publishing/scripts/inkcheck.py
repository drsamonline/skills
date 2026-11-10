#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Measure where ink actually falls on each page, and compare with the trim.

    python3 inkcheck.py book.pdf --trim 6x9 --pages 701-828
    python3 inkcheck.py book.pdf --trim 6x9 --sample 40

CSS says the margin is 0.875 in. This measures the PDF and tells you whether it
actually is. That distinction matters: a table wider than its column, a heading
rule, a tinted box or a rounding error all move ink without changing the CSS.

Thresholds are KDP's minimums, not your design margins — a page can sit well
inside the design margin and still be fine. Use --min-margin to check against
your own intent instead.
"""
from __future__ import annotations
import argparse, glob, os, re, subprocess, sys, tempfile

from PIL import Image


def gutter_for(pages):
    if pages <= 150:  return 0.375
    if pages <= 300:  return 0.5
    if pages <= 500:  return 0.625
    if pages <= 700:  return 0.75
    return 0.875


def page_count(pdf):
    r = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
    m = re.search(r"Pages:\s+(\d+)", r.stdout)
    return int(m.group(1)) if m else 0


def render(pdf, page, dpi, tmp):
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(page), "-l", str(page),
                    pdf, os.path.join(tmp, f"p{page:05d}")], check=False,
                   capture_output=True)
    hits = glob.glob(os.path.join(tmp, f"p{page:05d}*.png"))
    return hits[0] if hits else None


def ink_bbox(png, threshold, min_ink=3):
    """Bounding box of real ink.

    A single antialiasing pixel at the edge of a justified line is not a layout
    overflow, and counting it produces false alarms. A row or column only counts
    when it holds at least `min_ink` dark pixels.
    """
    im = Image.open(png).convert("L")
    W, H = im.size
    px = im.load()

    def col_ink(x):
        return sum(1 for y in range(0, H, 2) if px[x, y] < threshold) >= min_ink

    def row_ink(y):
        return sum(1 for x in range(0, W, 2) if px[x, y] < threshold) >= min_ink

    left = next((x for x in range(W) if col_ink(x)), None)
    if left is None:
        return None
    right = next((x for x in range(W - 1, -1, -1) if col_ink(x)), left)
    top = next((y for y in range(H) if row_ink(y)), 0)
    bottom = next((y for y in range(H - 1, -1, -1) if row_ink(y)), H - 1)
    return left, right, top, bottom, W, H


def main():
    ap = argparse.ArgumentParser(description="Check real ink extents against the trim.")
    ap.add_argument("pdf")
    ap.add_argument("--trim", default="6x9", help="WxH in inches, e.g. 6x9 or 8.5x11")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--threshold", type=int, default=200,
                    help="luminance below which a pixel counts as ink (default 200; "
                         "raise to ~245 to include pale tints)")
    ap.add_argument("--min-margin", type=float, default=None,
                    help="check against this instead of KDP's minimums")
    ap.add_argument("--sample", type=int, default=24, help="pages to sample (0 = all)")
    ap.add_argument("--min-ink", type=int, default=3,
                    help="dark pixels a row/column needs before it counts as ink "
                         "(default 3; stops antialiasing fringes raising false alarms)")
    a = ap.parse_args()

    m = re.match(r"([\d.]+)x([\d.]+)$", a.trim)
    if not m:
        sys.exit("--trim must look like 6x9")
    W_IN, H_IN = float(m.group(1)), float(m.group(2))

    total = page_count(a.pdf)
    if not total:
        sys.exit("could not read the page count")

    if a.min_margin is not None:
        g_min = a.min_margin
        outside = top_m = bottom_m = a.min_margin
    else:
        g_min = gutter_for(total)
        outside = top_m = bottom_m = 0.25

    if a.sample and a.sample < total:
        step = max(1, total // a.sample)
        pages = sorted(set(list(range(1, min(total, 12) + 1)) +
                           list(range(12, total + 1, step)) + [total]))
    else:
        pages = list(range(1, total + 1))

    print(f"{a.pdf}")
    print(f"  {total} pages, trim {W_IN} x {H_IN} in")
    print(f"  required: gutter {g_min} in · outside/top/bottom {outside} in"
          f"  (threshold {a.threshold})")
    print(f"  sampling {len(pages)} page(s)\n")
    print(f"{'page':>6} {'left':>7} {'right':>7} {'top':>7} {'bottom':>7}  side   result")

    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        for p in pages:
            png = render(a.pdf, p, a.dpi, tmp)
            if not png:
                print(f"{p:>6}   render failed")
                continue
            bb = ink_bbox(png, a.threshold, a.min_ink)
            if bb is None:
                print(f"{p:>6}   blank page")
                continue
            left, right, top, bottom, W, H = bb
            L = left / a.dpi
            R = (W - 1 - right) / a.dpi
            T = top / a.dpi
            B = (H - 1 - bottom) / a.dpi
            recto = (p % 2 == 1)
            need_L = g_min if recto else outside
            need_R = outside if recto else g_min
            fails = []
            if L < need_L - 0.004: fails.append(f"left {L:.3f}<{need_L}")
            if R < need_R - 0.004: fails.append(f"right {R:.3f}<{need_R}")
            if T < top_m - 0.004: fails.append(f"top {T:.3f}<{top_m}")
            if B < bottom_m - 0.004: fails.append(f"bottom {B:.3f}<{bottom_m}")
            side = "recto" if recto else "verso"
            if fails:
                bad.append((p, fails))
                print(f"{p:>6} {L:7.3f} {R:7.3f} {T:7.3f} {B:7.3f}  {side}   FAIL: " + ", ".join(fails))
            else:
                print(f"{p:>6} {L:7.3f} {R:7.3f} {T:7.3f} {B:7.3f}  {side}   ok")

    print()
    if bad:
        print(f"{len(bad)} page(s) put ink closer to the trim edge than allowed.")
        print("Fix the layout, not the trim: a table wider than its column, a rule")
        print("or a box that overhangs, or a margin set in px that rounds down.")
        return 1
    print("all sampled pages keep ink inside the printable area")
    return 0


if __name__ == "__main__":
    sys.exit(main())
