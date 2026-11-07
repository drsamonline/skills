# -*- coding: utf-8 -*-
"""Design-motif library for books.

A book's design should not be limited to vines, runes and sigils. This module
collects emblem families so any chapter can carry a distinct, on-theme mark:

  * emblems  - eye, loop, spiral, seed, mask, vortex, vesica, compass, lantern,
               peak, lyre, plus a large cover emblem
  * celestial- sun, moon, star, orbit, constellation
  * botanical- leaf, seedpod, fern, blossom
  * geometric- rings, chevron, fan, sunburst, grid
  * line     - flourish, wave, knot, drop-cap initial frame

Every motif is a bare ``<svg viewBox=...>`` string drawn with **explicit palette
colours** (never ``currentColor``), so it rasterises in colour for the DOCX and
EPUB as well as rendering inline in HTML/PDF. Type/stroke minimums are kept so a
motif stays legible at 70-100 px.

Usage:
    import motifs
    FIGURES = {"__FIG_SIGIL_CH1__": motifs.render("loop"),
               "__FIG_SIGIL_CH2__": motifs.render("spiral", colour="#0e6b76")}
    # in a chapter opener:
    #   <span class="chapter-sigil">__FIG_SIGIL_CH1__</span>

Or list what is available:
    motifs.families()   # {"emblems": [...], "celestial": [...], ...}
"""
import math

# Default palette (the "lagoon" teal). Override with set_palette() or per call.
PAL = {
    "primary": "#0e6b76", "deep": "#084a53", "light": "#6fbcc4",
    "pale": "#b7e0e5", "ink": "#0f313a", "accent": "#d9a24b",
    "paper": "#eef7f9",
}


def set_palette(**kw):
    """Override one or more palette colours for every motif drawn after this."""
    PAL.update({k: v for k, v in kw.items() if v})
    return PAL


def _c(name):
    return PAL.get(name, name)


def _svg(body, size=160, cls="sigil-svg"):
    return ('<svg class="%s" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'preserveAspectRatio="xMidYMid meet" role="img" aria-hidden="true">%s</svg>'
            % (cls, size, size, body))


def _ring(cx, cy, r, colour, w=2.4, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    return ('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
            % (cx, cy, r, colour, w, d))


def _diamond(cx, cy, s, fill):
    return ('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="%s"/>'
            % (cx, cy - s, cx + s, cy, cx, cy + s, cx - s, cy, fill))


def _rays(cx, cy, r1, r2, n, colour, w=2.2, rot=0.0):
    out = []
    for i in range(n):
        a = rot + 2 * math.pi * i / n
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"/>'
                   % (cx + r1 * math.cos(a), cy + r1 * math.sin(a),
                      cx + r2 * math.cos(a), cy + r2 * math.sin(a), colour, w))
    return "".join(out)


def _spiral(cx, cy, rmax, turns, colour, w=2.6, step=0.14, squash=0.92):
    pts, t = [], 0.0
    while t <= turns * 2 * math.pi:
        r = 3 + (rmax - 3) * (t / (turns * 2 * math.pi))
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t) * squash))
        t += step
    d = "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"/>' % (d, colour, w)


# --- emblems ---------------------------------------------------------------

def eye():
    b = [_ring(80, 80, 74, _c("light"), 1.6), _ring(80, 80, 66, _c("primary"), 1.6, "2 7"),
         '<path d="M18 80 Q80 30 142 80 Q80 130 18 80 Z" fill="%s" stroke="%s" stroke-width="2.6"/>' % (_c("paper"), _c("primary")),
         _ring(80, 80, 22, _c("primary"), 2.2), '<circle cx="80" cy="80" r="8" fill="%s"/>' % _c("deep")]
    for x, y in ((80, 15), (145, 80), (80, 145), (15, 80)):
        b.append(_diamond(x, y, 6, _c("accent")))
    return _svg("".join(b))


def loop():
    b = [_ring(80, 80, 74, _c("light"), 1.6), _ring(80, 80, 58, _c("primary"), 1.6, "2 7"),
         '<path d="M80 22 A58 58 0 1 1 33 110" fill="none" stroke="%s" stroke-width="3.4" stroke-linecap="round"/>' % _c("primary"),
         '<circle cx="80" cy="22" r="7" fill="%s"/>' % _c("accent")]
    for i in range(12):
        a = 2 * math.pi * i / 12
        b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
                 % (80 + 50 * math.cos(a), 80 + 50 * math.sin(a), 80 + 56 * math.cos(a), 80 + 56 * math.sin(a), _c("pale")))
    b.append('<circle cx="80" cy="80" r="7" fill="%s"/>' % _c("deep"))
    return _svg("".join(b))


