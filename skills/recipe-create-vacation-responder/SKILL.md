---
name: recipe-create-vacation-responder
description: Enable a Gmail out-of-office auto-reply with a custom message and date range.
license: Apache-2.0
metadata:
  title: "recipe create vacation responder"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-vacation-responder/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Set Up a Gmail Vacation Responder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Enable a Gmail out-of-office auto-reply with a custom message and date range.

## Steps

1. Enable vacation responder: `gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": true, "responseSubject": "Out of Office", "responseBodyPlainText": "I am out of the office until Jan 20. For urgent matters, contact backup@company.com.", "restrictToContacts": false, "restrictToDomain": false}'`
2. Verify settings: `gws gmail users settings getVacation --params '{"userId": "me"}'`
3. Disable when back: `gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": false}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-vacation-responder/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
