---
name: kitbox
description: Assemble a large offline utility suite as a single HTML file: one template, one build, and a test suite that fuzzes, checks accessibility, exercises interaction and verifies the minified build is the same app.
metadata:
  title: "Kitbox"
---

# Kitbox — 493 tools in one HTML file, with the checks that make that claim true

Kitbox ships **493 tools across 27 categories in one HTML file** (`kitbox.html`, about 1101 KB), with no install, no build step for the user, no dependencies at runtime and no network call. The interesting part is not the size — it is that every one of those claims is checked by a script.

## When to use

- You are adding to an offline single-file app that has grown past the point where a human can re-check it by hand.
- You want a tool registry that cannot drift from the tools it lists.
- You need a build whose minified output is proven to behave like the source.

## Method

1. Keep the page generated: `src/index.template.html` plus `src/js/`, assembled by `tools/build.py` into `kitbox.html`. Never hand-edit the built file.
2. Register tools through generated data — `tools/gen-all-tools.js` writes the tool list and `tools/gen-codes.js --check` verifies the codes — so a tool that is not registered is a build failure, not a missing feature.
3. Run the checks as separate, named jobs: `test/smoke.js`, `axe.js` (accessibility), `fuzz.js`, `interact.js`, `deep.js`, `links.js`, and `minified.js` against the minified build. `npm run check` chains them with lint, types and the generated-data checks.
4. Build the distributable with `npm run dist` (`tools/dist.py`) and keep `latest/` as the published artefact.
5. Treat badges as generated: `tools/check-badges.js` fails when the badge numbers stop matching the app.

## Key files / entry points

- `src/index.template.html`, `src/js/` — the source; `kitbox.html` — the build.
- `tools/build.py`, `tools/minify.js`, `tools/dist.py` — the build chain.
- `test/*.js` — smoke, accessibility, fuzz, interaction, deep, links, minified.
- `ids.json`, `codes.json`, `ALL_TOOLS.md` — the generated registry.
- `package.json` — `check` is the whole gate in one command.

## Gotchas

- A generated page that someone edits by hand is overwritten on the next build; the source of truth is `src/`.
- Fuzz and interaction tests are what keep a 493-tool page from regressing silently — the smoke test alone proves nothing at this size.
- Testing the minified build separately is not duplication: it is the only check that the minifier did not change behaviour.
- `npm run lib` and `tsc` run over the built library, so a type error can surface only after a build.

## Source projects

- [kitbox](https://github.com/drsamonline/kitbox) — the template/build split, the generated tool registry and the seven-level test suite.
