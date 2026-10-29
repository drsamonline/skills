---
name: html-deck-styles
description: HTML deck styles — 30+ art-directed slide systems. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "HTML deck styles — 30+ art-directed slide systems"
  origin: "nexu-io/html-anything"
  merged-from: "22 skills"
  category: "office-docs"
---

# HTML deck styles — 30+ art-directed slide systems

A merge of 22 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- HTML deck styles — 30+ art-directed slide systems. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `deck-blueprint` | 奶油纸 + 锈红 + 蓝图网格 mask + 黑边硬卡片 + pipeline 盒 |
| `deck-course-module` | 暖纸背景 + Playfair, 左侧学习目标常驻, 含 MCQ 自测页 |
| `deck-dir-key-nav` | 8 页单色背景, 160px display + 4px accent + Mono 箭头列表 |
| `deck-graphify-dark` | 深夜渐变 + 漂浮 orbs + SVG 力导向图谱 + JetBrains Mono |
| `deck-guizang-editorial` | 电子杂志 × 电子墨水; 10 个版面 + 5 套调色板 (墨水/靛蓝瓷/森林墨/牛皮纸/沙丘) |
| `deck-hermes-cyber` | 黑底 + CRT 网格扫描线 + $ 命令行标题 + 薄荷绿大字 + 三档 tag |
| `deck-ljg-present` | 把 outline 1:1 铸成色块大字宣言 deck, 原文不动只做美化。三档主题 black / red / yellow |
| `deck-magazine-web` | 电子杂志 × 电子墨水风, WebGL 流体背景 + 衬线 display |
| `deck-obsidian-claude` | GitHub-dark + 紫蓝环境光 + 三色渐变标题 + GitHub 风代码 |
| `deck-open-slide-canvas` | 锁死 1920×1080 画布, React 组件级自由组合, 不绑模板 |
| `deck-pitch` | 10 页融资 deck, 白底 + 蓝紫渐变 hero, traction 柱状, $X.XM ask |
| `deck-presenter-mode` | tokyo-night 默认主题, T 切换 5 主题, S 打开提词器 popup |
| `deck-product-launch` | 暗 hero + 亮内容, 橙→桃 accent, 特性卡 + 定价 + CTA |
| `deck-replit` | Replit Slides 八套主题 (helix/holm/vance/bevel/world/atlas/bluehouse) |
| `deck-safety-alert` | 红琥珀警示色 + hazard 条纹 + L1/L2/L3 tier 卡片 + 删除线标题 |
| `deck-simple` | 通用 horizontal-swipe HTML deck, 不要 magazine 调 |
| `deck-swiss-international` | 16 列网格 + 单一饱和 accent + 22 个锁死版面 (Klein Blue / Lemon / Mint / Safety Orange) |
| `deck-tech-sharing` | GitHub-dark + JetBrains Mono + 终端代码块, 含 agenda + Q&A |
| `deck-xhs-pastel` | 奶油底 + 柔光 blob + 马卡龙圆角卡片 + Playfair 斜体序号 |
| `deck-xhs-post` | 9 页 3:4 竖版图文, 暖 pastel + 虚线 sticker 卡片 |
| `deck-xhs-white` | 纯白 + 顶部彩虹 bar + 渐变文字 + 马卡龙软卡片 + 黑底 pill |
| `ppt-keynote` | 苹果 Keynote 级别幻灯片, 一屏一卡, 键盘左右切换 |

## deck-blueprint

【模板: Knowledge Arch Blueprint Deck】
【意图】认真的、印刷友好的架构 / pipeline 讲解 deck。
【布局】
- 奶油 #F0EAE0 底 + 蓝图 48px 网格 mask
- Pipeline 步骤盒 (其中一个抬高)
- 右侧锈红 #B5392A insight callout
- Playfair serif 大字 + SVG 虚线反馈环
【设计细节】
- 零渐变零软阴影

## deck-course-module

【模板: 课程 / 培训模块 Deck】
【意图】教学 / workshop 用 deck, 持续显示学习目标。
【布局】
- Cover (模块名 + 讲师)
- Learning objectives 列表 (左侧持续显示)
- 正文页 (concept + 例子)
- MCQ 自测页
- Wrap-up + 下一模块预告
【设计细节】
- warm paper bg + Playfair serif

## deck-dir-key-nav

【模板: 极简方向键 Keynote】
【意图】“有话要说但没什么可看” 的极简 keynote。
【布局】
- 页数由【用户内容】决定 (短内容 8 页起步, 长内容应更多); 每页单色背景, 从下列调色板里循环选取 (靛 / 奶 / 绛 / 翠 / 灰 / 紫 / 白 / 炭), 同色可复用
- 160px display 标题 + 4px 短粗 accent 线
- 箭头 → 前缀的 Mono 列表
- 左下 ← → kbd 提示 + 右下页码

