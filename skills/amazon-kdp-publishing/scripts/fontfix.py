#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Turn print-unsafe fonts into print-safe static ones, and prepare the CSS.

    # from a stylesheet that carries base64 web fonts
    python3 fontfix.py --css book.css --dest ~/.local/share/fonts

    # from a folder of font files you already have
    python3 fontfix.py --from-dir ./fonts --dest ~/.local/share/fonts

    # a single file
    python3 fontfix.py --from-file EBGaramond.ttf --dest ~/.local/share/fonts

What it does, and why it is needed:

Chromium embeds a *variable* font as **Type 3** in PDF, and print engines reject
Type 3. Pinning the font to a static instance (one fixed weight, no fvar table)
makes Chromium embed it as CID TrueType, which every printer accepts.

It also writes a fontconfig file and a copy of your CSS with the @font-face
blocks removed — the system font must be used, not the web font, or you get
Type 3 again.
"""
from __future__ import annotations
import argparse, base64, io, os, re, shutil, sys

try:
    from fontTools.ttLib import TTFont
except ImportError:
    sys.exit("fontTools is required:  pip install fonttools brotli")

try:
    from fontTools.varLib.instancer import instantiateVariableFont
except ImportError:
    instantiateVariableFont = None

DEFAULT_WEIGHTS = [400, 500, 600, 700]


# ---------------------------------------------------------------- CSS input
def faces_from_css(css_text):
    """Yield (family, style, weight, bytes, is_latin) for each @font-face."""
    for block in re.findall(r"@font-face\s*\{[^}]*\}", css_text):
        fam = re.search(r"font-family:\s*['\"]?([^'\";]+)", block)
        style = re.search(r"font-style:\s*([a-z]+)", block)
        weight = re.search(r"font-weight:\s*(\d+)", block)
        data = re.search(r"base64,([A-Za-z0-9+/=\s]+)", block)
        urange = re.search(r"unicode-range:\s*([^;]+);", block)
        if not (fam and data):
            continue
        is_latin = True
        if urange and "U+0000-00FF" not in urange.group(1):
            is_latin = False          # keep the basic-latin subset only
        raw = base64.b64decode(re.sub(r"\s+", "", data.group(1)))
        yield (fam.group(1).strip(),
               style.group(1) if style else "normal",
               int(weight.group(1)) if weight else 400,
               raw, is_latin)


def strip_font_face(css_text):
    return re.sub(r"@font-face\s*\{[^}]*\}", "", css_text)


# ---------------------------------------------------------------- conversion
def to_static(raw, weight, style):
    """Decode a font, and if it is variable, pin it to one weight."""
    ft = TTFont(io.BytesIO(raw))
    ft.flavor = None
    variable = "fvar" in ft
    if variable:
        if instantiateVariableFont is None:
            raise RuntimeError("fontTools.varLib.instancer unavailable — pip install fonttools")
        ft = instantiateVariableFont(ft, {"wght": weight}, inplace=False, updateFontNames=True)
    return ft, variable


def safe_name(family, style, weight):
    fam = re.sub(r"[^A-Za-z0-9]+", "", family) or "Font"
    return f"{fam}-{style}-{weight}.ttf"


def write_fontconfig(dest, path):
    cfg = f"""<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <dir>{dest}</dir>
  <cachedir>~/.cache/fontconfig</cachedir>
</fontconfig>
"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(cfg)
    return path


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Make fonts print-safe (kill Type 3).")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--css", help="stylesheet containing base64 @font-face rules")
    src.add_argument("--from-dir", help="folder of .ttf/.otf/.woff2/.woff files")
    src.add_argument("--from-file", help="a single font file")
    ap.add_argument("--dest", default=os.path.expanduser("~/.local/share/fonts"))
    ap.add_argument("--conf", default=os.path.expanduser("~/.config/fontconfig/fonts.conf"))
    ap.add_argument("--css-out", help="write the @font-face-stripped CSS here")
    ap.add_argument("--weights", default=",".join(map(str, DEFAULT_WEIGHTS)))
    a = ap.parse_args()

    weights = [int(w) for w in a.weights.split(",") if w.strip()]
    os.makedirs(a.dest, exist_ok=True)
    written, variables = [], 0

    if a.css:
        css = open(a.css, encoding="utf-8").read()
        seen = set()
        for fam, style, weight, raw, latin in faces_from_css(css):
            if not latin:
                continue
            key = (fam, style, weight)
            if key in seen:
                continue
            seen.add(key)
            try:
                ft, was_var = to_static(raw, weight, style)
            except Exception as e:
                print(f"  ! {fam} {style} {weight}: {type(e).__name__}: {e}")
                continue
            variables += 1 if was_var else 0
            out = os.path.join(a.dest, safe_name(fam, style, weight))
            ft.save(out)
            written.append((fam, style, weight, out, was_var))
        stripped = strip_font_face(css)
        css_out = a.css_out or re.sub(r"\.css$", "", a.css) + ".systemfonts.css"
        open(css_out, "w", encoding="utf-8").write(stripped)
        print(f"\nCSS written without @font-face: {css_out}")

    else:
        files = []
        if a.from_dir:
            for n in sorted(os.listdir(a.from_dir)):
                if n.lower().endswith((".ttf", ".otf", ".woff2", ".woff")):
                    files.append(os.path.join(a.from_dir, n))
        else:
            files = [a.from_file]

        for f in files:
            raw = open(f, "rb").read()
            base = re.sub(r"\.(ttf|otf|woff2|woff)$", "", os.path.basename(f), flags=re.I)
            style = "italic" if "italic" in base.lower() or "oblique" in base.lower() else "normal"
            m = re.search(r"(bold|semibold|medium|black|light|\d{3})", base, re.I)
            weight = 700 if (m and "bold" in m.group(1).lower()) else 400
            try:
                ft, was_var = to_static(raw, weight, style)
            except Exception as e:
                print(f"  ! {os.path.basename(f)}: {type(e).__name__}: {e}")
                continue
            variables += 1 if was_var else 0
            out = os.path.join(a.dest, safe_name(base, style, weight))
            ft.save(out)
            written.append((base, style, weight, out, was_var))

    if not written:
        print("\nnothing converted — check the input", file=sys.stderr)
        return 1

    conf = write_fontconfig(a.dest, a.conf)
    print(f"fontconfig written: {conf}")
    print(f"installed {len(written)} font file(s) into {a.dest}"
          f"  ({variables} were variable and have been pinned to a static instance)\n")
    for fam, style, weight, out, was_var in written:
        flag = "  <- was variable" if was_var else ""
        print(f"  {fam} {style} {weight}  ->  {os.path.basename(out)}{flag}")

    print("\nNext, so the render actually uses these and not the web font:")
    print(f"  export FONTCONFIG_FILE={conf}")
    print("  fc-cache -f")
    print(f"  fc-match 'Your Family Name'      # must name your font, not a fallback")
    print("  python3 printrender.py --html book.html --out book.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
