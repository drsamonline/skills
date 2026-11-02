---
name: ai-bridge
description: A VS Code extension plus bridge that attaches to an already signed-in browser tab over the Chrome DevTools Protocol and drives it from the editor — no API key, with per-site adapters and an OpenAI-compatible surface.
metadata:
  title: "AI Bridge — driving a signed-in web chat from the editor"
---

# AI Bridge — driving a signed-in web chat from the editor

You are already signed in to ChatGPT in Chrome. AI Bridge attaches to that tab over the Chrome DevTools Protocol and drives it from inside VS Code: reading answers, writing edits into the workspace, and keeping project state that survives a new chat. No API key and no second subscription.

## When to use

- You want to reuse a signed-in web chat from an editor instead of paying for a second API.
- You are writing a browser-driving integration that must survive a UI change.
- You need one internal surface over several chat providers with different DOMs.

## Method

1. Split the TypeScript workspace into three projects — `shared/`, `bridge/`, `extension/` — with project references and `tsc -b` as the build; bundle the extension with esbuild (`npm run build:bundle`).
2. Put each provider behind an adapter in `bridge/src/adapters/` (`chatgpt.ts`, `claude.ts`, `gemini.ts`, `custom.ts`, `domAdapter.ts`) with a shared `types.ts` and a `registry.ts`; a DOM change is then one adapter, not the bridge.
3. Expose an OpenAI-compatible surface in `bridge/src/api/` (`openaiCompat.ts`, `stream.ts`, `errors.ts`, `modelId.ts`) so editor clients that speak that protocol work unchanged.
4. Handle sign-in explicitly (`adapters/signin.ts`) — the whole premise is that a session exists, so detecting its absence is a first-class path.
5. Test per behaviour with the `test/*.cjs` scripts, including the CDP attach (`test/cdp-attach.cjs`), a fixture adapter (`test/chatgpt-fixture.cjs`) and the handshake; `npm run test:all` is the gate.
6. Package with `npm run package` (`scripts/make-vsix.mjs`) and release via `.github/workflows/release.yml`.

## Key files / entry points

- `bridge/src/adapters/` — per-provider DOM drivers.
- `bridge/src/api/` — the OpenAI-compatible surface and streaming.
- `extension/` — the VS Code client; `shared/` — the common types.
- `test/*.cjs` — the behaviour tests; `scripts/make-vsix.mjs` — packaging.

## Gotchas

- Scraping a web UI is a moving target: keep the selectors in one adapter and assert the shape with a fixture.
- The CDP attach needs a browser started with remote debugging; a normally-launched Chrome will not accept the connection.
- "No API key" is only true while the tab is signed in — a session expiry has to surface as a clear error, not an empty answer.
- Streaming a response that the UI renders progressively means the completion signal comes from the DOM, not from a protocol event.

## Source projects

- [ai-bridge](https://github.com/drsamonline/ai-bridge) — the adapter registry, the OpenAI-compatible surface and the CDP test suite.