def spiral():
    return _svg(_ring(80, 80, 74, _c("light"), 1.6) + _spiral(80, 80, 62, 3.0, _c("primary"), 2.8)
                + '<circle cx="80" cy="80" r="6" fill="%s"/>' % _c("deep"))


def seed():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M80 128 C56 106 56 68 80 44 C104 68 104 106 80 128 Z" fill="%s" stroke="%s" stroke-width="2.6"/>' % (_c("paper"), _c("primary")),
         '<line x1="80" y1="52" x2="80" y2="124" stroke="%s" stroke-width="1.8"/>' % _c("accent"),
         _rays(80, 80, 30, 40, 5, _c("light"), 1.8, -1.5708)]
    return _svg("".join(b))


def mask():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M80 26 C46 26 36 52 38 80 C40 106 60 122 80 134 C100 122 120 106 122 80 C124 52 114 26 80 26 Z" fill="%s" stroke="%s" stroke-width="2.6"/>' % (_c("paper"), _c("primary")),
         '<path d="M52 74 Q64 64 76 74 Q64 84 52 74 Z" fill="none" stroke="%s" stroke-width="2.2"/>' % _c("deep"),
         '<path d="M84 74 Q96 64 108 74 Q96 84 84 74 Z" fill="none" stroke="%s" stroke-width="2.2"/>' % _c("deep"),
         '<path d="M66 104 Q80 112 94 104" fill="none" stroke="%s" stroke-width="2"/>' % _c("primary")]
    return _svg("".join(b))


def vortex():
    return _svg(_ring(80, 80, 74, _c("light"), 1.6) + _spiral(80, 80, 66, 4.2, _c("primary"), 2.6, 0.12)
                + '<circle cx="80" cy="80" r="6" fill="%s"/>' % _c("deep")
                + '<path d="M40 122 Q60 114 80 122 T120 122" fill="none" stroke="%s" stroke-width="2" opacity="0.8"/>' % _c("pale"))


def vesica():
    b = [_ring(80, 80, 74, _c("light"), 1.6), _ring(62, 80, 44, _c("primary"), 2.4),
         _ring(98, 80, 44, _c("primary"), 2.4),
         '<polygon points="80,48 98,80 80,112 62,80" fill="%s" stroke="%s" stroke-width="2"/>' % (_c("paper"), _c("accent")),
         '<circle cx="62" cy="80" r="5" fill="%s"/>' % _c("deep"), '<circle cx="98" cy="80" r="5" fill="%s"/>' % _c("deep")]
    return _svg("".join(b))


def compass():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<polygon points="80,22 138,80 80,138 22,80" fill="none" stroke="%s" stroke-width="2.2"/>' % _c("primary"),
         '<polygon points="121,39 121,121 39,121 39,39" fill="none" stroke="%s" stroke-width="2.2"/>' % _c("primary"),
         '<circle cx="80" cy="80" r="7" fill="%s"/>' % _c("deep"), _diamond(80, 22, 6, _c("accent"))]
    return _svg("".join(b))


def lantern():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M66 40 Q80 28 94 40" fill="none" stroke="%s" stroke-width="2.4"/>' % _c("primary"),
         '<path d="M58 54 Q80 38 102 54 L110 118 L50 118 Z" fill="%s" stroke="%s" stroke-width="2.6"/>' % (_c("paper"), _c("primary")),
         '<line x1="48" y1="118" x2="112" y2="118" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % _c("primary"),
         '<path d="M80 68 C72 80 74 92 80 98 C86 92 88 80 80 68 Z" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_c("accent"), _c("accent")),
         _rays(80, 84, 18, 26, 4, _c("pale"), 1.6, -1.5708)]
    return _svg("".join(b))


def peak():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M20 116 L60 58 L84 92 L106 62 L140 116" fill="none" stroke="%s" stroke-width="2.8" stroke-linejoin="round"/>' % _c("primary"),
         _ring(112, 48, 13, _c("accent"), 2.2),
         '<path d="M44 44 l7 -6 l7 6" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % _c("deep"),
         '<path d="M60 36 l6 -5 l6 5" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % _c("deep"),
         '<line x1="24" y1="116" x2="136" y2="116" stroke="%s" stroke-width="2.4" stroke-linecap="round"/>' % _c("primary")]
    return _svg("".join(b))


def lyre():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M56 42 C38 72 40 104 58 122" fill="none" stroke="%s" stroke-width="2.8" stroke-linecap="round"/>' % _c("primary"),
         '<path d="M104 42 C122 72 120 104 102 122" fill="none" stroke="%s" stroke-width="2.8" stroke-linecap="round"/>' % _c("primary"),
         '<line x1="56" y1="42" x2="104" y2="42" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>' % _c("primary"),
         '<line x1="58" y1="122" x2="102" y2="122" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>' % _c("primary")]
    for x in (68, 80, 92):
        b.append('<line x1="%d" y1="46" x2="%d" y2="118" stroke="%s" stroke-width="1.6"/>' % (x, x, _c("pale")))
    b.append('<circle cx="80" cy="82" r="5" fill="%s"/>' % _c("accent"))
    return _svg("".join(b))


