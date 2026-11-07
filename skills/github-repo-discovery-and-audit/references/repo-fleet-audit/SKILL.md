---
name: repo-fleet-audit
description: >
  Audit an entire GitHub account's repository fleet and produce a decision-grade analysis: a
  function-and-feature inventory of every repo, a capability matrix, and four syntheses — which apps
  should take a capability from which, which belong in one suite, which should merge into new apps,
  and what new products the collection makes possible. Use this whenever someone asks to "scan all my
  repos", "audit my repositories", "compare my projects", "what should I merge or consolidate", "which
  of my apps overlap", "review my whole GitHub", "find duplicated work across my projects", or wants a
  portfolio review, technical due diligence on their own code, a repo catalogue, or a plan for turning
  a collection of side projects into products or a suite. Also use it when someone asks for a repeatable
  repo-audit procedure or an audit skill. Works for 5 repositories or 500.
allowed-tools: execute_code terminal read_file write_file patch search_files
license: MIT
metadata:
  version: "1.0"
  author: "Dr Sohil Momin"
  category: "engineering / portfolio analysis"
---

# Repo fleet audit

A fleet audit answers one question a file listing cannot: **given everything this person has already
built, what should exist next, and what should stop existing?** The answer is not a summary of each
repository. It is a set of claims about relationships — this app should take that capability, these
four belong together, these two merge into something neither is.

Those claims are only credible if they rest on measurement rather than on READMEs. So the procedure
below has one non-negotiable core: **clone the code and measure it.** Everything else is synthesis on
top of that measurement.

## Why the measurement matters more than it looks

Two traps make a fleet audit worthless, and both are easy to fall into:

1. **Trusting self-description.** A registry, a README, a roadmap or a project index tells you what
   the author *intended*. Adoption, duplication and capability live in the filesystem. In a real
   audit of a 100-repo fleet, the author's own registry claimed consumers for eight shared libraries
   that no repository actually imported — the single most important finding of the audit, and one that
   was invisible from the documentation.
2. **Keyword classification.** Tagging repositories as "has search" because the word "search" appears
   in a heading produces a matrix that is confidently wrong. An early keyword pass tagged 44 of 100
   repos as LAN apps because the pattern `\blan\b` matched the filename `lan-kit.js`. Hand-classify
   capabilities against the source. At a hundred repos this takes an hour and it is the difference
   between a table someone can act on and one they cannot.

## The pipeline

Eight steps. Steps 1–5 are mechanical and scripted; steps 6–8 are judgement and are yours.

```
1 enumerate  →  2 acquire  →  3 walk  →  4 extract  →  5 measure adoption
                                                              ↓
                                     6 classify → 7 cluster → 8 synthesise → deliverables
```

### 1. Enumerate

List every repository the account can reach, from *every* access path available — the CLI, each
connected GitHub app, and any org membership. Reconcile the lists; a repo visible through one
connector and not another is usually a permissions story worth knowing before you write conclusions.

```bash
bash scripts/01_enumerate.sh <owner> > repos.tsv
```

Expect one line per repo: `name<TAB>language<TAB>sizeKB<TAB>updated<TAB>description`. Check the count
against the account's own repo list. If the number is suspiciously round (25, 30, 100) you have hit a
pagination cap, not a small fleet.

### 2. Acquire

Shallow-clone every repository in parallel. Depth 1 with a single branch is right: a full clone pulls
history the audit never reads, and history is most of the bytes.

```bash
bash scripts/02_clone_all.sh repos.tsv /scratch/repos
```

The script is resumable — re-running skips what is already there, so a fleet that takes longer than
one command timeout can be acquired in batches. Check free disk first: a hundred repos with vendored
engines ran to 1.5 GB here, and a single Chromium-derived repo can be 170 MB on its own.

### 3–4. Walk and extract

```bash
python3 scripts/03_scan.py /scratch/repos /scratch/work/scan
```

This produces `scan.json`: per repository, the file count, lines of application code, extension
histogram, entry points, HTML title and meta description, page heading structure, the largest source
files, and **named code units** — functions, classes, routes and exports, extracted per language
(Python `def`/`class`/route decorators, JavaScript function/arrow/class/export, Rust `pub fn` and
`pub type`, C/C++ definitions, Dart, Go).

Two things it must exclude, and does: vendored dependency directories (`node_modules`, `vendor`,
`third_party`, `target`, `build`, `.venv`, `deps`, `Pods`, …) and binary assets. Without those
exclusions a 100-repo fleet reports 27,000 "HTML files" that are mostly a bundled test corpus, and
every LOC figure becomes meaningless.

Treat the unit count as **surface area, not quality**. A repo with 200 units is a big tool; it is not
better than one with 14.

### 5. Measure adoption — the step that changes the answer

For every shared library in the fleet, find out whether another repository actually ships it. This is
the only honest measure of reuse. Do it by filename presence inside a foreign repo:

```bash
python3 scripts/04_kit_adoption.py /scratch/repos --declared declared.json
```

The script writes `adoption.json` itself. Do not redirect its stdout into that filename: stdout is the
human-readable table, and `adoption.json` must stay parseable JSON for the workbook. `--declared` takes
a JSON map of `{library: [claimed consumers]}`; a `declared.json` sitting in the working directory or at
the root of the fleet is picked up without the flag.