## deck-graphify-dark

【模板: Graphify Dark Graph Deck】
【意图】AI-native / 知识图谱 / dev-tool launch deck。
【布局】
- Cover: #06060c→#0e1020 渐变 + 浮动 blur orbs + SVG 力导向 graph
- Section 页: 彩虹渐变标题
- 代码 / CLI 页: JetBrains Mono 高亮
- Glassmorphism 卡片页

## deck-guizang-editorial

【模板: 贵赞编辑墨水 Deck (Editorial × E-Ink)】
【意图】叙事、观点、分享、个人风格表达。墨纸印刷感, 不要科技感。Inspired by op7418/guizang-ppt-skill Style A。

【调色板 — 5 选 1, 严禁改 hex、严禁混用】
- 🖋 **墨水经典 Monocle** — ink `#0a0a0b`, paper `#f1efea`, paper-tint `#e8e5de`, ink-tint `#18181a`. 默认 / 通用商业 / 科技。
- 🌊 **靛蓝瓷 Indigo Porcelain** — ink `#0a1f3d`, paper `#f1f3f5`, paper-tint `#e4e8ec`, ink-tint `#152a4a`. 科技 / 研究 / 数据。
- 🌿 **森林墨 Forest Ink** — ink `#1a2e1f`, paper `#f5f1e8`, paper-tint `#ece7da`, ink-tint `#253d2c`. 自然 / 可持续 / 文化。
- 🍂 **牛皮纸 Kraft Paper** — ink `#2a1e13`, paper `#eedfc7`, paper-tint `#e0d0b6`, ink-tint `#3a2a1d`. 怀旧 / 人文 / 文学。
- 🌙 **沙丘 Dune** — ink `#1f1a14`, paper `#f0e6d2`, paper-tint `#e3d7bf`, ink-tint `#2d2620`. 艺术 / 设计 / 时尚。

【布局 — 10 个磁带式版式池, 可复用; **数量由【用户内容】决定**, 完整覆盖每个要点; 短内容 6-12 张起步, 长内容应更多 (同一版式可在不同章节重复使用)】
- **L01 Hero Cover** — 居中大字 hero typography + kicker + subtitle + lead paragraph + 底部元数据 row。
- **L02 Act Divider** — kicker + 8.5-10vw 巨大 headline + 一句引言; 章节切换可反色 (ink ↔ paper)。
- **L03 Big Numbers Grid** — 3×2 数据卡 (label / 大数字 / 注释)。
- **L04 Quote + Image** — 左 kicker + headline + body + callout; 右 16:10 图 (基线对齐 baseline 不是 top)。
- **L05 Image Grid** — 3×2 或 3×1 等高图网格 (26vh 或 22vh); 严格统一高度。
- **L06 Pipeline / Flow** — 横向编号步骤组, 每步: №X + 标题 + 描述; 支持键盘逐步推进。
- **L07 Hero Question** — 7vw 全屏单一问句, 按语义断行, 周围极简。
- **L08 Big Quote** — 5.8vw 巨大衬线引文 + 英文翻译 + 署名 + 日期。
- **L09 Before / After** — 1:1 split; 左列 opacity .55 (旧/before); 右列 full brightness (新/after)。
- **L10 Mixed Media** — 8:4 比例; 左大段文字 (kicker / headline / body / callout) + 右 3:4 竖图作辅助。

【设计细节】
- **严禁**: 渐变 / drop-shadow / 圆角 / 圆形装饰 / blur / SVG 图标库 / emoji 装饰。
- **字体**: Display 用 `Playfair Display` (英) / `Noto Serif SC` (中); Body 用 `Inter` / `Noto Sans SC`; 编号 / 数字偶尔可用 italic 衬线。
- **杂志感细节**: kicker 用 11px uppercase letterspacing 0.12em; folio 右下角 `01 / 12`; 顶部细 hairline rule + 期刊 logo / topic。
- **不许**: 数据捏造、Lorem ipsum、占位图片 URL。所有图请用纯 CSS / SVG 内联描绘 (色块 + 简笔)。
- 键盘 ← / → 切换; hash 同步; 单文件 HTML。

## deck-hermes-cyber

【模板: Hermes Cyber Terminal Deck】
【意图】CLI / agent / dev tool 测评 deck (含 trace, diff, benchmark)。
【布局】
- #0a0c10 黑底 + 56px 赛博网格 + CRT 暗角
- 窗口红绿灯 chrome + `$ prompt` 标题
- 薄荷绿 #7ed3a4 大字 + JetBrains Mono
- Stroke-only 柱状图 + blinking 光标
- 琥珀 / 绿 / 红 三档 tag

