---
name: optical-kit-fountain
description: A systematic LT fountain code with self-describing frames and a pluggable codec — the shared optical-transfer core behind the QR and colour-matrix senders.
metadata:
  title: "Optical transfer: fountain code and frames"
---

# Optical transfer: fountain code and frames

Sending a file as light means the receiver will miss frames — a hand shakes, a
screen refreshes. `optical-kit` is the answer to that: a systematic LT fountain
code that turns a payload into an endless stream of symbols, so any *enough*
symbols reconstruct the file, plus a frame layer that says which symbol this is.

## When to use

- You are building a sender or receiver that moves bytes over a screen and a
  camera, with no network, Bluetooth or cable.
- You need to survive dropped frames without a request/retry loop.
- You want to change the codec (QR, colour matrix) without rewriting the
  transport.

## Method

1. Pack the payload once: build a session over the bytes with a block size, and
   let the kit produce symbol indices for each frame it emits.
2. Emit frames with `frame-kit`: each frame is self-describing — magic,
   `transferId`, `symbolId`, `totalLength`, `payloadCRC` — so a receiver that
   joins late can still identify what it is looking at.
3. On the receiving side, feed decoded symbols into the collector; track
   `progress` and `complete`. The `restarted` flag tells you the sender began a
   new transfer.
4. Verify `payloadCRC` before declaring success, then unpack the payload.
5. Draw the symbol with whatever codec you chose — the codec is pluggable, and
   the QR layer is a separate concern.

## Key files

- `optical-kit.js` — session, symbol generation, pack/unpack, block size,
  progress.
- `frame-kit.js` — the frame header, the collector, CRC and restart detection.
- `test-node.js` in each — the encode/decode behaviour.

## Gotchas

- A sender and a receiver must agree on **both** the frame format and the codec.
  A version skew looks exactly like a bad camera.
- `BLINKTRANSFER`, `blinkcode-ai` and `helioprism` each still ship their own
  `lib/fountain.js` even though the kit implements the fountain — three copies to
  retire. All three also vendor `frame-kit.js` twice (at the repo root and under
  `src/lib/`).
- The codec is not in this kit. The QR layer lives in `qr.js` and is duplicated
  across the same repos; see the `qr-code-encoder` skill.
- Optical transfer is slow and line-of-sight: a 1 MB file is a long stare at a
  screen. Compress first (`compress-kit`) and say so in the UI.

## Source projects

- [optical-kit](https://github.com/drsamonline/optical-kit) — the fountain code and transport.
- [frame-kit](https://github.com/drsamonline/frame-kit) — the self-describing frame and collector.
- [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) — animated QR transfer at ~20 FPS.
- [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) — SpectraCode colour matrices.
- [helioprism](https://github.com/drsamonline/helioprism) — two optical transports in one app.
