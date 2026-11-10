# -*- coding: utf-8 -*-
"""Build a complete KDP publication set from one spec file, as one zip.

    python3 kdp_build.py --spec book.json

The zip contains interior (colour + greyscale), cover (paperback and/or
hardcover), the editable DOCX, a metadata sheet, a specification sheet and a QA
report, plus the HTML source master.

The one genuinely tricky part is that the gutter margin depends on the page
count, and the page count depends on the gutter — narrowing the text block makes
the book longer, which can push it into a band requiring a wider gutter. This
script iterates until the band stops moving, and reports how many passes it
took.
"""

from __future__ import annotations
import argparse, importlib, json, os, re, shutil, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kdp_specs as S
import build_interior as BI
import build_cover as BC

CHROMIUM = os.environ.get("CHROMIUM", "/usr/local/bin/chromium")


# ------------------------------------------------------------------ helpers
def sheet_html(inner, cls="", foot=None):
    f = (f'<div class="page-foot"><span>{foot}</span><span class="rule"></span>'
         f'<span class="pg">{{PG}}</span></div>') if foot else ""
    return f'<section class="sheet {cls}">{inner}{f}</section>'


def front_matter(meta, spec):
    """Five fixed front sheets: title, copyright, dedication, about, foreword."""
    t = meta.get("title", spec["title"])
    sub = meta.get("subtitle", spec.get("subtitle", ""))
    author = meta.get("author", spec.get("author", ""))
    imprint = meta.get("imprint", spec.get("imprint", ""))
    year = spec.get("year", "2026")
    contact = spec.get("contact", "")

    title_pg = (f'<div class="page-content"><div class="center-page title-page">'
                f'<h1>{t}</h1><div class="subtitle">{sub}</div>'
                f'<div class="author">{author}</div>'
                f'<div class="imprint">{imprint}</div></div></div>')

    copy = spec.get("copyright_notice") or (
        f"<p><strong>{t}</strong></p><p>&copy; {year} {author}. All rights reserved.</p>"
        f"<p>No part of this publication may be reproduced, stored in a retrieval system, or "
        f"transmitted in any form or by any means without the prior written permission of the "
        f"author, except for brief quotations in a review or scholarly work.</p>"
        + (f"<p>{contact}</p>" if contact else ""))
    copy_pg = f'<div class="page-content"><div class="center-page"><div class="copy-page">{copy}</div></div></div>'

    ded = meta.get("dedication", "")
    ded_pg = (f'<div class="page-content"><div class="center-page dedication"><p>{ded}</p>'
              f'</div></div>') if ded else f'<div class="page-content"></div>'

    about = spec.get("about_html") or (
        f'<div class="page-content"><div class="front-h">About the Author</div>'
        f'<div class="author-body">{spec.get("author_bio_html", "")}</div></div>')

    fw = meta.get("foreword_pre", [])
    fwp = meta.get("foreword_post", [])
    fw_html = "".join(f"<p>{x}</p>" for x in fw)
    fwp_html = "".join(f"<p>{x}</p>" for x in fwp)
    fore = (f'<div class="page-content"><div class="front-h">Foreword</div>'
            f'<h2 style="margin-top:0;">{meta.get("foreword_head","Foreword")}</h2>'
            f'{fw_html}{fwp_html}</div>')

    return [sheet_html(title_pg, cls="title-page"), sheet_html(copy_pg),
            sheet_html(ded_pg), sheet_html(about), sheet_html(fore)]


def check_margins(spec, pages, g):
    """Report every margin against KDP's minimum for this page count."""
    need = S.gutter(pages)
    out = []
    out.append(("gutter", spec["gutter"], need, spec["gutter"] >= need))
    omin = S.outside_margin(False)
    for k in ("outside", "top", "bottom"):
        v = spec["margins"][k]
        out.append((k, v, omin, v >= omin))
    return out


