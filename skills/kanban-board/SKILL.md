---
name: kanban-board
description: To do / In progress / In review / Done 四列, 卡片 + 头像 + 泳道
license: Apache-2.0
metadata:
  title: "kanban board"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/kanban-board/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

【模板: Kanban 看板】
【意图】类 Trello 的 Kanban 单页。
【布局】
- 顶部 filter bar (assignee / label / search)
- 4 列: To do / In progress / In review / Done
- 卡片含: 标题 / labels / due / avatar / 评论数
- 可选 swimlanes (按 epic / assignee 分组)
【设计细节】
- 不需要真 drag, 但视觉上要像可拖

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/kanban-board/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
