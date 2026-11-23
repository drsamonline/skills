---
name: doc-claims-guard
description: Keep a repository's prose from lying about the code — make every status, ratio, release and "not yet" a claim a command re-derives, and fail the build when it drifts. Use when docs, READMEs, roadmaps or requirement registers have gone stale, when a benchmark number has no artifact behind it, or when setting up guards so a project's documents cannot silently decay again.
metadata:
  title: "Prose that nothing recomputes"
---

# Prose that nothing recomputes

A status, a ratio and a "not yet" are all **claims**. A claim that no command re-derives decays
silently, in whichever direction the project moves — and it never fails a build, because it was never
a test.

Six documents in one repository were wrong at the same time, in six directions, and the suite was
green throughout: the README said ingestion was not implemented (it had shipped), the roadmap had
last been verified six weeks earlier and still said "Not started", the progress table quoted a
502-test gate when it was 765, the landing page denied two published releases, the requirements
register said **"Not started" × 35** six weeks after the code shipped, and the headline compression
ratio had **no committed artifact at all** — three different runs wearing one label.

This skill is the repair method and, more usefully, the guards that stop it recurring.

## When to use

- A repository's documents disagree with its code, or with each other.
- A published number cannot be traced to a committed artifact.
- A requirement register, roadmap or status file has not been re-read against the code since the
  code changed.
- You are setting up a new project and want the documents to stay true without a human re-reading
  them every week.

## Method

1. **List every claim, not every file.** Go document by document and write down each *checkable*
   statement: "X is implemented", "the ratio is 0.3352", "no releases yet", "requirement Y is Not
   started". A claim you cannot check is a claim you cannot defend — either attach a check or
   soften the sentence.

2. **Give each claim a source of truth, or withdraw it.** Three grades, in order of preference:
   - **derived** — a committed artifact (results JSON, manifest, changelog heading) that a script
     reads. Best: it cannot drift, only move.
   - **cited** — a named module or test file, which at least must exist.
   - **withdrawn** — no artifact exists. Say so, in the document, with the reason. *"This figure is
     withdrawn: the run that produced it was overwritten when a later run reused its file names"* is
     a sentence a reader can trust; a silently replaced number is not.

3. **Recompute before rewriting.** Every number in the sweep comes from a command whose output was
   read — not from the previous document, and not from memory. When two documents disagree, the
   artifact decides; when there is no artifact, the number is withdrawn.

4. **Fix the structural cause, not just the sentence.** A status should name the module and the test
   that back it, in the same row, so the next reader can check it without a sweep. "Not started" is
   not a safe default: it was wrong for 30 of 35 rows for six weeks.

5. **Add the guards, and mutation-test each one.** A guard that has never been seen to fail is a
   comment. For every guard: reintroduce the defect, watch it go red, restore, watch it go green.
   Two are worth copying into any repo (`scripts/`, both dependency-free):
   - `check_cited_paths.py` — every tree-qualified path a document names must exist;
   - `check_derived_facts.py` — read a fact from its source file and assert the prose agrees
     (this is what catches "no releases yet" when the CHANGELOG has two).

6. **Make the strongest guard a gate.** A checker that reports is an advisory nobody reads. Run it
   with `--strict` in CI on the day the figures agree — that is the day it becomes a gate.

7. **Re-read what you changed, through the API.** A pushed commit is not a finished one; read the
   file back and confirm the content, not the intention.

## The two failure modes that hide inside this one

- **A number with no artifact can only be replaced by another number nobody can check.** Prefer
  withdrawing it to re-quoting it.
- **"Absent from the environment" is not "absent from the estate."** Tools recorded as unavailable
  for weeks were sitting in a sibling repository's `bin/`. Before you write "not measured because
  the binary is missing", search the estate. In that case it changed a decision (the real gap was
  23.49 %, not the 6.59 % the blocked measurement suggested).

## Key files

- `scripts/check_cited_paths.py` — the cited-path guard; takes a repo root and a list of documents.
- `scripts/check_derived_facts.py` — the derived-fact guard; takes a small JSON config.
- `references/failure-catalogue.md` — the six real drifts, what each looked like, and the guard that
  catches it.
- `references/mutation-testing.md` — how to prove a guard works, with the four mutations that
  exposed guards which passed for the wrong reason.

## Gotchas

- **Prose wraps.** A guard that matches a line will fail on where a sentence breaks; match a
  paragraph or a normalised blob. One guard here failed exactly this way on its first run.
- **Timings are not sizes.** A doc asserting "6.0× the time" will drift every re-run on a shared
  machine (it moved 21×–24× across three runs). Pin the exact figures that are exact, and assert only
  that a timing claim *exists*.
- **A test that depends on the machine tests the machine.** A guard that looked for a missing binary
  passed locally and failed in CI, because the runner had the binary. Stub the lookup, do not trust
  the box.
- **Mutation-test the guard, not the fix.** Adding the missing sentence back must turn the guard red;
  if it does not, the guard is measuring something else.
- **Do not rewrite history to look consistent.** Append a correction to a historical entry; a
  document that quietly changes its past is a document nobody can audit.

## Source projects

`lexora` — the sweep and all eleven guards; `audit` — the log entry and the owner-TODO pattern;
`knowledge` — issue 0004, "a number in a document that nothing recomputes".
Related skill: `browser-compression-with-measured-claims` covers the same instinct for one class of
claim (a compression table generated from a measured corpus). This skill generalises it to every
claim a repository makes about itself.
