---
name: heavenzip
description: The CHCE orchestrator that chains prebuilt compression binaries into one pipeline: profile-driven configuration, a binary-sync workflow, and the bundling, licensing and permission decisions written down before the code lands.
metadata:
  title: "CHCE orchestrator scaffold"
---

# CHCE orchestrator scaffold

The orchestrator that chains prebuilt CHCE binaries into one pipeline. The tree is deliberately a **scaffold**: `bin/` and `src/orchestrator/` hold only `.gitkeep`, and what exists is the configuration model, the sync workflow and the written decisions. Read it as a design that has been pinned down, not as a running program.

## When to use

- You are laying out a multi-binary pipeline before writing the orchestrator.
- You need to decide — in writing — how bundled third-party binaries are licensed and permissioned.
- You want configuration profiles per content type rather than one global settings file.

## Method

1. Model the pipeline in `config/syc.ini` and keep one profile per content class: `config/profiles/text.ini`, `config/profiles/media.ini`, `config/profiles/max-ratio.ini`.
2. Deliver the binaries with `.github/workflows/sync-binaries.yml` rather than committing them; `bin/` stays a placeholder directory.
3. Write the decisions down before the code: `docs/BUNDLING.md`, `docs/LICENSING_DECISION.md`, `docs/PERMISSIONS.md`, `docs/TOOL_MANIFEST.md`.
4. Keep the agent brief in `AGENT_PROMPT.md` and the scope in `PROJECT_OVERVIEW.md` so a contributor knows what is in and out.
5. Keep `tests/` present but empty until there is something to test — an empty test directory is honest; a fake test is not.

## Key files / entry points

- `config/syc.ini`, `config/profiles/*.ini` — the pipeline and its profiles.
- `docs/TOOL_MANIFEST.md`, `docs/BUNDLING.md`, `docs/LICENSING_DECISION.md`, `docs/PERMISSIONS.md`.
- `.github/workflows/sync-binaries.yml` — how `bin/` is populated.
- `AGENT_PROMPT.md`, `PROJECT_OVERVIEW.md`.

## Gotchas

- A scaffold described as a working orchestrator is a false claim; say which parts are placeholders.
- Bundling third-party compressors makes their licences your problem — the decision has to be recorded, not assumed.
- Profiles that differ only in one key drift; keep the shared keys in `syc.ini` and the difference in the profile.
- Binaries in the tree bloat history; sync them from Releases or a build artifact.

## Source projects

- [heavenzip](https://github.com/drsamonline/heavenzip) — the profile model, the sync workflow and the bundling/licensing documents.
