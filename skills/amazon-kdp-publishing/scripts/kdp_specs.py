# -*- coding: utf-8 -*-
"""Every Amazon KDP constant and every piece of geometry maths, in one place.

Import this rather than retyping numbers into a build script. If a figure is
wrong here it is wrong everywhere, which is the point — one place to fix.

Verified against KDP's help pages: Print Options (G201834180), Set Trim Size,
Bleed and Margins (GVBQ3CMEQW3W2VL6), Paperback Submission Guidelines
(G201857950), Create a Paperback Cover (G201953020), Create a Hardcover Cover
(GDTKFJPNQCBTMRV6).
"""

from __future__ import annotations

BLEED = 0.125                      # inches, top/bottom/outside only

# --------------------------------------------------------------------------
# Paper: spine thickness per page, and which inks each paper supports
# --------------------------------------------------------------------------
PAPER = {
    "white":      {"thickness": 0.002252, "label": "Black ink, white paper"},
    "cream":      {"thickness": 0.002500, "label": "Black ink, cream paper"},
    "groundwood": {"thickness": 0.002350, "label": "Black ink, groundwood paper"},
    "std_color":  {"thickness": 0.002252, "label": "Standard colour, white paper"},
    "premium_color": {"thickness": 0.002347, "label": "Premium colour, white paper"},
}

