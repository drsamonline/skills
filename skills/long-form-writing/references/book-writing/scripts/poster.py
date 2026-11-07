# -*- coding: utf-8 -*-
"""One-page A4 poster for any book, rendered from the content module's META.

Reads kicker_line (or kicker), title/title_html, subtitle, quote, quote_source,
blurb (or back_paras) and imprint from the module. Colours come from the theme
(see themes.py), so the poster matches the book.

Usage:
    BOOK_DIR=/path/to/project python3 poster.py <content_module> [<out.pdf>]
"""
import os, sys, subprocess
import booklib, themes

BOOK = booklib.book_dir()
CH = booklib.chromium()
sys.path.insert(0, BOOK)
import ornaments

CSS = (open(os.path.join(BOOK, "fonts/fonts.css")).read() + "\n"
       + open(os.path.join(BOOK, "book.css")).read())

POSTER = """
<style>
  @page{ size:A4; margin:0; }
  .poster{ position:relative; width:793.7px; height:1122.5px; overflow:hidden;
           background:radial-gradient(120%% 90%% at 50%% 0%%, var(--cover-1) 0%%, var(--cover-2) 44%%, var(--cover-3) 100%%);
           color:var(--on-dark); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .poster .orn-frame{ color:var(--gold-soft); }
  .p-inner{ position:relative; z-index:3; height:100%%; display:flex; flex-direction:column;
            align-items:center; justify-content:center; text-align:center; padding:110px 96px; }
  .p-garland{ color:var(--marigold-soft); margin-bottom:14px; }
  .p-kick{ font-family:'Inter',sans-serif; font-size:12px; letter-spacing:.5em; text-transform:uppercase; color:var(--gold-soft); }
  .p-title{ font-family:'Cinzel',serif; font-size:74px; line-height:1.0; letter-spacing:.05em; color:var(--on-dark-title);
            text-transform:uppercase; margin:22px 0 0; }
  .p-sub{ font-family:'EB Garamond',serif; font-style:italic; font-size:26px; color:var(--on-dark-sub); margin-top:16px; }
  .p-rule{ width:170px; height:1px; background:var(--gold-soft); margin:26px auto; opacity:.85; }
  .p-quote{ font-family:'EB Garamond',serif; font-style:italic; font-size:24px; line-height:1.5;
            color:var(--on-dark); max-width:560px; margin:6px auto 0; }
  .p-quote .att{ display:block; font-family:'Inter',sans-serif; font-style:normal; font-size:11px;
                 letter-spacing:.28em; text-transform:uppercase; color:var(--gold-soft); margin-top:16px; }
  .p-blurb{ font-family:'EB Garamond',serif; font-size:17px; line-height:1.62; color:var(--on-dark-sub);
            max-width:540px; margin:26px auto 0; }
  .p-mar{ color:var(--marigold-soft); margin:30px 0 22px; }
  .p-author{ font-family:'Inter',sans-serif; font-size:16px; letter-spacing:.42em; text-transform:uppercase; color:var(--on-dark-author); }
  .p-imprint{ font-family:'Inter',sans-serif; font-size:10px; letter-spacing:.36em; text-transform:uppercase; color:var(--gold-soft); margin-top:14px; }
</style>
<div class="poster">
  %s
  <div class="p-inner">
    <div class="p-garland">%s</div>
    <div class="p-kick">%s</div>
    <h1 class="p-title">%s</h1>
    <div class="p-sub">%s</div>
    <div class="p-rule"></div>
    <div class="p-quote">%s%s</div>
    <div class="p-blurb">%s</div>
    <div class="p-mar">%s</div>
    <div class="p-author">%s</div>
    <div class="p-imprint">%s</div>
  </div>
</div>
"""


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    mod = booklib.load_module(argv[1])
    meta = mod.META
    theme = themes.pick(meta)
    out = argv[2] if len(argv) > 2 else ("%s_-_Poster.pdf" % meta["title"].replace(" ", "_"))

    kick = meta.get("kicker_line") or meta.get("kicker") or "A Book"
    title_html = meta.get("title_html") or meta["title"]
    sub = meta.get("subtitle", "")
    quote = meta.get("quote", "")
    att = meta.get("quote_source", "")
    blurb = meta.get("blurb") or " ".join(meta.get("back_paras", []) or [])
    author = meta.get("author", "")
    imprint = meta.get("imprint", "")

    quote_html = ("&ldquo;%s&rdquo;" % quote) if quote else ""
    att_html = ('<span class="att">%s</span>' % att) if att else ""

    poster = POSTER % (ornaments.corner_frame(), ornaments.marigold_garland(n=11, w=520),
                       kick, title_html, sub, quote_html, att_html, blurb,
                       ornaments.marigold_motif(size=58), author, imprint)
    html = ('<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + CSS + themes.css_vars(theme)
            + '</style></head><body style="margin:0">' + poster + '</body></html>')
    open(os.path.join(BOOK, "_poster.html"), "w").write(html)
    outp = os.path.join(BOOK, out)
    subprocess.run([CH, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=12000", "--print-to-pdf=" + outp,
                    "file://" + os.path.join(BOOK, "_poster.html")], capture_output=True, timeout=200)
    print("poster:", os.path.getsize(outp), "bytes")


if __name__ == "__main__":
    main(sys.argv)
