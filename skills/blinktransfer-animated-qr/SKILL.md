---
name: blinktransfer-animated-qr
description: Offline file transfer over animated QR codes at ~20 FPS: a Vite-built PWA compresses files, renders a header plus a data stream of 1600-byte frames, and reassembles them on a receiver camera.
metadata:
  title: "BlinkTransfer — animated QR file transfer"
---

# BlinkTransfer — animated QR file transfer

BlinkTransfer moves files between two devices with no internet, Bluetooth or cable, by animating QR codes at ~20 FPS. It compresses images (canvas JPEG at adjustable quality) or other files (gzip via `CompressionStream`), shows a focus-assist pattern, then streams a header frame and data frames; the receiver points its camera at the screen and reassembles the file. Practical speed ~30 KB/s; max 5 MB per file, 20 MB per batch.

## When to use

- You need to move a file with no shared network or cable.
- You want a small Vite PWA that still runs offline after first load.
- You want a reference for chunked, CRC-checked optical transfer.

## Method

1. Build with Vite: `npm run dev` (port 3000), `npm run build` → `dist/`, `npm run preview`. The built output is a small set of static assets; the app is also copied to `docs/play/` for Pages.
2. Compress before sending: images via canvas-based JPEG at 10–90% quality; everything else via the `CompressionStream` API (gzip).
3. Frame format: 1600 bytes per frame (1573 data + 27 header). Header = version(1) + UUID(16) + k(4) + symbolIndex(4) + CRC-16(2).
4. Sender flow: select files → optional quality → 2-second focus-assist pattern → header QR with metadata → animated data stream at 20 FPS → keep the screen visible.
5. Receiver flow: grant camera → point at the sender's QR → progress bar counts collected symbols → 'Save Files' when complete.
6. Use the Wake Lock API to keep the screen on during transfer, and a service worker to cache the app for offline use.
7. Add a QR generator (`src/lib/qrcode-gen.js`) and shared utils; ship a landing page in `docs/index.html` with `robots.txt`, `sitemap.xml`, `404.html` and `.nojekyll`.
8. Build the portable EXE + APK with the shared workflow (`.github/workflows/build-apps.yml`).

## Key files / entry points

- `src/main.js`, `src/lib/qrcode-gen.js`, `src/lib/utils.js`.
- `index.html`, `manifest.json`, `sw.js`, `vite.config.js`, `package.json`.
- `docs/play/` (published app), `docs/index.html` (landing page), `docs/404.html`, `robots.txt`, `sitemap.xml`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Frame rate and payload must be balanced against the target camera; a missed frame costs a full loop.
- The receiver needs a secure context for `getUserMedia` — Pages over https works; `file://` does not.
- Compression is not free: already-compressed input (JPEG/ZIP/MP4) barely shrinks, so transfer time tracks the original size.
- Keep the screen awake during display or the transfer stalls when the phone dims.
- The 5 MB/file and 20 MB/batch caps are practical, not arbitrary — document them.

## Source projects

- [BLINKTRANSFER](https://github.com/drsamonline/BLINKTRANSFER) — MIT, Vite PWA, 20 FPS animated QR transfer.

