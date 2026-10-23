---
name: unstoppable-mind-companion
description: An offline companion app to The Unstoppable Mind: the book's key points and exercises, a 7-day challenge and flashcards — in a single ~30 KB file with no JavaScript at all.
metadata:
  title: "The Unstoppable Mind — companion"
---

# The Unstoppable Mind — companion

The Unstoppable Mind — Companion is a small, offline companion to the book *The Unstoppable Mind: Mastering Habituation, Confidence, and Power*. It is the book's key points and its exercises, a 7-day challenge and flashcards, in a form you can carry on your phone. It is a single ~30 KB file built with **no JavaScript** — pure HTML/CSS.

## When to use

- You want an ultra-light companion app with no JavaScript.
- You need a CSS-only disclosure/flashcard pattern.
- You are turning a book's exercises into an offline checklist.

## Method

1. Keep the app a single file with no JavaScript; use HTML + CSS only (details/summary, :target, or checkbox hacks for interaction).
2. Structure content as the book's key points, its exercises, a 7-day challenge checklist and flashcards.
3. Use inline SVG badges (`badges/*.svg`) rather than external image services for the README.
4. Publish a play copy at `docs/play/` and a landing page at `docs/index.html`.
5. Build EXE + APK with `.github/workflows/build-apps.yml`.
6. Licence: free to use.

## Key files / entry points

- `docs/play/index.html` — the app (no JS); `docs/index.html` — landing page.
- `badges/*.svg` — inline README badges; `preview.png`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- No-JS interaction needs semantic HTML (details/summary) to stay accessible and keyboard-operable.
- Keep the file tiny — the ~30 KB size is part of the appeal.
- It is a companion, not the book; keep the distinction.

## Source projects

- [unstoppable-mind-companion](https://github.com/drsamonline/unstoppable-mind-companion) — free to use, no JavaScript.

