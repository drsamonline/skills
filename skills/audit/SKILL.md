---
name: audit
description: The change log for a multi-repo fleet: collectors that read state through the GitHub API, a dated markdown log of what was measured and fixed, and scheduled health and licence checks.
metadata:
  title: "Fleet audit — measured, logged, evidenced"
---

# Fleet audit — measured, logged, evidenced

A repo that exists to answer *"what did we change, and what proves it worked?"* across a whole fleet. Collectors read repository state through the API into `state/*.json`; the findings are written as dated markdown under `log/YYYY-MM/`; two scheduled workflows re-check health and licences.

## When to use

- You maintain many repositories and need one place that records what was measured and what was fixed.
- You want audit conclusions backed by fetched bytes and status codes, not by memory.
- You need a repeatable licence and health sweep across a fleet.

## Method

1. Collect with the API, not with raw fetches, for anything that can change: `tools/collect.py` walks the repos and writes `state/repos.json`, `state/readmes.json`, `state/schedules.json`, `state/licences.json`.
2. Diff a fresh collection against the last one with `tools/diff.py` so a change is a delta, not a re-read.
3. Derive fleet health with `tools/fleet_health.py` into `docs/health.json` and serve it from `docs/index.html`.
4. Check licences with `tools/licence_check.py`; normalise licence badges with `tools/fix_licence_badges.py` rather than editing them by hand.
5. Write each session up as one dated file under `log/YYYY-MM/` — what was measured, what was fixed, and the evidence. A finding with no evidence line does not go in.
6. Schedule the checks in `.github/workflows/health.yml` and `licence-check.yml`.

## Key files / entry points

- `tools/collect.py`, `tools/diff.py`, `tools/fleet_health.py`, `tools/licence_check.py`, `tools/fix_licence_badges.py`.
- `state/*.json` — the collected snapshot; `docs/health.json` — the derived view.
- `log/YYYY-MM/*.md` — the dated record.
- `.github/workflows/health.yml`, `.github/workflows/licence-check.yml`.

## Gotchas

- Reading state through raw file fetches gives you a cached answer with no status code; the API tells you whether the thing exists.
- A log entry that states a fix without the command or the response that proved it is an opinion.
- The collector is the slow part of the loop — batch it, and diff rather than re-collect per question.
- Licence detection is a guess unless the file is read; record what was read, not what the repo's language suggests.

## Source projects

- [audit](https://github.com/drsamonline/audit) — the collector/diff/health tools, the state snapshots and the dated log.
