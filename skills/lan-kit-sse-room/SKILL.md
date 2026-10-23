---
name: lan-kit-sse-room
description: Give a local-network app a real-time multi-client room without a WebSocket library or any dependency, using Server-Sent Events for server-to-client and plain POST for client-to-server.
metadata:
  title: "A LAN room with Server-Sent Events and POST"
---

# A LAN room with Server-Sent Events and POST

## When to use

When several devices on the same Wi-Fi need a shared live channel — a scoreboard,
a queue, a shared board — and there is **no internet** and you do not want to
bundle a WebSocket library.

## Method

1. **Host** (Node, zero deps): a plain `http` server.
2. **server → clients:** `GET /events` writes `text/event-stream`, keeps the
   response open, and writes `event: …\ndata: …\n\n` frames. Track each open
   response in a `Set`.
3. **clients → server:** `POST /send` reads the body and **broadcasts** it to
   every open SSE response.
4. **Keep-alive:** write a `: ping` comment every ~15 s so proxies and browsers
   do not drop an idle stream; `retry: 2000` tells the browser how fast to
   reconnect.
5. **Browser client:** `new EventSource(url + "/events")`, with `addEventListener`
   per event type; send with `fetch(url + "/send", {method:"POST", ...})`.
6. **Health:** `GET /health` returns the room and client count.

## Key files

- `lan-host.js` — `createHost({room, history})` → `listen`, `broadcast`,
  `onMessage`, `clients`, `close`.
- `lan-kit.js` — `Lan.client({url, onOpen, onMessage})`, `Lan.roomCode()`,
  `Lan.hostUrl(port)`.
- `test-node.js` — the verified host round-trip.

## Gotchas

- **No WebSocket framing.** SSE + POST avoids implementing RFC 6455 by hand —
  that is the whole reason to prefer it on a LAN.
- **Late joiners.** Keep a short message `history` and replay it on connect, or a
  device that joins mid-session sees nothing.
- **Not a security boundary.** Anyone on the LAN can read and post; add a room
  code check in the app, and never send secrets.
- **Node has no global `EventSource` before v22** — test the *host* in Node, and
  the *client* in a browser.

## Source projects

`HMS` (LAN hospital-management host); `lan-kit` (the shared host + client).
