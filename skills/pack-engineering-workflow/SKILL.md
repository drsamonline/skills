---
name: pack-engineering-workflow
description: How the work itself is run: turn a request into a spec and tickets, implement in thin verifiable slices, test-first, debug systematically, request and receive review, dispatch subagents, and finish a branch — the full loop the popular agent skill collections are built around.
license: see each member
metadata:
  title: "Engineering workflow pack"
  kind: "index pack"
  members: "68"
---

# Engineering workflow pack

68 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 8 upstream repositories (DietrichGebert/ponytail, addyosmani/agent-skills, anthropics/skills, emilkowalski/skills, mattpocock/skills, mcollina/skills, …).

## When to use

- Starting anything larger than a one-file change.
- A plan or spec exists and has to become commits.
- Review is needed — asking for it, or acting on it.
- Work needs splitting across parallel agents, or handing off to a fresh session.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`ask-matt`](../ask-matt/SKILL.md) | Ask which skill or flow fits your situation. A router over the skills in this repo. | mattpocock/skills | MIT |
| [`brainstorming`](../brainstorming/SKILL.md) | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or out of… | obra/superpowers | MIT |
| [`chief-of-staff`](../chief-of-staff/SKILL.md) | Pursue a long-running goal in a single session by co-ordinating subagents. | mattpocock/skills | MIT |
| [`claude-handoff`](../claude-handoff/SKILL.md) | Hand the current conversation off to a fresh background agent that picks up the work immediately. | mattpocock/skills | MIT |
| [`code-review-and-quality`](../code-review-and-quality/SKILL.md) | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality… | addyosmani/agent-skills | MIT |
| [`code-simplification`](../code-simplification/SKILL.md) | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be.… | addyosmani/agent-skills | MIT |
| [`codebase-design`](../codebase-design/SKILL.md) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make… | mattpocock/skills | MIT |
| [`context-engineering`](../context-engineering/SKILL.md) | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure rules files and… | addyosmani/agent-skills | MIT |
| [`debugging-and-error-recovery`](../debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match expectations, or you encounter any… | addyosmani/agent-skills | MIT |
| [`deprecation-and-migration`](../deprecation-and-migration/SKILL.md) | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when migrating a database… | addyosmani/agent-skills | MIT |
| [`diagnosing-bugs`](../diagnosing-bugs/SKILL.md) | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. | mattpocock/skills | MIT |
| [`diagnosing-superpowers`](../diagnosing-superpowers/SKILL.md) | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took… | obra/superpowers | MIT |
| [`dispatching-parallel-agents`](../dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | obra/superpowers | MIT |
| [`documentation-and-adrs`](../documentation-and-adrs/SKILL.md) | Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public APIs, shipping… | addyosmani/agent-skills | MIT |
| [`domain-modeling`](../domain-modeling/SKILL.md) | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. | mattpocock/skills | MIT |
| [`executing-plans`](../executing-plans/SKILL.md) | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available | obra/superpowers | MIT |
| [`find-skills`](../find-skills/SKILL.md) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in… | vercel-labs/skills | MIT |
| [`finishing-a-development-branch`](../finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | obra/superpowers | MIT |
| [`git-workflow-and-versioning`](../git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy working tree into… | addyosmani/agent-skills | MIT |
| [`grill-me`](../grill-me/SKILL.md) | A relentless interview to sharpen a plan or design. | mattpocock/skills | MIT |
| [`grill-with-docs`](../grill-with-docs/SKILL.md) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | mattpocock/skills | MIT |
| [`grilling`](../grilling/SKILL.md) | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. | mattpocock/skills | MIT |
| [`handoff`](../handoff/SKILL.md) | Compact the current conversation into a handoff document for another agent to pick up. | mattpocock/skills | MIT |
| [`idea-refine`](../idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, when you need to stress-test… | addyosmani/agent-skills | MIT |
| [`implement`](../implement/SKILL.md) | Implement a piece of work based on a spec or set of tickets. | mattpocock/skills | MIT |
| [`implement-spec`](../implement-spec/SKILL.md) | Implement the result of /to-spec and /to-tickets in code. | mattpocock/skills | MIT |
| [`improve-codebase-architecture`](../improve-codebase-architecture/SKILL.md) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | mattpocock/skills | MIT |
| [`incremental-implementation`](../incremental-implementation/SKILL.md) | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a… | addyosmani/agent-skills | MIT |
| [`interview-me`](../interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview until ~95% confidence about the… | addyosmani/agent-skills | MIT |
| [`loop-me`](../loop-me/SKILL.md) | Grill me about specs for the workflows I want to build, within this workspace. | mattpocock/skills | MIT |
| [`migrate-to-shoehorn`](../migrate-to-shoehorn/SKILL.md) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. | mattpocock/skills | MIT |
| [`performance-optimization`](../performance-optimization/SKILL.md) | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, when you suspect performance regressions, when Core… | addyosmani/agent-skills | MIT |
| [`planning-and-task-breakdown`](../planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when… | addyosmani/agent-skills | MIT |
| [`ponytail`](../ponytail/SKILL.md) | You are a lazy senior developer. The best code is the code never written. You solve the whole problem with the least new code. End your reply with one or two lines: what you… | DietrichGebert/ponytail | MIT |
| [`ponytail-audit`](../ponytail-audit/SKILL.md) | Audit the whole repo like the senior developer who just inherited it and will be paged when it breaks. Order of importance: correct, safe, holds under load, tested, fast, lean.… | DietrichGebert/ponytail | MIT |
| [`ponytail-debt`](../ponytail-debt/SKILL.md) | Every deliberate ponytail shortcut is marked with a shortcut: comment naming its ceiling and upgrade path (older code may say ponytail:). This collects them into one ledger so… | DietrichGebert/ponytail | MIT |
| [`ponytail-gain`](../ponytail-gain/SKILL.md) | Show ponytail measured impact as a scoreboard: less code, less cost, more speed, from the agentic benchmark averages. One-shot display. | DietrichGebert/ponytail | MIT |
| [`ponytail-help`](../ponytail-help/SKILL.md) | Display this reference card when invoked. One-shot, do NOT change mode, write flag files, or persist anything. | DietrichGebert/ponytail | MIT |
| [`ponytail-review`](../ponytail-review/SKILL.md) | Review a change like the senior developer who will be paged when it breaks. Order of importance: correct, safe, holds under load, tested, fast, lean. Lean still matters: every… | DietrichGebert/ponytail | MIT |
| [`pr`](../pr/SKILL.md) | Use when writing a PR body. | mattpocock/skills | MIT |
| [`pr-labeling`](../pr-labeling/SKILL.md) | Classify a skills CLI pull request from its description and patch, while respecting existing labels. | vercel-labs/skills | MIT |
| [`prototype`](../prototype/SKILL.md) | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one that feels right.… | emilkowalski/skills | MIT |
| [`receiving-code-review`](../receiving-code-review/SKILL.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and… | obra/superpowers | MIT |
| [`requesting-code-review`](../requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | obra/superpowers | MIT |
| [`research`](../research/SKILL.md) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts… | mattpocock/skills | MIT |
| [`retro`](../retro/SKILL.md) | Conduct a retrospective on a coding session. | mattpocock/skills | MIT |
| [`scaffold-exercises`](../scaffold-exercises/SKILL.md) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or… | mattpocock/skills | MIT |
| [`setup-matt-pocock-skills`](../setup-matt-pocock-skills/SKILL.md) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills. | mattpocock/skills | MIT |
| [`setup-pre-commit`](../setup-pre-commit/SKILL.md) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure… | mattpocock/skills | MIT |
| [`setup-ts-deep-modules`](../setup-ts-deep-modules/SKILL.md) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files.… | mattpocock/skills | MIT |
| [`skill-creator`](../skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill,… | anthropics/skills | Apache-2.0 |
| [`skill-optimizer`](../skill-optimizer/SKILL.md) | Optimizes AI skills for activation, clarity, and cross-model reliability. Use when creating or editing skill packs, diagnosing weak skill uptake, reducing regressions, tuning… | mcollina/skills | MIT |
| [`source-driven-development`](../source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official docs before implementing it, or when you want… | addyosmani/agent-skills | MIT |
| [`spec-driven-development`](../spec-driven-development/SKILL.md) | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requirements document… | addyosmani/agent-skills | MIT |
| [`subagent-driven-development`](../subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session | obra/superpowers | MIT |
| [`systematic-debugging`](../systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | obra/superpowers | MIT |
| [`teach`](../teach/SKILL.md) | Teach the user a new skill or concept, within this workspace. | mattpocock/skills | MIT |
| [`to-questionnaire`](../to-questionnaire/SKILL.md) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | mattpocock/skills | MIT |
| [`to-spec`](../to-spec/SKILL.md) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. | mattpocock/skills | MIT |
| [`to-tickets`](../to-tickets/SKILL.md) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in… | mattpocock/skills | MIT |
| [`triage`](../triage/SKILL.md) | Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention. | vercel-labs/skills | MIT |
| [`using-agent-skills`](../using-agent-skills/SKILL.md) | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to the piece of work at hand. This is the meta-skill… | addyosmani/agent-skills | MIT |
| [`using-git-worktrees`](../using-git-worktrees/SKILL.md) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or… | obra/superpowers | MIT |
| [`using-superpowers`](../using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions | obra/superpowers | MIT |
| [`wait-what`](../wait-what/SKILL.md) | Stop. That last message did not land: re-pitch it. | mattpocock/skills | MIT |
| [`wizard`](../wizard/SKILL.md) | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking… | mattpocock/skills | MIT |
| [`writing-plans`](../writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code | obra/superpowers | MIT |
| [`writing-skills`](../writing-skills/SKILL.md) | Use when creating new skills, editing existing skills, or verifying skills work before deployment | obra/superpowers | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0, MIT). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
