# -*- coding: utf-8 -*-
"""Shared helpers for the book toolchain.

Every tool reads the project folder from BOOK_DIR and the browser from CHROMIUM,
and takes everything book-specific from the content module. That is what lets
the same scripts build any book in any language.

The content module is the single source of truth. It exposes:

  META        dict  - title, subtitle, title_html, kicker, word, num, imprint,
                      dedication, foreword_head, foreword_pre, foreword_post,
                      back_paras, lang; optionally blurb, quote, quote_source,
                      kicker_line, author, series.
  INTRO       dict  - {"key", "title", "kicker", "num", "kind", "blocks": [...]}
  CHAPTERS    list  - of the same shape
  CLOSING     dict  - the same shape
  GLOSSARY    list  - [(term, definition), ...]
  BIBLIOGRAPHY list - [ref, ...]
  INDEX_TERMS list  - [(term, [section-key, ...]), ...]
  POEM        dict  - the same shape as a section
  FIGURES     dict  - optional: {"__FIG_NAME__": "<svg ...>", ...}
  L10N        dict  - optional: per-language labels for the designed DOCX

Figure placeholders look like __FIG_SOMETHING__ inside a block; the builder
substitutes the matching SVG from FIGURES. The rasteriser writes each figure to
<lang>_<something>.png, the name make_docx_designed.py looks for.
"""
import os, re, sys, base64, importlib


def book_dir():
    return os.environ.get("BOOK_DIR", "/scratch/work/book")


def chromium():
    return os.environ.get("CHROMIUM", "/usr/local/bin/chromium")


def _on_path(book):
    if book not in sys.path:
        sys.path.insert(0, book)


def load_module(name, book=None):
    """Import a content module (or any module) from the project folder."""
    _on_path(book or book_dir())
    return importlib.import_module(name)


def load_kit(lang):
    """Import the language kit: `bookkit_<lang>`, falling back to `bookkit`."""
    _on_path(book_dir())
    for name in ("bookkit_%s" % lang, "bookkit"):
        try:
            return importlib.import_module(name)
        except ImportError:
            continue
    raise ImportError("no bookkit module (bookkit_%s / bookkit) in %s" % (lang, book_dir()))


def module_lang(mod):
    return (getattr(mod, "META", {}) or {}).get("lang", "en")


def figures(mod):
    """The placeholder -> SVG map a module exposes ({} when it exposes none)."""
    return dict(getattr(mod, "FIGURES", {}) or {})


def sub_figs(block, figmap):
    """Substitute the first figure placeholder found in a block."""
    for key, svg in figmap.items():
        if key in block:
            return block.replace(key, svg)
    return block


def fig_name(lang, key):
    """PNG filename for a figure placeholder: __FIG_CONDITIONING_CYCLE__ ->
    en_conditioning_cycle.png."""
    k = re.sub(r"^__FIG_", "", key)
    k = re.sub(r"__$", "", k)
    k = re.sub(r"[^a-z0-9]+", "_", k.lower()).strip("_")
    return "%s_%s.png" % (lang, k or "figure")


def labels(mod, defaults):
    """Merge a module's optional L10N dict over a set of default labels."""
    g = dict(defaults)
    g.update(getattr(mod, "L10N", {}) or {})
    return g


# --- author-supplied images (scanned sketches, photographs) -----------------

_MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
         "webp": "image/webp", "gif": "image/gif", "svg": "image/svg+xml"}


def data_uri(path, book=None):
    """Base64-embed an image file so the built HTML stays self-contained."""
    p = path if os.path.isabs(path) else os.path.join(book or book_dir(), path)
    ext = os.path.splitext(p)[1].lower().lstrip(".")
    mime = _MIME.get(ext, "image/png")
    with open(p, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


def inline_images(html, book=None):
    """Replace relative <img src> paths with data URIs (skip data/http)."""
    def repl(m):
        src = m.group(1)
        if src.startswith("data:") or src.startswith("http") or src.startswith("//"):
            return m.group(0)
        try:
            return m.group(0).replace(src, data_uri(src, book))
        except OSError:
            return m.group(0)
    return re.sub(r'<img[^>]*\bsrc="([^"]+)"', repl, html)


def sketch_block(src, caption="", cls="fig"):
    """A figure block for an author-supplied image (path relative to BOOK_DIR)."""
    cap = ('<figcaption>%s</figcaption>' % caption) if caption else ""
    alt = (caption or "sketch").replace('"', "'")
    return '<figure class="%s"><img src="%s" alt="%s">%s</figure>' % (cls, src, alt, cap)