## deck-ljg-present

【模板: 宣言式演讲（Outline-Faithful）】

【意图】把用户的 outline / markdown 1:1 视觉化为色块大字 manifesto deck。**不抽提、不重写、不重排、不浓缩**——只决定每一行/每一节渲染为哪一页。审美参考：Felipe Franco / BIG STUDIOS 的 manifesto 大字海报。

【铁律 — 全部违反必须重做】
- 标题不改字, 段落不改字, 列表不改字, 顺序不重排
- 唯一允许的"动"是**物理分页**（一段太长拆成多页）
- 不抽 manifesto / 不写新句子 / 不删内容 / 不放图片图标 / 不用过渡动画
- 一篇只用一个主题色（black / red / yellow 三选一）

【outline → 页面映射】

| 输入元素 | 输出页 |
|---|---|
| `# 一级标题` | 独占 **emphasis** 封面页（accent 底色, 通常单字/单短词） |
| `## 二级标题` | 独占 **theme** 页（大字标题独占一页） |
| `### 三级标题`+ | 独占 theme 页（字号自动降一档） |
| 段落（≤30字） | 单 theme 页 |
| 段落（30-80字, 多句号） | 每句一页（medium 档） |
| 段落（>80字） | 按 ~30 字一页拆, 末尾加 `⋯` |
| `- 列表项`（≤4） | 一页全展示, indent 按嵌套深度 0/1/2 |
| 列表 5-8 项 | 拆 2 页, 每页 3-4 项, 项数接近 |
| 列表 >8 项 | 拆多页, 每页 4 项 |
| 表格 ≤6 行 | 单页 |
| 表格 >6 行 | 拆多页, 每页保留表头 |
| `**强调**` / `` `code` `` | 自动 `hl: true` |
| `---` 分隔符 | 独立 **emphasis 休止页**（空 emphasis, 纯色块） |

**首末页自动 emphasis**：文档首段（如已是 `#` 则合并）+ 文档末段 = emphasis 开场 / 收束页。一级标题就是天然的章节断点, 不要为了凑节奏强行加 emphasis。

【主题色推断 — 一篇只能一个】

| 文档调性 / 标签 | theme | 默认页 | emphasis 页 | hl 色（仅 theme 页生效） |
|---|---|---|---|---|
| 沉思 / 论证 / 笔记（默认） | **black** | 黑底白字 | 红底白字 | 红 `#E63956` |
| 宣言 / 号召 / 演讲（含 `share` / `manifesto` / `keynote` / `talk` 标签或语气） | **red** | 红底白字 | 黑底白字 | 柔金黄 `#FFE082` |
| 反讽 / 警觉 / 批判（含 `critique` / `warn` / `rant`） | **yellow** | 黄底黑字 | 黑底白字 | 红 `#E63956` |

显式覆盖：用户写"用 red / 用 yellow / 用黑底"即按指令。无任何线索时默认 black。

【视觉规范 — 数值锁死】

色板（仅 4 色, 不许改 hex）：
```
--c-black:  #1A1A1A
--c-red:    #E63956
--c-yellow: #FFD400
--c-white:  #FFFFFF
--c-gold:   #FFE082
```

字体栈（必须用 ultra-bold 900, letter-spacing `-0.05em`）：
```
"Helvetica Neue", "Arial Black", "Inter", "PingFang SC", "Heiti SC", "STHeiti", -apple-system, sans-serif
font-weight: 900
```

字号档位（按本页**最长那一行**字符数, CJK 按 1.8 计权, 多行页降一档）：

| 档位 | 字符数 | font-size |
|---|---|---|
| single | ≤2 | `clamp(320px, 80vmin, 1100px)` |
| short | 3-6 | `clamp(240px, 55vmin, 780px)` |
| medium | 7-14 | `clamp(150px, 35vmin, 480px)` |
| long | 15-26 | `clamp(100px, 22vmin, 320px)` |
| xlong | 27+ | `clamp(64px, 14vmin, 200px)` |

排版：
- padding `6vmin 7vmin`, 让大字撑满边缘
- `.lines` 块在屏幕内水平居中, 但块内每行 **left-aligned**（消除右侧空白同时保 indent 错位）
- line-height `1.05`, 行间 gap `0.15em`
- 内容垂直居中
- 页脚：左下页码（`01 / 08`）+ 右下副标题, 13px monospace, opacity 0.5, uppercase, letter-spacing `0.12em`
- emphasis 页：背景换 `--acc-bg`, 字色换 `--acc-fg`, 行内 `.hl` 自动 `color: inherit`（emphasis 整页就是高亮）
- indent 档位：0 = `0`, 1 = `7vmin`, 2 = `16vmin`

