# -*- coding: utf-8 -*-
"""Merge the language editions of a book into one self-contained HTML file with a
language switcher.

Takes the languages and their built files on the command line, so it works for
any book:

    BOOK_DIR=/path/to/project python3 combine_langs.py <slug> <title> \
        en=english.html hi=book_hi.html gu=book_gu.html

The first language listed (after ordering) is shown on load; the rest sit behind
the switcher and #<lang> deep links. The stylesheet is taken once, from the first
file, so it stays byte-identical across languages. Printing hides the switcher.
"""
import os, re, sys

BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")

LABELS = {"en": "English", "hi": "हिन्दी", "gu": "ગુજરાતી", "mr": "मराठी",
          "bn": "বাংলা", "ta": "தமிழ்", "te": "తెలుగు", "kn": "ಕನ್ನಡ",
          "ml": "മലയാളം", "pa": "ਪੰਜਾਬੀ", "or": "ଓଡ଼ିଆ", "as": "অসমীয়া"}
ORDER = ["en", "hi", "gu", "mr", "bn", "ta", "te", "kn", "ml", "pa", "or", "as"]

BAR_CSS = """
.langbar{position:fixed;top:14px;right:14px;z-index:99999;display:flex;gap:4px;
  background:#6e1f2a;padding:5px;border-radius:999px;box-shadow:0 3px 14px rgba(0,0,0,.28);
  font-family:'Inter','Noto Sans Devanagari','Noto Sans Gujarati',sans-serif;}
.langbar button{border:0;background:transparent;color:#f0dcc4;font:inherit;font-size:13px;
  line-height:1;padding:8px 14px;border-radius:999px;cursor:pointer;white-space:nowrap;}
.langbar button:hover{color:#fff;}
.langbar button.on{background:#b8862b;color:#3a1016;font-weight:600;}
.book.lang-hidden{display:none !important;}
@media print{.langbar{display:none !important;}}
"""

SCRIPT = """
(function(){
  var ok = %s;
  var btns = Array.prototype.slice.call(document.querySelectorAll('#langbar button'));
  var books = Array.prototype.slice.call(document.querySelectorAll('.book'));
  function show(l){
    if (ok.indexOf(l) < 0) l = ok[0];
    books.forEach(function(b){ b.classList.toggle('lang-hidden', b.getAttribute('data-lang') !== l); });
    btns.forEach(function(x){ x.classList.toggle('on', x.getAttribute('data-lang') === l); });
    document.documentElement.lang = l;
    try { history.replaceState(null, '', '#' + l); } catch(e){}
  }
  btns.forEach(function(x){ x.addEventListener('click', function(){ show(x.getAttribute('data-lang')); }); });
  var h = (location.hash || '').replace('#','');
  show(ok.indexOf(h) >= 0 ? h : ok[0]);
})();
"""


def style_of(path):
    s = open(path).read()
    return re.search(r'<style>(.*?)</style>', s, re.S).group(1)


def inner_of(path):
    s = open(path).read()
    i = s.find('<div class="book">')
    j = s.rfind('</div></body>')
    return s[i + len('<div class="book">'):j]


def build(slug, title, pairs):
    if not pairs:
        raise SystemExit("no language files given")
    pairs = sorted(pairs, key=lambda p: ORDER.index(p[0]) if p[0] in ORDER else 99)
    codes = [c for c, _ in pairs]
    css = style_of(os.path.join(BOOK, pairs[0][1]))
    parts = ['<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">' % codes[0],
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<title>%s</title>' % title,
             '<style>%s</style><style>%s</style></head><body>' % (css, BAR_CSS)]
    bar = "".join('<button data-lang="%s">%s</button>' % (c, LABELS.get(c, c.upper())) for c in codes)
    parts.append('<div class="langbar" id="langbar" role="group" aria-label="Choose language">%s</div>' % bar)
    for i, (c, path) in enumerate(pairs):
        hid = "" if i == 0 else " lang-hidden"
        parts.append('<div class="book%s" data-lang="%s">%s</div>' % (hid, c, inner_of(os.path.join(BOOK, path))))
    parts.append('<script>%s</script></body></html>' % (SCRIPT % repr(codes)))
    doc = "".join(parts)
    out = os.path.join(BOOK, "%s_-_All_Languages.html" % slug)
    open(out, "w").write(doc)
    print("%s: %s bytes -> %s" % (slug, len(doc), os.path.basename(out)))


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return
    slug, title = argv[1], argv[2]
    pairs = []
    for a in argv[3:]:
        if "=" not in a:
            print("skipping (expected lang=path):", a)
            continue
        lang, path = a.split("=", 1)
        pairs.append((lang.strip(), path.strip()))
    build(slug, title, pairs)


if __name__ == "__main__":
    main(sys.argv)
