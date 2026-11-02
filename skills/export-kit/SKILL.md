---
name: export-kit
description: One zero-dependency file that turns bytes into a download, a Blob, a CSV or a store-only ZIP, working from file:// as well as Pages — so no app hand-rolls a save dialog or a ZIP writer again.
metadata:
  title: "Export kit — getting files off the device"
---

# Export kit — getting files off the device

Every single-file app was re-implementing the same thing: `Blob` → `URL.createObjectURL` → a hidden anchor → click. And one app hand-wrote a ZIP. This kit is that code once: `save()` for a download, `toBlob()`/`blobUrl()` for the primitives, a store-only `zip()` with `crc32`, and a CSV writer that unions the columns it is given.

## When to use

- An app needs to save text, JSON, CSV or binary to the user's device.
- You need a ZIP without a dependency and without compression.
- You are writing a table export and want one header row across heterogeneous rows.

## Method

1. Load `export-kit.js` as a plain script; it attaches `Export` to the global and also exports for Node (`module.exports`).
2. Use `Export.save(data, filename, mime)` for a download, or `toBlob()`/`blobUrl()` when you need the primitive.
3. Use `Export.zip(files)` for a store-only archive — it writes the central directory and CRC32 itself, so there is nothing to install.
4. Use the CSV helper for tabular export; it builds the header from the union of keys, so a sparse row does not shift the columns.
5. Test with `node test-node.js` and keep the worked demo at `demo/index.html`; the README's "Verified" section records what was actually exercised.

## Key files / entry points

- `export-kit.js` — the whole kit.
- `demo/index.html` — the worked example.
- `test-node.js` — the Node-side tests.

## Gotchas

- `URL.createObjectURL` leaks until revoked; a long-lived page that exports repeatedly must revoke.
- A store-only ZIP does not compress — say so, or someone will wonder why the file is large.
- CSV cells containing a quote, comma or newline need escaping; a naive join produces a file that opens wrong.
- A download triggered without a user gesture is blocked by some browsers; keep the call inside the click handler.

## Source projects

- [export-kit](https://github.com/drsamonline/export-kit) — the save/zip/csv primitives and the store-only ZIP writer.
