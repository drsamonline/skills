#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render an HTML master to PDF with the print-safe fonts, then prove it.

    python3 printrender.py --html book.html --out book.pdf
    python3 printrender.py --html book.html --out book.pdf --conf ~/.config/fontconfig/fonts.conf

It refuses to hand back a file that contains Type 3 fonts. Chromium exits 0 even
when it writes a broken PDF, so the only trustworthy signal is to read the file
back and inspect its fonts — which is what this does before it exits.
"""
from __future__ import annotations
import argparse, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROMIUM = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")


def run(html, out, conf=None, budget=40000, chromium=CHROMIUM):
    env = dict(os.environ)
    if conf:
        env["FONTCONFIG_FILE"] = os.path.expanduser(conf)

    if os.path.exists(out):
        os.remove(out)

    cmd = [chromium, "--headless=new", "--no-sandbox", "--disable-gpu",
           "--no-pdf-header-footer", f"--virtual-time-budget={budget}",
           f"--print-to-pdf={os.path.abspath(out)}", "file://" + os.path.abspath(html)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=280, env=env)

    if not os.path.exists(out) or os.path.getsize(out) < 2000:
        raise RuntimeError(
            "Chromium produced no usable PDF.\n"
            "  A relative file:// URL is the usual cause — paths are made absolute here,\n"
            "  so check the HTML path exists and the page renders in a browser.\n"
            + (r.stderr or "")[:500])

    info = {}
    p = subprocess.run(["pdfinfo", out], capture_output=True, text=True)
    for line in p.stdout.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            info[k.strip()] = v.strip()
    return info


def verify(pdf):
    """Run the auditor as a gate. Returns (ok, output)."""
    r = subprocess.run([sys.executable, os.path.join(HERE, "fontaudit.py"), pdf],
                       capture_output=True, text=True)
    return r.returncode == 0, r.stdout


def main():
    ap = argparse.ArgumentParser(description="Render HTML to a print-safe PDF.")
    ap.add_argument("--html", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--conf", default=os.path.expanduser("~/.config/fontconfig/fonts.conf"))
    ap.add_argument("--budget", type=int, default=40000)
    ap.add_argument("--allow-type3", action="store_true",
                    help="render anyway and warn (do not use for a print upload)")
    a = ap.parse_args()

    print(f"rendering {a.html} -> {a.out}")
    info = run(a.html, a.out, conf=a.conf, budget=a.budget)
    print(f"  pages    : {info.get('Pages', '?')}")
    print(f"  page size: {info.get('Page size', '?')}")
    print(f"  size     : {os.path.getsize(a.out) // 1024} KB")

    ok, report = verify(a.out)
    print(report)
    if not ok and not a.allow_type3:
        print("REFUSING to pass this file: it contains Type 3 or unembedded fonts.")
        print("Run fontfix.py first, export FONTCONFIG_FILE, then render again.")
        return 1
    if not ok:
        print("WARNING: Type 3 fonts present. Do not upload this to a print service.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
