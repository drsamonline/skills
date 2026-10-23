---
name: whispering-body-first-aid
description: A free, offline home first-aid companion (EN/HI/GU) with 30 commonly used homeopathic first-aid remedies, a plain-language symptom finder, dosing and handling guidance, and emergency signs.
metadata:
  title: "The Whispering Body — first-aid box"
---

# The Whispering Body — first-aid box

The Whispering Body — First-Aid Box is a free, offline home first-aid companion to the book *The Whispering Body*. It carries 30 commonly used homeopathic first-aid remedies, a plain-language symptom finder, dosing and handling guidance, and emergency signs, in English, हिन्दी and ગુજરાતી. Installable PWA; works offline.

## When to use

- You are building a multilingual (EN/HI/GU) offline consumer health app.
- You need a symptom-finder navigation over a small remedy set.
- You want the trilingual i18n pattern used across the companion apps.

## Method

1. Keep the app single-file and offline; publish at `docs/play/` with icons (`icon-192`, `icon-512`, maskable) and a landing page at `docs/index.html`.
2. Structure content as a plain-language symptom finder that leads to one of 30 first-aid remedies, plus dosing/handling guidance and emergency signs.
3. Implement the trilingual UI (English / Hindi / Gujarati) with a language switch; keep all three in sync.
4. Show the emergency reminder (call 112 / 108) and the 'general information only — not a substitute for professional care' notice.
5. Build EXE + APK with `.github/workflows/build-apps.yml`.

## Key files / entry points

- `docs/play/index.html` — the app; `docs/play/icon-*.png`.
- `docs/index.html` — landing page; `docs/icon-*.png`.
- `.github/workflows/build-apps.yml`.

## Gotchas

- Keep all three languages in sync — a missing translation is worse than a fallback.
- The emergency notice and the not-medical-advice disclaimer must be visible, not buried.
- Dosing guidance must match the source exactly; do not paraphrase doses.
- Content is copyrighted — free to use, reuse needs a licence.

## Source projects

- [whispering-body-first-aid](https://github.com/drsamonline/whispering-body-first-aid) — v2.0, free to use.

