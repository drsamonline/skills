---
name: gws-events-renew
description: Google Workspace Events: Renew/reactivate Workspace Events subscriptions.
license: Apache-2.0
metadata:
  title: "gws events renew"
  origin: "googleworkspace/cli"
  upstream-path: "skills/gws-events-renew/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# events +renew

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Renew/reactivate Workspace Events subscriptions

## Usage

```bash
gws events +renew
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--name` | — | — | Subscription name to reactivate (e.g., subscriptions/SUB_ID) |
| `--all` | — | — | Renew all subscriptions expiring within --within window |
| `--within` | — | 1h | Time window for --all (e.g., 1h, 30m, 2d) |

## Examples

```bash
gws events +renew --name subscriptions/SUB_ID
gws events +renew --all --within 2d
```

## Tips

- Subscriptions expire if not renewed periodically.
- Use --all with a cron job to keep subscriptions alive.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-events](../gws-events/SKILL.md) — All subscribe to google workspace events commands

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/gws-events-renew/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