def font_gate(pdf):
    """Type 3 fonts are rejected by print engines. Check the file, do not assume.

    Chromium embeds a *variable* font as Type 3, and it exits 0 either way, so
    the PDF itself is the only trustworthy signal.
    """
    try:
        r = subprocess.run([sys.executable, os.path.join(HERE, "fontaudit.py"), pdf],
                           capture_output=True, text=True, timeout=180)
    except Exception as e:
        return False, f"font audit could not run ({type(e).__name__})"
    out = r.stdout or ""
    n = re.search(r"fonts: (\d+)", out)
    n = n.group(1) if n else "?"
    if r.returncode == 0:
        names = re.search(r"PASS\s+all embedded, no Type 3 \u2014 (.+)", out)
        detail = f"{n} fonts, all embedded, no Type 3"
        if names:
            detail += f" ({names.group(1)[:70]})"
        return True, detail
    t3 = re.search(r"FAIL\s+(\d+) Type 3", out)
    if t3:
        return False, f"{t3.group(1)} Type 3 font(s) — print engines reject these"
    return False, "unembedded or Type 3 fonts present"


def qa_md(spec, pages, g, margins, info, results):
    lines = ["# QA report", "",
             f"Generated for **{spec['title']}** — {spec['binding']}, "
             f"{spec['trim'][0]}×{spec['trim'][1]} in, {spec['paper']}.", "",
             "## Page budget", "",
             f"- Page count: **{pages}**",
             f"- Allowed range: {info['range'][0]}–{info['range'][1]}",
             f"- Inside range: **{'yes' if info['ok'] else 'NO'}**", ""]
    if not info["ok"]:
        lines += [f"> {info['message']}", ""]

    lines += ["## Margins against KDP minimums", "",
              "| Margin | Used (in) | Minimum (in) | Pass |", "|---|---|---|---|"]
    for name, used, need, ok in margins:
        lines.append(f"| {name} | {used} | {need} | {'yes' if ok else '**NO**'} |")
    fonts = [r for r in results if r[0].startswith("Fonts")]
    lines += ["", "## Font embedding", "",
              "Print engines reject Type 3 fonts. Chromium produces them for any",
              "*variable* font, and exits 0 while doing it.", ""]
    for name, ok, detail in fonts:
        lines.append(f"- {'PASS' if ok else '**FAIL**'} — {name}: {detail}")
    if fonts and not all(f[1] for f in fonts):
        lines += ["", "> **Do not upload this.** Run the font fix in",
                  "> `references/font-embedding.md`: pin static font instances,",
                  "> strip `@font-face` from the CSS, and re-render."]
    lines += ["", "## Files", ""]
    for name, ok, detail in results:
        lines.append(f"- [{'x' if ok else ' '}] **{name}** — {detail}")
    lines += ["", "## What this report cannot tell you", "",
              "- The **KDP Print Previewer** is the authoritative check; run it before publishing.",
              "- A **physical proof** is the only way to confirm colour, paper and binding.",
              "- **Hardcover spine width** is not published by KDP — confirm against their "
              "template generator before printing.", ""]
    return "\n".join(lines)


def spec_md(spec, pages, g):
    return "\n".join([
        "# Specification", "",
        "Every figure measured from the built files.", "",
        "| Field | Value |", "|---|---|",
        f"| Title | {spec['title']} |",
        f"| Binding | {spec['binding']} |",
        f"| Trim | {g['trim'][0]} × {g['trim'][1]} in |",
        f"| Paper | {S.PAPER[spec['paper']]['label']} |",
        f"| Page count | {pages} |",
        f"| Gutter (inside) | {spec['gutter']} in, mirrored |",
        f"| Outside / top / bottom | {spec['margins']['outside']} / "
        f"{spec['margins']['top']} / {spec['margins']['bottom']} in |",
        f"| Spine | {g['spine']} in ({g['spine']*25.4:.1f} mm)"
        + (" — approximate" if g.get("approximate_spine") else "") + " |",
        f"| Cover size | {g['width']} × {g['height']} in |",
        f"| Cover in points | {S.to_points(g['width'])} × {S.to_points(g['height'])} pt |",
        f"| Spine text | {'allowed' if g['spine_text_allowed'] else 'not allowed (<79 pages)'} |",
        "",
        "## Reproducing this book", "",
        "Re-run `kdp_build.py` with the same spec. If the page count changes, the spine "
        "changes with it — the cover must be rebuilt, not reused.",
    ]) + "\n"