def cover():
    b = [_ring(120, 120, 112, _c("light"), 1.8), _ring(120, 120, 101, _c("primary"), 1.6, "3 8"),
         _ring(120, 120, 74, _c("primary"), 2.2), _rays(120, 120, 78, 96, 12, _c("accent"), 2.2),
         '<path d="M52 120 Q86 100 120 120 T188 120" fill="none" stroke="%s" stroke-width="2.6" opacity="0.9"/>' % _c("light"),
         _ring(120, 120, 30, _c("accent"), 2.4), '<circle cx="120" cy="120" r="10" fill="%s"/>' % _c("deep")]
    for x, y in ((120, 12), (228, 120), (120, 228), (12, 120)):
        b.append(_diamond(x, y, 8, _c("accent")))
    return _svg("".join(b), size=240, cls="sigil-svg cover-sigil-svg")


# --- celestial -------------------------------------------------------------

def sun():
    b = [_ring(80, 80, 74, _c("light"), 1.6), _ring(80, 80, 30, _c("accent"), 2.6),
         _rays(80, 80, 38, 66, 16, _c("primary"), 2.4)]
    return _svg("".join(b))


def moon():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M100 30 A54 54 0 1 0 100 130 A44 44 0 1 1 100 30 Z" fill="%s" stroke="%s" stroke-width="2.4"/>' % (_c("paper"), _c("primary")),
         _diamond(120, 50, 6, _c("accent"))]
    return _svg("".join(b))


def star():
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = 60 if i % 2 == 0 else 26
        pts.append("%.1f,%.1f" % (80 + r * math.cos(a), 80 + r * math.sin(a)))
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<polygon points="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>' % (" ".join(pts), _c("primary")),
         '<circle cx="80" cy="80" r="7" fill="%s"/>' % _c("accent")]
    return _svg("".join(b))


def orbit():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<ellipse cx="80" cy="80" rx="62" ry="30" fill="none" stroke="%s" stroke-width="2.2"/>' % _c("primary"),
         '<ellipse cx="80" cy="80" rx="30" ry="62" fill="none" stroke="%s" stroke-width="2.2"/>' % _c("primary"),
         _ring(80, 80, 10, _c("accent"), 2.4), '<circle cx="142" cy="80" r="6" fill="%s"/>' % _c("deep")]
    return _svg("".join(b))


def constellation():
    pts = [(44, 52), (70, 78), (96, 44), (118, 74), (92, 108), (58, 116)]
    b = [_ring(80, 80, 74, _c("light"), 1.6)]
    for i in range(len(pts) - 1):
        b.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.6" stroke-dasharray="3 5"/>'
                 % (pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], _c("pale")))
    for i, (x, y) in enumerate(pts):
        b.append('<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (x, y, 6 if i % 2 == 0 else 4, _c("primary") if i % 2 == 0 else _c("accent")))
    return _svg("".join(b))


# --- botanical -------------------------------------------------------------

def leaf():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M80 128 C46 108 40 60 80 30 C120 60 114 108 80 128 Z" fill="%s" stroke="%s" stroke-width="2.6"/>' % (_c("paper"), _c("primary")),
         '<path d="M80 34 L80 124" stroke="%s" stroke-width="2"/>' % _c("accent")]
    for y in (56, 76, 96):
        b.append('<path d="M80 %d Q62 %d 56 %d" fill="none" stroke="%s" stroke-width="1.6"/>' % (y, y + 6, y + 14, _c("light")))
        b.append('<path d="M80 %d Q98 %d 104 %d" fill="none" stroke="%s" stroke-width="1.6"/>' % (y, y + 6, y + 14, _c("light")))
    return _svg("".join(b))


def blossom():
    petals = []
    for i in range(6):
        a = 2 * math.pi * i / 6 - math.pi / 2
        petals.append('<ellipse cx="%.1f" cy="%.1f" rx="18" ry="30" fill="%s" stroke="%s" stroke-width="1.8" '
                      'transform="rotate(%.0f %.1f %.1f)"/>'
                      % (80, 52, _c("paper"), _c("primary"), math.degrees(a) + 90, 80, 52))
    b = [_ring(80, 80, 74, _c("light"), 1.6)] + petals + [_ring(80, 80, 14, _c("accent"), 2.6),
         '<circle cx="80" cy="80" r="5" fill="%s"/>' % _c("deep")]
    return _svg("".join(b))


