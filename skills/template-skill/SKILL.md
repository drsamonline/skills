---
name: template-skill
description: Reusable template for authoring new Agent Skills with clear triggers, workflow, and I/O contracts.
license: see LICENSE-NOTICE.md
metadata:
  title: "template skill"
  origin: "NoizAI/skills"
  upstream-path: "skills/template-skill/SKILL.md"
  upstream-commit: "779f30af588ebf4dd17fc0acaa590ae147a0d3f5"
  category: "media-design"
---

# <skill-name>

[简体中文](./SKILL.zh-CN.md) | English

One-line description of what this skill solves.

## Triggers

- trigger keyword 1
- trigger keyword 2

## Use Cases

- Typical scenario 1
- Typical scenario 2
- Typical scenario 3

## Inputs

- Required inputs:
  - `field_a`: Description
  - `field_b`: Description
- Optional inputs:
  - `field_c`: Description

## Outputs

- Success output format (example)
- Failure output format (example)

## Workflow

1. Validate input completeness
2. Build request parameters
3. Execute core action
4. Format outputs
5. Provide retry or fallback strategy on failure

## Limitations

- Clearly define capability boundaries
- Explain common failure causes

## Examples

- Input example:
  - `...`
- Output example:
  - `...`

## Provenance

Imported from [NoizAI/skills](https://github.com/NoizAI/skills) at commit `779f30a`, path `skills/template-skill/SKILL.md`. The upstream repository publishes no licence file; included at the catalogue owner's direction, all rights with its authors — see `LICENSE-NOTICE.md`.
