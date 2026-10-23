---
name: optical-kit-fountain
description: Transfer files over a screen-to-camera (or speaker-to-mic) link using a systematic LT fountain code, so any ~k frames reconstruct the file and a dropped frame costs time, never correctness.
metadata:
  title: "Optical file transfer with a fountain code"
---

# Optical file transfer with a fountain code

## When to use

When you need to move data between two devices with **no network** and **no
back-channel** — a screen showing to a camera, a speaker to a microphone, or a
colour matrix — and the channel will drop frames. Numbered frames are fragile
here (the receiver must catch every one). A fountain code fixes that.

## Method

1. Split the payload into `k` fixed-size blocks.
2. **Systematic prefix:** frames `0..k-1` carry block `i` verbatim, so a clean
   read costs no overhead.
3. **Repair frames:** frames `>= k` carry the XOR of a pseudorandom subset of
   blocks, with the subset derived deterministically from `(session, seq)` and
   degree drawn from a **robust soliton** distribution.
4. **Self-describing frames:** magic, session, sequence, `k`, block size, total
   length, and a CRC — so a receiver can lock onto a stream mid-flight.
5. **Decode by peeling:** solve a block whenever a frame has exactly one unknown
   left; XOR it out of every frame that mentions it; repeat.
6. **Reduce on insert:** when adding a frame, first XOR out every already-solved
   block it contains — otherwise its "unknown count" is wrong and peeling solves
   it incorrectly. (This is the subtle bug that breaks most first attempts.)

## Key files

- `optical-kit.js` — `Optical.Sender`, `Optical.Receiver`, `Optical.Fountain`,
  `Optical.Decoder`, `Optical.Frame`, `Optical.crc32`, `Optical.bytes`.
- `test-node.js` — the verified round-trip, including dropped frames.

## Gotchas

- **No back-channel** — the receiver cannot ask for a resend; that is the whole
  reason for a fountain code.
- **Peeling needs the robust soliton**, not the ideal one, or the tail never
  completes and overhead balloons.
- **Determinism** — sender and receiver must derive the same degree and the same
  subset from `(session, seq)`; use an integer-only PRNG so engines agree.
- **Codec is pluggable** — the kit moves bytes; the app draws them (QR, colour
  matrix, multi-code grid).

## Source projects

`helioprism`, `blinkcode-ai`, `BLINKTRANSFER` — consolidated into `optical-kit`.