【输出契约】

输出**单文件 HTML**, 完全自包含, inline CSS + inline JS, 直接在 iframe sandbox 里能跑。骨架照下面这个模板, 把 `SLIDES` 数组、`<title>`、`{{SUBTITLE}}`、`body[data-theme]` 填好即可。**不要外链 CDN, 不要外部资源**。

SLIDES 数组每项形态：
```js
// 默认 theme 页
{ lines: [ { indent: 0, chunks: [ {t: "前段"}, {t: "高亮词", hl: true}, {t: "后段"} ] } ] }
// emphasis 页（accent 底色, inline hl 自动忽略）
{ emphasis: true, lines: [ { indent: 0, chunks: [ {t: "AI"} ] } ] }
// 休止页 = emphasis + 空 lines
{ emphasis: true, lines: [] }
```

完整 HTML 骨架（agent 应**复用 CSS 与 JS 不要改**, 只填 SLIDES / title / subtitle / data-theme）：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><!-- 文档标题 --></title>
<style>
  :root {
    --c-black: #1A1A1A; --c-red: #E63956; --c-yellow: #FFD400;
    --c-white: #FFFFFF; --c-gold: #FFE082;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    width: 100%; height: 100%;
    font-family: "Helvetica Neue", "Arial Black", "Inter", "PingFang SC", "Heiti SC", "STHeiti", -apple-system, sans-serif;
    font-weight: 900; overflow: hidden;
    -webkit-font-smoothing: antialiased;
    letter-spacing: -0.05em;
  }
  body[data-theme="black"]  { --bg: var(--c-black);  --fg: var(--c-white); --acc-bg: var(--c-red);   --acc-fg: var(--c-white); --hl: var(--c-red); }
  body[data-theme="red"]    { --bg: var(--c-red);    --fg: var(--c-white); --acc-bg: var(--c-black); --acc-fg: var(--c-white); --hl: var(--c-gold); }
  body[data-theme="yellow"] { --bg: var(--c-yellow); --fg: var(--c-black); --acc-bg: var(--c-black); --acc-fg: var(--c-white); --hl: var(--c-red); }
  body { background: var(--bg); }
  .stage { position: fixed; inset: 0; }
  .slide {
    position: absolute; inset: 0; display: none;
    flex-direction: column; justify-content: center; align-items: center;
    padding: 6vmin 7vmin;
    background: var(--bg); color: var(--fg);
  }
  .slide.active { display: flex; }
  .slide[data-emphasis="true"] { background: var(--acc-bg); color: var(--acc-fg); }
  .slide .hl { color: var(--hl); }
  .slide[data-emphasis="true"] .hl { color: inherit; }
  .lines { display: flex; flex-direction: column; gap: 0.15em; line-height: 1.05; max-width: 100%; align-items: flex-start; }
  .line { white-space: nowrap; text-align: left; }
  .line[data-indent="0"] { padding-left: 0; }
  .line[data-indent="1"] { padding-left: 7vmin; }
  .line[data-indent="2"] { padding-left: 16vmin; }
  .slide[data-len="single"] .lines { font-size: clamp(320px, 80vmin, 1100px); }
  .slide[data-len="short"]  .lines { font-size: clamp(240px, 55vmin, 780px); }
  .slide[data-len="medium"] .lines { font-size: clamp(150px, 35vmin, 480px); }
  .slide[data-len="long"]   .lines { font-size: clamp(100px, 22vmin, 320px); }
  .slide[data-len="xlong"]  .lines { font-size: clamp(64px,  14vmin, 200px); }
  .pager, .subtitle {
    position: fixed; bottom: 2.5vmin;
    font-family: "Menlo", "Monaco", monospace;
    font-size: 13px; font-weight: 400; letter-spacing: 0.12em;
    user-select: none; z-index: 10; text-transform: uppercase;
    opacity: 0.5; color: var(--fg);
  }
  .pager { left: 3vmin; }
  .subtitle { right: 3vmin; }
  body[data-current="emphasis"] .pager,
  body[data-current="emphasis"] .subtitle { color: var(--acc-fg); }
