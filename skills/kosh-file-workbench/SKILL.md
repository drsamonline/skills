---
name: kosh-file-workbench
description: Split, squeeze, archive, verify and inspect files through one engine, a CLI and a local web UI — and where a CHCE compression engine is installed, drive it across a process boundary instead of reimplementing its format.
metadata:
  title: "Kosh — the file workbench that drives engines across a process boundary"
---

# Kosh — the file workbench that drives engines across a process boundary

One engine, one CLI, one local UI, and a rule about honesty: where a CHCE engine is installed,
Kosh calls it rather than pretending to be it.

## When to use

- You need to split a large image into parts that prove themselves, pack a directory into a verified container, or check a container without extracting it.
- You are about to reimplement a compression format that a CHCE engine already ships — call the engine instead.
- You want a repeatable chain of file steps written down as a recipe rather than remembered as shell history.

## Method

1. Ask what is present first: `kosh engines` lists the CHCE engines found and their versions — that answer decides whether a step is delegated or done in-process.
2. Sample before committing: `kosh scan photo.raw` answers "would the engine help?" from a sample rather than from the whole file.
3. Optimise: `kosh optimize photos/ --level 2 --strip` (PNG/ZIP/GZIP/JPEG, losslessly smaller).
4. Pack and prove: `kosh pack project/ -o project.kosh`, then `kosh verify project.kosh` — verification needs no extraction.
5. Split: `kosh split backup.img --size 700M -o parts/` produces parts that prove themselves.
6. Chain steps as a recipe: `kosh run recipe.yaml`, which writes a manifest of what ran.
7. Use the same engine in a browser with `kosh ui`.

## Key files / entry points

- `kosh/cli.py` — the command surface (`engines`, `scan`, `optimize`, `pack`, `split`, `verify`, `run`, `ui`).
- `kosh/core/engine.py` — the process-boundary adapter to a CHCE engine.
- `kosh/core/` — `archive.py`, `optimize.py`, `pack.py`, `splitjoin.py`, `recipe.py`, `bench.py`, `doctor.py`, `util.py`.
- `docs/FORMAT.md` — the container format; `docs/RECIPES.md` — the recipe language; `docs/FINDINGS.md` — what was measured; `docs/ORIGINALS.md` — what is untouched.
- `.github/workflows/fuzz.yml` — the fuzz job, alongside `ci.yml` and `release.yml`.

## Gotchas

- **Delegating is the point.** A reimplemented codec is a second source of truth for a format and will drift from the engine; the boundary exists to prevent that.
- **`verify` must not extract.** Verification that writes files cannot be run on a suspect archive; keep the check read-only.
- **The engine may not be installed.** `kosh engines` first, every time — a missing engine is a different code path, not an error to retry.
- **A recipe is a manifest, not a shell script.** Steps run in-process with a recorded manifest, so a step that shells out loses the record.
- **Licence is MIT here, unlike the rest of the fleet.** Check before copying a header from a PolyForm repo.

## Source projects

- [kosh](https://github.com/drsamonline/kosh) — the engine, CLI, recipe language and docs.
- [heavenzip](https://github.com/drsamonline/heavenzip) — the CHCE orchestrator whose prebuilt engines Kosh drives.
