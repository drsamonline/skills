---
name: gws-gmail
description: Gmail: Send, read, and manage email.
license: Apache-2.0
metadata:
  title: "gws gmail"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-gmail/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# gmail (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws gmail <resource> <method> [flags]
```

## Helper Commands

| Command | Description |
|---------|-------------|
| [`+send`](../gws-gmail-send/SKILL.md) | Send an email |
| [`+triage`](../gws-gmail-triage/SKILL.md) | Show unread inbox summary (sender, subject, date) |
| [`+reply`](../gws-gmail-reply/SKILL.md) | Reply to a message (handles threading automatically) |
| [`+reply-all`](../gws-gmail-reply-all/SKILL.md) | Reply-all to a message (handles threading automatically) |
| [`+forward`](../gws-gmail-forward/SKILL.md) | Forward a message to new recipients |
| [`+read`](../gws-gmail-read/SKILL.md) | Read a message and extract its body or headers |
| [`+watch`](../gws-gmail-watch/SKILL.md) | Watch for new emails and stream them as NDJSON |

## API Resources

### users

  - `getProfile` — Gets the current user's Gmail profile.
  - `stop` — Stop receiving push notifications for the given user mailbox.
  - `watch` — Set up or update a push notification watch on the given user mailbox.
  - `drafts` — Operations on the 'drafts' resource
  - `history` — Operations on the 'history' resource
  - `labels` — Operations on the 'labels' resource
  - `messages` — Operations on the 'messages' resource
  - `settings` — Operations on the 'settings' resource
  - `threads` — Operations on the 'threads' resource

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws gmail --help

# Inspect a method's required params, types, and defaults
gws schema gmail.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-gmail/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
