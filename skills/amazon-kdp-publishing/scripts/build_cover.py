# -*- coding: utf-8 -*-
"""Build a full KDP cover spread — paperback or case-laminate hardcover.

One canvas carrying back, spine and front. Geometry comes from kdp_specs, so
the spine always matches the current page count; never type a spine width into
a design by hand.

The design is deliberately restrained: a solid ground, a title block, a blurb
and an author block. Replace the strings in COVER_SPEC, or pass your own dict,
and keep the structure — the zone maths is what makes it print correctly.
"""

from __future__ import annotations
import base64, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kdp_specs as S

CHROMIUM = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")

DEFAULT_SPEC = {
    "title": "Book Title",
    "subtitle": "A subtitle that says what the book is",
    "author": "Author Name",
    "imprint": "",
    "kicker": "A Reference Volume",
    "blurb": ["What the book is, in a few sentences a reader would recognise."],
    "poem": None,                    # list of lines, or None
    "poem_attr": "",
    "author_bio": "",
    "photo": None,                   # path to a jpg/png
    "legal": "",
    "colors": {
        "ground_d": "#073b34", "ground": "#0e6b5c", "ground_l": "#12796a",
        "accent": "#d8b45c", "text": "#f7f1e4", "text_soft": "#e6dcc4",
    },
}


def _b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()


def _css(g, spec):
    c = spec["colors"]
    hc = g["binding"] == "hardcover"
    if hc:
        zones = (f'.wrap{{width:{g["wrap"]}in;}}'
                 f'.back,.front{{width:{g["trim"][0]}in;}}'
                 f'.hinge{{width:{g["hinge"]}in;}}'
                 f'.spine{{width:{g["spine"]}in;}}')
    else:
        zones = (f'.wrap{{width:{g["bleed"]}in;}}'
                 f'.back,.front{{width:{g["trim"][0]}in;}}'
                 f'.hinge{{width:0;}}'
                 f'.spine{{width:{g["spine"]}in;}}')
    safe = g["safe_margin"]
    bleed = g["bleed"]
    band = round(1.2 + safe + bleed + 0.12, 3)   # barcode + clearance
    return f"""
@page {{ size: {g['width']}in {g['height']}in; margin:0; }}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:{g['width']}in;height:{g['height']}in;}}
body{{font-family:'EB Garamond',Georgia,'Times New Roman',serif;
  background:linear-gradient(155deg,{c['ground_d']} 0%,{c['ground']} 46%,{c['ground_l']} 62%,{c['ground_d']} 100%);
  color:{c['text']};}}
.sheet{{display:flex;width:{g['width']}in;height:{g['height']}in;}}
{zones}
.panel{{position:relative;overflow:hidden;}}
.hinge{{background:rgba(0,0,0,0.18);}}

.front .inner{{position:absolute;inset:0;padding:{safe}in;
  display:flex;flex-direction:column;align-items:center;text-align:center;}}
.kicker{{font-size:8.5pt;letter-spacing:.42em;text-transform:uppercase;color:{c['accent']};}}
.rule{{width:1.15in;height:1px;background:{c['accent']};margin:.16in 0;}}
h1{{font-size:40pt;line-height:1.03;font-weight:600;margin-top:.12in;}}
.subtitle{{font-size:14.5pt;font-style:italic;color:{c['text_soft']};margin-top:.2in;line-height:1.35;}}
.front .foot{{margin-top:auto;}}
.author{{font-size:13pt;letter-spacing:.26em;text-transform:uppercase;}}
.imprint{{font-size:8pt;letter-spacing:.34em;text-transform:uppercase;color:{c['accent']};margin-top:.13in;}}

.spine .inner{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;}}
.spine .txt{{transform:rotate(90deg);white-space:nowrap;font-size:10.5pt;
  letter-spacing:.24em;text-transform:uppercase;}}

.back .inner{{position:absolute;inset:0;padding:{safe}in;display:flex;flex-direction:column;}}
.blurb{{font-size:9.7pt;line-height:1.44;color:{c['text_soft']};text-align:justify;margin-bottom:.1in;}}
.blurb strong{{color:{c['text']};}}
.poem{{margin:auto 0;padding:.18in 0;border-top:1px solid {c['accent']}77;
  border-bottom:1px solid {c['accent']}77;text-align:center;}}
.poem .line{{font-size:11.5pt;font-style:italic;line-height:1.6;}}
.poem .attr{{font-size:8.2pt;color:{c['accent']};margin-top:.07in;}}
.authorblock{{display:flex;align-items:center;gap:.22in;}}
.avatar{{width:1.02in;height:1.02in;border-radius:50%;border:1.5px solid {c['accent']};
  object-fit:cover;flex:0 0 auto;}}
.ab-name{{font-size:11.5pt;letter-spacing:.06em;}}
.ab-bio{{font-size:8.2pt;line-height:1.38;color:{c['text_soft']};margin-top:.045in;}}
.legal{{margin-top:.13in;font-size:6.7pt;line-height:1.38;color:{c['text_soft']};opacity:.7;}}
.brand{{margin-top:.08in;font-size:7.5pt;letter-spacing:.3em;text-transform:uppercase;color:{c['accent']};}}
/* KDP places its own barcode in the lower-right of the back cover: a 2 x 1.2 in
   area that must be free of text, images and design elements, and light and
   solid so it scans. Reserve a light band and keep every element out of it. */
.backband{{position:absolute;left:0;right:0;bottom:0;height:{band}in;
  background:{c['text']};z-index:0;}}
.back .inner{{padding-bottom:{band}in;z-index:1;}}
.backlegal{{position:absolute;left:{safe}in;right:{safe + 2.25}in;
  bottom:{bleed + safe}in;font-size:6.7pt;line-height:1.38;
  color:{c['ground_d']};z-index:2;}}
/* the band is light, so anything inside it must be dark — the base .legal and
   .brand colours are chosen for the dark ground and vanish here */
.backlegal .legal{{color:{c['ground_d']};opacity:.82;margin-top:0;}}
.backlegal .brand{{color:{c['ground_d']};opacity:.9;margin-top:.06in;}}
.barcode{{position:absolute;right:{safe}in;bottom:{bleed + safe}in;
  width:2in;height:1.2in;background:{c['text']};z-index:3;}}
"""


