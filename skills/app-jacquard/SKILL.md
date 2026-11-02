---
name: app-jacquard
description: A Weft-8 8-bit assembler and VM in the browser, with the clock, calendar, clipboard and accelerometer exposed as memory-mapped peripherals — automation you can read as assembly.
metadata:
  title: "Jacquard — the loom you program"
---

# Jacquard — the loom you program

Automation usually hides behind coloured boxes. Jacquard puts a real machine underneath it: a fictional 8-bit CPU — the Weft-8, sixteen registers, four flags, twenty-seven instructions — programmed in assembly, with the clock, the calendar, the clipboard and the accelerometer exposed as **memory-mapped peripherals**. You read a register, you act on it.

## When to use

- You want a small automation surface whose logic is readable as assembly.
- You need to expose host capabilities (time, clipboard, sensors) to a sandboxed machine.
- You are teaching how a program talks to hardware.

## Method

1. Load the machine from `docs/play/weft8.js` and keep the page logic in `docs/play/index.html` — the machine is a script on a global, not a bundle.
2. Map each peripheral to fixed addresses and document the map in the page; a peripheral is a memory address, so the contract is the address table.
3. Write programs as assembly text in the page so the reader can see the whole program, not a summary of it.
4. Treat a missing peripheral (no accelerometer on a desktop, clipboard permission denied) as a defined value, not an exception.
5. Test with `node test-node.js` and `node tests/page-smoke.js` (`npm test`); the README keeps an honest note on the instruction count.

## Key files / entry points

- `docs/play/weft8.js` — the assembler and VM.
- `docs/play/index.html` — the editor, the address map and the run loop.
- `test-node.js`, `tests/page-smoke.js`.

## Gotchas

- Memory-mapped peripherals need a "not present" value; an exception inside the VM turns a missing sensor into a crash.
- Clipboard and sensor reads are permission-gated — the program has to handle refusal as a normal result.
- An instruction count quoted in the README drifts from the implementation; the note exists because that already happened.
- Reading a peripheral each loop iteration is not the same as sampling it once; decide which the program means.

## Source projects

- [app-jacquard](https://github.com/drsamonline/app-jacquard) — the assembler/VM and the memory-mapped peripheral map.
