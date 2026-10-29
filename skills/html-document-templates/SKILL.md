---
name: html-document-templates
description: HTML document templates — resume, invoice, notes, OKRs, spec, runbook, article. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "HTML document templates — resume, invoice, notes, OKRs, spec, runbook, article"
  origin: "nexu-io/html-anything"
  merged-from: "30 skills"
  category: "office-docs"
---

# HTML document templates — resume, invoice, notes, OKRs, spec, runbook, article

A merge of 30 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- HTML document templates — resume, invoice, notes, OKRs, spec, runbook, article. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `article-magazine` | Substack / Medium 高级感长文排版, 适合公众号、博客发布 |
| `article-sketchnote-editorial` | 把一个概念铸成杂志专题档案——真问题→失败→转折→顿悟→命名, 6 个 layout 模具 + 4 字族对比 + 探案档案细节 |
| `blog-post` | 杂志感长文, 含 masthead、hero、figures、pull quote、作者署名 |
| `competitive-teardown` | 定位图 + 功能矩阵 + 价格对比 + 机会窗口, 把竞品资料转成产品决策报告 |
| `dating-web` | 消费感配对仪表板: 信号 ticker + KPI + 30 天柱状 + 趋势 |
| `digital-eguide` | 两页跨页电子指南, 封面 + 课程页 + pull-quote + 步骤列表 |
| `doc-kami-parchment` | 暖羊皮纸底 (#f5f4ed) + 墨蓝单色 accent (#1B365D) + 单一衬线字体, 编辑级排印 |
| `eng-runbook` | 服务概述 + alerts 表 + dashboards + 操作命令 + on-call + 事故清单 |
| `exec-briefing-memo` | Decision needed + recommendation + evidence + tradeoffs, 把复杂材料压成可拍板的一页 |
| `experiment-readout` | 假设 + 指标 + 结果 + 解释 + 决策, 把 A/B 或产品实验转成行动建议 |
| `frame-data-chart-nyt` | NYT-newsroom 排版 + 错峰揭示动画 + 编辑级图表 (折线/柱/范围带) |
| `frame-flowchart-sticky` | SVG 曲线连接 + 便利贴节点 + 光标交互, 像白板 brainstorm |
| `frame-glitch-title` | 数字故障 / 像散偏移 / 数据腐败标题, 适合视频转场 / cyberpunk hero |
| `frame-light-leak-cinema` | 胶片漏光 + 颗粒噪点 + 16:9 letterbox + 衬线大字, 电影感开场 / 章节卡 |
| `frame-liquid-bg-hero` | WebGL 风流体置换背景 + 顶部叠加金句, 适合视频片头 / landing hero / 海报 |
| `frame-logo-outro` | Logo 分块组装入场 + glow bloom + tagline 揭示, 适合视频片尾 / 品牌闭幕 |
| `frame-macos-notification` | 拟真 macOS 通知 banner + app icon + 标题正文, 适合 video overlay / 产品发布预告 |
| `gamified-app` | 三屏: 封面 / 今日任务带 XP / 任务详情, 暗色舞台 |
| `hr-onboarding` | 首周日程 + buddy + 学习路径 + 设备 + 完成标准 |
| `info-funnel` | 3-6 阶递减漏斗, 突出转化率 / 筛选比例 / 流量损耗。竖图适合 IG Story / 小红书 |
| `invoice` | 标准发票: 寄件/收件 + 明细 + 税 + 总额 + 付款指引 |
| `meeting-notes` | 标题 + 出席 + 议程 + 决议 + action items + 下次 |
| `mobile-app` | 像素级 iPhone 15 Pro 边框, 一屏 app 截图 |
| `mobile-onboarding` | 三个手机框并排: splash / value-prop / sign-in |
| `mockup-device-3d` | iPhone + MacBook 仿 GLTF 静态展架, 屏幕内嵌真实 HTML 内容, 玻璃镜头折射, 360° 转盘构图 |
| `pm-spec` | 问题 + 成功指标 + 范围 + user stories + 设计 + 发布 + 待解决 |
| `resume-modern` | 现代极简简历, A4 单页, 适合打印或导出 PDF |
| `team-okrs` | 季度 banner + 3 个目标 + KR 进度条 + owner + 状态 pill |
| `vfx-text-cursor` | 光标拖光 + 彩色像散射线 + 定向光斑, 适合视频片头逐字揭示金句 |
| `weekly-update` | 6-8 页横向滑动周报: 已发布 / 进行中 / 阻塞 / 指标 / 求助 |

## article-magazine

【模板: 杂志文章】
- 顶部 hero: 大标题 (text-5xl/6xl) + 可选副标题 + 作者 / 阅读时间 / 日期元数据。
- 正文: 单栏, 最大宽度约 700px, 居中。段落 `text-lg leading-relaxed text-neutral-700 dark:text-neutral-300`。
- H2 / H3 标题用 serif 字体, 让正文与标题有视觉对比。
- 引用块使用左侧粗 accent 色边线 + 斜体。
- 代码块: 圆角 + 深色背景 + 浅色文字, 显示语言标签。
- 列表项使用自定义 bullet（小方块 / accent 圆点）。
- 章节之间用 `<hr>` 分隔, 但样式做成中央居中的小 ornament。
- 文末加一个简单的 "如果觉得有用，欢迎转发" 行动卡片。

## article-sketchnote-editorial

【模板: 编辑式视觉笔记（Editorial Sketchnote）】

【灵魂】把一个**概念**铸成一份编辑式图文档案。读者翻它像翻一本期刊专题——从真问题（专题刊头）→ 失败的尝试（便签批注、档案标签）→ 一句"等等——"的转折（跨栏大标题）→ 看见那个东西（Hero 对开页）→ 名字（Closing 名牌）。

**不是博物馆陈列, 是杂志栏目。不是教科书定义, 是探案档案。** 视觉与叙事一起负责, 让读者自己经历"卡住—走不通—翻过去—看见了"的弧线。文字克制, 不点题。

【六条公理 — 任一不过, 重做】

1. **有真问题在前** — 起点是具体的、可触摸的、卡住的问题。不是「什么是 X」, 是「当时的人们用 A、B、C 都不够」。问题必须有裂缝。
2. **必须有失败** — 路径中至少一次失败（或走偏、半对了）。线性"由此可得"会杀掉张力。
3. **顿悟在前、命名在后** — 读者先「看到」, 再被告诉「这叫……」。**标题不能出现概念名**。
4. **「现在」视角** — 每一站是「他/她那一刻能看到什么」, 不是「我们站在 100 年后回望」。后世评价不进画面。
5. **文字克制, 不点题** — 禁用「你以为你刚才学到了一个概念」「你重新分娩了它」之类的元自指。让叙事张力自己产生发明感。允许诗意余韵（"于是, 你看见了山"）。
6. **中文母语表达** — 不要翻译腔。动词驱动 / 具体物件 / 口语节奏。禁忌："被 X""进行 X""在...的背景下""随着 X 的发展""该方法在多个维度上展现优势"。

【六个 layout 模具 — 节奏锁死】

每站必须用**不同的** layout, 节奏才出现：

| 序 | 站点 | class | 视觉特征 |
|---|---|---|---|
| 01 | 起点 / Feature | `.feature` | 米色底 + grid 6fr/6fr, 左大 SVG 图 / 右文字; kicker + Serif 大标题 + italic lead + drop-cap body |
| 02 | 失败一 / Note | `.note` | 双栏 grid（左 sidekick 涂鸦区 + 右 540px 便签纸）; 便签微旋 0.5deg + 顶部虚线穿孔 + 红笔删除线 + scribble + footnote ¹ |
| 03 | 失败二 / Archive | `.archive` | 全宽 + 黑色印章 stamp（168px, 含 ✕ 大字）+ 右栏 body + SVG 网格图 + verdict 红色 italic |
| 04 | 转折 / Cross | `.cross` | 全宽 + Serif 200px **由内容决定的转折爆点**（禁套「等等」）+ amber 高亮 + 二栏 |
| 05 | 顿悟 / Hero | `.hero` | 蓝色顶边 4px + grid 7fr/5fr; 左大 SVG / 右 pull-quote + drop-cap body |
| 06 | 命名 / Closing | `.closing` | 米色底 + 双线顶边 + 中心对称 + 巨大 Serif 名 + byline 上下细线 + epilogue |

**节奏铁律**: 开阔（feature）→ 紧（note 错位）→ 紧（archive 横长）→ 爆（cross 200px）→ 开阔（hero）→ 静（closing 中心对称）。不是均匀展开, 是有呼吸的——开阔与紧凑交替, 转折时大爆炸, 最后回到中心对称。

**禁区**：6 个节都是 60-80px margin-top 的均匀间距 = 画廊陈列, 不是漫画分镜, 重排。

【字族对比 — 必须四种同时使用】

- **Serif** (`Noto Serif SC`)：杂志主标题、mega-name、italic lead、pull-quote
- **Sans** (`Noto Sans SC`)：正文 body-sans、failed station head、kicker 后文字
- **Mono** (`JetBrains Mono` / `SF Mono`)：编号 num、kicker label、byline、footnote ¹、stamp
- **Hand** (`Caveat` / 楷体)：手写批注 scribble、ask 设问、caption

**任一缺席 = 视觉回到 AI 单一字族的均质感, 灵魂崩**。

【颜色系统 — ≤4 主色】

```
--bg:          #FAF7EF   /* 暖米白底 */
--paper:       #F5F1E5   /* 米色卡（feature/closing 底）*/
--ink-strong:  #0F0F0F   /* 重要文字, 避免 #000 */
--ink:         #1F1F1F   /* body */
--ink-light:   #6B6B6B   /* kicker, caption */
--red:         #B23A2C   /* 错误、批注、强调 */
--blue-deep:   #3D5A80   /* 顿悟视觉 */
--amber:       #BB8A2B   /* 转折提示 */
--amber-soft:  #D7A85A   /* 高亮底色 */
```

**禁止 `#000` 纯黑**。≤ 4 主色（红 + 蓝 + amber + 中性）。

【必备装饰结构件】

`kicker / drop-cap / byline / stamp` 是结构必须项。其它按需取用：

- **kicker** — 站点序号 + 类型小字：Mono uppercase 13px + 黑底白字 num 方块 + 36px 短横线
- **drop-cap** — body 首字：`::first-letter` float left, 96px Serif
- **lead** — feature 引言：italic 23px Serif + 红色左边线 2px
- **pull-quote** — hero 关键句：italic 38px Serif + 蓝色边线 4px + 浮动 `\201C` 大引号 100px
- **strike** — failed body 删除关键词：`text-decoration: line-through` 红色 2.5px
- **scribble** — note 红笔批注：Caveat 24px + 6deg 旋转 + 红色 + 虚线红边框
- **stamp** — archive 失败印章：黑底白字 12px Mono + ✕ Serif 64px
- **verdict** — archive 结案语：italic 19px Serif 红色 + 上虚线分隔
- **footnote** — note 脚注：Mono 13px + ¹ 上标
- **byline** — closing 出处：Mono 14px uppercase + letter-spacing 0.18em + 上下细黑线
- **mega** — cross 转折爆点：Serif 200px + amber 渐变高亮（核心字 1-3 个）
- **epilogue** — closing 余韵：italic 26px Serif + `—` 红色破折号前缀

【sidekick 涂鸦区 — note 模具左栏不能空】

三种填法（按内容选, 不要堆满）：
- **SVG 速写** — 失败本质能用 1-2 个图形姿态画出来 → `<svg viewBox="0 0 280 220">` 简笔画 + 红笔批注
- **手写公式** (`.formula`) — 失败本质能压成 1-3 行文字关系 → Caveat 22px + 虚线左边线 + 微旋 -1deg
- **箭头评注** (`.arrow`) — 单点强调 → Caveat 26px + 微旋 6deg + 红色

**约束**：sidekick 是注脚不抢戏 / 涂鸦感优先精致（歪斜、虚线、留缝隙）/ 颜色克制（黑灰 + 红）/ 内容密度低（宁可少不要塞三个图）。

【HTML 骨架（agent 复用结构, 内容由叙事弧线决定）】

```html
<div class="magazine-head">
  <div class="top-bar">
    <div class="left"><span class="badge">№ 01</span><span>[领域 · 年份]</span></div>
    <div class="right">[ENGLISH CATEGORY]</div>
  </div>
  <h1>[不剧透标题]<br>[第二行可选]</h1>
  <p class="deck">[italic 引言: 暗示问题但不揭示答案]</p>
</div>

<section class="feature">
  <div class="visual"><svg>[SVG 大图, max-width 540]</svg></div>
  <div class="meta">
    <div class="kicker"><span class="num">01</span><span class="rule"></span>起点 · [时空锚点]</div>
    <h2 class="head-serif">[卡住的问题]</h2>
    <p class="lead">[一句简洁领题]</p>
    <div class="body-sans drop-cap"><p>[具体例子]</p><p>[关键转折用 <em></em> 强调]</p><span class="ask">[开放设问？]</span></div>
  </div>
</section>

<aside class="note">
  <div class="sidekick">
    <!-- 三选一: SVG / .formula / .arrow + 可选 .doodle-caption -->
  </div>
  <div class="paper">
    <div class="kicker"><span class="num">02</span>第一次尝试</div>
    <h3 class="head-sans">[动作名]</h3>
    <div class="body-serif"><p>[思路]</p><p>失败用 <span class="strike">删除线</span></p></div>
    <div class="footnote"><span class="mark">¹</span><span>[根本原因]</span></div>
    <div class="scribble">[一句红笔批注]</div>
  </div>
</aside>

<section class="archive">
  <div class="stamp"><div class="label">EX-02</div><div class="x">✕</div><div class="case">Failed</div></div>
  <div class="body-area">
    <div class="kicker"><span>第二次尝试</span></div>
    <h3 class="head-sans">[动作名]</h3>
    <div class="visual"><svg>[失败示意]</svg></div>
    <div class="body-serif"><p>[思路 + 失败]</p></div>
    <div class="verdict">[结案语]</div>
  </div>
</section>

<section class="cross">
  <h2 class="mega"><span class="em">[转折爆点 1-3 字]</span>[可选后缀]</h2>
  <div class="grid">
    <div class="left">
      <div class="kicker"><span class="num">04</span>转折</div>
      <div class="body-serif"><p>[反向陈述]</p></div>
      <span class="ask">[转折设问？]</span>
    </div>
    <div class="right"><svg>[反向姿态]</svg><p class="caption">[caption]</p></div>
  </div>
</section>

<section class="hero">
  <div class="layout">
    <div class="visual"><svg>[大幅 hero 图]</svg><p class="caption">[caption]</p></div>
    <div class="text">
      <div class="kicker"><span class="num">05</span>顿悟</div>
      <h2 class="head-serif">[姿态名, 不出现概念名]</h2>
      <div class="pull-quote">[核心句子]</div>
      <div class="body-serif drop-cap"><p>[洞察的具体表述]</p></div>
    </div>
  </div>
</section>

<section class="closing">
  <p class="approach">[这种 X 的研究对象, 叫——]</p>
  <h1 class="mega-name">[中文概念名]</h1>
  <div class="en-name">[English Name]</div>
  <div class="byline"><span><strong>[人名]</strong></span><span class="sep">·</span><span>[年份]</span><span class="sep">·</span><span>[文献]</span></div>
  <div class="closing-body"><p>[它打开了什么]</p><p>[它换了什么眼睛]</p></div>
  <p class="epilogue">[诗意余韵, 不元自指]</p>
</section>
```

**字号与节奏 padding 对照**：

| section | padding 上 / 下 | margin-top | 留白尺度 |
|---|---|---|---|
| feature | 38 / 44 | — | 中 |
| note | 22 / 22 | 24 | 小 |
| archive | 22 / 24 | 24 | 小 |
| cross | 64 / 60 | 30 | 大 |
| hero | 52 / 48 | 32 | 中偏小 |
| closing | 60 / 64 | 32 | 大 |

参考完整 CSS 见同目录 `example.html`（每个 class 都已实现）。

【输出契约】

输出**单文件 HTML**, inline CSS + Google Fonts CDN（Noto Serif SC / Noto Sans SC / Caveat / JetBrains Mono）。不写 JS, 静态长图。容器宽 1080px, 高度自适应。

【自检 6 项 — 任一不过, 重做】

1. **问题站**: 标题没出现概念名 / 问题具体可触摸 / "他/她那一刻"视角
2. **失败站**: 至少 1 次失败 / 失败有线索（删除线 / verdict / footnote）
3. **顿悟前命名后**: 命名只在 closing / hero 标题不剧透
4. **文字克制**: 没有"你以为你刚才……"自指句式
5. **中文母语**: 没有"被 X""进行 X""随着 X 的发展"等翻译腔
6. **节奏不均匀**: 6 节 margin-top 不全等 / 留白集中在 cross 与 closing

【禁区】
- 标题不能出现概念名（剧透）
- 不要把图标 / emoji 当装饰
- 不要 #000 纯黑
- 不要居中所有标题（feature/note/archive 左对齐 / cross/closing 才居中）
- 不要让 6 节 padding 一致
- 不要 Inter 字体
- 不要点题元自指
- sidekick 不能空

【致谢】
本 skill 改编自 [lijigang/ljg-skills · ljg-card -v sketchnote](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-card)（v2.3.0）。原版输出 PNG（playwright 截图）, html-anything 版直接输出单文件 HTML, 6 公理 + 6 layout + 4 字族 + 节奏与原版一致。

## blog-post

【模板: 博客长文 / Blog Post】
【意图】≥ 600 字的真正的长文章, 排版以 typography 为主, 70% 文字 20% 图 10% chrome。
【布局】
- Masthead (publication name + date)
- Hero (大标题 + 副标 + 作者署名 + 阅读时间)
- 正文 (单栏 65ch, 含 figures, pull quotes, 行内引用)
- Author bio 卡片
- Related posts (3 张卡)
【设计细节】
- Pull quote 用大号 serif 斜体 + 左侧色条
- Figures 自带 caption (italic, smaller)
- 代码块: 圆角 + 深色 + 语言标签

## competitive-teardown

【模板: 竞品拆解 / Competitive Teardown】
【意图】这不是文章、不是 PRD、不是 pitch deck。目标是把多个竞品的杂乱资料转成一份可决策的产品战略报告, 帮团队回答: "我们和它们到底差在哪里, 下一步该怎么打?"

【适合输入】
- 竞品官网 / 定价页 / changelog / 用户评论 / 销售反馈 / 内部调研笔记
- 2-6 个竞品最合适; 如果用户只给一个竞品, 输出单竞品 deep dive
- 可以包含表格、bullet、链接摘录、访谈记录、截图说明

【必须输出的结构】
1. Header: 市场 / 产品类别 / 报告日期 / 结论一句话。
2. Executive takeaway: 3 条最重要判断, 每条必须包含 "so what"。
3. Positioning map: 用 2×2 象限或坐标图表现竞品定位。坐标轴必须来自用户内容, 不要套模板词。
4. Competitor cards: 每个竞品一张卡, 包含 target user、core promise、pricing signal、primary strength、visible weakness。
5. Feature matrix: 行是关键能力, 列是竞品 + "Us / Opportunity"; 用 ✓ / △ / — 表达覆盖度, 并用短注释说明。
6. Pricing / packaging read: 价格层级、免费试用、限制项、企业销售动作。
7. UX / messaging notes: 从用户材料中抽取 4-6 条可观察细节, 不要泛泛而谈。
8. Opportunity windows: 3 个机会窗口, 每个包含 why now、target segment、first move、risk。
9. Recommended moves: 近期 30 天 / 90 天 / 180 天行动建议。

【设计要求】
- 战略咨询 + 产品战情室风格: 信息密度高、扫描快、图表清楚。
- 使用 restrained palette: ink / paper / muted blue / signal amber 或类似专业色。
- Feature matrix 必须横向可读; 小屏可变成 stacked cards。
- 不要做成营销落地页, 不要做成普通文章。

【可选风格模板 — 参考 assets/】
根据用户内容选择最贴合的一种, 不要三种混用:
- `assets/war-room-grid.html`: 默认风格。浅色战情室 / 咨询报告, 适合产品团队、PM、普通商业读者。
- `assets/radar-map.html`: 深色雷达图 / market intelligence console, 适合安全、AI、开发者工具、平台型竞品。
- `assets/analyst-dossier.html`: 纸质分析档案 / investment research dossier, 适合投研、行业分析、正式战略备忘。

如果用户没有指定风格, 优先使用 `war-room-grid`; 如果输入强调市场格局、技术雷达、攻防态势, 使用 `radar-map`; 如果输入像研究笔记、投资备忘或行业报告, 使用 `analyst-dossier`。

【内容真实性】
- 只使用用户提供的竞品、价格、功能、评论。缺失信息用 "not found in source" 或 "unknown" 标注。
- 不要发明市场份额、ARR、客户名、定价数字。
- 如果用户资料明显不足, 仍然输出报告, 但在 "Evidence gaps" 中列出缺口。

## dating-web

【模板: 社区 / 配对 Dashboard】
【意图】消费产品感的数据墙, editorial typography + 克制的高亮色。
【布局】
- Left rail 导航
- Ticker bar 实时信号
- Headline KPIs
- 30-day mutual-matches 柱状图
- Match-rate 趋势 block

## digital-eguide

【模板: 电子指南双页预览】
【意图】creator brand 的 lead-magnet 风格, 一封面一内页跨页排列。
【布局】
- Page 1 封面: display title + 作者 + 'What's inside' 数据 + TOC teaser
- Page 2 内页: lesson body + pull-quote + step list
【设计细节】
- lifestyle / creator brand 调子, 柔和米色
- 两页 side-by-side 横向, 像翻开的书

## doc-kami-parchment

【模板: Kami 羊皮纸文档】
【意图】严肃排版文档: one-pager / 长报告 / 信函 / 简历 / 财报 / changelog / portfolio。Inspired by tw93/kami。强调"写得像被排过版的纸", 不是 dashboard, 不是网页。

【硬性视觉签名 — 不许改】
- **画布**: 暖羊皮纸 `#f5f4ed` (永远不用纯白 `#fff`)。次级背景 `#efeee5`。
- **墨色**: 主文字 `#1f1d18` (近黑暖灰, 不用纯黑 `#000`)。次文字 `#6b665b`。
- **唯一色彩**: 墨蓝 `#1B365D` ——所有 accent (链接、tag 描边、重点数字、引用左 rule) 只能用这一个色, 严禁多色。
- **字体**: 一种语言一种衬线, 全文不混用:
  - 英文: `Charter` (fallback: `Source Serif Pro`, `Iowan Old Style`)
  - 中文: `TsangerJinKai02 W04` (fallback: `Noto Serif SC`)
  - 日文: `YuMincho` (fallback: `Noto Serif JP`)
  - Body 400, Heading 500 (不要 700/800/900)。
- **行高**: 标题 1.1–1.3, 紧凑正文 1.4–1.45, 阅读型正文 1.5–1.55。
- **绝不**: drop-shadow / blur / 圆角 ≥ 8px / 渐变 / 霓虹色 / rgba (用 solid hex)。
- **细节**: tag 用 solid hex 背景方块 (因为 WeasyPrint 不渲染 rgba 好); 单线几何 icon; 边缘 1px hairline `#d4d1c5` rule, 长度受控不到边。

【可选文档类型 — 按用户内容判断】
- **One-Pager** — 顶 logotype (Charter italic) + 标题 + lede + 3 列要点 + 底脚 metadata。
- **Long Doc** — 封面页 (大标题 + 副标 + 作者 + 日期) → 目录 (kicker + page no.) → 章节 (folio 顶角 + section rule + body) → 注释脚注 + 文末 colophon。
- **Letter** — 抬头地址 + 日期 + 收件人 + 正文 (左对齐, 段间空 1.5em) + 署名 + 签名占位线。
- **Portfolio** — 项目 hero (大标题 + sub) + 1 张全幅图 (用 CSS 块绘制占位) + 项目描述 + 角色 / 时间 / stack 元数据 row。
- **Resume** — 顶部姓名 (大字) + tagline 一行 + contact row + 主要 section: experience (公司 / 时间 / 职位 / bullets) + skills + education。
- **Slides** — keynote 风, 页数由【用户内容】决定 (短内容 6 页起步, 长内容应更多), 每页满铺羊皮纸, 大标题 + lede + 角标 page no., 简洁到只有"被印出来"的感觉。
- **Equity Report** — 公司名 + ticker + Q × 年份 + key metrics row (revenue / margin / yoy) + body 分析 + 图表 (SVG 单色折线)。
- **Changelog** — 版本号 (Charter italic 大字) + 日期 + 改动列表 (Added / Changed / Fixed), 单 rule 分隔。

【设计准则】
- "Composed pages, not dashboards." 不要堆 KPI 卡, 不要堆 emoji 图标, 不要 hero gradient。
- "Ring or whisper only, no hard drop shadows." 阴影只能是 `0 0 0 1px #d4d1c5` 这种 hairline 描边。
- 文字层级靠**衬线对比 + 字号 + 留白**, 不靠颜色。
- 单文件 HTML, 用 Tailwind CDN; 全文中英混排时加盘古之白; 不要外链图片, 占位用 paper-tint 色块 + 1px ink 描边。

## eng-runbook

【模板: Engineering Runbook】
【意图】工程 oncall 用的可拷贝命令的 runbook 单页。
【布局】
- Service overview (拓扑 + 依赖)
- Alerts table (severity / threshold / runbook link)
- Dashboards links 卡片
- Common procedures (mono 代码块, 一键复制)
- On-call rotation (本周 + 下周)
- Incident response checklist

## exec-briefing-memo

【模板: 高管决策简报 / Executive Briefing Memo】
【意图】这不是会议纪要、不是周报、不是 PRD。它的唯一目标是帮助决策者在 3 分钟内理解问题并拍板。

【适合输入】
- 长会议记录、调研材料、战略讨论、销售反馈、产品数据、投资备忘
- 用户可能给很多碎片信息; 你要提炼成一个明确 decision frame

【必须输出的结构】
1. Memo header: 主题、owner、audience、date、decision deadline。
2. Decision needed: 用一句话写清楚需要拍板的问题。
3. Recommendation: 明确建议, 不要写 "可以考虑"。必须包含 confidence level。
4. Why now: 为什么现在需要决定, 不决定的代价是什么。
5. Key facts: 5-7 个事实证据, 每条标注来源类型 (sales / product / finance / customer / ops)。
6. Tradeoff table: Option A / Option B / Option C, 对比 upside、cost、risk、reversibility。
7. Risks & mitigations: 3-5 个风险, 每个给缓解动作。
8. Decision path: approve / reject / ask for more evidence 三种路径各自下一步。
9. Next actions: owner、due date、expected artifact。

【设计要求】
- 像顶级咨询公司的 one-page decision memo: 克制、清楚、密度高。
- 首屏必须直接呈现 decision + recommendation, 不要先铺陈背景。
- 使用强层级: 大号结论、紧凑证据卡、对比表、状态 pill。
- 不要做成长文章; 不要做成 deck; 不要写空泛商业黑话。

【可选风格模板 — 参考 assets/】
根据决策场景选择一种, 不要三种混用:
- `assets/board-memo.html`: 默认风格。浅色高管 memo, 适合 CEO/CFO/CRO、运营、产品决策。
- `assets/decision-command.html`: 深色 command center, 适合紧急决策、风险处置、incident、go/no-go、launch gate。
- `assets/board-paper.html`: 正式 board paper / 董事会纸质议案, 适合董事会、投资人、合规、预算审批。

如果用户没有指定风格, 优先使用 `board-memo`; 如果材料强调紧急、风险、行动指挥, 使用 `decision-command`; 如果材料面向董事会或正式审批, 使用 `board-paper`。

【内容真实性】
- 不要捏造数字、客户、预算、日期。
- 如果缺少关键信息, 在 Evidence gaps 中列出, 但仍给出基于现有证据的 provisional recommendation。

## experiment-readout

【模板: 实验复盘 / Experiment Readout】
【意图】这不是普通数据报告、不是 dashboard。目标是回答: "这个实验说明了什么, 我们下一步应该上线、停止、继续跑, 还是重新设计?"

【适合输入】
- A/B test、增长实验、定价实验、onboarding 改版、功能灰度、邮件实验
- 可以是 markdown、CSV、表格粘贴或混合记录

【必须输出的结构】
1. Header: 实验名称、owner、日期、实验状态、decision。
2. Hypothesis: 原始假设, 必须改写成可验证句式。
3. Setup: audience、variant、duration、sample size、primary metric、guardrail metrics。
4. Result snapshot: primary metric lift、absolute delta、sample、confidence / caveat。
5. Metric table: Control vs Variant, primary + secondary + guardrail。
6. Interpretation: 解释结果为什么发生, 区分 signal、noise、unknown。
7. Decision: Ship / iterate / extend / stop 四选一, 并给理由。
8. Follow-up experiments: 2-4 个下一步实验, 每个包含 hypothesis、expected impact、effort。
9. Instrumentation notes: 数据缺口、埋点问题、样本偏差。

【设计要求】
- 产品数据团队风格: 清楚、可信、行动导向。
- 首屏必须有大号 decision badge 和 primary metric delta。
- 图表可以用 CSS/SVG/Chart.js; 如果用 Chart.js, canvas 外层必须固定高度。
- 不要把结果包装得过度确定; 小样本或缺少显著性时必须明确 caveat。

【可选风格模板 — 参考 assets/】
根据实验语境选择一种, 不要三种混用:
- `assets/product-readout.html`: 默认风格。浅色产品实验复盘, 适合 PM / growth / leadership readout。
- `assets/lab-notebook.html`: 研究实验室 notebook, 适合 early-stage experiment、定性 + 定量混合、需要保留 caveat 的探索实验。
- `assets/growth-console.html`: 深色 growth analytics console, 适合增长团队、实时指标、漏斗 / activation / conversion readout。

如果用户没有指定风格, 优先使用 `product-readout`; 如果材料强调研究过程和不确定性, 使用 `lab-notebook`; 如果材料强调增长指标、漏斗、实时监控或运营节奏, 使用 `growth-console`。

【内容真实性】
- 只使用用户提供的数据。不要捏造 p-value、confidence、样本量。
- 如果没有统计显著性信息, 用 "directional" / "inconclusive" / "needs more data" 表达。

## frame-data-chart-nyt

【模板: NYT 风数据图表帧】
【意图】把一段数据 (CSV / JSON / 一句结论) 做成《纽约时报》专栏感的单帧/动画图表, 适合视频片段或推特卡。Inspired by hyperframes data-chart。

【画布】1920×1080, 暖白底 `#f7f5ee` 或墨黑底 `#0e0e0e` 二选一; 文字色和背景相反。

【布局】
- **顶部 kicker** (11px uppercase letterspace 0.14em, 颜色 = accent 红 `#a91d1d` 或 mint `#5fb38a`): 数据来源 + 类目, 如 "GLOBAL · WEEKLY ACTIVE USERS · 2018–2026"。
- **大字标题** (Cheltenham / Playfair / Source Serif Pro, 5.6vw, italic 副标可选): 一句结论。**结论必须从用户数据中提炼**, 不是描述图。
- **图表区** (占画布 55-65%):
  - 折线: 1-2 条线, 主线 ink 实心 2.5px, 次线 dashed 1.5px; 数据点用 6px 实心圆; 关键点旁标注 `2024 · 412M` 黑色 mono 小字。
  - 柱状: 全部 ink 单色或加 1 道 accent 高亮柱; 柱顶大数字; 柱底类目斜体 (Cheltenham italic)。
  - 范围带 (range band): 浅灰填充 `#e6e2d2` 包络 + 中线 ink。
- **底部 source + footnote** (10px mono, opacity 0.6): "Source: 用户数据 · Chart by html-anything"。
- **错峰揭示动画**: 标题 fade-in (0s), kicker (200ms), 折线 stroke-dashoffset 1.2s ease-out (400ms), 数据标签依次 100ms 间隔。可被 `prefers-reduced-motion` 关闭。

【设计细节】
- **绝不**: 使用 chart.js / d3 库 (除非 jsdelivr CDN 引入); 推荐手写 SVG, 不超过 80 行 inline。
- 字体: 标题 `Source Serif Pro` 或 `Cheltenham` (无则用 `Playfair Display`); body `IBM Plex Sans` 或 `Inter`; 数据标签 `IBM Plex Mono`。
- 1 个主色 (ink) + 1 个 accent (NYT red `#a91d1d` / 编辑 mint `#5fb38a` / 暖橙 `#d97757` 三选一)。
- Y 轴刻度仅 hairline + 3-4 个 tick, 标签在轴外侧 mono 字。
- 严禁 grid 全屏铺线、阴影、3D 立体柱; 严禁 emoji。
- 必须用用户提供的数据。如果输入是文本结论, 自动估算合理坐标 (但要标注 "schematic"); 如果是 CSV/JSON, 直接绘制。
- 单文件 HTML; 数据点旁注释格式: `<text class="annot">2024 · 412M</text>`。

## frame-flowchart-sticky

【模板: 便利贴流程图帧 (Sticky Flowchart)】
【意图】把一个流程 / 系统 / 工作流画成"白板 + 便利贴"的样子, 适合 onboarding 视频、运营流程说明、系统架构讲解。Inspired by hyperframes flowchart。

【画布】1920×1080。背景: 米黄白板纸 `#f4ede1` 或冷灰白板 `#f0f2f4`; 加非常浅的 hex grid `rgba(0,0,0,0.04)` 让它有白板感。

【节点 (Sticky Notes)】
- 每节点 = 一张 240×180px 便利贴, 4 套颜色随机分配: 黄 `#fcd34d` / 桃 `#fca5a5` / 薄荷 `#a7f3d0` / 天 `#a5b4fc`。
- 便利贴有轻微旋转 `transform: rotate(±2deg)` 不一致, 投影 `drop-shadow(0 6px 14px rgba(0,0,0,0.12))`, 顶部胶带 `linear-gradient(...)` 装饰。
- 节点内容: 1 个 emoji 或单线 SVG icon + 大字标题 (16-20px) + 一行描述 (12px)。
- 节点字体: `Kalam` / `Caveat` / `Patrick Hand` 手写感字体 (中文用 `霞鹜文楷` 或 `LXGW WenKai Screen`)。

【连接线 (SVG)】
- 用 `<path>` Bezier 曲线连接节点, stroke `#2a2a2a`, width 2.5, `stroke-linecap: round`, `stroke-dasharray: 0` (实线) 或 `8 6` (虚线 = 条件分支)。
- 箭头终端用 `marker-end`, 黑色三角小箭头。
- 复杂节点可有循环或分支: 同一节点连出 2 条 (分叉) 或 2 条进入一节点 (合并)。

【可选交互】
- 顶部 caption (sans, 12px uppercase): "FLOW · MIGRATION · 2026"。
- 鼠标 hover 节点: 抬起阴影 + scale 1.05, 用 CSS transition。
- 一个"光标"装饰 (`<svg>` arrow + name tag), 浮在某节点旁, 模拟 figma 协作光标。

【设计细节】
- 至少 5 个节点, 最多 12 个。
- 节点排布不要全部居中对齐, 要有一点白板风的"随手贴"感, 但保证连接线清晰不交叉。
- 严禁: 全屏深色背景、霓虹色、企业 dashboard 风格。
- 字体不能用 Inter / 衬线, 必须手写感。
- 单文件 HTML, 不要外部图标库 (用 inline SVG)。
- 必须用用户的真实流程内容; 节点文字直接来自用户输入。

## frame-glitch-title

【模板: 故障艺术标题帧 (Glitch Title)】
【意图】单帧 hero / 视频转场 / cyberpunk 风格标题。Inspired by hyperframes glitch。

【画布】1920×1080, 背景 `#070708` 近黑或 CRT 暗灰 `#0d0e10`; 加 56px 网格 (透明 5%) + scanlines 横线 (透明 8%, 2px 间隔)。

【主标题】
- 居中, 6-9vw, weight 800/900, 字体 `Space Grotesk Bold` / `Inter Tight Black` / `JetBrains Mono Bold`。
- 颜色: 主层 `#f5f5f7`; 后面套 2 层伪影:
  - cyan `#00f0ff` translate(`-3px`, `1px`)。
  - magenta `#ff2bd6` translate(`3px`, `-1px`)。
- 整层加 clip-path 切片 5-8 段, 每段 `@keyframes` 随机 translateX -10px → 10px, 持续 80-160ms, 错峰播放, 营造 "data corruption" 像散。
- 每隔 1.5s 触发一次"重故障" — 整个标题被 horizontal smear 1 frame, 用 `filter: url(#displacementFilter)` 或简单 CSS 平移。

【附加层】
- 顶部一行 caption (uppercase mono, 11px, opacity 0.6): `>> SIGNAL_LOST · CH-04 · 14:32:08`。
- 标题下面 1 行副标 (24-28px, mono, opacity 0.7), 偶发被 ` ̶▒̶` 字符替换 (假乱码)。
- 角落随机点缀 `█▓▒░` ASCII 噪点 chunks。
- 底部 timecode (mono, opacity 0.4)。
- 整画面叠 noise grain 层 `background-image: url("data:image/svg+xml,...turbulence...")`, opacity 6%, mix-blend-mode overlay。

【SVG 滤镜 (可选)】
- 定义 `<filter id="rgbShift">` 用 `feColorMatrix` + `feOffset` + `feMerge` 把 R/G/B 三通道偏移; 整层 `filter: url(#rgbShift)` 在故障瞬间应用。

【设计细节】
- 颜色仅用: 黑 / 白 / cyan / magenta / 一点 amber 警告色; 严禁全彩虹。
- 字体: 西文 `Space Grotesk` 或 `JetBrains Mono` Bold; 中文 `Noto Sans Mono CJK SC` 或 `Noto Sans SC` Bold。
- 严禁 lorem ipsum; 必须用用户的标题 + 副标。
- 动效用 `@keyframes`, 可被 `prefers-reduced-motion` 关闭 (退回静态 chromatic split)。
- 单文件 HTML。

## frame-light-leak-cinema

【模板: 胶片漏光电影帧】
【意图】纪录片 / 个人短片 / 视频章节卡的开场单帧 —— 暖橙漏光 + 35mm 颗粒 + 衬线大字, 古典胶片质感。Inspired by hyperframes light-leak。

【画布】
- **2.39:1 letterbox** (推荐): 1920×800, 上下黑边各 140px (`#000`)。
- 或 16:9: 1920×1080, 无 letterbox。

【背景】
- 底层: 深暖色 (深红棕 `#1a0d08` / 墨绿 `#0a1410` / 蓝紫 `#0d0e1a`) 或场景描绘 (CSS gradient 模拟天空 / 室内 / 室外)。
- **胶片漏光 (Light Leak)**: 2-3 个大 `radial-gradient(ellipse at top right, #ffb547 0%, transparent 50%)` + 1 个底部 `linear-gradient(to top, #d97757 0%, transparent 30%)`; 颜色取暖橙 / 桃 / 玫红 / 暗黄, **不要冷蓝**。
- **35mm Grain**: 全屏覆盖 SVG turbulence noise 图层, opacity 14%, `mix-blend-mode: overlay`; 也可用 `background-image: url("data:image/svg+xml,...feTurbulence...")`。
- 可选: 1 道 `feDisplacementMap` 模拟胶片摆动 (慎用)。

【文字】
- 中央或左下: 大字衬线 (Source Serif Pro / Playfair Display / EB Garamond) 5-8vw, weight 500 italic; 颜色暖白 `#f5e9d6` 或 cream。
- 副标 (24-28px) 一行, opacity 0.7, 同样衬线。
- 角落 caption (uppercase letterspace 0.18em, 10-11px, mono, opacity 0.5): "REEL 03 · CH I · 1985"。
- 底部 timecode + 拍摄地 + 日期 (mono, opacity 0.4)。

【可选附加】
- "胶片划痕": 几条 1-2px 竖向白线, opacity 0.2, 不规则间距 (用 `box-shadow` 多重 inset 或多个 `<div>`)。
- "胶片齿孔": letterbox 黑边内, 等距小白方块 (CSS repeating-linear-gradient)。
- 入场动效: 整画面从 underexposed (brightness 0.3) → normal, 800ms 内; 漏光位置缓慢漂移 12s 一个周期。

【设计细节】
- 颜色绝不超过 4 个色相 (深背景 + 2 个暖漏光色 + 文字 cream)。
- 严禁: 蓝紫漏光 (违反胶片质感)、emoji、霓虹色、几何 dashboard 装饰。
- 中文: `Noto Serif SC` italic 不存在 → 用 `Noto Serif SC` regular + 字距加大。
- 必须用用户提供的标题; 自动估算合理"年份 / 章节 / 地点" 元数据 (但来源用户内容)。
- 单文件 HTML, 用 `prefers-reduced-motion` 关动效。

## frame-liquid-bg-hero

【模板: 流体背景 Hero】
【意图】可作为视频片头帧、SaaS landing 顶部 hero、海报底图。WebGL 流体感, 但用 CSS / canvas 退化绘制, 确保单文件可双击打开。Inspired by hyperframes vfx-liquid-background。

【画布】1920×1080 (横) 或 1080×1920 (竖), 二选一。背景占满。

【流体背景 — 3 种实现, 按用户偏好选】
1. **CSS 多层 radial-gradient 错位呼吸** (最稳, 默认推荐):
   - 3-5 个大椭圆 `radial-gradient(...)`, 颜色取自调色板。
   - 每个椭圆套 `@keyframes` 平移 + scale + hue-rotate, 周期 8-14s, 错峰; 整个画面叠 `mix-blend-mode: screen` 或 `overlay`。
   - 顶层加 1 层 `backdrop-filter: blur(80px)` 让边缘更糊。
2. **Canvas + simple perlin noise** (中阶):
   - 80 行 inline JS, 用 `requestAnimationFrame` 画 metaballs 或 simplex noise field。
   - 性能允许时启用, `prefers-reduced-motion` 时降回静态截图。
3. **WebGL fragment shader** (高阶, 慎用):
   - 用 jsdelivr CDN 引 `regl` 或 inline plain WebGL。
   - shader 写 domain-warp noise; 单个 quad, 一个 uniform `u_time`。

【顶层文字层】
- 居中或左下: 一句巨型金句 (5-7vw, 衬线或粗 sans), 字体: `Source Serif Pro` / `Inter Tight` / `Manrope Black`。
- 文字色用 paper white `#fafaf8` 或 ink, 取决于背景明暗; 加 `mix-blend-mode: difference` 让它在任何流体颜色上都可读。
- 副标 (小 sans, opacity 0.7) 一行。
- 底部可选 CTA chip 或 hairline + 元数据 row。

【调色 — 4 选 1, 不要彩虹】
- 🌅 **Solar Peach** — `#ffb18a` + `#f78b4c` + `#d97757`, 暖橙桃。
- 🌊 **Ocean Aqua** — `#5ac8fa` + `#0a84ff` + `#1e3a8a`, 海蓝。
- 🌌 **Aurora Violet** — `#a78bfa` + `#7c5cff` + `#1e1b4b`, 极光紫。
- 🌿 **Forest Mint** — `#86efac` + `#34d399` + `#065f46`, 苔森林。

【设计细节】
- 严禁: 多色彩虹 (>4 个色相)、PowerPoint 渐变、霓虹荧光叠加。
- 字体: 中文用 `Noto Serif SC` (display) / `Noto Sans SC` (副标)。
- 严禁外链图片; 全部 CSS + SVG + 可选 canvas。
- 必须用用户提供的金句 / 标题; 如果用户输入是数据 → 提炼一句 ≤ 18 字的金句。
- 单文件 HTML, 可被 `prefers-reduced-motion` 关动效。

## frame-logo-outro

【模板: Logo 收尾帧 (Logo Outro)】
【意图】视频结尾的品牌 reveal 帧 —— logo 分块拼装 + glow bloom + tagline 上浮 + CTA。Inspired by hyperframes logo-outro。

【画布】1920×1080, 黑色 `#08090c` 或品牌深色背景; 加微妙 vignette `radial-gradient(...)` 让中心更亮。

【布局】
- **中心 Logo**: 用 CSS / 内联 SVG 绘制; 由 4-8 个几何块 (圆 / 方 / 三角 / hairline) 组成。
  - 入场动画: 每个块从屏幕外滑入 (±100px 不同方向) + scale 1.4→1.0 + opacity 0→1, 错峰 80ms; 总时长 1.2s。
  - 入场完成后, 整个 logo 加 glow bloom: `filter: drop-shadow(0 0 24px <accent>40)`; 同时一道 shimmer `mask-image` 横扫 logo (500ms)。
- **品牌名**: logo 下方 6-8% 位置, 大字 (Inter Tight / SF Pro Display, 48-72px, weight 700, letter-spacing -0.02em), 入场: typewriter or fade-up after logo bloom (1.4s 开始)。
- **Tagline**: 品牌名下方一行 (24-28px, weight 400, opacity 0.7), fade in (1.8s)。
- **底部 CTA + 元数据**: 双行底部 row, 例如 `htmlanything.dev · @htmlanything · 2026`, 11px uppercase letter-spacing 0.16em, 颜色 opacity 0.4, hairline 分隔。

【调色 — 4 选 1, 不混用】
- 🌌 **Midnight Indigo** — bg `#08090c`, accent `#7c5cff` (霓虹紫蓝 glow)。
- 🌅 **Solar Amber** — bg `#0e0a08`, accent `#ffb547` (暖琥珀)。
- 🌿 **Forest Mint** — bg `#0a1410`, accent `#5fb38a` (薄荷绿)。
- ⚪ **Bone & Ink** — bg `#f1efea`, accent `#0a0a0b` (无 neon, 走 editorial 风, glow 改成阴影)。

【设计细节】
- **绝不**: 用外链 logo 图片; logo 必须用纯 CSS / 内联 SVG 几何绘制。
- 入场动画用 `@keyframes` + `animation-delay`; 可被 `prefers-reduced-motion` 关闭。
- 字体: 西文 `Inter Tight` / `SF Pro Display` / `Manrope`; 中文 `Noto Sans SC` weight 700。
- 必须用用户提供的品牌名 + tagline; 若没有, 跑 fallback "HTML Anything" / "Anything → beautiful HTML"。
- 单文件 HTML; 整个动画完成后 freeze (不要 loop, 这是视频结尾帧)。
- 顶部可选 5px ribbon (accent 色) 增加品牌识别。

## frame-macos-notification

【模板: macOS 通知横幅】
【意图】把一段公告 / 消息 / 提示渲染成 macOS Big Sur+ 风格的通知横幅, 适合视频角落叠加、产品发布预告、社媒图。Inspired by hyperframes macos-notification。

【画布】两种用法:
- 视频叠加 1920×1080, 通知放右上角, 周围透明。
- 单独 banner 480×120, 居中输出。

【横幅结构】
- 外框: 圆角 14px (macOS Big Sur 标准), 480×120 (或更长 480×180 含正文), 12-16px 内边距。
- 背景: **frosted glass** 效果 — `background: rgba(245,245,247,0.78)` + `backdrop-filter: blur(40px) saturate(180%)`; 暗色版 `rgba(28,28,30,0.78)`。
- 边框: 1px `rgba(0,0,0,0.06)` (light) / `rgba(255,255,255,0.08)` (dark); 顶部加 1px 亮 highlight `rgba(255,255,255,0.5)`。
- 阴影: `0 10px 40px rgba(0,0,0,0.18), 0 2px 6px rgba(0,0,0,0.08)`。

【内容】
- 左侧: **App icon** (44×44, 圆角 10px, CSS gradient + 1 个 emoji 或 monogram 字母, **不用外链图片**)。
- 中间:
  - 顶部 row: App 名 (SF Pro 13px, weight 600) + `now` 或具体时间 (12px, opacity 0.6) — 两端对齐。
  - 标题 (15px, weight 600, 1 行截断)。
  - 正文 (13px, weight 400, 1-2 行截断, line-height 1.35)。
- 右侧 (可选): action button "Open" 或 "Reply" (capsule, 浅灰底)。

【字体】
- 主: `SF Pro Text` → fallback `Inter` / `system-ui`; 中文用 `PingFang SC` / `Noto Sans SC`。

【可选附加】
- 多条通知堆叠: 第一条在前, 后面 2 条向后向下递缩 (scale 0.96 + opacity 0.6 + translateY)。
- 入场动效: 从屏幕外右侧滑入 `transform: translateX(110%)→0`, 200ms ease-out; 可被 `prefers-reduced-motion` 关闭。
- 右上角控制 chip "Clear" (hover 显示, opacity 默认 0)。

【设计细节】
- light mode 背景白磨砂, dark mode (推荐 video) 几乎黑磨砂。
- icon 不能用外链 emoji 图片, 用 unicode emoji 或 CSS 绘制几何。
- 必须用用户提供的内容; 标题 + 正文清晰来自用户输入。
- 单文件 HTML, 注意 `backdrop-filter` Safari 需要 `-webkit-` 前缀。

## gamified-app

【模板: 游戏化 App / Quest UI】
【意图】类 RPG 习惯养成 app, dark showcase stage 上三个 phone frame。
【布局】
- Frame 1: Cover / Poster
- Frame 2: Today's quests + XP ribbon + level bar
- Frame 3: Quest detail (子任务 + 奖励)
【设计细节】
- 醒目的 quest tile 渐变 + 等级 ribbon + 底部 tab bar

## hr-onboarding

【模板: 新员工入职】
【意图】新员工首周看一眼就知道怎么过的单页。
【布局】
- Welcome hero (姓名 + 入职日 + 团队)
- First-week schedule (5 天 timeline)
- Manager + Buddy 卡片
- Learning track 列表
- Equipment checklist
- “你设置好了当且仅当…” outcomes 区

## info-funnel

【模板: 漏斗信息图（Funnel Infographic）】

【意图】把"从大到小"的转化 / 筛选 / 损耗过程一眼看清。**宽顶（输入）→ 窄底（结果）**, 每一阶有明确的"剩多少"和"漏多少"。典型场景：marketing funnel（曝光→点击→注册→付费）、招聘漏斗（投递→面试→录用→入职）、决策漏斗（候选→筛选→敲定）。

【数据形态】

输入应是有序的 **3-6 个阶段** + 每阶的绝对数值（人数 / 件数 / 金额）。可选每阶名称、说明、单位。若用户只给了百分比, 默认顶端 = 100% / 10000 人。

```
阶段 1: 100,000 名访客
阶段 2:  18,500 名注册（18.5%）
阶段 3:   6,200 名启动试用（33.5%）
阶段 4:   1,450 名转付费（23.4%）
阶段 5:     920 名 30 天留存（63.4%）
```

【布局规则】

| 区域 | 内容 | 占比 |
|---|---|---|
| **Hero 顶部**（约 15%） | 标题（≤ 20 字, 22-32px CJK）+ 副标题 / 时间窗口（灰色 14-16px） | 上 15% |
| **漏斗主体**（约 65%） | 3-6 个梯形 stage, 每段含：左大数字（48-72px tabular-nums）+ 右阶段名（18-22px bold）+ 右二行说明（13-15px 灰）+ 段间小箭头标转化率 | 中 65% |
| **底部 stat strip**（约 20%） | 累计转化率（最大字号 80-120px）+ 1-2 句洞察文本（漏出最严重的环节 / 关键提示） | 下 20% |

【漏斗实现】

用 **CSS `clip-path: polygon()`** 切梯形, 不用 SVG：
- 每段 stage 是一个 `<div>`, 设固定 height（120-200px）+ 不同 clip-path
- clip-path 的左右收缩量 = 50% × `(1 - bottom_width_ratio)`, 累计每段比上一段窄
- 每段背景色用同一 hue 不同 lightness, 顶端最饱和, 底端最深（accent → ink）
- 阶段之间有 4-8px gap, 让"流动"感更明显
- 数字用 `font-variant-numeric: tabular-nums`, letter-spacing `-0.02em`

【主题色 — 三选一, 不许混】

| 主题 | 适用 | 顶端 | 底端 | ink | paper |
|---|---|---|---|---|---|
| **klein-blue**（默认） | 商业 / SaaS / AI 产品 | `#4F7BD8` | `#002FA7` | `#0A0A0A` | `#FAFAF8` |
| **sunset-amber** | 零售 / 消费 / 餐饮 | `#FBB040` | `#C73E1D` | `#0A0A0A` | `#FFF8EC` |
| **deep-forest** | 招聘 / 教育 / 健康 | `#56A06E` | `#1F4D2E` | `#0A0A0A` | `#F4F0E6` |

文字色：
- 漏斗内部数字与名字一律白色（`#FFFFFF`）
- 顶端 / 副标题 / 底部 strip 用 ink（`#0A0A0A`）
- 灰色辅助文字：`rgba(10,10,10,0.55)`

【字体栈】

```
"PingFang SC", "Heiti SC", "Helvetica Neue", "Arial", -apple-system, sans-serif
```

数字（tabular-nums 必须）：
```
"SF Mono", "JetBrains Mono", "Menlo", "Roboto Mono", monospace
```

**禁用 Inter** —— 它太"AI 默认味"。优先 PingFang SC（CJK）+ Helvetica Neue（拉丁）。

【字号 / 间距锁死】

- 主标题：`clamp(28px, 2.8vw, 36px)` font-weight 800 letter-spacing `-0.02em`
- 副标题：`14-16px` font-weight 500 ink/0.6
- 段内大数字：`clamp(48px, 5.5vw, 72px)` tabular-nums font-weight 900 white
- 段内阶段名：`20-22px` font-weight 700 white
- 段内说明：`13-15px` font-weight 400 white/0.85
- 段间转化率徽章：`13px` font-weight 700, paper 底 ink 字, 圆角 6px, padding 2px 8px
- 底部累计大数字：`clamp(80px, 12vw, 120px)` font-weight 900 ink letter-spacing `-0.04em`
- 底部洞察：`16-18px` font-weight 500 ink/0.75 max-width 80%
- 整体 padding：`6vmin 7vmin`
- 段间 gap：`6px`
- Hero 与漏斗之间 gap：`32-48px`
- 漏斗与 strip 之间 gap：`48-64px`

【输出契约】

输出**单文件 HTML**, inline CSS, **不写 JS**（静态图）。**不外链 CDN / 图标库 / 字体文件**。
- 不放图标 / 不用 emoji 装饰（漏斗本身就是图）
- 不放图表（饼图 / 柱状图）—— 一篇一个漏斗
- 不放公司 logo
- background 是 paper, 整张图占满 viewport
- 用 `aspect-ratio: 9 / 16` 锁定容器, 内容用 flex column 填充

【数据规范】

- 顶端数 = 100% 基准
- 每阶转化率 = `当前段 / 上一段`
- 累计转化率 = `末段 / 顶段`
- 数字千分位用半角逗号（10,000 不要 10000）
- 百分比保留 1 位小数（18.5% 不要 18.50% 也不要 19%）
- 单位（人 / 件 / $）放在数字后, 13-15px 灰色
- 编绝对数比写百分比更有说服力（"少了 81,500 人"比"漏掉 81.5%"更扎心）

【洞察文本（底部 strip）】

写 **1-2 句**, 总长 ≤ 60 字：
- 第一句：累计数字 + 评价（"100,000 个访客中, 只剩 920 个真正留下"）
- 第二句（可选）：指出最大漏出环节（"最大流失在『访客→注册』, 81.5% 在第一步就走了"）

禁止 AI 文案腔（"通过本图表可以看出"、"由此可见"、"综上所述"）。直接说事实。

【分阶段视觉宽度计算】

5 阶时, top_width=100%, bottom_width=30%（漏斗收口）。每段 bottom_width 比上一段窄 `(100-30)/5 = 14%`。例如：
- Stage 1: top 100% → bottom 86%
- Stage 2: top 86% → bottom 72%
- Stage 3: top 72% → bottom 58%
- Stage 4: top 58% → bottom 44%
- Stage 5: top 44% → bottom 30%

clip-path 公式（每段独立 div）：
```css
clip-path: polygon(
  {(100-top)/2}% 0%,
  {100-(100-top)/2}% 0%,
  {100-(100-bottom)/2}% 100%,
  {(100-bottom)/2}% 100%
);
```

3-4 阶时收口可以放宽到 `40-45%`, 6 阶时压到 `22-25%`。

【禁区】
- 不要在漏斗段内画图标 / 插画
- 不要把数字放在段右、名字放在左（要左数字 / 右名字, 形成视觉重力）
- 不要让段高度跟数值挂钩（这是 funnel 不是 H-bar chart, 信息密度靠宽度收缩传达）
- 不要让漏斗居中悬浮——它该填满中段, 顶部贴 Hero, 底部贴 strip
- 不要超过 6 阶（信息过载, 拆成两张图）
- 不要 3D / 阴影 / 发光（platine 干净版式）
- 不要 Inter 字体（见上）
- 不要写"以下是漏斗"、"如下图所示"之类的 meta 文字

【致谢】
本 skill 设计参考 [baoyu-skills · baoyu-infographic](https://github.com/JimLiu/baoyu-skills) 的 funnel layout 规范, 视觉补完 + HTML 实现由 html-anything 独立编写。

## invoice

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

## meeting-notes

【模板: 会议纪要】
【意图】现代会议纪要, 强 action items。
【布局】
- Title bar (会议名 + 时间 + 出席 avatars)
- Agenda checklist
- Decisions block (圆角卡片)
- Action items table (Owner / Due / Status)
- Next meeting footer

## mobile-app

【模板: iPhone 单屏 App】
【意图】一个屏幕的 mobile app 设计, 放在像素级 iPhone 15 Pro frame 里。
【布局】
- Status bar (时间 + 电池 + 信号)
- App header (标题 / 头像 / 搜索)
- Main content (一个清晰的 archetype: feed / list / detail / form)
- Bottom tab bar (4-5 tab)
【设计细节】
- 真实的 dynamic island; safe-area 留白

## mobile-onboarding

【模板: App 引导三屏】
【意图】并排展示三个 mobile onboarding 关键屏。
【布局】
- Phone 1: Splash (logo + tagline)
- Phone 2: Value-prop (illustration + 1 句 + dot indicators)
- Phone 3: Sign-in (email / Apple / Google + 主 CTA)

## mockup-device-3d

【模板: 设备 3D 展架 (Device 3D Showcase / HTML-in-Canvas)】
【意图】产品发布、App 演示、设计稿展示。把用户提供的 UI 内容真实渲染到 iPhone / MacBook "屏幕"里, 周围用 CSS 3D transform 模拟 GLTF 模型的玻璃 / 高光 / 折射。Inspired by hyperframes vfx-iphone-device。

【硬性构图】
- **画布**: 1920×1080, 暖灰渐变背景 `radial-gradient(#1a1a1f → #0a0a0f)`, 底部反射地面 (mirror gradient)。
- **iPhone 15 Pro 模型**: 左侧 / 中部, `transform: rotateY(-12deg) rotateX(4deg) translateZ(40px)`; 边框钛金属银 `#a8a8ad` (实心 4px) + 屏幕圆角 56px; 屏幕内嵌 iframe-like div, 真实渲染用户的 HTML 内容 (mobile viewport 375×812)。
- **MacBook Pro 14"** (可选第二台): 右侧, 略小, `rotateY(8deg)`; 上盖屏幕嵌入桌面 viewport 内容 (1440×900 缩放); 底座键盘 + trackpad 用 CSS 阴影线条绘制 (不画键帽细节)。
- **玻璃 / 镜头光斑**: 顶部加 2-3 个 `radial-gradient(ellipse, rgba(255,255,255,0.4) 0%, transparent 60%)` 的椭圆 highlight, 模拟 morphing glass lens。
- **地面反射**: 设备下方 `transform: scaleY(-1)` + `mask-image: linear-gradient(to bottom, rgba(0,0,0,0.4), transparent 70%)`。

【屏幕内容来源】
- 用户提供的是文本/数据 → 自动渲染为一个 mock app 界面 (顶部 status bar + 标题 + body + 底部 tab bar 或 home indicator)。
- 用户提供的是 HTML → 原样嵌入屏幕 div 内 (注意缩放 transform 让它适配屏幕宽高)。
- 屏幕内 UI 用 Tailwind, 字号要按 mobile 真实尺寸 (text-sm / text-base, 不要 text-9xl)。

【可选附加元素】
- 右下角 "product slug" 角标: 大 logo + 一行 tagline + 副标 hairline。
- 顶部一行 caption (英文 sans, 字号小, 透明 0.6): 产品 codename / 日期 / 版本。
- 加 8s 自动 CSS 转盘: `@keyframes turntable` rotateY -12 ↔ 12, ease-in-out infinite alternate; 可被 `prefers-reduced-motion` 关闭。

【设计细节】
- **绝不**: 用外部 mockup 图片 URL (任何 unsplash / dribbble link), 全部用 CSS / SVG 绘制设备。
- 字体: 设备外的 caption / logo 用 `Inter Tight` / `SF Pro` 风格; 设备内根据用户内容自适应。
- 背景可选 4 套调色: charcoal / pearl / midnight blue / mocha; 不要彩虹渐变。
- 单文件 HTML; iframe 不要用 srcdoc 嵌套 (容易出问题), 用 `<div class="screen">` + Tailwind 渲染内容。
- 必须用用户真实数据填充屏幕内容, 严禁 lorem ipsum 或 "Your text here"。

## pm-spec

【模板: PRD / Product Spec】
【意图】产品需求文档单页, 结构清晰。
【布局】
- Title bar + 状态 pill (draft/approved/shipped)
- Problem & Why now
- Success metrics (3-5 个 KPI)
- Scope (in / out)
- User stories (Given/When/Then)
- Design notes (含占位 mockup)
- Rollout plan + Open questions

## resume-modern

【模板: 现代极简简历】
- 容器宽度模拟 A4: `w-[210mm] min-h-[297mm] mx-auto`, 内边距 16-20mm。
- 顶部姓名巨大 (text-4xl), 底下一行 contact (邮箱 / 电话 / 城市 / GitHub / LinkedIn), 中间用细竖线分隔。
- 主体两栏可选: 左 60% 主线（经历/项目/教育）, 右 40% 副线（技能/语言/获奖）。
- 章节标题: small caps 风格, 上方一条短 accent 线 (w-8 h-0.5)。
- 经历每条: 公司 + 职位 + 时间区间 (右对齐), 下方 1-3 条 bullet 用动词开头。
- 不使用花哨颜色, 黑白灰 + 1 个 accent (深蓝 / 墨绿)。
- 添加 @media print 样式, 隐藏不必要的元素, 颜色保留。

## team-okrs

【模板: Team OKRs】
【意图】OKR 追踪页, 一眼看出进度。
【布局】
- Quarter banner (Q? + 主题)
- 3 个 objectives 列, 每个含一组 KR
- 每个 KR 一条进度条 + 数值 + owner avatar + 状态 pill
- 右侧 'this quarter at a glance' 摘要

## vfx-text-cursor

【模板: VFX 文字光标 (Text Cursor)】
【意图】视频开场/Hero 帧 —— 光标在画布上"打字", 文字逐字浮现, 后面拖着彩色像散尾迹 + 定向光斑。Inspired by hyperframes vfx-text-cursor。

【画布】1920×1080, 背景 `#06070a` 暗哑黑 或 `#0a0d12` (有暖偏蓝); 加微妙 vignette。

【内容】
- 一句金句 (中英不限), 居中, 字号 6-8vw, weight 700, 字体 `Inter Tight` / `Source Sans 3` / `Noto Sans SC`。
- 逐字揭示, 每个字符 80ms 间隔; 当前字符后面跟着一个 cursor `▍` (或细 vertical bar)。
- 已揭示文字默认白色 `#f5f5f7`, opacity 1; 即将揭示位置加 chromatic ghost: 一份 `text-shadow: 2px 0 #ff3b6f, -2px 0 #00d4ff` 在 reveal 瞬间, 200ms 内收敛回正常。
- 光标本身: 16px 宽矩形, 颜色 = accent (取 1: hot pink `#ff3b6f` / cyan `#00d4ff` / amber `#ffb547`), 闪烁 `@keyframes` 1.0s 周期; 后面拖一条 60-120px 的 motion blur trail (径向渐变到透明)。

【光斑 / 射线】
- 在打字位置附近随机生成 3-5 道**定向光斑** (light leak): 用 `linear-gradient(45deg, transparent, accent20, transparent)` 的细长矩形 + `mix-blend-mode: screen`, 不规则角度。
- 当文字打完, 整段文字加 0.5s shimmer sweep (光带横扫)。

【字段】
- 顶部 caption (uppercase letterspace 0.18em, 11px, opacity 0.5): "FRAME 01 · OPENING"。
- 文字底下副标 (24-28px, opacity 0.6): 来源 / 章节。
- 右下角 timecode (`00:03:21` mono)。

【设计细节】
- **绝不**: 多色彩虹 chromatic (只用 1 个 hot pink + cyan 这种二元像散, 不要 R/G/B 全色)。
- 字体: 西文 `Inter Tight` Bold; 中文 `Noto Sans SC` Bold; 严禁衬线。
- 动效用 `@keyframes` + JS 计时器 (`setTimeout` 逐字), 可被 `prefers-reduced-motion` 关闭 (直接显示所有字)。
- 必须用用户提供的金句; 不要捏造。
- 单文件 HTML, 不要外链字体以外的资源。

## weekly-update

【模板: 团队周报 Deck】
【意图】6-8 页 horizontal-swipe slides, 周报固定结构。
【布局】
- Cover (周次 + 团队 + 一句话主题)
- Shipped (列表 + owner)
- In flight (进度条)
- Blocked (红色 callout)
- Metrics (KPI 卡片网格 + 周对比)
- Asks (求助清单)
- Thanks 收尾
【设计细节】
- 键盘左右切换, hash 同步

## Provenance

Merged from 30 skills of [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`. Licence Apache-2.0 — the source text of every variant is preserved above.
