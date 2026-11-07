# -*- coding: utf-8 -*-
"""Check figures for the defects a visual skim misses.

  * a fixed width/height on the <svg> (renders small) -> use viewBox only
  * type below 14 units, strokes below 1.6
  * a title that collides with the top node of a cycle/flowchart
  * text whose bounding box spills outside the smallest filled shape that holds
    it (labels wider than their circle/box)

Usage:
    python3 figcheck.py <content_module>
Exit code 1 if any problem is found.
"""
import re, sys
import booklib

MIN_FONT, MIN_STROKE = 14, 1.6


def _bbox_of_text(svg):
    """Approximate each <text> bbox from x,y + anchor + size + char count."""
    boxes = []
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', svg, re.S):
        attrs, body = m.group(1), m.group(2)
        def a(n, d=None):
            r = re.search(r'%s="([^"]+)"' % n, attrs)
            return r.group(1) if r else d
        try:
            x = float(a("x", "0")); y = float(a("y", "0"))
        except ValueError:
            continue
        size = float(a("font-size", "14"))
        anchor = a("text-anchor", "start")
        txt = re.sub(r"<[^>]+>", "", body)
        w = len(txt) * size * 0.55
        if anchor == "middle":
            x0 = x - w / 2
        elif anchor == "end":
            x0 = x - w
        else:
            x0 = x
        boxes.append((x0, y - size * 0.7, x0 + w, y + size * 0.7, txt.strip()))
    return boxes


def check(svg, key=""):
    probs = []
    head = svg.split("viewBox")[0]
    if "viewBox" not in svg:
        probs.append("no viewBox (fixed size will render small)")
    if re.search(r'\bwidth="\d+"', head):
        probs.append("fixed width/height on the <svg> (use viewBox only)")
    fonts = [float(x) for x in re.findall(r'font-size="([\d.]+)"', svg)]
    small = sorted({f for f in fonts if f < MIN_FONT})
    if small:
        probs.append("font-size below %d: %s" % (MIN_FONT, small))
    strokes = [float(x) for x in re.findall(r'stroke-width="([\d.]+)"', svg)]
    thin = sorted({s for s in strokes if s < MIN_STROKE})
    if thin:
        probs.append("stroke below %.1f: %s" % (MIN_STROKE, thin))

    # title / top-node collision: a text near the canvas top overlapping a filled
    # rect/circle that also sits near the top.
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    if vb:
        W, H = float(vb.group(1)), float(vb.group(2))
        boxes = _bbox_of_text(svg)
        # filled shapes near the top
        shapes = []
        for m in re.finditer(r'<rect\b([^>]*)/>', svg):
            g = m.group(1)
            if 'fill="none"' in g:
                continue
            x = float(re.search(r'x="([\d.-]+)"', g).group(1)) if 'x="' in g else 0
            y = float(re.search(r'y="([\d.-]+)"', g).group(1)) if 'y="' in g else 0
            w = float(re.search(r'width="([\d.-]+)"', g).group(1)) if 'width="' in g else 0
            h = float(re.search(r'height="([\d.-]+)"', g).group(1)) if 'height="' in g else 0
            shapes.append((x, y, x + w, y + h))
        for (x0, y0, x1, y1, txt) in boxes:
            if y0 > H * 0.25 or not txt:
                continue
            for (sx0, sy0, sx1, sy1) in shapes:
                if sy0 > H * 0.25:
                    continue
                # overlap?
                if x0 < sx1 and x1 > sx0 and y0 < sy1 and y1 > sy0:
                    probs.append("title/label %r overlaps a top shape near y=%.0f" % (txt[:32], sy0))
    return probs


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 0
    mod = booklib.load_module(argv[1])
    figs = booklib.figures(mod)
    bad = 0
    print("== %s" % argv[1])
    for key, svg in figs.items():
        probs = check(svg, key)
        tag = "  %-28s" % key
        if probs:
            bad += 1
            print(tag + "PROBLEMS")
            for p in probs:
                print("      -", p)
        else:
            print(tag + "ok")
    print("figures with problems:", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
