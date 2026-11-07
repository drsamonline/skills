---
name: symbolic-math
description: "Exact symbolic mathematics in Python: algebra, calculus, equation solving, symbolic linear algebra, physics, plus lambdify and LaTeX generation. Use when a task needs symbolic results, explicit assumptions or exact arithmetic, and use NumPy or SciPy when the workload is purely numerical."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Symbolic mathematics with SymPy"
  category: "data-and-schema"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "sympy"
---

# Symbolic mathematics with SymPy

Symbolic work is exact by default, and the two habits that keep it exact are declaring symbols with assumptions and never letting a float in early. Everything else — solvers, simplification, lambdify — depends on those two.

## When to use

- An answer must be exact or closed-form: a derivative, an integral, a solution set, a simplification.
- A formula must be produced symbolically and then evaluated numerically at scale.
- LaTeX or code must be generated from an expression.

## Method

1. Declare every symbol first with `symbols()`, and give assumptions (`positive=True`, `real=True`, `integer=True`) — they change what simplification and solving can do.
2. Keep arithmetic exact: use `Rational(1, 2)` rather than `0.5`. Convert to float only at the point of reporting.
3. Choose the right tool per task: `simplify` when you want the shortest form, `expand`/`factor`/`apart` when you know the target form, `solve` for closed-form, `nsolve` or `lambdify` for numeric.
4. Verify a solution by substitution rather than trusting the solver — symbolic solvers can return extraneous roots.
5. For repeated numeric evaluation, `lambdify` to NumPy; never evaluate a symbolic expression inside a loop.
6. Check matrix and tensor operations symbolically before moving to numerics, so the algebra is confirmed independently of the implementation.
7. Report the exact result, and the numerical value with its precision, separately.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`sympy`](references/sympy/) | Symbolic mathematics reference: symbols and assumptions, exact arithmetic, simplification, solving, lambdify, LaTeX, patterns. |

## Key files / entry points

- `references/sympy/` — core capabilities, assumptions, exact arithmetic, solvers, lambdify, LaTeX, and worked use-case patterns.

## Gotchas

- Undeclared symbols silently become new ones, and the expression stops matching.
- Floats in a symbolic expression defeat exact simplification.
- A solver's answer needs substitution back into the equation.
- Evaluating symbolically in a loop is orders of magnitude slower than lambdify.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `sympy` — no licence file shipped with the source
