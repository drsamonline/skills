---
name: compress-kit-streams
description: gzip, deflate and deflate-raw over the platform's Compression Streams, with byte and base64 helpers — the browser counterpart to lexora.
metadata:
  title: "Compression with Compression Streams"
---

# Compression with Compression Streams

`Compress` is the browser side of compression: gzip, deflate and deflate-raw,
implemented on the platform's `CompressionStream` / `DecompressionStream` so an
app never bundles a compression library. One file, no dependencies.

## When to use

- A single-file app embeds a large payload (a repertory, a search index, a PDF)
  and the HTML is too big.
- You are shipping an export the user will email and want it smaller.
- You need to *read* a payload that was compressed at build time.

## Method

1. Guard the platform: `Compress.available()` is false without
   `CompressionStream` — every call rejects with a plain error rather than a
   silent no-op.
2. `await Compress.gzip(bytes)` / `await Compress.gunzip(bytes)` for bytes;
   `deflate` and `deflateRaw` for the other two formats.
3. `await Compress.compressString(text)` returns base64, and
   `await Compress.decompressString(b64)` returns the text — the pair to use when
   the payload has to live inside an HTML file or JSON.
4. Compress at build time where you can: a prebuilt base64 payload means the app
   never pays for compression on the user's device.

## Key files

- `compress-kit.js` — `available`, `bytes.*`, `gzip`/`gunzip`,
  `deflate`/`deflateRaw`, `compressString`/`decompressString`.
- `test-node.js` — round-trips (Node 18+ has the same streams).

## Gotchas

- Base64 costs about 33%: compress first, then base64, and measure the result
  rather than assuming the file got smaller.
- The kit's guarantee is *a* round-trip; `lexora`'s guarantee is byte-exact
  recovery after conservative canonicalisation on the CLI/server. They are not
  the same promise, and a compressed artefact from one is not the other's.
- `kent-repertory-explorer` decompresses its embedded data inline and throws
  "This browser cannot decompress the embedded data" when the API is missing —
  the same guard the kit's `available()` gives you.
- `offline-pdf-toolkit` and `kent-repertory-explorer` use the streams directly
  instead of vendoring the kit; they are the adoption targets.

## Source projects

- [compress-kit](https://github.com/drsamonline/compress-kit) — the wrapper.
- [lexora](https://github.com/drsamonline/lexora) — exact-text compression with a byte-exact round-trip on the CLI.
- [kent-repertory-explorer](https://github.com/drsamonline/kent-repertory-explorer) — a 1.9 MB repertory that ships decompressed-by-stream.
- [offline-pdf-toolkit](https://github.com/drsamonline/offline-pdf-toolkit) — in-browser PDF work on the same platform APIs.
