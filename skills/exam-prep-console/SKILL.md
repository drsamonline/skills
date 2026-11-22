---
name: exam-prep-console
description: Build an offline exam-preparation console: a 15-day guided plan over a fixed unit blueprint, a glossary, a question bank with rationales, a full-length NTA-style CBT simulator and unit diagnostics — one HTML file, zero network at runtime.
metadata:
  title: "NTET Homoeopathy"
---

# NTET Homoeopathy — an offline exam console with a question bank

A complete offline course for the NCH/NTA National Teachers' Eligibility Test (Homoeopathy):
15 guided days in plain English, a 112-term glossary, a 280-question bank with rationales, a full
100-question paper and unit diagnostics — one HTML file, no server, no sync, no telemetry.

## When to use

- A syllabus has a **fixed blueprint** (units and weights) and the study plan should be derived from it, not invented.
- Practice has to feel like the real paper: 100 questions, NTA-style navigation, a timer, a review screen.
- The learner may be offline for the whole course, so the app caches its shell once and runs with the network off.

## Method

1. Write the blueprint first — units, weights and the day-by-day plan — and let every screen read from it. A 15-day plan that contradicts the paper's weights teaches the wrong thing.
2. Keep the question bank as data with a **rationale per question**; a bank without rationales is a scoreboard, not a course.
3. Build the simulator to the real paper's shape: 100 questions, section navigation, marking, a review-before-submit screen.
4. Derive **unit diagnostics** from the same answers — where the learner lost marks, by unit — so the next session is planned rather than repeated.
5. Include a glossary of the terms the paper uses, in plain language.
6. Ship as one file with a PWA shell so the whole course is one cache entry.

## Key files / entry points

- The blueprint and the 15-day plan (the data every screen reads).
- The question bank with rationales.
- The CBT simulator and the diagnostics view.

## Gotchas

- A 280-question bank for a 100-question paper is thin if the plan drills the same units twice; balance by unit weight, not by count.
- A timer that keeps running when the tab is hidden punishes the wrong thing — pause on visibility change or say that it does not.
- Exam content is teaching material: a rationale that is wrong is worse than a missing question, so every addition needs review.

## Source projects

- [ntet-homoeopathy-cbt](https://github.com/drsamonline/ntet-homoeopathy-cbt)
