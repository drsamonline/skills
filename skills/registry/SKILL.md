---
name: registry
description: Keep the estate's facts in versioned JSON files that a dashboard and an agent read from the same place, with each file's producer named and every definition of "built" measured rather than inferred.
metadata:
  title: "Registry"
---

# Registry — the machine-readable truth a dashboard and an agent both read

The central database for the Forge system: the machine-readable truth that the dashboard and the agent both read, so the two cannot disagree about what exists.

## When to use

- Several consumers (a dashboard, a scheduled agent, a report) need the same facts and must not each derive them differently.
- A metric like "built" has drifted into meaning whatever the last script meant.
- You want an empty file to be a visible failure rather than a silent zero.

## Method

1. One file per question, each with a named producer: `repos.json` (metadata and a metadata-completeness score), `deps.json` (the kit dependency graph), `catalog.json` (the estate as nodes and edges), `plan.json`, `queue.json`, `quota.json`, `proposals.json`, `audit-history.json`.
2. Publish counts from the file that owns them — `catalog.json` carries `counts: {kits, apps, edges}` — instead of recounting elsewhere.
3. Define the score before publishing it: the metadata-completeness score is five booleans (description, licence, homepage, Pages, not archived) and explicitly **not** build quality.
4. Measure "built" in `build-status.json` from four signals — a published release, Pages on, the demo URL answering, and the app's own build having succeeded — with `built = release AND pages AND (demo where pages is on)`.
5. Regenerate with `.github/workflows/refresh.yml`; keep `tools/build-status.py` and `tools/manifest.py` as the scripts that decide, and `tools/_gate.py` as the manifest gate for the tools themselves.

## Key files / entry points

- `repos.json`, `deps.json`, `catalog.json`, `plan.json`, `build-status.json`, `queue.json`, `quota.json`, `proposals.json`, `audit-history.json`.
- `tools/build-status.py` — what "built" means, implemented.
- `tools/manifest.py`, `tools/_gate.py` — provenance and the write gate.
- `.github/workflows/refresh.yml` — the producer.

## Gotchas

- **A file with no producer is not an empty result.** `builds.json` has no producer: an empty `builds` list means nothing writes it, not that nothing was built. Measured build status lives in `build-status.json`.
- A metadata score of 5/5 says the fields are filled in, not that the build works — a repository whose build failed on its latest run can still score 5/5.
- A kit is decided by `role`, not by name; a name-based rule silently drops kits declared only in the registry.
- Two definitions of the same number is how `plan.json` ended up carrying both a measured `built` and an older name-matched one; label the difference rather than overwriting it.

## Source projects

- [registry](https://github.com/drsamonline/registry) — the file set, the score definitions and the producer for each.
