# -*- coding: utf-8 -*-
"""Report the real text fill of every A4 sheet (px of content)."""
import os, sys, re, json, html, subprocess
BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
CH = "/usr/local/bin/chromium"
SRC = sys.argv[1]

SCRIPT = ('<script>window.addEventListener("load",function(){var o=[];'
          'document.querySelectorAll(".sheet-a4").forEach(function(s,i){var pc=s.querySelector(".page-content");'
          'if(!pc){o.push({i:i+1,h:0});return;}var bot=0;'
          '[].forEach.call(pc.children,function(c){var cs=getComputedStyle(c);'
          'var b=c.offsetTop+c.offsetHeight+parseFloat(cs.marginBottom||0)+parseFloat(cs.marginTop||0);'
          'if(b>bot)bot=b;});'
          'o.push({i:i+1,h:Math.round(bot)});});'
          'document.documentElement.innerHTML="<body><pre id=\\"out\\">"+JSON.stringify(o)+"</pre></body>";});</script>')

s = open(os.path.join(BOOK, SRC)).read().replace("</body>", SCRIPT + "</body>")
tmp = os.path.join(BOOK, "_fill.html"); open(tmp, "w").write(s)
r = subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--virtual-time-budget=20000", "--dump-dom", "file://" + tmp],
                   capture_output=True, text=True, timeout=250)
d = json.loads(html.unescape(re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S).group(1)))
AVAIL = 966.0
print("pages:", len(d))
print("under-60%-full interior pages:")
for x in d:
    if x["h"] < 0.60 * AVAIL:
        print("  p%-3d %4d px  (%d%%)" % (x["i"], x["h"], round(100 * x["h"] / AVAIL)))
print("min interior fill:", min(x["h"] for x in d[5:] if x["h"] > 0), "px")
