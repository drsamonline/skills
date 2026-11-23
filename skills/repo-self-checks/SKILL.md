---
name: repo-self-checks
description: The tools/check-*.mjs family a no-build repository runs on itself — links that resolve, a version that matches its changelog, exported symbols that carry JSDoc, a README test count that is true, and assets that declare their licence. Use when adding CI to a static site, when a README number drifts, or when a repository needs a cheap honest gate.
metadata:
  title: "The check-* self-check family"
---

# The `check-*` self-check family

Five small, dependency-free scripts that each answer one question about a repository and
exit non-zero when the answer is wrong. They live in `tools/` and are run by CI, and each
was written because a claim nothing else checked had already gone stale: a link to a file
that was deleted, a `VERSION` no changelog agreed with, a README count that described a
test suite from three commits ago.

## When to use

- A static site or single-file app needs CI that costs nothing to run.
- A README states a number (tests passed, tools, checks) and you want it to be true.
- You are adding a second repo to a check that already exists in a first, and want the
  flag set that makes it portable (`--warn`, `--root`, `--ignore`).
- A build is green but the documentation is stale — these are the checks that catch it.

## Method

1. **`tools/check-links.mjs` — every local `href` and `src` resolves.**
   `node tools/check-links.mjs [dir]`; `--ignore <prefix>` skips pages whose path relative
   to the root starts with that prefix. Use the ignore flag for build fragments that carry
   a doctype but are concatenated later, because their paths resolve against the output,
   not against where the fragment sits.
2. **`tools/check-meta.mjs` — the version and licence a repo states agree with its files.**
   It compares `VERSION` against the newest heading in `CHANGELOG.md`, `package.json`
   against `VERSION`, and the licence named in `README.md` against `LICENSE`. Absent files
   are skipped, so the same script runs in any repo. `--warn` reports and exits `0`.
3. **`tools/check-docs.mjs` — every module-level export carries a JSDoc block.** The rule is
   deliberately narrow: a doc comment directly above the export, or above the line that
   starts it; class methods are exempt because the class block explains the object. `--src`
   points at the source directory (default `play/src`), `--list` prints what is missing,
   `--warn` exits `0`.
4. **`tools/check-claims.js` — a README number is a claim.** It reads the first `N passed`
   in `README.md`, runs `test-node.js`, and fails on a mismatch. A README with no `N passed`
   is itself a failure, because then nothing can be checked.
5. **`tools/check-assets.mjs` — every binary asset is declared.** Every file with an asset
   extension needs an entry in `ASSETS.json` naming a `source` (a URL, or `own`) and a
   `licence` from the allow list; an entry with no file behind it fails too, so the manifest
   cannot rot. `--root ..` points it at another repository.
6. **`tests/page-smoke.js` — drive the page, do not just parse it.** It loads the page in
   jsdom (a test-only dependency) and asserts the behaviour the links check cannot see.
7. **Adopt the measurement before the rule.** Every check with `--warn` exists for a repo
   with a known drift: run it in warn mode, get the number into the record, fix the drift,
   then remove `--warn` in the commit that makes it pass.

## Key files

- `tools/check-links.mjs`, `tools/check-meta.mjs`, `tools/check-docs.mjs`,
  `tools/check-claims.js`, `tools/check-assets.mjs` — the five checks.
- `tests/page-smoke.js` — the jsdom page test.
- `ASSETS.json` — the asset manifest `check-assets.mjs` reads, and the allow list of licences
  it enforces (a CC-BY-SA sprite carries share-alike into every project that recolours it).
- `CHANGELOG.md`, `VERSION`, `package.json`, `LICENSE`, `README.md` — the five files
  `check-meta.mjs` cross-references.
- The CI workflow that calls them — each check is one `run:` step and needs no install.

## Gotchas

- **These are copies, and they have diverged.** Measured 2026-11-23: `check-links.mjs` in 13
  repos in 6 distinct versions, `check-meta.mjs` in 9 repos in one version, `check-claims.js`
  in 8 repos in 2 versions, `check-assets.mjs` in 5 repos in one version, `check-docs.mjs` in
  4 repos in 2 versions. Adopt from the repo with the newest version, not from whichever one
  you opened first.
- **`check-links` checks what a browser only asks for when you click it.** That is why it
  finds what the runtime smoke test cannot: a tab that is never opened still has links.
- **`--ignore` is for fragments, not for failures.** A prefix that excludes a whole page
  because its links were wrong is a check that has stopped checking.
- **`check-claims` runs the suite.** On a slow suite it doubles CI time; that is the price of
  a README number that is true, and the alternative is a number nobody maintains.
- **A licence allow list is a legal control, not a lint.** Adding an extension to it is a
  licensing decision about every repo that will ever copy that asset.
- **`--warn` that never gets removed is a permanent exemption.** Track it, or the check
  becomes decoration.

## Source projects

- [Hellgate](https://github.com/drsamonline/Hellgate) — the widest set: links, meta, docs and claims side by side.
- [art-kit](https://github.com/drsamonline/art-kit) — `check-assets.mjs` and its licence allow list.
- [code-kit](https://github.com/drsamonline/code-kit) — `check-claims.js`, the README `N passed` gate.
- [game-kit](https://github.com/drsamonline/game-kit) — all four `check-*` scripts in one kit repo.
- [weft8-kit](https://github.com/drsamonline/weft8-kit) — `tests/page-smoke.js` driving a page in jsdom.
