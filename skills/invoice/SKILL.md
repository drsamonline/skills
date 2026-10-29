---
name: invoice
description: 标准发票: 寄件/收件 + 明细 + 税 + 总额 + 付款指引
license: Apache-2.0
metadata:
  title: "invoice"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/invoice/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

【模板: 可打印发票】
【意图】A4 可打印的发票单页。
【布局】
- Header: 发票号 / 日期 / 截止日
- From / Bill to 两块
- Line items table (描述 / 数量 / 单价 / 金额)
- Tax breakdown + Totals (右对齐)
- Payment instructions 区
【设计细节】
- @media print 样式; 颜色对比保留

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/invoice/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
