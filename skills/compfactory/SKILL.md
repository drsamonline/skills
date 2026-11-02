---
name: compfactory
description: The development workspace that builds every CHCE engine in order: a PowerShell and shell script set to build all, bump the vendored-source pin, and sync the repositories.
metadata:
  title: "Compfactory — the CHCE build workspace"
---

# Compfactory — the CHCE build workspace

The workspace the CHCE multi-repository project is developed in. It holds no product code: it holds the scripts that build all the engines in the right order, move the vendored-source pin, and keep the repositories in step.

## When to use

- Several repositories must be built in a fixed order and kept on the same source pin.
- You need one command that rebuilds the family, on Windows or on a shell.
- You are coordinating a submodule bump across consumers.

## Method

1. Build everything with `scripts/build-all.ps1` — the order lives there, in one place.
2. Move the vendored source with `scripts/bump-hcs.ps1` rather than editing pins by hand in each consumer.
3. Sync the repositories with `scripts/sync.ps1` on Windows and `scripts/sync.sh` elsewhere; keep the two in step deliberately, since they are the same operation twice.
4. Keep the workspace brief in `AGENT_PROMPT.md` and the map in `PROJECT_OVERVIEW.md` so the scripts are not the only documentation.
5. Run the sync on dispatch (`.github/workflows/dispatch-sync.yml`) rather than on a schedule — a sync is a decision.

## Key files / entry points

- `scripts/build-all.ps1`, `scripts/bump-hcs.ps1`.
- `scripts/sync.ps1`, `scripts/sync.sh`.
- `.github/workflows/dispatch-sync.yml`.
- `AGENT_PROMPT.md`, `PROJECT_OVERVIEW.md`.

## Gotchas

- A PowerShell script and a shell script that do "the same thing" drift; change both in one commit.
- A workspace repository that grows product code stops being a workspace.
- Bumping a pin in one consumer and not the others produces a family that cannot be built together.
- A scheduled sync fights a human's in-flight change; dispatch is the right trigger.

## Source projects

- [compfactory](https://github.com/drsamonline/compfactory) — the build-order, pin-bump and sync scripts.
