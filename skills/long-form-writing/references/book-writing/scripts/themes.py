# -*- coding: utf-8 -*-
"""Named colour themes for the book toolchain.

A theme is a palette of named colours. The stylesheets route every colour through
CSS custom properties, so one theme recolours the whole book - cover, rules,
headings, tables, callouts, panels, the page surround and the watermark - in a
single move. The same palette drives the designed DOCX and the ornaments, so
every format matches.

Pick a theme with the BOOK_THEME environment variable, or META["theme"] on the
content module (the env var wins). Default: "ember", the original maroon/gold.

    BOOK_THEME=sage python3 build_any.py content_book_en out.html

Shipped themes: ember, sage, indigo, slate, plum, terracotta, midnight.
"""
import os

DEFAULT = "ember"

# The colours a theme names directly; the rest are derived in resolve().
THEMES = {
    "ember": {
        "paper": "#fbf7f0", "ink": "#241c14",
        "maroon": "#6e1f2a", "maroon_deep": "#4c1019",
        "gold": "#b8862b", "gold_soft": "#d8b45c",
        "marigold": "#dd8a1c", "marigold_soft": "#f0b45a",
        "cover1": "#7a2230", "cover2": "#5e1620", "cover3": "#3c0d15",
    },
    "sage": {
        "paper": "#f7f5ec", "ink": "#1e241c",
        "maroon": "#2f5140", "maroon_deep": "#20382b",
        "gold": "#a98b4a", "gold_soft": "#c9b177",
        "marigold": "#c07a2c", "marigold_soft": "#dc9d55",
        "cover1": "#31513f", "cover2": "#24402f", "cover3": "#152a1d",
    },
    "indigo": {
        "paper": "#f6f5f2", "ink": "#1b1e2c",
        "maroon": "#2b3070", "maroon_deep": "#1c2050",
        "gold": "#b1743a", "gold_soft": "#cf9a63",
        "marigold": "#c98a3a", "marigold_soft": "#e0a866",
        "cover1": "#2c3272", "cover2": "#1f2455", "cover3": "#12163a",
    },
    "slate": {
        "paper": "#f5f6f5", "ink": "#1a2124",
        "maroon": "#2b3d45", "maroon_deep": "#1d2a30",
        "gold": "#3f8f86", "gold_soft": "#6bb3a8",
        "marigold": "#d9a441", "marigold_soft": "#e6bd6e",
        "cover1": "#24363e", "cover2": "#1a2a31", "cover3": "#0e1a1f",
    },
    "plum": {
        "paper": "#faf6f7", "ink": "#241826",
        "maroon": "#5a2352", "maroon_deep": "#3d1537",
        "gold": "#c08a6a", "gold_soft": "#d9a98a",
        "marigold": "#d98a6a", "marigold_soft": "#e8ab8e",
        "cover1": "#6a2a60", "cover2": "#4e1c46", "cover3": "#33102e",
    },
    "terracotta": {
        "paper": "#faf4ec", "ink": "#2a1d15",
        "maroon": "#9c4a2f", "maroon_deep": "#76351f",
        "gold": "#a9762f", "gold_soft": "#c69a5c",
        "marigold": "#cf7a2a", "marigold_soft": "#df9a54",
        "cover1": "#a85a38", "cover2": "#8a4527", "cover3": "#5e2f1a",
    },
    "midnight": {
        "paper": "#f4f4f2", "ink": "#16181a",
        "maroon": "#3a3f45", "maroon_deep": "#23272b",
        "gold": "#8a8f98", "gold_soft": "#b6bbc3",
        "marigold": "#c9a227", "marigold_soft": "#ddbd5a",
        "cover1": "#2b3036", "cover2": "#1f242a", "cover3": "#101317",
    },
}


def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(t):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(v)))) for v in t)


def mix(a, b, t):
    """Blend two hex colours: t=0 -> a, t=1 -> b."""
    ca, cb = _rgb(a), _rgb(b)
    return _hex(tuple(ca[i] + (cb[i] - ca[i]) * t for i in range(3)))


def resolve(name):
    """The full CSS-variable map for a theme, deriving everything not named."""
    t = THEMES.get(name, THEMES[DEFAULT])
    p, ink = t["paper"], t["ink"]
    maroon, gold, gold_soft = t["maroon"], t["gold"], t["gold_soft"]
    return {
        "paper": p,
        "paper-edge": mix(p, ink, 0.06),
        "ink": ink,
        "ink-soft": mix(ink, p, 0.30),
        "ink-faint": mix(ink, p, 0.52),
        "maroon": maroon,
        "maroon-deep": t["maroon_deep"],
        "gold": gold,
        "gold-soft": gold_soft,
        "marigold": t["marigold"],
        "marigold-soft": t["marigold_soft"],
        "rule": mix(p, maroon, 0.16),
        "rule-strong": mix(p, gold, 0.55),
        "zebra": mix(p, maroon, 0.05),
        "page-bg": mix(p, ink, 0.15),
        "watermark": ink,
        "foot": mix(ink, p, 0.55),
        "panel": mix(p, gold, 0.10),
        "panel-2": mix(p, gold, 0.06),
        "th-text": p,
        "mobile-bg": mix(p, ink, 0.07),
        "cover-1": t["cover1"], "cover-2": t["cover2"], "cover-3": t["cover3"],
        "backcover-1": t["cover2"],
        "backcover-2": mix(t["cover2"], ink, 0.25),
        "backcover-3": t["cover3"],
        "on-dark": p,
        "on-dark-title": mix(p, "#ffffff", 0.35),
        "on-dark-sub": mix(p, gold_soft, 0.35),
        "on-dark-author": mix(p, "#ffffff", 0.18),
        "on-dark-gold": gold_soft,
    }


def css_vars(name):
    """A `:root{...}` block that overrides the stylesheet's defaults."""
    v = resolve(name)
    return ":root{%s}" % "".join("--%s:%s;" % (k, val) for k, val in v.items())


def rgb(name, key, fallback="#000000"):
    """An (r, g, b) tuple for python-docx, from a theme variable."""
    return _rgb(resolve(name).get(key, fallback))


def names():
    return list(THEMES)


def pick(meta=None):
    """The theme for a build: BOOK_THEME env wins, then META["theme"], else default."""
    return os.environ.get("BOOK_THEME") or (meta or {}).get("theme") or DEFAULT
