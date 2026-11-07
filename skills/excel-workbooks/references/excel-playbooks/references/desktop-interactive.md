# Desktop Interactive (Card 12 how-to demos / Card 13 refreshing data connections)

## Card 12: in-app operation demo (cu_display: highlight)

**Route contract**
- **Primary channel**: version-aware guidance when the user wants to learn; `excel-live-control` when they instead want the change made in an open connected workbook and the required command is advertised.
- **Escalation trigger**: a visual CU lesson is allowed only when the exact operation has current O1 evidence for the detected OS, Excel edition/version, fixture, recovery path, and postcondition.
- **Hybrid handoff**: explain the goal and observable state first, then run one O1-scoped demonstration on a disposable copy and leave a concise observed step card.
- **Fallback**: provide version-aware guidance and ask the user to perform the unverified app step; do not improvise a menu path.
- **Verification**: use an operation-specific state check, such as scrolling for frozen panes or validating allowed/rejected input for a dropdown, and record the observed app scope.
- **CU display / reason**: `highlight` only after O1; when verified, the observed app operation is itself the teaching deliverable and the result is visible in the user's workbook.

**Trigger phrases**: "how do I do this" / "how do I freeze the top two rows" / "how do I make a dropdown list"
**Mode split**: "teach me" selects guidance or an O1-verified visual demo; "just do it" selects `excel-live-control` when available or a standalone workbook route when the user agrees.
**Steps**: (1) understand where they are stuck (2) detect the app, OS, edition, and version (3) load an O1 path only when its scope matches exactly (4) otherwise provide guidance or explore only as an explicit test on a disposable copy (5) verify the finished state (6) save the observed path and postcondition as test evidence before promoting it.
↯ The user's version has different menus -> stop following the stale path, inspect the visible controls, and treat the new path as provisional until the postcondition passes.
**Launch how-to library (10 items, picked from the official featured set plus internal samples)**: freeze panes / dropdown lists / removing outline grouping symbols / replacing XLOOKUP with INDEX+MATCH / conditional formatting to highlight duplicates / getting started with pivot tables / creating a chart quickly / text to columns / setting the print area / protecting a worksheet.
**CU reasoning (for the front end)**: once O1 exists, the demo is the deliverable and the user can see the postcondition. The library name alone does not make an operation recording-ready.
**Output assertion**: the target state is reached (each how-to has its own state check).

## Card 13: refresh Power Query and external data connections (web or desktop by source/state)

**Route contract**
- **Primary channel**: My Browser for a runtime-verified signed-in web plan/source that supports the required refresh state.
- **Escalation trigger**: use `excel-live-control` only if the connected session advertises a suitable refresh command; use Desktop CU only when the exact source/state and refresh/recovery path has current O1 evidence.
- **Hybrid handoff**: preflight source type, expected row count/control total, credentials boundary, and retained state before opening any interactive surface; after refresh, export only the verification receipt or requested artifact.
- **Fallback**: produce a diagnosis and user-operated refresh checklist, or rebuild the deterministic transformation through `Spreadsheets` when native connection state is not required.
- **Verification**: source row count or control total matches, refresh status and timestamp update, the intended query/connection is identified, and all credential interaction is user-operated.
- **CU display / reason**: `yes` only after O1 for an app-bound source/state; CU is justified by retained connection state or a local runtime dependency, not by refresh as a generic action.

**Trigger phrases**: "refresh this report for me" / "the data connection is throwing an error"
**Precondition**: identify source type, network reachability, credential location, the signed-in web plan, and whether a desktop-only add-in or workbook state is involved.
**Steps**:
1. Choose My Browser only after a supported web preflight; otherwise use an advertised live command or an O1-gated Desktop path for the app-bound source/state
2. Start with one identified query or connection; broaden the refresh only after the narrow result passes
3. Inspect the connection's reported status; ⚠ **a credential prompt means stop immediately and hand it back to the user. The agent never touches credentials.**
4. Check the result against source row count, a specified control total, refresh status, and refresh timestamp
↯ The source is unreachable -> output a diagnosis split three ways (network / permissions / the source changed). Do not keep hammering at it.
**Output assertions**: timestamp updated; credential interaction is 100% performed by the user (a security assertion).
**CU reasoning (for the front end)**: a desktop dependency may justify CU only after the exact path passes O1. Otherwise My Browser, advertised live tools, guidance, or a standalone transformation is the supported route.
