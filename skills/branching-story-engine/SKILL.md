---
name: branching-story-engine
description: Build a choose-your-own-adventure reader where the carried state decides which doors are still open and the trail records every passage in order — offline, no accounts, with the engine tested headlessly against the real book.
metadata:
  title: "app-story-engine"
---

# app-story-engine — the state is the story

A book the reader moves through. A "choose your own adventure" app usually forgets what you
chose — the branches are a tree of screens and the reader is a click. Here the **state is the
story**: what you pick changes what you carry, what you carry decides which doors are still open,
and the trail shows every passage you went through, in order, return visits included.

## When to use

- Choices have to *accumulate*: an item, a debt, a reputation that closes one path and opens another.
- The reader must be able to see where they have been — a trail, not a back button.
- The engine has to be testable without a browser, and the book has to be data rather than code.

## Method

1. Split the engine from the book. `compile` the book data into passages, then `newGame`, `choicesFor`, `advance` — the engine knows nothing about the specific story.
2. Make state the gate: a choice is available only if the carried state satisfies it, and a closed door is shown as closed rather than hidden.
3. Record the trail as an ordered list of passage ids with repeats, so the reader can retrace and the developer can see a path through the book.
4. Put `save`/`load` behind a `createStore` so the same engine runs on localStorage, memory or a test double.
5. Test the engine *and* the shipping book with `node test-node.js` — 141 assertions over real passages, because a book with an unreachable passage is a bug in the book.

## Key files / entry points

- `docs/play/story-engine.js` — the engine.
- `docs/play/book.js` — *The Fifth Mile*, the book as data.
- `docs/play/index.html` — the reader.
- `test-node.js` — the headless suite.

## Gotchas

- A branch that no choice can reach is invisible until someone plays the whole tree; assert reachability in the test, not in a walkthrough.
- "Return visits included" means the trail is a log, not a set — de-duplicating it loses the loop the reader took.
- Keeping the book as data is what makes a second book cheap; the moment a passage holds code, it is a one-book engine.

## Source projects

- [app-story-engine](https://github.com/drsamonline/app-story-engine)
