---
name: neo-nova-compiler
description: A statically-typed compiled systems language (NOVA) whose Rust compiler lowers through one semantic IR to four backends — C, JavaScript, Rust and WebAssembly. Use when adding a language feature that must touch the whole pipeline, when changing the type system, or when you need a reference multi-backend compiler with real gates around it.
metadata:
  title: "NEO — NOVA language and compiler"
  version: "1.2.0"
---

# NEO — NOVA language and compiler

NOVA is a statically-typed, compiled systems language. Its Rust compiler lowers source
through lexer → parser → semantic analyser → SIR (Semantic Intermediate Representation) →
lowerer → one of four backends: C (the reference), JavaScript, Rust and WebAssembly. A
runtime, package manager, language server and debugger ship alongside.

<!-- status:begin -->
| | |
|---|---|
| Version | `0.7.0` |
| Rust | 13,445 lines in `compiler/src`, 31,306 across the workspace |
| ADRs | 14 |
| Gates (no toolchain) | `diagnostic`, `docs`, `error-code`, `example`, `extension`, `grammar`, `stdlib`, `type-name` |
| Standard library | 4 modules, 0 listed as not compiling |
<!-- status:end -->

That block is generated from [`docs/status.json`](https://github.com/drsamonline/NEO/blob/master/docs/status.json)
by `scripts/refresh_status.py` — do not edit it by hand. Test counts and coverage are **not**
in it: they move on every commit and would drift, so they live in `docs/HANDOVER.md`.

**Read `docs/HANDOVER.md` first, every session.** It is the authoritative state document:
what is done, what is next in order, and the gotchas that will each cost a CI cycle. It is
kept current deliberately — a stale handover is treated as a defect.

## When to use

- Adding a language feature and needing to touch every stage consistently.
- Changing anything in the type system — the highest-risk area in this repository.
- Wanting a reference architecture for one IR feeding several backends.
- Working on the standard library or the gates around it.

## Method

1. **Read `docs/HANDOVER.md` and `DEV_PLAN.md` before starting.** Do not begin from a
   task description alone; the handover records what was already tried.
2. **Front end**: lexer → parser → semantic analyser produce an AST; the lowerer converts
   the AST to SIR, which every backend consumes. Adding a backend must not require
   front-end changes.
3. **Ratchet files are load-bearing, and each has a format.**
   - `coverage-floor.txt` — may only go up, unless a change genuinely lowers it, in which
     case lower it **in the same commit** and say why. It has a 0.05% tolerance that hides
     about six lines, so a small fall passes silently; do not let it.
   - `stdlib/not-compiling.txt` — **one line per entry**, module name first. The check reads
     the first word of every non-comment line as a module name, so a wrapped paragraph
     becomes nine modules that do not exist and the ratchet fails in both directions. It is
     currently empty, and the file stays because the check is what notices the first module
     that stops compiling.
4. **Gates run without a toolchain**: `tools/docs-check.py`, `stdlib-check.py`,
   `grammar-check.py`, `example-check.py`, `type-name-check.py`, `status.py --check`. Run
   them before pushing; they take seconds and each catches a class of drift that no compiler
   run would.
5. **The accuracy gate compiles and runs every program under `examples/` and
   `tests/parity/` with ASan and UBSan.** It is the cheapest signal for codegen that is
   valid C but wrong, and it has caught real regressions within a minute.
6. **Every hard decision gets an ADR** in `docs/adr/`, indexed from `docs/README.md` —
   `tools/docs-check.py` enforces the link. Read 0006, 0007 and 0008 before touching arrays,
   strings or casts.
7. **When you find a defect, ask what check would have caught it** and add that check. More
   bugs in this repository were found by gates than by reading.

## Key files / entry points

- `compiler/src/` — `lexer`, `parser`, `sema`, `lowerer`, `backend`, `runtime.rs`.
- `crates/nova-common/src/` — the AST and SIR that every stage shares.
- `backends/` — the JavaScript, Rust and WebAssembly emitters.
- `stdlib/` — `core`, `io`, `math`, `text`, each with its own README.
- `compiler/tests/` — `end_to_end.rs`, `stdlib.rs`, `format.rs`, `item_tree.rs`,
  `stdlib_parse.rs`; `README.md` in that directory says what each covers.
- `docs/HANDOVER.md`, `docs/status.json`, `DEV_PLAN.md`, `docs/adr/`, `docs/tooling.md`.

## Gotchas

- **The default branch is `master`**, not `main` — every other drsamonline repo uses `main`.
- **A type must be rendered with `type_display`, never `TypeExpr::name`.** `Option<int>`
  stores name `Option` plus a generics list; reading `.name` gives `Option`, and `c_type`
  maps that to `int`, so the argument disappears with no diagnostic. This one mistake
  produced ten defects across the lowerer and the analyser. `tools/type-name-check.py`
  fails CI on it.
- **A helper that inspects a `SirExpr` must unwrap `SirExpr::Typed` first.** The lowerer
  annotates expressions with their type, so `range(0, 4)` arrives as
  `Typed { expr: Call { callee: "range" } }`. A helper matching the call directly never
  matches — that made every `for i in range(..)` iterate zero times, in a module that
  compiled and passed every gate. The same check covers this.
- **A struct field needs a complete type.** Structs are emitted in dependency order, because
  `Holder { maybe: Option<int> }` must follow `Option_int`.
- **A `while`/`if` branch whose only item is an expression puts it in `final_expr`**, not in
  `statements`. Reading only `statements` drops the body — `lower_branch` handles both.
- **`/tmp` is 64 MB in the sandbox** and fills with clones; work in `/scratch/work`.
- **`-std=c11` is strict ISO**, so POSIX hides `struct timespec` and `nanosleep`. The
  runtime defines `_POSIX_C_SOURCE`; only the sanitiser job uses strict C, which is why the
  stdlib gate passes and the accuracy gate catches it.
- **Coverage is a CI-only measurement.** `cargo llvm-cov` cannot link through the
  toolchain workaround below; read the number from the Coverage job rather than predicting it.
- **`stdlib/not-compiling.txt` and `coverage-floor.txt` both ratchet in two directions** —
  a module that starts compiling must be removed, a floor that rises must be raised.

## Working without a Rust toolchain

`static.rust-lang.org` is not reachable from the sandbox, so `rustup` cannot install
anything. `conda.anaconda.org` **is** reachable and conda-forge ships a complete stable
toolchain as plain tarballs — extract `rust` and `rust-std-x86_64-unknown-linux-gnu`, put
`bin` on `PATH`, and the whole suite runs locally in seconds instead of a four-minute CI
round trip per change. There is no `cc`, so point the linker at Zig (`pip install ziglang`,
then `-C linker=<wrapper execing 'zig cc'>`) and set `CC` for the tests.

Two older loops also work: `./scripts/dev-loop.sh <branch>` builds on a runner and downloads
the binaries, and `zig cc` alone compiles emitted C to reproduce a C-level failure.

## Source projects

- [NEO](https://github.com/drsamonline/NEO) — Rust, NOVA language, `master` branch, v0.7.0.
