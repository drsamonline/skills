---
name: pack-google-workspace
description: Drive Gmail, Drive, Calendar, Docs, Sheets, Slides, Chat and Tasks from the command line with googleworkspace/cli — 95 skills covering auth, search, batch operations, file handling and the failure modes of each service.
license: see each member
metadata:
  title: "Google Workspace pack"
  kind: "index pack"
  members: "95"
---

# Google Workspace pack

95 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 1 upstream repositories.

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
| [`recipe-backup-sheet-as-csv`](../recipe-backup-sheet-as-csv/SKILL.md) | Export a Google Sheets spreadsheet as a CSV file for local backup or processing. | googleworkspace/cli | Apache-2.0 |
| [`recipe-batch-invite-to-event`](../recipe-batch-invite-to-event/SKILL.md) | Add a list of attendees to an existing Google Calendar event and send notifications. | googleworkspace/cli | Apache-2.0 |
| [`recipe-block-focus-time`](../recipe-block-focus-time/SKILL.md) | Create recurring focus time blocks on Google Calendar to protect deep work hours. | googleworkspace/cli | Apache-2.0 |
| [`recipe-bulk-download-folder`](../recipe-bulk-download-folder/SKILL.md) | List and download all files from a Google Drive folder. | googleworkspace/cli | Apache-2.0 |
| [`recipe-collect-form-responses`](../recipe-collect-form-responses/SKILL.md) | Retrieve and review responses from a Google Form. | googleworkspace/cli | Apache-2.0 |
| [`recipe-compare-sheet-tabs`](../recipe-compare-sheet-tabs/SKILL.md) | Read data from two tabs in a Google Sheet to compare and identify differences. | googleworkspace/cli | Apache-2.0 |
| [`recipe-copy-sheet-for-new-month`](../recipe-copy-sheet-for-new-month/SKILL.md) | Duplicate a Google Sheets template tab for a new month of tracking. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-classroom-course`](../recipe-create-classroom-course/SKILL.md) | Create a Google Classroom course and invite students. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-doc-from-template`](../recipe-create-doc-from-template/SKILL.md) | Copy a Google Docs template, fill in content, and share with collaborators. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-events-from-sheet`](../recipe-create-events-from-sheet/SKILL.md) | Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-expense-tracker`](../recipe-create-expense-tracker/SKILL.md) | Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-feedback-form`](../recipe-create-feedback-form/SKILL.md) | Create a Google Form for feedback and share it via Gmail. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-gmail-filter`](../recipe-create-gmail-filter/SKILL.md) | Create a Gmail filter to automatically label, star, or categorize incoming messages. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-meet-space`](../recipe-create-meet-space/SKILL.md) | Create a Google Meet meeting space and share the join link. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-presentation`](../recipe-create-presentation/SKILL.md) | Create a new Google Slides presentation and add initial slides. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-shared-drive`](../recipe-create-shared-drive/SKILL.md) | Create a Google Shared Drive and add members with appropriate roles. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-task-list`](../recipe-create-task-list/SKILL.md) | Set up a new Google Tasks list with initial tasks. | googleworkspace/cli | Apache-2.0 |
| [`recipe-create-vacation-responder`](../recipe-create-vacation-responder/SKILL.md) | Enable a Gmail out-of-office auto-reply with a custom message and date range. | googleworkspace/cli | Apache-2.0 |
| [`recipe-draft-email-from-doc`](../recipe-draft-email-from-doc/SKILL.md) | Read content from a Google Doc and use it as the body of a Gmail message. | googleworkspace/cli | Apache-2.0 |
| [`recipe-email-drive-link`](../recipe-email-drive-link/SKILL.md) | Share a Google Drive file and email the link with a message to recipients. | googleworkspace/cli | Apache-2.0 |
| [`recipe-find-free-time`](../recipe-find-free-time/SKILL.md) | Query Google Calendar free/busy status for multiple users to find a meeting slot. | googleworkspace/cli | Apache-2.0 |
| [`recipe-find-large-files`](../recipe-find-large-files/SKILL.md) | Identify large Google Drive files consuming storage quota. | googleworkspace/cli | Apache-2.0 |
| [`recipe-forward-labeled-emails`](../recipe-forward-labeled-emails/SKILL.md) | Find Gmail messages with a specific label and forward them to another address. | googleworkspace/cli | Apache-2.0 |
| [`recipe-generate-report-from-sheet`](../recipe-generate-report-from-sheet/SKILL.md) | Read data from a Google Sheet and create a formatted Google Docs report. | googleworkspace/cli | Apache-2.0 |
| [`recipe-label-and-archive-emails`](../recipe-label-and-archive-emails/SKILL.md) | Apply Gmail labels to matching messages and archive them to keep your inbox clean. | googleworkspace/cli | Apache-2.0 |
| [`recipe-log-deal-update`](../recipe-log-deal-update/SKILL.md) | Append a deal status update to a Google Sheets sales tracking spreadsheet. | googleworkspace/cli | Apache-2.0 |
| [`recipe-organize-drive-folder`](../recipe-organize-drive-folder/SKILL.md) | Create a Google Drive folder structure and move files into the right locations. | googleworkspace/cli | Apache-2.0 |
| [`recipe-plan-weekly-schedule`](../recipe-plan-weekly-schedule/SKILL.md) | Review your Google Calendar week, identify gaps, and add events to fill them. | googleworkspace/cli | Apache-2.0 |
| [`recipe-post-mortem-setup`](../recipe-post-mortem-setup/SKILL.md) | Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat. | googleworkspace/cli | Apache-2.0 |
| [`recipe-reschedule-meeting`](../recipe-reschedule-meeting/SKILL.md) | Move a Google Calendar event to a new time and automatically notify all attendees. | googleworkspace/cli | Apache-2.0 |
| [`recipe-review-meet-participants`](../recipe-review-meet-participants/SKILL.md) | Review who attended a Google Meet conference and for how long. | googleworkspace/cli | Apache-2.0 |
| [`recipe-review-overdue-tasks`](../recipe-review-overdue-tasks/SKILL.md) | Find Google Tasks that are past due and need attention. | googleworkspace/cli | Apache-2.0 |
| [`recipe-save-email-attachments`](../recipe-save-email-attachments/SKILL.md) | Find Gmail messages with attachments and save them to a Google Drive folder. | googleworkspace/cli | Apache-2.0 |
| [`recipe-save-email-to-doc`](../recipe-save-email-to-doc/SKILL.md) | Save a Gmail message body into a Google Doc for archival or reference. | googleworkspace/cli | Apache-2.0 |
| [`recipe-schedule-recurring-event`](../recipe-schedule-recurring-event/SKILL.md) | Create a recurring Google Calendar event with attendees. | googleworkspace/cli | Apache-2.0 |
| [`recipe-send-team-announcement`](../recipe-send-team-announcement/SKILL.md) | Send a team announcement via both Gmail and a Google Chat space. | googleworkspace/cli | Apache-2.0 |
| [`recipe-share-doc-and-notify`](../recipe-share-doc-and-notify/SKILL.md) | Share a Google Docs document with edit access and email collaborators the link. | googleworkspace/cli | Apache-2.0 |
| [`recipe-share-event-materials`](../recipe-share-event-materials/SKILL.md) | Share Google Drive files with all attendees of a Google Calendar event. | googleworkspace/cli | Apache-2.0 |
| [`recipe-share-folder-with-team`](../recipe-share-folder-with-team/SKILL.md) | Share a Google Drive folder and all its contents with a list of collaborators. | googleworkspace/cli | Apache-2.0 |
| [`recipe-sync-contacts-to-sheet`](../recipe-sync-contacts-to-sheet/SKILL.md) | Export Google Contacts directory to a Google Sheets spreadsheet. | googleworkspace/cli | Apache-2.0 |
| [`recipe-watch-drive-changes`](../recipe-watch-drive-changes/SKILL.md) | Subscribe to change notifications on a Google Drive file or folder. | googleworkspace/cli | Apache-2.0 |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
