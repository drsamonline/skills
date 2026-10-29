---
name: recipe-create-meet-space
description: Create a Google Meet meeting space and share the join link.
license: Apache-2.0
metadata:
  title: "recipe create meet space"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-meet-space/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Google Meet Conference

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-meet`, `gws-gmail`

Create a Google Meet meeting space and share the join link.

## Steps

1. Create meeting space: `gws meet spaces create --json '{"config": {"accessType": "OPEN"}}'`
2. Copy the meeting URI from the response
3. Email the link: `gws gmail +send --to team@company.com --subject 'Join the meeting' --body 'Join here: MEETING_URI'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-meet-space/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
