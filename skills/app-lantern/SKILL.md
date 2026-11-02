---
name: app-lantern
description: A local content server: one device hosts a pack, everyone else opens the printed address in a plain browser and browses and searches it, with no internet at any point.
metadata:
  title: "Lantern — a library served over the room's Wi-Fi"
---

# Lantern — a library served over the room's Wi-Fi

One device becomes a local content server; everyone else on the network opens the address it prints in a plain browser and browses, searches and reads a bundled library. Nothing leaves the network. It is the LAN pattern applied to *reading* rather than to a shared board.

## When to use

- You need to serve content to a room with no internet and no app install.
- You are shipping a "pack" of content that a non-technical person can start.
- You want search over a bundled corpus without a database.

## Method

1. Keep the three parts separate: `server.js` (the host), `public/index.html` (what a phone opens), `lib/search.js` (the query).
2. Define a **pack** as data — `examples/starter-pack.json` is the worked example — so content can be added without touching the server.
3. Build the distributable with `tools/build.mjs` into `dist/lantern.js` (and the zipped pack), and audit it with `tools/audit.mjs`.
4. Reuse the shared room client in `public/lan-kit.js` rather than re-implementing the join handshake.
5. Test with `node test-node.js` (`npm test`) and `npm start` to run it; the README documents what happens when things go wrong.
6. Show a demo at `docs/demo/` on the landing page so the product can be understood without a second laptop.

## Key files / entry points

- `server.js` — the host; `public/index.html` — the reader UI.
- `lib/search.js` — search over the pack.
- `examples/starter-pack.json` — the pack format.
- `tools/build.mjs`, `tools/audit.mjs`, `dist/lantern.js`.

## Gotchas

- A phone that joins the Wi-Fi still needs the *address*; printing a QR is the difference between a demo and a product.
- A pack that is loaded whole into memory caps the corpus size — search should stream or index, not hold everything.
- `localhost` on the host is not reachable from the room; bind to the LAN interface and print that address.
- Zipped distributions drift from the source unless `tools/build.mjs` is the only way the zip is made.

## Source projects

- [app-lantern](https://github.com/drsamonline/app-lantern) — the host/reader/search split and the pack format.
