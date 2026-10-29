---
name: html-dashboard-styles
description: HTML dashboard styles — KPI boards, analytics and team dashboards. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "HTML dashboard styles — KPI boards, analytics and team dashboards"
  origin: "nexu-io/html-anything"
  merged-from: "8 skills"
  category: "frontend-ui"
---

# HTML dashboard styles — KPI boards, analytics and team dashboards

A merge of 8 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- HTML dashboard styles — KPI boards, analytics and team dashboards. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `dashboard` | 固定侧栏 + 顶栏 + KPI 网格 + 1-2 张图 |
| `data-report` | 把 CSV/Excel/JSON 数据转成漂亮的可视化报告页 |
| `finance-report` | Masthead + KPI + 收入/烧钱图 + P&L 表 + 重点 + 展望 |
| `flowai-team-dashboard` | 三个 tab 的团队管理后台: 成员、详情、活动日志, 含图表 + CSV 导出 |
| `kanban-board` | To do / In progress / In review / Done 四列, 卡片 + 头像 + 泳道 |
| `live-dashboard` | Notion 风团队仪表板, KPI + 7 日 sparkline + activity feed + 任务表 |
| `social-media-dashboard` | 平台切换 + 粉丝/互动 KPI + 增长曲线 + Top post + 热门话题 |
| `social-media-matrix` | 电影感多平台社媒分析: 互动图、悬浮洞察、区间对比、明暗主题 |

## dashboard

【模板: 管理后台 Dashboard】
【意图】标准 admin/analytics 仪表板单页。
【布局】
- Fixed left sidebar (logo + 导航 + 用户 footer)
- Top bar (search + 通知 + avatar)
- Main: KPI cards 网格 (3-5 个)
- 1-2 张主图表 (折线 / 柱 / 区域)
- 底部 recent activity 列表

## data-report

【模板: 数据可视化报告】
- 头部: 报告标题 + 时间区间 + 数据来源说明。
- KPI 卡片网格: 3-5 个最重要指标, 每个卡片显示数值 + 同比变化 + 微型趋势线。
- 主图表区: 至少 2 个图表 (柱状 / 折线 / 饼 / 散点), 使用 Chart.js 或 ECharts (jsdelivr CDN 引入), 数据从用户输入解析得到。
- **图表容器必须有固定高度**: 每个 `<canvas>` 外层包一个 `<div style="position:relative;height:NNNpx">` (KPI 迷你图 ~40px, 主图表 ~240–280px)。Chart.js 用 `responsive:true, maintainAspectRatio:false` 时若父容器没有显式高度, 会陷入 ResizeObserver 死循环, 图表无限增高直至卡死浏览器。**绝对不要**直接给 canvas 写 `height=` 属性当布局, 那个只是初始值。
- 数据表格: 用户原始数据节选, 使用 `<table>` + 现代化样式 (zebra stripe, hover, sticky header)。
- 洞察块: 3-5 条文字洞察, 用 emoji 开头, 像产品周报。
- 底部"方法论"折叠区。
- 配色克制专业: 主色 1 + 中性色阶, 图表用调色板。
- **必须解析用户提供的实际数据**, 不要捏造。

## finance-report

【模板: 季度财报 / Finance Report】
【意图】财务向单页报告, 数字 + 图表 + 文字洞察。
【布局】
- Masthead (公司 + Q + 报告标题) + 4 个 hero KPI
- Revenue chart + Burn chart (Chart.js / ECharts)
- P&L 概要表 (zebra + sticky header)
- Top-line highlights (5 条 bullet)
- Outlook 段落
- Methodology 折叠区

## flowai-team-dashboard

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

## kanban-board

【模板: Kanban 看板】
【意图】类 Trello 的 Kanban 单页。
【布局】
- 顶部 filter bar (assignee / label / search)
- 4 列: To do / In progress / In review / Done
- 卡片含: 标题 / labels / due / avatar / 评论数
- 可选 swimlanes (按 epic / assignee 分组)
【设计细节】
- 不需要真 drag, 但视觉上要像可拖

## live-dashboard

【模板: Live Team Dashboard】
【意图】Notion 风的团队动态总览, 即使没有数据源也用 seed 数据兜底。
【布局】
- Header (团队 + 时间窗)
- KPI 卡片网格
- 7 天 sparkline 趋势
- Real-time activity feed (avatar + 动作 + 时间)
- Linked database task table (zebra + 状态 pill)
【设计细节】
- Notion-callout / toggle / 数据库表配色风格

## social-media-dashboard

【模板: 社媒创作者仪表板】
【意图】面向博主 / 创作者的社媒数据看板。
【布局】
- 顶部平台 switcher (X / LinkedIn / YouTube / Instagram / TikTok)
- KPI 卡片 (followers / engagement / likes / reposts)
- Follower-growth chart
- Top post this week 预览
- Side: trending topics / top comments

## social-media-matrix

【模板: 社媒矩阵追踪 (Social Matrix Tracker)】
【意图】电影感、数据密集的多平台社媒看板。
【布局】
- Hero header (统一品牌 + 时间窗 + 主题切换)
- Multi-platform KPI matrix (横 platform × 纵 metric)
- 交互式 charts (hover tooltip + range compare)
- Insights drawer (右抽屉, 文字洞察)
- Top posts grid
【设计细节】
- dark / light 切换; 数据用 seed 兜底

## Provenance

Merged from 8 skills of [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`. Licence Apache-2.0 — the source text of every variant is preserved above.
