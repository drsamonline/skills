#!/usr/bin/env python3
"""Fleet scanner: extract purpose, stack, entry points and named code units per repo.

    python3 03_scan.py <repos-dir> <out-dir>

Writes <out-dir>/scan.json. Read the module docstring in SKILL.md step 3-4 for what each field means.

Extraction is capped, because one 200k-line repo would otherwise dominate the run and the report:
    FLEET_MAX_UNITS          total units collected per repo (default 140)
    FLEET_MAX_UNIT_FILES     files contributing units per repo (default 14)
    FLEET_MAX_UNITS_PER_FILE units recorded per file (default 70)
The caps are written into scan.json under `unit_cap`, so every count in the report can be read against
the cap that produced it. Raise them with the environment variables for a small fleet.
"""
import json, os, re, sys
from collections import Counter, defaultdict

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/scratch/repos"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/scratch/work/scan"
MAX_UNITS = int(os.environ.get("FLEET_MAX_UNITS", "140"))
MAX_UNIT_FILES = int(os.environ.get("FLEET_MAX_UNIT_FILES", "14"))
MAX_UNITS_PER_FILE = int(os.environ.get("FLEET_MAX_UNITS_PER_FILE", "70"))
os.makedirs(OUT, exist_ok=True)

EXCL_DIRS = {".git", "node_modules", "vendor", "third_party", "third-party", "external",
             ".venv", "venv", "__pycache__", "target", "build", ".next", "coverage",
             "deps", "_deps", "bower_components", ".gradle", "Pods", "obj", "bin64",
             "thirdparty", "subprojects", "vcpkg", "site-packages"}
EXCL_EXT = {".png",".jpg",".jpeg",".webp",".gif",".ico",".svg",".woff",".woff2",".ttf",
            ".mp3",".mp4",".wav",".ogg",".zip",".gz",".pdf",".exe",".apk",".jar",
            ".pyc",".o",".a",".so",".dll",".bin",".wasm",".map",".lock",".pack",".idx"}
CODE_EXT = {".py",".js",".mjs",".cjs",".ts",".tsx",".jsx",".html",".htm",".rs",".c",".h",
            ".cpp",".cc",".hpp",".cs",".java",".kt",".dart",".go",".rb",".php",".sh",
            ".ps1",".lua",".gd",".swift",".m",".sql",".css",".scss",".vue",".svelte"}

RE_PY_FN   = re.compile(r"^[ \t]*(?:async[ \t]+)?def[ \t]+([A-Za-z_]\w*)", re.M)
RE_PY_CLS  = re.compile(r"^[ \t]*class[ \t]+([A-Za-z_]\w*)", re.M)
RE_ROUTE   = re.compile(r"^[ \t]*@[\w.]*(?:route|get|post|put|patch|delete)\(\s*[\"']([^\"']+)", re.M)
RE_JS_FN   = re.compile(r"\bfunction[ \t]+([A-Za-z_$][\w$]*)[ \t]*\(")
RE_JS_ARROW= re.compile(r"\b(?:const|let|var)[ \t]+([A-Za-z_$][\w$]*)[ \t]*=[ \t]*(?:async[ \t]*)?(?:function[ \t]*)?\(?[^)=\n]{0,80}\)?[ \t]*=>")
RE_JS_CLS  = re.compile(r"\bclass[ \t]+([A-Za-z_$][\w$]*)")
RE_JS_EXP  = re.compile(r"\bexport[ \t]+(?:default[ \t]+)?(?:async[ \t]+)?(?:function|class|const|let)[ \t]+([A-Za-z_$][\w$]*)")
RE_RS_FN   = re.compile(r"^[ \t]*pub(?:\([^)]*\))?[ \t]+(?:async[ \t]+)?fn[ \t]+([A-Za-z_]\w*)", re.M)
RE_RS_TYPE = re.compile(r"^[ \t]*pub[ \t]+(?:struct|enum|trait)[ \t]+([A-Za-z_]\w*)", re.M)
RE_C_FN    = re.compile(r"^[A-Za-z_][\w \t\*]*[ \t\*]([A-Za-z_]\w*)[ \t]*\([^;{}]*\)[ \t]*\{", re.M)
RE_GO_FN   = re.compile(r"^func[ \t]+(?:\([^)]*\)[ \t]*)?([A-Za-z_]\w*)", re.M)
RE_DART_FN = re.compile(r"^[ \t]*(?:Future|Stream|void|int|double|String|bool|Widget|List|Map)[\w<>?, ]*[ \t]+([a-zA-Z_]\w*)[ \t]*\(", re.M)
RE_HEAD    = re.compile(r"<h([1-3])[^>]*>(.*?)</h\1>", re.S | re.I)
RE_TITLE   = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
RE_SCRIPT  = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S | re.I)
RE_META_D  = re.compile(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', re.I)
RE_TAG     = re.compile(r"<[^>]+>")

def strip_tags(s):
    return re.sub(r"\s+", " ", RE_TAG.sub(" ", s)).strip()

def read(p, cap=400000):
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            return f.read(cap)
    except Exception:
        return ""

def walk(repo):
    files = []
    for dirpath, dirnames, filenames in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d not in EXCL_DIRS and not d.startswith(".git")]
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            ext = os.path.splitext(fn)[1].lower()
            if ext in EXCL_EXT:
                continue
            files.append((os.path.relpath(p, repo), p, ext))
    return files

