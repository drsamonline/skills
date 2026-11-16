---
name: code-kit
description: A QR encoder in one dependency-free file — byte mode, versions 1-40, all four error levels, all eight masks, the symbol as a boolean matrix so a canvas, an SVG or a terminal can draw it — plus syntax highlighting and copyable code blocks. The encoder is verified by a QR reader written inside the test file and against segno as an independent implementation.
metadata:
  title: "Code kit — QR encoding, highlighting and copyable blocks"
---

# Code kit — QR encoding, highlighting and copyable blocks

The QR encoder is the centre of this kit: byte mode, versions 1-40, error levels L/M/Q/H and all
eight masks, with the matrix exposed as data. Drawing is the caller's choice — there is no
canvas, no image and no font.

## When to use

- You need a QR code with no CDN and no network, at a version or error level you choose.
- You want the symbol as data (a boolean matrix) so the same code can paint a canvas, an SVG or a terminal.
- You need syntax-highlighted code or a copyable snippet block without a highlighter dependency.

## Method

1. `require("./code-kit.js")` in Node, or use `window.Code` in a page.
2. Encode with `Code.qr.encode(text, { level: "M" })`; `level`, `version` and `mask` can each be pinned when a target requires it.
3. Read `qr.size` and `qr.modules` (a `[[bool]]` matrix) and draw it yourself, or take a ready string from `Code.qr.svg(text)` (quiet zone included) or `Code.qr.ascii(text)` for a terminal.
4. Highlight with `Code.highlight(source, "js")`, and build a copyable block with `Code.snippet.html(source, "bash")`.
5. Verify with `node test-node.js` — it contains a QR **reader** that parses the format information, checks the BCH code, unmasks, walks the placement order, de-interleaves, checks that every Reed-Solomon syndrome is zero and decodes the payload, across nine versions, every level and once per mask.
6. Cross-check against an independent implementation with `scripts/verify-qr.py` (needs `pip install segno`); it runs in CI on every push and reports 10 of 10 cases agreeing.

## Key files / entry points

- `code-kit.js` — `Code.qr` (encoder, `svg`, `ascii`), `Code.highlight`, `Code.snippet`.
- `test-node.js` — 95 assertions, including the in-file QR reader.
- `scripts/verify-qr.py` — the independent check against segno.
- `docs/API.md`, `docs/index.html`, `VERSION`.

## Gotchas

- **The padding difference with segno is deliberate.** segno writes an extra zero byte when the data stream is already byte-aligned; this kit follows ISO/IEC 18004 §7.4.10 and writes nothing. The matrices still agree — do not "fix" it to match segno.
- **`qr.modules` is the contract, not an image.** A caller that assumes a canvas will not work in a terminal, and the kit will not hand one out.
- **The mask matters.** It is chosen by the standard's penalty rule unless pinned; pinning it to compare two encoders is fine, shipping a pinned mask is not.
- **The table change is the risky change.** Reed-Solomon tables and placement order are checked against an independent implementation in CI for exactly that reason.

## Source projects

- [code-kit](https://github.com/drsamonline/code-kit) — the encoder, the highlighter, the in-file QR reader and the segno cross-check.
- [frame-kit](https://github.com/drsamonline/frame-kit) — the transfer core the QR output feeds in the optical apps.
