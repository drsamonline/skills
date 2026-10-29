---
name: recipe-gmail
description: Gmail recipes — label, forward, archive, draft, auto-reply. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "Gmail recipes — label, forward, archive, draft, auto-reply"
  origin: "googleworkspace/cli"
  merged-from: "8 skills"
  category: "google-workspace"
---

# Gmail recipes — label, forward, archive, draft, auto-reply

A merge of 8 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- Gmail recipes — label, forward, archive, draft, auto-reply. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `recipe-create-gmail-filter` | Create a Gmail filter to automatically label, star, or categorize incoming messages. |
| `recipe-create-vacation-responder` | Enable a Gmail out-of-office auto-reply with a custom message and date range. |
| `recipe-draft-email-from-doc` | Read content from a Google Doc and use it as the body of a Gmail message. |
| `recipe-email-drive-link` | Share a Google Drive file and email the link with a message to recipients. |
| `recipe-forward-labeled-emails` | Find Gmail messages with a specific label and forward them to another address. |
| `recipe-label-and-archive-emails` | Apply Gmail labels to matching messages and archive them to keep your inbox clean. |
| `recipe-save-email-attachments` | Find Gmail messages with attachments and save them to a Google Drive folder. |
| `recipe-save-email-to-doc` | Save a Gmail message body into a Google Doc for archival or reference. |

## recipe-create-gmail-filter

### Create a Gmail Filter

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Create a Gmail filter to automatically label, star, or categorize incoming messages.

#### Steps

1. List existing labels: `gws gmail users labels list --params '{"userId": "me"}' --format table`
2. Create a new label: `gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Receipts"}'`
3. Create a filter: `gws gmail users settings filters create --params '{"userId": "me"}' --json '{"criteria": {"from": "receipts@example.com"}, "action": {"addLabelIds": ["LABEL_ID"], "removeLabelIds": ["INBOX"]}}'`
4. Verify filter: `gws gmail users settings filters list --params '{"userId": "me"}' --format table`

## recipe-create-vacation-responder

### Set Up a Gmail Vacation Responder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Enable a Gmail out-of-office auto-reply with a custom message and date range.

#### Steps

1. Enable vacation responder: `gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": true, "responseSubject": "Out of Office", "responseBodyPlainText": "I am out of the office until Jan 20. For urgent matters, contact backup@company.com.", "restrictToContacts": false, "restrictToDomain": false}'`
2. Verify settings: `gws gmail users settings getVacation --params '{"userId": "me"}'`
3. Disable when back: `gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": false}'`

## recipe-draft-email-from-doc

### Draft a Gmail Message from a Google Doc

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-gmail`

Read content from a Google Doc and use it as the body of a Gmail message.

#### Steps

1. Get the document content: `gws docs documents get --params '{"documentId": "DOC_ID"}'`
2. Copy the text from the body content
3. Send the email: `gws gmail +send --to recipient@example.com --subject 'Newsletter Update' --body 'CONTENT_FROM_DOC'`

## recipe-email-drive-link

### Email a Google Drive File Link

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-gmail`

Share a Google Drive file and email the link with a message to recipients.

#### Steps

1. Find the file: `gws drive files list --params '{"q": "name = '\''Quarterly Report'\''"}'`
2. Share the file: `gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "client@example.com"}'`
3. Email the link: `gws gmail +send --to client@example.com --subject 'Quarterly Report' --body 'Hi, please find the report here: https://docs.google.com/document/d/FILE_ID'`

## recipe-forward-labeled-emails

### Forward Labeled Gmail Messages

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Find Gmail messages with a specific label and forward them to another address.

#### Steps

1. Find labeled messages: `gws gmail users messages list --params '{"userId": "me", "q": "label:needs-review"}' --format table`
2. Get message content: `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'`
3. Forward via new email: `gws gmail +send --to manager@company.com --subject 'FW: [Original Subject]' --body 'Forwarding for your review:

[Original Message Body]'`

## recipe-label-and-archive-emails

### Label and Archive Gmail Threads

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Apply Gmail labels to matching messages and archive them to keep your inbox clean.

#### Steps

1. Search for matching emails: `gws gmail users messages list --params '{"userId": "me", "q": "from:notifications@service.com"}' --format table`
2. Apply a label: `gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"addLabelIds": ["LABEL_ID"]}'`
3. Archive (remove from inbox): `gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"removeLabelIds": ["INBOX"]}'`

## recipe-save-email-attachments

### Save Gmail Attachments to Google Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-drive`

Find Gmail messages with attachments and save them to a Google Drive folder.

#### Steps

1. Search for emails with attachments: `gws gmail users messages list --params '{"userId": "me", "q": "has:attachment from:client@example.com"}' --format table`
2. Get message details: `gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'`
3. Download attachment: `gws gmail users messages attachments get --params '{"userId": "me", "messageId": "MESSAGE_ID", "id": "ATTACHMENT_ID"}'`
4. Upload to Drive folder: `gws drive +upload --file ./attachment.pdf --parent FOLDER_ID`

## recipe-save-email-to-doc

### Save a Gmail Message to Google Docs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-docs`

Save a Gmail message body into a Google Doc for archival or reference.

#### Steps

1. Find the message: `gws gmail users messages list --params '{"userId": "me", "q": "subject:important from:boss@company.com"}' --format table`
2. Get message content: `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'`
3. Create a doc with the content: `gws docs documents create --json '{"title": "Saved Email - Important Update"}'`
4. Write the email body: `gws docs +write --document-id DOC_ID --text 'From: boss@company.com
Subject: Important Update

[EMAIL BODY]'`

## Provenance

Merged from 8 skills of [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`. Licence Apache-2.0 — the source text of every variant is preserved above.