# --- geometric / art-deco --------------------------------------------------

def rings():
    b = [_ring(80, 80, 72, _c("primary"), 3), _ring(80, 80, 54, _c("accent"), 2.4),
         _ring(80, 80, 36, _c("primary"), 2), _ring(80, 80, 18, _c("accent"), 1.8),
         '<circle cx="80" cy="80" r="6" fill="%s"/>' % _c("deep")]
    return _svg("".join(b))


def chevron():
    b = [_ring(80, 80, 74, _c("light"), 1.6)]
    for i, y in enumerate((44, 64, 84, 104)):
        col = _c("primary") if i % 2 == 0 else _c("accent")
        b.append('<path d="M34 %d L80 %d L126 %d" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                 % (y, y - 16, y, col))
    return _svg("".join(b))


def fan():
    b = [_ring(80, 118, 62, _c("light"), 1.6)]
    for i in range(7):
        a = math.pi + i * math.pi / 6
        b.append('<line x1="80" y1="118" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>'
                 % (80 + 62 * math.cos(a), 118 + 62 * math.sin(a), _c("primary") if i % 2 == 0 else _c("accent")))
    for r in (24, 44):
        b.append('<path d="M%.1f %.1f A%d %d 0 0 1 %.1f %.1f" fill="none" stroke="%s" stroke-width="1.8"/>'
                 % (80 - r, 118, r, r, 80 + r, 118, _c("light")))
    return _svg("".join(b))


def sunburst():
    b = [_ring(80, 80, 74, _c("light"), 1.6), _ring(80, 80, 24, _c("accent"), 2.6)]
    for i in range(24):
        a = 2 * math.pi * i / 24
        r1 = 34 if i % 2 == 0 else 40
        b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"/>'
                 % (80 + r1 * math.cos(a), 80 + r1 * math.sin(a), 80 + 70 * math.cos(a), 80 + 70 * math.sin(a),
                    _c("primary"), 2.4 if i % 2 == 0 else 1.6))
    return _svg("".join(b))


# --- line / calligraphic ---------------------------------------------------

def flourish():
    return ('<svg class="flourish-svg" viewBox="0 0 280 40" xmlns="http://www.w3.org/2000/svg" '
            'preserveAspectRatio="xMidYMid meet" role="img" aria-hidden="true">'
            '<path d="M20 20 C60 8 100 32 140 20 C180 8 220 32 260 20" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"/>'
            '<circle cx="140" cy="20" r="5" fill="%s"/></svg>' % (_c("primary"), _c("accent")))


def wave():
    b = [_ring(80, 80, 74, _c("light"), 1.6)]
    for i, y in enumerate((56, 80, 104)):
        col = _c("primary") if i % 2 == 0 else _c("accent")
        b.append('<path d="M28 %d Q54 %d 80 %d T132 %d" fill="none" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>'
                 % (y, y - 16, y, y, col))
    return _svg("".join(b))


def knot():
    b = [_ring(80, 80, 74, _c("light"), 1.6),
         '<path d="M80 30 C120 30 130 70 100 80 C70 90 60 130 100 130" fill="none" stroke="%s" stroke-width="2.6"/>' % _c("primary"),
         '<path d="M80 130 C40 130 30 90 60 80 C90 70 100 30 60 30" fill="none" stroke="%s" stroke-width="2.6"/>' % _c("accent"),
         '<circle cx="80" cy="80" r="6" fill="%s"/>' % _c("deep")]
    return _svg("".join(b))


# --- registry --------------------------------------------------------------

MOTIFS = {
    "eye": eye, "loop": loop, "spiral": spiral, "seed": seed, "mask": mask,
    "vortex": vortex, "vesica": vesica, "compass": compass, "lantern": lantern,
    "peak": peak, "lyre": lyre, "cover": cover,
    "sun": sun, "moon": moon, "star": star, "orbit": orbit, "constellation": constellation,
    "leaf": leaf, "blossom": blossom,
    "rings": rings, "chevron": chevron, "fan": fan, "sunburst": sunburst,
    "flourish": flourish, "wave": wave, "knot": knot,
}

FAMILY = {
    "emblems": ["eye", "loop", "spiral", "seed", "mask", "vortex", "vesica", "compass", "lantern", "peak", "lyre", "cover"],
    "celestial": ["sun", "moon", "star", "orbit", "constellation"],
    "botanical": ["leaf", "blossom"],
    "geometric": ["rings", "chevron", "fan", "sunburst"],
    "line": ["flourish", "wave", "knot"],
}


def families():
    return dict(FAMILY)


def render(key):
    return MOTIFS[key]()


def block(key, caption="", cls="sigil"):
    """A small inline block that a content module can reference as a placeholder."""
    return '<figure class="%s">%s</figure>' % (cls, key)
