---
name: html-web-page-styles
description: HTML web page styles — landing, pricing, docs, wireframe and prototype looks. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "HTML web page styles — landing, pricing, docs, wireframe and prototype looks"
  origin: "nexu-io/html-anything"
  merged-from: "10 skills"
  category: "frontend-ui"
---

# HTML web page styles — landing, pricing, docs, wireframe and prototype looks

A merge of 10 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- HTML web page styles — landing, pricing, docs, wireframe and prototype looks. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `docs-page` | 【模板: 技术文档页】 【意图】API / 教程文档单页, 长读体验优先。 【布局】 - Inline-start nav (sections + sticky) - Article body (含代码块, callouts, 表格) - Inline-end TOC (sticky, scroll |
| `motion-frames` | 可循环 CSS 动效组合: 旋转环、地球仪、计时器、视差标签 |
| `pricing-page` | 【模板: 定价页】 【意图】标准 SaaS 三档定价页, 一眼对齐价值与价格。 【布局】 - Header + monthly/annual 切换 - 3 档定价卡片 (Free / Pro / Enterprise), 中间档 popular 高亮 - 完整特性对比表 (✓ / – / 不同档勾) |
| `prototype-web` | 可点击的功能性 Web 原型, 含导航、英雄区、特性区、CTA |
| `saas-landing` | 单页 SaaS 落地页, 含 hero/features/social-proof/pricing/CTA |
| `waitlist-page` | 极简产品预发布落地页, 含邮箱捕获、logo、装饰图层 |
| `web-proto-brutalist` | Swiss industrial-print 风: 单字 grotesque、巨数字、ASCII 装饰 |
| `web-proto-editorial` | Editorial-minimalist: 暖色单色 canvas + serif display + grotesque body |
| `web-proto-soft` | Apple 调: 银/奶 canvas + 双层斜面卡片 + button-in-button + spring |
| `wireframe-sketch` | 网格背景 + marker 笔触 + 多 tab + sticky note + scribble 图表 |

## docs-page

【模板: 技术文档页】
【意图】API / 教程文档单页, 长读体验优先。
【布局】
- Inline-start nav (sections + sticky)
- Article body (含代码块, callouts, 表格)
- Inline-end TOC (sticky, scroll-spy)
- 顶栏 search + version + 主题切换
【设计细节】
- 代码块: 圆角 + dark + 语言标签 + 复制按钮
- callout: info / warn / danger 三色

## motion-frames

【模板: Motion 帧 / Hero Loop】
【意图】一帧带循环动效的 hero, 可作为视频片头或落地页大图。
【布局】
- Rotating type ring (SVG + transform)
- Animated globe / 抽象几何
- Ticking timer (mono 字体, JS 可有可无)
- Parallax labels 浮动
【设计细节】
- 纯 CSS 动效, 流畅可循环
- 电影感调色 + 1 个霓虹 accent

## pricing-page

【模板: 定价页】
【意图】标准 SaaS 三档定价页, 一眼对齐价值与价格。
【布局】
- Header + monthly/annual 切换
- 3 档定价卡片 (Free / Pro / Enterprise), 中间档 popular 高亮
- 完整特性对比表 (✓ / – / 不同档勾)
- FAQ (details/summary)
- 底部 CTA

## prototype-web

【模板: Web 产品原型】
- 输出一个完整的产品 landing page。
- Sections: Top Nav (logo + 导航 + CTA 按钮) → Hero (大标题 + 副标 + 双 CTA + 可视化占位) → Features (3-6 个特性卡) → How it works (步骤) → Social proof (logo wall / 评价) → Pricing (可选) → Footer。
- 使用现代 SaaS 设计趋势: 大字号、柔和渐变、glassmorphism 卡片、滚动到视图入场动画 (pure CSS 即可)。
- 响应式: 移动端单栏, 桌面多栏; 至少处理 `md:` 断点。
- 添加交互: nav 滚动变色; 特性卡 hover 浮起; FAQ 可手风琴展开 (用 `<details>`)。
- 这是高保真原型, 应该让人觉得"明天就能上线"。

## saas-landing

【模板: SaaS Landing】
【意图】完整的 SaaS 产品落地页, 把用户内容映射到标准 sections。
【布局】
- Top nav (logo + 导航 + sign-in + 主 CTA)
- Hero (大标题 + 副标 + 双 CTA + 可视化占位)
- Logo wall (社会认证)
- Features (3-6 个特性卡, icon + 标题 + 描述)
- How it works (3 步流程, 数字 + 标题 + 描述)
- Pricing (2-3 档, 推荐档高亮)
- FAQ (details/summary 手风琴)
- Footer
【设计细节】
- 现代 SaaS 风: 大字号, 柔和渐变, glassmorphism 卡片, 滚动入场动画
- 至少处理 `md:` 断点, 移动端单栏

## waitlist-page

【模板: 等候名单页 / Waitlist】
【意图】为新产品 / 早鸟内测做一张极简等候页。
【布局】
- 居中布局: brand logo + 一行 tagline + 大字 hero (说清楚做什么)
- 邮箱捕获 input + submit 按钮 (合并成一个 pill)
- 下方 3 个小卖点 (icon + 一行字)
- 底部 founders note + 社交链接
【设计细节】
- 装饰: SVG 渐变 mesh / 噪点纹理 / 一颗星轨
- 成功提交后给一个微动效 (✓ + 文案变化)

## web-proto-brutalist

【模板: Brutalist 网页原型】
【意图】Swiss Industrial Print 风格, 不柔和不友好, 强权威感。
【布局】
- Newsprint canvas + hairline grid dividers
- Monolithic black grotesque 标题, viewport-bleeding 巨数字
- Hazard-red accent + ASCII 装饰 (┌─┘ 等)
- Sections 用极简数字编号

## web-proto-editorial

【模板: Editorial 网页原型】
【意图】杂志感 minimalist, 大量留白 + 微动效。
【布局】
- Warm monochrome canvas
- Serif display + grotesque body + mono meta
- 1px hairline borders, 极柔和 chip
- Macro-whitespace, ambient micro-motion

## web-proto-soft

【模板: Apple Soft 原型】
【意图】Apple-tier 软质感, squircle + spring motion + ambient mesh。
【布局】
- Silver / cream canvas + ambient mesh background
- Double-bezel 卡片 (内外两层圆角 + 高光)
- Button-in-button CTA
- Spring motion (微反弹的 hover)

## wireframe-sketch

【模板: 手绘 Wireframe】
【意图】白板 / 草稿前阶段的 wireframe 探索。
【布局】
- Graph-paper 背景
- 多 tab labels (variants 标签)
- scribbled chart placeholders + hatched fills
- Sticky-note annotations (黄色, 旋转一点点)
【设计细节】
- 字体: Caveat / Architects Daughter; 不要规规矩矩的对齐

## Provenance

Merged from 10 skills of [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`. Licence Apache-2.0 — the source text of every variant is preserved above.
