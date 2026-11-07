#!/usr/bin/env python3
"""Build the inventory workbook (.xlsx) — the evidence behind the report.

    python3 06_build_workbook.py <scan-dir> <fleet.json> <out.xlsx> [adoption.json]

Sheets: Read me · Fleet · Capability matrix · Function index · Libraries · Conformance · Overlap ·
Decisions.

Everything here is generated from measurement. Authored content comes from files, not from editing
this script:
  - references/capability-codes.json fixes the matrix column order and set. Without it the columns
    fall back to first-seen order and two runs of the same account are not comparable.
  - overlap.json (step-7 clusters), decisions.json (the four analyses), adoption.json (step 5).
  - the METHOD text below, which you edit to match what you actually did.
"""
import json, os, sys
from collections import Counter
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

scan_dir = sys.argv[1] if len(sys.argv) > 1 else '/scratch/work/scan'
fleet_path = sys.argv[2] if len(sys.argv) > 2 else 'fleet.json'
out_path = sys.argv[3] if len(sys.argv) > 3 else 'fleet-inventory.xlsx'
adoption_path = sys.argv[4] if len(sys.argv) > 4 else None

SCAN = json.load(open(os.path.join(scan_dir, 'scan.json')))
ROWS = json.load(open(fleet_path))
HERE = os.path.dirname(os.path.abspath(__file__))
CODES_PATH = os.path.join(HERE, '..', 'references', 'capability-codes.json')


def load_caps():
    """The taxonomy fixes the column order and the column set. A capability nobody has still gets a
    column: an all-blank column is a finding, and deriving columns from the data hides it."""
    for p in (os.path.join(scan_dir, 'caps.json'), CODES_PATH):
        if os.path.exists(p):
            raw = json.load(open(p))
            return [[c, l] for c, l in (raw.items() if isinstance(raw, dict) else raw)]
    return None


CAPS = load_caps()
if CAPS is None:
    seen = []
    for r in ROWS:
        for c in r.get('caps', []):
            if c not in seen:
                seen.append(c)
    CAPS = [[c, c] for c in seen]
    print('WARNING: no capability-codes.json found — matrix columns are in first-seen order and are '
          'not comparable between runs', file=sys.stderr)

NAVY, ACCENT = '1F3352', '2E5A88'
LIGHT, GREEN, AMBER, RED = 'EDF2F8', 'E4F0E2', 'FBF0DC', 'FBE4E4'
thin = Side(style='thin', color='C9D3E0')
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def head(ws, row=1):
    for c in ws[row]:
        if c.value is None:
            continue
        c.font = Font(bold=True, color='FFFFFF', size=10)
        c.fill = PatternFill('solid', fgColor=NAVY)
        c.alignment = Alignment(vertical='center', wrap_text=True)
        c.border = BORDER
    ws.row_dimensions[row].height = 30


def widths(ws, w):
    for i, x in enumerate(w, start=1):
        ws.column_dimensions[get_column_letter(i)].width = x


wb = Workbook()

# ------------------------------------------------------------------ Read me
ws = wb.active
ws.title = 'Read me'
ws['A1'] = 'Fleet audit — inventory workbook'
ws['A1'].font = Font(bold=True, size=18, color=NAVY)
n = len(ROWS)
tot_loc = sum(r.get('loc', 0) for r in ROWS)
tot_units = sum(r.get('units', 0) for r in ROWS)
ws['A2'] = f'{n} repositories · {tot_loc:,} lines of application code · {tot_units:,} named code units'
ws['A2'].font = Font(italic=True, size=10, color='55606E')

