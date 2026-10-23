---
name: neo-nova-compiler
description: A statically-typed compiled systems language: a Rust compiler lowers NOVA through lexer, parser, semantic analyser, SIR and a lowerer to four backends (C, JavaScript, Rust, WebAssembly), with runtime, package manager, LSP and debugger.
metadata:
  title: "NEO — NOVA language and compiler"
---

# NEO — NOVA language and compiler

NOVA is a statically-typed, compiled systems programming language. Its Rust compiler lowers source through a semantic pipeline — lexer → parser → semantic analyser → SIR (Semantic Intermediate Representation) → lowerer — to four backends: C, JavaScript, Rust and WebAssembly. A runtime (memory/type/error/FFI), a package manager, a language server and a debugger ship alongside. Phases 1–3 are complete; Phase 4 is in progress.

## When to use

- You are adding a language feature and need to touch the whole pipeline consistently.
- You want a reference multi-backend compiler architecture with a shared IR.
- You need to understand the toolchain (package manager, LSP, debugger) around a language.

## Method

1. Front end: lexer → parser → semantic analyser produce an AST; a lowerer converts the AST to SIR (the shared IR every backend consumes).
2. Backends: emit C, JavaScript, Rust and WebAssembly from SIR — add a target by implementing the backend interface without touching the front end.
3. Runtime: memory management (arena allocation, GC foundation), a type registry with dynamic values, panic handling with backtraces, and C FFI.
4. Tooling: package manager (`pkg/`), language server, debugger and editor integration (`EDITOR_INTEGRATION.md`).
5. Track phases in `DEV_PLAN.md`; document architecture in `ARCHITECTURE.md` and `BACKEND_API.md`; run CI via `.github/workflows/ci.yml`.
6. Note: this repo's default branch is **`master`** (every other drsamonline repo uses `main`).

## Key files / entry points

- `compiler/` — lexer, parser, semantic analyser, SIR, lowerer.
- `backends/` — C, JavaScript, Rust, WebAssembly emitters.
- `runtime/`, `pkg/` — runtime and package manager.
- `DEV_PLAN.md`, `ARCHITECTURE.md`, `BACKEND_API.md`, `COMPATIBILITY.md`, `EDITOR_INTEGRATION.md`.

## Gotchas

- The default branch is `master`, not `main` — scripts and links must not assume `main`.
- Adding a backend must not require front-end changes; keep SIR the single contract.
- Be honest about phase status: pre-release, no live demo yet.
- Keep the four backends' test suites in sync or a language feature silently regresses on one target.

## Source projects

- [NEO](https://github.com/drsamonline/NEO) — Rust, NOVA language, `master` branch, v0.6.0.

