# The six drifts, and the guard that catches each

Measured on one repository (`lexora`) on 2026-11-23. Every one of these read fine, and the suite was
green throughout. They are ordered by how expensive they were to find, not by size.

## 1. A capability the README said did not exist

**Looked like:** "byte-level canonicalization … is implemented; TXT/PDF *file ingestion* is not
implemented yet. Build scope is English-only."

**Was:** ingestion, OCR, a queryable archive, three language plugins and a GUI client had all shipped
with tests, over six weeks.

**Guard:** the maturity table cites the module and the test; `check_cited_paths.py` fails when the
citation stops resolving, and a reviewer gets something concrete to check.

## 2. A milestone table three weeks behind its own status file

**Looked like:** `ROADMAP.md` "Last verified 2026-10-15", M3 "Not started", while `STATUS.md` said
2026-11-16 and M3's code had landed.

**Guard:** every state document carries `Last verified: YYYY-MM-DD`; a test asserts the spread across
them is ≤ 14 days. It caught two more documents on its first run — including the README's own header.

## 3. A test count that nothing recomputed

**Looked like:** "502 passed, 1 skipped" in a document, with the suite at 765.

**Guard:** the README may carry **no** static count (a guard forbids the badge shape); the live number
is the CI badge, and a measured count lives in `STATUS.md` beside the date it was measured.

## 4. A landing page that denied two published releases

**Looked like:** "Phase 1 complete, no releases yet" in the meta description *and* the footer, with two
tags published.

**Guard:** `check_derived_facts.py` — read the release headings from `CHANGELOG.md`; if any exist, the
page may not say there are none. Derive the fact, do not hardcode it, or the guard goes stale the same
way the page did.

## 5. A requirements register claiming a project that no longer existed

**Looked like:** 35 rows, all "Not started", under the sentence "no code exists yet".

**Was:** 30 of them built and tested.

**Guard:** a status names its evidence — module + test in the same row — and both documents join the
cited-path guard, so a row citing a file that does not exist fails the build. Statuses were rewritten
to **Met / Partial / Open**, with the unmet half of a Partial stated in the cell itself. 35 open
became 4.

## 6. The headline number with no artifact — the worst one

**Looked like:** a benchmark table quoting the shipped default as `0.3352` on "172 files / 78.6 MiB".

**Was:** three different runs wearing one label. `0.3367` was revision 4's heldout-only first cut;
`0.3360` was revision 5's all-splits run; **`0.3352` had no surviving artifact at all**, because
revision 5's run reused revision 4's file names and overwrote them. "746 MB" was never that run's size
either.

**Guard, in three parts:**
- the document quotes a **revision** with every figure, and names the artifact beside it;
- the claims checker recomputes every published ratio from the committed artifacts and keys on
  `(system, revision)` — the ambiguity was never the number, it was the missing revision;
- the withdrawn figure stays in the document, marked withdrawn, with the reason. A number that
  disappears looks like it was never wrong.

## The two near-misses

- **A gram-index figure ("5× the stored payload") from an uncommitted generator.** Re-measured with a
  committed probe: it is a 3.15×–13.29× curve, and the proposal built on it (pack the table) was wrong
  because the cost is rows, not gram width. *Guard: every quoted measurement names its artifact.*
- **A measurement instrument that invented a 20.4 % error rate** on a canonicaliser that had made no
  incorrect change, from a whole-document diff over repetitive text. *Guard: test the instrument for
  the errors it invents, not only the ones it finds.*
