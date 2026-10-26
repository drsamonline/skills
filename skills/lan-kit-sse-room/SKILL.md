---
name: lan-kit-sse-room
description: A LAN room in the browser: a client over Server-Sent Events for server-to-client and POST for client-to-server, with a host URL helper — no internet, no accounts.
metadata:
  title: "A LAN room over SSE and POST"
---

# A LAN room over SSE and POST

`Lan` is the light way to put several devices in one room on the same Wi-Fi:
the host serves a room, the clients subscribe with Server-Sent Events and talk
back with POST. No internet, no accounts, no build step.

## When to use

- Several people in one room must see the same live state (a whiteboard, an
  order board, a scoreboard) and there is no internet.
- You want live updates without a WebSocket server or a dependency.
- The heavy option (a database-owning server) is more than the problem needs.

## Method

1. Run `lan-host.js` on one machine in the room; it serves the room and a
   `Lan.hostUrl(port)` helper the clients can use.
2. On each client: `var c = Lan.client({ url: Lan.hostUrl(8080), onOpen: fn,
   onMessage: fn })`. `onOpen` gives you the room identity.
3. Send with `c.send({ from: "me", text: "hello room" })` — every client message
   is a POST to the host.
4. Keep the message small and idempotent: the host broadcasts what it receives,
   and a client that reconnects gets the room's current state, not a replay of
   every message.
5. Announce the URL in the room (a QR code is the usual way) so nobody types an
   IP address.

## Key files

- `lan-kit.js` — the browser client (`Lan.client`, `Lan.hostUrl`, `send`).
- `lan-host.js` — the host side the client talks to.

## Gotchas

- SSE is one-way. Server-to-client is a stream; client-to-server is a POST per
  message, so a chatty room becomes many small requests.
- There is **no authentication**: anyone on the Wi-Fi who has the URL is in the
  room. Never put patient data, marks or anything private in a room.
- `HMS` is the heavy sibling — a server that owns SQLite, with UDP discovery and
  a WebView2 client. Choose it when the data must persist on a server.
- `canteen-lan` and `chalk-lan` both vendor `lan-kit.js`, so this is one of the
  few kits with real adoption; a change here must be re-vendored in both.
- A phone that changes network drops the room; the app must re-subscribe rather
  than show a frozen board.

## Source projects

- [lan-kit](https://github.com/drsamonline/lan-kit) — client and host.
- [canteen-lan](https://github.com/drsamonline/canteen-lan) — order from the table over the room's Wi-Fi.
- [chalk-lan](https://github.com/drsamonline/chalk-lan) — one whiteboard for the room.
- [app-companion-forge](https://github.com/drsamonline/app-companion-forge) — an offline pocket console for Forge that uses the kit.
