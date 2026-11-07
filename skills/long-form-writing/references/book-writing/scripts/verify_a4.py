# -*- coding: utf-8 -*-
"""Verify the A4 build: sheet height, overflow, footer watermark; screenshot pages."""
import os, sys, json, re, html, subprocess, glob
from PIL import Image
BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
CH = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")

SCRIPT = ('<script>window.addEventListener("load",function(){var o=[];'
          'document.querySelectorAll(".sheet-a4").forEach(function(s,i){var pc=s.querySelector(".page-content");'
          'o.push({i:i+1,h:Math.round(s.getBoundingClientRect().height),'
          'cvov:pc.scrollHeight-pc.clientHeight,chov:pc.scrollWidth-pc.clientWidth});});'
          'document.documentElement.innerHTML="<body><pre id=\\"out\\">"+JSON.stringify(o)+"</pre></body>";});</script>')


def run(src, extra=""):
    s = open(src).read()
    if extra:
        s = s.replace("</head>", "<style>%s</style></head>" % extra)
    s = s.replace("</body>", SCRIPT + "</body>")
    tmp = os.path.join(BOOK, "_v.html"); open(tmp, "w").write(s)
    r = subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--virtual-time-budget=20000", "--dump-dom", "file://" + tmp],
                       capture_output=True, text=True, timeout=250)
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    return json.loads(html.unescape(m.group(1)))


def main(path):
    d = run(path)
    print("sheets:", len(d), "| max height:", max(x["h"] for x in d))
    vo = [x["i"] for x in d if x["cvov"] > 1]
    ho = [x["i"] for x in d if x["chov"] > 1]
    print("v-overflow pages:", vo)
    print("h-overflow pages:", ho)
    # watermark check: recolour the footer box red and count its pixels per page
    s = open(path).read().replace("</head>", '<style>.page-foot .wm{background:#ff0000!important;color:#ff0000!important;border-color:#ff0000!important;}</style></head>')
    tmp = os.path.join(BOOK, "_wm.html"); open(tmp, "w").write(s)
    subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + os.path.join(BOOK, "_wm.pdf"), "--virtual-time-budget=30000",
                    "file://" + tmp], capture_output=True, timeout=280)
    os.makedirs(os.path.join(BOOK, "wm"), exist_ok=True)
    for f in glob.glob(os.path.join(BOOK, "wm", "*.png")):
        os.remove(f)
    subprocess.run(["pdftoppm", "-png", "-r", "30", os.path.join(BOOK, "_wm.pdf"), os.path.join(BOOK, "wm", "p")],
                   capture_output=True, timeout=200)
    files = sorted(glob.glob(os.path.join(BOOK, "wm", "p-*.png")))
    ok = 0
    for f in files:
        red = sum(1 for r, g, b in Image.open(f).convert("RGB").getdata() if r > 150 and g < 110 and b < 110)
        if red >= 60:
            ok += 1
    print("watermark: %d/%d pages carry the mark" % (ok, len(files)))


if __name__ == "__main__":
    main(sys.argv[1])