</style>
</head>
<body data-theme="red"><!-- black|red|yellow -->
<div class="stage" id="stage"></div>
<div class="pager" id="pager">01 / 01</div>
<div class="subtitle" id="subtitle"><!-- 副标题 / 品牌, 可空 --></div>
<script>
  const SLIDES = [ /* 填入按 outline 映射出的 slides 数组 */ ];
  const stage = document.getElementById('stage');
  const pager = document.getElementById('pager');
  const body = document.body;
  function lineCharLen(chunks) {
    const CJK = /[　-〿㐀-䶿一-鿿豈-﫿＀-￯]/;
    return chunks.reduce((acc, c) => {
      let len = 0;
      for (const ch of (c.t || '')) len += CJK.test(ch) ? 1.8 : 1;
      return acc + len;
    }, 0);
  }
  function maxLineLen(lines) { return lines && lines.length ? Math.max(...lines.map(l => lineCharLen(l.chunks || []))) : 0; }
  function lengthTier(maxLen, lineCount) {
    const adj = maxLen + Math.max(0, lineCount - 1) * 4;
    if (adj <= 2)  return 'single';
    if (adj <= 6)  return 'short';
    if (adj <= 14) return 'medium';
    if (adj <= 26) return 'long';
    return 'xlong';
  }
  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  SLIDES.forEach((s) => {
    const el = document.createElement('div');
    el.className = 'slide';
    if (s.emphasis) el.setAttribute('data-emphasis', 'true');
    if (s.lines && s.lines.length) {
      el.setAttribute('data-len', lengthTier(maxLineLen(s.lines), s.lines.length));
      const linesEl = document.createElement('div');
      linesEl.className = 'lines';
      s.lines.forEach(line => {
        const lineEl = document.createElement('div');
        lineEl.className = 'line';
        lineEl.setAttribute('data-indent', String(line.indent || 0));
        lineEl.innerHTML = (line.chunks || []).map(c => {
          const t = escapeHtml(c.t);
          return c.hl ? '<span class="hl">' + t + '</span>' : t;
        }).join('');
        linesEl.appendChild(lineEl);
      });
      el.appendChild(linesEl);
    }
    stage.appendChild(el);
  });
  const slides = stage.querySelectorAll('.slide');
  let idx = 0;
  function show(i) {
    if (i < 0) i = 0; if (i >= slides.length) i = slides.length - 1;
    slides[idx].classList.remove('active');
    idx = i;
    slides[idx].classList.add('active');
    pager.textContent = String(idx + 1).padStart(2, '0') + ' / ' + String(slides.length).padStart(2, '0');
    body.setAttribute('data-current', slides[idx].getAttribute('data-emphasis') === 'true' ? 'emphasis' : 'theme');
  }
  function next() { show(idx + 1); }
  function prev() { show(idx - 1); }
  document.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowRight': case ' ': case 'Enter': case 'j': case 'PageDown': e.preventDefault(); next(); break;
      case 'ArrowLeft': case 'k': case 'PageUp': e.preventDefault(); prev(); break;
      case 'Home': e.preventDefault(); show(0); break;
      case 'End': e.preventDefault(); show(slides.length - 1); break;
      case 'f': case 'F': e.preventDefault(); document.fullscreenElement ? document.exitFullscreen?.() : document.documentElement.requestFullscreen?.(); break;
    }
  });
  let touchX = null;
  document.addEventListener('touchstart', (e) => { touchX = e.touches[0].clientX; });
  document.addEventListener('touchend', (e) => {
    if (touchX == null) return;
    const dx = e.changedTouches[0].clientX - touchX;
    if (dx < -40) next(); else if (dx > 40) prev();
    touchX = null;
  });
  document.addEventListener('click', (e) => {
    if (e.target.closest('.pager,.subtitle')) return;
    const mid = window.innerWidth / 2;
    if (e.clientX > mid) next(); else prev();
  });
  show(0);
