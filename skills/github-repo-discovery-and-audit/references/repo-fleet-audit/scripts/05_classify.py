#!/usr/bin/env python3
"""Build the classification template you then fill in by hand.

    python3 05_classify.py <scan-dir|scan.json> [repos-dir] [--hints hints.json]
                           [--conformance conformance.json] > fleet.json

Emits, per repository: the measured facts, the objective convention flags (computed here, so
you do not have to check them by hand), a suggested category, and an EMPTY capability list.

Then edit fleet.json. Set `caps` for every repository from the taxonomy in
references/capability-taxonomy.md, and write the `note` — one sentence on what this repo is in
the fleet and whether it is well placed. Write the note while the source is still open; it
becomes the catalogue in the report and it is much cheaper now than later.

A blank `caps` list is a deliberate failure mode: it makes an unclassified repository obvious
instead of letting a guess pass as a measurement.

The category suggestion is the only keyword-driven decision in the pipeline and it never touches
`caps`. Category vocabulary is data: override the defaults with --hints rather than editing this
file, because a fleet's own words belong to that fleet.
"""
import json, os, re, sys
from collections import Counter


def parse_args(argv):
    pos, opts = [], {}
    i = 1
    while i < len(argv):
        if argv[i].startswith('--'):
            opts[argv[i][2:]] = argv[i + 1] if i + 1 < len(argv) else ''
            i += 2
        else:
            pos.append(argv[i])
            i += 1
    return pos, opts


pos, opts = parse_args(sys.argv)
arg = pos[0] if pos else '/scratch/work/scan'
repos_dir = pos[1] if len(pos) > 1 else '/scratch/repos'
scan_dir = os.path.dirname(os.path.abspath(arg)) if arg.endswith('.json') else arg
scan = json.load(open(os.path.join(scan_dir, 'scan.json')))

# Category vocabulary is data, not code. A fleet's own words belong to that fleet, so the shipped
# defaults are generic and --hints <json> replaces them. This is the only keyword-driven decision in
# the pipeline, it only ever suggests a category, and it never writes `caps`.
DEFAULT_HINTS = {
    'kit': ['kit', 'lib', 'sdk', 'runtime', 'engine'],
    'meta': ['dashboard', 'control', 'audit', 'backup', 'registry', 'hub', 'console', 'release'],
    'engine': ['compiler', 'parser', 'lexer', 'browser', 'server', 'builder', 'toolbox', 'optimizer'],
    'game': ['game', 'shooter', 'platformer', 'rpg', 'arcade', 'idle', 'puzzle'],
    'teaching': ['teach', 'exercise', 'classroom', 'curriculum', 'course', 'lesson', 'tutorial'],
}
CATEGORY_NAMES = {
    'kit': 'Kit / shared library',
    'meta': 'Meta / system',
    'engine': 'Engine / platform / tool',
    'game': 'Game',
    'teaching': 'Teaching / curriculum',
}

# Objective convention paths are one estate's house layout. Override with --conformance.
CONF = {'landing': ['docs/index.html', 'index.html'], 'play_prefix': ['docs/play/']}


def load_hints(path=None):
    hints = {k: list(v) for k, v in DEFAULT_HINTS.items()}
    if path and os.path.exists(path):
        for k, v in json.load(open(path)).items():
            hints[k] = list(v)
    return hints


hints = load_hints(opts.get('hints'))
if opts.get('conformance') and os.path.exists(opts['conformance']):
    CONF.update(json.load(open(opts['conformance'])))


def flags(root):
    f = dict(landing=False, play=False, sw=False, tests=False, ci=False,
             licence=False, changelog=False, readme=False)
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d != '.git']
        for x in fn:
            rel = os.path.relpath(os.path.join(dp, x), root)
            if x == 'sw.js':
                f['sw'] = True
            if re.match(r'(test|selftest)', x, re.I) or rel.startswith('tests/'):
                f['tests'] = True
            if rel.startswith('.github/workflows/'):
                f['ci'] = True
            if rel in CONF['landing']:
                f['landing'] = True
            if any(rel.startswith(p) for p in CONF['play_prefix']):
                f['play'] = True
            if x.upper().startswith(('LICENSE', 'LICENCE')):
                f['licence'] = True
            if x.upper().startswith('CHANGELOG'):
                f['changelog'] = True
            if x.lower().startswith('readme'):
                f['readme'] = True
    return f


def suggest(name, d, hints):
    """Suggest a category from evidence: repo name, page headings, README features, named units.

    This is the only keyword-driven decision in the pipeline and it never touches `caps`. A capability
    is marked by reading the source; a category is a starting point for a human edit.
    """
    name_txt = name.lower()
    body = ' '.join([d.get('html_title') or '', d.get('intro') or '',
                     ' '.join(d.get('headings', [])),
                     ' '.join(d.get('readme_features', [])),
                     ' '.join(u[1] for units in d.get('units', {}).values() for u in units)]).lower()

    def score(words):
        return sum(3 for w in words if w in name_txt) + sum(1 for w in words if w in body)

    ranked = sorted(((score(v), k) for k, v in hints.items()), key=lambda t: (-t[0], t[1]))
    top, kind = ranked[0] if ranked else (0, '')
    if top < 3:
        return 'Offline app'
    return CATEGORY_NAMES.get(kind, 'Offline app')


out = []
for name in sorted(scan):
    d = scan[name]
    root = os.path.join(repos_dir, name)
    out.append({
        'name': name,
        'category': suggest(name, d, hints),
        'title': d['html_title'],
        'intro': d['intro'],
        'features': d['readme_features'][:12],
        'entries': d['entries'][:6],
        'code_files': d['code_files'][:8],
        'headings': d['headings'][:12],
        'files': d['files'], 'loc': d['loc'], 'units': d['unit_count'],
        'unit_cap': d.get('unit_cap', {}),
        'flags': flags(root) if os.path.isdir(root) else {},
        'caps': [],
        'note': '',
    })

json.dump(out, sys.stdout, indent=1)
print(f"\n{len(out)} repositories -> fill in 'caps' and 'note' for every one", file=sys.stderr)
