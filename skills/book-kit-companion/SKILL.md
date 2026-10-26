---
name: book-kit-companion
description: The companion-app-from-a-book pattern in one zero-dependency file: chapters, key points, practices, flashcards, in-book search and reading progress with notes.
metadata:
  title: "Companion app from a book"
---

# Companion app from a book

Eight of the estate's apps are companions to a book, and they all want the same
shape: a title, chapters, key points, practices, flashcards, a way to search
inside the book, and a record of what has been read. `book-kit` is that shape,
once. One file, zero dependencies.

## When to use

- You are building an app that accompanies a book: read a chapter, take the key
  points, do the practice, keep a note.
- You want flashcards and reading progress without designing a data model.
- You need in-book search (by chapter title or by key point) in an offline app.

## Method

1. Keep the book as data, not markup: one JSON file with `title`, `author`,
   `chapters[]` (`title`, `keyPoints`, `practices`, optional `body`) and
   `flashcards[]` (`front`, `back`).
2. `var book = Book.load(json);` — the kit normalises it and gives you
   `book.chapters`, `book.chapter(i)`, `book.keyPoints(i)`,
   `book.practices(i)`, `book.chapterByTitle(prefix)` and `book.flashcards`.
3. `book.search(q)` returns matches with their chapter index, so a result can
   jump straight to the chapter.
4. `var p = book.progress(store);` — `markRead(i)`, `isRead(i)`, `toggle(i)`,
   `percent()`, `note(i, text)`. `store` is any object with `get(key, default)`
   and `set(key, value)`; pass web-kit's `Loom.storage` so progress lands in the
   same place as the rest of the app's state.
5. Wire the flashcards to `srs-kit` if they should be scheduled rather than
   shown in order.

## Key files

- `book-kit.js` — `Book.load`, chapter/practice/key-point accessors, `search`,
  `progress`.
- `test-node.js` — the worked example, including a fake in-memory store.

## Gotchas

- `progress()` needs a store with `get`/`set`. An app that keeps state in one
  big `localStorage` blob should pass a two-function adapter, not rewrite the kit.
- Chapter fields accept aliases — `keyPoints` or `points`, `practices` or
  `exercises`. Pick one spelling and keep the book JSON consistent; a mixed file
  silently loses a section.
- The kit models no content and no licence. The book's text stays the author's,
  and each app carries its own attribution and medical disclaimer.
- Most companions in the estate still hand-roll this shape, so their book JSON
  files differ from one another and from the kit's expectations.

## Source projects

- [book-kit](https://github.com/drsamonline/book-kit) — the pattern itself.
- [whispering-body-first-aid](https://github.com/drsamonline/whispering-body-first-aid) — 30 first-aid remedies, EN/HI/GU.
- [gentle-pediatrics-companion](https://github.com/drsamonline/gentle-pediatrics-companion) — triage-first paediatric companion.
- [the-symphony-companion](https://github.com/drsamonline/the-symphony-companion) — cards, practices, breathing timer, journal.
- [unstoppable-mind-companion](https://github.com/drsamonline/unstoppable-mind-companion) — a companion with no JavaScript at all.
- [read-live-transform-app](https://github.com/drsamonline/read-live-transform-app) — 74 chapters, read/live/keep.