METHOD = [
    ('What this workbook is',
     'The machine-checkable record behind the audit report: what every repository contains, what it can '
     'do, and how it conforms to the project conventions. The narrative analysis lives in the report. '
     'This file is the evidence.'),
    ('How it was built',
     '1. Every repository the account can reach was enumerated and shallow-cloned (depth 1, single '
     'branch). 2. Each tree was walked, excluding vendored dependency directories and binary assets. '
     '3. Named code units were extracted per language by regex over the application\'s own files. '
     '4. Capabilities were assigned by hand against the source — not inferred by keyword. '
     '5. Library adoption was measured by finding each shared library\'s file inside another repository.'),
    ('Sheet guide',
     'Fleet — one row per repository with size, stack, capabilities and purpose.\n'
     'Capability matrix — the grid the comparison is built on; columns come from the fixed taxonomy.\n'
     'Function index — named code units, capped per repository; the cap is stated on the sheet.\n'
     'Libraries — each shared library, who claims it, who ships it.\n'
     'Conformance — objective convention checks per repository.\n'
     'Overlap — capability clusters: where repositories duplicate each other.\n'
     'Decisions — the four analyses, recorded as data.'),
    ('Reading the matrix',
     'Every capability in the taxonomy gets a column even when no repository has it. An all-blank '
     'column is a finding, not noise: it is a capability this fleet does not have. Column order is '
     'fixed by references/capability-codes.json, so two audits of the same account are comparable.'),
    ('Reading the numbers',
     'LOC and code units count the application\'s own source only; vendored engines are excluded so the '
     'figures describe authored code. "Units" is the count of named functions, classes, routes and '
     'exports found — a proxy for surface area, not a quality measure. Do not rank repositories by it.'),
]
r = 4
for title, body in METHOD:
    ws.cell(r, 1, title).font = Font(bold=True, size=11, color=ACCENT)
    r += 1
    c = ws.cell(r, 1, body)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[r].height = max(30, 15 * (body.count('\n') + 1) + 8 * (len(body) // 110))
    r += 2
ws.column_dimensions['A'].width = 120

# ------------------------------------------------------------------ Fleet
ws = wb.create_sheet('Fleet')
cols = ['Repository', 'Category', 'LOC', 'Files', 'Units', 'Capabilities', 'Entry points', 'Purpose']
ws.append(cols)
for x in ROWS:
    ws.append([x['name'], x.get('category', ''), x.get('loc', 0), x.get('files', 0),
               x.get('units', 0), ' '.join(x.get('caps', [])),
               ', '.join(x.get('entries', [])[:3]),
               (x.get('intro') or x.get('title') or '')[:300]])
head(ws)
widths(ws, [42, 26, 9, 8, 8, 28, 34, 90])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BORDER
        c.font = Font(size=9)
        c.alignment = Alignment(vertical='top', wrap_text=(c.column in (6, 7, 8)))
ws.freeze_panes = 'B2'
ws.auto_filter.ref = f'A1:H{ws.max_row}'

# ------------------------------------------------------------------ Matrix
ws = wb.create_sheet('Capability matrix')
ws.append(['Repository', 'Category'] + [c for c, _ in CAPS] + ['Capability count'])
for x in sorted(ROWS, key=lambda y: (-len(y.get('caps', [])), y['name'])):
    caps = x.get('caps', [])
    ws.append([x['name'], x.get('category', '')] + ['●' if c in caps else '' for c, _ in CAPS] + [len(caps)])
head(ws)
widths(ws, [42, 26] + [6] * len(CAPS) + [17])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BORDER
        c.font = Font(size=9)
        if 3 <= c.column <= 2 + len(CAPS):
            c.alignment = Alignment(horizontal='center')
            if c.value == '●':
                c.fill = PatternFill('solid', fgColor=LIGHT)
ws.freeze_panes = 'C2'
base = ws.max_row + 2
ws.cell(base, 1, 'Column key').font = Font(bold=True, size=10, color=ACCENT)
for i, (code, label) in enumerate(CAPS):
    ws.cell(base + 1 + i, 1, code).font = Font(bold=True, size=9)
    ws.cell(base + 1 + i, 2, label).font = Font(size=9)

# ------------------------------------------------------------------ Function index
ws = wb.create_sheet('Function index')
ws.append(['Repository', 'File', 'Kind', 'Name'])
count = 0
capped = 0
for x in ROWS:
    s = SCAN.get(x['name'], {})
    if s.get('unit_cap', {}).get('truncated'):
        capped += 1
    for f, units in s.get('units', {}).items():
        for kind, name in units:
            ws.append([x['name'], f, kind, name])
            count += 1
head(ws)
widths(ws, [42, 58, 10, 44])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.font = Font(size=9, name='Consolas' if c.column == 4 else 'Calibri')
ws.freeze_panes = 'A2'
ws.auto_filter.ref = f'A1:D{ws.max_row}'
note_row = ws.max_row + 2
ws.cell(note_row, 1, f'{count:,} units listed. Extraction is capped per repository ({capped} '
                     f'repositories hit the cap); the Units column on the Fleet sheet counts units '
                     f'found, not units listed. Caps: FLEET_MAX_UNITS, FLEET_MAX_UNIT_FILES and '
                     f'FLEET_MAX_UNITS_PER_FILE in 03_scan.py.'
        ).font = Font(italic=True, size=9, color='55606E')

# ------------------------------------------------------------------ Libraries
ws = wb.create_sheet('Libraries')
ws.append(['Library', 'Ships it', 'Count', 'Referenced by', 'Verdict'])
if adoption_path and os.path.exists(adoption_path):
    ad = json.load(open(adoption_path))['kits']
    for k in sorted(ad, key=lambda x: -(len(ad[x]['vendored_by']) + len(ad[x]['referenced_by']))):
        d = ad[k]
        users = sorted(set(d['vendored_by']) | set(d['referenced_by']))
        ws.append([k, ', '.join(d['vendored_by']) or '—', len(d['vendored_by']),
                   ', '.join(d['referenced_by']) or '—',
                   'Used' if users else 'NO CONSUMERS — adopt or delete'])
else:
    ws.append(['(run 04_kit_adoption.py and pass adoption.json to populate this sheet)', '', '', '', ''])
head(ws)
widths(ws, [20, 70, 9, 60, 34])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BORDER
        c.font = Font(size=9)
        c.alignment = Alignment(vertical='top', wrap_text=True)
    v = row[2].value or 0
    row[2].fill = PatternFill('solid', fgColor=GREEN if v >= 3 else (AMBER if v else RED))
    row[2].alignment = Alignment(horizontal='center')
ws.freeze_panes = 'A2'

# ------------------------------------------------------------------ Conformance
FLAGS = [('landing', 'Landing page'), ('play', 'Playable app'), ('sw', 'Service worker'),
         ('tests', 'Self-tests'), ('ci', 'CI workflow'), ('licence', 'LICENSE'),
         ('changelog', 'CHANGELOG'), ('readme', 'README')]
ws = wb.create_sheet('Conformance')
ws.append(['Repository', 'Category'] + [l for _, l in FLAGS] + ['Met (of 8)'])
def flag_val(x, k):
    """`sw` and the PWA capability read the same file. One answer, not two."""
    if k == 'sw' and 'PWA' in x.get('caps', []):
        return True
    return bool(x.get('flags', {}).get(k))


for x in sorted(ROWS, key=lambda y: (-sum(flag_val(y, k) for k, _ in FLAGS), y['name'])):
    ws.append([x['name'], x.get('category', '')] + ['✓' if flag_val(x, k) else '' for k, _ in FLAGS]
              + [sum(flag_val(x, k) for k, _ in FLAGS)])
head(ws)
widths(ws, [42, 26] + [15] * len(FLAGS) + [12])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BORDER
        c.font = Font(size=9)
        c.alignment = Alignment(horizontal='center' if c.column > 2 else 'left')
    v = row[2 + len(FLAGS)].value or 0
    row[2 + len(FLAGS)].fill = PatternFill('solid', fgColor=GREEN if v == 8 else (AMBER if v >= 6 else RED))
ws.freeze_panes = 'C2'

# ------------------------------------------------------------------ Overlap
OVERLAP = []
for p in (os.path.join(scan_dir, 'overlap.json'), 'overlap.json'):
    if os.path.exists(p):
        OVERLAP = [(x.get('cluster', ''), x.get('code', ''), ', '.join(x.get('repos', [])),
                    x.get('why', '')) for x in json.load(open(p))]
        break
if not OVERLAP:
    OVERLAP = [('(no overlap.json found — write the step-7 clusters to it)', '', '', '')]
ws = wb.create_sheet('Overlap')
ws.append(['Capability cluster', 'Code', 'Repositories involved', 'Why it matters'])
for row in OVERLAP:
    ws.append(list(row))
head(ws)
widths(ws, [34, 8, 74, 90])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BORDER
        c.font = Font(size=9)
        c.alignment = Alignment(vertical='top', wrap_text=True)

# ------------------------------------------------------------------ Decisions
DEC = []
for p in (os.path.join(scan_dir, 'decisions.json'), 'decisions.json'):
    if os.path.exists(p):
        DEC = json.load(open(p))
        break
ws = wb.create_sheet('Decisions')
ws.append(['Analysis', 'Name', 'From / components', 'What moves', 'Why it matters', 'Effort', 'Risk'])
if DEC:
    for d in sorted(DEC, key=lambda z: (z.get('rank') or 999, z.get('analysis', ''))):
        ws.append([d.get('analysis', ''), d.get('name', ''),
                   ', '.join(d.get('from', []) or d.get('components', [])
                             or list(d.get('parts', {}) or {})),
                   d.get('what', ''), d.get('why', ''), d.get('effort', ''), d.get('risk', '')])
else:
    ws.append(['(no decisions.json found — record the four analyses there; schema in '
               'references/decisions-schema.json)', '', '', '', '', '', ''])
head(ws)
widths(ws, [20, 40, 40, 52, 62, 14, 40])
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BORDER
        c.font = Font(size=9)
        c.alignment = Alignment(vertical='top', wrap_text=True)
ws.freeze_panes = 'B2'

wb.save(out_path)
print(f'saved {out_path}: {n} repos, {count} code units, {len(wb.sheetnames)} sheets')
