---
name: Compression with the platform's Compression Streams
description: Compress and decompress data in a web app or Node without bundling a compression library, using the built-in CompressionStream / DecompressionStream (gzip, deflate, deflate-raw).
---

# Compression with the platform's Compression Streams

## When to use

When an app needs to shrink data before storing, sending or sealing it, and you
do not want to ship a compression library. Modern browsers and Node 18+ have
`CompressionStream` and `DecompressionStream` built in.

## Method

1. Create the stream: `new CompressionStream(format)` (or `DecompressionStream`).
2. Write the bytes into `stream.writable` and close it.
3. Read from `stream.readable` and concatenate the chunks.
4. Formats: **gzip** (portable, has a header), **deflate** (zlib), and
   **deflate-raw** (no header — smallest, when both ends are yours).

## Key files

- `compress-kit.js` — `Compress.gzip/gunzip`, `deflate/inflate`,
  `deflateRaw/inflateRaw`, `compressString/decompressString`, `ratio`, `human`.
- `test-node.js` — the verified round-trip.

## Gotchas

- **Read the stream directly, not via `Response`/`Blob`.** `new Response(stream)`
  pulls in undici in Node, which allocates WASM and can fail in constrained
  environments ("Out of memory: Cannot allocate Wasm memory"). A `getReader()`
  pump avoids that and runs everywhere the streams exist.
- **Await the writer.** Chain `writer.write(bytes).then(() => writer.close())`
  before pumping the reader, or you can close early.
- **Feature-detect.** Expose `available()`; fall back to storing uncompressed if
  the platform lacks the streams.
- **Compress then encrypt** — compression is not security; pair with `crypto-kit`.

## Source projects

`lexora` (CLI/server counterpart); `compress-kit` (the shared browser core).