# --------------------------------------------------------------------------
# Paperback trims -> page range per paper type.  None = not offered.
# --------------------------------------------------------------------------
PAPERBACK_TRIMS = {
    (5.00, 8.00):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (5.06, 7.81):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (5.25, 8.00):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (5.50, 8.50):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (6.00, 9.00):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (6.14, 9.21):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (6.69, 9.61):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (7.00, 10.00):   {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (7.44, 9.69):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (7.50, 9.25):    {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (8.00, 10.00):   {"white": (24, 828), "cream": (24, 776), "groundwood": (24, 812),
                      "std_color": (72, 600), "premium_color": (24, 828)},
    (8.25, 6.00):    {"white": (24, 800), "cream": (24, 750), "groundwood": (24, 784),
                      "std_color": (72, 600), "premium_color": (24, 800)},
    (8.25, 8.25):    {"white": (24, 800), "cream": (24, 750), "groundwood": (24, 784),
                      "std_color": (72, 600), "premium_color": (24, 800)},
    (8.27, 11.69):   {"white": (24, 780), "cream": (24, 730), "groundwood": (24, 764),
                      "std_color": None, "premium_color": (24, 590)},
    (8.50, 8.50):    {"white": (24, 590), "cream": (24, 550), "groundwood": (24, 578),
                      "std_color": (72, 600), "premium_color": (24, 590)},
    (8.50, 11.00):   {"white": (24, 590), "cream": (24, 550), "groundwood": (24, 578),
                      "std_color": (72, 600), "premium_color": (24, 590)},
}

# --------------------------------------------------------------------------
# Hardcover: five trims only, 75-550 pages on every offered paper
# --------------------------------------------------------------------------
HARDCOVER_TRIMS = [(5.5, 8.5), (6.0, 9.0), (6.14, 9.21), (7.0, 10.0), (8.25, 11.0)]
HARDCOVER_RANGE = (75, 550)
HARDCOVER_PAPERS = ("white", "cream", "premium_color")   # no groundwood, no std colour

# Hardcover case geometry. KDP does not publish a spine formula; these
# constants reproduce KDP's own worked example (6x9, 300pp -> 14.439 x 10.417).
HC_WRAP = 0.591
HC_HINGE = 0.197
HC_OVERHANG = 0.236
HC_BOARD_ALLOWANCE = 0.189

# --------------------------------------------------------------------------
# Margins
# --------------------------------------------------------------------------
def gutter(pages: int) -> float:
    """Minimum inside (gutter) margin in inches for a paperback page count."""
    if pages <= 150:  return 0.375
    if pages <= 300:  return 0.5
    if pages <= 500:  return 0.625
    if pages <= 700:  return 0.75
    if pages <= 828:  return 0.875
    raise ValueError(f"{pages} pages exceeds the 828-page paperback maximum")


def outside_margin(bleed: bool = False) -> float:
    return 0.375 if bleed else 0.25


# A margin set to exactly the minimum fails in practice. Rendering rounds, a
# table can overhang its column by a hair, and KDP measures the ink, not the CSS.
# Add a buffer so the measured margin lands safely above the requirement.
MARGIN_SAFETY = 0.012          # inches


def safe_gutter(pages: int) -> float:
    """Gutter to actually design with: KDP's minimum plus the safety buffer."""
    return round(gutter(pages) + MARGIN_SAFETY, 4)


def safe_outside(bleed: bool = False) -> float:
    return round(outside_margin(bleed) + MARGIN_SAFETY, 4)


SPINE_TEXT_MIN_PAGES = 79
SPINE_TEXT_CLEARANCE = 0.0625
BARCODE_W, BARCODE_H = 2.0, 1.2


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
def page_range(trim, paper: str, binding: str = "paperback"):
    trim = _norm(trim)
    if binding == "hardcover":
        if trim not in HARDCOVER_TRIMS:
            raise ValueError(f"{trim} is not a hardcover trim. Choose one of {HARDCOVER_TRIMS}")
        if paper not in HARDCOVER_PAPERS:
            raise ValueError(f"{paper} is not offered in hardcover. Use one of {HARDCOVER_PAPERS}")
        return HARDCOVER_RANGE
    table = PAPERBACK_TRIMS.get(trim)
    if table is None:
        raise ValueError(f"{trim} is not a standard paperback trim. Custom trims are "
                         f"4-8.5 in wide and 6-11.69 in tall; check the limits yourself.")
    rng = table.get(paper)
    if rng is None:
        raise ValueError(f"{paper} is not offered at {trim} in paperback")
    return rng


def check_pages(trim, paper: str, pages: int, binding: str = "paperback") -> dict:
    """Is this page count publishable at this trim/paper/binding?

    Returns a dict with ok / message / range / alternatives, so a caller can
    print the reason rather than just a boolean.
    """
    lo, hi = page_range(trim, paper, binding)
    ok = lo <= pages <= hi
    out = {"ok": ok, "trim": _norm(trim), "paper": paper, "binding": binding,
           "pages": pages, "range": (lo, hi)}
    if ok:
        out["message"] = f"{pages} pages is inside {lo}-{hi} for {_norm(trim)} {paper} {binding}."
        return out

    out["message"] = (f"{pages} pages is OUTSIDE the {lo}-{hi} range for {_norm(trim)} "
                      f"{paper} {binding}.")
    alts = []
    if binding == "paperback":
        for t, tab in PAPERBACK_TRIMS.items():
            r = tab.get(paper)
            if r and r[0] <= pages <= r[1]:
                alts.append(f"{t[0]}x{t[1]} in ({r[1]} max)")
    out["alternatives"] = alts
    if alts:
        out["message"] += (" Trims that WOULD fit: " + "; ".join(alts) +
                           ". Note that a smaller trim carries more pages, not fewer.")
    return out


def _norm(trim):
    return (round(float(trim[0]), 2), round(float(trim[1]), 2))


# --------------------------------------------------------------------------
# Geometry
# --------------------------------------------------------------------------
def spine_width(pages: int, paper: str) -> float:
    return pages * PAPER[paper]["thickness"]


def paperback_cover(trim, pages: int, paper: str) -> dict:
    """Full paperback spread, back + spine + front, with bleed."""
    w, h = _norm(trim)
    spine = spine_width(pages, paper)
    return {
        "binding": "paperback",
        "spine": round(spine, 4),
        "width": round(BLEED + w + spine + w + BLEED, 4),
        "height": round(BLEED + h + BLEED, 4),
        "bleed": BLEED,
        "trim": (w, h),
        "spine_text_allowed": pages >= SPINE_TEXT_MIN_PAGES,
        "safe_margin": 0.25,
    }


def hardcover_cover(trim, pages: int, paper: str) -> dict:
    """Case-laminate spread: wrap + back + hinge + spine + hinge + front + wrap.

    The spine formula is NOT published by KDP. These constants reproduce KDP's
    published example to within 0.002 in, but confirm against KDP's template
    generator before printing.
    """
    w, h = _norm(trim)
    spine = spine_width(pages, paper) + HC_BOARD_ALLOWANCE
    return {
        "binding": "hardcover",
        "spine": round(spine, 4),
        "width": round(HC_WRAP + w + HC_HINGE + spine + HC_HINGE + w + HC_WRAP, 4),
        "height": round(HC_WRAP + h + HC_OVERHANG + HC_WRAP, 4),
        "trim": (w, h),
        "wrap": HC_WRAP,
        "hinge": HC_HINGE,
        "safe_margin": 0.635,
        "spine_text_allowed": pages >= SPINE_TEXT_MIN_PAGES,
        "approximate_spine": True,
    }


def cover_geometry(trim, pages: int, paper: str, binding: str = "paperback") -> dict:
    if binding == "hardcover":
        return hardcover_cover(trim, pages, paper)
    return paperback_cover(trim, pages, paper)


def interior_page_size(trim, bleed: bool = False) -> tuple:
    """Page size in inches. With bleed: wider by one bleed, taller by two."""
    w, h = _norm(trim)
    if bleed:
        return (round(w + BLEED, 4), round(h + BLEED * 2, 4))
    return (w, h)


def to_points(inches: float) -> float:
    return round(inches * 72, 2)


def to_px(inches: float, dpi: int = 96) -> float:
    return round(inches * dpi, 2)


def report(trim, pages: int, paper: str, binding: str = "paperback") -> str:
    """Human-readable spec block for the package's specification sheet."""
    g = cover_geometry(trim, pages, paper, binding)
    lo, hi = page_range(trim, paper, binding)
    lines = [
        f"Binding            : {binding}",
        f"Trim               : {g['trim'][0]} x {g['trim'][1]} in",
        f"Paper              : {PAPER[paper]['label']}",
        f"Page count         : {pages}  (allowed {lo}-{hi})",
        f"Gutter (inside)    : {gutter(pages)} in, mirrored",
        f"Outside/top/bottom : {outside_margin()} in",
        f"Spine width        : {g['spine']} in ({g['spine'] * 25.4:.1f} mm)"
        + ("  [APPROXIMATE - confirm with KDP template]" if g.get("approximate_spine") else ""),
        f"Cover size         : {g['width']} x {g['height']} in",
        f"  in points        : {to_points(g['width'])} x {to_points(g['height'])} pt",
        f"Spine text allowed : {'yes' if g['spine_text_allowed'] else 'no (needs 79+ pages)'}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    # Self-check against KDP's published worked example.
    ex = hardcover_cover((6, 9), 300, "white")
    assert abs(ex["width"] - 14.439) < 0.01, ex["width"]
    assert abs(ex["height"] - 10.417) < 0.01, ex["height"]
    assert check_pages((8.5, 11), "white", 800)["ok"] is False
    assert check_pages((6, 9), "white", 752)["ok"] is True
    assert gutter(752) == 0.875 and gutter(120) == 0.375
    print("kdp_specs self-check passed")
    print()
    print(report((6, 9), 752, "white", "paperback"))
