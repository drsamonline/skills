---
name: app-clip-loom
description: Clipboard cleanup as five Weft-8 programs you can read in full: strip tracking parameters, tidy extracted text, rewrap a paragraph — each twenty lines of assembly on a machine in the page.
metadata:
  title: "Clip Loom — clipboard programs you can read"
---

# Clip Loom — clipboard programs you can read

A link with eleven tracking parameters. Text pulled out of a PDF with three spaces between every word. A paragraph going into a field that will not wrap. Clip Loom does those jobs with **programs you can read in full** — twenty lines of Weft-8 assembly each, running on a machine that lives in the page. No extension, no network, no hidden rules.

## When to use

- You want a text transformation whose behaviour is auditable line by line.
- You need clipboard cleanup (tracking parameters, whitespace, wrapping) with no service.
- You are showing that "a script you can read" is a real alternative to a black-box tool.

## Method

1. Keep each transformation as one Weft-8 program in `docs/play/clip.js`, with the five programs listed and named in the page.
2. Run the machine from `docs/play/weft8.js`; the program operates on the pasted text, and the result is offered for copy.
3. State each program's scope in its header — what it removes and what it deliberately leaves alone.
4. Handle the clipboard permission path explicitly: a paste that cannot be read must say so rather than silently doing nothing.
5. Test with `node test-node.js` and `node tests/page-smoke.js` (`npm test`); release via `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/clip.js` — the five programs.
- `docs/play/weft8.js` — the machine.
- `docs/play/index.html` — paste, run, copy.
- `test-node.js`, `tests/page-smoke.js`.

## Gotchas

- Clipboard access needs a user gesture and a permission; a background paste fails silently.
- Stripping "all parameters" breaks links that need them — a tracking-parameter list is the honest approach, with the list visible.
- A transformation that mangles non-Latin text is a bug users find immediately; test outside ASCII.
- Twenty lines of assembly is a promise about readability — keep new programs short or move them out of the kit.

## Source projects

- [app-clip-loom](https://github.com/drsamonline/app-clip-loom) — the five readable clipboard programs.
