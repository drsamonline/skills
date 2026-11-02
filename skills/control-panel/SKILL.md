---
name: control-panel
description: An inventory of every workflow across a repository fleet: what runs, when, what calls what, and what is connected to nothing — built by scanning the trees and served as a static page.
metadata:
  title: "Control panel — every workflow, and what calls what"
---

# Control panel — every workflow, and what calls what

Nothing in a large fleet knows its own shape: reusable workflows, callers, schedules, dispatches, and no single place that answers *"what runs, and what calls what?"*. This repo is that place. It scans the trees, derives an inventory, and serves it as a static page — with the gaps listed as data.

## When to use

- You have many workflows across many repositories and no map of them.
- You need to find workflows that nothing calls, or callers pinned to a stale SHA.
- You want the answer as a generated artefact, not as a hand-drawn diagram.

## Method

1. Fetch and scan with `tools/fetch.py` and `tools/scan.py`, writing `docs/inventory.json` — every workflow, its triggers and its `uses:` edges.
2. Derive the interaction graph with `tools/interactions.py` into `docs/interactions.json`, and the caller routes with `tools/plan.py` into `docs/routes.json`.
3. List what is connected to nothing with `tools/gaps.py` into `docs/gaps.json` — an uncalled reusable workflow is a finding, not an error.
4. Simulate the chosen routes with `tools/simulate.py` before changing anything, and check a workflow's shape with `tools/wf_check.py`.
5. Run the scan on a schedule (`.github/workflows/scan.yml`) and verify a commit landed with `tools/commit-and-verify.sh`.
6. Serve `docs/index.html` over the JSON; the page is a view of the inventory, not a second source of truth.

## Key files / entry points

- `tools/scan.py`, `tools/interactions.py`, `tools/plan.py`, `tools/gaps.py`, `tools/simulate.py`, `tools/wf_check.py`.
- `docs/inventory.json`, `docs/interactions.json`, `docs/routes.json`, `docs/gaps.json`, `docs/plan.json`.
- `tools/commit-and-verify.sh` — the post-push check.

## Gotchas

- A `uses:` edge pinned to a commit SHA is a different node from the same workflow pinned to a branch; the graph must keep the ref.
- Callers that point at `@main` look fine in the inventory and are unreproducible in practice — surface the ref, not just the target.
- Scanning raw files without status codes hides a workflow in a repository that no longer exists.
- A push that exited zero is not proof the change landed; verify the tree.

## Source projects

- [control-panel](https://github.com/drsamonline/control-panel) — the scan/graph/gaps pipeline and the commit-and-verify check.
