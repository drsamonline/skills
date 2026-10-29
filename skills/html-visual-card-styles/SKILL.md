---
name: html-visual-card-styles
description: HTML card and poster styles — social cards, carousels, posters, motion frames. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.
license: Apache-2.0
metadata:
  title: "HTML card and poster styles — social cards, carousels, posters, motion frames"
  origin: "nexu-io/html-anything"
  merged-from: "11 skills"
  category: "media-design"
---

# HTML card and poster styles — social cards, carousels, posters, motion frames

A merge of 11 thin sibling skills that each did one small job. They are kept together because the useful decision is which variant to pick, not which file to open. Original ids are preserved as headings.

## When to use

- HTML card and poster styles — social cards, carousels, posters, motion frames. Use when the task is to produce one of these variants and you need the right starting point rather than a blank page.

## The variants

| Variant | What it is |
|---|---|
| `card-twitter` | 【模板: Twitter 分享卡】 - 容器 w-1600px h-900px, 暗色 / 亮色二选一根据内容情绪。 - 中央一句 hero 金句 (text-6xl, font-semibold, 限 2-3 行)。 - 下方作者署名 + 头像占位 + handle。 - 左上角小标签 (类型:  |
| `card-xiaohongshu` | 【模板: 小红书图文卡片】 - 输出 N 张连续卡片, 每张 w-1080px h-1440px, 用 flex 纵向排列方便整体截图也方便单张截图。N 由【用户内容】信息量决定: 短内容 3-6 张起步, 长内容应更多 (小红书平台单帖最多 18 图, 通常 9 张以内最佳); 一张卡只承载一个核 |
| `email-marketing` | 产品发布邮件, 含 masthead、hero、CTA、规格表, table-fallback |
| `magazine-poster` | Sunday-paper 风格, 大字 serif headline + 双栏正文 + 编号 sections |
| `poster-hero` | 【模板: 营销海报】 - 容器 w-1080px h-1920px mx-auto, 全屏渐变 / mesh 背景。 - 上部 30% 留白 + 一个大 emoji 或抽象几何图形。 - 中部主标题占视觉中心 (text-8xl, font-black), 一句话副标题。 - 下部信息卡片: 3-5 |
| `social-carousel` | 三张方形卡片轮播, 标题串联, 品牌 mark + 编号 |
| `social-reddit-card` | 拟真 Reddit 帖子卡 + 上下投票 + 评论数, 适合视频叠加 / 故事分享 |
| `social-spotify-card` | Spotify Now Playing 风格卡: 专辑封面 + 进度条 + 播放控制, 适配视频叠加 / 个人主页 |
| `social-x-post-card` | 拟真 X 推文卡片 + 互动数据 (likes/reposts/views), 适配视频叠加或图卡分享 |
| `sprite-animation` | 像素美术 + kinetic 字体的解说帧, 纯 CSS 循环, 可录视频 |
| `video-hyperframes` | Hyperframes / Remotion 兼容的连续帧动画, 可自动播放 |

## card-twitter

【模板: Twitter 分享卡】
- 容器 `w-[1600px] h-[900px]`, 暗色 / 亮色二选一根据内容情绪。
- 中央一句 hero 金句 (text-6xl, font-semibold, 限 2-3 行)。
- 下方作者署名 + 头像占位 + handle。
- 左上角小标签 (类型: "Insight" / "Data" / "Quote")。
- 右下角品牌水印。
- 整张卡片有微妙的纹理 (grid 网格 / noise / dot pattern)。
- 截图后可直接配推文发出, 视觉简洁有力。

## card-xiaohongshu

【模板: 小红书图文卡片】
- 输出 N 张连续卡片, 每张 `w-[1080px] h-[1440px]`, 用 flex 纵向排列方便整体截图也方便单张截图。N 由【用户内容】信息量决定: 短内容 3-6 张起步, 长内容应更多 (小红书平台单帖最多 18 图, 通常 9 张以内最佳); 一张卡只承载一个核心观点。
- 第一张是封面: 巨大的标题 + 1 行副标题 + 一个吸引人的标签 (类似 "干货预警" / "建议收藏")。
- 中间几张展开正文, 每张一个核心观点, 配 emoji + 短句 + 1-2 个例子。
- 最后一张是总结 + 行动号召 (关注 / 收藏 / 评论)。
- 配色: 选择柔和的莫兰迪色或粉色系; 元素圆润, 大量留白。
- 字号大、行距宽、对比强（小红书在手机上看, 小字根本看不清）。
- 每张卡片右下角小水印 (作者名 / 日期)。

## email-marketing

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

## magazine-poster

【模板: 杂志风海报 / Magazine Poster】
【意图】Newsprint editorial 风格的长图海报, 读起来像一篇报纸全版。
【布局】
- Dateline 顶栏 (publication / date / issue)
- Oversized serif headline (含 strike-through 词 + 斜体 accent)
- 双栏 body 正文
- 6 个编号 sections, 每个含小标题 + 1-2 段 + pull-quote
- 底部署名 + 小 ornament
【设计细节】
- 纸感: 暖灰 cream 背景 + 细 dot pattern, 黑字
- 字体: Playfair Display + IBM Plex Serif + JetBrains Mono

## poster-hero

【模板: 营销海报】
- 容器 `w-[1080px] h-[1920px] mx-auto`, 全屏渐变 / mesh 背景。
- 上部 30% 留白 + 一个大 emoji 或抽象几何图形。
- 中部主标题占视觉中心 (text-8xl, font-black), 一句话副标题。
- 下部信息卡片: 3-5 条核心要点用图标 + 短句。
- 底部右下角放品牌 / 二维码 (用 SVG 占位)。
- 使用大胆的色彩: 渐变背景 (from-violet-500 via-fuchsia-500 to-indigo-500 之类), 文字白色 + 1 个对比色高亮。
- 使用 SVG 做装饰性元素 (圆 / 三角 / 波浪 / 噪点纹理)。

## social-carousel

【模板: 三联社交轮播 / Social Carousel】
【意图】3 张 1080×1080 方形卡片, headline 跨张串联。
【布局】
- Card 1: display headline (开头) + 品牌 mark + 1/3
- Card 2: display headline (中段) + 视觉重点 + 2/3
- Card 3: display headline (结尾) + CTA + loop icon + 3/3
【设计细节】
- 颜色统一一套调色板, 卡片之间渐进切换
- 三个 headline 拼起来是完整一句话

## social-reddit-card

【模板: Reddit 帖子卡】
【意图】把一段故事 / 提问 / 段子, 渲染成 Reddit 帖子卡片, 用于视频叠加、社媒故事分享。Inspired by hyperframes reddit-post。

【画布】1280×720 (视频叠加) 或 800×600 (单卡分享); 背景透明或暗色 `#0b1416`。

【卡片结构】
- 外框: 圆角 16px, bg 白 `#ffffff` (light) 或 `#1a1a1b` (dark, 推荐 video overlay), border 1px `#edeff1` / `#343536`。
- 左侧 **vote rail** (40-56px 宽):
  - 上箭头 ▲ (16px, `#878a8c`, hover 变橙 `#ff4500`)。
  - 票数 (Inter, 17px, weight 700, 居中, 颜色: 0 灰 / 正橙 / 负蓝); 大数字用 `12.3k` 格式。
  - 下箭头 ▼ (hover 变蓝 `#7193ff`)。
- 主体区:
  - 顶部 meta row: 子版块图标 (CSS 圆形 + 字母) + `r/subreddit` (粗) + `· Posted by u/username · 3h` (小字灰)。
  - **标题** (Inter / IBM Plex Sans, 22-28px, weight 500, dark text)。
  - 内容: 16px body 或 引用块或 1 张图 (CSS 渐变占位)。
  - 底部 action row: 💬 `1.2k Comments` · 🏆 Awards · ⤴️ Share · ⋯ icon。
- 顶部右上角 Reddit Snoo logo (内联 SVG, 橙色 `#ff4500`)。

【字体】
- 主: `IBM Plex Sans` → fallback `Inter`, weight 400/500/700。
- 数字: 同主字体。
- 中文: `Noto Sans SC`。

【设计细节】
- Light mode: bg `#fff`, text `#1c1c1c`, secondary `#7c7c7c`。
- Dark mode (推荐): bg `#1a1a1b`, text `#d7dadc`, secondary `#818384`, border `#343536`。
- 票数颜色: 正 = `#ff4500`, 负 = `#7193ff`, 0 = `#878a8c`。
- 标题点击区可加微妙背景 hover。
- 严禁外链图片; 图片占位用 CSS 渐变 + 描述。
- 必须用用户提供的内容; 自动生成合理的 subreddit / username / 票数。
- 单文件 HTML; icon 内联 SVG (上下箭头、评论气泡、奖杯)。

## social-spotify-card

【模板: Spotify Now-Playing 卡】
【意图】把一首歌、一段播客、或一段个人介绍渲染成 Spotify 正在播放卡, 适合 video overlay / 个人 about page / 创作者 hero。Inspired by hyperframes spotify-card。

【画布】两个尺寸:
- 横版视频叠加: 1280×720, 卡片居中或左下角浮动。
- 紧凑横条 widget: 600×200, 可嵌入到任何 hero。

【卡片结构】
- 外框: 圆角 12-16px; bg 用专辑封面色提取的暗渐变 (e.g. `linear-gradient(135deg, #1e3264 0%, #0d1f3d 100%)`) 或 Spotify 经典 `#121212`; 边缘有 1px subtle border。
- 左侧: **专辑封面** (CSS 渐变 + 大字 monogram 或抽象几何描绘, 不能外链图片), 圆角 6px, 60-200px 方形。
- 右侧:
  - 顶部 `NOW PLAYING` (uppercase letterspace 0.14em, 11px, 绿色 `#1DB954`)。
  - **歌名 / 标题** (Inter / Spotify Circular, 22-28px, weight 700, 白色)。
  - **艺人 / 副标** (16px, weight 400, opacity 0.7)。
  - 进度条: 4px 高, 圆角, 灰色背景 + 白色 fill (`width: 38%`); 两端时间戳 `1:24 / 3:42` (mono, 11px, 灰)。
  - 控制行: ⏮ ⏯ ⏭ icon (inline SVG, 24px, 白色 fill), shuffle / repeat icon 较小。
- 右上角: Spotify logo (内联 SVG, 绿色 `#1DB954` 圆 + 三道白色波纹)。
- 可选: 右下角小型音波动效 (3 个 bar `@keyframes`)。

【字体】
- 主: `Spotify Circular` → fallback `Inter` / `Inter Tight`, weight 400 / 700。
- 数字: 同主字体, 不用 mono 太多。

【设计细节】
- Spotify 经典 dark mode: `#121212` bg, `#1DB954` accent, `#b3b3b3` secondary text。
- 若用户输入是文本/标题 → 把 "标题" 当歌名, "副标/作者" 当艺人, 估算"时长" 3:42 默认。
- 若用户输入是音乐相关 → 直接对应。
- 严禁外链图片; 封面用 CSS 渐变 + 文字 logo / 几何描绘。
- 微动效: 音波动效用 `@keyframes`, 可被 `prefers-reduced-motion` 关闭。
- 单文件 HTML。

## social-x-post-card

【模板: X (Twitter) 帖子卡】
【意图】把一段推文内容 (或用户的金句) 渲染成一张拟真度极高的 X 帖子卡片, 用于视频叠加、推特发图、知识沉淀。Inspired by hyperframes x-post。

【画布】1280×720 或 1080×1080, 暗背景 `#0f1419` 或亮背景 `#ffffff` (按 X 主题); 卡片居中, 阴影柔和。

【卡片结构】
- 外框: 圆角 16px, 1px border `#2f3336` (dark) / `#eff3f4` (light), 内边距 16px。
- 顶部 row: 头像 (48×48 圆形, 用 CSS gradient 占位) + 用户名 + handle `@username` + verified 蓝勾 + 时间 (mono, 12px, 灰)。
- 正文: 17-22px, 字重 400; 链接用 X 蓝 `#1d9bf0`; hashtag 同色; mention 同色; 段落间空 0.6em。
- 可选: 引用卡 (小卡内嵌, 灰底, 圆角 12px)。
- 可选: 1 张图 (CSS 渐变 + 描述占位, 不能外链图片), 比例 16:9, 圆角 12px。
- 互动 row: 4 个 icon + 数字 (回复 / 转推 / 引用 / 点赞), icon 用 inline SVG (X 官方风格), 灰色, hover 时变色。
- 顶部右上 X logo 单线 SVG。
- 浏览量 row: 👁️ + 数字 (小字)。

【字体】
- 西文: `Chirp` (X 的字体) → fallback `Inter` 或 `Segoe UI`。
- 中文: `Noto Sans SC` / `PingFang SC`。
- 数字: 同主字体, 不用 mono。

【设计细节】
- 配色 light: bg `#fff`, text `#0f1419`, secondary `#536471`, border `#eff3f4`, accent `#1d9bf0`。
- 配色 dark (推荐, 视频叠加用): bg `#000`, text `#e7e9ea`, secondary `#71767b`, border `#2f3336`, accent `#1d9bf0`。
- 数字格式化: 1.2K / 4.5M (不要原始 1234)。
- 内容必须来自用户输入, 不能编造推文。
- 若用户输入是数据 → 自动总结成一句"金句"推文 (≤ 280 字符)。
- 单文件 HTML; icon 内联 SVG; 不要任何外部图片 URL。
- 可选: 卡片背后加微妙径向高光 `radial-gradient(...)` 增加视频叠加的可读性。

## sprite-animation

【模板: 像素 / 8-bit 动画解说】
【意图】教育型动画的单帧海报, 纯 CSS keyframes 循环, 不用 JS。
【布局】
- Full-bleed cream stage
- Bold display year / 大字数字
- 中心一个像素艺术 mascot (SVG 或纯 CSS 绘制)
- kinetic 中文 / 日文 display 字
- 底部 timeline ribbon 一直走
【设计细节】
- 动画用 @keyframes, 不依赖 JS
- 复古调色板: 红 / 米 / 墨绿

## video-hyperframes

【模板: Hyperframes 视频帧】
- 输出 N 个连续 `<section class="frame">`, 每个 `w-[1920px] h-[1080px]`; N 由【用户内容】信息密度决定 (短脚本 6-10 帧起步, 长脚本应更多, 每帧只承载一个镜头/概念)。
- 每帧表达一个镜头/概念: 文字 + 视觉构图 (中央构图 / 黄金分割 / 三分法)。
- 每帧底部隐藏标记 `<!-- frame:N duration:3000 transition:fade -->` 供后续 Remotion / Hyperframes 渲染脚本读取。
- 顶部加一段 JavaScript 自动播放: 每 3 秒切换到下一帧, 也支持点击 / 方向键控制; 角落显示进度条。
- 第 1 帧是 hook (一个数据 / 一个反常识 / 一个问题), 第 2-N 是论证, 最后是结论 + CTA。
- 字号巨大 (text-9xl), 一句话即可, 不要堆砌。
- 配色统一一套电影感 (深色背景 + 1 个霓虹强调色)。
- 输出最后包含一段简短注释 `<!-- HYPERFRAMES_META: ... -->`, 包含每帧 duration / transition / sceneSummary 的 JSON 元数据, 用于后续转 Remotion。

## Provenance

Merged from 11 skills of [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`. Licence Apache-2.0 — the source text of every variant is preserved above.
