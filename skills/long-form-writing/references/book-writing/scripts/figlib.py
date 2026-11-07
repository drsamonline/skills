# -*- coding: utf-8 -*-
"""Reusable inline-SVG diagram builders for book figures.

Figures are the part of a book that most often comes out too small or unreadable:
a hand-drawn SVG with a big viewBox and tiny type renders as a faint scribble.
Everything here is built to a fixed canvas so figures always come out large and
legible:

  * the canvas is 640 units wide (about the width of the A4 text column), so one
    unit is roughly one pixel at print size - draw at the real size;
  * type is never smaller than MIN_FONT (14 units) and strokes never thinner
    than MIN_STROKE (1.6), so nothing fades at print scale;
  * every figure is a bare ``<svg viewBox=...>`` string, ready to drop into a
    content module's FIGURES map.

Builders: flowchart, tree, cycle, timeline, matrix, compare, bars, line, and the
low-level node()/arrow()/text() pieces.

Sketches. Call ``set_style("sketch")`` (or pass ``sketch=True`` to a builder) and
every line, box and axis is drawn with a hand-drawn wobble in pencil grey, so the
diagrams read as sketched rather than drafted. The wobble is deterministic (the
same figure looks the same every run) and is pure geometry, so it rasterises
cleanly for the DOCX. Type stays crisp - only the strokes are rough - so
legibility is not sacrificed.

Usage:
    import figlib, themes
    figlib.set_style("sketch")                 # hand-drawn look for this book
    FIGURES = {
        "__FIG_LOOP__": figlib.flowchart(["Notice the cue", "Name the story",
                                          "Choose one move", "Repeat"],
                                         pal_=themes.resolve("sage"),
                                         title="The change loop"),
    }
"""
import math, re

# --- canvas + legibility minimums -------------------------------------------
W = 640           # default canvas width, ~ the A4 text column
MIN_FONT = 14     # smallest type, in canvas units
MIN_STROKE = 1.6  # thinnest stroke

PALETTE = {
    "paper": "#fbf7f0", "panel": "#f7f1e4", "panel2": "#faf4e8",
    "rule": "#cbb98f", "ink": "#241c14", "soft": "#4b4034",
    "accent": "#6e1f2a", "accent2": "#b8862b", "ondark": "#f7efe1",
}
FONT = "'EB Garamond', Georgia, 'Noto Sans Devanagari', serif"
LABEL_FONT = "'Inter', Arial, 'Noto Sans Devanagari', sans-serif"

SKETCH = False        # module style; set_style() flips it
PENCIL = "#3f3f3f"    # graphite grey used for sketch strokes


def set_style(style="clean", pencil=None):
    """Style every figure drawn after this call: "clean" or "sketch"."""
    global SKETCH, PENCIL
    SKETCH = (str(style).lower() == "sketch")
    if pencil:
        PENCIL = pencil
    return SKETCH


def pal(p=None):
    d = dict(PALETTE)
    if p:
        d["accent"] = p.get("accent") or p.get("maroon") or d["accent"]
        d["accent2"] = p.get("accent2") or p.get("gold") or d["accent2"]
        d["paper"] = p.get("paper") or d["paper"]
        d["panel"] = p.get("panel") or d["panel"]
        d["panel2"] = p.get("panel2") or p.get("panel-2") or d["panel2"]
        d["rule"] = p.get("rule") or p.get("rule-strong") or d["rule"]
        d["ink"] = p.get("ink") or d["ink"]
        d["soft"] = p.get("soft") or p.get("ink-soft") or d["soft"]
    return d


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _wrap(text, width):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines or [""]


# --- deterministic wobble ----------------------------------------------------

def _h(x, y, s=0):
    """A stable pseudo-random value in 0..1 from a coordinate (no RNG state)."""
    n = math.sin(x * 12.9898 + y * 78.233 + s * 37.719) * 43758.5453
    return n - math.floor(n)


