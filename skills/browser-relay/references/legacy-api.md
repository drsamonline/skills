# Legacy HTTP API

Use these endpoints for compatibility with older clients. For new multi-step work, use the runtime and action API.

## HTTP API Reference

The HTTP API below is for code, tests, custom tools, and low-level debugging.
For interactive agent work, prefer the CLI workflow above.

Errors are structured across HTTP, CLI `--json`, and MCP tool errors:

```
{ "ok": false, "code": "invalid_request", "error": "url is required", "message": "url is required", "status": 400, "retryable": false }
```

Agents should branch on `code` rather than matching localized/free-form error
text. `retryable: true` means a reconnect/retry is reasonable.

### 1. browser_tabs
List all attached browser tabs.
```
GET http://127.0.0.1:18795/api/tabs
```
Returns: `{ ok: true, tabs: [{ id, title, url }] }`

### 2. browser_navigate
Navigate a tab to a URL.
```
POST http://127.0.0.1:18795/api/navigate
Header: Content-Type: application/json
Body: { "url": "https://example.com", "tabId?": "optional-tab-id" }
```

### 2b. browser_console
Read captured console, page error, and browser log entries.
```
GET http://127.0.0.1:18795/api/console?tabId=<id>&limit=100&level=error&clear=false
POST http://127.0.0.1:18795/api/console/clear
Body: { "tabId?": "...", "level?": "error" }
```
Use this after actions that may trigger frontend errors or warnings.

### 2c. browser_network
Read captured request/response/finished/failed network events. Sensitive
headers such as `Authorization`, `Cookie`, `Proxy-Authorization`, and
`Set-Cookie` are redacted; request bodies are not captured.
```
GET http://127.0.0.1:18795/api/network?tabId=<id>&type=response&status=500&limit=100&clear=false
POST http://127.0.0.1:18795/api/network/clear
Body: { "tabId?": "...", "type?": "request|response|finished|failed", "method?": "GET", "status?": 500, "requestId?": "...", "url?": "substring" }
```
Use this after actions that fail silently, after form submits, or when console
errors imply an API request failed.

### 3. browser_snapshot
Get a text representation of the current page (interactive elements annotated).
```
GET http://127.0.0.1:18795/api/snapshot?tabId=<id>&format=text&maxLength=100000
```
Format can be `"text"` (annotated DOM) or `"html"` (raw HTML).

### 3b. browser_wait
Wait for a CSS selector to be attached to the DOM or become visible. Prefer
this over fixed sleeps after navigation or actions.
```
POST http://127.0.0.1:18795/api/wait
Body: {
  "selector": "button.submit",
  "state?": "attached|visible",
  "timeoutMs?": 5000,
  "pollMs?": 100,
  "tabId?": "..."
}
```
`state` defaults to `visible`. `timeoutMs` accepts 1–20000 and `pollMs`
accepts 50–1000. A timeout returns `code: "wait_timeout"` with
`retryable: true`; a tab closing or the extension disconnecting fails
immediately instead of waiting for the timeout.

### 4. browser_click
Click an element by CSS selector. Scrolls into view first, uses real mouse events.
```
POST http://127.0.0.1:18795/api/click
Body: { "selector": "button.submit", "tabId?": "...", "doubleClick?": false }
```

### 5. browser_type
Type text into an input field. Optionally clear and submit.
```
POST http://127.0.0.1:18795/api/type
Body: {
  "text": "hello world",
  "selector?": "input[name='q']",
  "clear?": true,
  "submit?": true,
  "tabId?": "..."
}
```

### 6. browser_scroll
Scroll the page.
```
POST http://127.0.0.1:18795/api/scroll
Body: { "direction": "down|up|top|bottom", "amount?": 800, "tabId?": "..." }
```

### 7. browser_key
Press a key or keyboard shortcut using real keyboard events.
```
POST http://127.0.0.1:18795/api/key
Body: { "key?": "Enter", "combo?": "Control+L", "tabId?": "..." }
```

Use `combo` for shortcuts (`Control+L`, `Meta+K`, `Shift+Tab`) and `key`
for single keys (`Enter`, `Escape`, `ArrowDown`, `a`).

### 8. browser_screenshot
Capture a PNG screenshot (base64).
```
POST/GET http://127.0.0.1:18795/api/screenshot?tabId=<id>&fullPage=true
```
Full-page captures use layout metrics plus a clipped screenshot when possible,
then fall back to Chrome's `captureBeyondViewport` path. Returns:
`{ ok: true, data: "base64...", format: "png", fullPage, strategy, width?, height?, bytes }`

### 9. browser_eval
Evaluate arbitrary JavaScript in the page. The escape hatch.
```
POST http://127.0.0.1:18795/api/eval
Body: { "expression": "document.querySelector('h1').innerText", "tabId?": "..." }
```

### 10. browser_download
Get the URL of an image/media/link element.
```
POST http://127.0.0.1:18795/api/download
Body: { "selector": "img.profile-pic", "tabId?": "..." }
```

### 10. browser_download_start
Start a real Chrome download from a URL using the user's browser profile.
```
POST http://127.0.0.1:18795/api/download/start
Body: {
  "url": "https://example.com/file.pdf",
  "filename?": "files/file.pdf",
  "saveAs?": false,
  "conflictAction?": "uniquify|overwrite|prompt"
}
```
Returns: `{ ok: true, downloadId, id, options }`

### 11. browser_downloads
List Chrome downloads plus recent Browser Relay download events.
```
GET http://127.0.0.1:18795/api/downloads?limit=20&state=complete
POST http://127.0.0.1:18795/api/downloads/clear
```
Use this after `browser_download_start` to verify completion or diagnose interruptions.

Real downloads require the extension's `downloads` permission. If Browser Relay
was already loaded in Chrome before this capability was installed, reload the
unpacked extension in `chrome://extensions`.
