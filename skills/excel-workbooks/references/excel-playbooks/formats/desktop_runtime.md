# Desktop Runtime (the Manus Desktop layer: default app / shared folder / CU decision / web tier)

If the session has no Desktop layer, skip sections 1-3. Route standalone workbook artifacts through `Spreadsheets`; use My Browser only when it is exposed in the current session and the requested Excel web state is supported.

## 1. Default-app detection (a conditional branch, not a mandatory start-up step)

Run this only when the requested deliverable must open in the user's preferred app, the user asks for an in-app demonstration, or the workflow needs an app runtime. Pure file creation and transformation do not need it.

- **macOS** (through the terminal channel):
  `osascript -e 'tell application "System Events" to get name of (application file id (do shell script "mdls -name kMDItemCFBundleIdentifier -raw $(mdfind \"kMDItemContentType == com.microsoft.excel.xls\" | head -1)"))'` is too heavy — **a one-line Swift call is more reliable**:
  `swift -e 'import AppKit; print(NSWorkspace.shared.urlForApplication(toOpen: URL(fileURLWithPath: "<path to some .xlsx>"))?.lastPathComponent ?? "none")'`
- **Windows** (PowerShell):
  `(Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.xlsx\UserChoice").ProgId`
- Branch on the result: `Microsoft Excel` -> Excel-specific branches may be considered after runtime preflight; `Numbers` -> deliver xlsx and reroute macro / PQ / slicer requests; `WPS Spreadsheets` -> deliver a compatible artifact but do not assume Excel macro behavior; `LibreOffice Calc` -> support xlsx/ODS delivery and reroute Excel-native PQ state; none -> standalone artifact only.
- The detected default is a delivery and compatibility signal. It does not prove that the app GUI is required, that the app is currently controllable, or that an Excel/Numbers/WPS/Calc procedure transfers across products.
- A failed detection does not block standalone delivery: treat it as "unknown" and use `Spreadsheets`. It blocks only claims that depend on a named app runtime.

## 2. Shared-folder precondition (pathguard)

Desktop local-file reads and writes require an authorized shared-folder root, and **a symlink cannot cross that boundary**. When the file sits outside, ask the user to move it into the shared folder or switch to upload. This bridge makes files reachable; it does not select an authoring engine and it is not Computer Use. Ask for an output location and preserve the original unless the user explicitly requests an in-place edit.

## 3. Five app-native escalation areas (not automatic Computer Use authorization)

| # | App-native state that may matter | Cards |
|---|---|---|
| 1 | A native query whose source, network reachability, add-in, or retained query state is unavailable on the standalone route | 9, 13 |
| 2 | Recalculation that depends on RTD or a third-party add-in installed in the user's Excel runtime | 13 |
| 3 | Importing or verifying VBA in the user's Excel runtime | 10 |
| 4 | An active locked workbook or a native object not supported by the standalone writer, such as a slicer | the file-lock branch, 5 |
| 5 | A visual lesson or print-layout task whose deliverable is the observed app state | 12 |

Preflight in this order:

1. If the workbook is already open, tagged, selected, or connected, defer to `excel-live-control`. It uses CU only for setup/focus and operates workbook content with advertised connected-session commands.
2. If the target is Excel for the web, use My Browser only when the current session exposes it and the signed-in account, plan, source, and retained state pass preflight.
3. Use Desktop CU only when the exact operation has an O1 event for the detected OS, Excel edition/version, fixture, recovery path, and objective postcondition. An O2 menu path is a candidate test, not permission to execute or record.
4. Without O1, provide version-aware guidance or a standalone artifact fallback. Do not improvise an app-native path.

On any credential, account, MFA, macro-security, or password prompt, stop and let the user take control.

## 4. Web version (the My Browser channel) capability tier — the answer to "why not just use the web version"

Excel for the web supports Power Query import, editing, loading, credential management, and refresh for documented sources, with plan and source limits. It does not run VBA. Route a web request through My Browser only after runtime availability and the signed-in account/source are checked. App-bound sources, add-ins, VBA, or desktop-only workbook state still require a separately verified Excel route; deterministic standalone batches belong to `Spreadsheets`.

## 5. Cross-OS notes

- Excel for Mac: branch Power Query by the current source matrix rather than assuming Windows parity. Do not execute or record a Mac GUI path without O1 for the installed build.
- Excel for Windows: organization policy may block macros or add-ins. The user or administrator handles policy changes. A Mac O1 event never releases a Windows route.
