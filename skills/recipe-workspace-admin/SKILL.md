---
name: recipe-workspace-admin
description: Workspace admin recipes — tasks, forms, classroom, contacts, personas. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "Workspace admin recipes — tasks, forms, classroom, contacts, personas"
  origin: "googleworkspace/cli"
  merged-from: "9 skills"
  category: "google-workspace"
---

# Workspace admin recipes — tasks, forms, classroom, contacts, personas

A merge of 9 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- Workspace admin recipes — tasks, forms, classroom, contacts, personas. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `recipe-block-focus-time` | Create recurring focus time blocks on Google Calendar to protect deep work hours. |
| `recipe-collect-form-responses` | Retrieve and review responses from a Google Form. |
| `recipe-create-classroom-course` | Create a Google Classroom course and invite students. |
| `recipe-create-expense-tracker` | Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries. |
| `recipe-create-feedback-form` | Create a Google Form for feedback and share it via Gmail. |
| `recipe-create-task-list` | Set up a new Google Tasks list with initial tasks. |
| `recipe-log-deal-update` | Append a deal status update to a Google Sheets sales tracking spreadsheet. |
| `recipe-review-overdue-tasks` | Find Google Tasks that are past due and need attention. |
| `recipe-send-team-announcement` | Send a team announcement via both Gmail and a Google Chat space. |

## recipe-block-focus-time

### Block Focus Time on Google Calendar

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Create recurring focus time blocks on Google Calendar to protect deep work hours.

#### Steps

1. Create recurring focus block: `gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Focus Time", "description": "Protected deep work block", "start": {"dateTime": "2025-01-20T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-20T11:00:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"], "transparency": "opaque"}'`
2. Verify it shows as busy: `gws calendar +agenda`

## recipe-collect-form-responses

### Check Form Responses

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`

Retrieve and review responses from a Google Form.

#### Steps

1. List forms: `gws forms forms list` (if you don't have the form ID)
2. Get form details: `gws forms forms get --params '{"formId": "FORM_ID"}'`
3. Get responses: `gws forms forms responses list --params '{"formId": "FORM_ID"}' --format table`

## recipe-create-classroom-course

### Create a Google Classroom Course

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-classroom`

Create a Google Classroom course and invite students.

#### Steps

1. Create the course: `gws classroom courses create --json '{"name": "Introduction to CS", "section": "Period 1", "room": "Room 101", "ownerId": "me"}'`
2. Invite a student: `gws classroom invitations create --json '{"courseId": "COURSE_ID", "userId": "student@school.edu", "role": "STUDENT"}'`
3. List enrolled students: `gws classroom courses students list --params '{"courseId": "COURSE_ID"}' --format table`

## recipe-create-expense-tracker

### Create a Google Sheets Expense Tracker

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries.

#### Steps

1. Create spreadsheet: `gws drive files create --json '{"name": "Expense Tracker 2025", "mimeType": "application/vnd.google-apps.spreadsheet"}'`
2. Add headers: `gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["Date", "Category", "Description", "Amount"]'`
3. Add first entry: `gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["2025-01-15", "Travel", "Flight to NYC", "450.00"]'`
4. Share with manager: `gws drive permissions create --params '{"fileId": "SHEET_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "manager@company.com"}'`

## recipe-create-feedback-form

### Create and Share a Google Form

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`, `gws-gmail`

Create a Google Form for feedback and share it via Gmail.

#### Steps

1. Create form: `gws forms forms create --json '{"info": {"title": "Event Feedback", "documentTitle": "Event Feedback Form"}}'`
2. Get the form URL from the response (responderUri field)
3. Email the form: `gws gmail +send --to attendees@company.com --subject 'Please share your feedback' --body 'Fill out the form: FORM_URL'`

## recipe-create-task-list

### Create a Task List and Add Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Set up a new Google Tasks list with initial tasks.

#### Steps

1. Create task list: `gws tasks tasklists insert --json '{"title": "Q2 Goals"}'`
2. Add a task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Review Q1 metrics", "notes": "Pull data from analytics dashboard", "due": "2024-04-01T00:00:00Z"}'`
3. Add another task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Draft Q2 OKRs"}'`
4. List tasks: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table`

## recipe-log-deal-update

### Log Deal Update to Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Append a deal status update to a Google Sheets sales tracking spreadsheet.

#### Steps

1. Find the tracking sheet: `gws drive files list --params '{"q": "name = '\''Sales Pipeline'\'' and mimeType = '\''application/vnd.google-apps.spreadsheet'\''"}'`
2. Read current data: `gws sheets +read --spreadsheet SHEET_ID --range "Pipeline!A1:F"`
3. Append new row: `gws sheets +append --spreadsheet SHEET_ID --range 'Pipeline' --values '["2024-03-15", "Acme Corp", "Proposal Sent", "$50,000", "Q2", "jdoe"]'`

## recipe-review-overdue-tasks

### Review Overdue Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Find Google Tasks that are past due and need attention.

#### Steps

1. List task lists: `gws tasks tasklists list --format table`
2. List tasks with status: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID", "showCompleted": false}' --format table`
3. Review due dates and prioritize overdue items

## recipe-send-team-announcement

### Announce via Gmail and Google Chat

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-chat`

Send a team announcement via both Gmail and a Google Chat space.

#### Steps

1. Send email: `gws gmail +send --to team@company.com --subject 'Important Update' --body 'Please review the attached policy changes.'`
2. Post in Chat: `gws chat +send --space spaces/TEAM_SPACE --text '📢 Important Update: Please check your email for policy changes.'`

## Provenance

Merged from 9 skills of [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`. Licence Apache-2.0 — the source text of every variant is preserved above.
