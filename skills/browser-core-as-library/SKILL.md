---
name: browser-core-as-library
description: Turn a browser engine into a library with frontends on top instead of a monolith behind build flags — a pinned NetSurf fork exposing one interface to framebuffer, GTK, headless and text clients that share the same parser, layout and network code.
metadata:
  title: "Nodus"
---

# Nodus — one browser core, many frontends

A knot is where separate strands hold each other without being spliced into one. Nodus is a
NetSurf fork (pinned at `f08191a`) turned into a **library with frontends on top**, plus the
frontend nobody had written: a real text-mode browser sharing the parser, layout and network code
with the graphical one. Tier 1 of the Aetheris family, 25-70 MB.

## When to use

- One engine has to serve several UIs — GUI, framebuffer, headless, text — without `#ifdef` soup.
- You want a browser core you can link into another program, not a program you can only run.
- The budget is 25-70 MB and every frontend shares the cost.

## Method

1. Fork at a **pinned commit** and write the fork point down; an unpinned fork is a different program next month.
2. Extract the core behind one interface (load, layout, render, fetch), and let each frontend implement only the surface it needs.
3. Write the missing frontend as proof the interface is real: a text-mode browser on the same core. If it needs core changes, the interface was wrong.
4. Keep the tiers explicit in `FAMILY.md` with size budgets, so each sibling's trade-off is a stated decision rather than an accident.
5. Treat the frontends as separate build targets sharing one library, not one binary with modes.

## Key files / entry points

- `FAMILY.md` — the four tiers and their budgets.
- The core library and its frontend directory — framebuffer, GTK, headless, text.
- Fork point: NetSurf `f08191a`.

## Gotchas

- A "library" that still needs the frontend's event loop is not a library; the headless frontend is the honest test.
- Shared parser and layout mean a bug in one frontend is a bug in all of them — the text frontend is the cheapest way to reproduce it.
- Size budgets decay silently as features land; the tier table only works if it is checked.

## Source projects

- [nodus](https://github.com/drsamonline/nodus)
