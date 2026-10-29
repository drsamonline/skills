---
name: pack-security-audit
description: Security review of code, APIs, services, CLIs and libraries: vulnerability classes to look for, hardening an input handler, adversarial review of a decision before it ships, and the guardrails that stop an agent running a destructive command.
license: see each member
metadata:
  title: "Security and audit pack"
  kind: "index pack"
  members: "9"
---

# Security and audit pack

9 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 5 upstream repositories (addyosmani/agent-skills, affaan-m/ECC, cloudflare/security-audit-skill, mattpocock/skills, sickn33/agentic-awesome-skills).

## When to use

- Auditing a codebase, endpoint, CLI or library for exploitable weaknesses.
- Hardening code against injection, auth bypass or unsafe deserialisation.
- A consequential decision needs a fresh-context adversarial pass.
- An agent needs hard guardrails around git and shell.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`constraint-driven-development`](../constraint-driven-development/SKILL.md) | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matter, supplies sane default thresholds… | addyosmani/agent-skills | MIT |
| [`doubt-driven-development`](../doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before proceeding, when… | addyosmani/agent-skills | MIT |
| [`flutter-dart-code-review`](../flutter-dart-code-review/SKILL.md) | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals), Dart idioms,… | affaan-m/ECC | MIT |
| [`git-guardrails-claude-code`](../git-guardrails-claude-code/SKILL.md) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git… | mattpocock/skills | MIT |
| [`laravel-security`](../laravel-security/SKILL.md) | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations. Use when reviewing… | affaan-m/ECC | MIT |
| [`mle-workflow`](../mle-workflow/SKILL.md) | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback. Use when building,… | affaan-m/ECC | MIT |
| [`security-and-hardening`](../security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authentication, data storage, or external integrations,… | addyosmani/agent-skills | MIT |
| [`security-audit`](../security-audit/SKILL.md) | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability… | cloudflare/security-audit-skill | MIT |
| [`zeroize-audit`](../zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow… | sickn33/agentic-awesome-skills | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (MIT). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
- Skills marked as mined from an aggregator have incomplete upstream attribution; check `meta.json` before republishing them elsewhere.
