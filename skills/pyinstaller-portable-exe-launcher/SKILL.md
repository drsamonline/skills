---
name: PyInstaller portable EXE launcher
description: Turn a static web app into one double-clickable portable Windows .exe: a tiny Python launcher serves the bundled app/ over 127.0.0.1 and opens the browser, frozen by PyInstaller --onefile.
---

# PyInstaller portable EXE launcher

The desktop counterpart of the APK wrap. `exe/launcher.py` picks a free loopback port, serves a bundled `app/` folder with `http.server`, opens the default browser at it, and keeps running until the console window is closed. `exe/build.py` freezes launcher + app into one `<APP_NAME>-portable.exe` with `PyInstaller --onefile`. The result is a single file with no installer and no registry footprint.

## When to use

- You have a static web app and want a Windows deliverable a non-technical user can double-click.
- You want zero install, zero registry writes, and a file that runs from a USB stick.
- The same app is also shipped as an Android APK — both wrappers consume the same HTML.

## Method

1. Write `launcher.py`. Resolve the bundled data dir with `sys._MEIPASS` when `getattr(sys, 'frozen', False)`, else the script directory. That dir holds `app/`.
2. Pick a free port by binding `('127.0.0.1', 0)` and reading `getsockname()[1]`.
3. Subclass `SimpleHTTPRequestHandler` to silence logging (`log_message` no-op) and send `Cache-Control: no-store`; serve with `ThreadingHTTPServer` bound to `127.0.0.1`.
4. Open the browser with `threading.Timer(0.7, lambda: webbrowser.open(url)).start()` so the server is ready first, then `serve_forever()` with a `KeyboardInterrupt` handler.
5. Write `build.py`. Compute the `--add-data` separator from `os.name` (`;` on Windows, `:` elsewhere), then call `PyInstaller --noconfirm --clean --onefile --name <APP_NAME>-portable --distpath dist --workpath build --specpath spec --add-data <app_dir><sep>app launcher.py`. Output is `dist/<APP_NAME>-portable.exe`.
6. Read `APP_NAME` from the environment so the same script names the EXE for any app; default to `app` if unset.
7. In CI (windows-latest): checkout the app repo and the kit, set up Python 3.12, `pip install pyinstaller`, copy `APP_SRC/` into `builder/exe/app/`, run `python builder/exe/build.py`, and upload the EXE as an artifact.

## Key files / entry points

- `exe/launcher.py` — the loopback static server + browser opener.
- `exe/build.py` — the PyInstaller `--onefile` build.
- `exe/requirements.txt` — `pyinstaller`.
- `exe/app/` — the staged app folder (copied from the consuming repo before build).

## Gotchas

- `--add-data` separator differs by platform; getting it wrong silently produces an EXE that cannot find `app/`. Detect from `os.name`.
- The EXE is **unsigned**, so Windows SmartScreen will warn on first run — tell users 'More info → Run anyway'. Code-signing is out of scope for this kit.
- Bundle the app folder under the literal name `app` so `sys._MEIPASS/app` resolves at runtime; keep `launcher.py`'s `APP_DIR` in sync.
- `--onefile` unpacks to a temp dir on each run, so first launch is a little slower and some AV tools are suspicious of the packed binary.
- Build on `windows-latest`: PyInstaller does not cross-compile a Windows EXE from Linux.

## Source projects

- [app-builder](https://github.com/drsamonline/app-builder) — `exe/launcher.py`, `exe/build.py` and the workflow that consumes them.
- [All4ONE](https://github.com/drsamonline/All4ONE) — a large Python toolkit shipped as one portable `utility_suite.exe` built in CI (`build-windows-exe.yml`).

