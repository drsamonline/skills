---
name: agent-operating-discipline
description: "How to work rather than what to build: split work into independent tasks and dispatch them in parallel with focused context, and refuse to claim anything is done until a verification command has actually run and its output read. Use before starting multi-part work, when several independent tasks could run concurrently, or whenever you are about to say a task is complete, fixed or passing."
license: "per source — see references/*/LICENSE"
metadata:
  title: "Agent operating discipline"
  category: "engineering-workflow"
  origin: "merged pack, imported 2026-11-07"
  merged-from: "dispatching-parallel-agents, verification-before-completion"
---

# Agent operating discipline

Two rules that catch most of the ways agent work goes wrong. **Parallelism** is only safe between tasks with no shared state, and it fails when the task briefs are vague. **Verification** is only meaningful if the command was run after the last change and its output was read — evidence before claims, always.

## When to use

- Two or more tasks could be worked on at once with no shared state or ordering.
- You are about to report work as complete, fixed, passing or shipped.
- You are about to commit, push, or open a pull request.

## Method

1. For delegation: identify genuinely independent domains. If the tasks share files, state, or an ordering, they are not parallel — do them in sequence.
2. Write each agent brief as if the agent has never seen the conversation: the goal, the context it needs, the constraints ('do not change production code', 'fix tests only'), and the exact shape of the answer you want.
3. State the write scope per agent so two agents cannot touch the same file; split by file, never by concern.
4. Dispatch in parallel, then review and integrate the results yourself — and verify the fixes do not conflict.
5. Do not delegate exploratory debugging (you do not yet know what is broken), and do not delegate a decision that needs the user.
6. For verification: before any success claim, run the command that proves it and read the output. The order is write → run (pass) → revert the fix → run (must fail) → restore → run (pass), so you know the test actually tests the change.
7. Never report a partial result as complete, and never report a command's success when you only saw its exit code.
8. If the verification fails, the claim is wrong — say what failed rather than softening the claim.

## Sources merged here

Each row is one skill that went into this one. The full original text, scripts and assets live in
`references/<id>/` — read the row first, then that folder.

| Source skill | What it adds |
|---|---|
| [`dispatching-parallel-agents`](references/dispatching-parallel-agents/) | When work is parallelisable, how to write agent briefs, what to hand back, and when not to dispatch. |
| [`verification-before-completion`](references/verification-before-completion/) | The evidence-before-claims gate: what must be run, what counts as proof, and the excuses to reject. |

## Key files / entry points

- `references/dispatching-parallel-agents/` — the dispatch pattern, brief structure, common mistakes, when not to use it.
- `references/verification-before-completion/` — the iron law, the gate function, red flags and rationalisation traps.

## Gotchas

- Vague briefs ('fix it') return work you cannot integrate.
- Agents inheriting the whole conversation lose focus — give them the context, not the history.
- A passing suite that was run before the last edit proves nothing.
- Increasing a timeout is not a fix for a hang.

## Licence & attribution

The merged text above is © 2026 Dr. Sohil Momin. Each merged source keeps its own licence and
attribution inside its folder under `references/`; where a source shipped a `LICENSE`, that file is
preserved verbatim next to it.

- `dispatching-parallel-agents` — no licence file shipped with the source
- `verification-before-completion` — no licence file shipped with the source
