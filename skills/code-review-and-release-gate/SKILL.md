---
name: code-review-and-release-gate
description: "Review a diff, pull request or release candidate and produce a prioritised, evidence-backed verdict: bugs, security issues, N+1 queries, code smells, architectural concerns, documentation coverage, and a ship-or-block call. Use for pull-request review, a code-quality audit, a pre-merge check, or deciding whether a release candidate is safe to ship."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Code review and release gate"
  category: "code-quality"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "code-reviewer, final-release-review"
---

# Code review and release gate

One posture for two scales. At the **diff** scale you are looking for defects a machine cannot see. At the **release** scale you are deciding whether a candidate is safe to ship, which is the same judgement with a wider blast radius. Both end in an ordered list of what must change before approval, and both require that a claim about behaviour is backed by something you ran or read.

## When to use

- A pull request or diff needs review before merge.
- A release candidate or release plan needs a ship-or-block recommendation.
- A codebase needs a quality or security audit.

## Method

1. Read the intent first: the PR description, linked issues and any author comments. A review that argues with a documented decision wastes everyone's time.
2. Map the diff: what changed, what it touches, and which existing behaviour it can break. For a release, establish the diff base and confirm the candidate's ancestry rather than assuming it.
3. Hunt in priority order: correctness and data loss, then security (injection, XSS, insecure deserialization, secrets), then performance pathologies (N+1 queries, unbounded loops, missing indexes), then design and naming.
4. Prove every finding. Cite the file and line, show the failing case or the query, and say what breaks. A finding you cannot point at is a hunch — label it as one or drop it.
5. Report critical issues the moment you find them rather than holding them for the end.
6. Never block on a style preference a linter already covers, and acknowledge the author's reasoning before proposing an alternative.
7. For a release, also check: versioning policy compliance, documentation coverage (check open docs PRs before claiming a gap), migration path, and the unblock checklist.
8. Write the verdict as a required template: ordered findings table, then the recommendation with the specific unblock conditions.
9. Do not run the approval action yourself — hand the maintainer the body to paste, and never publish an undisclosed vulnerability.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`code-reviewer`](references/code-reviewer/) | Diff-scale review: prioritised categories, security and performance patterns, constraints, output template. |
| [`final-release-review`](references/final-release-review/) | Release-scale review: gate policy, candidate mapping, contract audit, documentation coverage, ship-or-block report. |

## Key files / entry points

- `references/code-reviewer/` — the review workflow, pattern library (bad/good examples), constraints, output template.
- `references/final-release-review/` — the release-readiness workflow, deterministic gate policy, report format, unblock checklist.

## Gotchas

- Style opinions dressed as blockers erode trust in the review.
- A release review that only reads the diff misses contract and documentation regressions.
- Never switch or reset the maintainer's checkout, and never invoke the release-prep automation.
- Approving silently on someone's behalf is not a review.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `code-reviewer` — no licence file shipped with the source
- `final-release-review` — no licence file shipped with the source
