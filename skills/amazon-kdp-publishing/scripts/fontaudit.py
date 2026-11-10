#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit PDFs for the font problems that get a print file rejected.

    python3 fontaudit.py file.pdf [more.pdf ...] [dir ...]
    python3 fontaudit.py --json file.pdf

Exit code is 0 only when every file is clean. That is deliberate: it makes the
script usable as a gate in a build pipeline.

What it flags, and why:

  Type 3 fonts      The killer. Type 3 glyphs are stored as drawing procedures,
                    not as a real font program. Print engines (KDP, IngramSpark)
                    reject or mangle them. Chromium produces Type 3 whenever it
                    is asked to embed a *variable* font, or a font it cannot
                    subset into a CID font.
  not embedded      The glyphs are not in the file at all; the printer will
                    substitute something.
  Type 1 / Type 3   Older or synthetic formats. Type 1 is acceptable but rare
                    in modern output; Type 3 never is.
"""
from __future__ import annotations
import argparse, json, os, re, subprocess, sys

OK_TYPES = ("CID TrueType", "TrueType", "Type 1C", "CID Type 0C")


def pdf_fonts(path):
    """Return [{name, type, emb, sub}] from pdffonts, or raise."""
    r = subprocess.run(["pdffonts", path], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or "pdffonts failed")
    rows = []
    for line in r.stdout.splitlines()[2:]:
        if not line.strip():
            continue
        # pdffonts columns: name  type  encoding  emb  sub  uni  object ID
        m = re.match(r"^(.*?)\s{2,}(\S.*?)\s{2,}(\S+)\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+(\d+)\s+(\d+)\s*$", line)
        if not m:
            parts = line.split()
            if len(parts) >= 5:
                rows.append({"name": parts[0], "type": " ".join(parts[1:-4]) or "?",
                             "emb": parts[-4], "sub": parts[-3], "raw": line})
            continue
        rows.append({"name": m.group(1).strip(), "type": m.group(2).strip(),
                     "emb": m.group(4), "sub": m.group(5), "raw": line})
    return rows


def classify(rows):
    type3 = [r for r in rows if "Type 3" in r["type"]]
    notemb = [r for r in rows if r["emb"].lower() != "yes"]
    other = [r for r in rows if "Type 3" not in r["type"] and r["emb"].lower() == "yes"
             and not any(t in r["type"] for t in OK_TYPES)]
    return type3, notemb, other


def audit(path, as_json=False):
    rows = pdf_fonts(path)
    type3, notemb, other = classify(rows)
    ok = not type3 and not notemb
    out = {
        "file": path,
        "fonts": len(rows),
        "type3": [{"name": r["name"], "type": r["type"]} for r in type3],
        "not_embedded": [r["name"] for r in notemb],
        "unusual": [{"name": r["name"], "type": r["type"]} for r in other],
        "ok": ok,
    }
    if as_json:
        return out
    print(f"\n{path}")
    print(f"  fonts: {len(rows)}")
    if not rows:
        print("  ! no fonts at all — the page may be images, or the text is outlined")
    if type3:
        print(f"  FAIL  {len(type3)} Type 3 font(s) — print engines reject these:")
        for r in type3[:6]:
            print(f"          {r['name']}  [{r['type']}]")
        if len(type3) > 6:
            print(f"          ... and {len(type3) - 6} more")
    if notemb:
        print(f"  FAIL  {len(notemb)} font(s) not embedded: " + ", ".join(r['name'] for r in notemb[:6]))
    if other:
        print(f"  note  {len(other)} font(s) in an unusual format: "
              + ", ".join(f"{r['name']} [{r['type']}]" for r in other[:4]))
    if ok:
        names = sorted({r["name"].split("+")[-1] for r in rows})
        print(f"  PASS  all embedded, no Type 3 — {', '.join(names[:6])}"
              + (" ..." if len(names) > 6 else ""))
    return out


def gather(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, names in os.walk(p):
                files += [os.path.join(root, n) for n in sorted(names) if n.lower().endswith(".pdf")]
        elif p.lower().endswith(".pdf"):
            files.append(p)
        else:
            print(f"skip (not a PDF): {p}", file=sys.stderr)
    return files


def main():
    ap = argparse.ArgumentParser(description="Audit PDFs for print-unsafe fonts.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    files = gather(a.paths)
    if not files:
        print("no PDFs found", file=sys.stderr)
        return 2

    results = []
    for f in files:
        try:
            results.append(audit(f, as_json=a.json))
        except Exception as e:
            print(f"\n{f}\n  ERROR {type(e).__name__}: {e}")
            results.append({"file": f, "ok": False, "error": str(e)})

    if a.json:
        print(json.dumps(results, indent=2))
    bad = [r for r in results if not r.get("ok")]
    print(f"\n{'=' * 60}\n{len(results)} file(s) checked · {len(bad)} failed")
    if bad:
        print("\nFix: run fontfix.py to install static font instances, then")
        print("     re-render from source with printrender.py.")
        print("     See references/why-type-3-happens.md")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
