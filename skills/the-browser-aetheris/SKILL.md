---
name: The_Browser — Aetheris experimental browser
description: An experimental C++20 browser engine derived from Ladybird/SerenityOS, built with CMake + vcpkg and tested with CTest; explicitly not production-ready and honest about provenance.
---

# The_Browser — Aetheris experimental browser

Aetheris Browser is an experimental C++ browser engine with a dependency-free rendering foundation, built on a Ladybird/SerenityOS-derived codebase. It is explicitly **not production-ready** and documents its upstream provenance. It uses CMake + vcpkg, CTest for tests, clang-format/clang-tidy/clangd config, and devcontainers for reproducible builds.

## When to use

- You are studying a real C++ browser-engine codebase and its build system.
- You need a reproducible C++ build via devcontainers + vcpkg.
- You want a template for an experimental project that states its limitations honestly.

## Method

1. Build with CMake + vcpkg; keep `.clang-format`, `.clang-tidy` and `.clangd` for consistent tooling.
2. Use devcontainers (`.devcontainer/`) with per-distro install scripts and a vcpkg cache feature so a contributor gets a working toolchain in one step.
3. Test with CTest (the Aetheris suite); document the rendering pipeline and architecture in `docs/ARCHITECTURE.md` and `docs/USER_GUIDE.md`.
4. State provenance and status up front: derived from Ladybird/SerenityOS, experimental, not production-ready.
5. Ship a landing page in `docs/` with an interactive rendering-pipeline walkthrough.

## Key files / entry points

- `CMakeLists.txt` + vcpkg manifest; `.clang-format`, `.clang-tidy`, `.clangd`.
- `.devcontainer/` (features for ladybird toolchain + vcpkg cache).
- `docs/ARCHITECTURE.md`, `docs/USER_GUIDE.md`, `docs/index.html`.

## Gotchas

- Do not imply production readiness; the project is experimental and says so.
- Keep the upstream (Ladybird/SerenityOS) attribution visible.
- A C++ engine build is heavy — the devcontainer + vcpkg cache is what makes it reproducible.
- Landing-page links should point at the rendering-pipeline walkthrough, not promise a downloadable browser build unless one exists.

## Source projects

- [The_Browser](https://github.com/drsamonline/The_Browser) — C++20, CMake + vcpkg, experimental.

