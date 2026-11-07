# -*- coding: utf-8 -*-
"""Export page-exact PDFs from a built eBook HTML.

Colour and grayscale A4 from an A4 master, plus (optionally) a phone-sized PDF
from the reflowable mobile HTML. Grayscale is a CSS `filter: grayscale(1)` pass,
so its text is rendered, not selectable - state this to the user.

Usage:
    BOOK_DIR=/path/to/project python3 pdf_export.py <src.html> <out_base> [<mobile.html> <mobile.pdf>]

Writes <out_base>.pdf and <out_base>_grayscale.pdf (and the mobile PDF) in
BOOK_DIR. Set CHROMIUM to override the browser path.
"""
import os, sys, subprocess

BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
CH = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")


def to_pdf(src, out, extra_style=""):
    s = open(src).read()
    if extra_style:
        s = s.replace("</head>", "<style>%s</style></head>" % extra_style)
    tmp = os.path.join(BOOK, "_pdf_src.html")
    open(tmp, "w").write(s)
    subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=25000",
                    "--print-to-pdf=" + out, "file://" + tmp],
                   capture_output=True, timeout=250)


def pages(path):
    try:
        r = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60)
        for ln in r.stdout.splitlines():
            if ln.startswith("Pages:"):
                return ln
    except Exception:
        pass
    return ""


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return
    src = os.path.join(BOOK, argv[1])
    base = argv[2]
    mobile_html = argv[3] if len(argv) > 3 else None
    mobile_pdf = argv[4] if len(argv) > 4 else None

    colour = os.path.join(BOOK, base + ".pdf")
    gray = os.path.join(BOOK, base + "_grayscale.pdf")
    to_pdf(src, colour)
    to_pdf(src, gray, "html{filter:grayscale(1);}")
    print(base + ".pdf", os.path.getsize(colour), pages(colour))
    print(base + "_grayscale.pdf", os.path.getsize(gray), pages(gray))

    if mobile_html and mobile_pdf:
        mout = os.path.join(BOOK, mobile_pdf)
        to_pdf(os.path.join(BOOK, mobile_html), mout,
               "@page{size:390px 844px;margin:0}*{print-color-adjust:exact;}")
        print(mobile_pdf, os.path.getsize(mout), pages(mout))


if __name__ == "__main__":
    main(sys.argv)
