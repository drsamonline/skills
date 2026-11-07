# -*- coding: utf-8 -*-
"""Parse a plain-text/markdown manuscript into an ornamental-pack content module.

The manuscript is split on `## ` (H2) headings; if there are none, `# ` (H1) is
used instead. Each heading opens a section with key/title/kicker/num/blocks.

Conversion rules (see references/lessons-and-gotchas.md, section 3):

  * `---` on its own line            -> ornaments.rune_divider()  (a scene break)
  * a bold-only paragraph `**X**`    -> div.exhibit sub-head with an ex-label
  * the first paragraph of a section -> p.lead with a drop-cap span
  * inline `*x*` -> <em>,  `**x**` -> <strong>
  * `### ` -> <h3>
  * the leading/trailing `---` of a section is STRIPPED, so a chapter's end
    marker never becomes an ornament-only page
  * the manuscript's own `*(Chapter N - end)*` markers are dropped
  * a trailing bullet list (a contents list the author typed) is dropped

Output: content_<slug>_<lang>.py exposing META, INTRO, CHAPTERS, CLOSING,
GLOSSARY, INDEX_TERMS, ABOUT_HTML, BACK_HTML - the interface build_a4.py,
build_mobile.py and make_docx.py expect.

GLOSSARY and INDEX_TERMS are authored later (Phase 4); the parser emits empty
lists as placeholders you fill in.

Usage:
    BOOK_DIR=/path/to/project python3 parse_manuscript.py <manuscript.md> <slug> <lang>

`<lang>` is en | hi | gu (used only for the output filename and META["lang"]).
META can be overridden with env vars BOOK_TITLE, BOOK_SUBTITLE, BOOK_KICKER,
BOOK_IMPRINT; otherwise title/subtitle are read from the manuscript's `# ` head.
"""
import os, re, sys

BOOK = os.environ.get("BOOK_DIR", "/scratch/work/book")
sys.path.insert(0, BOOK)
try:
    import ornaments
    _DIVIDER = ornaments.rune_divider()
except Exception:  # ornaments.py not on the path yet - keep the class name
    _DIVIDER = '<div class="rune-divider" aria-hidden="true"></div>'

END_MARKER = re.compile(r"^\*\(\s*.*?\bend\b.*?\)\*$", re.I)
DIVIDER_LINE = re.compile(r"^-{3,}$")
INTRO_TITLES = ("introduction", "intro", "prologue", "preface", "foreword")
CLOSING_TITLES = ("epilogue", "afterword", "closing", "conclusion", "envoi")
# Back matter is authored in Phase 4, not parsed from the manuscript.
SKIP_TITLES = ("glossary", "index", "bibliography", "acknowledg", "contents",
               "about the author", "references")


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "section"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    """Escape, then apply inline emphasis. Order matters: bold before italic."""
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
    t = re.sub(r"\*([^*]+?)\*", r"<em>\1</em>", t, flags=re.S)
    return t


def split_sections(text):
    """Return (title, subtitle, [(heading, body_lines), ...])."""
    lines = text.split("\n")
    head_title, subtitle = "", ""
    for ln in lines:
        if ln.startswith("# ") and not head_title:
            head_title = ln[2:].strip()
        elif head_title and not subtitle and ln.strip() and not ln.startswith("#"):
            subtitle = ln.strip()
            break

    marker = "## "
    if not any(ln.startswith("## ") for ln in lines):
        marker = "# "

    sections, cur = [], None
    for ln in lines:
        if ln.startswith(marker) and not ln.startswith(marker + "#"):
            if cur:
                sections.append(cur)
            cur = {"heading": ln[len(marker):].strip(), "body": []}
        elif cur is not None:
            cur["body"].append(ln)
    if cur:
        sections.append(cur)
    return head_title, subtitle, sections


