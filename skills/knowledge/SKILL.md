---
name: knowledge
description: Keep an indexed, searchable record of what every run did and why every failure was fixed, with a retention rule that keeps failures forever and successes for ninety days.
metadata:
  title: "Knowledge"
---

# Knowledge — a black box for every run log and every resolved problem

Every run log and every resolved problem for the Forge system, indexed and kept so any problem can be understood later. The loop is explicit: a failure becomes a log, a log becomes an issue, an issue that is a *method* becomes a skill.

## When to use

- An automated estate produces more runs than anyone can read, and the same failure keeps being re-diagnosed.
- You need a record that answers "why is this like this" months later.
- You want a retention policy that is a rule rather than a habit.

## Method

1. Write logs as `logs/<repo>/<date>-<run>.md` — one file per run, per repository, date-first so the directory sorts chronologically.
2. When a problem is resolved, write `issues/<id>.md` in the shape **symptom → cause → fix**. That shape is what makes the file reusable; a log without a cause is not knowledge.
3. Regenerate `index.json` with `scripts/build_index.py` — it is a build product, never hand-edited.
4. Apply `retention.json`: **failures are kept forever, successes for 90 days.** Failures are the expensive thing to rediscover.
5. Read it through `docs/index.html`, which loads `index.json`; the repository is private, so the viewer is a local tool rather than a site.

## Key files / entry points

- `logs/<repo>/<date>-<run>.md` — run logs.
- `issues/<id>.md` — resolved problems, symptom → cause → fix.
- `index.json`, `scripts/build_index.py` — the index and its generator.
- `retention.json` — the keep rule.
- `docs/` — the system plan, build order, app master list and the ideas file.

## Gotchas

- The viewer is only useful if the index is current; a stale `index.json` makes the whole black box look empty.
- Free GitHub Pages publishes only from public repositories, so a private repository's `docs/` is a local page — do not plan around it being served.
- A log that records what happened but not the cause turns into a file nobody opens twice.
- Full logs stay here; only a sanitised summary belongs on a public dashboard.

## Source projects

- [knowledge](https://github.com/drsamonline/knowledge) — the log/issue/index layout and the retention rule.