Cross-check against whatever the project claims. Where they disagree, **trust the filesystem** and say
so in the report — the disagreement is itself a finding, usually the most actionable one in the whole
audit. The script prints that comparison by default whenever a declared map is present, so the finding
is produced by the run rather than by remembering to ask for it. Two refinements worth knowing:

- A library can be *deliberately removed* after being shared (one repo's changelog recorded exactly
  that), leaving two copies of the same maths that must now agree. Look for it.
- A README that names a library is not adoption. A `<script src>` or a vendored file is.

### 6. Classify

Assign capabilities by hand, on a fixed taxonomy, against the source. `references/capability-taxonomy.md`
has the 19-column taxonomy used here, with the rule for each column and the failure mode it prevents.
Generate a starting template from the scan, then edit it:

```bash
python3 scripts/05_classify.py /scratch/work/scan > fleet.json   # template to fill in
```

The argument is the scan **directory**; the script also accepts the `scan.json` path inside it. Add
`--hints hints.json` to supply the fleet's own category vocabulary, and `--conformance conformance.json`
if its landing-page and playable-app paths differ from the defaults.

Keep the taxonomy **fixed across the whole fleet**. A capability that appears in one repo and not
another must be a real difference, not a different reading of the words. Record objective conventions
separately as booleans — service worker present, tests present, CI present, licence present, landing
page present — because those are checkable and make a conformance table for free.

### 7. Cluster

Find capabilities implemented more than once. A cluster of two is a coincidence; three or more is
duplication worth naming, and the size of the cluster is a proxy for the maintenance it costs. Rank
clusters by (repositories involved) × (how hard the capability is to get right). Cryptography, clinical
scoring and search rank high; a service worker ranks low even when thirty-five repos have one.

Write the clusters to `overlap.json` as `[{cluster, code, repos, why}]`. The workbook's Overlap sheet
reads that file; without it the sheet ships empty, and it is the sheet carrying the most insight.

### 8. Synthesise — the four analyses

Full frameworks, with the tests that separate a real grouping from a coincidence, are in
`references/analysis-frameworks.md`. In short:

| Analysis | Question | The test |
|---|---|---|
| **Improvement pairs** | Which app should take a capability from which? | Does the receiving app have a *visible gap* that the donor already fills? |
| **Suites** | Which apps belong together without merging? | Would one user want all of it on one day? |
| **Merges** | Which two apps become a better third thing? | Does the combined product answer a question neither could alone? |
| **New products** | What does the collection make cheap to build? | Is the expensive component already written and tested? |

Rank every recommendation by *value ÷ effort*, and be willing to say "do nothing here". An audit that
recommends forty changes is a wish list; one that names the three moves that matter is usable.

Record the four analyses as data, not only as prose: `decisions.json`, schema in
`references/decisions-schema.json`. The report argues from it, the workbook's Decisions sheet lists it,
and a re-run can diff it against the last audit. A recommendation that cannot be written as one of those
objects is not yet a finding.

## Deliverables

Produce two artefacts, and keep the evidence they rest on:

1. **An inventory workbook** (`.xlsx`) — the record. Sheets: read-me and method, the fleet table, the
   capability matrix, the full function index, the library-adoption table, conformance, the overlap
   clusters, and the recorded decisions. `scripts/06_build_workbook.py` builds it from `scan.json` +
   `fleet.json` + `adoption.json` + `overlap.json` + `decisions.json`, with the matrix columns fixed by
   `references/capability-codes.json`.
2. **A report** (`.docx`) — the argument. Structure, section by section, in
   `references/report-structure.md`; `scripts/docx_kit.py` is the renderer toolkit (headings, tables,
   callouts, TOC field, page numbers).

**The evidence:** `scan.json`, `fleet.json`, `adoption.json`, `overlap.json` and `decisions.json`, kept
in the working directory so the next audit is a re-run rather than a re-do.

**Write the narrative yourself.** The scripts produce structure and tables; the value of the report is
the judgement in it. Never let a template write the findings.

## Rules that keep the audit honest

- **State what you did not verify.** You read READMEs, structure, function names and UI headings — not
  every line. Name the large or third-party-derived codebases you sampled rather than audited, and say
  what your conclusions about them are and are not based on.
- **Separate intent from evidence.** Where a changelog or registry disagrees with the code, report
  both and trust the code.
- **Never infer a capability from a keyword.** If you cannot point at the source, the cell is empty.
- **Quantify before you advise.** "Seven apps hand-roll a trilingual string table" is a finding;
  "localisation could be improved" is not.
- **Give permission to delete.** Consolidation is usually the highest-value recommendation available
  to a large fleet, and the hardest to say. Say it.
- **Do not rank repositories by score.** A codebase's worth is not its line count, its test coverage
  or its capability count. Rank *relationships* and *decisions*, not repos.

## Scaling notes

- **Under 20 repos:** skip the workbook, put the matrix in the report. The synthesis is still the point.
- **20–150 repos:** the full pipeline as written. Clone in batches; the scan is fast, the synthesis is slow.
- **Over 150 repos:** sample the long tail for the catalogue but never for the capability matrix —
  classify everything, because the matrix is what the recommendations rest on. Delegate the
  per-repository catalogue writing to sub-agents if you have them, and keep the synthesis yourself.
- **Monorepos and vendored trees** inflate every count. Exclude before you measure, and say what you
  excluded.
