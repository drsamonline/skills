---
name: smartbill-app
description: A fast, serverless single-page billing and invoicing app for Indian businesses: GST-ready (HSN/SAC, CGST/SGST, state codes, reverse charge), 100% local IndexedDB storage and A4 print layout.
metadata:
  title: "SmartBill India — serverless billing"
---

# SmartBill India — serverless billing

SmartBill India is a fast, serverless, single-page billing and invoicing app built with Vue.js and Tailwind for Indian businesses. All data is stored on-device in IndexedDB (no backend), with GST support (HSN/SAC, CGST, SGST, state codes, reverse charge), tax invoices / quotations / proforma invoices, master settings (company profile, bank details, logos, signatures, payment QR, pre-loaded items) and strict A4 print alignment.

## When to use

- You are building an offline, serverless business document app.
- You need GST-ready invoicing for India with A4 print parity.
- You want a local-first data model with export and no backend.

## Method

1. Single-page Vue 3 + Tailwind app; keep the built app at `docs/play/index.html` (root `index.html` mirrors it) so Pages serves it.
2. Store all data locally in IndexedDB — no backend database, no signup; the data stays on the device.
3. Model GST: HSN/SAC codes, CGST/SGST split, state codes and reverse-charge mechanics; support Tax Invoice, Quotation and Proforma.
4. Master settings: company profile, bank details, terms, and uploads for logo, authorised signature and payment QR; pre-load product/service items with default rates and tax brackets.
5. Print: strict grid alignment for professional A4 output; mobile-first responsive layout.
6. Ship a landing page (`docs/index.html`) with the full SEO block, `robots.txt`, `sitemap.xml`, `404.html`, `.nojekyll`; build EXE + APK with `.github/workflows/build-apps.yml`.
7. Licence: custom dual (state it clearly).

## Key files / entry points

- `docs/play/index.html` — the app; `index.html` — root copy; `docs/index.html` — landing page.
- `docs/assets/logo.svg`, `docs/404.html`, `docs/robots.txt`, `docs/sitemap.xml`, `docs/.nojekyll`.
- `.github/workflows/build-apps.yml`, `CHANGELOG.md`, `LICENSE`.

## Gotchas

- GST rules are jurisdiction-specific and change; label the tax fields precisely and never silently guess a rate.
- A4 print parity needs print-specific CSS (`@media print`), not just a responsive layout.
- Local-only storage means backups matter — offer export.
- The licence is a custom dual licence — state it plainly.

## Source projects

- [smartbill-app](https://github.com/drsamonline/smartbill-app) — Vue 3 + Tailwind, custom dual licence, v1.0.0.

