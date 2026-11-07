# Run log

Append one block per delivered run, newest last. Never rewrite or delete past
blocks — the window for the next run is derived from the last block here.

Format:

```
## <window end, YYYY-MM-DD> — window <window start> to <window end>
- Delivered: <channel>, <filename>, <N> PRs, <M> pages
- Notes: <skipped repos, gaps, partial failures — or "none">
```

## Window derivation

- If this log has no blocks, use the configured rolling window ending
  yesterday.
- Otherwise the next window starts the day after the last logged window end and
  ends yesterday, so consecutive runs tile without gaps or overlap.
- If that gap exceeds twice the configured window length (missed runs), keep the
  full span and say so in the report summary — a long window is better than a
  silent hole.
- After delivering, append the block. If delivery fails, append nothing; the
  window stays open and the next run covers it again.

## Log
