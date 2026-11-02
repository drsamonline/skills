---
name: weft8-classroom
description: A teacher's pack for teaching how a computer works: nine exercises on the Weft-8, each starting incomplete so the class can see what the machine does and then fix it, with a teacher's guide.
metadata:
  title: "Weft-8 Classroom — nine exercises that start broken"
---

# Weft-8 Classroom — nine exercises that start broken

A first lesson in how computers work, built on a machine with twenty-seven instructions and **no `if` statement** — so the student builds one. Every exercise starts incomplete: the machine runs, does something visible, and the class can see exactly what is missing. The teaching method is the product.

## When to use

- You are teaching what a CPU, a register and a branch actually are.
- You want exercises where the failure is observable rather than asserted.
- You need a teacher's guide and a runnable page in one package.

## Method

1. Start from `docs/play/classroom.js` with `docs/play/weft8.js` beside it; the exercise set is data in the page, so adding a tenth exercise is a data edit.
2. Keep each exercise incomplete in a way that *runs* — a blank that produces a wrong-but-visible result teaches more than a crash.
3. Write the teaching order and the expected wrong answers in `TEACHER.md`, so a second teacher can run the same lesson.
4. Test with `node test-node.js` (the exercise data) and `node tests/page-smoke.js` (the page) via `npm test`.
5. Ship the landing page at `docs/index.html` and release through `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/classroom.js` — the exercises; `docs/play/weft8.js` — the machine.
- `TEACHER.md` — the guide and the expected misconceptions.
- `test-node.js`, `tests/page-smoke.js`.

## Gotchas

- An exercise that throws before printing teaches nothing; make the wrong state visible first.
- The absence of `if` is the lesson — do not give the class a branch opcode to make an exercise easier.
- A teacher's guide that assumes the machine is already understood is the guide nobody uses on day one.
- Exercise order matters more than exercise count; the ninth exercise depends on the eighth's idea.

## Source projects

- [weft8-classroom](https://github.com/drsamonline/weft8-classroom) — the nine-exercise sequence and the teacher's guide.
