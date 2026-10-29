---
name: recipe-send-team-announcement
description: Send a team announcement via both Gmail and a Google Chat space.
license: Apache-2.0
metadata:
  title: "recipe send team announcement"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-send-team-announcement/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Announce via Gmail and Google Chat

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-chat`

Send a team announcement via both Gmail and a Google Chat space.

## Steps

1. Send email: `gws gmail +send --to team@company.com --subject 'Important Update' --body 'Please review the attached policy changes.'`
2. Post in Chat: `gws chat +send --space spaces/TEAM_SPACE --text '📢 Important Update: Please check your email for policy changes.'`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-send-team-announcement/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
