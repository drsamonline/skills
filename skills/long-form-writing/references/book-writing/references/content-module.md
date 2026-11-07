# The content module — the one contract every tool shares

Every builder, verifier, rasteriser and packager in this skill reads its
book-specific content from a single **content module**: `content_<book>_<lang>.py`
in the project folder. Nothing is hardcoded in the tools, so the same scripts
build any book in any language. This file is the contract.

## The interface

A content module exposes these names:

```python
META = {
    "title": "...", "subtitle": "...", "title_html": "...",
    "kicker": "...", "word": "...", "num": 3, "imprint": "...",
    "dedication": "...", "foreword_head": "...",
    "foreword_pre": [...], "foreword_post": [...], "back_paras": [...],
    "lang": "en",
    # optional, used by the poster / combined file:
    "author": "...", "series": "...", "blurb": "...",
    "quote": "...", "quote_source": "...", "kicker_line": "...",
}

INTRO    = {"key": "introduction", "title": "...", "kicker": "", "num": "",
            "kind": "flow", "blocks": [<html strings>]}
CHAPTERS = [ {"key": "chapter-1", "title": "...", "kicker": "", "num": "1",
              "kind": "flow", "blocks": [...]}, ... ]
CLOSING  = {"key": "closing", "title": "...", "kind": "flow", "blocks": [...]}
POEM     = {"key": "poem", "title": "...", "kind": "flow", "blocks": [...]}

GLOSSARY     = [("Term", "definition"), ...]
BIBLIOGRAPHY = ["Author (Year). ...", ...]
INDEX_TERMS  = [("Term", ["chapter-1", "chapter-4"]), ...]

FIGURES = {"__FIG_CONDITIONING_CYCLE__": "<svg ...>", ...}   # optional
L10N    = {"font": "Georgia", ...}                            # optional
```

Block kinds the builders understand: a `chapter-open` div, `h2`/`h3`, `p` (with
`class="lead"` for the opener), `figure.fig` carrying a `__FIG_KEY__`
placeholder, `table.data`, `div.callout`, `div.vignette`, and the poem's
`stanza`/`line` divs.

## FIGURES and figure naming

A figure is written in a block as a placeholder, e.g.
`<figure class="fig">__FIG_CONDITIONING_CYCLE__</figure>`. The module's `FIGURES`
dict maps that placeholder to an inline SVG. The builders substitute it in; the
rasteriser writes it to a PNG.

The PNG filename is derived identically everywhere by `booklib.fig_name`:
strip `__FIG_` and the trailing `__`, lower-case, non-alphanumerics to `_`, and
prefix the language — so `__FIG_CONDITIONING_CYCLE__` in the English module
becomes `en_conditioning_cycle.png`. `rasterize_all.py` writes that name and
`make_docx_designed.py` looks for that same name, so the two never disagree.

## L10N — localised labels for the designed DOCX

The designed DOCX needs a handful of localised strings that are not part of the
manuscript: the copyright lines, the series line, the safety note, and the
section headings. Any book supplies them in an `L10N` dict, usually on its
**language kit** (`bookkit_<lang>.py`), so they live beside the rest of that
language's front/back matter. The generator falls back to generic English
defaults for anything not supplied. Keys:

`series` (with `{w}` filled from `META["word"]`), `author`, `c_rights`, `c_ed`,
`c_no`, `c_disc`, `c_case`, `contact`, `about_h`, `about_p`, `fore_h`,
`safety_l`, `safety_p`, `toc_h`, `gloss_h`, `idx_h`, `bib_h`, `font`.

If `about_p` is absent, the generator derives the About-the-Author paragraphs
from the kit's `ABOUT_HTML`.

## How each tool reads the module

| Tool | Reads | Command |
|---|---|---|
| `build_any.py` | META, sections, FIGURES; kit by `META["lang"]` | `build_any.py <module> <out.html>` |
| `make_docx_designed.py` | META, sections, FIGURES, L10N, kit | `make_docx_designed.py <module> <out.docx> [lang]` |
| `rasterize_all.py` | FIGURES | `rasterize_all.py <module> [<module> ...]` |
| `poster.py` | META | `poster.py <module> [<out.pdf>]` |
| `combine_langs.py` | the built HTML files | `combine_langs.py <slug> <title> en=a.html hi=b.html ...` |
| `verify_combined.py` | a combined file's `data-lang` set | `verify_combined.py <combined.html> ...` |

Every tool reads the project folder from `BOOK_DIR` and the browser from
`CHROMIUM`.

## A minimal module

```python
META = {"title": "The Long Afternoon", "subtitle": "A small book about light.",
        "title_html": "The Long Afternoon", "kicker": "A Book",
        "word": "One", "num": 1, "imprint": "MATNEO", "lang": "en",
        "dedication": "For everyone who looked up.",
        "foreword_head": "A word before", "foreword_pre": ["..."],
        "foreword_post": [], "back_paras": ["..."],
        "quote": "...", "quote_source": "From the Epilogue", "author": "A. Author"}
INTRO = {"key": "introduction", "title": "Introduction", "kicker": "", "num": "",
         "kind": "flow", "blocks": ['<p class="lead">...</p>']}
CHAPTERS = [{"key": "chapter-1", "title": "The First Room", "kicker": "", "num": "1",
             "kind": "flow", "blocks": ['<p>...</p>']}]
CLOSING = {"key": "closing", "title": "Epilogue", "kicker": "", "num": "",
           "kind": "flow", "blocks": ['<p>...</p>']}
POEM = {"key": "poem", "title": "Coda", "kind": "flow", "blocks": []}
GLOSSARY = []; BIBLIOGRAPHY = []; INDEX_TERMS = []
FIGURES = {}
```

`parse_manuscript.py` emits a module of exactly this shape for the ornamental
pack, so a supplied manuscript and a hand-written module are interchangeable.
