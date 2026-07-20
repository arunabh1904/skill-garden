---
name: write-build-intuition
description: "Create or revise Build Intuition posts for arunabh1904.github.io. Use for intuition-first technical deep dives, worked examples, derivations, diagrams, and interactive explainers whose main job is to build a durable mental model rather than survey a literature."
---

# Write Build Intuition

Read and apply [the universal writing style](../writing-style/SKILL.md).

## Workflow

1. Name the misconception, opaque mechanism, or mental gap the post will resolve.
2. State the core mental model early in concrete language.
3. Move from a minimal example to the general mechanism. Make every abstraction pay rent by explaining what it predicts or lets the reader derive.
4. Define notation immediately before use. Explain every equation in words and connect it to the mental model.
5. Use worked examples, counterexamples, boundary cases, or small simulations to test understanding.
6. Use a diagram for relationships or state changes, a table for exact comparisons, and an interactive component only when manipulating an input reveals the concept better than static prose.
7. End with a transfer test: a new case the reader can now reason through, plus the limits of the mental model.

## Repo Shape

- Use `section: build-intuition` and `/build intuition/YYYY/MM/DD/<postSlug>.html`.
- Prefer `.md`; use `.mdx` only for imports, JSX, or a genuinely useful interactive component.
- Use `$...$` and `$$...$$` for math.
- Store local visuals in `public/assets/images/` and keep them simple enough to understand at a glance.

Do not turn the post into an encyclopedic survey. Cite necessary sources, but organize around understanding rather than paper coverage.
