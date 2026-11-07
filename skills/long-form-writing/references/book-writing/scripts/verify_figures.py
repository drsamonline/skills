# -*- coding: utf-8 -*-
"""Check that a book's figures are large enough and legible.

Hand-drawn figures are the usual source of "the diagram is too small". This
audits every figure in a content module's FIGURES map and reports:

  * the canvas size and aspect ratio;
  * any figure drawn with fixed width/height instead of a viewBox (renders small);
  * any type below the legibility floor (figlib.MIN_FONT);
  * any figure whose canvas is narrower than the text column, or whose aspect
    ratio is so extreme it will render as a thin strip.

Usage:
    BOOK_DIR=/path/to/project python3 verify_figures.py <content_module> [<module> ...]

Exit code is non-zero if any figure fails, so it can gate a build.
"""
import os, re, sys
import booklib, figlib

MIN_CANVAS = 500          # canvas units; below this a figure is cramped
MAX_ASPECT = 1.15         # height/width; above this a figure is taller than wide
MIN_ASPECT = 0.16         # below this a figure renders as a thin strip


def check(modname):
    mod = booklib.load_module(modname)
    figs = booklib.figures(mod)
    bad = 0
    if not figs:
        print(modname, "- no FIGURES map")
        return 0
    for key, svg in figs.items():
        probs = list(figlib.audit(svg))
        m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
        if not m:
            probs.append("no numeric viewBox")
            print("  %-28s %s" % (key, "; ".join(probs)))
            bad += 1
            continue
        w, h = float(m.group(1)), float(m.group(2))
        aspect = h / w if w else 0
        if w < MIN_CANVAS:
            probs.append("canvas only %d units wide (min %d)" % (w, MIN_CANVAS))
        if aspect > MAX_ASPECT:
            probs.append("too tall (aspect %.2f)" % aspect)
        if aspect < MIN_ASPECT:
            probs.append("too thin (aspect %.2f)" % aspect)
        status = "; ".join(probs) if probs else "ok"
        print("  %-28s %dx%d aspect %.2f  %s" % (key, int(w), int(h), aspect, status))
        if probs:
            bad += 1
    return bad


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    total = 0
    for m in argv[1:]:
        print("==", m)
        total += check(m)
    print("figures with problems:", total)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv)
