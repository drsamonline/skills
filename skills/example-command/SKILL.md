---
name: example-command
description: An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout
license: Apache-2.0
metadata:
  title: "example command"
  origin: "anthropics/claude-plugins-official"
  upstream-path: "plugins/example-plugin/skills/example-command/SKILL.md"
  upstream-commit: "f8c5e7a1dcb71b10cb74586224b5401f3de5db28"
  category: "engineering-workflow"
---

# Example Command (Skill Format)

This demonstrates the `skills/<name>/SKILL.md` layout for user-invoked slash commands. It is functionally identical to the legacy `commands/example-command.md` format — both are loaded the same way; only the file layout differs.

## Arguments

The user invoked this with: $ARGUMENTS

## Instructions

When this skill is invoked:

1. Parse the arguments provided by the user
2. Perform the requested action using allowed tools
3. Report results back to the user

## Frontmatter Options Reference

Skills in this layout support these frontmatter fields:

- **name**: Skill identifier (matches directory name)
- **description**: Short description shown in /help
- **argument-hint**: Hints for command arguments shown to user
- **allowed-tools**: Pre-approved tools for this skill (reduces permission prompts)
- **model**: Override the model (e.g., "haiku", "sonnet", "opus")

## Example Usage

```
/example-command my-argument
/example-command arg1 arg2
```

## Provenance

Imported from [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) at commit `f8c5e7a`, path `plugins/example-plugin/skills/example-command/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
