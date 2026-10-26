---
name: qr-code-encoder
description: A QR encoder in one dependency-free file: byte mode, ECC L/M/Q/H, versions 1-40, Reed-Solomon over GF(256) and the ISO/IEC 18004 block tables — for rendering a code offline without shipping a QR library.
metadata:
  title: "Self-contained QR encoder"
---

# Self-contained QR encoder

Two different QR layers exist in this estate and only one of them is
dependency-free. `TTB`'s `tools/qr.js` is a complete byte-mode encoder — ECC
L/M/Q/H, versions 1–40, Reed–Solomon over GF(256), the standard block and EC
tables, BCH for the format and version bits — in 92 lines with no runtime
dependency. `BLINKTRANSFER` and `helioprism` instead wrap `qrcode-generator`
(MIT) and `jsQR` (Apache-2.0) behind a small `qr.js`.

## When to use

- An offline app must draw a QR code and you do not want a bundled QR library
  (or a CDN) in a single-file build.
- You are moving a payload optically and need to know what a QR can actually
  hold.
- You need arbitrary binary to survive the round trip, not just text.

## Method

1. Pick the smallest version that fits: the encoder walks versions 1–40 and
   computes capacity from `(totalCodewords − eccCodewords) × 8`, throwing above
   roughly 2,953 bytes.
2. Build the codewords: mode indicator, character-count indicator (8 bits below
   version 10, 16 above), the bytes, a terminator, then pad bytes to the block
   boundary.
3. Split into blocks with the ISO/IEC 18004 block and EC tables, compute the
   Reed–Solomon parity per block over GF(256) with the primitive polynomial
   `0x11d`, and interleave.
4. Add the BCH-coded format bits (`0x537`) and version bits (`0x1f25`), then
   place the modules with the standard finder, timing and alignment patterns.
5. Draw the matrix to a canvas with a quiet-zone margin of 4 modules.

## Key files

- `TTB/tools/qr.js` — the zero-dependency encoder (tables, GF(256) arithmetic,
  `rsEncode`, `bch15`, `bch18`, `pickVersion`, codeword builder).
- `BLINKTRANSFER/src/lib/qr.js` and `helioprism/src/lib/qr/qr.js` — the
  library-backed wrapper: `encodeMatrix`, `drawQR`, `decodeImage`,
  `decodeWithScales`.
- `TTB/tools/qr.js` is also the only encoder here that has no decoder beside it.

## Gotchas

- **Binary safety.** `qrcode-generator`'s byte mode maps one character to one
  byte, and `jsQR` exposes `binaryData`. The wrapper therefore passes a latin-1
  string in and reads bytes out. Base64 through a QR costs 33% and is the wrong
  habit.
- A QR holds about 2,953 bytes. A file needs the fountain/frame layer above it
  (`optical-kit` + `frame-kit`); a QR alone is for keys, URLs and small payloads.
- The zero-dependency encoder encodes only — a scanner needs a decoder such as
  `jsQR`, which is a dependency the extension route can avoid but a camera app
  cannot.
- Two QR layers in one estate is the duplication this skill exists to end: pick
  the dependency-free encoder for new work and retire the wrappers as the three
  optical repos adopt `optical-kit`.
- Error-correction level trades capacity for robustness; L is the default in the
  wrapper and it is what makes a long payload fit at all.

## Source projects

- [TTB](https://github.com/drsamonline/TTB) — the zero-dependency encoder in `tools/qr.js`.
- [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) — the library-backed QR layer for animated transfer.
- [helioprism](https://github.com/drsamonline/helioprism) — a byte-identical copy of that same QR layer.
- [optical-kit](https://github.com/drsamonline/optical-kit) — the transport a QR payload rides on.
