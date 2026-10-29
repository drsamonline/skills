---
name: recipe-save-email-attachments
description: Find Gmail messages with attachments and save them to a Google Drive folder.
license: Apache-2.0
metadata:
  title: "recipe save email attachments"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-save-email-attachments/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Save Gmail Attachments to Google Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-drive`

Find Gmail messages with attachments and save them to a Google Drive folder.

## Steps

1. Search for emails with attachments: `gws gmail users messages list --params '{"userId": "me", "q": "has:attachment from:client@example.com"}' --format table`
2. Get message details: `gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'`
3. Download attachment: `gws gmail users messages attachments get --params '{"userId": "me", "messageId": "MESSAGE_ID", "id": "ATTACHMENT_ID"}'`
4. Upload to Drive folder: `gws drive +upload --file ./attachment.pdf --parent FOLDER_ID`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-save-email-attachments/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
