---
name: email-marketing
description: 产品发布邮件, 含 masthead、hero、CTA、规格表, table-fallback
license: Apache-2.0
metadata:
  title: "email marketing"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/email-marketing/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

【模板: 品牌产品发布邮件】
【意图】纯 HTML 邮件, 600px 单栏, 兼容邮件客户端。
【布局】
- Masthead (wordmark 居中)
- Hero 图块 (SVG 占位)
- Headline lockup (含 skewed-italic accent)
- Body copy + primary CTA 按钮
- Specifications grid (3 列)
- Footer (社交 + 退订)
【设计细节】
- 使用 `<table role='presentation'>` 做布局兜底
- 颜色用 inline style (不要依赖 class)

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/email-marketing/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
