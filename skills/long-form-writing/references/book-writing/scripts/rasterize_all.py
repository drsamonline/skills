# -*- coding: utf-8 -*-
"""Rasterise every figure a content module exposes to PNG, for DOCX embedding.

Figures come from the module's FIGURES map, so this works for any book. Each
figure is written to <lang>_<name>.png - the filename make_docx_designed.py
looks for.

Rasterising is done with CairoSVG at high resolution (FIG_SCALE, default 3x,
capped at FIG_WIDTH px) so the figures are crisp when scaled in the DOCX; if
CairoSVG is unavailable it falls back to a headless-Chromium screenshot.

Usage:
    BOOK_DIR=/path/to/project python3 rasterize_all.py <content_module> [<module> ...]
"""
import os, re, sys, subprocess
import booklib

BOOK = booklib.book_dir()
CH = booklib.chromium()
SCALE = float(os.environ.get("FIG_SCALE", "3"))     # 3x for crisp print / DOCX
MAXW = int(os.environ.get("FIG_WIDTH", "2000"))


def vb(svg):
    return [float(x) for x in re.search(r'viewBox="([\d.\s]+)"', svg).group(1).split()]


def raster_cairosvg(svg, png, w):
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=png,
                     output_width=min(MAXW, int(w * SCALE)))


def raster_chromium(svg, png, w, h):
    W = int(w * SCALE); H = int(h * SCALE)
    html = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<style>html,body{margin:0;padding:0;background:#fbf7f0}'
            'svg{width:%dpx;height:%dpx;display:block}</style></head><body>%s</body></html>'
            % (W, H, svg))
    tmp = os.path.join(BOOK, "_fig.html")
    open(tmp, "w").write(html)
    subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--screenshot=" + png, "--window-size=%d,%d" % (W, H),
                    "--hide-scrollbars", "--default-background-color=FFFBF7F0",
                    "file://" + tmp], capture_output=True, timeout=120)


def rasterise(modname):
    mod = booklib.load_module(modname)
    lang = booklib.module_lang(mod)
    figs = booklib.figures(mod)
    if not figs:
        print(modname, "- no FIGURES map")
        return
    for key, svg in figs.items():
        x, y, w, h = vb(svg)
        png = os.path.join(BOOK, booklib.fig_name(lang, key))
        try:
            raster_cairosvg(svg, png, w)
        except Exception:
            raster_chromium(svg, png, w, h)
        print(os.path.basename(png), os.path.getsize(png) if os.path.exists(png) else "MISSING")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    for m in argv[1:]:
        rasterise(m)


if __name__ == "__main__":
    main(sys.argv)
