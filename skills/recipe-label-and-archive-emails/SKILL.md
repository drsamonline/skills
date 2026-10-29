---
name: recipe-label-and-archive-emails
description: Apply Gmail labels to matching messages and archive them to keep your inbox clean.
license: Apache-2.0
metadata:
  title: "recipe label and archive emails"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-label-and-archive-emails/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Label and Archive Gmail Threads

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Apply Gmail labels to matching messages and archive them to keep your inbox clean.

## Steps

1. Search for matching emails: `gws gmail users messages list --params '{"userId": "me", "q": "from:notifications@service.com"}' --format table`
2. Apply a label: `gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"addLabelIds": ["LABEL_ID"]}'`
3. Archive (remove from inbox): `gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"removeLabelIds": ["INBOX"]}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-label-and-archive-emails/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
