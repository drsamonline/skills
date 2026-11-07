# LUT library (authoring)

`index.json` is the agent-consumed catalog of color-grade looks. Each entry resolves
on demand — no `.cube` bodies are committed to the repo.

Each look has:

- `id`, `description`, `tags`, `intensity` — matching + application metadata.
- `url` (optional) — a hosted `.cube` downloaded, validated, and frozen at resolve
  time, exactly like bgm/image assets.
- `params` (optional) — a deterministic `buildCube` spec used offline (`--local-only`)
  or as a fallback if the `url` download/validation fails.

An entry needs at least one of `url` or `params`; prefer both (CDN url with a params
fallback) so resolution is never blocked on the network.

## Hosting a new look (operators)

1. Generate the `.cube` (e.g. `resolve -t lut --params '{...}'` or a graded export).
2. Upload it to the public CDN origin bucket:

   ```
# [MANUS OVERRIDE] Disabled upstream credential/provider path; use the Manus media contract instead.
   ```

> **[MANUS OVERRIDE]** This upstream credential or provider route is disabled in Manus. Use Manus-native media generation and write the project ledger as specified in `_manus-overrides/media-generation.md`; use a permitted local fallback only when Tier 1 does not fit.

3. Add an entry to `index.json` with that `url` (and ideally a `params` fallback).
