---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
license: MIT
metadata:
  title: "handoff"
  origin: "mattpocock/skills"
  upstream-path: "skills/productivity/handoff/SKILL.md"
  upstream-commit: "a496f5513d4a4cf889bc48e189e579f4b0bdf6aa"
  category: "engineering-workflow"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

## Provenance

Imported from [mattpocock/skills](https://github.com/mattpocock/skills) at commit `a496f55`, path `skills/productivity/handoff/SKILL.md`. Licensed MIT by its authors — the full text is in `LICENSE`.
