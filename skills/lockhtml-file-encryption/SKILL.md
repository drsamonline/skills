---
name: LockHTML — PIN-protected documents
description: Encrypt any file into a single self-contained .html that asks for a PIN (AES-256-GCM + Argon2id), with one-time view, expiry, recipient keys, hidden volumes, Shamir shares and age interop — via a Python CLI and a browser GUI.
---

# LockHTML — PIN-protected documents

LockHTML turns an ordinary file (HTML, PDF, photo, anything) into a single self-contained `.html` that asks for a PIN; enter it and the document appears. It offers one-time view / N views / expiry, Argon2id (default) or PBKDF2, X25519 recipient mode, age interop, Shamir secret sharing, keyfiles, Ed25519 signing, duress PIN, hidden volumes and watermarking. There is a Python CLI plus a browser GUI that runs offline.

## When to use

- You need to send a file that only opens with a PIN and optionally only once.
- You want browser-side decryption with no server and no upload.
- You need advanced modes: recipient public keys, hidden volumes, or k-of-n sharing.

## Method

1. CLI (Python 3.9+): derive a key from the PIN with Argon2id (or PBKDF2-SHA256), encrypt with AES-256-GCM, and emit a single `.html` that embeds the ciphertext plus a small decryption UI.
2. Implement the view policy (one-time / N views / do-not-open-before / expiry) and, for large streaming files, a chunked streaming bundle that decrypts straight to disk at constant memory (Chromium).
3. Optional modes: X25519 recipient keys (lock to a public key, PIN as second factor), `age` interop (read/write X25519 age files), Shamir k-of-n shares, keyfile requirement, Ed25519 signing, duress PIN (opens a decoy) and watermarking.
4. `--auto-kdf` times the machine and picks the strongest Argon2id cost that still unlocks quickly.
5. Browser GUI: a self-contained page using WebCrypto that decrypts a locked file offline; ship it as a PWA under `docs/play/`.
6. Build the portable EXE + APK with the shared workflow (`.github/workflows/build-apps.yml`), run tests with `.github/workflows/ci.yml`, and publish with `publish.yml`; `Makefile` drives local tasks.
7. Document the two containers and the format in `docs/DESIGN.md`, `docs/FORMAT.md`, `docs/AGE.md` and `docs/AUDIT.md`.

## Key files / entry points

- Python package + CLI entry points; `Makefile`.
- `docs/play/` — the browser GUI (WebCrypto), `docs/index.html` — landing page.
- `docs/DESIGN.md`, `docs/FORMAT.md`, `docs/AGE.md`, `docs/AUDIT.md`.
- `.github/workflows/ci.yml`, `build-apps.yml`, `publish.yml`.

## Gotchas

- Get the crypto right: AES-256-GCM with a unique nonce per message, a memory-hard KDF (Argon2id) and authenticated encryption. Do not invent primitives.
- One-time view is best-effort (the recipient can copy the plaintext) — say so plainly rather than overclaiming.
- Constant-memory streaming matters for video/disk images; building the whole file in memory will fail.
- The locked `.html` must be self-contained and work offline in any browser — no CDN.

## Source projects

- [lockhtml](https://github.com/drsamonline/lockhtml) — MIT, Python CLI + offline browser GUI.

