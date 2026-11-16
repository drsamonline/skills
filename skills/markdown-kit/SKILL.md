---
name: markdown-kit
description: CommonMark's core plus the GitHub extensions (tables, task lists, alerts), safe by default — source HTML is escaped, a javascript: link and a data: image are refused — and a streaming mode that renders what is finished and holds back what a language model may still be in the middle of writing.
metadata:
  title: "Markdown kit — rendering, and a streaming reveal"
---

# Markdown kit — rendering, and a streaming reveal

A model does not send a document; it sends chunks, and half of them end in the middle of a code
fence. This kit renders what is finished and holds back what could still change.

## When to use

- An app shows model output and is currently converting markdown with a regex or a CDN library.
- You need a renderer with no dependency, no CDN and no network — the offline-first constraint.
- Output arrives token by token and the page must not flicker between half-parsed states.

## Method

1. `require("./markdown-kit.js")` in Node, or use `window.Md` in a page.
2. Render a finished string with `Md.render(text)`.
3. For streaming, hold one `var s = Md.stream()` per message; call `s.push(chunk)` on every delta and use the returned `{ html, complete }` — `complete: false` means the tail is still being held back.
4. Call `s.done()` when the stream ends to render the finished buffer, then reset for the next message.
5. Rely on the sanitiser: HTML in the source is escaped and never passed through, and unsafe link/image schemes are refused. Do not add a second sanitiser on top.
6. Verify with `node test-node.js` — 92 assertions covering every block and inline construct, the sanitiser, and the streaming rules: a partial heading is not a heading, half-written emphasis is not bold, an open fence is code.

## Key files / entry points

- `markdown-kit.js` — the renderer, the `stream()` object and the `SAFE` scheme check.
- `test-node.js` — 92 assertions, including the streaming cases.
- `docs/API.md`, `docs/index.html`, `VERSION`.

## Gotchas

- **A trailing blank line is what finalises a block.** The streaming renderer holds the last block back on purpose; feeding it one line at a time without a terminator leaves the last paragraph unpainted.
- **Markdown inside a fence stays literal** — a code block showing markdown renders the markdown, not the output. That is asserted, so a "fix" that renders inside fences breaks a test.
- **Safe by default means no raw HTML.** An app that wants embedded HTML has to escape it into a code block; there is no opt-out flag.
- **Consumers: none yet, by design.** The intended first adopters are the AI-facing apps (SmartNotes, ai-bridge, Matneo), which render model output by hand today. Adoption is one app at a time, by the owner.

## Source projects

- [markdown-kit](https://github.com/drsamonline/markdown-kit) — the kit, its API and its 92 assertions.
