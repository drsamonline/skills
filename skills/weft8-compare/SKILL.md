---
name: weft8-compare
description: Five small jobs written three times — for the Weft-8, for x86-64 and for AArch64 — laid side by side so the question of what a computer really is stops being abstract.
metadata:
  title: "Weft-8 Compare — the same job in three machines"
---

# Weft-8 Compare — the same job in three machines

Five small jobs — load, add, compare, branch, store — implemented three times: for the Weft-8, for x86-64 and for AArch64. Put them side by side and the answer to "what is a computer, really?" stops being abstract. The README is honest about which columns are actually verified.

## When to use

- You are explaining what is machine and what is convention.
- You need a side-by-side that does not overstate what has been executed.
- You are teaching assembly to people who will only ever read it.

## Method

1. Keep the five jobs fixed across all three columns — the comparison is only useful if the task does not change.
2. Put the three listings in `docs/play/compare.js` as data so the page can align them line by line.
3. Mark clearly which columns have been *run* and which have only been *written*; the README's honesty section is the model.
4. Test the page with `node tests/page-smoke.js` and the data with `node test-node.js` (`npm test`).
5. Ship the landing page at `docs/index.html`; release through `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/compare.js` — the three listings and the alignment.
- `docs/play/weft8.js` — the machine used for the first column.
- `test-node.js`, `tests/page-smoke.js`.

## Gotchas

- A comparison that quietly changes the task per column proves nothing; keep the job identical.
- Writing assembly and running it are different claims — say which one each column supports.
- AArch64 and x86-64 differ in operand order and in how a compare sets flags; a "same thing" annotation that ignores that misleads.
- The smallest machine is the clearest one — do not pad the Weft-8 column to look like the others.

## Source projects

- [weft8-compare](https://github.com/drsamonline/weft8-compare) — the five jobs and the three-column presentation.
