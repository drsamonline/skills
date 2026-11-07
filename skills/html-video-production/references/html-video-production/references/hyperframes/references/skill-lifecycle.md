# Skill installation and freshness

Read this reference when installing or updating skills, diagnosing unexpected workflow behavior, or running HyperFrames setup in CI.

HyperFrames installs the core set eagerly and workflow skills lazily.

- **Core set:** `/hyperframes`, the `hyperframes-*` domain skills, and `/media-use`.
> **[MANUS OVERRIDE]** This upstream credential or provider route is disabled in Manus. Use Manus-native media generation and write the project ledger as specified in `_manus-overrides/media-generation.md`; use a permitted local fallback only when Tier 1 does not fit.

## What `init` does

> **[MANUS OVERRIDE]** This upstream credential or provider route is disabled in Manus. Use Manus-native media generation and write the project ledger as specified in `_manus-overrides/media-generation.md`; use a permitted local fallback only when Tier 1 does not fit.

The `--skip-skills` CLI flag is temporarily ignored. CI and tests may opt out with `HYPERFRAMES_SKIP_SKILLS=1`.

## Diagnose and update

```bash
npx hyperframes skills check
npx hyperframes skills check --json
# [MANUS OVERRIDE] Disabled upstream credential/provider path; use the Manus media contract instead.
# [MANUS OVERRIDE] Disabled upstream credential/provider path; use the Manus media contract instead.
npx hyperframes skills
```

- `skills check` exits non-zero when an installed skill is stale or the core set is incomplete. Workflows available on demand but not installed are not failures.
- Bare `skills update` refreshes the core set and everything already installed, prunes unpublished skills, and does not expand the workflow set.
- Named `skills update <name...>` also installs those named workflows or domain skills.
- Bare `skills` installs the full published set explicitly.

> **[MANUS OVERRIDE]** This upstream credential or provider route is disabled in Manus. Use Manus-native media generation and write the project ledger as specified in `_manus-overrides/media-generation.md`; use a permitted local fallback only when Tier 1 does not fit.

The CLI may print a one-line stale-skill reminder during `render`, `lint`, or `check`. Treat a failed update as a visible tool failure; do not continue from a remembered workflow contract.
