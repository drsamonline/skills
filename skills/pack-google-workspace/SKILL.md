---
name: pack-google-workspace
description: Drive Gmail, Drive, Calendar, Docs, Sheets, Slides, Chat and Tasks from the command line with googleworkspace/cli — 95 skills covering auth, search, batch operations, file handling and the failure modes of each service.
license: see each member
metadata:
  title: "Google Workspace pack"
  kind: "index pack"
  members: "60"
---

# Google Workspace pack

60 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 1 upstream repositories.

## When to use

- Reading or sending mail, or searching a mailbox from a script.
- Creating, moving or sharing Drive files and folders.
- Reading or writing Sheets, Docs and Slides programmatically.
- Managing Calendar events, Tasks or Chat spaces.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`gws-admin-reports`](../gws-admin-reports/SKILL.md) | Google Workspace Admin SDK: Audit logs and usage reports. | googleworkspace/cli | Apache-2.0 |
| [`gws-calendar`](../gws-calendar/SKILL.md) | Google Calendar: Manage calendars and events. | googleworkspace/cli | Apache-2.0 |
| [`gws-calendar-agenda`](../gws-calendar-agenda/SKILL.md) | Google Calendar: Show upcoming events across all calendars. | googleworkspace/cli | Apache-2.0 |
| [`gws-calendar-insert`](../gws-calendar-insert/SKILL.md) | Google Calendar: Create a new event. | googleworkspace/cli | Apache-2.0 |
| [`gws-chat`](../gws-chat/SKILL.md) | Google Chat: Manage Chat spaces and messages. | googleworkspace/cli | Apache-2.0 |
| [`gws-chat-send`](../gws-chat-send/SKILL.md) | Google Chat: Send a message to a space. | googleworkspace/cli | Apache-2.0 |
| [`gws-classroom`](../gws-classroom/SKILL.md) | Google Classroom: Manage classes, rosters, and coursework. | googleworkspace/cli | Apache-2.0 |
| [`gws-docs`](../gws-docs/SKILL.md) | Read and write Google Docs. | googleworkspace/cli | Apache-2.0 |
| [`gws-docs-write`](../gws-docs-write/SKILL.md) | Google Docs: Append text to a document. | googleworkspace/cli | Apache-2.0 |
| [`gws-drive`](../gws-drive/SKILL.md) | Google Drive: Manage files, folders, and shared drives. | googleworkspace/cli | Apache-2.0 |
| [`gws-drive-upload`](../gws-drive-upload/SKILL.md) | Google Drive: Upload a file with automatic metadata. | googleworkspace/cli | Apache-2.0 |
| [`gws-events`](../gws-events/SKILL.md) | Subscribe to Google Workspace events. | googleworkspace/cli | Apache-2.0 |
| [`gws-events-renew`](../gws-events-renew/SKILL.md) | Google Workspace Events: Renew/reactivate Workspace Events subscriptions. | googleworkspace/cli | Apache-2.0 |
| [`gws-events-subscribe`](../gws-events-subscribe/SKILL.md) | Google Workspace Events: Subscribe to Workspace events and stream them as NDJSON. | googleworkspace/cli | Apache-2.0 |
| [`gws-forms`](../gws-forms/SKILL.md) | Read and write Google Forms. | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail`](../gws-gmail/SKILL.md) | Gmail: Send, read, and manage email. | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-forward`](../gws-gmail-forward/SKILL.md) | Gmail: Forward a message to new recipients. | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-read`](../gws-gmail-read/SKILL.md) | Gmail: Read a message and extract its body or headers. | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-reply`](../gws-gmail-reply/SKILL.md) | Gmail: Reply to a message (handles threading automatically). | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-reply-all`](../gws-gmail-reply-all/SKILL.md) | Gmail: Reply-all to a message (handles threading automatically). | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-send`](../gws-gmail-send/SKILL.md) | PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it. | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-triage`](../gws-gmail-triage/SKILL.md) | Gmail: Show unread inbox summary (sender, subject, date). | googleworkspace/cli | Apache-2.0 |
| [`gws-gmail-watch`](../gws-gmail-watch/SKILL.md) | Gmail: Watch for new emails and stream them as NDJSON. | googleworkspace/cli | Apache-2.0 |
| [`gws-keep`](../gws-keep/SKILL.md) | Manage Google Keep notes. | googleworkspace/cli | Apache-2.0 |
| [`gws-meet`](../gws-meet/SKILL.md) | Manage Google Meet conferences. | googleworkspace/cli | Apache-2.0 |
| [`gws-modelarmor`](../gws-modelarmor/SKILL.md) | Google Model Armor: Filter user-generated content for safety. | googleworkspace/cli | Apache-2.0 |
| [`gws-modelarmor-create-template`](../gws-modelarmor-create-template/SKILL.md) | Google Model Armor: Create a new Model Armor template. | googleworkspace/cli | Apache-2.0 |
| [`gws-modelarmor-sanitize-prompt`](../gws-modelarmor-sanitize-prompt/SKILL.md) | Google Model Armor: Sanitize a user prompt through a Model Armor template. | googleworkspace/cli | Apache-2.0 |
| [`gws-modelarmor-sanitize-response`](../gws-modelarmor-sanitize-response/SKILL.md) | Google Model Armor: Sanitize a model response through a Model Armor template. | googleworkspace/cli | Apache-2.0 |
| [`gws-people`](../gws-people/SKILL.md) | Google People: Manage contacts and profiles. | googleworkspace/cli | Apache-2.0 |
| [`gws-script`](../gws-script/SKILL.md) | Manage Google Apps Script projects. | googleworkspace/cli | Apache-2.0 |
| [`gws-script-push`](../gws-script-push/SKILL.md) | Google Apps Script: Upload local files to an Apps Script project. | googleworkspace/cli | Apache-2.0 |
| [`gws-shared`](../gws-shared/SKILL.md) | gws CLI: Shared patterns for authentication, global flags, and output formatting. | googleworkspace/cli | Apache-2.0 |
| [`gws-sheets`](../gws-sheets/SKILL.md) | Google Sheets: Read and write spreadsheets. | googleworkspace/cli | Apache-2.0 |
| [`gws-sheets-append`](../gws-sheets-append/SKILL.md) | Google Sheets: Append a row to a spreadsheet. | googleworkspace/cli | Apache-2.0 |
| [`gws-sheets-read`](../gws-sheets-read/SKILL.md) | Google Sheets: Read values from a spreadsheet. | googleworkspace/cli | Apache-2.0 |
| [`gws-slides`](../gws-slides/SKILL.md) | Google Slides: Read and write presentations. | googleworkspace/cli | Apache-2.0 |
| [`gws-tasks`](../gws-tasks/SKILL.md) | Google Tasks: Manage task lists and tasks. | googleworkspace/cli | Apache-2.0 |
| [`gws-workflow`](../gws-workflow/SKILL.md) | Google Workflow: Cross-service productivity workflows. | googleworkspace/cli | Apache-2.0 |
| [`gws-workflow-email-to-task`](../gws-workflow-email-to-task/SKILL.md) | Google Workflow: Convert a Gmail message into a Google Tasks entry. | googleworkspace/cli | Apache-2.0 |
| [`gws-workflow-file-announce`](../gws-workflow-file-announce/SKILL.md) | Google Workflow: Announce a Drive file in a Chat space. | googleworkspace/cli | Apache-2.0 |
| [`gws-workflow-meeting-prep`](../gws-workflow-meeting-prep/SKILL.md) | Google Workflow: Prepare for your next meeting: agenda, attendees, and linked docs. | googleworkspace/cli | Apache-2.0 |
| [`gws-workflow-standup-report`](../gws-workflow-standup-report/SKILL.md) | Google Workflow: Today's meetings + open tasks as a standup summary. | googleworkspace/cli | Apache-2.0 |
| [`gws-workflow-weekly-digest`](../gws-workflow-weekly-digest/SKILL.md) | Google Workflow: Weekly summary: this week's meetings + unread email count. | googleworkspace/cli | Apache-2.0 |
| [`persona-content-creator`](../persona-content-creator/SKILL.md) | Create, organize, and distribute content across Workspace. | googleworkspace/cli | Apache-2.0 |
| [`persona-customer-support`](../persona-customer-support/SKILL.md) | Manage customer support — track tickets, respond, escalate issues. | googleworkspace/cli | Apache-2.0 |
| [`persona-event-coordinator`](../persona-event-coordinator/SKILL.md) | Plan and manage events — scheduling, invitations, and logistics. | googleworkspace/cli | Apache-2.0 |
| [`persona-exec-assistant`](../persona-exec-assistant/SKILL.md) | Manage an executive's schedule, inbox, and communications. | googleworkspace/cli | Apache-2.0 |
| [`persona-hr-coordinator`](../persona-hr-coordinator/SKILL.md) | Handle HR workflows — onboarding, announcements, and employee comms. | googleworkspace/cli | Apache-2.0 |
| [`persona-it-admin`](../persona-it-admin/SKILL.md) | Administer IT — monitor security and configure Workspace. | googleworkspace/cli | Apache-2.0 |
| [`persona-project-manager`](../persona-project-manager/SKILL.md) | Coordinate projects — track tasks, schedule meetings, and share docs. | googleworkspace/cli | Apache-2.0 |
| [`persona-researcher`](../persona-researcher/SKILL.md) | Organize research — manage references, notes, and collaboration. | googleworkspace/cli | Apache-2.0 |
| [`persona-sales-ops`](../persona-sales-ops/SKILL.md) | Manage sales workflows — track deals, schedule calls, client comms. | googleworkspace/cli | Apache-2.0 |
| [`persona-team-lead`](../persona-team-lead/SKILL.md) | Lead a team — run standups, coordinate tasks, and communicate. | googleworkspace/cli | Apache-2.0 |
| [`recipe-calendar`](../recipe-calendar/SKILL.md) | Calendar and Meet recipes — events, free/busy, invites, conferences. Use when the task is to produce one of these variants and you need the right starting point rather than a… | googleworkspace/cli | Apache-2.0 |
| [`recipe-docs`](../recipe-docs/SKILL.md) | Docs and Slides recipes — create, template, share, report. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page. | googleworkspace/cli | Apache-2.0 |
| [`recipe-drive`](../recipe-drive/SKILL.md) | Drive recipes — folders, sharing, bulk download, change watches. Use when the task is to produce one of these variants and you need the right starting point rather than a blank… | googleworkspace/cli | Apache-2.0 |
| [`recipe-gmail`](../recipe-gmail/SKILL.md) | Gmail recipes — label, forward, archive, draft, auto-reply. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page. | googleworkspace/cli | Apache-2.0 |
| [`recipe-sheets`](../recipe-sheets/SKILL.md) | Sheets recipes — read, compare, duplicate, export, track. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page. | googleworkspace/cli | Apache-2.0 |
| [`recipe-workspace-admin`](../recipe-workspace-admin/SKILL.md) | Workspace admin recipes — tasks, forms, classroom, contacts, personas. Use when the task is to produce one of these variants and you need the right starting point rather than a… | googleworkspace/cli | Apache-2.0 |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