def build(spec, trim, pages, paper, binding, out_html, css_extra=""):
    g = S.cover_geometry(trim, pages, paper, binding)
    s = dict(DEFAULT_SPEC); s.update(spec)
    c = s["colors"]

    avatar = ""
    if s.get("photo") and os.path.exists(s["photo"]):
        avatar = f'<img class="avatar" src="data:image/jpeg;base64,{_b64(s["photo"])}" alt="{s["author"]}">'

    blurb = "".join(f'<p class="blurb">{b}</p>' for b in s["blurb"])
    poem = ""
    if s.get("poem"):
        lines = "".join(f'<div class="line">{ln}</div>' for ln in s["poem"])
        attr = f'<div class="attr">{s["poem_attr"]}</div>' if s.get("poem_attr") else ""
        poem = f'<div class="poem">{lines}{attr}</div>'

    authorblock = ""
    if avatar or s.get("author_bio"):
        authorblock = (f'<div class="authorblock">{avatar}<div>'
                       f'<div class="ab-name">{s["author"]}</div>'
                       f'<div class="ab-bio">{s.get("author_bio","")}</div></div></div>')

    legal = f'<div class="legal">{s["legal"]}</div>' if s.get("legal") else ""
    brand = f'<div class="brand">{s["imprint"]}</div>' if s.get("imprint") else ""
    hinge = '<div class="hinge"></div>' if binding == "hardcover" else ""

    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>{_css(g, s)}{css_extra}</style></head><body><div class="sheet">
  <div class="panel wrap"></div>
  <div class="panel back">
    <div class="backband"></div>
    <div class="inner">
      {blurb}{poem}{authorblock}
    </div>
    <div class="backlegal">{legal}{brand}</div>
    <div class="barcode"></div>
  </div>
  {hinge}
  <div class="panel spine"><div class="inner">
    <div class="txt">{s['title']}{' · ' + s['author'] if s['author'] else ''}</div>
  </div></div>
  {hinge}
  <div class="panel front"><div class="inner">
    <div class="kicker">{s['kicker']}</div><div class="rule"></div>
    <h1>{s['title']}</h1>
    <div class="subtitle">{s['subtitle']}</div>
    <div class="foot">
      <div class="author">{s['author']}</div>
      <div class="imprint">{s['imprint']}</div>
    </div>
  </div></div>
  <div class="panel wrap"></div>
</div></body></html>"""
    with open(out_html, "w", encoding="utf-8") as fh:
        fh.write(html)
    return g


def render(out_html, out_pdf, timeout=200):
    subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=20000",
                    "--print-to-pdf=" + out_pdf, "file://" + os.path.abspath(out_html)],
                   capture_output=True, timeout=timeout)
    return out_pdf
