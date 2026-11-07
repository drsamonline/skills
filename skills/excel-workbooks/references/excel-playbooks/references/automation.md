# Automation (Card 9 PQ pipeline / Card 10 macros / Card 16 recurring)

## Card 9: turn a repeating process into a reusable query pipeline (`cu_display: conditional-highlight`)

**Route contract**
- **Primary channel**: `Spreadsheets` for a reproducible standalone transformation when native Power Query state is not required; otherwise preflight the exact Excel web/desktop state before selecting an app route.
- **Escalation trigger**: use My Browser only when it is exposed and the signed-in plan/source supports the required query state. Use `excel-live-control` only for advertised commands. Use Desktop CU only for a source/state whose exact setup and refresh subflow has current O1 evidence on the detected build.
- **Hybrid handoff**: design and test the transformation on small samples, then create native query state only through the selected verified surface and deliver separate pipeline documentation.
- **Fallback**: keep the tested standalone transformation as a manual or scheduled pipeline; if schedule/source reachability is unproved, deliver a manual runner and documentation.
- **Verification**: a new sample refreshes into the expected rows and control totals, the intended reusable state survives reopen, and schema drift follows the documented failure branch.
- **CU display / reason**: `conditional-highlight` only after O1; CU is justified when the user's source or retained native query state genuinely requires Desktop Excel and the visible configuration produces a reusable workbook asset.

**Trigger phrases**: "I do this every month, can it be automated" / "freeze this process into something reusable"
**Precondition**: identify the source type, where its credentials live, whether the signed-in web plan supports import/edit/refresh, whether the result must remain a native Excel query, and whether desktop Excel is installed. Numbers or LibreOffice users -> reroute to a documented standalone transformation unless the user chooses Excel.
**Steps**:
1. Interview them on the process (what they do by hand each month, inputs and outputs)
2. Design the query: source, merge, and transform steps; include explicit tolerance for source-structure drift
3. Select the surface: My Browser for a runtime-verified supported web-plan/source combination; advertised live-control commands when available; an O1-gated Desktop CU path for a desktop-only source/state; `Spreadsheets` when retained native query state is unnecessary
4. Configure the smallest test query only on a verified surface, then add one new sample and refresh it
5. Deliver a "Pipeline Documentation" writeup: what each step does and how to change it (so it is not an undocumented black box)
↯ A PQ step errors -> roll that step back; if the whole thing is not viable -> fall back to the scheduled standalone approach in Card 16.
**CU reasoning (for the front end)**: highlight only when the actual source or retained state requires desktop Excel. The value is a visible, reusable pipeline in the user's workbook—not a blanket claim that Power Query is desktop-only. Do not publish a recorded desktop path until the current Excel build and selected source have an O1 event.
**Output assertion**: drop in a new sample -> refresh -> the result and reusable state are correct on the selected verified surface.

## Card 10: write or fix a macro (VBA)

**Route contract**
- **Primary channel**: software/source editing for supplied `.bas` or `.cls` files, plus `Spreadsheets` only for a separate test workbook or non-VBA workbook content.
- **Escalation trigger**: an import/run in Excel is allowed only through an exact current-build O1 CU subflow. `excel-live-control` explicitly does not claim macro enablement or execution unless a future advertised schema proves it.
- **Hybrid handoff**: create or review source and a side-effect manifest first; after user approval, hand the source and dated workbook copy to the O1-scoped app verification step.
- **Fallback**: deliver reviewed source, a harmless fixture, expected results, and user-run instructions without claiming the macro was installed or executed.
- **Verification**: source review passes, the smallest harmless test produces the expected workbook change, undeclared side effects remain zero, and rollback works on the dated copy.
- **CU display / reason**: `yes` only after O1; the meaningful CU moment is proving the macro inside the user's actual Excel runtime, not drafting source text.

**Trigger phrases**: "write me a macro" / "this macro is broken, fix it"
**Red lines**: no VBA password cracking; no macros that send things out automatically (mass email and the like — anything that sends is draft-only).
**Paths**:
- Existing source is supplied as `.bas` or `.cls`: review and edit it as source; import/run only through a dated workbook copy and an O1-verified Excel subflow
- Macro exists only inside `.xlsm`: do not claim that openpyxl can edit its VBA source. Export the module from the real VBE first, or limit the task to preserving the binary payload while editing non-VBA workbook content
- New macro: generate a `.bas` source file plus an import card; import and verify only when the exact Excel app path has O1 and the user approves the side-effect manifest
**Steps**: (1) obtain editable source and identify side effects (writes, sends, deletes, external processes) (2) write or edit a harmless testable module (3) prepare a dated workbook copy (4) when O1 permits, import and run the smallest test (5) compare the expected side-effect manifest (6) deliver source, workbook copy, comments, and rollback instructions. Without O1, stop after the source/test package and mark execution unverified.
↯ Macro security policy blocks it -> guide the user to adjust the setting themselves (the agent does not change security settings for them); note the mac VBA sandbox restrictions.
**Output assertions**: on the demo data the macro's result equals the expectation; no undeclared side effects.

## Card 16: generate and distribute a report on a schedule

**Route contract**
- **Primary channel**: `Spreadsheets` for the report artifact plus a scheduler actually exposed in the current Manus runtime and able to reach the chosen source.
- **Escalation trigger**: if no scheduler or source-access path is runtime-verified, keep the workflow manual; do not infer recurring access from a one-time Desktop shared-folder session.
- **Hybrid handoff**: prove one manual report run first, then pass frozen parameters and a reachable source to the exposed scheduler; communication remains draft-only or addressed to the user themselves.
- **Fallback**: deliver the reusable manual report runner, source checklist, and run-log schema without registering an automation.
- **Verification**: three scheduled cycles produce the same controlled result as the manual run, missing sources suppress empty delivery, and each run writes an observable receipt.
- **CU display / reason**: `no`; scheduling and artifact generation do not require Excel GUI state.

**Trigger phrases**: "email me this report automatically every Monday"
**Red line**: distribution stops at "send it to the user themselves / generate a draft". Nothing goes out automatically.
**Architecture gate**: schedule only sources that the scheduled runtime can demonstrably reach. A local Desktop shared-folder path is not production-supported here until a scheduled-run event proves availability; otherwise use a cloud-accessible source or keep the workflow manual.
**Steps**: (1) get a single run of the pipeline working (reuse Card 1 / Card 4) (2) freeze the parameters (3) prove the current runtime exposes a scheduler and can reach the chosen source (4) register only when those preconditions pass (5) write a run-log sheet on every run.
↯ A source file is missing on some run -> skip it and notify. Do not send an empty report.
**Output assertions**: 3 consecutive cycles trigger successfully; the output matches the single manual run.
