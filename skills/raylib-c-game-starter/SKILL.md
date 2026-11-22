---
name: raylib-c-game-starter
description: Write a one-file C game starter on raylib with the same contract as the browser kit: fixed timestep, scenes, an ECS and a CRC-checked save — inside a 10 MB ceiling, as one binary for Windows, macOS, Linux, web, Android and a Raspberry Pi.
metadata:
  title: "raylib-starter"
---

# raylib-starter — the C answer to game-kit

One C file, a fixed timestep, scenes, save and an ECS — on raylib. The C answer to `game-kit`: the
same names, the same behaviour and the same tests, on a 2.4 MB engine instead of a browser. Built
for the 10 MB ceiling, as one binary that runs on Windows, macOS, Linux, the web (Emscripten),
Android and a Raspberry Pi.

## When to use

- The game must be a native binary — a Raspberry Pi, a kiosk, an offline machine with no browser.
- The size budget is the requirement (10 MB total), so an engine plus a framework is already too much.
- You want one contract across two platforms: the same loop, scenes, ECS and save as the browser kit.

## Method

1. Keep it to **one C file** plus raylib; the constraint is what makes it readable in an afternoon.
2. Fixed timestep with an accumulator and a clamp, exactly as the browser kit does it — same names, same behaviour, same tests.
3. Scenes as a small table of function pointers (`enter`, `update`, `draw`, `exit`), not an object system.
4. ECS as arrays: components in parallel arrays indexed by entity id, systems iterating the arrays. In C the data layout *is* the design.
5. Save with a CRC over the payload, so a truncated or hand-edited file is refused rather than loaded as nonsense.
6. Cross-compile from one source to every target; test the logic headlessly by keeping rendering behind a thin seam.

## Key files / entry points

- The single `.c` file: loop, scenes, ECS, save.
- The build for each target (native, Emscripten, Android).

## Gotchas

- A CRC is not a checksum for security, only for corruption — say which, or someone will trust it with a save file they care about.
- Fixed timestep in C needs the same `maxFrame` clamp as the browser: a debugger pause otherwise replays thousands of steps at once.
- Emscripten changes the frame loop; the web build must drive the same accumulator, not `emscripten_set_main_loop`'s own clock.

## Source projects

- [raylib-starter](https://github.com/drsamonline/raylib-starter)
