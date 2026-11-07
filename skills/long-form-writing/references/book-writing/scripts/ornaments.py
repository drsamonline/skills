# -*- coding: utf-8 -*-
"""Ornamental SVG library for *Life Is a Comedy*.

Design language: a theatrical memoir. Deep burgundy ground, warm gold rules,
ivory paper, and a marigold-orange accent (the book's central image — the
wrong-coloured garlands). Ornaments: scrolling vines, inscriptional "runes"
used as scene dividers, and a marigold motif.

Everything is inline SVG so it embeds in HTML, PDF and DOCX alike.
"""
import math

# Themed ornament colours. A builder calls set_palette() from the chosen theme
# so borders, rules and vines match the rest of the book.
PALETTE = {"rule": "#cbb98f", "accent": "#dd8a1c", "vine": "#b8862b"}


def set_palette(colours):
    """Override the ornament palette from a theme's resolved colours."""
    for k in ("rule", "accent", "vine"):
        if colours.get(k):
            PALETTE[k] = colours[k]


# ---------------------------------------------------------------- helpers

def _polars(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))


def marigold(cx, cy, r, colour="currentColor", petals=12, inner=7):
    """A ruffled marigold bloom drawn as two rings of petals + a centre."""
    out = ['<g fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round">' % (colour, max(1.15, r * 0.08))]
    # outer ring
    for i in range(petals):
        a = 360.0 / petals * i
        x1, y1 = _polars(cx, cy, r * 0.42, a)
        x2, y2 = _polars(cx, cy, r, a)
        px, py = _polars(cx, cy, r * 0.72, a + 360.0 / petals / 2)
        out.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f"/>' % (x1, y1, px, py, x2, y2))
    # inner ring
    for i in range(inner):
        a = 360.0 / inner * i + 12
        x1, y1 = _polars(cx, cy, r * 0.18, a)
        x2, y2 = _polars(cx, cy, r * 0.52, a)
        px, py = _polars(cx, cy, r * 0.36, a + 360.0 / inner / 2)
        out.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f"/>' % (x1, y1, px, py, x2, y2))
    out.append('<circle cx="%.1f" cy="%.1f" r="%.1f"/>' % (cx, cy, r * 0.14))
    out.append('</g>')
    return "".join(out)


def vine_corner(colour="currentColor", w=1.5):
    """Top-left corner scroll. Mirror/rotate for the other three corners."""
    return (
        '<g fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round">'
        '<path d="M2 88 C2 46 10 20 32 8 C52 -2 72 1 88 5"/>'
        '<path d="M18 72 C28 68 34 60 36 50 C37 44 41 40 47 38"/>'
        '<path d="M30 40 C40 38 48 30 50 20"/>'
        '<path d="M8 58 C14 54 18 47 18 39"/>'
        '</g>'
        '<g fill="%s">'
        # leaves
        '<path d="M36 50 c-7 -1 -12 -7 -12 -14 c8 0 14 6 14 14 z"/>'
        '<path d="M50 20 c-6 -2 -10 -8 -9 -15 c7 1 12 7 11 15 z"/>'
        '<path d="M18 39 c-6 0 -11 -5 -11 -12 c6 0 11 5 11 12 z"/>'
        # berry cluster
        '<circle cx="66" cy="6" r="2.1"/><circle cx="73" cy="9" r="1.7"/>'
        '<circle cx="60" cy="3" r="1.5"/>'
        '</g>' % (colour, w, colour)
    )


def corner_frame(inset=26, arm=96, colour="currentColor", w=1.2):
    """Four vine corners placed for a box of the given inset (viewBox 0 0 793.7 1122.5)."""
    W, H = 793.7, 1122.5
    def g(cx, cy, rot):
        return ('<g transform="translate(%.1f %.1f) rotate(%d)" '
                'transform-origin="0 0">%s</g>' % (cx, cy, rot, vine_corner(colour, w)))
    # vine_corner draws in a 90x90 box anchored at its top-left (0,0).
    parts = []
    parts.append(g(inset, inset, 0))                                   # top-left
    parts.append('<g transform="translate(%.1f %.1f) scale(-1 1)">%s</g>' % (W - inset, inset, vine_corner(colour, w)))   # top-right
    parts.append('<g transform="translate(%.1f %.1f) scale(-1 -1)">%s</g>' % (W - inset, H - inset, vine_corner(colour, w)))  # bottom-right
    parts.append('<g transform="translate(%.1f %.1f) scale(1 -1)">%s</g>' % (inset, H - inset, vine_corner(colour, w)))       # bottom-left
    return ('<svg class="orn orn-frame" viewBox="0 0 %.1f %.1f" xmlns="http://www.w3.org/2000/svg" '
            'preserveAspectRatio="none" aria-hidden="true">%s</svg>' % (W, H, "".join(parts)))


