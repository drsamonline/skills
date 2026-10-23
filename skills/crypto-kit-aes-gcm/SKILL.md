---
name: crypto-kit-aes-gcm
description: Encrypt app data in the browser with the Web Crypto API — AES-256-GCM for authenticated encryption and PBKDF2 for passphrase keys — behind a small shared wrapper instead of hand-rolled crypto.
metadata:
  title: "Browser crypto with AES-256-GCM"
---

# Browser crypto with AES-256-GCM

## When to use

When a web app needs to protect data on the device — a sealed note, a locked
page, a one-time-view message — and you want **authenticated** encryption without
shipping a crypto library or rolling your own primitives.

## Method

1. Use **Web Crypto** (`crypto.subtle`) — never implement AES or PBKDF2 yourself.
2. **AES-256-GCM** for encryption: it authenticates, so tampering throws instead
   of silently returning garbage.
3. **PBKDF2-SHA256** to turn a passphrase into a key (250,000 iterations by
   default; allow an override for tests).
4. **A sealed envelope** carries everything needed to open it: version, iteration
   count, salt, iv, ciphertext — as bytes or base64, so it is portable.
5. **One-time view:** seal with a random key, hand the key out of band, and delete
   it after the first `open`. The kit gives primitives; the app owns the "used
   once" state.
6. **AAD** (associated data) binds extra context to the ciphertext without
   encrypting it — useful for binding an id or a purpose.

## Key files

- `crypto-kit.js` — `CryptoKit.seal/open`, `sealString/openString`, `deriveKey`,
  `encrypt/decrypt`, `newKey/exportKey/importKey`, `randomBytes`.
- `test-node.js` — the verified round-trip (7 checks).

## Gotchas

- **Secure context required.** Web Crypto needs **https or localhost**; a page
  opened from `file://` may not have it. GitHub Pages is https, so deployed apps
  are fine.
- **Wrong passphrase and tampering both throw** — treat both as "cannot open".
- **Iterations cost time.** High is safer; allow a low value in tests so they
  stay fast.
- **Don't roll your own.** If you find yourself writing AES round functions or a
  hash, stop and use the platform.

## Source projects

`lockhtml` (command-line counterpart), and the browser apps `seance` / `vault`
that build on `crypto-kit`.
