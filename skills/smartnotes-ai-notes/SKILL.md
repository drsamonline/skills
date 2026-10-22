---
name: SmartNotes — AI note scheduler
description: An AI-powered note capture, categorisation and reminder-scheduling app with a brutalist UI: write in plain English and an LLM classifies, prioritises, titles and extracts dates.
---

# SmartNotes — AI note scheduler

SmartNote Scheduler is an AI-powered note capture, categorisation and reminder-scheduling app with a brutalist UI. Write notes in plain natural language and an LLM classifies them (Tasks, Deadlines, Schedule, Thoughts, Learning), detects priority, generates a title, and extracts dates/times ('tomorrow at 3pm'). Built with React 19, tRPC 11 and Drizzle ORM. MIT.

## When to use

- You are building an LLM-assisted productivity app and need a structured classification flow.
- You want a React 19 + tRPC 11 + Drizzle reference with a brutalist design system.
- You need natural-language date extraction into scheduled reminders.

## Method

1. Client: React 19 (Vite) with a brutalist UI (`client/src/components/*`: dashboard, note card, filters, dialogs, AI chat box, error boundary).
2. API: tRPC 11 over a typed server with Drizzle ORM and a migration folder (`drizzle/`, `drizzle.config.ts`).
3. On note capture, call the LLM to classify the note, detect priority (Low/Medium/High), generate a title, and extract dates/times into reminders.
4. Keep the components small and composable; include a `_core` hooks layer and an error boundary.
5. Document the roadmap in `docs/IMPLEMENTATION_PLAN.md` and the portable-app plan in `docs/PORTABLE_APPS.md`.
6. Ship the landing page at `docs/index.html`; licence MIT.

## Key files / entry points

- `client/src/components/*`, `client/src/App.tsx`, `client/index.html`.
- `drizzle/`, `drizzle.config.ts` — schema/migrations.
- `docs/IMPLEMENTATION_PLAN.md`, `docs/PORTABLE_APPS.md`, `docs/index.html`.
- `eslint.config.js`, `components.json`.

## Gotchas

- LLM classification must degrade gracefully: if the model is unavailable, still save the note unclassified rather than losing it.
- Natural-language date parsing is error-prone — show the parsed date and let the user correct it.
- Never hardcode API keys; use environment configuration and flag it.
- Portable EXE/APK support is planned, not shipped — do not imply otherwise.

## Source projects

- [SmartNotes](https://github.com/drsamonline/SmartNotes) — MIT, v1.0.0, React 19 + tRPC 11 + Drizzle.

