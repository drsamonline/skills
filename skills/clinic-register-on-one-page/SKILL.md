---
name: clinic-register-on-one-page
description: Build a daily outpatient register that lays out the whole month ready to type into, updates counts and department splits as you write, prints for the file, exports to Excel, and keeps several centres apart — offline with no network request at all.
metadata:
  title: "OPD Register"
---

# OPD Register — the clinic day, at typing speed

The daily OPD register on one page, at typing speed. Every day of the month is laid out and ready
to type into; counts, department splits and the daily trend update as you write; the register
prints for the file, exports a day-wise sheet to Excel, and several OPD centres stay apart in the
same app. Nothing leaves the device, and the page makes no network request at all.

## When to use

- A paper register is being replaced and the staff already know how to use paper: the layout is the interface.
- The month is the unit of work, not the day — a grid you can type across beats a form per entry.
- The output has to satisfy two audiences: a printed page for the file, a spreadsheet for the statistics.

## Method

1. Render the **whole month** as a grid, one cell per patient slot, and let typing move through it — no "add entry" dialog.
2. Derive every statistic (daily count, department split, trend) from the same cells as you type; never keep a second tally that can drift.
3. Keep several centres as separate namespaces, so switching a centre does not mix its register with another's.
4. Print with a real print stylesheet — the file copy is the legal artifact, and a screenshot is not.
5. Export a day-wise sheet to Excel (CSV) from the same data the grid holds.
6. Test the arithmetic (counts, splits, month boundaries) rather than the pixels.

## Key files / entry points

- The month grid (the primary interface).
- The statistics derived from it.
- The print stylesheet and the Excel export.

## Gotchas

- Month boundaries: the 31st has no counterpart in the next month, and a register that silently drops a day loses patients.
- A second tally kept for the dashboard is the classic drift — derive, do not accumulate.
- Printing from a scrolling grid cuts columns; the print layout has to be designed, not inherited.

## Source projects

- [app-opd-register](https://github.com/drsamonline/app-opd-register)
