---
name: book-kit-companion
description: Model a book as chapters, key points, practices and flashcards, with search and persisted reading progress - the shape six companion apps repeat.
metadata:
  title: "A companion app from a book"
---

# A companion app from a book

## When to use

Model a book as chapters, key points, practices and flashcards, with search and persisted reading progress - the shape six companion apps repeat.

## Method

Extract the capability into a single, zero-dependency file (`book.js`-style),
verify it headless in Node, and let the apps delegate to it instead of repeating it.

## Key files

- the kit's main `.js` file — the API
- `test-node.js` — the verified behaviour (run it before and after any change)

## Gotchas

- Keep the app's own public API stable while swapping in the kit, so its tests
  still pass — that is the proof the refactor is correct.
- One file, zero dependencies, MIT; register it and give it a landing page.

## Source projects

whispering-body-first-aid, gentle-pediatrics-companion, the-symphony-companion, book-kit
