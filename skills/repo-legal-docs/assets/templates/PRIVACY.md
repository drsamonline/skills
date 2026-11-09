# Privacy

Version: 1.0
Effective: {{DATE}}
Owner: {{NAME}}, {{CONTACT}}
Changes: Initial version.

<!-- Pick ONE opening that is true. Delete the others. The claim must match
     the audit output for network_call and on_device_storage. -->

## What this app collects

**Nothing.** {{APP_NAME}} has no server, no account and no analytics. It makes no network request at all — you can verify that in your browser's network panel or with a packet capture; an empty list is the expected result.

<!-- OR, for an app with a third-party call: -->
<!-- {{APP_NAME}} sends {{WHAT}} to {{PROVIDER CATEGORY, e.g. "the AI provider you configure"}}. Nothing else leaves your device. We do not receive, store or see that data. -->

## What is stored on your device

{{List each thing stored, the storage mechanism, and the key prefix. Example: notes and checklists are written to this browser's `localStorage` under the `{{prefix}}:` prefix.}}

None of it leaves the device. Clearing your browser or app data erases it. {{Name the export/erase control if one exists.}}

## Files you open

Files you {{open/convert/edit}} are read by the app on your device and written back as a plain download. They are never transmitted.

## Links that leave the app

{{Name the one screen with outbound links, or state there are none.}} Following an outbound link takes you to a service with its own privacy policy.

## Your rights

<!-- Keep only if the DPDP Act 2023 applies: the app processes digital
     personal data of individuals in India. For an app that collects nothing,
     say so plainly instead. -->

Under the Digital Personal Data Protection Act, 2023 you may request access to, correction of, or erasure of your personal data, and you may withdraw consent at any time. Write to {{GRIEVANCE EMAIL}}. We respond within {{N}} days. If you are not satisfied, you may complain to the Data Protection Board of India.

## Changes

If a future version adds a network call, this document and the CI check that forbids one change in the same commit.

Contact: {{EMAIL}}
