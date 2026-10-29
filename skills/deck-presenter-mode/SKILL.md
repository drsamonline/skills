---
name: deck-presenter-mode
description: tokyo-night 默认主题, T 切换 5 主题, S 打开提词器 popup
license: Apache-2.0
metadata:
  title: "deck presenter mode"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/deck-presenter-mode/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

【模板: Presenter Mode Deck】
【意图】怕忘词的演讲者专用 deck, 含逐字稿 notes 与 popup teleprompter。
【布局】
- 每页 + `<aside class="notes">` 150-300 字稿
- 右下小 toolbar: T 切主题 / S 打开 popup
- Popup: CURRENT / NEXT / SCRIPT / TIMER 四张磁吸卡
【设计细节】
- 默认 tokyo-night; 共 5 套主题 (含 light)

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/deck-presenter-mode/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