# ---------------------------------------------------------------- runes

# Each rune is a list of stroke sub-paths in a 16 x 24 box.
RUNES = [
    ["M8 2 V22", "M8 9 L15 4", "M8 15 L15 20"],            # ᚲ-like
    ["M3 22 L8 2 L13 22", "M5 15 H11"],                     # ᛗ-like
    ["M4 4 H12", "M8 4 V22", "M8 13 L13 8"],                # ᚨ-like
    ["M5 2 V22", "M5 2 L13 10 L5 14", "M5 14 L13 22"],      # ᛒ-like
    ["M4 22 L8 2 L12 22", "M8 2 V22"],                      # ᛉ-like
    ["M5 2 V22", "M11 2 V22", "M5 12 L11 12"],              # ᚼ-like
    ["M4 2 L12 22", "M12 2 L4 22"],                         # ᚷ-like
    ["M8 2 V22", "M3 2 L8 9 L13 2"],                        # ᛏ-like
]


def rune_glyph(idx, size=24, colour="currentColor", w=1.5, flip=False):
    strokes = RUNES[idx % len(RUNES)]
    body = "".join('<path d="%s"/>' % s for s in strokes)
    tr = ' transform="scale(-1,1) translate(-16,0)"' if flip else ''
    return ('<svg class="orn orn-rune" viewBox="0 0 16 24" width="%.1f" height="%.1f" '
            'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<g%s fill="none" stroke="%s" stroke-width="%.2f" stroke-linecap="round" '
            'stroke-linejoin="round">%s</g></svg>'
            % (size * 16 / 24.0, size, tr, colour, w, body))


def sprig(colour="currentColor", w=1.1, flip=False):
    """A short vine sprig with a leaf-pair and a curling tip."""
    body = ('<g fill="none" stroke="%s" stroke-width="%.2f" stroke-linecap="round">'
            '<path d="M2 9 H56"/>'
            '<path d="M56 9 c6 -6 14 -6 18 0 c-6 6 -14 6 -18 0"/>'
            '<ellipse cx="24" cy="5.5" rx="7.5" ry="3.1" transform="rotate(-18 24 5.5)"/>'
            '<ellipse cx="40" cy="12.5" rx="7.5" ry="3.1" transform="rotate(18 40 12.5)"/>'
            '</g>' % (colour, w))
    tr = ' transform="scale(-1,1) translate(-80,0)"' if flip else ''
    return ('<svg class="orn orn-sprig" viewBox="0 0 80 18" width="80" height="18" '
            'xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g%s>%s</g></svg>' % (tr, body))


def rune_divider(colour="currentColor"):
    """A symmetric ornamental scene-break: vine sprigs, mirrored runes, and a
    marigold at the centre — clearly decorative, never reading as a word."""
    return ('<div class="rune-divider" aria-hidden="true">'
            + sprig(colour, flip=True)
            + rune_glyph(2, size=15, colour=colour, w=1.3, flip=True)
            + '<span class="orn-diamond"></span>'
            + marigold_motif(colour, size=32)
            + '<span class="orn-diamond"></span>'
            + rune_glyph(2, size=15, colour=colour, w=1.3)
            + sprig(colour)
            + '</div>')


def rune_medallion(num_text, size=74, colour="currentColor"):
    """Chapter number set inside a ring of runes — the chapter opener mark."""
    r = size / 2.0
    ticks = []
    for i in range(len(RUNES)):
        a = 360.0 / len(RUNES) * i - 90
        x1, y1 = _polars(r, r, r - 3, a)
        x2, y2 = _polars(r, r, r - 9, a)
        ticks.append('<path d="M%.1f %.1f L%.1f %.1f"/>' % (x1, y1, x2, y2))
    return (
        '<svg class="orn orn-medallion" viewBox="0 0 %d %d" width="%d" height="%d" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<g fill="none" stroke="%s" stroke-width="1.4" stroke-linecap="round">'
        '<circle cx="%.1f" cy="%.1f" r="%.1f"/>'
        '<circle cx="%.1f" cy="%.1f" r="%.1f" stroke-width="0.8"/>%s</g>'
        '<text x="%.1f" y="%.1f" text-anchor="middle" dominant-baseline="central" '
        'font-family="Cinzel, serif" font-size="%.1f" fill="%s">%s</text></svg>'
        % (size, size, size, size, colour, r, r, r - 1.5, r, r, r - 6.5, "".join(ticks),
           r, r + 1, size * 0.42, colour, num_text)
    )


