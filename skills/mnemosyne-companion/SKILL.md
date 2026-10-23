---
name: mnemosyne-companion
description: A single offline HTML study companion for Mnemosyne Materia Medica: 100 polycrest remedies as poetic pearls, keynotes and spaced-repetition drills, in three drill modes.
metadata:
  title: "Mnemosyne Companion"
---

# Mnemosyne Companion

Mnemosyne Companion is the study companion to *Mnemosyne Materia Medica: A Memory-Optimised Clinical Guide to 100 Polycrest Homoeopathic Remedies*. It carries the study material of all 100 remedies — poetic pearls, keynotes, modalities, differentials and miasmatic groupings — and turns it into an active-recall drill with a spaced-repetition schedule and three drill modes. One offline HTML file. Deliberately not the full book.

## When to use

- You are building a spaced-repetition study app over a fixed corpus.
- You want the pearls/keynotes/differentials study model for homeopathy.
- You need a single-file app with a scheduling algorithm and drill modes.

## Method

1. Ship one offline HTML file (`dist/Mnemosyne_Companion.html`) with the study corpus embedded.
2. Model each remedy as poetic pearls, keynotes, modalities, differentials and miasmatic groupings (8 keynotes each).
3. Implement active recall with a spaced-repetition schedule and three drill modes.
4. Keep it clearly a *companion*, not the book: clinical descriptions and case histories stay in the text.
5. Publish a play copy at `docs/play/` and a landing page at `docs/index.html`; build EXE + APK with `.github/workflows/build-apps.yml`.
6. State the licence: proprietary, all rights reserved.

## Key files / entry points

- `dist/Mnemosyne_Companion.html` — the app.
- `docs/play/`, `docs/index.html` — served copy and landing page; `assets/` screenshots.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Keep it a study aid, not a clinical reference — say so (a disclaimer doc exists).
- The book's clinical content is copyrighted and must not be reproduced in the app.
- Spaced repetition needs persistence and a stable schedule; store progress locally.

## Source projects

- [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion) — v1.0.0, proprietary.

