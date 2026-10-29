---
name: exec-briefing-memo
description: Decision needed + recommendation + evidence + tradeoffs, 把复杂材料压成可拍板的一页
license: Apache-2.0
metadata:
  title: "exec briefing memo"
  origin: "nexu-io/html-anything"
  upstream-path: "next/src/lib/templates/skills/exec-briefing-memo/SKILL.md"
  upstream-commit: "975fb3bcb98f1777781fb4c738902d36e32c8c46"
  category: "frontend-ui"
---

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

## Provenance

Imported from [nexu-io/html-anything](https://github.com/nexu-io/html-anything) at commit `975fb3b`, path `next/src/lib/templates/skills/exec-briefing-memo/SKILL.md`. Licensed Apache-2.0 — the full text is in `LICENSE`.
