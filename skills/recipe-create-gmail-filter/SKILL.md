---
name: recipe-create-gmail-filter
description: Create a Gmail filter to automatically label, star, or categorize incoming messages.
license: Apache-2.0
metadata:
  title: "recipe create gmail filter"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-gmail-filter/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Gmail Filter

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Create a Gmail filter to automatically label, star, or categorize incoming messages.

## Steps

1. List existing labels: `gws gmail users labels list --params '{"userId": "me"}' --format table`
2. Create a new label: `gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Receipts"}'`
3. Create a filter: `gws gmail users settings filters create --params '{"userId": "me"}' --json '{"criteria": {"from": "receipts@example.com"}, "action": {"addLabelIds": ["LABEL_ID"], "removeLabelIds": ["INBOX"]}}'`
4. Verify filter: `gws gmail users settings filters list --params '{"userId": "me"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-gmail-filter/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
