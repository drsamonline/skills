---
name: decision-first-notes
description: Store decisions rather than notes: an atomic DR-NNNN record with a lifecycle and a supersession chain, notes that serve as evidence for it, procedures that emerged from repetition, and tasks derived from decisions — so the office can answer why, not just what.
metadata:
  title: "DayDoc"
---

# DayDoc — decision-first office notes

Every notes app stores notes. DayDoc stores **decisions** — and treats notes as the evidence for
them. A note is one of four things: a Decision (an atomic `DR-NNNN` with a lifecycle and a
supersession chain), Evidence (a note that supports, cites or contradicts a decision), a Procedure
(an SOP that emerged from the same steps written down repeatedly), or a Task derived from a decision
or a meeting.

## When to use

- The question people actually ask is "why is it like this?", and the answer is scattered across meeting notes.
- A decision gets reversed and nobody knows which note is current.
- The office needs SOPs that came from practice rather than from a template.

## Method

1. Make the decision the **atomic object**: an id (`DR-NNNN`), a state, an owner, a date, and the decision in one sentence.
2. Model **supersession** explicitly: a new decision points at the one it replaces, and the old one is marked superseded, never deleted.
3. Attach evidence: every note that supports, cites or contradicts a decision links to it. A note with no decision is allowed, but it is not the record.
4. Promote repetition into a **procedure**: when the same steps appear three times, they become an SOP linked to the decisions that produced them.
5. Derive tasks from decisions and meetings, and keep them linked to their source so a reversed decision can find its tasks.

## Key files / entry points

- The decision record (id, lifecycle, supersession chain).
- The evidence links from notes to decisions.
- The procedure (SOP) view.

## Gotchas

- Without a lifecycle, "decided" and "done" collapse into one state and the supersession chain becomes unreadable.
- Evidence that only supports is a filter bubble: the contradiction is the most valuable note in the file.
- Deleting a superseded decision breaks every reference to it — supersede, never delete.

## Source projects

- [DayDoc](https://github.com/drsamonline/DayDoc)