</script>
</body>
</html>
```

【调用流程 — agent 内部】
1. 读用户内容（markdown / outline / 纯文本）
2. 按上面表格做 **outline → slides 数组** 映射, 不抽提不重写
3. 推断 theme（标签 > 语气 > 默认 black）
4. 复用骨架, 替换 `<title>` / `data-theme` / `<div id="subtitle">` 内容 / `SLIDES` 数组
5. 一次性输出整个 HTML 文档

【品味准则】
- outline 是真理, skill 是渲染器
- 一级标题 = emphasis 封面（天然章节断点）
- 二级标题 = 独占 theme 页（给标题应有的重量）
- 列表错位靠 indent 0/1/2 体现嵌套深度
- `**强调**` 自动 hl
- 拆页保持视觉一致性（同源块字号/缩进对齐）
- 左对齐不居中——这是 manifesto 美学的灵魂

【禁区】
- 不抽 manifesto（不要"找钉子", 作者已经写好了 outline）
- 不写新句子、不重组顺序、不删内容
- 不放图片 / 不放图标 / 不加过渡动画
- 不在 emphasis 页用 inline hl（emphasis 整页就是高亮）
- 不混用多个 theme（一篇一个气质）
- 不擅自加 emphasis（只有一级标题 / 首末页 / 分隔符）

【致谢】
本 skill 改编自 [lijigang/ljg-skills · ljg-present](https://github.com/lijigang/ljg-skills/tree/md/skills/ljg-present)（v3.0.0）。原版输出多主题包含 cyber-hacker 模式与 PNG 投影; html-anything 版只保留 3 主题 + 单文件 HTML 输出。审美灵感继续指向 Felipe Franco / BIG STUDIOS 的 manifesto 字体海报。

## deck-magazine-web

【模板: 杂志风网页 PPT (magazine-web-ppt)】
【意图】horizontal-swipe HTML deck, 杂志 × e-ink 调。
【布局】
- Cover (衬线 display + WebGL 流体背景)
- 章节幕封页
- 数据大字报页 (一个巨数字 + 一句解释)
- 图片网格页
- 金句页 (Sunday-paper 风)
【设计细节】
- 字体: Playfair / Noto Serif SC display + Inter / 思源 sans body
- 键盘 ← / → 切换; hash 同步

## deck-obsidian-claude

【模板: Obsidian Claude Gradient Deck】
【意图】类 GitHub Blog / Linear Changelog 的开发者教程 deck。
【布局】
- GitHub-dark #0d1117 + 紫蓝 radial 环境光 + 60px 网格 mask
- 居中布局 + 紫色 pill tag
- 三色渐变标题 (#a855f7→#60a5fa→#34d399)
- GitHub 风代码 palette + 紫色左边框高亮块

## deck-open-slide-canvas

【模板: 1920 画布自由 Deck】
【意图】不想被模板束缚的场景 (个人作品集、奇特演讲、艺术 / 设计课 deck)。给一个固定 1920×1080 画布 + 极强的类型 / 调色约束, 让 agent 像写 React 组件一样按内容自由排布每一页。Inspired by 1weiho/open-slide。

【硬性技术规格】
- 画布: 每页严格 `width: 1920px; height: 1080px;` 用 `transform: scale(...)` 适配视窗 (默认 `scale(0.7)` 居中)。
- **绝对禁止 overflow**: 每页内容必须 fit in 1920×1080, 不许滚动条出现。
- 字号 type scale (px): `2xs:18 · xs:22 · sm:28 · md:36 · lg:48 · xl:64 · 2xl:88 · 3xl:120 · 4xl:160 · 5xl:220`。
- 边距 padding: 96 / 128 / 160 三档之一。
- 每页有 `<section class="slide" data-slide-id="<n>">`。

【调色板 — 每个 deck 选 1 套, 全程不改】
- 🌫 **Ash & Lime** — bg `#f1efea`, ink `#161616`, accent `#c5e803`。
- 🌌 **Sea Indigo** — bg `#0a0e1a`, ink `#f5f5f7`, accent `#5ac8fa`。
- 🧉 **Mate Mocha** — bg `#1a1411`, ink `#f5e9d6`, accent `#d97757`。
- 🌸 **Pearl Rose** — bg `#fdf6f3`, ink `#1a1015`, accent `#ff5d8f`。

【布局自由度 — 这是核心】
- 不强制模板, 每页根据**内容性质**自选布局: cover / question / quote / image-text / 三列 / 五列 / 列表 / 数据卡 / 满版图。
- 但每页**必须遵守一条规则**: 视觉重心 (visual hierarchy) 只有 1 个 — 一句金句、一个数字、一张图, 不要"什么都强调"。
- 不许塞两段平等的文字; 真要并列就上 3 列等权重网格。

【字体】
- 西文: `Inter Tight` (display) + `Inter` (body); 或 `Source Serif Pro` (editorial 风时)。
- 中文: `Noto Sans SC` (sans 风) 或 `Noto Serif SC` (editorial 风); 不混 sans + serif。
- mono: `JetBrains Mono` 给数据 / 时间戳。

【设计细节】
- 严禁 emoji 装饰 (内容里的允许); 严禁多色彩虹; accent 只用一个色。
- 严禁 SVG icon 套用 lucide / feather 等通用库 (自己写 inline SVG)。
- 加键盘 ← / → 切换 + hash 同步; 角标固定: 右下 `№N/M`, 左下 deck title。
- 必须用用户的真实内容; 严禁 lorem ipsum。
- 单文件 HTML; Tailwind CDN; 不要外链图片。

## deck-pitch

【模板: Investor Pitch Deck】
【意图】10 页投资人 ready 的 fundraising deck。
【布局】
- Cover (Logo + Tagline + Round/$Ask)
- Problem · Solution · Why Now
- Product (截图占位)
- Market size (TAM/SAM/SOM)
- Traction (柱状图大数字)
- Business model
- Go-to-market
- Team
- Ask: $4.5M-style page
- Thanks / Contact

## deck-presenter-mode