def readme_of(repo):
    for cand in ("README.md","readme.md","README.rst","README.txt","README"):
        p = os.path.join(repo, cand)
        if os.path.exists(p):
            return p
    return None

def features_from_readme(txt):
    """Bullets and bolded feature lines from the README."""
    out = []
    for line in txt.splitlines():
        s = line.strip()
        if re.match(r"^[-*+]\s+\S", s) or re.match(r"^\d+\.\s+\S", s):
            s = re.sub(r"^[-*+\d.]+\s+", "", s)
            s = re.sub(r"\*\*|__|`|\[|\]\([^)]*\)", "", s).strip()
            if 8 < len(s) < 200:
                out.append(s)
    seen, uniq = set(), []
    for s in out:
        k = s.lower()[:60]
        if k not in seen:
            seen.add(k); uniq.append(s)
    return uniq

def main():
    repos = {}
    for name in sorted(os.listdir(ROOT)):
        repo = os.path.join(ROOT, name)
        if not os.path.isdir(repo):
            continue
        files = walk(repo)
        if not files:
            continue
        ext_count = Counter()
        loc = 0
        code_files = []
        for rel, p, ext in files:
            ext_count[ext] += 1
            if ext in CODE_EXT:
                try:
                    n = sum(1 for _ in open(p, "rb"))
                except Exception:
                    n = 0
                loc += n
                code_files.append((rel, p, ext, n))
        code_files.sort(key=lambda t: -t[3])

        readme_p = readme_of(repo)
        readme = read(readme_p, 60000) if readme_p else ""
        # first prose paragraph
        paras = [b.strip() for b in re.split(r"\n\s*\n", readme) if b.strip()]
        intro = ""
        for b in paras:
            if b.startswith("#") or b.startswith("[!") or b.startswith("<"):
                continue
            intro = re.sub(r"[*_`]|\[([^\]]*)\]\([^)]*\)", r"\1", b)
            intro = re.sub(r"\s+", " ", intro).strip()
            if len(intro) > 40:
                break

        # entry points
        entries = [rel for rel, p, ext, n in code_files
                   if os.path.basename(rel).lower() in
                   {"index.html","app.html","main.py","app.py","server.py","index.js",
                    "main.js","main.rs","main.c","main.cpp","main.dart","package.json"}]
        # html info
        html_title, html_desc, headings = "", "", []
        htmls = [t for t in code_files if t[2] in (".html",".htm")]
        if htmls:
            big = htmls[0]
            h = read(big[1], 500000)
            m = RE_TITLE.search(h);  html_title = strip_tags(m.group(1))[:160] if m else ""
            m = RE_META_D.search(h); html_desc = strip_tags(m.group(1))[:220] if m else ""
            for lvl, body in RE_HEAD.findall(h)[:60]:
                t = strip_tags(body)
                if 2 < len(t) < 90:
                    headings.append(t)
            seen=set(); headings=[x for x in headings if not (x.lower() in seen or seen.add(x.lower()))]

        # code units
        units = defaultdict(list)   # file -> [(kind,name)]
        total_units = 0
        for rel, p, ext, n in code_files[:120]:
            if total_units > MAX_UNITS:
                break
            txt = read(p, 400000)
            found = []
            if ext == ".py":
                found += [("class", x) for x in RE_PY_CLS.findall(txt)]
                found += [("fn", x) for x in RE_PY_FN.findall(txt)]
                found += [("route", x) for x in RE_ROUTE.findall(txt)]
            elif ext in (".js",".mjs",".cjs",".ts",".tsx",".jsx"):
                found += [("class", x) for x in RE_JS_CLS.findall(txt)]
                found += [("export", x) for x in RE_JS_EXP.findall(txt)]
                found += [("fn", x) for x in RE_JS_FN.findall(txt)]
                found += [("fn", x) for x in RE_JS_ARROW.findall(txt)]
            elif ext in (".html",".htm"):
                for sc in RE_SCRIPT.findall(txt)[:6]:
                    found += [("class", x) for x in RE_JS_CLS.findall(sc)]
                    found += [("fn", x) for x in RE_JS_FN.findall(sc)]
                    found += [("fn", x) for x in RE_JS_ARROW.findall(sc)]
            elif ext == ".rs":
                found += [("fn", x) for x in RE_RS_FN.findall(txt)]
                found += [("type", x) for x in RE_RS_TYPE.findall(txt)]
            elif ext in (".c",".h",".cpp",".cc",".hpp"):
                found += [("fn", x) for x in RE_C_FN.findall(txt)[:200]]
            elif ext == ".go":
                found += [("fn", x) for x in RE_GO_FN.findall(txt)]
            elif ext == ".dart":
                found += [("fn", x) for x in RE_DART_FN.findall(txt)]
            # dedupe, keep order
            seen=set(); clean=[]
            for k,v in found:
                if v in seen or v in {"if","for","while","switch","catch","function","return"}:
                    continue
                seen.add(v); clean.append([k,v])
            if clean:
                units[rel] = clean
                total_units += len(clean)

        repos[name] = {
            "name": name,
            "intro": intro[:900],
            "readme_features": features_from_readme(readme)[:40],
            "files": len(files),
            "loc": loc,
            "ext": dict(ext_count.most_common(12)),
            "code_files": [[rel, n] for rel, p, ext, n in code_files[:40]],
            "entries": entries[:12],
            "html_title": html_title,
            "html_desc": html_desc,
            "headings": headings[:40],
            "units": {k: v[:MAX_UNITS_PER_FILE] for k, v in list(units.items())[:MAX_UNIT_FILES]},
            "unit_count": total_units,
            "unit_cap": {"max_units": MAX_UNITS, "max_files": MAX_UNIT_FILES,
                         "max_per_file": MAX_UNITS_PER_FILE,
                         "captured": sum(len(v[:MAX_UNITS_PER_FILE])
                                         for v in list(units.values())[:MAX_UNIT_FILES]),
                         "truncated": total_units > MAX_UNITS or len(units) > MAX_UNIT_FILES},
            "docs": sorted([rel for rel, p, ext in files
                            if ext in (".md",".txt") and "/" not in rel])[:25],
        }
        print(f"{name:45s} files={len(files):5d} loc={loc:7d} units={total_units:4d}", file=sys.stderr)

    json.dump(repos, open(os.path.join(OUT, "scan.json"), "w"), indent=1)
    print(f"\n{len(repos)} repos scanned -> {OUT}/scan.json", file=sys.stderr)

main()
