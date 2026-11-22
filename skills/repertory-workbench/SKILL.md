---
name: repertory-workbench
description: Build an offline homeopathic repertory workbench: a symptom picker beside a ranked remedy list, 178 remedies and 634 symptoms with 30,412 graded links, mobile-first sheets and bottom tabs — single-file HTML, PWA, no account, no tracking.
metadata:
  title: "Remedy Finder"
---

# Remedy Finder — a repertory workbench, not a search box

An offline homeopathic repertory workbench — not another symptom search box. Symptom picker on the
left, ranked remedies on the right; 178 remedies, 634 symptoms and 30,412 graded links from
Repertorium Publicum (2008), in a single-file HTML app with a PWA shell.

## When to use

- The work is **repertorisation**: several symptoms chosen together, remedies ranked by the grades they hold across all of them.
- The user is at a desk on a laptop and at a bedside on a phone — the layout has to serve both.
- The data is large for a static app (30k graded links) and must load without a server.

## Method

1. Model the data as remedies × symptoms with a **grade per link**, and nothing else; the whole app is a view over that matrix.
2. Rank by summed grade across the *selected* symptoms, and show which symptoms each remedy scored on — a ranking without its evidence is a black box.
3. Two layouts, one codebase: picker beside ranking on desktop, bottom tabs and sheets on mobile.
4. Keep the provenance on screen: the repertory edition the links come from belongs in the app, not only in the README.
5. Ship as one file with a PWA shell so the matrix loads once and works offline.

## Key files / entry points

- The graded links dataset (remedies × symptoms × grade).
- The ranking function.
- The desktop split view and the mobile tab/sheet views.

## Gotchas

- Grade scales differ between repertories; mixing two books' grades without normalising invents a ranking.
- A picker that only offers symptoms by exact name hides the near-synonyms that matter in repertory work — group them.
- This is a study and reference tool: the app should say what it is not (a prescription), in the app.

## Source projects

- [remedy-finder](https://github.com/drsamonline/remedy-finder)
