---
name: recipe-create-classroom-course
description: Create a Google Classroom course and invite students.
license: Apache-2.0
metadata:
  title: "recipe create classroom course"
  origin: "googleworkspace/cli"
  upstream-path: "skills/recipe-create-classroom-course/SKILL.md"
  upstream-commit: "a3768d0e82ad83cca2da97724e46bea4ff0e6dbd"
  category: "google-workspace"
---

# Create a Google Classroom Course

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-classroom`

Create a Google Classroom course and invite students.

## Steps

1. Create the course: `gws classroom courses create --json '{"name": "Introduction to CS", "section": "Period 1", "room": "Room 101", "ownerId": "me"}'`
2. Invite a student: `gws classroom invitations create --json '{"courseId": "COURSE_ID", "userId": "student@school.edu", "role": "STUDENT"}'`
3. List enrolled students: `gws classroom courses students list --params '{"courseId": "COURSE_ID"}' --format table`

## Provenance

Imported from [googleworkspace/cli](https://github.com/googleworkspace/cli) at commit `a3768d0`, path `skills/recipe-create-classroom-course/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
