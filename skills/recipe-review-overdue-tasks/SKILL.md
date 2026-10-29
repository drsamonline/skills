---
name: recipe-review-overdue-tasks
description: Find Google Tasks that are past due and need attention.
license: Apache-2.0
metadata:
  title: "recipe review overdue tasks"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-review-overdue-tasks/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Review Overdue Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Find Google Tasks that are past due and need attention.

## Steps

1. List task lists: `gws tasks tasklists list --format table`
2. List tasks with status: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID", "showCompleted": false}' --format table`
3. Review due dates and prioritize overdue items

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-review-overdue-tasks/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
