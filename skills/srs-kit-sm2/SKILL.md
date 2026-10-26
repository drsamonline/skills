---
name: srs-kit-sm2
description: Schedule flashcards with SM-2 in one zero-dependency file: ease, interval, reps, lapses, due cards, stats and a configurable cadence.
metadata:
  title: "Spaced repetition with SM-2"
---

# Spaced repetition with SM-2

`Srs` is the shared scheduler behind the study and companion apps. Given a card
and how well it was recalled, it decides when the card comes back. One file,
zero dependencies, usable from a browser (`window.Srs`) or Node
(`module.exports`).

## When to use

- An app has cards, drills or review queues and needs a due date for each one.
- You are about to write "if recalled easily, multiply the interval by the ease
  factor" for the third time.
- A study app must keep working offline with the schedule stored locally.

## Method

1. Load `srs-kit.js`. It exports `Srs` on the global object, or through
   `module.exports` in Node.
2. Make a card: `var c = Srs.newCard();` — the card carries `ease`, `interval`,
   `reps`, `lapses`, `due` and `last`.
3. Review it: `c = Srs.review(c, quality, now, opts)` with `quality` on the SM-2
   0–5 scale. A quality below 3 is a lapse and resets the interval.
4. Leave `opts` out and you get the classic cadence — first interval 1 day, then
   6, lapse back to 1. Pass `firstInterval`, `secondInterval`, `lapseInterval`
   or `dailyCap` (or put them on the card, so a deck can carry its own cadence).
5. Read `c.due` for the review queue and keep the cards in the app's own store
   (`Loom.storage` from web-kit, IndexedDB, or a JSON file the user exports).

## Key files

- `srs-kit.js` — the whole scheduler; the `DEFAULTS` object is the cadence.
- `test-node.js` — the behaviour that must not change when the kit is updated.

## Gotchas

- The two numbers SM-2 hardcodes are 1 and 6. `conqueror-os` had made them
  configurable in its own copy, so they are folded back here as **opt-in**
  options — an existing caller keeps the old behaviour exactly. Do not change
  `DEFAULTS` to suit one app.
- `conqueror-os` still runs its own inline "spaced repetition (SM-2 lite)"
  inside `index.html`. Porting it means mapping its cadence onto these options,
  not forking the kit.
- `mnemosyne-companion` schedules its drills itself, so its card state is not
  interchangeable with an `Srs` card. An export/import path has to translate.
- `srs-kit.js` is vendored by no app yet; the two apps that need it hand-roll
  the maths.

## Source projects

- [srs-kit](https://github.com/drsamonline/srs-kit) — the scheduler itself.
- [conqueror-os](https://github.com/drsamonline/conqueror-os) — an inline SM-2 lite whose configurability was folded into the kit.
- [mnemosyne-companion](https://github.com/drsamonline/mnemosyne-companion) — spaced-repetition drills over 100 polycrest remedies.