【模板: Presenter Mode Deck】
【意图】怕忘词的演讲者专用 deck, 含逐字稿 notes 与 popup teleprompter。
【布局】
- 每页 + `<aside class="notes">` 150-300 字稿
- 右下小 toolbar: T 切主题 / S 打开 popup
- Popup: CURRENT / NEXT / SCRIPT / TIMER 四张磁吸卡
【设计细节】
- 默认 tokyo-night; 共 5 套主题 (含 light)

## deck-product-launch

【模板: Product Launch Keynote】
【意图】新产品发布的 Keynote 风 deck。
【布局】
- Cover (暗背景 + 大字主题)
- Why we built this (问题)
- Introducing (产品名 + 1 张 hero shot)
- Feature cards (3-6 个)
- Pricing tiers
- CTA / Available now
【设计细节】
- accent: 暖橙→桃 渐变

## deck-replit

【模板: Replit Slides Style Deck】
【意图】Replit Slides 风的单文件 horizontal-swipe deck, 选 1 套主题不混用。
【布局】
- Pick one theme: helix / holm / vance / bevel / world-dark / world-mint / atlas / bluehouse
- Cover + agenda + N 个 content + 收尾 (N 由【用户内容】长度决定, 完整覆盖每个要点; 短内容 6-10 起步, 长内容应更多)
【设计细节】
- 每套主题有完整调色板 + 字体 + accent, 不要混用

## deck-safety-alert

【模板: Safety Alert Deck】
【意图】安全 / 风险 / 事故复盘 / red team / policy-as-code 用 deck。
【布局】
- 顶/底 45° 红黑 hazard 条纹
- 红色删除线否定标题
- L1/L2/L3 绿 / 琥珀 / 红 tier 卡片
- 圆点状态 alert box
- policy-yaml 代码块 (红左边框 + bad 关键词高亮)
- 红绿 checklist + 事故堆叠柱状图

## deck-simple

【模板: Simple Deck】
【意图】干净通用的 horizontal-swipe deck (pitch / overview / study)。
【布局】
- Cover + N 个 content 页 + 收尾 (N 由【用户内容】长度决定, 完整覆盖每个要点; 短内容 6-10 起步, 长内容应更多)
- 每页一个核心信息 + 1 张图 / 1 个图表
- 顶部 progress bar
【设计细节】
- 键盘 ← / → 切换 + hash 同步

## deck-swiss-international

【模板: 瑞士国际主义 Deck (Swiss International)】
【意图】事实、产品、分析、方法论表达。极度冷静、理性、学院派, 没有任何手绘 / 噪点 / 装饰。Inspired by op7418/guizang-ppt-skill Style B。

【主题】**只能从下面 4 套二选一, 不许混用、不许改 hex**:
- 🔵 **Klein Blue (IKB)** — accent `#002FA7`, paper `#fafaf8`, ink `#0a0a0a`. 商业 / AI / 设计场景。
- 🟡 **Lemon Yellow** — accent `#FFD500`, paper `#f7f5ee` (淡奶油), ink `#0a0a0a`. 年轻 / 零售 / 体育。文字必须用黑色 (不能白色)。
- 🟢 **Lemon Green / Neon** — accent `#C5E803`, paper `#f7f5ee`, ink `#0a0a0a`. 可持续 / 科技初创 / Gen-Z 品牌。文字必须用黑色。
- 🟠 **Safety Orange** — accent `#FF6B35`, paper `#f7f5ee`, ink `#0a0a0a`. 工业 / 汽车 / 紧急消息。文字用白色 + bold ≥ 600。