def to_blocks(body):
    """Turn a section body into a list of block-HTML strings."""
    blocks = []
    paras = [p.strip() for p in re.split(r"\n\s*\n", "\n".join(body)) if p.strip()]
    # drop a trailing bullet list (a contents list the author typed)
    while paras and all(l.strip().startswith("- ") for l in paras[-1].split("\n")):
        paras.pop()

    lead_done = False
    for p in paras:
        if DIVIDER_LINE.match(p):
            blocks.append(_DIVIDER)
            continue
        if END_MARKER.match(p):
            continue
        m = re.fullmatch(r"\*\*(.+)\*\*", p, re.S)
        if m and "\n" not in p:
            blocks.append('<div class="exhibit"><span class="ex-label">%s</span></div>'
                          % inline(m.group(1)))
            continue
        if p.startswith("### "):
            blocks.append("<h3>%s</h3>" % inline(p[4:].strip()))
            continue
        text = " ".join(l.strip() for l in p.split("\n"))
        html = inline(text)
        if not lead_done:
            m = re.match(r"([A-Za-z\u0900-\u097F\u0A80-\u0AFF\u0B80-\u0BFF])(.*)", html, re.S)
            if m:
                html = '<span class="dropcap">%s</span>%s' % (m.group(1), m.group(2))
            blocks.append('<p class="lead">%s</p>' % html)
            lead_done = True
        else:
            blocks.append("<p>%s</p>" % html)

    # strip leading / trailing scene-break dividers
    while blocks and blocks[0].startswith('<div class="rune-divider"'):
        blocks.pop(0)
    while blocks and blocks[-1].startswith('<div class="rune-divider"'):
        blocks.pop()
    return blocks


def classify(heading):
    t = heading.lower().strip()
    if t in INTRO_TITLES or t.startswith("introduction"):
        return "intro"
    if t in CLOSING_TITLES:
        return "closing"
    return "chapter"


def build(manuscript_path, book_slug, lang):
    text = open(manuscript_path, encoding="utf-8").read()
    head_title, subtitle, sections = split_sections(text)

    intro, chapters, closing = None, [], None
    used_keys = set()
    for sec in sections:
        h = sec["heading"].lower().strip()
        if any(h.startswith(s) for s in SKIP_TITLES):
            continue
        kind = classify(sec["heading"])
        blocks = to_blocks(sec["body"])
        if not blocks:
            continue
        key = slug(sec["heading"])
        while key in used_keys:
            key += "-x"
        used_keys.add(key)
        num = str(len(chapters) + 1) if kind == "chapter" else ""
        node = {"key": key, "title": sec["heading"], "kicker": "",
                "num": num, "kind": "flow", "blocks": blocks}
        if kind == "intro":
            intro = node
        elif kind == "closing":
            closing = node
        else:
            chapters.append(node)

    if intro is None:
        intro = {"key": "introduction", "title": "Introduction", "kicker": "",
                 "num": "", "kind": "flow", "blocks": []}
    if closing is None:
        closing = {"key": "closing", "title": "Closing", "kicker": "",
                   "num": "", "kind": "flow", "blocks": []}

    title = os.environ.get("BOOK_TITLE") or head_title or book_slug
    meta = {
        "title": title,
        "title_html": title,
        "subtitle": os.environ.get("BOOK_SUBTITLE") or subtitle,
        "kicker": os.environ.get("BOOK_KICKER", ""),
        "imprint": os.environ.get("BOOK_IMPRINT", "MATNEO"),
        "lang": lang,
    }

    about = ('<div class="page-content"><div class="front-h">About the Author</div>\n'
             '  <div class="author-body"><p>Fill from assets/author-bio-template.md.</p>'
             '</div></div>')
    back = ('<div class="page-content"><div class="center-page">'
            '<p>Back-cover copy goes here.</p></div></div>')

    out = {
        "META": meta,
        "INTRO": intro,
        "CHAPTERS": chapters,
        "CLOSING": closing,
        "GLOSSARY": [],
        "INDEX_TERMS": [],
        "ABOUT_HTML": about,
        "BACK_HTML": back,
    }
    path = os.path.join(BOOK, "content_%s_%s.py" % (book_slug, lang))
    with open(path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Generated by parse_manuscript.py from %s - do not hand-edit the\n'
                'block HTML; re-run the parser after changing the manuscript or\n'
                'ornaments.py (divider SVGs are baked in at parse time).\n"""\n'
                % os.path.basename(manuscript_path))
        for name in ("META", "INTRO", "CHAPTERS", "CLOSING",
                     "GLOSSARY", "INDEX_TERMS", "ABOUT_HTML", "BACK_HTML"):
            f.write("%s = %s\n\n" % (name, repr(out[name])))
    return path, len(chapters), sum(len(c["blocks"]) for c in chapters)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    p, nch, nblk = build(sys.argv[1], sys.argv[2], sys.argv[3])
    print("wrote %s  (%d chapters, %d blocks)" % (p, nch, nblk))
