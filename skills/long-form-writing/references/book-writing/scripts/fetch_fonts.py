# -*- coding: utf-8 -*-
"""Download webfonts from Google Fonts and build a base64-embedded fonts.css."""
import os, re, base64, urllib.request

OUT = os.environ.get("BOOK_DIR", "/scratch/work/book") + "/fonts"
os.makedirs(OUT, exist_ok=True)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")

FAMILIES = [
    "EB+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600",
    "Cinzel:wght@400;500;600;700",
    "Inter:wght@400;500;600",
]

def get(url, ua=UA):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    return urllib.request.urlopen(req, timeout=40).read()

blocks_out = []
for fam in FAMILIES:
    css_url = "https://fonts.googleapis.com/css2?family=%s&display=swap" % fam
    css = get(css_url).decode("utf-8")
    # split into @font-face blocks
    faces = re.findall(r"@font-face\s*\{[^}]*\}", css)
    for face in faces:
        ur = re.search(r"unicode-range:\s*([^;]+);", face)
        # keep ONLY the basic-latin subset (one block per weight/style)
        if ur:
            rng = ur.group(1)
            if not rng.strip().startswith("U+0000-00FF"):
                continue
        m = re.search(r"url\((https://[^)]+\.woff2)\)", face)
        if not m:
            continue
        url = m.group(1)
        data = get(url)
        b64 = base64.b64encode(data).decode("ascii")
        newface = face.replace(url, "data:font/woff2;base64," + b64)
        blocks_out.append(newface)
        print("embedded", fam.split(":")[0], len(data), "bytes")

open(os.path.join(OUT, "fonts.css"), "w").write("\n".join(blocks_out))
print("fonts.css bytes:", os.path.getsize(os.path.join(OUT, "fonts.css")))
