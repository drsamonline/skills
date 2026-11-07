# Report structure

The report is the argument; the workbook is the evidence. Keep them separate — do not put the matrix in
the report and do not put the findings in the workbook.

Aim for 25–55 pages on a 100-repository fleet, and much less on a small one. Length is a function of
the catalogue, not of the prose: the catalogue is one short block per repository and it is what makes
the report a record rather than an opinion.

## Front matter

- **Cover** — a title that names the fleet, a one-sentence statement of what the audit found, and a
  strip of five measured numbers (repositories, lines of code, code units, shared libraries and how many
  are actually used, and the size of the largest corpus). Numbers, not adjectives.
- **Contents** — a real Word TOC field so it updates.
- **One line on the evidence base** — name the workbook and say every figure is measured from the
  checked-out source rather than from the project's own documentation.

## 1. What this audit is

Restate the ask in the asker's terms, then say what you found in plain language before any table. The
reader should be able to stop after page two and still know the answer.

Then **the headline findings** — five to seven, each a bold claim followed by the measurement that
supports it. Not "the fleet has some duplication" but "of eighteen shared libraries, seven are used by
another repository and ten have zero consumers; the project registry claims consumers for eight that do
not import them."

## 2. What I could and could not verify

Short, and non-negotiable. State: what was cloned and read; what was sampled rather than audited (name
the large or third-party-derived codebases); that you read what the code declares, not what it does
under load; and where you trusted documentation and where you did not. An audit that does not bound
its own claims is a pitch.

## 3. How the audit was run

The eight steps in order, one paragraph each, with the one methodological choice that changed the
answer. This section is what makes the report reproducible, and it is what the reader will reuse.

## 4. The fleet at a glance

- Category table: what the repositories *are*, with counts and a description of each category.
- Capability spread: the column totals from the matrix, with a reading per row (infrastructure /
  common / rare). Two or three sentences of interpretation — which capability is the estate's identity,
  which is strategically important and duplicated.
- Conformance: the objective flags, the totals, and the **gaps**. Highlight any capability the fleet
  has and does not advertise (service workers with no install prompt is the classic).

## 5. The catalogue

One block per repository, grouped by category, ordered within a group by surface area. Each block:

- **Name** as a heading, then one metadata line: category · language · LOC · files · code units.
- **The capability fingerprint** — the codes, so a reader can scan for `OF SF ZD` or `OF LAN CA CL`.
- **What it is for** — the project's own opening description, trimmed to two sentences. Do not rewrite
  it; the author's own framing is data.
- **Key units** — two or three files with their most telling function names. This is what makes the
  catalogue a technical record rather than a blurb.
- **An audit note**, for the repositories that deserve one — roughly a third of them. Say what the repo
  is in the fleet: the keystone, the best implementation of a component, the one that removed a shared
  library, the only server-side product, the most rigorous engineering, the one with no adopters.

Keep notes to two or three sentences. The temptation is to write a paragraph per repo; resist it, or
the catalogue swamps the analysis.

## 6. The structural finding

If the audit surfaced one thing that conditions everything else — a half-wired shared layer, a
misleading registry, a missing data model — give it its own section before the four analyses, with the
measurement table. This is usually the section the reader remembers.

Include a subsection on **the duplications that cost the most**: five to seven clusters, each with the
count of implementations and one sentence on what it costs the user, not only the maintainer. Duplicated
code that prevents two apps sharing data is a user-facing defect.

## 7–10. The four analyses

One section each, in the order: improvement pairs, suites, merges, new products. Frameworks and tests
in `analysis-frameworks.md`.

- **Improvement pairs** as a table: from, to, what transfers, why it matters, effort. Then one
  paragraph naming the three you would do first.
- **Suites** as one block each: name, size, composition, shared spine, what the user gains, why this
  grouping rather than a coincidence. Then a subsection on ordering — which to build first and why,
  including the ones not worth building.
- **Merges** as one block each: the new name, what merges, the product, why the merge is necessary,
  which components carry each half.
- **New products** as one block each: the gap, the parts, what it does, the data model, the constraints
  it must respect, effort, principal risk.

## 11. What I would do first

Phased, ordered by compounding value, with a time estimate per phase. Phase 0 should be the cheap work
that makes everything after it cheaper. End with an explicit "deliberately last" paragraph.

## 12. Risks, and the things I would not do

Five or six, each a bold claim and an explanation. Include the risk the author will not want to hear
(sustainability, a server that is about to become load-bearing, a compliance obligation, a claim that
could be wrong under pressure). Frame it as protecting the work, because that is what it is.

## 13. Appendix

- The full index: one line per repository with category, capabilities, LOC and purpose.
- The gap lists: repositories with no test, with no CI, with no licence.
- Anything the reader will want to check: the adoption table, the methodology caveats.

## Style

- **Prose, not bullets,** for anything that is an argument. Tables for anything that is a comparison.
  Bullets only where the content is genuinely a list.
- **Numbers in the text.** Every qualitative claim should have a measurement near it.
- **Name the specific thing.** "lockhtml's Argon2id with auto-calibrated cost", not "better crypto".
- **No score for a repository.** Rank relationships and decisions, never repos.
- **Say the uncomfortable thing.** The most useful sentences in an audit are the ones the author would
  not write about their own work.
