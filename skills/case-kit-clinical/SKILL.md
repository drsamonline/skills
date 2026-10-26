---
name: case-kit-clinical
description: Clinical case tracking in one zero-dependency file: sections, dated symptoms with severity, follow-ups with remedy and response, a timeline, a summary and a plain-JSON interchange record.
metadata:
  title: "Clinical case tracking"
---

# Clinical case tracking

`Case` is the record shape behind the case-taking apps: a case has sections, dated
symptoms and follow-ups, and can print a timeline and a summary. One file, zero
dependencies.

## When to use

- An app records a patient's case over time and needs a structure that survives
  a follow-up visit.
- You want a symptom log with severity that can be charted later.
- You need an interchange format so a case can move between two of our apps.

## Method

1. `var c = Case.create({ title: "Skin case 12" });`
2. Fill the classical sections: `Case.section(c, "history", text)`, then
   `"habits"`, `"mapping"` — the same three the HHMS model uses.
3. Log dated symptoms: `Case.addSymptom(c, { note: "...", severity: 3 })`. The
   severity is what the summary averages and what a chart plots.
4. Record follow-ups with `{ date, note, remedy, potency, response }` — the
   response field is what makes a follow-up useful a year later.
5. Read `Case.timeline(c)` and `Case.summary(c)` for the visit view, and
   `Case.toJSON` / the plain-JSON interchange record (`patient` + `version` +
   `cases`) to move a case between apps.
6. Encrypt the export with `crypto-kit` when it leaves the device.

## Key files

- `case-kit.js` — `create`, `section`, symptoms, follow-ups, timeline, summary,
  interchange record.
- `test-node.js` — the record behaviour and the summary arithmetic.

## Gotchas

- The kit deliberately models **no patient identifiers**. The app owns the name,
  the phone number and the address, and keeps them local — that is the design,
  not an omission.
- `severity` is per symptom and averaged for the summary; it is not a diagnosis
  and the apps must not present it as one.
- `HMS` keeps its case records in SQLite on the LAN server (`case_record` model),
  so its store and this record are not the same thing. A bridge is an explicit
  export/import, never a shared file.
- `skin-case-tracker` tracks exactly this shape but does not vendor the kit, so
  its JSON is its own dialect.
- Section names are free-form strings; a typo silently creates a new section
  rather than failing.

## Source projects

- [case-kit](https://github.com/drsamonline/case-kit) — the record.
- [skin-case-tracker](https://github.com/drsamonline/skin-case-tracker) — a 90-day pattern engine on the HHMS model.
- [app-encrypted-case-log](https://github.com/drsamonline/app-encrypted-case-log) — the one app that already vendors the kit, with AES-256-GCM at rest.
- [HMS](https://github.com/drsamonline/HMS) — the hospital system whose case model the sections follow.