【布局 — 22 个可复用版式池, 不许新增或改造版式; **数量由内容决定**, 把【用户内容】完整覆盖完为止 (短内容 6-10 张起步, 长内容应远超此范围, 同一版式可在不同章节重复使用)】
- **S01 Cover** — 全屏 accent + ASCII 呼吸点阵 + 反白标题 + 元数据 chrome (date / № / topic)。
- **S02 Vertical Timeline** — 左侧虚线轴 + 圆点; 右侧节点 = 年份 + KPI + 描述。
- **S03 Statement** — 9.6vw 居中巨字 + 左侧大段留白 + 底部 hairline + 注释。
- **S04 Six Cells** — 2×3 网格, 每格: icon + 编号 + 短标题 + 单行描述。
- **S05 Three Sub-cards** — 左侧 hero 标题 + 右侧 3 张水平堆叠的灰色卡。
- **S06 KPI Tower** — 4 列变高蓝色柱状; 柱顶 icon; 柱底大数字 + 标签。
- **S07 H-Bar Chart** — 水平排名横条, 宽度反映数据, 末端标数字。
- **S08 Duo Compare** — 垂直分割线; 左 Before / 右 After。
- **S09 Closing Manifesto** — 左 IKB 块 + ASCII 点阵 + 宣言; 右白底 + 3 条要点。
- **S10 Dot Matrix Statement** — 居中宣言 + 角落几何点矩阵 / 圆环矩阵。
- **S11 Horizontal Timeline** — 顶部 headline, 中部 hairline 轴, 等距节点, 节点下方步骤名。
- **S12 Manifesto + Ink Banner** — 上半 headline + 解释; 下半全宽黑色横幅 + 反白小字。
- **S13 Three Forces Cards** — 左 ink hero 块; 右 3 张灰色卡, 每卡: 大数字 + 文本。
- **S14 Loop Diagram** — 左编号步骤; 右 SVG 同心环; 中心 "LOOP" 标签。
- **S15 Image Matrix + Hero Stat** — 4×3 等高卡片 (12 项) + 底部 summary 大数字 + 标签。
- **S16 Multi-card Brief** — 3×2 微卡; 主文左上, 注脚右下, 单卡 accent 高亮。
- **S17 System Diagram** — 左 headline + 3 段描述; 右 SVG 三同心圆 + 外部标签。
- **S18 Why Now** — 3 列, 每列: category label + headline + 描述 + 底部数字 (最后一列 accent)。
- **S19 Four Cards** — 顶部 accent hairline + headline + 4 张等宽卡 (元数据 / 标题 / 正文)。
- **S20 Stacked KPI Ledger** — 垂直行 + hairline 分隔; 左大数字 / 中标签 / 右 icon。
- **S21 Tech Spec Sheet** — 左标题块 / 中 3 个 KPI hairline / 右变高柱 / 底数据。
- **S22 Image Hero** — 上 60% 全宽图 + 白色标题块覆盖; 下 40% 解释 + 3 列 KPI。

【设计细节 — 绝对铁律】
- **只用直角**: 全程 `border-radius: 0`。圆角 = 立刻违反。
- **1px hairline borders**, 黑色或 accent; 严禁阴影 / 渐变 / blur。
- **16 列网格**: `grid-template-columns: repeat(16, 1fr); gap: 0`。
- **字体**: Inter Tight (Latin display) / Inter (body) / Noto Sans SC (中文) / JetBrains Mono (数据); 严禁衬线、严禁装饰字体。
- **字号极端反差**: cover 用 9.6vw display, body 14-16px, label 11px uppercase letterspacing 0.08em。
- **键盘 ← / → 切换 + hash 同步**; 角标固定: `№N/N` 右下, topic 标签左下。
- **不许编造**: 数字必须来自用户输入, 图表柱高 = 真实数据按比例。
- 输出单文件 HTML, 不用任何外部图片 URL; 装饰几何 (ASCII 矩阵 / 同心圆) 用纯 CSS 或内联 SVG。

## deck-tech-sharing

【模板: Tech Sharing Deck】
【意图】工程内部分享 / 会议 talk 的 deck。
【布局】
- Cover (议题 + 讲者 + handle)
- Agenda 页
- 正文页若干 (代码块 + 关键观点)
- Demo 页 (terminal 截图)
- Q&A 页
【设计细节】
- GitHub-dark 配色 + JetBrains Mono

## deck-xhs-pastel

【模板: 马卡龙慢生活 Deck】
【意图】生活方式 / 个人成长 / 情绪向内容用 deck。
【布局】
- 奶油 #fef8f1 底 + 三个柔光 blob
- Playfair 斜体衬线 display + sans 正文
- 28px 圆角马卡龙卡片 (桃 / 薄荷 / 天 / 紫 / 柠 / 玫)
- Playfair 斜体 01-04 序号
- SVG donut 图 + chip+page 顶栏

## deck-xhs-post

【模板: 小红书 / Instagram Carousel】
【意图】发小红书 / IG carousel 的 9 页 3:4 竖版图文。
【布局】
- Cover + N 个 content 页 + 收尾 CTA (N 由【用户内容】决定, 完整覆盖每个要点; 短内容 7 页起步, 长内容应更多, 受小红书平台单帖图片数约束建议总数 ≤ 18)
- 暖色 pastel 背景
- 虚线 sticker 卡片 + 底部页码 dots

## deck-xhs-white

【模板: 白底杂志风 Deck】
【意图】可同时发小红书图文与横版 PPT 双用的白底杂志风。
【布局】
- 纯白背景 + 顶部 10 色彩虹 bar
- 80-110px display 标题 + 紫→蓝→绿→橙→粉渐变文字
- 马卡龙软卡片组 (粉 / 紫 / 蓝 / 绿 / 橙)
- 黑底白字 .focus pill + 引用大块

## ppt-keynote

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

Merged from 22 skills of [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`. Licence Apache-2.0 — the source text of every variant is preserved above.
