---
name: recipe-create-presentation
description: Create a new Google Slides presentation and add initial slides.
license: Apache-2.0
metadata:
  title: "recipe create presentation"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-presentation/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Google Slides Presentation

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-slides`

Create a new Google Slides presentation and add initial slides.

## Steps

1. Create presentation: `gws slides presentations create --json '{"title": "Quarterly Review Q2"}'`
2. Get the presentation ID from the response
3. Share with team: `gws drive permissions create --params '{"fileId": "PRESENTATION_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-presentation/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
