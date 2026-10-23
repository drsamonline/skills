---
name: optical-file-transfer
description: Move a file between two devices with no network, Bluetooth or cable, by rendering it as animated QR codes or colour-matrix frames and reading them back with a camera.
metadata:
  title: "Optical file transfer (QR and colour-matrix)"
---

# Optical file transfer (QR and colour-matrix)

Two drsamonline projects move files optically. **BLINKTRANSFER** animates QR codes at ~20 FPS: each frame carries 1600 bytes (1573 data + a 27-byte header) and a receiver camera reassembles them. **blinkcode-ai** goes further with **SpectraCode** colour matrices: a file becomes a compact 'File DNA' container, is painted as a grid of 36 reference colours with bullseye markers and a calibration strip, and is decoded by detecting markers, fitting a homography and correcting colour per cell. Both are offline-first PWAs; no server is involved after first load.

## When to use

- Two devices must exchange a file with no shared network, no Bluetooth and no cable.
- The payload is small-to-moderate (hundreds of KB) and a few seconds of screen-to-camera time is acceptable.
- You want a demonstration of optical/vision coding in the browser with the platform's own APIs.

## Method

1. **Sender**: pick files, optionally compress (canvas-based JPEG for images at adjustable quality; `CompressionStream`/gzip for everything else), then render a **header frame** with metadata followed by an **animated data stream** at a fixed frame rate. Show a focus-assist/calibration pattern before the stream.
2. **Frame layout (QR path)**: pack each frame to ~1600 bytes = a header (version byte + 16-byte UUID + 4-byte k + 4-byte symbol index + 2-byte CRC) plus data, and render with a QR generator. Aim for a payload that scans reliably at the chosen FPS.
3. **Frame layout (colour-matrix path)**: encode the file into a 'File DNA' container, apply a Reed-Solomon `RS(255,223)` block code (16 correctable bytes/block), and paint cells with a 36-colour palette. Use bullseye markers + a calibration strip, two grid densities (120×80 / 60×40) signalled by a density patch, and auto-detect density on receive.
4. **Receiver**: request the camera (`getUserMedia`), continuously scan frames, detect markers, fit a homography, apply 3×4 colour correction, classify each cell, then collect frames by their index. Tolerate out-of-order frames; verify with CRC-32; stop when all symbols are collected; offer 'Save files' / Web Share.
5. Keep the screen awake during display/scan with the Wake Lock API; register a service worker so the app works offline after first load.
6. Provide a **loopback self-test** that pushes each rendered frame back through the real optical decoder, so the whole pipeline is testable on one device without a camera.
7. Validate decoding in simulation: render a code, apply perspective tilt, a colour cast and vignetting, and decode end-to-end in the test suite.
8. State the honest limits in the UI and README: throughput ≈ payload × frame rate (BLINKTRANSFER ~30 KB/s at 20 FPS; blinkcode ~15 KB/s at 3 FPS), one frame's capacity (blinkcode: 5,111 payload bytes; 1,097 in robust density), and that lossless 1000:1 compression is impossible (~2–4× on text, ~1× on already-compressed data).

## Key files / entry points

- BLINKTRANSFER: `src/lib/qrcode-gen.js`, `src/lib/utils.js`, `src/main.js`, `sw.js`, `manifest.json`; published under `docs/play/`.
- blinkcode-ai: `src/lib/arith.js` (arithmetic coder + order-1 model), `codec.js`, `format.js`, `image-codec.js`, `geometry.js`, `palette.js`, `rs.js`, `spectracode.js`, `spectra-decode.js`, `stream.js`, `storage.js`, `surface.js`; `src/workers/*`; `tools/build-model.js`, `tools/serve.js`; `tests/`.
- Both: `docs/play/index.html` + `docs/play/sw.js` (the offline PWA), `docs/index.html` (landing page).

## Gotchas

- Camera decode is validated in simulation, not against physical phone optics. Real glare, motion blur and cheap sensors may still need per-cell voting and multi-frame averaging.
- Every missed frame costs a full loop on the QR path — keep the frame rate and payload in balance with the target camera.
- Lossless compression cannot beat entropy: a '1000:1 lossless' claim is false. Extreme ratios only exist in a genuinely lossy perceptual mode (an image → 64-value latent → soft 32×32 reconstruction).
- The 'neural' model in blinkcode-ai is a mock with a real interface (order-1 byte statistics + DCT quantiser scales, ~129 KB) — the model bundle, caching and API are production-shaped, the weights are not a large net. TensorFlow.js is intentionally not bundled (no runtime CDN allowed).
- Wake Lock and `getUserMedia` need a secure context (https) and a user gesture; guard and message failures instead of failing silently.
- Keep the app self-contained (no CDN) so it still works after the first load with no network.

## Source projects

- [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) — animated QR file transfer at 20 FPS, 1600-byte frames, CRC-16 per frame, PWA.
- [blinkcode-ai](https://github.com/drsamonline/blinkcode-ai) — SpectraCode colour-matrix transfer with arithmetic coding, Reed-Solomon, homography-based decode and a loopback self-test.

