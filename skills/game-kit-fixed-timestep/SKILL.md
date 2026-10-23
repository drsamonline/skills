---
name: game-kit-fixed-timestep
description: Advance browser-game logic in equal fixed steps with an accumulator, clamping a huge frame so a backgrounded tab never spirals into thousands of updates; plus input, scenes, save/load and maths.
metadata:
  title: "A fixed-timestep game loop"
---

# A fixed-timestep game loop

## When to use

Any browser game or animation where physics or rules must behave the same at 30,
60 or 144 fps — and where a tab can be backgrounded and come back with a huge
elapsed time.

## Method

1. Keep an accumulator of real elapsed time.
2. Each frame add `dt`, then run whole `step`s (default `1/60`) while the
   accumulator holds one: `update(step)` each time.
3. **Clamp the frame** (`maxFrame`, e.g. 0.25 s) so a long pause does not queue
   thousands of steps; and cap the steps per frame as a second guard.
4. Pass the leftover fraction to `render(alpha)` for smooth interpolation.
5. Expose `tick(dt)` separately from `start()` (requestAnimationFrame), so the
   loop is **deterministic and testable headless**.

## Key files

- `game-kit.js` — `Game.loop`, `Game.input`, `Game.Scenes`, `Game.save`,
  `Game.clamp/lerp/dist/aabb/rand`.
- `test-node.js` — the verified loop (step counts, clamp, sub-step frames).

## Gotchas

- **Do not update by raw `dt`.** Frame-rate-dependent logic changes behaviour per
  device; fixed steps do not.
- **Always clamp.** Without it, returning to a backgrounded tab runs thousands of
  catch-up steps at once (the "spiral of death").
- **Floating point.** 60 × (1/60) can land a hair under 1.0, so compare with a
  tiny epsilon (`acc + 1e-9 >= step`) or a whole second simulates as 59 steps.
- **Test headless.** Drive `tick(dt)` in Node; keep `requestAnimationFrame` in the
  browser path only.

## Source projects

`neon-engine` and `Aethelgard-Engine`; consolidated into `game-kit`.
