---
name: write-blog-post
description: "Create or revise Blog posts for arunabh1904.github.io, including reflective essays, intuition-first technical explainers, research commentary, and tutorial-depth multi-paper surveys. Use when section is blog, when a draft teaches a durable mental model, or when it synthesizes a field into an argument. Do not apply the compact one-paper Arxiv Note template."
---

# Write Blog Post

Read and apply [the universal writing style](../writing-style/SKILL.md).

## One Blog Workflow

Use this workflow for every Blog post. Essay, tutorial, and survey are settings inside the same process, not separate templates.

1. **Set the contract.** Write the audience, controlling question, intended payoff, evidence boundary, and one-sentence thesis. Choose the dominant reading job: reflect on an experience, build a technical mental model, or synthesize research. This choice changes the evidence and depth, not the workflow.
2. **Map the route.** List the minimum concepts needed to answer the controlling question and order them by dependency. Give every proposed heading one private question and one output. Remove a heading when its output is unused; demote a variant, application, or historical note beneath the concept it changes. For a connected series, define each installment's question and handoff before drafting.
3. **Choose depth and evidence.** For fast-moving research, state the evidence cutoff. Choose intuition-only, key-derivation, or full-derivation depth and keep that altitude stable. Build a source ledger that separates reported evidence from synthesis. In reflective writing, use first person to locate experience or judgment and qualify memory when needed; do not turn recollection into universal evidence.
4. **Write the title, opening, and headings.** Open on the live tension: a result, constraint, misconception, failure, scene, or concrete question. The first paragraph must name the subject and make the payoff felt without generic importance framing. Use short headings that name the next question, mechanism, or turn. A title may be witty or punchy when it remains precise and tells a technical reader what the post is about; reject clickbait and vague intrigue.
5. **Draft one paragraph per question.** State the answer early, develop the mechanism or evidence, interpret it, and land on a consequence or handoff. Assume a technical baseline, but define paper-specific objects, notation, and uncommon acronyms. Move from the smallest useful example to the general mechanism when teaching. Use worked examples, counterexamples, boundary cases, or small simulations only when they change what the reader can predict.
6. **Make sources self-contained.** Scale explanation to a source's role. Give a citation cameo one exact sentence. For a load-bearing paper, explain `inherited problem -> minimal mechanism -> reported evidence -> decision implication`, plus the strongest live limit when it changes the conclusion. Classify paper variants by the axis they change before comparing them. Never create a parade of abstracts or make the reader open a link to understand the post.
7. **Design technical objects and visuals.** Define notation before an equation and explain what its result changes. Add a table when several exact mappings need one frame. Add a figure when a mechanism, comparison, or state transition is easier to inspect than to describe. Give a comparison one controlled axis and reuse the same input or scene across panels. Separate inherited infrastructure from the paper's contribution; show where evidence is assigned, discarded, fused, reweighted, carried, or removed. Preserve source figures unchanged with paper and figure citations. Label custom visuals as explanatory synthesis and verify them against primary sources.
8. **Write around every object.** Use `setup -> object -> interpretation -> consequence` for code, equations, tables, and visuals. For animation, storyboard `input -> operation -> output -> failure`. Reject a visual whose motion cannot be summarized precisely, changes several axes at once, or implies an unsupported paper claim. Inspect the rendered asset at desktop and mobile sizes for legibility, contrast, wrapping, animation timing, aspect ratio, overflow, and reduced-size use.
9. **Add insight and make it audio-native.** Use a sparse Markdown callout such as `> **Deep insight:** ...` only for an earned synthesis, decision boundary, or mental-model correction. Keep the main path linear, repeat stable technical nouns, announce changes of level, and use short recall phrases after long gaps. Do not depend on `above`, `below`, color, or panel position without naming and verbalizing the relationship. A listener should follow the complete argument without scrubbing backward.
10. **Run the universal editorial passes.** Apply the ordered context, explanation, simple-English, insight-and-music, de-slop, and audio-and-deletion passes in the prose system. Preserve purposeful repetition, signposting, parallel structure, declarative openings, and em dashes when they carry meaning.
11. **End by transferring the model.** Do not recap headings. A reflective post should advance the claim or leave an honest tension. A tutorial should give a transfer test, limits, and the next answer the reader can now derive. A survey should state what the evidence does not establish, give a decision guide when useful, and end with a falsifiable synthesis or research question.

The finished post must remain self-contained, cumulative, source-grounded, and proportionate: its contribution must repay its length.

## Repo Shape

- Use `section: blog` and `/blog/YYYY/MM/DD/<postSlug>.html`.
- Use a short shelf summary that names the post's question or payoff rather than a year-prefixed paper label.
- Prefer `.md`; use `.mdx` only for imports, JSX, or an interactive component.
- Use `$...$` and `$$...$$` for math.
- Put local visuals in `public/assets/images/`; introduce and interpret each one.
