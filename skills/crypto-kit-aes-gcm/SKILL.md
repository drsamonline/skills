---
name: crypto-kit-aes-gcm
description: AES-256-GCM encryption with PBKDF2-SHA256 passphrase keys, a sealed envelope and a one-time-view helper on the Web Crypto API — the one place crypto lives.
metadata:
  title: "AES-256-GCM with PBKDF2 passphrases"
---

# AES-256-GCM with PBKDF2 passphrases

`CK` wraps the Web Crypto API so an app never hand-rolls cryptography:
authenticated AES-256-GCM, passphrase keys through PBKDF2-SHA256, a portable
sealed envelope, and a one-time-view helper. One file, no dependencies.

## When to use

- A record has to be encrypted at rest on the device, or sealed before it is
  exported.
- You need "open once, then it is gone" for a note or a file.
- You are about to write `crypto.subtle.importKey` by hand — don't; call this.

## Method

1. Check the platform: `CK.available()` is false when there is no
   `crypto.subtle`, which is the case for a page opened over `file://`.
2. Turn bytes into text/base64 with `CK.bytes.*` so a payload can be stored as a
   string.
3. Derive a key from a passphrase with PBKDF2-SHA256 (the kit's default is
   250,000 iterations) and seal the plaintext into an envelope of
   `salt + iv + ciphertext`.
4. Store or transmit the envelope as bytes or base64; open it with the same
   passphrase.
5. For one-time view, seal with a random key, keep the key only in memory, and
   delete it after the first successful open.

## Key files

- `crypto-kit.js` — `available`, `bytes.*`, passphrase key derivation, seal/open,
  one-time view.
- `test-node.js` — round-trip and tamper behaviour.

## Gotchas

- **Secure context only.** `crypto.subtle` exists over https or localhost and is
  absent on `file://`. The same single file that works on GitHub Pages throws
  when the user double-clicks it — guard with `available()` and say so plainly.
- The PBKDF2 iteration count is a compatibility constant, not a tuning knob:
  raising it makes every existing envelope unopenable.
- `lockhtml` uses **Argon2id**, not PBKDF2, and also ships Shamir shares, hidden
  volumes and recipient keys. Its envelopes and the kit's are not
  interchangeable, and those extras are not in the kit.
- `conqueror-os` and `lockhtml` both implement AES-GCM themselves in more than
  one file. Those are the duplicates this kit exists to retire.
- Authenticated encryption detects tampering — it does not hide that a file is
  encrypted, and it does not protect a weak passphrase.

## Source projects

- [crypto-kit](https://github.com/drsamonline/crypto-kit) — the wrapper.
- [lockhtml](https://github.com/drsamonline/lockhtml) — PIN-protected HTML with Argon2id, Shamir shares and one-time view.
- [app-encrypted-case-log](https://github.com/drsamonline/app-encrypted-case-log) — the app that vendors the kit.
- [seance](https://github.com/drsamonline/seance) — sealed notes, opened once.
