---
name: pack-mobile-apps
description: Native and cross-platform mobile work: Android with Kotlin, Compose and Material 3, iOS application development, Flutter, React Native and Expo animation, and Dart Genkit — including the design rules that make a mobile UI feel native rather than ported.
license: see each member
metadata:
  title: "Mobile apps pack"
  kind: "index pack"
  members: "11"
---

# Mobile apps pack

11 skills, each kept as its own skill in `skills/<id>/` — this pack is the index that tells you which one to read. Drawn from 6 upstream repositories.

## When to use

- Building or extending an Android, iOS, Flutter or React Native app.
- The UI has to follow Material 3 or the platform's own design language.
- Animation on mobile needs to feel native, not web-like.

## The skills

| Skill | What it does | From | Licence |
|---|---|---|---|
| [`android-native-dev`](../android-native-dev/SKILL.md) | Android native application development and UI design guide. Covers Material Design 3, Kotlin/Compose development, project configuration, accessibility, and build… | MiniMax-AI/skills | MIT |
| [`animate-expo`](../animate-expo/SKILL.md) | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs on, which… | emilkowalski/skills | MIT |
| [`developing-genkit-dart`](../developing-genkit-dart/SKILL.md) | Generates code and provides documentation for the Genkit Dart SDK. Use when the user asks to build AI agents in Dart, use Genkit flows, or integrate LLMs into Dart/Flutter… | google/skills | Apache-2.0 |
| [`flutter-dev`](../flutter-dev/SKILL.md) | A practical guide for building cross-platform applications with Flutter 3 and Dart. Focuses on proven patterns, state management, and performance optimization. | MiniMax-AI/skills | MIT |
| [`frontend-architecture`](../frontend-architecture/SKILL.md) | A portable, framework-agnostic architecture style for any React or React Native frontend. Organizes apps into feature modules with page/screen directories, a strict… | sickn33/agentic-awesome-skills | MIT |
| [`frontend-observability`](../frontend-observability/SKILL.md) | A portable, framework-agnostic field-side observability pattern for React or React Native integrations. | sickn33/agentic-awesome-skills | MIT |
| [`ios-application-dev`](../ios-application-dev/SKILL.md) | A practical guide for building iOS applications using UIKit, SnapKit, and SwiftUI. Focuses on proven patterns and Apple platform conventions. | MiniMax-AI/skills | MIT |
| [`kotlin-exposed-patterns`](../kotlin-exposed-patterns/SKILL.md) | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern. Use when working with… | affaan-m/ECC | MIT |
| [`kotlin-testing`](../kotlin-testing/SKILL.md) | Patrones de pruebas Kotlin con Kotest, MockK, pruebas de coroutines, pruebas basadas en propiedades y cobertura con Kover. Sigue la metodología TDD con prácticas idiomáticas de… | affaan-m/ECC | MIT |
| [`react-native-dev`](../react-native-dev/SKILL.md) | A practical guide for building production-ready React Native and Expo applications. Covers UI, animations, state, testing, performance, and deployment. | MiniMax-AI/skills | MIT |
| [`vercel-react-native-skills`](../vercel-react-native-skills/SKILL.md) | Comprehensive best practices for React Native and Expo applications. Contains rules across multiple categories covering performance, animations, UI patterns, and… | vercel-labs/agent-skills | NOASSERTION |

## Method

Read the table, pick the one skill that matches the situation, then open `../<id>/SKILL.md`. Two rules: do not load a dozen of these to look thorough, and prefer the narrower skill when two overlap.

## Gotchas

- The licences differ inside this pack (Apache-2.0, MIT, NOASSERTION). Each member carries its own `LICENSE` file; nothing here is relicensed.
- These are upstream skills, imported as written. Where one assumes a tool or service you do not use, the method still applies — the commands do not.