def _rough_path(x1, y1, x2, y2, amp, s):
    """A wobbly open path from (x1,y1) to (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    n = max(2, int(L / 16))
    px, py = -dy / L, dx / L
    pts = []
    for i in range(n + 1):
        t = i / n
        x, y = x1 + dx * t, y1 + dy * t
        o = (_h(x, y, s) - 0.5) * 2 * amp
        pts.append((x + px * o, y + py * o))
    return "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])


def _line(x1, y1, x2, y2, color=None, w=None, pal_=None, amp=1.6, s=0, dashed=False):
    P = pal_ or PALETTE
    if SKETCH:
        c = color or PENCIL
        ww = max(1.3, w or 1.4)
        dash = ' stroke-dasharray="7 5"' if dashed else ""
        return ('<path d="%s" fill="none" stroke="%s" stroke-width="%.2f" '
                'stroke-linecap="round"%s/>' % (_rough_path(x1, y1, x2, y2, amp, s), c, ww, dash))
    c = color or P["rule"]
    ww = max(MIN_STROKE, w or MIN_STROKE)
    dash = ' stroke-dasharray="6 5"' if dashed else ""
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.2f"%s/>'
            % (x1, y1, x2, y2, c, ww, dash))


def _rect(x, y, w, h, fill=None, stroke=None, pal_=None, radius=0, s=0):
    P = pal_ or PALETTE
    if SKETCH:
        stroke = stroke or PENCIL
        corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        d = ""
        for i in range(4):
            a, b = corners[i], corners[(i + 1) % 4]
            d += _rough_path(a[0], a[1], b[0], b[1], 1.5, s + i)
        out = ['<path d="%s" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>'
               % (d, fill or "none", stroke)]
        if fill:
            out.append('<path d="%s" fill="none" stroke="%s" stroke-width="0.9" opacity="0.35" '
                       'transform="translate(1.3,1.5)"/>' % (d, stroke))
        return "".join(out)
    fill = fill or "none"
    stroke = stroke or P["rule"]
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" ry="%d" '
            'fill="%s" stroke="%s" stroke-width="%.2f"/>'
            % (x, y, w, h, radius, radius, fill, stroke, MIN_STROKE))


# --- low-level pieces --------------------------------------------------------

def text(x, y, s, size=MIN_FONT, color=None, anchor="middle", bold=False,
         font=None, italic=False, pal_=None):
    c = color or (pal_ or PALETTE)["ink"]
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" '
            'font-weight="%s" font-style="%s" fill="%s" text-anchor="%s" '
            'dominant-baseline="middle">%s</text>'
            % (x, y, font or FONT, max(MIN_FONT, size), "600" if bold else "400",
               "italic" if italic else "normal", c, anchor, esc(s)))


def node(x, y, w, h, label, fill=None, stroke=None, color=None, size=16,
         bold=False, pal_=None, radius=9, sketch=None):
    P = pal_ or PALETTE
    global SKETCH
    was = SKETCH
    if sketch is not None:
        SKETCH = sketch
    try:
        out = [_rect(x, y, w, h, fill=fill or P["panel"], stroke=stroke, pal_=P,
                     radius=radius, s=x + y)]
    finally:
        SKETCH = was
    lines = _wrap(label, max(6, int(w / (size * 0.52))))
    lh = size * 1.25
    cy = y + h / 2 - (len(lines) - 1) * lh / 2
    for i, ln in enumerate(lines):
        out.append(text(x + w / 2, cy + i * lh, ln, size=size, color=color or P["ink"], bold=bold, pal_=P))
    return "".join(out)


def arrow(x1, y1, x2, y2, color=None, pal_=None, head=8.0, width=None, sketch=None):
    P = pal_ or PALETTE
    global SKETCH
    was = SKETCH
    if sketch is not None:
        SKETCH = sketch
    try:
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
        out = [_line(x1, y1, bx, by, color=color, w=width, pal_=P, s=x1 + y1)]
        if SKETCH:
            c = color or PENCIL
            for da in (-0.5, 0.5):
                hx = x2 - head * math.cos(ang + da); hy = y2 - head * math.sin(ang + da)
                out.append(_line(x2, y2, hx, hy, color=c, w=1.4, pal_=P, amp=0.8, s=x2 + hy))
        else:
            c = color or P["rule"]
            left = (x2 - head * math.cos(ang - 0.5), y2 - head * math.sin(ang - 0.5))
            right = (x2 - head * math.cos(ang + 0.5), y2 - head * math.sin(ang + 0.5))
            out.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
                       % (x2, y2, left[0], left[1], right[0], right[1], c))
        return "".join(out)
    finally:
        SKETCH = was


def wrap(body, w=W, h=360, cls="fig-svg", bg=None, pal_=None):
    P = pal_ or PALETTE
    bgrect = ('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (w, h, bg)) if bg else ""
    return ('<svg class="%s" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'preserveAspectRatio="xMidYMid meet" role="img">%s%s</svg>'
            % (cls, w, h, bgrect, body))


def block(key, caption="", cls="fig"):
    """A figure block for a content module, wrapping the FIGURES placeholder."""
    cap = ('<figcaption>%s</figcaption>' % esc(caption)) if caption else ""
    return '<figure class="%s">%s%s</figure>' % (cls, key, cap)


# --- high-level diagrams ----------------------------------------------------

def flowchart(steps, w=W, vertical=True, pal_=None, title=None):
    P = pal(pal_)
    n = len(steps)
    if vertical:
        bw, bh, gap = int(w * 0.62), 54, 26
        x = (w - bw) / 2
        top = 34 if title else 14
        h = top + n * bh + (n - 1) * gap + 14
        out = []
        if title:
            out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
        for i, s in enumerate(steps):
            y = top + i * (bh + gap)
            out.append(node(x, y, bw, bh, s, fill=P["panel2"] if i % 2 else P["panel"], pal_=P))
            if i < n - 1:
                out.append(arrow(x + bw / 2, y + bh, x + bw / 2, y + bh + gap, pal_=P))
        return wrap("".join(out), w=w, h=int(h), pal_=P)
    bw, bh = int((w - 24 - (n - 1) * 26) / n), 66
    top = 40 if title else 16
    h = top + bh + 24
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    for i, s in enumerate(steps):
        x = 12 + i * (bw + 26)
        out.append(node(x, top, bw, bh, s, fill=P["panel"] if i % 2 else P["panel2"], pal_=P, size=15))
        if i < n - 1:
            out.append(arrow(x + bw, top + bh / 2, x + bw + 26, top + bh / 2, pal_=P))
    return wrap("".join(out), w=w, h=int(h), pal_=P)


def tree(root, branches, w=W, pal_=None, title=None):
    P = pal(pal_)
    top = 40 if title else 16
    rw, rh = int(w * 0.5), 48
    rx = (w - rw) / 2
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    out.append(node(rx, top, rw, rh, root, fill=P["accent"], color=P["ondark"], stroke=P["accent"], pal_=P))
    n = len(branches)
    lw, lh = int((w - 20 - (n - 1) * 12) / n), 46
    ly = top + rh + 70
    for i, b in enumerate(branches):
        lx = 10 + i * (lw + 12)
        cx = lx + lw / 2
        out.append(arrow(rx + rw / 2, top + rh, cx, ly, pal_=P))
        label = b if isinstance(b, str) else b[0]
        out.append(node(lx, ly, lw, lh, label, fill=P["panel"], pal_=P, size=15))
    return wrap("".join(out), w=w, h=int(ly + lh + 18), pal_=P)


def cycle(steps, w=W, pal_=None, title=None):
    P = pal(pal_)
    cx, cy, R = w / 2, (150 if title else 140), 108
    bw, bh = 150, 50
    n = len(steps)
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    pos = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    for i in range(n):
        x1, y1 = pos[i]; x2, y2 = pos[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        out.append(arrow(x1 + dx / L * (bh * 0.62), y1 + dy / L * (bh * 0.62),
                         x2 - dx / L * (bh * 0.62), y2 - dy / L * (bh * 0.62), pal_=P))
    for i, s in enumerate(steps):
        x, y = pos[i]
        out.append(node(x - bw / 2, y - bh / 2, bw, bh, s, fill=P["panel"], pal_=P, size=15))
    return wrap("".join(out), w=w, h=int(cy + R + bh), pal_=P)


def timeline(items, w=W, pal_=None, title=None):
    P = pal(pal_)
    top = 46 if title else 24
    axis_y = top + 34
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    out.append(_line(16, axis_y, w - 16, axis_y, pal_=P, w=2.0, s=axis_y))
    n = len(items)
    step = (w - 40) / max(1, n - 1)
    for i, (when, what) in enumerate(items):
        x = 20 + i * step
        out.append('<circle cx="%.1f" cy="%d" r="5" fill="%s"/>' % (x, axis_y, P["accent2"]))
        out.append(text(x, axis_y - 18, when, size=14, bold=True, color=P["accent"], pal_=P))
        for j, ln in enumerate(_wrap(what, 16)):
            out.append(text(x, axis_y + 20 + j * 17, ln, size=14, color=P["soft"], pal_=P))
    return wrap("".join(out), w=w, h=int(axis_y + 74), pal_=P)


def matrix(xlab, ylab, quads, w=W, pal_=None, title=None):
    P = pal(pal_)
    top = 46 if title else 22
    gw, gh = int(w * 0.66), 260
    gx, gy = (w - gw) / 2, top + 16
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    labels = quads + ["", "", "", ""]
    cells = [(gx + gw / 2, gy, gw / 2, gh / 2, 0), (gx, gy, gw / 2, gh / 2, 1),
             (gx, gy + gh / 2, gw / 2, gh / 2, 2), (gx + gw / 2, gy + gh / 2, gw / 2, gh / 2, 3)]
    fills = [P["panel2"], P["panel"], P["panel"], P["panel2"]]
    for (cx, cy, cw, ch, idx) in cells:
        out.append(_rect(cx, cy, cw, ch, fill=fills[idx], pal_=P, s=cx + cy))
        out.append(text(cx + cw / 2, cy + ch / 2, labels[idx], size=15, color=P["ink"], pal_=P))
    out.append(text(gx + gw / 2, gy + gh + 20, xlab, size=15, bold=True, color=P["accent"], pal_=P))
    out.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="15" font-weight="600" fill="%s" '
               'text-anchor="middle" transform="rotate(-90 %.1f %.1f)">%s</text>'
               % (gx - 28, gy + gh / 2, LABEL_FONT, P["accent"], gx - 28, gy + gh / 2, esc(ylab)))
    return wrap("".join(out), w=w, h=int(gy + gh + 34), pal_=P)


def compare(cols, rows, w=W, pal_=None, title=None):
    P = pal(pal_)
    top = 44 if title else 16
    n = len(cols)
    cw = (w - 20) / n
    rh = 42
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    out.append(_rect(10, top, w - 20, rh, fill=P["accent"], stroke=P["accent"], pal_=P, s=top))
    for j, c in enumerate(cols):
        out.append(text(10 + j * cw + cw / 2, top + rh / 2, c, size=15, bold=True, color=P["ondark"], pal_=P))
    y = top + rh
    for i, row in enumerate(rows):
        fill = P["panel2"] if i % 2 else P["paper"]
        out.append(_rect(10, y, w - 20, rh, fill=fill, pal_=P, s=y))
        for j, cell in enumerate(row[:n]):
            out.append(text(10 + j * cw + cw / 2, y + rh / 2, cell, size=14, color=P["ink"], pal_=P))
        y += rh
    return wrap("".join(out), w=w, h=int(y + 10), pal_=P)


def bars(data, w=W, pal_=None, title=None, unit=""):
    P = pal(pal_)
    top = 46 if title else 24
    base = top + 210
    n = len(data)
    bw = min(70, int((w - 40) / max(1, n) * 0.6))
    step = (w - 40) / max(1, n)
    vmax = max([v for _, v in data] + [1])
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    out.append(_line(20, base, w - 20, base, pal_=P, w=2.0, s=base))
    for i, (lab, val) in enumerate(data):
        x = 20 + i * step + (step - bw) / 2
        h = max(4, (base - top - 30) * val / vmax)
        out.append(_rect(x, base - h, bw, h, fill=P["accent2"] if i % 2 else P["accent"],
                         stroke=P["ink"], pal_=P, radius=4, s=x))
        out.append(text(x + bw / 2, base - h - 12, "%s%s" % (val, unit), size=14, bold=True, color=P["ink"], pal_=P))
        for j, ln in enumerate(_wrap(lab, 12)):
            out.append(text(x + bw / 2, base + 16 + j * 16, ln, size=14, color=P["soft"], pal_=P))
    return wrap("".join(out), w=w, h=int(base + 50), pal_=P)


def line(points, w=W, pal_=None, title=None, ylab=""):
    P = pal(pal_)
    top = 46 if title else 24
    base = top + 200
    n = len(points)
    x0, x1 = 40, w - 24
    vmax = max([v for _, v in points] + [1])
    out = []
    if title:
        out.append(text(w / 2, 18, title, size=17, bold=True, color=P["accent"], pal_=P))
    out.append(_line(x0, top + 10, x0, base, pal_=P, s=top))
    out.append(_line(x0, base, x1, base, pal_=P, s=base))
    step = (x1 - x0) / max(1, n - 1)
    pts = []
    for i, (lab, val) in enumerate(points):
        x = x0 + i * step
        y = base - (base - top - 20) * val / vmax
        pts.append((x, y))
        out.append(text(x, base + 16, lab, size=14, color=P["soft"], pal_=P))
    if SKETCH:
        d = "M%.1f %.1f " % pts[0] + " ".join("L%.1f %.1f" % p for p in pts[1:])
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round"/>'
                   % (d, P["accent"]))
    else:
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6"/>'
                   % (" ".join("%.1f,%.1f" % p for p in pts), P["accent"]))
    for x, y in pts:
        out.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (x, y, P["accent2"]))
    if ylab:
        out.append(text(x0 - 6, top + 4, ylab, size=14, bold=True, color=P["accent"], anchor="start", pal_=P))
    return wrap("".join(out), w=w, h=int(base + 34), pal_=P)


def audit(svg):
    """Return a list of legibility problems with a figure SVG (empty = fine)."""
    probs = []
    if "viewBox" not in svg:
        probs.append("no viewBox (fixed width/height will render small)")
    fonts = [float(x) for x in re.findall(r'font-size="([\d.]+)"', svg)]
    small = [f for f in fonts if f < MIN_FONT]
    if small:
        probs.append("font-size below %d: %s" % (MIN_FONT, sorted(set(small))))
    head = svg.split("viewBox")[0]
    if re.search(r'\bwidth="\d+"', head):
        probs.append("fixed width/height on the <svg> (use viewBox only)")
    return probs
