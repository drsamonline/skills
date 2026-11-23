# Proving a guard works

A guard that has never been seen to fail is a comment. Every guard in this skill was checked the same
way, and four of them were wrong the first time.

## The loop

1. **Break it on purpose.** Reintroduce the exact defect the guard exists for — the stale date, the
   missing file, the withdrawn number, the denied release.
2. **Run only the guard.** It must go red, and the failure message must name the thing you broke. A red
   that says "assertion failed" is not enough: the message is what a future reader acts on.
3. **Restore, and run it again.** Green.
4. **Commit the loop in the test file**, not only the guard: a comment saying "mutation-tested" is worth
   less than the test that pins the *mechanism*.

## The four mutations that exposed a guard passing for the wrong reason

**1. A paragraph, not a line.** A withdrawal notice wrapped mid-sentence, so the line containing the
withdrawn number did not contain the word "withdrawn". The guard failed on its first run — on correct
prose. Fix: match a paragraph (split on blank lines), or normalise whitespace first.

**2. The machine, not the code.** A guard asserted that a missing binary is recorded as missing. It
passed locally and failed in CI, because the runner *had* the binary. Fix: stub the lookup
(`shutil.which`) instead of trusting the box.

**3. A fast codec rounded to zero.** A probe rounded each median to four decimals for display; on a
small input the fastest codec landed under 0.05 ms, rounded to `0.0000 s`, and the multiplier divided
by it. Passed locally, `ZeroDivisionError` on the runner. Fix: more precision for the value, a guard on
the division, and a test with a tiny input.

**4. An error message read as a version.** A version probe matched the word "version" — and the tool's
error output was `Unsupported command: --version`, so a failure was recorded as a version string. Fix:
match the banner the tool actually prints, and prefer a positive marker (`7-Zip`) over a generic word.

## What each of these has in common

The guard was measuring something adjacent to what it claimed. That is the failure mode to hunt: not
"does the guard pass", but **"would it pass if the thing it guards were broken?"** — and, just as
often, **"does it depend on this machine rather than on this repository?"**
