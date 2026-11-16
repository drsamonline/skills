---
name: toolworks-merged-catalogue
description: One offline index over two independently built toolboxes — 565 tools from the TTB browser extension and 404 from the All4ONE Windows binary, 969 rows with search and a source on every entry — built by reading both catalogues and modifying neither repository.
metadata:
  title: "Toolworks — merging two catalogues without touching either"
---

# Toolworks — merging two catalogues without touching either

Two toolboxes were built separately and neither knew what the other had. This repository is the
index that does: one page, every tool, searchable, offline.

## When to use

- Two of your projects overlap and you need one searchable index before you decide what to merge, rename or retire.
- You must add an index without changing either source repository — its code, history, licence and users stay as they are.
- You need provenance on every row, so a wrong entry can be traced back to the catalogue it came from.

## Method

1. Read the two catalogues as data, not as code: TTB ships 565 entries, All4ONE 404, and this repository only reads them.
2. Merge into `data/catalogue.json` with a `source` on every tool — never a row without one, or a duplicate becomes unattributable.
3. Record where each half came from and what was changed in `SOURCES.md`.
4. Serve the index from `index.html`: 969 rows, search, and a filter by source and by group, working offline.
5. Check the merge with `tools_check.py` and the `check.yml` workflow before publishing.
6. When a tool looks wrong or missing, use the issue templates (`missing-tool.yml`, `wrong-entry.yml`) rather than editing the source repositories.

## Key files / entry points

- `data/catalogue.json` — the merged catalogue; every row carries a `source`.
- `index.html` — the whole index: 969 rows, search, source and group filters.
- `SOURCES.md` — provenance for both halves and what was changed.
- `tools_check.py`, `.github/workflows/check.yml` — the integrity check.
- `windows/README-WINDOWS.md` — the Windows-side note.

## Gotchas

- **The two sources are not merged, they are indexed.** A tool that exists in both is two rows with two sources until a human decides; silently de-duplicating loses the provenance that makes the index trustworthy.
- **Neither original repository is touched.** That is the rule the project is built on — an index that edits its sources cannot be re-run.
- **Counts are the claim.** 969 = 565 + 404; a check that lets the total drift from the two catalogues turns the headline into a guess.
- **Offline means no API.** The page reads a local JSON file; a search that needs a server is a different product.

## Source projects

- [TOOLWORKS](https://github.com/drsamonline/TOOLWORKS) — the index, the merged catalogue and its provenance.
- [TTB](https://github.com/drsamonline/TTB) — the browser extension's 565-entry catalogue (read, not modified).
- [All4ONE](https://github.com/drsamonline/All4ONE) — the Windows binary's 404-entry catalogue (read, not modified).
