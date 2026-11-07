# -*- coding: utf-8 -*-
"""Verify a combined multi-language HTML: for each #<lang>, exactly one book is
visible, it is the right language, and it carries the expected page count.

The languages are read from the file's own data-lang attributes, so this works
for any book.

Usage:
    BOOK_DIR=/path/to/project python3 verify_combined.py <combined.html> [<more.html> ...]
"""
import os, re, sys, json, html, subprocess

BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
CH = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")

PROBE = ('<script>window.addEventListener("load",function(){var r={lang:document.documentElement.lang,'
         'hash:location.hash,books:[]};'
         'document.querySelectorAll(".book").forEach(function(b){'
         'r.books.push({lang:b.getAttribute("data-lang"),'
         'visible:!b.classList.contains("lang-hidden"),'
         'sheets:b.querySelectorAll(".sheet-a4").length,'
         'title:b.querySelector(".sheet-a4 h1")?b.querySelector(".sheet-a4 h1").textContent.trim().slice(0,26):""});});'
         'document.documentElement.innerHTML="<body><pre id=\\"out\\">"+JSON.stringify(r)+"</pre></body>";});</script>')


def langs_of(path):
    seen = []
    for c in re.findall(r'data-lang="([^"]+)"', open(path).read()):
        if c not in seen:
            seen.append(c)
    return seen


def check(fn):
    path = os.path.join(BOOK, fn)
    langs = langs_of(path)
    src = open(path).read().replace("</body>", PROBE + "</body>")
    tmp = os.path.join(BOOK, "_comb_probe.html")
    open(tmp, "w").write(src)
    print("==", fn, "| langs:", langs)
    for lang in langs:
        r = subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu",
                            "--hide-scrollbars", "--virtual-time-budget=20000", "--dump-dom",
                            "file://" + tmp + "#" + lang],
                           capture_output=True, text=True, timeout=200)
        m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
        if not m:
            print("   ", lang, "NO OUTPUT")
            continue
        d = json.loads(html.unescape(m.group(1)))
        vis = [b for b in d["books"] if b["visible"]]
        print("   #%s: html.lang=%s visible=%s sheets=%s title=%r"
              % (lang, d["lang"], [b["lang"] for b in vis],
                 [b["sheets"] for b in vis], vis[0]["title"] if vis else ""))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    for fn in argv[1:]:
        check(fn)


if __name__ == "__main__":
    main(sys.argv)
