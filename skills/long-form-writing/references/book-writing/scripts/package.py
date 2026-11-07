# -*- coding: utf-8 -*-
"""Assemble the delivery folder and zip for a book.

By default it builds the **no-PDF** package the skill standardises on:

  01_English/   A4 eBook HTML, eBook HTML, EPUB, Designed DOCX
  Supporting/   poster PDF, KDP metadata, audit log, AI/plagiarism report,
                author instructions, marketing kit
  <slug>_-_Complete.zip

A full-book PDF is produced/copied **only** when --pdf is passed and the files
exist. Extra languages are added only when asked, via --lang.

Usage:
    python3 package.py <slug> [--dir BOOK_DIR] [--out OUT_DIR] [--pdf]
                       [--lang <code>=<folder-name>] ...

Discovery is by filename convention; anything missing is reported, and a missing
required artifact makes the run exit non-zero (a book is not done until the whole
set exists).
"""
import os, sys, glob, shutil, zipfile

SUPPORTING = ["KDP_Metadata.md", "99_AUDIT_LOG.md", "AI_Plagiarism_Report.md",
              "Author_Instructions.md", "Instagram_Marketing.md"]


def first(patterns, d):
    for p in patterns:
        hits = sorted(glob.glob(os.path.join(d, p)))
        if hits:
            return hits[0]
    return None


def discover(d):
    arts = {}
    arts["a4"] = first(["*A4 eBook.html", "*A4*.html"], d)
    eb = [f for f in sorted(glob.glob(os.path.join(d, "*eBook.html"))) if "A4" not in f]
    arts["ebook"] = eb[0] if eb else None
    arts["epub"] = first(["*.epub"], d)
    arts["docx"] = first(["*Designed.docx", "*.docx"], d)
    arts["poster"] = first(["*Poster*.pdf", "*poster*.pdf"], d)
    return arts


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 1
    slug = argv[1]
    d = os.environ.get("BOOK_DIR", ".")
    out = None
    want_pdf = False
    langs = []
    i = 2
    while i < len(argv):
        if argv[i] == "--dir":
            d = argv[i + 1]; i += 2
        elif argv[i] == "--out":
            out = argv[i + 1]; i += 2
        elif argv[i] == "--pdf":
            want_pdf = True; i += 1
        elif argv[i] == "--lang":
            langs.append(argv[i + 1]); i += 2
        else:
            i += 1
    out = out or os.path.join(d, "deliver")
    a = discover(d)

    root = os.path.join(out, slug)
    if os.path.isdir(root):
        shutil.rmtree(root)
    en = os.path.join(root, "01_English"); sup = os.path.join(root, "Supporting")
    os.makedirs(en); os.makedirs(sup)

    missing = []
    for key, folder in (("a4", en), ("ebook", en), ("epub", en), ("docx", en)):
        if a[key]:
            shutil.copy2(a[key], folder)
        else:
            missing.append(key)
    if a["poster"]:
        shutil.copy2(a["poster"], sup)
    else:
        missing.append("poster")
    for name in SUPPORTING:
        p = os.path.join(d, name)
        if not os.path.isfile(p):
            alt = os.path.join(d, "support", name)
            if os.path.isfile(alt):
                p = alt
        if os.path.isfile(p):
            shutil.copy2(p, sup)
        else:
            missing.append(name)

    # extra languages (optional; only when asked)
    for j, spec in enumerate(langs):
        code, folder = (spec.split("=", 1) + [spec])[:2]
        dst = os.path.join(root, "0%d_%s" % (j + 2, folder))
        os.makedirs(dst, exist_ok=True)
        for pat in ("*%s*.html" % code, "*%s*.docx" % code, "*%s*.epub" % code):
            for f in sorted(glob.glob(os.path.join(d, pat))):
                shutil.copy2(f, dst)

    # full-book PDFs — only on request
    if want_pdf:
        for f in sorted(glob.glob(os.path.join(d, "*A4*.pdf")) + glob.glob(os.path.join(d, "*Mobile*.pdf"))):
            shutil.copy2(f, en)
    else:
        print("no full-book PDF packaged (pass --pdf to include any that exist)")

    zpath = os.path.join(root, "%s_-_Complete.zip" % slug.replace(" ", "_"))
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for folder in os.listdir(root):
            fp = os.path.join(root, folder)
            if os.path.isdir(fp):
                for f in sorted(glob.glob(os.path.join(fp, "*"))):
                    z.write(f, os.path.join(folder, os.path.basename(f)))
    print("package:", zpath)
    if missing:
        print("MISSING (build these before delivering):", ", ".join(missing))
        return 1
    print("complete set packaged.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
