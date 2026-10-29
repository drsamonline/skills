---
name: recipe-watch-drive-changes
description: Subscribe to change notifications on a Google Drive file or folder.
license: Apache-2.0
metadata:
  title: "recipe watch drive changes"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-watch-drive-changes/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Watch for Drive Changes

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-events`

Subscribe to change notifications on a Google Drive file or folder.

## Steps

1. Create subscription: `gws events subscriptions create --json '{"targetResource": "//drive.googleapis.com/drives/DRIVE_ID", "eventTypes": ["google.workspace.drive.file.v1.updated"], "notificationEndpoint": {"pubsubTopic": "projects/PROJECT/topics/TOPIC"}, "payloadOptions": {"includeResource": true}}'`
2. List active subscriptions: `gws events subscriptions list`
3. Renew before expiry: `gws events +renew --subscription SUBSCRIPTION_ID`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-watch-drive-changes/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
