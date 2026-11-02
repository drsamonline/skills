---
name: app-weft-puzzles
description: Six small programming puzzles solved in Weft-8 assembly on a machine with no conditional: the constraint is the lesson, because you have to build the branch yourself.
metadata:
  title: "Weft Puzzles — six puzzles, no if statement"
---

# Weft Puzzles — six puzzles, no if statement

A robot on a grid, six puzzles, and a machine with sixteen registers, four flags and twenty-seven instructions — **and no `if`**. So you build one, out of `CMP` and `JZ`. That is the whole point: the constraint is the lesson, and the puzzle set is designed around it.

## When to use

- You are teaching branching by removing it.
- You want a puzzle game whose levels are data and whose rules are a real machine.
- You need a small, complete example of a puzzle harness over an emulator.

## Method

1. Keep the world and its rules in `docs/play/world.js` and the machine in `docs/play/weft8.js`; the puzzle data describes the level, the machine enforces the rules.
2. Express each puzzle as a goal over machine state (position, register, output) so success is checked by the machine, not by string comparison of the program.
3. Order the six puzzles so the first needs no branch, the second needs one, and the later ones need composition.
4. Give the player the full instruction set in the page — hiding opcodes makes the puzzle about guessing.
5. Test with `node test-node.js` and `node tests/page-smoke.js` (`npm test`); release via `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/world.js` — the robot and the goal checks.
- `docs/play/weft8.js` — the machine.
- `test-node.js`, `tests/page-smoke.js`.

## Gotchas

- Checking a win by matching source text teaches nothing; check the resulting state.
- A puzzle that can be solved by writing the answer as data is not a programming puzzle — make the goal depend on execution.
- Step limits belong in the puzzle definition, or a brute-force loop solves it.
- Six good puzzles beat twenty padded ones; the later levels must introduce a new idea.

## Source projects

- [app-weft-puzzles](https://github.com/drsamonline/app-weft-puzzles) — the puzzle harness and the six-level progression.
