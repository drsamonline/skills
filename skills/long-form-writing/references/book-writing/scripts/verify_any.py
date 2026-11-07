# -*- coding: utf-8 -*-
"""Verify a built book: sheet heights, content overflow, watermark on every page."""
import os, sys, json, re, html, subprocess
from PIL import Image
import glob

BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
CHROMIUM = "/usr/local/bin/chromium"

SCRIPT = ('<script>window.addEventListener("load",function(){var o=[];'
          'document.querySelectorAll(".sheet-a4").forEach(function(s,i){var pc=s.querySelector(".page-content");'
          'o.push({i:i+1,h:Math.round(s.getBoundingClientRect().height),'
          'cvov:pc.scrollHeight-pc.clientHeight,chov:pc.scrollWidth-pc.clientWidth});});'
          'document.documentElement.innerHTML="<body><pre id=\\"out\\">"+JSON.stringify(o)+"</pre></body>";});</script>')

def render(src, out, extra_style=""):
    s = open(src).read()
    if extra_style:
        s = s.replace("</head>", "<style>%s</style></head>" % extra_style)
    s = s.replace("</body>", SCRIPT + "</body>")
    tmp = os.path.join(BOOK, "_v.html"); open(tmp, "w").write(s)
    r = subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--virtual-time-budget=15000", "--dump-dom", "file://" + tmp],
                       capture_output=True, text=True, timeout=200)
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    return json.loads(html.unescape(m.group(1)))

def watermark_count(src):
    s = open(src).read().replace("</head>", '<style>.page-foot .wm{background:#ff0000!important;color:#ff0000!important;border-color:#ff0000!important;}</style></head>')
    tmp = os.path.join(BOOK, "_wm.html"); open(tmp, "w").write(s)
    subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + os.path.join(BOOK, "_wm.pdf"), "--virtual-time-budget=20000",
                    "file://" + tmp], capture_output=True, text=True, timeout=200)
    for f in glob.glob(os.path.join(BOOK, "wm2", "*.png")): os.remove(f)
    os.makedirs(os.path.join(BOOK, "wm2"), exist_ok=True)
    subprocess.run(["pdftoppm", "-png", "-r", "36", os.path.join(BOOK, "_wm.pdf"), os.path.join(BOOK, "wm2", "p")],
                   capture_output=True, timeout=120)
    ok = 0; files = sorted(glob.glob(os.path.join(BOOK, "wm2", "p-*.png")))
    for f in files:
        red = sum(1 for r, g, b in Image.open(f).convert("RGB").getdata() if r > 150 and g < 110 and b < 110)
        if red >= 60: ok += 1
    return len(files), ok

def main(path):
    d = render(path, path)
    print("file:", os.path.basename(path), "| sheets:", len(d))
    print("  max sheet height:", max(x["h"] for x in d))
    print("  v-overflow pages:", [x["i"] for x in d if x["cvov"] > 0])
    print("  h-overflow pages:", [x["i"] for x in d if x["chov"] > 0])
    pages, ok = watermark_count(path)
    print(f"  watermark: {ok}/{pages} pages carry the mark")

for p in sys.argv[1:]:
    main(p)
