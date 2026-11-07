---
name: git-and-release-automation
description: "The commit-to-release path: split and stage changes, write a Conventional Commit, gate on lint and tests, push safely, run the CI pipeline with quality gates, and produce the user-facing changelog report from merged PRs. Use when committing, pushing, setting up or fixing CI/CD, adding a quality gate, choosing a deployment strategy, or publishing a changelog."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Git, CI and release automation"
  category: "ci-and-release"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "git-commit, push-to-github, ci-cd-and-automation, changelog-report"
---

# Git, CI and release automation

One pipeline in five stages, each with its own failure mode. Commits fail on message quality and accidental secrets; pushes fail on an unverified local state; CI fails on skipped gates; deploys fail without a rollback path; changelogs fail on invented entries. The method below is ordered so a mistake is caught at the cheapest stage.

## When to use

- Changes need committing, possibly split across several logical commits.
- A push should be the final safety gate after lint and tests.
- CI/CD is being set up or repaired, or a quality gate added.
- A changelog or release note must be generated from merged PRs.

## Method

1. Read the repository's own rules first (CONTRIBUTING, commit conventions, hooks) — they win over any default here.
2. Before staging, check for an operation in progress (merge, cherry-pick, revert, rebase) and for unmerged files. If one is in progress, do not unstage or split: the index holds that operation's result, and unstaging drops work. Commit it with the prepared message.
3. Examine the changes and stage by logical unit; never use interactive add (`-p`, `-i`) because it waits for a human.
4. Scan the staged file list for secrets (.env, credentials, private keys) before committing.
5. Write the Conventional Commit message: type, optional scope, imperative subject of 72 characters or less with no trailing period, body for the why, and `BREAKING CHANGE:` footer when applicable.
6. Commit, then verify the commit is what you intended (`git show --stat`, status clean).
7. Push only after lint and tests pass locally, and treat the push as the last gate rather than the first.
8. In CI, make the gates unskippable: if lint fails, fix the rule violation; if a test fails, fix the code. Never disable the check to get green.
9. Choose the deployment strategy from the risk: preview per PR, feature flags for staged rollout, and a rollback path that does not require a redeploy (disable the flag).
10. Keep production secrets out of CI; use separate CI credentials.
11. For a changelog, resolve the date window, discover repos, collect merged PRs only (closed-unmerged never appear), filter to the configured product scope, and write user-facing entries — title, contributors, plain-English detail. Never invent an entry for an unlabelled PR; judge from title and changed files, and say when you inferred.
12. Render the changelog from the print template with embedded fonts and no network at render time, then verify page breaks before delivery.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`git-commit`](references/git-commit/) | Conventional Commit workflow: operation-in-progress handling, staging, message format, safety rules. |
| [`push-to-github`](references/push-to-github/) | The final gate: run the checks, then push. |
| [`ci-cd-and-automation`](references/ci-cd-and-automation/) | CI pipelines, unskippable quality gates, deployment strategies, feature flags, rollback, dependency automation. |
| [`changelog-report`](references/changelog-report/) | The changelog report: config, PR collection, entry writing, print-optimised HTML template, PDF render and delivery. |

## Key files / entry points

- `references/git-commit/` — message format, types, breaking changes, the ordered workflow and safety rules.
- `references/push-to-github/` — the pre-push check-and-push gate.
- `references/ci-cd-and-automation/` — pipeline configuration, quality gates, deployment strategies, rollback, dependency automation.
- `references/changelog-report/` — the report template, config, PR collection, entry writing, print CSS and delivery.

## Gotchas

- Unstaging during an in-progress merge discards the resolution.
- An empty commit to 'retry' CI hides the real failure.
- A skipped gate is a decision to ship unverified code; make that decision explicitly or not at all.
- Changelog entries invented for unlabelled PRs are the fastest way to lose reader trust.
- Linking web fonts at render time breaks an offline or sandboxed PDF build.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `git-commit` — no licence file shipped with the source
- `push-to-github` — no licence file shipped with the source
- `ci-cd-and-automation` — no licence file shipped with the source
- `changelog-report` — no licence file shipped with the source