def rule_flourish(colour="currentColor"):
    """A short centred flourish rule used under titles and heads."""
    return (
        '<svg class="orn orn-flourish" viewBox="0 0 220 24" width="220" height="24" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<g fill="none" stroke="%s" stroke-width="1.2" stroke-linecap="round">'
        '<path d="M6 12 H86"/>'
        '<path d="M134 12 H214"/>'
        '<path d="M96 12 C100 6 106 6 110 12 C114 18 120 18 124 12"/>'
        '<path d="M86 12 C90 9 92 9 94 12"/>'
        '<path d="M126 12 C128 15 130 15 134 12"/>'
        '</g>'
        '<g fill="%s"><circle cx="110" cy="12" r="2.4"/></g></svg>' % (colour, colour)
    )


def marigold_garland(colour="currentColor", n=9, w=560):
    """An arched garland of marigolds — the cover's crown."""
    h = 96
    parts = ['<svg class="orn orn-garland" viewBox="0 0 %d %d" width="%d" height="%d" '
             'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' % (w, h, w, h)]
    # arc
    parts.append('<path d="M20 %d C20 30 %d 30 %d %d" fill="none" stroke="%s" '
                 'stroke-width="1" opacity="0.55"/>' % (h - 14, w - 20, w - 20, h - 14, colour))
    for i in range(n):
        t = (i + 0.5) / n
        # quadratic bezier point on the arc
        x0, y0, cx, cy, x1, y1 = 20, h - 14, w / 2.0, 30 - (h - 44), w - 20, h - 14
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1
        rr = 11 if i % 2 == 0 else 8
        parts.append(marigold(x, y, rr, colour, petals=10, inner=6))
    parts.append('</svg>')
    return "".join(parts)


def marigold_motif(colour="currentColor", size=64):
    return ('<svg class="orn orn-marigold" viewBox="0 0 100 100" width="%d" height="%d" '
            'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">%s</svg>'
            % (size, size, marigold(50, 50, 44, colour, petals=14, inner=8)))


def monogram(initials="SM", colour="currentColor", size=120):
    """A rune-framed monogram for the title page / cover."""
    return (
        '<svg class="orn orn-monogram" viewBox="0 0 140 140" width="%d" height="%d" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<g fill="none" stroke="%s" stroke-width="1.3">'
        '<circle cx="70" cy="70" r="60"/><circle cx="70" cy="70" r="54" stroke-width="0.7"/>'
        '<path d="M70 4 V16 M70 124 V136 M4 70 H16 M124 70 H136"/>'
        '<path d="M24 24 L32 32 M116 24 L108 32 M24 116 L32 108 M116 116 L108 108"/>'
        '</g>'
        '<text x="70" y="80" text-anchor="middle" font-family="Cinzel, serif" '
        'font-size="46" letter-spacing="2" fill="%s">%s</text></svg>'
        % (size, size, colour, colour, initials)
    )


def page_border(opener=False, rule=None, accent=None, vine=None):
    """Overlay SVG for the interior page border: a fine double rule on every
    page, plus vine corners and edge diamonds on part/chapter openers."""
    rule = rule or PALETTE["rule"]
    accent = accent or PALETTE["accent"]
    vine = vine or PALETTE["vine"]
    W, H = 793.7, 1122.5
    m, m2 = 30.0, 36.0
    p = ['<svg class="orn orn-border" viewBox="0 0 %.1f %.1f" xmlns="http://www.w3.org/2000/svg" '
         'preserveAspectRatio="none" aria-hidden="true">' % (W, H)]
    p.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="%s" stroke-width="1.1"/>'
             % (m, m, W - 2 * m, H - 2 * m, rule))
    p.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="%s" stroke-width="0.6"/>'
             % (m2, m2, W - 2 * m2, H - 2 * m2, accent))
    # edge midpoint diamonds
    for (dx, dy) in [(W / 2, m), (W / 2, H - m), (m, H / 2), (W - m, H / 2)]:
        p.append('<rect x="%.1f" y="%.1f" width="5" height="5" transform="rotate(45 %.1f %.1f)" fill="%s"/>'
                 % (dx - 2.5, dy - 2.5, dx, dy, accent))
    if opener:
        s = 0.6
        p.append('<g transform="translate(%.1f %.1f) scale(%.2f %.2f)">%s</g>' % (m2, m2, s, s, vine_corner(vine, 1.6)))
        p.append('<g transform="translate(%.1f %.1f) scale(%.2f %.2f)">%s</g>' % (W - m2, m2, -s, s, vine_corner(vine, 1.6)))
        p.append('<g transform="translate(%.1f %.1f) scale(%.2f %.2f)">%s</g>' % (W - m2, H - m2, -s, -s, vine_corner(vine, 1.6)))
        p.append('<g transform="translate(%.1f %.1f) scale(%.2f %.2f)">%s</g>' % (m2, H - m2, s, -s, vine_corner(vine, 1.6)))
    p.append('</svg>')
    return "".join(p)


# Convenience: the full-bleed corner frame used on cover and part-openers.
FRAME = corner_frame()
