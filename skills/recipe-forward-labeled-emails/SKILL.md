---
name: recipe-forward-labeled-emails
description: Find Gmail messages with a specific label and forward them to another address.
license: Apache-2.0
metadata:
  title: "recipe forward labeled emails"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-forward-labeled-emails/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Forward Labeled Gmail Messages

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Find Gmail messages with a specific label and forward them to another address.

## Steps

1. Find labeled messages: `gws gmail users messages list --params '{"userId": "me", "q": "label:needs-review"}' --format table`
2. Get message content: `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'`
3. Forward via new email: `gws gmail +send --to manager@company.com --subject 'FW: [Original Subject]' --body 'Forwarding for your review:

[Original Message Body]'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-forward-labeled-emails/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