# ------------------------------------------------------------------ main
def run(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    work = os.path.abspath(spec.get("workdir", "."))
    os.chdir(work)
    if work not in sys.path:
        sys.path.insert(0, work)      # the book module lives beside the spec
    trim = tuple(spec["trim"])
    paper = spec.get("paper", "white")
    binding = spec.get("binding", "paperback")

    css_parts = [open(p, encoding="utf-8").read() for p in spec["css"]]
    base_css = "\n".join(css_parts)

    # ---- iterate the gutter/page-count circular dependency ---------------
    g_in = spec["margins"]
    guess = S.gutter(200)          # a mid-band starting point
    history = []
    for attempt in range(1, 5):
        g = BI.geometry(trim, guess, g_in["outside"], g_in["top"], g_in["bottom"])
        css = base_css + "\n" + BI.trim_css(g)
        res = BI.build_master(spec["module"], css, g, "_interior.html",
                              extra_sections=None, front_sheets=None,
                              workdir=work)
        pages = res["total_pages"]
        need = S.gutter(pages)
        history.append((attempt, guess, pages, need))
        print(f"  pass {attempt}: gutter {guess} -> {pages} pages -> needs {need}")
        if abs(need - guess) < 1e-9:
            break
        guess = need
    spec["gutter"] = guess

    # rebuild once more with front matter included, at the settled gutter
    g = BI.geometry(trim, guess, g_in["outside"], g_in["top"], g_in["bottom"])
    css = base_css + "\n" + BI.trim_css(g)

    mod = importlib.import_module(spec["module"])
    meta = mod.META
    meta.setdefault("author", spec.get("author", ""))
    meta.setdefault("imprint", spec.get("imprint", ""))
    front = front_matter(meta, spec)

    res = BI.build_master(spec["module"], css, g, "_interior.html",
                          front_sheets=front, workdir=work)
    pages = res["total_pages"]
    need = S.gutter(pages)
    if need != guess:                       # front matter shifted the count
        spec["gutter"] = need
        g = BI.geometry(trim, need, g_in["outside"], g_in["top"], g_in["bottom"])
        css = base_css + "\n" + BI.trim_css(g)
        res = BI.build_master(spec["module"], css, g, "_interior.html",
                              front_sheets=front, workdir=work)
        pages = res["total_pages"]

    print(f"  settled: {pages} pages, gutter {spec['gutter']} in")

    info = S.check_pages(trim, paper, pages, binding)
    if not info["ok"]:
        print("  PAGE COUNT OUT OF RANGE:", info["message"])
        if info.get("alternatives"):
            print("  trims that would fit:", "; ".join(info["alternatives"]))

    # ---- build the package ----------------------------------------------
    outdir = os.path.join(work, "_pkg")
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir, exist_ok=True)
    stem = spec.get("file_stem", "Book")
    trim_tag = f"{trim[0]:g}x{trim[1]:g}"

    results = []
    interior = os.path.join(outdir, f"01_Interior_{trim_tag}_{paper}.pdf")
    BI.render_pdf("_interior.html", interior, gray=True, palette_css=BI.GRAY_PALETTE)
    pi = BI.pdf_info(interior)
    results.append(("Interior (greyscale)", pi.get("Pages") == str(pages),
                    f"{pi.get('Pages')} pages, {pi.get('Page size')}"))
    fok, fdet = font_gate(interior)
    results.append(("Fonts (interior)", fok, fdet))

    colour = os.path.join(outdir, f"02_Interior_{trim_tag}_{paper}_colour.pdf")
    BI.render_pdf("_interior.html", colour, gray=False)
    pc = BI.pdf_info(colour)
    results.append(("Interior (colour)", pc.get("Pages") == str(pages),
                    f"{pc.get('Pages')} pages"))
    cok, cdet = font_gate(colour)
    results.append(("Fonts (colour interior)", cok, cdet))

    # covers: paperback, hardcover, or both
    bindings = spec.get("build_bindings") or [binding]
    for b in bindings:
        try:
            cg = S.cover_geometry(trim, pages, paper, b)
            if b == "hardcover" and trim not in S.HARDCOVER_TRIMS:
                results.append((f"Cover ({b})", False,
                                f"{trim} is not a hardcover trim; skipped"))
                continue
            ch = f"_cover_{b}.html"
            BC.build(spec.get("cover", {}), trim, pages, paper, b, ch,
                     css_extra=spec.get("cover_css", ""))
            cpdf = os.path.join(outdir, f"03_Cover_{b}_{trim_tag}.pdf")
            BC.render(ch, cpdf)
            ci = BI.pdf_info(cpdf)
            ok = (ci.get("Pages") == "1" and
                  abs(float(ci["Page size"].split(" x ")[0]) - S.to_points(cg["width"])) < 1)
            cvok, cvdet = font_gate(cpdf)
            results.append((f"Fonts (cover {b})", cvok, cvdet))
            results.append((f"Cover ({b})", ok,
                            f"1 page, {ci.get('Page size')} (expected "
                            f"{S.to_points(cg['width'])} x {S.to_points(cg['height'])} pt)"))
        except Exception as e:
            results.append((f"Cover ({b})", False, f"{type(e).__name__}: {e}"))

    # DOCX
    try:
        import build_docx as BD
        dx = os.path.join(outdir, f"04_Manuscript_{trim_tag}.docx")
        BD.build(spec["module"], dx, trim, spec["gutter"],
                 g_in["outside"], g_in["top"], g_in["bottom"],
                 motif_dir=spec.get("motif_dir"))
        results.append(("DOCX manuscript", True, f"{os.path.getsize(dx)//1024} KB"))
    except Exception as e:
        results.append(("DOCX manuscript", False, f"{type(e).__name__}: {e}"))

    # sheets
    with open(os.path.join(outdir, "05_KDP_Metadata.md"), "w", encoding="utf-8") as fh:
        fh.write(spec.get("metadata_md") or
                 f"# Metadata\n\n**{spec['title']}**\n\n{spec.get('subtitle','')}\n\n"
                 f"Author: {spec.get('author','')}\n")
    with open(os.path.join(outdir, "06_KDP_Specification.md"), "w", encoding="utf-8") as fh:
        fh.write(spec_md(spec, pages, S.cover_geometry(trim, pages, paper, binding)))

    margins = check_margins(spec, pages, g)
    with open(os.path.join(outdir, "07_QA_Report.md"), "w", encoding="utf-8") as fh:
        fh.write(qa_md(spec, pages, S.cover_geometry(trim, pages, paper, binding),
                       margins, info, results))

    # source master
    src = os.path.join(outdir, "source"); os.makedirs(src, exist_ok=True)
    shutil.copy("_interior.html", os.path.join(src, "interior_master.html"))
    shutil.copy(spec_path, os.path.join(src, "book.json"))

    # zip
    zpath = os.path.join(work, spec.get("out", f"{stem}_KDP.zip"))
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(outdir):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.join(f"{stem}_KDP", os.path.relpath(full, outdir)))

    print(f"\n  package: {zpath}  ({os.path.getsize(zpath)//1024} KB)")
    print(f"  {pages} pages, spine {S.cover_geometry(trim, pages, paper, binding)['spine']} in")
    for name, ok, detail in results:
        print(f"    [{'x' if ok else ' '}] {name}: {detail}")
    return zpath


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    run(ap.parse_args().spec)
