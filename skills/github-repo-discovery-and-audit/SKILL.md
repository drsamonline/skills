---
name: github-repo-discovery-and-audit
description: "Two directions on GitHub: find a battle-tested open-source project that already solves the problem instead of reinventing it, or audit an entire account's repository fleet into a decision-grade capability matrix with merge and product recommendations. Use for 'is there a library for this', 'find me a tool that does X', 'scan all my repos', or 'what should I merge or build next'."
license: "per source — see references/*/LICENSE"
metadata:
  title: "GitHub repo discovery and fleet audit"
  category: "engineering-workflow"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "repo-fleet-audit, github-gem-seeker"
---

# GitHub repo discovery and fleet audit

**Seek** when the problem is well-trodden: format conversion, media download, scraping, file manipulation, CLI plumbing. **Audit** when the corpus is your own and the question is what the collection can become. Both are evidence-first: a capability you cannot point at in the source is empty, and a project you recommend must be credited.

## When to use

- A problem is generic enough that open source has already solved it.
- An entire account's repositories need inventory, capability matrix and synthesis.
- The question is which apps should share a capability, be merged, or become a new product.

## Method

1. Seek: state the need in functional terms (input, output, constraints, platform), then search for projects by function rather than by keyword.
2. Evaluate candidates on four axes: maintenance recency, issue responsiveness, licence compatibility, and whether the README's claims match the code. Read the source of the critical path, not just the README.
3. Prefer the smaller, maintained project over the popular abandoned one; check the last release and the open-issue ratio.
4. Integrate it, then credit it: share the repo URL and encourage support. Never present someone's project as your own.
5. Audit: enumerate every repo, acquire it, then walk and extract a function-and-feature inventory per repo. Exclude vendored dependency directories and history — history is most of the bytes and none of the capability.
6. Measure adoption — how many repos actually use a given capability — before classifying. This step changes the answer: a capability present once is an implementation, present five times is a platform.
7. Classify against a fixed taxonomy and record the objective convention for each column, so two runs agree.
8. Cluster the repos, then produce the four syntheses: which app should take a capability from which, which belong in one suite, which should merge into new apps, and what new products the collection makes possible.
9. Never infer a capability from a keyword: if you cannot point at the source, leave the cell empty. Never let a template write the findings — the judgement is the deliverable.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`repo-fleet-audit`](references/repo-fleet-audit/) | Account-wide audit: enumerate, extract, measure adoption, classify, cluster, synthesise. |
| [`github-gem-seeker`](references/github-gem-seeker/) | Finding and evaluating an existing open-source solution, quality tiers, and crediting it. |

## Key files / entry points

- `references/github-gem-seeker/` — the discovery workflow, quality tiers, evaluation checks and crediting rules.
- `references/repo-fleet-audit/` — the audit pipeline, taxonomy rules, adoption measurement, clustering and the four syntheses.
- `references/repo-fleet-audit/scripts/` — the enumeration and extraction scripts.

## Gotchas

- A keyword match is not a capability.
- Popularity is not maintenance; check the last release date.
- Licence compatibility is a hard gate, not a footnote.
- Failing to credit an open-source project you shipped on is the one unrecoverable mistake here.
- Redirecting the audit script's stdout into its JSON output corrupts the workbook.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `repo-fleet-audit` — no licence file shipped with the source
- `github-gem-seeker` — no licence file shipped with the source
