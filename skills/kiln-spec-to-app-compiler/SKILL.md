---
name: kiln-spec-to-app-compiler
description: A deterministic compiler that turns a small specification into a complete offline application as one HTML file: no model in the loop, no network, nothing to install. `python3 -m kiln pipeline` writes, builds and verifies in one command; a generated app is about 50 KB.
metadata:
  title: "KILN — spec in, finished app out"
---

# KILN — spec in, finished app out

A deterministic compiler: a small specification goes in, one working offline HTML application
comes out. There is no model in the loop and no network, so the same spec produces the same app.

## When to use

- You are about to hand-write yet another single-file offline app and its spec is already known.
- You need a generated app you can read, verify and re-generate — not a scaffold you then own by hand.
- You want a deterministic pipeline: spec → build → verify, with the gates recorded.

## Method

1. Whole pipeline in one command: `python3 -m kiln pipeline "a reading log with tags and a rating" --zip`. No `pip install`, no `npm install`, no `.env`, no API key, no network.
2. Or step by step: `python3 -m kiln new "a notes app with tags, search and export"`, then `python3 -m kiln build specs/app-notes.md -o out`, then `python3 -m kiln verify out/app-notes`.
3. Keep the spec in `specs/` — it is the source of truth; the generated HTML is output and is regenerated, not edited.
4. Read the guide for the part you are changing: `GUIDE-SPEC-REF.md` (spec syntax), `GUIDE-PATTERNS.md`, `GUIDE-FEATURES.md`, `GUIDE-LIMITS.md`, `USAGE.md`.
5. Look at `demo.html` for a gallery of every spec, `studio.html` for the studio surface and `fleet/index.html` for the fleet view before adding a new shape.
6. Verify with the suite in `tests/` and the `kiln.yml` CI workflow; the README badges report tests and gate status, and `docs/badge.json` is the machine-readable status.

## Key files / entry points

- `kiln/` — the compiler package (`python3 -m kiln`).
- `specs/` — the specifications; `schema/` — the spec schema; `catalogue/` — the catalogue the compiler reads.
- `templates/` — the app templates the generator fills.
- `USAGE.md`, `GUIDE-*.md`, `SPEC-SHAPE.md` — the reference set.
- `tests/`, `.github/workflows/kiln.yml` — the verification path.

## Gotchas

- **Deterministic is the contract.** Two builds of the same spec must produce the same bytes; anything that reads the clock, the network or a random seed in the generator breaks that.
- **The generated app is output, not source.** Editing `out/*.html` by hand means the next build silently discards the edit — change the spec or the template.
- **`GUIDE-LIMITS.md` is not decoration.** It states what the compiler does not generate; a spec that asks for more produces a working app with a missing feature, not an error.
- **A prompt bridge exists, but the model is not in the build.** Keep generation model-free, or the "same spec, same app" claim is gone.
- **50 KB is the target, not a limit to police.** A generated app that balloons usually means a template is inlining something that should be a reference.

## Source projects

- [KILN](https://github.com/drsamonline/KILN) — the compiler, the spec reference, the demo gallery and the fleet view.
