---
name: pack-frontend-ui
description: Interface work end to end: React and Next.js performance, composition and view transitions, CSS and layout craft, animation and motion, visual design language, shaders and web artifacts. Use when building, restyling or reviewing a user-facing interface.
license: see each member
metadata:
  title: "Frontend and UI pack"
  kind: "index pack"
  members: "180"
---

# Frontend and UI pack

180 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 11 upstream repositories.

## When to use

- Building or restructuring a React/Next.js app, a component library or a view transition.
- Choosing type, colour, spacing, layout or a whole visual language for a product.
- Animating something — entrance, interaction feedback, scroll — without hurting performance.
- Reviewing UI code against the Web Interface Guidelines.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`algorithmic-art`](../algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art,… | anthropics/skills | Apache-2.0 |
| [`algorithmic-color-palette`](../algorithmic-color-palette/SKILL.md) | Derive a full UI palette from one or two brand colours — state variants, brand-tinted greys, semantic colours. Use when building or expanding a colour system. | dembrandt/dembrandt-skills | MIT |
| [`animate`](../animate/SKILL.md) | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which… | emilkowalski/skills | MIT |
| [`animation-performance`](../animation-performance/SKILL.md) | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when an animation… | emilkowalski/skills | MIT |
| [`animation-vocabulary`](../animation-vocabulary/SKILL.md) | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS… | emilkowalski/skills | MIT |
| [`app-shell`](../app-shell/SKILL.md) | Top bar, sidebar rail, app launcher, tenant and environment cue, status bar. Use when designing the persistent shell, a collapsible sidebar, or navigation between apps behind… | dembrandt/dembrandt-skills | MIT |
| [`apple-design`](../apple-design/SKILL.md) | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, drag/swipe/sheet… | emilkowalski/skills | MIT |
| [`article-magazine`](../article-magazine/SKILL.md) | Substack / Medium 高级感长文排版, 适合公众号、博客发布 | nexu-io/html-anything | Apache-2.0 |
| [`article-sketchnote-editorial`](../article-sketchnote-editorial/SKILL.md) | 把一个概念铸成杂志专题档案——真问题→失败→转折→顿悟→命名, 6 个 layout 模具 + 4 字族对比 + 探案档案细节 | nexu-io/html-anything | Apache-2.0 |
| [`ask-sonner`](../ask-sonner/SKILL.md) | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and persisting toasts,… | emilkowalski/skills | MIT |
| [`authentic-product-representation`](../authentic-product-representation/SKILL.md) | Product visuals must show the real product with real data. Use when building landing pages, hero sections, screenshots or demo panels. | dembrandt/dembrandt-skills | MIT |
| [`banner-design`](../banner-design/SKILL.md) | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. Actions: design,… | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| [`baseline-ui`](../baseline-ui/SKILL.md) | Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. Use when the interface needs a fast cleanup or polish pass. | ibelick/ui-skills | MIT |
| [`blog-post`](../blog-post/SKILL.md) | 杂志感长文, 含 masthead、hero、figures、pull quote、作者署名 | nexu-io/html-anything | Apache-2.0 |
| [`brand`](../brand/SKILL.md) | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style… | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| [`brand-guidelines`](../brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style… | anthropics/skills | Apache-2.0 |
| [`brand-visual-language`](../brand-visual-language/SKILL.md) | Shape language across type, radius and icons carries brand personality. Use when starting a design system, picking icons or radius tokens, or reviewing visual consistency. | dembrandt/dembrandt-skills | MIT |
| [`break-ui`](../break-ui/SKILL.md) | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, long labels, non-Latin… | emilkowalski/skills | MIT |
| [`buddy-sings`](../buddy-sings/SKILL.md) | Turn your Claude Code pet into a singer. Each pet gets a unique vocal identity based on its name and personality — the same pet always sounds the same. | MiniMax-AI/skills | MIT |
| [`button-states`](../button-states/SKILL.md) | Rest, hover, active, focus, disabled and loading states, derived from the base colour. Use when designing buttons, links, inputs or any clickable component. | dembrandt/dembrandt-skills | MIT |
| [`canvas-design`](../canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other… | anthropics/skills | Apache-2.0 |
| [`card-twitter`](../card-twitter/SKILL.md) | 【模板: Twitter 分享卡】 - 容器 w-1600px h-900px, 暗色 / 亮色二选一根据内容情绪。 - 中央一句 hero 金句 (text-6xl, font-semibold, 限 2-3 行)。 - 下方作者署名 + 头像占位 + handle。 - 左上角小标签 (类型: "Insight" / "Data" /… | nexu-io/html-anything | Apache-2.0 |
| [`card-xiaohongshu`](../card-xiaohongshu/SKILL.md) | 【模板: 小红书图文卡片】 - 输出 N 张连续卡片, 每张 w-1080px h-1440px, 用 flex 纵向排列方便整体截图也方便单张截图。N 由【用户内容】信息量决定: 短内容 3-6 张起步, 长内容应更多 (小红书平台单帖最多 18 图, 通常 9 张以内最佳); 一张卡只承载一个核心观点。 - 第一张是封面: 巨大的标题 + 1… | nexu-io/html-anything | Apache-2.0 |
| [`clone-website`](../clone-website/SKILL.md) | Rebuild a live web page 1:1 from measurement into Figma, Penpot or code, then verify it. Use when reproducing a page or checking a rebuild against the original. | dembrandt/dembrandt-skills | MIT |
| [`color-font-skill`](../color-font-skill/SKILL.md) | Choose presentation-ready color palettes and font pairings for PPT/design tasks. Use when users ask for visual theme choices, brand-safe palettes, or font recommendations.… | MiniMax-AI/skills | MIT |
| [`color-mode-and-theme`](../color-mode-and-theme/SKILL.md) | Light, dark or both, and when a theme selector is worth it. Use when defining a base palette or deciding on dark mode support. | dembrandt/dembrandt-skills | MIT |
| [`competitive-teardown`](../competitive-teardown/SKILL.md) | 定位图 + 功能矩阵 + 价格对比 + 机会窗口, 把竞品资料转成产品决策报告 | nexu-io/html-anything | Apache-2.0 |
| [`component-canvas`](../component-canvas/SKILL.md) | Build a full-screen, interactive canvas to explore existing UI components and their variants with pan and zoom. | ibelick/ui-skills | MIT |
| [`component-family-consistency`](../component-family-consistency/SKILL.md) | Buttons, inputs, badges and pills share radius, colour logic, shadow, border and spacing. Use when building or reviewing a component library. | dembrandt/dembrandt-skills | MIT |
| [`coordinated-data-views`](../coordinated-data-views/SKILL.md) | Show a table and its map, diagram, timeline or chart together, with selection synced both ways. Use when data appears in two representations at once. | dembrandt/dembrandt-skills | MIT |
| [`create-canvas`](../create-canvas/SKILL.md) | Build a freeform canvas to explore, compare, and iterate on anything. | ibelick/ui-skills | MIT |
| [`create-design-md`](../create-design-md/SKILL.md) | Create or update a DESIGN.md from an existing product repository or public website. Use when asked to document an interface's design language, reconstruct its visual system,… | ibelick/ui-skills | MIT |
| [`dashboard`](../dashboard/SKILL.md) | 固定侧栏 + 顶栏 + KPI 网格 + 1-2 张图 | nexu-io/html-anything | Apache-2.0 |
| [`dashmotion`](../dashmotion/SKILL.md) | Create dark-themed, animated technical diagrams as self-contained HTML+SVG files — flowcharts whose connectors visibly flow, and architecture diagrams where requests travel as… | csthink/dashmotion | MIT |
| [`data-display-and-selection`](../data-display-and-selection/SKILL.md) | View modes, row selection, mass actions, sorting, filters, search and table patterns. Use when designing data tables, listings, file browsers or any collection. | dembrandt/dembrandt-skills | MIT |
| [`data-report`](../data-report/SKILL.md) | 把 CSV/Excel/JSON 数据转成漂亮的可视化报告页 | nexu-io/html-anything | Apache-2.0 |
| [`dating-web`](../dating-web/SKILL.md) | 消费感配对仪表板: 信号 ticker + KPI + 30 天柱状 + 趋势 | nexu-io/html-anything | Apache-2.0 |
| [`deck-blueprint`](../deck-blueprint/SKILL.md) | 奶油纸 + 锈红 + 蓝图网格 mask + 黑边硬卡片 + pipeline 盒 | nexu-io/html-anything | Apache-2.0 |
| [`deck-course-module`](../deck-course-module/SKILL.md) | 暖纸背景 + Playfair, 左侧学习目标常驻, 含 MCQ 自测页 | nexu-io/html-anything | Apache-2.0 |
| [`deck-dir-key-nav`](../deck-dir-key-nav/SKILL.md) | 8 页单色背景, 160px display + 4px accent + Mono 箭头列表 | nexu-io/html-anything | Apache-2.0 |
| [`deck-graphify-dark`](../deck-graphify-dark/SKILL.md) | 深夜渐变 + 漂浮 orbs + SVG 力导向图谱 + JetBrains Mono | nexu-io/html-anything | Apache-2.0 |
| [`deck-guizang-editorial`](../deck-guizang-editorial/SKILL.md) | 电子杂志 × 电子墨水; 10 个版面 + 5 套调色板 (墨水/靛蓝瓷/森林墨/牛皮纸/沙丘) | nexu-io/html-anything | Apache-2.0 |
| [`deck-hermes-cyber`](../deck-hermes-cyber/SKILL.md) | 黑底 + CRT 网格扫描线 + $ 命令行标题 + 薄荷绿大字 + 三档 tag | nexu-io/html-anything | Apache-2.0 |
| [`deck-ljg-present`](../deck-ljg-present/SKILL.md) | 把 outline 1:1 铸成色块大字宣言 deck, 原文不动只做美化。三档主题 black / red / yellow | nexu-io/html-anything | Apache-2.0 |
| [`deck-magazine-web`](../deck-magazine-web/SKILL.md) | 电子杂志 × 电子墨水风, WebGL 流体背景 + 衬线 display | nexu-io/html-anything | Apache-2.0 |
| [`deck-obsidian-claude`](../deck-obsidian-claude/SKILL.md) | GitHub-dark + 紫蓝环境光 + 三色渐变标题 + GitHub 风代码 | nexu-io/html-anything | Apache-2.0 |
| [`deck-open-slide-canvas`](../deck-open-slide-canvas/SKILL.md) | 锁死 1920×1080 画布, React 组件级自由组合, 不绑模板 | nexu-io/html-anything | Apache-2.0 |
| [`deck-pitch`](../deck-pitch/SKILL.md) | 10 页融资 deck, 白底 + 蓝紫渐变 hero, traction 柱状, $X.XM ask | nexu-io/html-anything | Apache-2.0 |
| [`deck-presenter-mode`](../deck-presenter-mode/SKILL.md) | tokyo-night 默认主题, T 切换 5 主题, S 打开提词器 popup | nexu-io/html-anything | Apache-2.0 |
| [`deck-product-launch`](../deck-product-launch/SKILL.md) | 暗 hero + 亮内容, 橙→桃 accent, 特性卡 + 定价 + CTA | nexu-io/html-anything | Apache-2.0 |
| [`deck-replit`](../deck-replit/SKILL.md) | Replit Slides 八套主题 (helix/holm/vance/bevel/world/atlas/bluehouse) | nexu-io/html-anything | Apache-2.0 |
| [`deck-safety-alert`](../deck-safety-alert/SKILL.md) | 红琥珀警示色 + hazard 条纹 + L1/L2/L3 tier 卡片 + 删除线标题 | nexu-io/html-anything | Apache-2.0 |
| [`deck-simple`](../deck-simple/SKILL.md) | 通用 horizontal-swipe HTML deck, 不要 magazine 调 | nexu-io/html-anything | Apache-2.0 |
| [`deck-swiss-international`](../deck-swiss-international/SKILL.md) | 16 列网格 + 单一饱和 accent + 22 个锁死版面 (Klein Blue / Lemon / Mint / Safety Orange) | nexu-io/html-anything | Apache-2.0 |
| [`deck-tech-sharing`](../deck-tech-sharing/SKILL.md) | GitHub-dark + JetBrains Mono + 终端代码块, 含 agenda + Q&A | nexu-io/html-anything | Apache-2.0 |
| [`deck-xhs-pastel`](../deck-xhs-pastel/SKILL.md) | 奶油底 + 柔光 blob + 马卡龙圆角卡片 + Playfair 斜体序号 | nexu-io/html-anything | Apache-2.0 |
| [`deck-xhs-post`](../deck-xhs-post/SKILL.md) | 9 页 3:4 竖版图文, 暖 pastel + 虚线 sticker 卡片 | nexu-io/html-anything | Apache-2.0 |
| [`deck-xhs-white`](../deck-xhs-white/SKILL.md) | 纯白 + 顶部彩虹 bar + 渐变文字 + 马卡龙软卡片 + 黑底 pill | nexu-io/html-anything | Apache-2.0 |
| [`dembrandt`](../dembrandt/SKILL.md) | Orchestrator that routes a UI/UX task through brand, tokens, layout, components, polish and accessibility. Use for multi-concern work such as a design review, UI build or… | dembrandt/dembrandt-skills | MIT |
| [`design`](../design/SKILL.md) | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corporate identity program (50… | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| [`design-style-skill`](../design-style-skill/SKILL.md) | 同一套设计可通过调整圆角（rectRadius）和间距呈现4种不同风格。根据场景选择合适的风格配方。 | MiniMax-AI/skills | MIT |
| [`design-system`](../design-system/SKILL.md) | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component… | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| [`digital-eguide`](../digital-eguide/SKILL.md) | 两页跨页电子指南, 封面 + 课程页 + pull-quote + 步骤列表 | nexu-io/html-anything | Apache-2.0 |
| [`doc-kami-parchment`](../doc-kami-parchment/SKILL.md) | 暖羊皮纸底 (#f5f4ed) + 墨蓝单色 accent (#1B365D) + 单一衬线字体, 编辑级排印 | nexu-io/html-anything | Apache-2.0 |
| [`docs-page`](../docs-page/SKILL.md) | 【模板: 技术文档页】 【意图】API / 教程文档单页, 长读体验优先。 【布局】 - Inline-start nav (sections + sticky) - Article body (含代码块, callouts, 表格) - Inline-end TOC (sticky, scroll-spy) - 顶栏 search +… | nexu-io/html-anything | Apache-2.0 |
| [`domain-expert-configuration`](../domain-expert-configuration/SKILL.md) | Settings for experts who are not developers — domain language, sane defaults, grouping by professional concept. Use when designing settings panels, solver configuration or… | dembrandt/dembrandt-skills | MIT |
| [`elevation-and-depth`](../elevation-and-depth/SKILL.md) | Shadows and layering that lift elements above the surface. Use when designing cards, dropdowns, modals, tooltips or any floating element. | dembrandt/dembrandt-skills | MIT |
| [`email-marketing`](../email-marketing/SKILL.md) | 产品发布邮件, 含 masthead、hero、CTA、规格表, table-fallback | nexu-io/html-anything | Apache-2.0 |
| [`emil-design-eng`](../emil-design-eng/SKILL.md) | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | emilkowalski/skills | MIT |
| [`eng-runbook`](../eng-runbook/SKILL.md) | 服务概述 + alerts 表 + dashboards + 操作命令 + on-call + 事故清单 | nexu-io/html-anything | Apache-2.0 |
| [`exec-briefing-memo`](../exec-briefing-memo/SKILL.md) | Decision needed + recommendation + evidence + tradeoffs, 把复杂材料压成可拍板的一页 | nexu-io/html-anything | Apache-2.0 |
| [`experiment-readout`](../experiment-readout/SKILL.md) | 假设 + 指标 + 结果 + 解释 + 决策, 把 A/B 或产品实验转成行动建议 | nexu-io/html-anything | Apache-2.0 |
| [`extract-design`](../extract-design/SKILL.md) | Extract colours, typography, spacing, components and W3C design tokens from a live website with Dembrandt. Use when you need a site's real tokens or want to seed a design… | dembrandt/dembrandt-skills | MIT |
| [`finance-report`](../finance-report/SKILL.md) | Masthead + KPI + 收入/烧钱图 + P&L 表 + 重点 + 展望 | nexu-io/html-anything | Apache-2.0 |
| [`find-animation-opportunities`](../find-animation-opportunities/SKILL.md) | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does not implement… | emilkowalski/skills | MIT |
| [`fixing-accessibility`](../fixing-accessibility/SKILL.md) | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls,… | ibelick/ui-skills | MIT |
| [`fixing-metadata`](../fixing-metadata/SKILL.md) | 1. Identify pages with missing or incorrect metadata (titles, descriptions, canonical, OG tags) 2. Audit against the priority rules below — fix critical issues (duplicates,… | ibelick/ui-skills | MIT |
| [`fixing-motion-performance`](../fixing-motion-performance/SKILL.md) | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stutter, transitions… | ibelick/ui-skills | MIT |
| [`flowai-team-dashboard`](../flowai-team-dashboard/SKILL.md) | 三个 tab 的团队管理后台: 成员、详情、活动日志, 含图表 + CSV 导出 | nexu-io/html-anything | Apache-2.0 |
| [`form-design`](../form-design/SKILL.md) | Helper text, placeholders, validation and submit behaviour. Use when designing or reviewing a form, input field or data entry UI. | dembrandt/dembrandt-skills | MIT |
| [`frame-data-chart-nyt`](../frame-data-chart-nyt/SKILL.md) | NYT-newsroom 排版 + 错峰揭示动画 + 编辑级图表 (折线/柱/范围带) | nexu-io/html-anything | Apache-2.0 |
| [`frame-flowchart-sticky`](../frame-flowchart-sticky/SKILL.md) | SVG 曲线连接 + 便利贴节点 + 光标交互, 像白板 brainstorm | nexu-io/html-anything | Apache-2.0 |
| [`frame-glitch-title`](../frame-glitch-title/SKILL.md) | 数字故障 / 像散偏移 / 数据腐败标题, 适合视频转场 / cyberpunk hero | nexu-io/html-anything | Apache-2.0 |
| [`frame-light-leak-cinema`](../frame-light-leak-cinema/SKILL.md) | 胶片漏光 + 颗粒噪点 + 16:9 letterbox + 衬线大字, 电影感开场 / 章节卡 | nexu-io/html-anything | Apache-2.0 |
| [`frame-liquid-bg-hero`](../frame-liquid-bg-hero/SKILL.md) | WebGL 风流体置换背景 + 顶部叠加金句, 适合视频片头 / landing hero / 海报 | nexu-io/html-anything | Apache-2.0 |
| [`frame-logo-outro`](../frame-logo-outro/SKILL.md) | Logo 分块组装入场 + glow bloom + tagline 揭示, 适合视频片尾 / 品牌闭幕 | nexu-io/html-anything | Apache-2.0 |
| [`frame-macos-notification`](../frame-macos-notification/SKILL.md) | 拟真 macOS 通知 banner + app icon + 标题正文, 适合 video overlay / 产品发布预告 | nexu-io/html-anything | Apache-2.0 |
| [`frontend-design`](../frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't… | anthropics/skills | Apache-2.0 |
| [`frontend-dev`](../frontend-dev/SKILL.md) | Build complete, production-ready frontend pages by orchestrating 5 specialized capabilities: design engineering, motion systems, AI-generated assets, persuasive copy, and… | MiniMax-AI/skills | MIT |
| [`frontend-ui-engineering`](../frontend-ui-engineering/SKILL.md) | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components, implementing layouts, meeting WCAG… | addyosmani/agent-skills | MIT |
| [`gamified-app`](../gamified-app/SKILL.md) | 三屏: 封面 / 今日任务带 XP / 任务详情, 暗色舞台 | nexu-io/html-anything | Apache-2.0 |
| [`generate-ui-from-brand`](../generate-ui-from-brand/SKILL.md) | Pipeline from a URL or DESIGN.md to tokens, decisions and a UI spec. Use when building UI for an existing brand, auditing a design system or fixing visual inconsistency. | dembrandt/dembrandt-skills | MIT |
| [`gestalt-ui-organisation`](../gestalt-ui-organisation/SKILL.md) | Group controls with Gestalt principles so users see what belongs together. Use when laying out components, navigation, toolbars, forms or dashboards. | dembrandt/dembrandt-skills | MIT |
| [`gif-sticker-maker`](../gif-sticker-maker/SKILL.md) | Convert user photos into 4 animated GIF stickers (Funko Pop / Pop Mart style). | MiniMax-AI/skills | MIT |
| [`global-toolbar-controls`](../global-toolbar-controls/SKILL.md) | Currency, language, region and unit selectors live in a low-profile header or footer spot. Use when designing locale switchers or product-wide preference controls. | dembrandt/dembrandt-skills | MIT |
| [`hallmark`](../hallmark/SKILL.md) | Design skill for websites and new pages that look designed, not generated. Use when the user asks to build or design something new, or names Hallmark. Never use it on an… | Nutlope/hallmark | MIT |
| [`hr-onboarding`](../hr-onboarding/SKILL.md) | 首周日程 + buddy + 学习路径 + 设备 + 完成标准 | nexu-io/html-anything | Apache-2.0 |
| [`improve-animations`](../improve-animations/SKILL.md) | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or cheaper… | emilkowalski/skills | MIT |
| [`improve-ui`](../improve-ui/SKILL.md) | Audit an existing product surface against its own design evidence, identify verified UI problems, and write self-contained implementation plans for another agent. Strictly… | ibelick/ui-skills | MIT |
| [`info-funnel`](../info-funnel/SKILL.md) | 3-6 阶递减漏斗, 突出转化率 / 筛选比例 / 流量损耗。竖图适合 IG Story / 小红书 | nexu-io/html-anything | Apache-2.0 |
| [`information-architecture`](../information-architecture/SKILL.md) | Naming, navigation, a UI that mirrors the data model, confirms for irreversible changes. Use when structuring a large application or naming its entities. | dembrandt/dembrandt-skills | MIT |
| [`invoice`](../invoice/SKILL.md) | 标准发票: 寄件/收件 + 明细 + 税 + 总额 + 付款指引 | nexu-io/html-anything | Apache-2.0 |
| [`kanban-board`](../kanban-board/SKILL.md) | To do / In progress / In review / Done 四列, 卡片 + 头像 + 泳道 | nexu-io/html-anything | Apache-2.0 |
| [`layout-paradigms-and-consistency`](../layout-paradigms-and-consistency/SKILL.md) | Choose a layout paradigm (feed, board, table, canvas, master-detail, dashboard) and reuse it across screens. Includes a landing page narrative framework. Use when structuring a… | dembrandt/dembrandt-skills | MIT |
| [`live-dashboard`](../live-dashboard/SKILL.md) | Notion 风团队仪表板, KPI + 7 日 sparkline + activity feed + 任务表 | nexu-io/html-anything | Apache-2.0 |
| [`loading-states-and-perceived-performance`](../loading-states-and-perceived-performance/SKILL.md) | Spinners, skeletons and staggered reveals that manage wait times. Use when designing loading states, async data or the feel of a slow interface. | dembrandt/dembrandt-skills | MIT |
| [`magazine-poster`](../magazine-poster/SKILL.md) | Sunday-paper 风格, 大字 serif headline + 双栏正文 + 编号 sections | nexu-io/html-anything | Apache-2.0 |
| [`marketing-vs-product-system`](../marketing-vs-product-system/SKILL.md) | A marketing site and its product may differ in density and scale but share one token layer. Use when the two drift apart, share components or need a single token owner. | dembrandt/dembrandt-skills | MIT |
| [`meeting-notes`](../meeting-notes/SKILL.md) | 标题 + 出席 + 议程 + 决议 + action items + 下次 | nexu-io/html-anything | Apache-2.0 |
| [`micro-interactions`](../micro-interactions/SKILL.md) | Small purposeful animations — toggles, animated icons, success moments. Use when designing interactive feedback, success states or loaders. | dembrandt/dembrandt-skills | MIT |
| [`minimax-music-gen`](../minimax-music-gen/SKILL.md) | Generate songs (vocal or instrumental) using the MiniMax Music API. Supports two creation modes: Basic (one-sentence-in, song-out) and Advanced Control (edit lyrics, refine… | MiniMax-AI/skills | MIT |
| [`minimax-music-playlist`](../minimax-music-playlist/SKILL.md) | Scan the user's music taste, build a taste profile, generate a personalized playlist, and create an album cover. This skill is designed for both agent and direct user… | MiniMax-AI/skills | MIT |
| [`mmx-cli`](../mmx-cli/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. Use when the user wants to create media content, chat with MiniMax models, perform web… | MiniMax-AI/skills | MIT |
| [`mobile-app`](../mobile-app/SKILL.md) | 像素级 iPhone 15 Pro 边框, 一屏 app 截图 | nexu-io/html-anything | Apache-2.0 |
| [`mobile-native`](../mobile-native/SKILL.md) | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. Covers sticky hover states,… | emilkowalski/skills | MIT |
| [`mobile-onboarding`](../mobile-onboarding/SKILL.md) | 三个手机框并排: splash / value-prop / sign-in | nexu-io/html-anything | Apache-2.0 |
| [`mockup-device-3d`](../mockup-device-3d/SKILL.md) | iPhone + MacBook 仿 GLTF 静态展架, 屏幕内嵌真实 HTML 内容, 玻璃镜头折射, 360° 转盘构图 | nexu-io/html-anything | Apache-2.0 |
| [`modal-and-overlay-patterns`](../modal-and-overlay-patterns/SKILL.md) | Modals, drawers, bottom sheets and popovers, each with its scope and blocking level. Use when designing dialogs, confirmations, side panels or action sheets. | dembrandt/dembrandt-skills | MIT |
| [`modular-scale-typography`](../modular-scale-typography/SKILL.md) | Ratio-based type scale where every size relates to the others. Use when defining font sizes or type tokens, or when typography feels arbitrary. | dembrandt/dembrandt-skills | MIT |
| [`motion-and-storytelling`](../motion-and-storytelling/SKILL.md) | Disney's animation principles and cinematic technique applied to UI motion. Use when designing transitions, scroll animations or onboarding motion. | dembrandt/dembrandt-skills | MIT |
| [`motion-frames`](../motion-frames/SKILL.md) | 可循环 CSS 动效组合: 旋转环、地球仪、计时器、视差标签 | nexu-io/html-anything | Apache-2.0 |
| [`nielsen-usability-heuristics`](../nielsen-usability-heuristics/SKILL.md) | Nielsen's 10 usability heuristics. Use when auditing an interface, designing interaction flows, writing error messages or reviewing usability. | dembrandt/dembrandt-skills | MIT |
| [`notifications-and-recovery`](../notifications-and-recovery/SKILL.md) | Toasts, inline errors, banners and recovery paths. Use when designing error states, success confirmations, async feedback or in-place editing. | dembrandt/dembrandt-skills | MIT |
| [`operational-expert-tool-ui`](../operational-expert-tool-ui/SKILL.md) | Dense, linear, status-at-a-glance UI for specialists who use a tool all day. Use when designing dispatch, warehouse, logistics, scheduling or other B2B operations tools. | dembrandt/dembrandt-skills | MIT |
| [`performance-and-web-vitals`](../performance-and-web-vitals/SKILL.md) | Lighthouse audits and Core Web Vitals — LCP, CLS, INP. Use when optimising page load, layout shift, input delay, images, fonts or render-blocking resources. | dembrandt/dembrandt-skills | MIT |
| [`pick-ui-library`](../pick-ui-library/SKILL.md) | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts, state,… | emilkowalski/skills | MIT |
| [`pm-spec`](../pm-spec/SKILL.md) | 问题 + 成功指标 + 范围 + user stories + 设计 + 发布 + 待解决 | nexu-io/html-anything | Apache-2.0 |
| [`poster-hero`](../poster-hero/SKILL.md) | 【模板: 营销海报】 - 容器 w-1080px h-1920px mx-auto, 全屏渐变 / mesh 背景。 - 上部 30% 留白 + 一个大 emoji 或抽象几何图形。 - 中部主标题占视觉中心 (text-8xl, font-black), 一句话副标题。 - 下部信息卡片: 3-5 条核心要点用图标 + 短句。 - 底部右下角放品牌… | nexu-io/html-anything | Apache-2.0 |
| [`ppt-keynote`](../ppt-keynote/SKILL.md) | 苹果 Keynote 级别幻灯片, 一屏一卡, 键盘左右切换 | nexu-io/html-anything | Apache-2.0 |
| [`pr-review`](../pr-review/SKILL.md) | Review pull requests against repository standards. Two-phase process: automated validation, then manual content review. | MiniMax-AI/skills | MIT |
| [`pricing-page`](../pricing-page/SKILL.md) | 【模板: 定价页】 【意图】标准 SaaS 三档定价页, 一眼对齐价值与价格。 【布局】 - Header + monthly/annual 切换 - 3 档定价卡片 (Free / Pro / Enterprise), 中间档 popular 高亮 - 完整特性对比表 (✓ / – / 不同档勾) - FAQ (details/summary) -… | nexu-io/html-anything | Apache-2.0 |
| [`prototype-web`](../prototype-web/SKILL.md) | 可点击的功能性 Web 原型, 含导航、英雄区、特性区、CTA | nexu-io/html-anything | Apache-2.0 |
| [`real-world-metaphors`](../real-world-metaphors/SKILL.md) | Cards, drawers, carousels and other patterns borrowed from the physical world. Use when designing layout patterns, gestures or navigation paradigms. | dembrandt/dembrandt-skills | MIT |
| [`remove-animations`](../remove-animations/SKILL.md) | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional data, and decoration with no purpose — then… | emilkowalski/skills | MIT |
| [`repeated-component-alignment`](../repeated-component-alignment/SKILL.md) | Cards, rows, tiles and cells are fixed slot models that stay aligned when content length varies. Use when building or reviewing any repeated component. | dembrandt/dembrandt-skills | MIT |
| [`responsive-paradigms`](../responsive-paradigms/SKILL.md) | Mobile, tablet and desktop are different paradigms, not one layout scaled. Use when designing responsive layouts or deciding what each breakpoint shows. | dembrandt/dembrandt-skills | MIT |
| [`resume-modern`](../resume-modern/SKILL.md) | 现代极简简历, A4 单页, 适合打印或导出 PDF | nexu-io/html-anything | Apache-2.0 |
| [`review-animations`](../review-animations/SKILL.md) | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. | emilkowalski/skills | MIT |
| [`saas-landing`](../saas-landing/SKILL.md) | 单页 SaaS 落地页, 含 hero/features/social-proof/pricing/CTA | nexu-io/html-anything | Apache-2.0 |
| [`scroll-areas`](../scroll-areas/SKILL.md) | Avoid inner scroll containers; when unavoidable, one axis at a time. Use when a layout, table or panel might scroll inside the page. | dembrandt/dembrandt-skills | MIT |
| [`semantic-html-and-seo`](../semantic-html-and-seo/SKILL.md) | Semantic HTML5, SEO basics, alt text, progressive enhancement and SPA concerns. Use when building web UI, reviewing markup or optimising for search. | dembrandt/dembrandt-skills | MIT |
| [`shader-dev`](../shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid simulation, particle systems, procedural generation, lighting,… | MiniMax-AI/skills | MIT |
| [`sizing-units`](../sizing-units/SKILL.md) | rem, px or relative units for each kind of value. Use when defining spacing and sizing tokens, control heights or media queries, or when a layout breaks under enlarged text. | dembrandt/dembrandt-skills | MIT |
| [`slack-gif-creator`](../slack-gif-creator/SKILL.md) | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for… | anthropics/skills | Apache-2.0 |
| [`slides`](../slides/SKILL.md) | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| [`social-carousel`](../social-carousel/SKILL.md) | 三张方形卡片轮播, 标题串联, 品牌 mark + 编号 | nexu-io/html-anything | Apache-2.0 |
| [`social-media-dashboard`](../social-media-dashboard/SKILL.md) | 平台切换 + 粉丝/互动 KPI + 增长曲线 + Top post + 热门话题 | nexu-io/html-anything | Apache-2.0 |
| [`social-media-matrix`](../social-media-matrix/SKILL.md) | 电影感多平台社媒分析: 互动图、悬浮洞察、区间对比、明暗主题 | nexu-io/html-anything | Apache-2.0 |
| [`social-reddit-card`](../social-reddit-card/SKILL.md) | 拟真 Reddit 帖子卡 + 上下投票 + 评论数, 适合视频叠加 / 故事分享 | nexu-io/html-anything | Apache-2.0 |
| [`social-spotify-card`](../social-spotify-card/SKILL.md) | Spotify Now Playing 风格卡: 专辑封面 + 进度条 + 播放控制, 适配视频叠加 / 个人主页 | nexu-io/html-anything | Apache-2.0 |
| [`social-x-post-card`](../social-x-post-card/SKILL.md) | 拟真 X 推文卡片 + 互动数据 (likes/reposts/views), 适配视频叠加或图卡分享 | nexu-io/html-anything | Apache-2.0 |
| [`sprite-animation`](../sprite-animation/SKILL.md) | 像素美术 + kinetic 字体的解说帧, 纯 CSS 循环, 可录视频 | nexu-io/html-anything | Apache-2.0 |
| [`status-colors-and-errors`](../status-colors-and-errors/SKILL.md) | Few semantic colours, each meaning one thing, and errors with a way forward. Use when designing status indicators, validation, alerts or error states. | dembrandt/dembrandt-skills | MIT |
| [`sticky-and-fixed-elements`](../sticky-and-fixed-elements/SKILL.md) | Sticky headers, bottom toolbars, floating action buttons and pinned table headers. Use when deciding what stays on screen while the user scrolls. | dembrandt/dembrandt-skills | MIT |
| [`surface-separation`](../surface-separation/SKILL.md) | Set a surface apart by one means — border, elevation or fill — and keep opacity for state. Use when designing cards, panels, list rows, toolbars or any container. | dembrandt/dembrandt-skills | MIT |
| [`tab-navigation`](../tab-navigation/SKILL.md) | Tabs swap views under a shared context. Use when designing tabbed layouts, settings pages, detail views or dashboards with several data views. | dembrandt/dembrandt-skills | MIT |
| [`team-okrs`](../team-okrs/SKILL.md) | 季度 banner + 3 个目标 + KR 进度条 + owner + 状态 pill | nexu-io/html-anything | Apache-2.0 |
| [`theme-factory`](../theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can… | anthropics/skills | Apache-2.0 |
| [`ui-context-and-scope`](../ui-context-and-scope/SKILL.md) | Show where the user is and what their actions affect — breadcrumbs, regions, scope labels. Use when designing deep navigation or multi-section layouts. | dembrandt/dembrandt-skills | MIT |
| [`ui-density`](../ui-density/SKILL.md) | Match information density to platform and user type. Use when designing data tables, dashboards or toolbars, or adapting a desktop product for mobile. | dembrandt/dembrandt-skills | MIT |
| [`ui-skills-root`](../ui-skills-root/SKILL.md) | Use before UI-related work to select the smallest useful UI Skills context through the ui-skills CLI. | ibelick/ui-skills | MIT |
| [`ui-styling`](../ui-styling/SKILL.md) | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Use… | nextlevelbuilder/ui-ux-pro-max-skill | Apache-2.0 |
| [`ui-ux-pro-max`](../ui-ux-pro-max/SKILL.md) | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces, including pages, components, design… | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| [`user-flows-and-guided-paths`](../user-flows-and-guided-paths/SKILL.md) | Guided multi-step paths and wizards. Use when designing onboarding, checkout, setup sequences or any multi-step journey. | dembrandt/dembrandt-skills | MIT |
| [`vercel-composition-patterns`](../vercel-composition-patterns/SKILL.md) | Composition patterns for building flexible, maintainable React components. Avoid boolean prop proliferation by using compound components, lifting state, and composing… | vercel-labs/agent-skills | NOASSERTION |
| [`vercel-react-best-practices`](../vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure… | vercel-labs/agent-skills | NOASSERTION |
| [`vercel-react-view-transitions`](../vercel-react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition… | vercel-labs/agent-skills | NOASSERTION |
| [`vfx-text-cursor`](../vfx-text-cursor/SKILL.md) | 光标拖光 + 彩色像散射线 + 定向光斑, 适合视频片头逐字揭示金句 | nexu-io/html-anything | Apache-2.0 |
| [`video-hyperframes`](../video-hyperframes/SKILL.md) | Hyperframes / Remotion 兼容的连续帧动画, 可自动播放 | nexu-io/html-anything | Apache-2.0 |
| [`vision-analysis`](../vision-analysis/SKILL.md) | Analyze images using the MiniMax MiniMaxunderstandimage MCP tool available in the MiniMax Token Plan. | MiniMax-AI/skills | MIT |
| [`visual-emphasis-and-hierarchy`](../visual-emphasis-and-hierarchy/SKILL.md) | Size, colour, weight and position mark what matters most. Use when designing button groups, CTAs, cards, dashboards or any layout with a primary action. | dembrandt/dembrandt-skills | MIT |
| [`waitlist-page`](../waitlist-page/SKILL.md) | 极简产品预发布落地页, 含邮箱捕获、logo、装饰图层 | nexu-io/html-anything | Apache-2.0 |
| [`wcag-accessibility`](../wcag-accessibility/SKILL.md) | WCAG 2.2 AA compliance as required by the European Accessibility Act. Use when designing, building or reviewing any user-facing interface for accessibility. | dembrandt/dembrandt-skills | MIT |
| [`web-artifacts-builder`](../web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex… | anthropics/skills | Apache-2.0 |
| [`web-proto-brutalist`](../web-proto-brutalist/SKILL.md) | Swiss industrial-print 风: 单字 grotesque、巨数字、ASCII 装饰 | nexu-io/html-anything | Apache-2.0 |
| [`web-proto-editorial`](../web-proto-editorial/SKILL.md) | Editorial-minimalist: 暖色单色 canvas + serif display + grotesque body | nexu-io/html-anything | Apache-2.0 |
| [`web-proto-soft`](../web-proto-soft/SKILL.md) | Apple 调: 银/奶 canvas + 双层斜面卡片 + button-in-button + spring | nexu-io/html-anything | Apache-2.0 |
| [`weekly-update`](../weekly-update/SKILL.md) | 6-8 页横向滑动周报: 已发布 / 进行中 / 阻塞 / 指标 / 求助 | nexu-io/html-anything | Apache-2.0 |
| [`wireframe-sketch`](../wireframe-sketch/SKILL.md) | 网格背景 + marker 笔触 + 多 tab + sticky note + scribble 图表 | nexu-io/html-anything | Apache-2.0 |
| [`write-swift`](../write-swift/SKILL.md) | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, task groups),… | emilkowalski/skills | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0, MIT, NOASSERTION). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
