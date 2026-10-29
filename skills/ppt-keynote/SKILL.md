---
name: ppt-keynote
description: 苹果 Keynote 级别幻灯片, 一屏一卡, 键盘左右切换
license: Apache-2.0
metadata:
  title: "ppt keynote"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/ppt-keynote/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

【模板: Keynote 风格 PPT】
- 每张幻灯片是一个 `<section class="slide">`, 整体宽 1280 高 720, 居中显示, 背景渐变。
- 单页内容极简: 大标题 + 1-3 行支持文字; 或一张数据图; 或一个金句。
- 字号: 标题 `text-7xl font-semibold tracking-tight`, 副标题 `text-2xl text-neutral-500`。
- 第一页是封面 (主题 + 演讲者 / 日期), 最后一页是 "Thanks." 或行动号召。
- 顶部右上角小指示器: 当前页 / 总页数。
- 加一段 JavaScript 监听 ArrowLeft / ArrowRight / 空格键切换 slide; 同时维护 hash (#/3)。
- 每页之间用 fade-in 动画。
- 保持留白, 数据卡片用 grid 布局对齐, 颜色克制。

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/ppt-keynote/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
