---
name: flowai-team-dashboard
description: 三个 tab 的团队管理后台: 成员、详情、活动日志, 含图表 + CSV 导出
license: Apache-2.0
metadata:
  title: "flowai team dashboard"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/flowai-team-dashboard/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

【模板: FlowAI 团队管理 Dashboard】
【意图】FlowAI 美学的团队管理 admin 单页。
【布局】
- Tabs: Team Members / Team Details / Activity Log
- KPI stat row
- Member table (avatar + 角色 + 状态)
- Role distribution bar chart
- Online presence + activity sparklines
- Top contributors panel
【设计细节】
- light/dark 切换, hover tooltip, click-to-zoom panels
- CSV export 按钮 (前端实现)

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/flowai-team-dashboard/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
