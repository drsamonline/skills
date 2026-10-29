---
name: pack-frontend-ui
description: Interface work end to end: React and Next.js performance, composition and view transitions, CSS and layout craft, animation and motion, visual design language, shaders and web artifacts. Use when building, restyling or reviewing a user-facing interface.
license: see each member
metadata:
  title: "Frontend and UI pack"
  kind: "index pack"
  members: "37"
---

# Frontend and UI pack

37 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 5 upstream repositories (MiniMax-AI/skills, addyosmani/agent-skills, anthropics/skills, emilkowalski/skills, vercel-labs/agent-skills).

## When to use

- Building or restructuring a React/Next.js app, a component library or a view transition.
- Choosing type, colour, spacing, layout or a whole visual language for a product.
- Animating something — entrance, interaction feedback, scroll — without hurting performance.
- Reviewing UI code against the Web Interface Guidelines.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`algorithmic-art`](../algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art,… | anthropics/skills | Apache-2.0 |
| [`animate`](../animate/SKILL.md) | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which… | emilkowalski/skills | MIT |
| [`animation-performance`](../animation-performance/SKILL.md) | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when an animation… | emilkowalski/skills | MIT |
| [`animation-vocabulary`](../animation-vocabulary/SKILL.md) | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS… | emilkowalski/skills | MIT |
| [`apple-design`](../apple-design/SKILL.md) | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, drag/swipe/sheet… | emilkowalski/skills | MIT |
| [`ask-sonner`](../ask-sonner/SKILL.md) | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and persisting toasts,… | emilkowalski/skills | MIT |
| [`brand-guidelines`](../brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style… | anthropics/skills | Apache-2.0 |
| [`break-ui`](../break-ui/SKILL.md) | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, long labels, non-Latin… | emilkowalski/skills | MIT |
| [`buddy-sings`](../buddy-sings/SKILL.md) | Turn your Claude Code pet into a singer. Each pet gets a unique vocal identity based on its name and personality — the same pet always sounds the same. | MiniMax-AI/skills | MIT |
| [`canvas-design`](../canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other… | anthropics/skills | Apache-2.0 |
| [`color-font-skill`](../color-font-skill/SKILL.md) | Choose presentation-ready color palettes and font pairings for PPT/design tasks. Use when users ask for visual theme choices, brand-safe palettes, or font recommendations.… | MiniMax-AI/skills | MIT |
| [`design-style-skill`](../design-style-skill/SKILL.md) | 同一套设计可通过调整圆角（rectRadius）和间距呈现4种不同风格。根据场景选择合适的风格配方。 | MiniMax-AI/skills | MIT |
| [`emil-design-eng`](../emil-design-eng/SKILL.md) | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | emilkowalski/skills | MIT |
| [`find-animation-opportunities`](../find-animation-opportunities/SKILL.md) | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does not implement… | emilkowalski/skills | MIT |
| [`frontend-design`](../frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't… | anthropics/skills | Apache-2.0 |
| [`frontend-dev`](../frontend-dev/SKILL.md) | Build complete, production-ready frontend pages by orchestrating 5 specialized capabilities: design engineering, motion systems, AI-generated assets, persuasive copy, and… | MiniMax-AI/skills | MIT |
| [`frontend-ui-engineering`](../frontend-ui-engineering/SKILL.md) | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components, implementing layouts, meeting WCAG… | addyosmani/agent-skills | MIT |
| [`gif-sticker-maker`](../gif-sticker-maker/SKILL.md) | Convert user photos into 4 animated GIF stickers (Funko Pop / Pop Mart style). | MiniMax-AI/skills | MIT |
| [`improve-animations`](../improve-animations/SKILL.md) | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or cheaper… | emilkowalski/skills | MIT |
| [`minimax-music-gen`](../minimax-music-gen/SKILL.md) | Generate songs (vocal or instrumental) using the MiniMax Music API. Supports two creation modes: Basic (one-sentence-in, song-out) and Advanced Control (edit lyrics, refine… | MiniMax-AI/skills | MIT |
| [`minimax-music-playlist`](../minimax-music-playlist/SKILL.md) | Scan the user's music taste, build a taste profile, generate a personalized playlist, and create an album cover. This skill is designed for both agent and direct user… | MiniMax-AI/skills | MIT |
| [`mmx-cli`](../mmx-cli/SKILL.md) | Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. Use when the user wants to create media content, chat with MiniMax models, perform web… | MiniMax-AI/skills | MIT |
| [`mobile-native`](../mobile-native/SKILL.md) | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. Covers sticky hover states,… | emilkowalski/skills | MIT |
| [`pick-ui-library`](../pick-ui-library/SKILL.md) | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts, state,… | emilkowalski/skills | MIT |
| [`pr-review`](../pr-review/SKILL.md) | Review pull requests against repository standards. Two-phase process: automated validation, then manual content review. | MiniMax-AI/skills | MIT |
| [`remove-animations`](../remove-animations/SKILL.md) | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional data, and decoration with no purpose — then… | emilkowalski/skills | MIT |
| [`review-animations`](../review-animations/SKILL.md) | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. | emilkowalski/skills | MIT |
| [`shader-dev`](../shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid simulation, particle systems, procedural generation, lighting,… | MiniMax-AI/skills | MIT |
| [`slack-gif-creator`](../slack-gif-creator/SKILL.md) | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for… | anthropics/skills | Apache-2.0 |
| [`theme-factory`](../theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can… | anthropics/skills | Apache-2.0 |
| [`vercel-composition-patterns`](../vercel-composition-patterns/SKILL.md) | Composition patterns for building flexible, maintainable React components. Avoid boolean prop proliferation by using compound components, lifting state, and composing… | vercel-labs/agent-skills | NOASSERTION |
| [`vercel-react-best-practices`](../vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure… | vercel-labs/agent-skills | NOASSERTION |
| [`vercel-react-view-transitions`](../vercel-react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition… | vercel-labs/agent-skills | NOASSERTION |
| [`vision-analysis`](../vision-analysis/SKILL.md) | Analyze images using the MiniMax MiniMaxunderstandimage MCP tool available in the MiniMax Token Plan. | MiniMax-AI/skills | MIT |
| [`web-artifacts-builder`](../web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex… | anthropics/skills | Apache-2.0 |
| [`web-design-guidelines`](../web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best… | vercel-labs/agent-skills | NOASSERTION |
| [`write-swift`](../write-swift/SKILL.md) | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, task groups),… | emilkowalski/skills | MIT |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0, MIT, NOASSERTION). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
