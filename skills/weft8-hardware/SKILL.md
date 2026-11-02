---
name: weft8-hardware
description: The Loom's 8-bit machine written a second time in about 180 lines of C, held against the JavaScript implementation by a generated corpus, so the two must agree on every case.
metadata:
  title: "Weft-8 in C — a parity harness for one machine"
---

# Weft-8 in C — a parity harness for one machine

A machine described in one language can hide a mistake inside that language's habits. So the Weft-8 is written a second time in C (`c/weft8.c`, `c/weft8.h`, `c/main.c`) and the two implementations are held against each other by an answer-checked corpus. The C port is the test.

## When to use

- You have an emulator or interpreter whose correctness you want to prove rather than assert.
- You need a differential test between two implementations of the same spec.
- You are porting a small machine to C and want the port to be checkable.

## Method

1. Write the second implementation against the spec, not against the first implementation's source — reading the original while porting copies its bugs.
2. Generate the corpus with `tools/gen-corpus.mjs` into `corpus.json`, and bake it into the C side as `c/corpus.h` so the harness has no file I/O to get wrong.
3. Run both sides over the same inputs and compare full state, not just the output byte — a divergence in flags is still a divergence.
4. Keep `tools/parity.mjs` as the comparison entry point and `tools/sync-demo.mjs` to push the same corpus into the browser demo (`docs/play/parity.js`).
5. Test with `node test-node.js` and release through `.github/workflows/build-apps.yml` and `test.yml`.

## Key files / entry points

- `c/weft8.c`, `c/weft8.h`, `c/main.c` — the C implementation.
- `corpus.json`, `c/corpus.h` — the shared corpus.
- `tools/gen-corpus.mjs`, `tools/parity.mjs`, `tools/sync-demo.mjs`.
- `docs/play/parity.js` — the browser view of the same comparison.

## Gotchas

- Porting by reading the original copies its mistakes; port from the spec and let the corpus find the disagreements.
- Comparing only the output hides flag and register bugs — compare the whole machine state after each step.
- A corpus that only exercises valid programs never tests the error paths; include the illegal ones.
- Baking the corpus into a header means regenerating it is a build step, not a runtime read.

## Source projects

- [weft8-hardware](https://github.com/drsamonline/weft8-hardware) — the C port, the generated corpus and the parity harness.
