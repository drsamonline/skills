---
name: featherweight-graphical-browser
description: Build a graphical browser for machines the modern web forgot — 2 GB netbooks, Pentium M laptops, 512 MB Raspberry Pis — as a hardened Dillo fork with no JavaScript engine, a scriptable surface, and a 15-30 MB budget.
metadata:
  title: "Sorex"
---

# Sorex — a featherweight GUI browser for old machines

The smallest mammal with a real bite. Sorex is a featherweight graphical browser for 2 GB netbooks,
Pentium M ThinkPads, 512 MB Raspberry Pis and VMs on a metered connection: a Dillo fork (pinned at
`6856c50`), hardened for speed, made scriptable, and given what a browser needs in 2026 *without*
a JavaScript engine. Tier 2 of the Aetheris family, 15-30 MB.

## When to use

- The target machine has less RAM than a modern page's heap.
- The page does not need JavaScript — a documentation site, a wiki, a form — and a real engine is overkill.
- You need the browser driven from a shell script, not from a user.

## Method

1. Start from a small engine (Dillo/FLTK) and pin the fork commit; the value is the size, so every addition is weighed against the budget.
2. Say what is missing out loud: no JavaScript engine. A browser that silently renders half a page is worse than one that says so.
3. Harden for speed on the target class of machine — measure on a 512 MB device, not on a workstation.
4. Add a scriptable surface (CLI flags, a control socket) so the browser can be a component.
5. Keep the tier table current: this is T2, and its 15-30 MB is a claim you re-measure each release.

## Key files / entry points

- `FAMILY.md` — the tiers and budgets.
- Fork point: Dillo `6856c50`.
- The scripting surface — how another program drives the browser.

## Gotchas

- No JavaScript is a *feature* here, but it is also a limit: a page that needs it renders as an empty shell, and the user must be told why.
- FLTK on a 2 GB machine is comfortable; the same build on a modern desktop looks broken, so test on the target.
- A browser that "works on old hardware" has to be *built* on old hardware or an emulator of it, or the claim is untested.

## Source projects

- [sorex](https://github.com/drsamonline/sorex)
