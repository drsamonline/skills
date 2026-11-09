---
name: smartnote-scheduler
description: Turn a free-text note into a classified, prioritised, dated reminder with a server that survives restarts: model-assigned categories, a heartbeat that processes due reminders, and a delivery log you can audit.
metadata:
  title: "SmartNote Scheduler"
---

# SmartNote Scheduler — notes that classify and date themselves

Notes that schedule themselves: write a note in plain English and it is classified, prioritised, dated and reminded — no folders, no date pickers, no category dropdowns. The repository is **in development** and has no hosted demo, because it needs a server.

## When to use

- You are building a notes or task tool where the user should not have to file or date anything.
- Reminders must survive a restart, so an in-process timer is not acceptable.
- A background action (a push, an email) has to be auditable after the fact.

## Method

1. Fix the taxonomy in the product, not the database: five categories — Tasks, Deadlines, Schedule, Thoughts, Learning — chosen by the model, plus Low/Medium/High priority and the date and time the note contains.
2. Keep the stack boring and typed: React 19 + Vite on the client, tRPC for the API, Drizzle ORM over MySQL, one router per aggregate (`server/notes.router.ts`, `server/routers.ts`).
3. Process due reminders from a **heartbeat endpoint**, not an in-process timer, so a restart does not lose them.
4. Log every delivery attempt as `sent`, `failed` or `skipped`. A failure must be visible, never silent.
5. Test with vitest at the unit level — `ai.test.ts`, `notifications.test.ts`, `noteExports.test.ts`, `noteTemplates.test.ts`, `offlinePreview.test.ts`, `preferences.test.ts`, `auth.logout.test.ts` — and run `tsc --noEmit` as the type gate.
6. Migrate with `npm run db:push` (`drizzle-kit generate` then `migrate`) rather than hand-editing the schema.

## Key files / entry points

- `server/ai.ts` — classification, priority and date extraction.
- `server/notes.router.ts`, `server/routers.ts` — the API surface.
- `server/notifications.ts` — delivery and the heartbeat path.
- `server/db.ts`, `server/storage.ts`, `drizzle/` — persistence and migrations.
- `client/src/` — the app; `shared/` — types both sides use.
- `package.json` — `dev`, `build`, `test`, `check`, `db:push`.

## Gotchas

- A reminder scheduled with `setTimeout` dies with the process; the heartbeat is the only design that survives a deploy.
- "Skipped" is a delivery outcome, not an absence — logging only successes hides the case the user will ask about.
- No hosted demo is a consequence of the architecture, not an omission; a browser-only preview cannot show the heartbeat.
- The model assigns the category, so the category set is a product decision that the prompt and the UI must agree on.

## Source projects

- [smartnote-scheduler](https://github.com/drsamonline/smartnote-scheduler) — the classification, the heartbeat and the delivery log.
