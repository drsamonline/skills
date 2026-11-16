---
name: frame-kit
description: The whole optical-transfer path in one file: a 22-byte self-describing frame with a payload CRC-32 and a header CRC-16, strict validation of bytes that arrive from a camera, a rateless LT fountain collector that tolerates duplicates and restarts on a new transfer id, and the byte/CRC/PRNG helpers underneath. Absorbed optical-kit on 2026-11-12.
metadata:
  title: "Frame kit — the shared transfer core"
---

# Frame kit — the shared transfer core

The kit is both halves of an optical transfer: it **moves bytes** with a systematic LT fountain
code and **wraps them** in a self-describing header, so a receiver can lock onto any frame,
mid-stream, with no separate handshake.

## When to use

- An app sends a file between two devices with no network, Bluetooth or cable — QR frames, colour matrices, a screen and a camera.
- You are decoding frames from an untrusted source (a camera) and need the header validated before it allocates anything.
- You need CRC-16/CCITT, CRC-32, a seeded PRNG or size formatting in the browser without a dependency.

## Method

1. Load `frame-kit.js` as a plain script; it attaches the global `Frame` (and exports for Node).
2. On the sending side, slice the payload into `k` blocks of `blockSize`, then build each symbol with `Frame.pack({ magic, transferId, k, blockSize, totalLength, payloadCRC: Frame.crc32(payload), symbolId, data })`.
3. On the receiving side, hand every decoded frame to `Frame.parse(frame, { magics: [0xb7], label: 'MyApp' })`. Pass the magic(s) you expect; anything else is dropped, not thrown.
4. Feed parsed symbols into a `FountainCollector`: it absorbs them in any order, tolerates duplicates, restarts when the transfer id changes, and verifies the payload checksum when it assembles.
5. Verify with `node test-node.js` — 19 assertions over the frame, its validation and the collector.

## Key files / entry points

- `frame-kit.js` — the whole kit: pack/parse, the collector, CRC-16/CCITT, CRC-32, the seeded PRNG, byte helpers.
- `docs/API.md` — the header layout and each call.
- `test-node.js` — the 19 assertions.
- `CHANGELOG.md` — records the 2026-11-12 absorption of `optical-kit`.
- `VERSION` — 2.0.0; a major bump because the frame changed.

## Gotchas

- **Two incompatible frame definitions existed.** `optical-kit` carried a 17-byte frame beside this 22-byte one, and the same three apps used both. This kit absorbed `optical-kit`; a copy of the old kit is a different frame format, not an older version of this one.
- **`magics` is not optional in practice.** A receiver that accepts any magic will try to interpret arbitrary bytes from a camera as a header.
- **A corrupt header must be dropped, not repaired.** The header CRC-16 exists so that a crafted or damaged frame cannot drive an allocation.
- **A rateless collector is order-free but not state-free.** Restart it when the transfer id changes, or symbols from two transfers will be mixed.
- **Bytes-equal is the wrong drift test.** Across this fleet, vendored copies of frame/optical kits differed in bytes and not in behaviour — the only difference was a lint header (`/* global module */` vs `/* global module, btoa, atob */`).

## Source projects

- [frame-kit](https://github.com/drsamonline/frame-kit) — the kit, its API and tests.
- [helioprism](https://github.com/drsamonline/helioprism), [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai), [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) — the three consumers that carried both frame definitions.
