#!/usr/bin/env python3
"""Measure shared-library adoption from the filesystem — the step that changes the answer.

    python3 04_kit_adoption.py <repos-dir> [--suffix -kit] [--declared declared.json] [--out adoption.json]

The script writes adoption.json itself. Do not redirect its stdout over that filename — stdout is the
human-readable table and adoption.json must stay parseable JSON. A declared.json in the working
directory or at the root of the fleet is picked up without a flag.

Two measurements, both from files rather than from documentation:

  1. VENDORING — for every candidate library, is its file physically present inside another
     repository? A README mention is not adoption. A registry entry is not adoption. A file is.
  2. IMPORTS — does another repository reference the library by name in a script tag, an
     import, or a require? This catches libraries consumed without a vendored copy.

Writes adoption.json:
    {"kits": {name: {"vendored_by": [...], "referenced_by": [...], "own": bool}},
     "unused": [...], "vendored_only": [...]}

--declared takes a JSON map of {library: [claimed consumers]} so you can print the gap between
what the project says and what the code does. That gap is usually the most actionable finding
in a whole audit, so print it loudly.
"""
import json, os, re, sys
from collections import defaultdict

SKIP_DIRS = {'.git', 'node_modules', 'vendor', 'third_party', 'third-party', 'external',
             '.venv', 'venv', '__pycache__', 'target', 'build', '.next', 'coverage',
             'deps', '_deps', 'bower_components', 'Pods', 'obj', 'subprojects', 'vcpkg'}
MAX_FILE = 1_500_000


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '/scratch/repos'
    suffix = '-kit'
    declared = {}
    out_path = 'adoption.json'
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == '--suffix':
            suffix = args[i + 1]; i += 2
        elif args[i] == '--declared':
            declared = json.load(open(args[i + 1])); i += 2
        elif args[i] == '--out':
            out_path = args[i + 1]; i += 2
        else:
            i += 1

    # A declared map sitting with the fleet is picked up without a flag. The claimed-vs-actual gap is
    # the most actionable finding in the audit, so it should not depend on remembering a flag.
    if not declared:
        for cand in ('declared.json', os.path.join(root, 'declared.json')):
            if os.path.exists(cand):
                declared = json.load(open(cand))
                print(f"declared map: {cand}\n", file=sys.stderr)
                break

    repos = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)))

    # pass 1: discover candidate libraries (any repo whose name ends with the suffix)
    kits = [r for r in repos if r.endswith(suffix)]
    # also discover libraries by file: <name><suffix>.js at the root of any repo
    file_names = defaultdict(set)
    for r in repos:
        base = os.path.join(root, r)
        for f in os.listdir(base):
            if f.endswith('.js') and f[:-3].endswith(suffix):
                file_names[f[:-3]].add(r)
    for k in file_names:
        if k not in kits:
            kits.append(k)
    kits = sorted(set(kits))

    vendored = defaultdict(set)
    referenced = defaultdict(set)

    # ONE combined pattern: 18 separate regexes over 50,000 files is minutes of work; one
    # alternation with a capture group is seconds. This is the difference between the script
    # finishing and timing out on a large fleet.
    if kits:
        alt = '|'.join(re.escape(k) for k in sorted(kits, key=len, reverse=True))
        ref_any = re.compile(r'(?:(?:src|href)\s*=\s*["\'][^"\']*(?:' + alt + r')\.js'
                             r'|(?:import|require)[^;\n]{0,80}["\'][^"\']*(?:' + alt + r')["\'/])')
        ref_name = re.compile(r'(' + alt + r')')
    else:
        ref_any = ref_name = None

    for r in repos:
        base = os.path.join(root, r)
        for dp, dn, fn in os.walk(base):
            dn[:] = [d for d in dn if d not in SKIP_DIRS]
            for f in fn:
                stem = f[:-3] if f.endswith('.js') else None
                if stem in kits and r != stem:
                    vendored[stem].add(r)
                if not f.endswith(('.html', '.htm', '.js', '.mjs', '.cjs', '.ts', '.tsx', '.vue', '.svelte')):
                    continue
                p = os.path.join(dp, f)
                try:
                    if os.path.getsize(p) > MAX_FILE:
                        continue
                    txt = open(p, encoding='utf-8', errors='replace').read()
                except Exception:
                    continue
                if ref_any is not None and ref_any.search(txt):
                    for k in set(ref_name.findall(txt)):
                        if k != r:
                            referenced[k].add(r)

    out = {'kits': {}, 'unused': [], 'vendored_only': []}
    for k in kits:
        v, ref = sorted(vendored.get(k, [])), sorted(referenced.get(k, []))
        out['kits'][k] = {'vendored_by': v, 'referenced_by': ref, 'own': k in repos}
        if not v and not ref:
            out['unused'].append(k)
        if v and k not in declared:
            out['vendored_only'].append(k)

    json.dump(out, open(out_path, 'w'), indent=1)

    print(f"{len(kits)} shared libraries found across {len(repos)} repositories\n")
    print(f"{'library':24s} {'vendored':>9s} {'referenced':>11s}  consumers")
    print('-' * 100)
    for k in sorted(kits, key=lambda x: -(len(out['kits'][x]['vendored_by']) + len(out['kits'][x]['referenced_by']))):
        d = out['kits'][k]
        users = sorted(set(d['vendored_by']) | set(d['referenced_by']))
        print(f"{k:24s} {len(d['vendored_by']):9d} {len(d['referenced_by']):11d}  {', '.join(users[:6])}")

    print(f"\nUSED     : {len(kits) - len(out['unused'])}")
    print(f"UNUSED   : {len(out['unused'])} -> {', '.join(out['unused']) or 'none'}")
    print(f"UNTRACKED: {', '.join(out['vendored_only']) or 'none'} (adopted but not declared anywhere)")

    if declared:
        print('\nCLAIMED vs ACTUAL')
        print('-' * 100)
        for k, claimed in declared.items():
            d = out['kits'].get(k, {'vendored_by': [], 'referenced_by': []})
            actual = set(d['vendored_by']) | set(d['referenced_by'])
            wrong = [c for c in claimed if c not in actual and not c.startswith('(')]
            phantom = sorted(actual - set(claimed))
            if wrong or phantom:
                print(f"  {k}:")
                if wrong:
                    print(f"     claimed but absent : {', '.join(wrong)}")
                if phantom:
                    print(f"     present but unclaimed: {', '.join(phantom)}")
        print('\nReport this gap. A library the project believes is shared and is not is worse '
              'than no library: it makes the fleet feel consolidated while it is not.')


main()
