---
name: pack-security-audit
description: Security review of code, APIs, services, CLIs and libraries: vulnerability classes to look for, hardening an input handler, adversarial review of a decision before it ships, and the guardrails that stop an agent running a destructive command.
license: see each member
metadata:
  title: "Security and audit pack"
  kind: "index pack"
  members: "24"
---

# Security and audit pack

24 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 7 upstream repositories.

## When to use

- Auditing a codebase, endpoint, CLI or library for exploitable weaknesses.
- Hardening code against injection, auth bypass or unsafe deserialisation.
- A consequential decision needs a fresh-context adversarial pass.
- An agent needs hard guardrails around git and shell.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`anti-entropy-governance`](../anti-entropy-governance/SKILL.md) | Use when touching retiring old logic, collapsing duplicate owners, removing fallbacks, or schema/persistence/source-of-truth boundaries; identify opportunities automatically;… | GanyuanRan/Aegis | MIT |
| [`communicating-concisely`](../communicating-concisely/SKILL.md) | Use when the user asks for caveman mode, fewer tokens, brief responses, compressed communication, or otherwise explicitly requests a much shorter answer. | GanyuanRan/Aegis | MIT |
| [`constraint-driven-development`](../constraint-driven-development/SKILL.md) | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matter, supplies sane default thresholds… | addyosmani/agent-skills | MIT |
| [`doubt-driven-development`](../doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before proceeding, when… | addyosmani/agent-skills | MIT |
| [`establishing-project-context`](../establishing-project-context/SKILL.md) | Use when the user asks to establish shared project language, or project work exposes a conflicting, renamed, or deprecated domain term that needs active semantic modeling.… | GanyuanRan/Aegis | MIT |
| [`first-principles-review`](../first-principles-review/SKILL.md) | Use when asked for first-principles or Occam's-razor review, or when high-risk decisions involve competing constraints, fallback growth, duplicate owners, or architecture… | GanyuanRan/Aegis | MIT |
| [`flutter-dart-code-review`](../flutter-dart-code-review/SKILL.md) | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals), Dart idioms,… | affaan-m/ECC | MIT |
| [`git-guardrails-claude-code`](../git-guardrails-claude-code/SKILL.md) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git… | mattpocock/skills | MIT |
| [`goal-framing`](../goal-framing/SKILL.md) | Use when the user explicitly sets an Aegis goal with /aegis-goal, Aegis goal:, or asks to define goal, success evidence, stop condition, or task boundaries before work. | GanyuanRan/Aegis | MIT |
| [`laravel-security`](../laravel-security/SKILL.md) | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations. Use when reviewing… | affaan-m/ECC | MIT |
| [`long-task-continuation`](../long-task-continuation/SKILL.md) | Use when a task is multi-step, may span context resets or sessions, uses subagents, or risks losing state before completion. | GanyuanRan/Aegis | MIT |
| [`mle-workflow`](../mle-workflow/SKILL.md) | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback. Use when building,… | affaan-m/ECC | MIT |
| [`recording-architecture-decisions`](../recording-architecture-decisions/SKILL.md) | Use when the user asks to create, write, update, amend, supersede, or evaluate an ADR, architecture decision record, durable architecture decision, decision log, or baseline… | GanyuanRan/Aegis | MIT |
| [`requesting-code-review`](../requesting-code-review/SKILL.md) | Use when requesting independent code review, after implementation slices, before merging high-risk work, or when verification exposes evidence, baseline, architecture,… | GanyuanRan/Aegis | MIT |
| [`security-and-hardening`](../security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authentication, data storage, or external integrations,… | addyosmani/agent-skills | MIT |
| [`security-audit`](../security-audit/SKILL.md) | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability… | cloudflare/security-audit-skill | MIT |
| [`systematic-debugging`](../systematic-debugging/SKILL.md) | Use when encountering a bug, test failure, or unexpected behavior, before proposing fixes | GanyuanRan/Aegis | MIT |
| [`ui-ux-governance`](../ui-ux-governance/SKILL.md) | Use when designing, changing, or reviewing user-facing interfaces or interaction flows, including API changes that alter visible states or recovery. Backend-only work without… | GanyuanRan/Aegis | MIT |
| [`update-aegis`](../update-aegis/SKILL.md) | Use when the user says `aegis:update`, asks to update or upgrade an installed Aegis method-pack, wants the latest Aegis version, or asks whether Aegis is current on this host. | GanyuanRan/Aegis | MIT |
| [`using-aegis`](../using-aegis/SKILL.md) | Use when starting a turn or checking Aegis skill routing. | GanyuanRan/Aegis | MIT |
| [`varlock`](../varlock/SKILL.md) | Secure environment variable management with Varlock. Use when handling secrets, API keys, credentials, or any sensitive configuration. Ensures secrets are never exposed in… | wrsmith108/varlock-claude-skill | MIT |
| [`verification-before-completion`](../verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed, passing, verified, release-ready, or ready to commit, merge, publish, or hand off. | GanyuanRan/Aegis | MIT |
| [`writing-plans`](../writing-plans/SKILL.md) | Use when you have an approved spec or written requirements for a multi-step task that needs a durable plan document before touching code. Small, single-owner, or fast-path… | GanyuanRan/Aegis | MIT |
| [`zeroize-audit`](../zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow… | sickn33/agentic-awesome-skills | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (MIT). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
