---
name: slides
description: Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies.
license: MIT
metadata:
  title: "slides"
  origin: "nextlevelbuilder/ui-ux-pro-max-skill"
  upstream-path: ".claude/skills/slides/SKILL.md"
  upstream-commit: "28b3b8dee8c976df4fa3e94aed4e092ad43fcb03"
  category: "frontend-ui"
---

# Slides

Strategic HTML presentation design with data visualization.

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `create` | Create strategic presentation slides | `references/create.md` |

## Script Paths

Script paths in this skill and its `references/` are relative to the directory that contains this SKILL.md, not to the project: `scripts/<file>` is this skill's own `scripts/` folder, and `../<skill>/scripts/<file>` is a sibling sub-skill installed alongside it. Build the full path from that directory (Claude Code reports it as the skill's base directory when the skill loads) and keep the working directory at the project root — the scripts read and write project files such as `docs/brand-guidelines.md`, `assets/design-tokens.json` or `src/` relative to it.

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Layout Patterns | `references/layout-patterns.md` |
| HTML Template | `references/html-template.md` |
| Copywriting Formulas | `references/copywriting-formulas.md` |
| Slide Strategies | `references/slide-strategies.md` |

## Routing

1. Parse subcommand from `$ARGUMENTS` (first word)
2. Load corresponding `references/{subcommand}.md`
3. Execute with remaining arguments

## Provenance

Imported from [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) at commit `28b3b8d`, path `.claude/skills/slides/SKILL.md`. Licensed MIT — the full text is in `LICENSE`.
