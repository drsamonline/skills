---
name: recipe-drive
description: Drive recipes — folders, sharing, bulk download, change watches. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "Drive recipes — folders, sharing, bulk download, change watches"
  origin: "googleworkspace/cli"
  merged-from: "6 skills"
  category: "google-workspace"
---

# Drive recipes — folders, sharing, bulk download, change watches

A merge of 6 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- Drive recipes — folders, sharing, bulk download, change watches. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `recipe-bulk-download-folder` | List and download all files from a Google Drive folder. |
| `recipe-create-shared-drive` | Create a Google Shared Drive and add members with appropriate roles. |
| `recipe-find-large-files` | Identify large Google Drive files consuming storage quota. |
| `recipe-organize-drive-folder` | Create a Google Drive folder structure and move files into the right locations. |
| `recipe-share-folder-with-team` | Share a Google Drive folder and all its contents with a list of collaborators. |
| `recipe-watch-drive-changes` | Subscribe to change notifications on a Google Drive file or folder. |

## recipe-bulk-download-folder

### Bulk Download Drive Folder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

List and download all files from a Google Drive folder.

#### Steps

1. List files in folder: `gws drive files list --params '{"q": "'\''FOLDER_ID'\'' in parents"}' --format json`
2. Download each file: `gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' -o filename.ext`
3. Export Google Docs as PDF: `gws drive files export --params '{"fileId": "FILE_ID", "mimeType": "application/pdf"}' -o document.pdf`

## recipe-create-shared-drive

### Create and Configure a Shared Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Create a Google Shared Drive and add members with appropriate roles.

#### Steps

1. Create shared drive: `gws drive drives create --params '{"requestId": "unique-id-123"}' --json '{"name": "Project X"}'`
2. Add a member: `gws drive permissions create --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}' --json '{"role": "writer", "type": "user", "emailAddress": "member@company.com"}'`
3. List members: `gws drive permissions list --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}'`

## recipe-find-large-files

### Find Largest Files in Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Identify large Google Drive files consuming storage quota.

#### Steps

1. List files sorted by size: `gws drive files list --params '{"orderBy": "quotaBytesUsed desc", "pageSize": 20, "fields": "files(id,name,size,mimeType,owners)"}' --format table`
2. Review the output and identify files to archive or move

## recipe-organize-drive-folder

### Organize Files into Google Drive Folders

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Create a Google Drive folder structure and move files into the right locations.

#### Steps

1. Create a project folder: `gws drive files create --json '{"name": "Q2 Project", "mimeType": "application/vnd.google-apps.folder"}'`
2. Create sub-folders: `gws drive files create --json '{"name": "Documents", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_FOLDER_ID"]}'`
3. Move existing files into folder: `gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'`
4. Verify structure: `gws drive files list --params '{"q": "FOLDER_ID in parents"}' --format table`

## recipe-share-folder-with-team

### Share a Google Drive Folder with a Team

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Share a Google Drive folder and all its contents with a list of collaborators.

#### Steps

1. Find the folder: `gws drive files list --params '{"q": "name = '\''Project X'\'' and mimeType = '\''application/vnd.google-apps.folder'\''"}'`
2. Share as editor: `gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "colleague@company.com"}'`
3. Share as viewer: `gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "stakeholder@company.com"}'`
4. Verify permissions: `gws drive permissions list --params '{"fileId": "FOLDER_ID"}' --format table`

## recipe-watch-drive-changes

### Watch for Drive Changes

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-events`

Subscribe to change notifications on a Google Drive file or folder.

#### Steps

1. Create subscription: `gws events subscriptions create --json '{"targetResource": "//drive.googleapis.com/drives/DRIVE_ID", "eventTypes": ["google.workspace.drive.file.v1.updated"], "notificationEndpoint": {"pubsubTopic": "projects/PROJECT/topics/TOPIC"}, "payloadOptions": {"includeResource": true}}'`
2. List active subscriptions: `gws events subscriptions list`
3. Renew before expiry: `gws events +renew --subscription SUBSCRIPTION_ID`

## Provenance

Merged from 6 skills of [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`. Licence Apache-2.0 — the source text of every variant is preserved above.
