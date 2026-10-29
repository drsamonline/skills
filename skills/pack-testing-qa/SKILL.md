---
name: pack-testing-qa
description: Test work in one place: Playwright patterns for E2E, component and API tests, page objects, CI wiring and Cypress/Selenium migration, browser testing through DevTools, test-first development, and the discipline of verifying before you claim something works.
license: see each member
metadata:
  title: "Testing and QA pack"
  kind: "index pack"
  members: "13"
---

# Testing and QA pack

13 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 5 upstream repositories (addyosmani/agent-skills, anthropics/skills, mattpocock/skills, obra/superpowers, testdino-hq/playwright-skill).

## When to use

- Writing, debugging or stabilising a Playwright suite.
- Deciding test structure — page objects, fixtures, component vs E2E.
- Moving a suite off Cypress or Selenium.
- About to claim work is done and needing the verification gate.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`browser-testing-with-devtools`](../browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors,… | addyosmani/agent-skills | MIT |
| [`playwright-ci`](../playwright-ci/SKILL.md) | Production-ready CI/CD configurations for Playwright — GitHub Actions, GitLab CI, CircleCI, Azure DevOps, Jenkins, Docker, parallel sharding, reporting, code coverage, and… | testdino-hq/playwright-skill | MIT |
| [`playwright-cli`](../playwright-cli/SKILL.md) | Automates browser interactions for testing and validating your own web applications using playwright-cli. Use when you need terminal-first browser control for navigation, form… | testdino-hq/playwright-skill | MIT |
| [`playwright-core`](../playwright-core/SKILL.md) | Battle-tested Playwright patterns for writing and debugging reliable E2E, API, component, visual, accessibility, and security tests. Use when you need locator strategy,… | testdino-hq/playwright-skill | MIT |
| [`playwright-frontend`](../playwright-frontend/SKILL.md) | For frontend engineers authoring UI — how to make components reliably locatable by tests and AI agents. Covers the official Playwright locator priority, semantic/accessible… | testdino-hq/playwright-skill | MIT |
| [`playwright-migration`](../playwright-migration/SKILL.md) | Step-by-step migration guides for moving to Playwright from Cypress or Selenium/WebDriver — command mappings, architecture changes, and incremental adoption strategies. | testdino-hq/playwright-skill | MIT |
| [`playwright-pom`](../playwright-pom/SKILL.md) | Page Object Model patterns for Playwright — when to use POM, how to structure page objects, and when fixtures or helpers are a better fit. | testdino-hq/playwright-skill | MIT |
| [`playwright-qa`](../playwright-qa/SKILL.md) | QA engineering workflows on top of Playwright. Use when a QA engineer asks to design test cases from a ticket, PRD or acceptance criteria, decide what to automate, write a bug… | testdino-hq/playwright-skill | MIT |
| [`playwright-skill`](../playwright-skill/SKILL.md) | Current Playwright (1.64) patterns for writing, debugging, and scaling reliable test suites. Use for any Playwright task, even ones you think you know, because the guides cover… | testdino-hq/playwright-skill | MIT |
| [`tdd`](../tdd/SKILL.md) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | mattpocock/skills | MIT |
| [`test-driven-development`](../test-driven-development/SKILL.md) | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code… | addyosmani/agent-skills | MIT |
| [`verification-before-completion`](../verification-before-completion/SKILL.md) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any… | obra/superpowers | MIT |
| [`webapp-testing`](../webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser… | anthropics/skills | Apache-2.0 |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0, MIT). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
