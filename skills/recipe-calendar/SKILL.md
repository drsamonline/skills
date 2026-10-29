---
name: recipe-calendar
description: Calendar and Meet recipes — events, free/busy, invites, conferences. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "Calendar and Meet recipes — events, free/busy, invites, conferences"
  origin: "googleworkspace/cli"
  merged-from: "9 skills"
  category: "google-workspace"
---

# Calendar and Meet recipes — events, free/busy, invites, conferences

A merge of 9 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- Calendar and Meet recipes — events, free/busy, invites, conferences. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `recipe-batch-invite-to-event` | Add a list of attendees to an existing Google Calendar event and send notifications. |
| `recipe-create-events-from-sheet` | Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row. |
| `recipe-create-meet-space` | Create a Google Meet meeting space and share the join link. |
| `recipe-find-free-time` | Query Google Calendar free/busy status for multiple users to find a meeting slot. |
| `recipe-plan-weekly-schedule` | Review your Google Calendar week, identify gaps, and add events to fill them. |
| `recipe-reschedule-meeting` | Move a Google Calendar event to a new time and automatically notify all attendees. |
| `recipe-review-meet-participants` | Review who attended a Google Meet conference and for how long. |
| `recipe-schedule-recurring-event` | Create a recurring Google Calendar event with attendees. |
| `recipe-share-event-materials` | Share Google Drive files with all attendees of a Google Calendar event. |

## recipe-batch-invite-to-event

### Add Multiple Attendees to a Calendar Event

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Add a list of attendees to an existing Google Calendar event and send notifications.

#### Steps

1. Get the event: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
2. Add attendees: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"attendees": [{"email": "alice@company.com"}, {"email": "bob@company.com"}, {"email": "carol@company.com"}]}'`
3. Verify attendees: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`

## recipe-create-events-from-sheet

### Create Google Calendar Events from a Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-calendar`

Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row.

#### Steps

1. Read event data: `gws sheets +read --spreadsheet SHEET_ID --range "Events!A2:D"`
2. For each row, create a calendar event: `gws calendar +insert --summary 'Team Standup' --start '2026-01-20T09:00:00' --end '2026-01-20T09:30:00' --attendee alice@company.com --attendee bob@company.com`

## recipe-create-meet-space

### Create a Google Meet Conference

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-meet`, `gws-gmail`

Create a Google Meet meeting space and share the join link.

#### Steps

1. Create meeting space: `gws meet spaces create --json '{"config": {"accessType": "OPEN"}}'`
2. Copy the meeting URI from the response
3. Email the link: `gws gmail +send --to team@company.com --subject 'Join the meeting' --body 'Join here: MEETING_URI'`

## recipe-find-free-time

### Find Free Time Across Calendars

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Query Google Calendar free/busy status for multiple users to find a meeting slot.

#### Steps

1. Query free/busy: `gws calendar freebusy query --json '{"timeMin": "2024-03-18T08:00:00Z", "timeMax": "2024-03-18T18:00:00Z", "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]}'`
2. Review the output to find overlapping free slots
3. Create event in the free slot: `gws calendar +insert --summary 'Meeting' --attendee user1@company.com --attendee user2@company.com --start '2024-03-18T14:00:00' --end '2024-03-18T14:30:00'`

## recipe-plan-weekly-schedule

### Plan Your Weekly Google Calendar Schedule

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Review your Google Calendar week, identify gaps, and add events to fill them.

#### Steps

1. Check this week's agenda: `gws calendar +agenda`
2. Check free/busy for the week: `gws calendar freebusy query --json '{"timeMin": "2025-01-20T00:00:00Z", "timeMax": "2025-01-25T00:00:00Z", "items": [{"id": "primary"}]}'`
3. Add a new event: `gws calendar +insert --summary 'Deep Work Block' --start '2026-01-21T14:00:00' --end '2026-01-21T16:00:00'`
4. Review updated schedule: `gws calendar +agenda`

## recipe-reschedule-meeting

### Reschedule a Google Calendar Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Move a Google Calendar event to a new time and automatically notify all attendees.

#### Steps

1. Find the event: `gws calendar +agenda`
2. Get event details: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
3. Update the time: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"start": {"dateTime": "2025-01-22T14:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-22T15:00:00", "timeZone": "America/New_York"}}'`

## recipe-review-meet-participants

### Review Google Meet Attendance

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-meet`

Review who attended a Google Meet conference and for how long.

#### Steps

1. List recent conferences: `gws meet conferenceRecords list --format table`
2. List participants: `gws meet conferenceRecords participants list --params '{"parent": "conferenceRecords/CONFERENCE_ID"}' --format table`
3. Get session details: `gws meet conferenceRecords participants participantSessions list --params '{"parent": "conferenceRecords/CONFERENCE_ID/participants/PARTICIPANT_ID"}' --format table`

## recipe-schedule-recurring-event

### Schedule a Recurring Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Create a recurring Google Calendar event with attendees.

#### Steps

1. Create recurring event: `gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Weekly Standup", "start": {"dateTime": "2024-03-18T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2024-03-18T09:30:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO"], "attendees": [{"email": "team@company.com"}]}'`
2. Verify it was created: `gws calendar +agenda --days 14 --format table`

## recipe-share-event-materials

### Share Files with Meeting Attendees

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`, `gws-drive`

Share Google Drive files with all attendees of a Google Calendar event.

#### Steps

1. Get event attendees: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
2. Share file with each attendee: `gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "attendee@company.com"}'`
3. Verify sharing: `gws drive permissions list --params '{"fileId": "FILE_ID"}' --format table`

## Provenance

Merged from 9 skills of [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`. Licence Apache-2.0 — the source text of every variant is preserved above.
