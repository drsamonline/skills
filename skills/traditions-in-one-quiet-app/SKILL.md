---
name: traditions-in-one-quiet-app
description: Combine several divination and self-reflection traditions — numerology, sun-sign astrology, lunar phase, biorhythm, tarot, runes and I Ching — into one offline app with a single Today screen, without ranking them or pretending they are science.
metadata:
  title: "Holistic"
---

# Holistic — eight traditions in one quiet app

Eight traditions, one quiet app: numerology, sun-sign astrology, lunar phase, biorhythm, a full
I Ching, 78 tarot cards and runes — 92 KB, offline, zero network requests.

## When to use

- Several belief systems have to sit in one product without one being treated as the "real" one.
- The content is reflective rather than predictive, and the interface has to carry that distinction.
- A small app has to hold a lot of structured content (78 cards, 64 hexagrams, 24 runes) without a database.

## Method

1. Put the **Today** screen first: the day's phase, the number, the card — a single quiet entry point rather than eight menus.
2. Keep each tradition a self-contained data set plus a small pure function (compute the number, draw the card, cast the hexagram); nothing is shared except the calendar.
3. Give every tradition the same visual weight. One app, eight columns — not one feature with seven extras.
4. Frame the output as reflection: say what the tradition says, not what will happen.
5. Compute the astronomical parts (lunar phase, sun sign) from real ephemerides rather than lookup tables, so the app is right in any year.
6. Keep it small: 92 KB is the whole app, content included.

## Key files / entry points

- The Today screen.
- One data set per tradition (78 tarot cards, 64 hexagrams, 24 runes, the numerology tables).
- The lunar/solar calculations.

## Gotchas

- Sun-sign boundaries are dates, not moments, unless you compute the actual ingress — decide which claim you are making and keep it consistent.
- A tarot deck has a licence history: use a deck whose artwork and meanings you may ship, or ship text-only.
- Mixing traditions invites invented correspondences; if you correlate them, say that the correlation is yours.

## Source projects

- [holistic](https://github.com/drsamonline/holistic)
