---
name: pack-backend-services
description: Server-side work: Node.js and TypeScript practice, Fastify REST APIs, OAuth 2.0/2.1 flows, advanced type design, API and module boundaries, and building MCP servers or calling the Claude API. Use when writing, hardening or extending a backend service.
license: see each member
metadata:
  title: "Backend and services pack"
  kind: "index pack"
  members: "15"
---

# Backend and services pack

15 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 7 upstream repositories.

## When to use

- A Node.js service, REST API or Fastify route needs writing, reviewing or debugging.
- OAuth or another auth flow has to be implemented correctly.
- API and module boundaries need designing before the code is written.
- You are building an MCP server or wiring a model API into a service.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`360-feedback-system`](../360-feedback-system/SKILL.md) | 360 feedback register: reviewer, subject, review cycle, visibility, due date and score, as CSV, SQL, JSON Schema or Notion on request. Use for 360 reviews or peer feedback cycles. | sickn33/agentic-awesome-skills | MIT |
| [`accounting-software-selection`](../accounting-software-selection/SKILL.md) | Scores shortlisted accounting packages against 57 evidence-backed fields, emitted as CSV, SQL, JSON Schema or Notion on request. Use for choosing accounting software. | sickn33/agentic-awesome-skills | MIT |
| [`api-and-interface-design`](../api-and-interface-design/SKILL.md) | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type… | addyosmani/agent-skills | MIT |
| [`claude-api`](../claude-api/SKILL.md) | This skill helps you build LLM-powered applications with Claude. Choose the right surface based on your needs, detect the project language, then read the relevant… | anthropics/skills | Apache-2.0 |
| [`fastify-best-practices`](../fastify-best-practices/SKILL.md) | Guides development of Fastify Node.js backend servers and REST APIs using TypeScript or JavaScript. Use when building, configuring, or debugging a Fastify application —… | mcollina/skills | MIT |
| [`fullstack-dev`](../fullstack-dev/SKILL.md) | When this skill is triggered, you MUST follow this workflow before writing any code. | MiniMax-AI/skills | MIT |
| [`hunt-graphql`](../hunt-graphql/SKILL.md) | Hunting skill for graphql vulnerabilities. | sickn33/agentic-awesome-skills | MIT |
| [`mcp-builder`](../mcp-builder/SKILL.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP… | anthropics/skills | Apache-2.0 |
| [`node`](../node/SKILL.md) | Provides domain-specific best practices for Node.js development with TypeScript, covering type stripping, async patterns, error handling, streams, modules, testing,… | mcollina/skills | MIT |
| [`nodejs-core`](../nodejs-core/SKILL.md) | Contributes to and debugs Node.js core, including nodejs/node commit and PR tone, contribution workflows, native crashes, V8 performance, node-gyp builds, N-API bindings, and… | mcollina/skills | MIT |
| [`oauth`](../oauth/SKILL.md) | Implements OAuth 2.0/2.1 authorization flows in Fastify applications — configures authorization code with PKCE, client credentials, device flow, refresh token rotation, JWT… | mcollina/skills | MIT |
| [`rails-conventions`](../rails-conventions/SKILL.md) | Modern Ruby and Rails application architecture, implementation, and review guidance for production codebases. Use when building or reviewing Ruby on Rails 8 features across… | ethos-link/rails-conventions | MIT |
| [`snipgrapher`](../snipgrapher/SKILL.md) | Configures and uses snipgrapher to generate polished code snippet images, including syntax-highlighted PNGs, SVGs, and WebP exports with custom themes, profiles, and styling… | mcollina/skills | MIT |
| [`tinystruct-patterns`](../tinystruct-patterns/SKILL.md) | Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct codebase or any project built on tinystruct — including generating the… | affaan-m/ECC | MIT |
| [`typescript-magician`](../typescript-magician/SKILL.md) | Designs complex generic types, refactors `any` types to strict alternatives, creates type guards and utility types, and resolves TypeScript compiler errors. Use when the user… | mcollina/skills | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0, MIT). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
