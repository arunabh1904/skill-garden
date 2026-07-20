---
name: write-blog-post
description: "Create or revise Blog posts for arunabh1904.github.io, including reflective essays, research commentary, and tutorial-depth multi-paper technical surveys. Use when section is blog or when a draft synthesizes a field into an argument. Do not apply the compact one-paper Arxiv Note template."
---

# Write Blog Post

Read and apply [the universal writing style](../writing-style/SKILL.md).

Before drafting, make a section map. Write one question and one output for every proposed heading. Remove a heading if its output is never used later; demote it if it is a variant or application of another topic. The heading sequence should remain intelligible without body text.

When the request could fit both Blog and Build Intuition, obey an explicit site category. Otherwise choose by the primary reading job: use Blog to synthesize evidence or advance a thesis across sources; use Build Intuition to teach one mental model through examples and derivation.

## Choose The Form

- Use an essay form for reflection, experience, research commentary, or a single thesis that does not need a literature tutorial.
- Use a survey form when the post synthesizes multiple papers, a training stage, a mechanism family, or a research lineage.

## Essay Form

1. State the concrete situation or claim early; do not begin with generic importance framing.
2. Use first person to locate experience or judgment, not as filler.
3. Develop fair qualifications and concrete consequences instead of flattening the essay into certainty or recap.
4. Use headings only when they help argument or pacing. Do not impose a rigid template on reflective writing.
5. Link sections through the pressure created by the previous section: a consequence, contradiction, or unresolved question.
6. End by advancing the claim, decision, or unresolved tension rather than summarizing headings.

## Multi-Paper Survey Form

1. Open with the narrow question, why it is consequential, the current thesis, scope, and exclusions.
2. State the evidence cutoff for fast-moving topics and choose a derivation depth: intuition only, key derivation, or full derivation. Keep the mathematical altitude consistent or announce when it changes.
3. Define the minimum vocabulary, system decomposition, or equation needed for the rest. Establish the canonical mechanism before surveying alternatives.
4. Organize the main path by prerequisite and mechanism. Put variants, applications, scaling methods, and historical updates beneath the concept they modify rather than presenting them as unrelated peers.
5. Classify variants by the axis they change before comparing them: representation space, prediction target, objective or path, conditioning, architecture, solver, data, or compute budget. Do not put changes on different axes into one flat list.
6. Explain each important paper as inherited problem -> minimal mechanism -> evidence -> decision implication. Do not create a parade of abstracts.
7. Compare papers inside one conceptual frame. Use equations, diagrams, and compact tables only when they carry the explanation. Frame each object before it appears and interpret it afterward.
8. Separate reported evidence from synthesis with calibrated language such as `reported`, `my read`, `promising`, `uncertain`, and `not yet demonstrated` where needed.
9. Carry recurring decision questions through the article: what is shared, what is the training unit, where compute is spent, which failure changes the recipe, and which matched control would falsify the claim.
10. End every major technical section with the exact result, limitation, or unresolved object that motivates the next section.
11. Include what the evidence does not establish, a practical decision guide when useful, and a concrete falsifiable research thesis.
12. Make the reading path cumulative: each layer gets a question and an artifact to produce, not merely a tiered bibliography.
13. Add canonical references for external facts, source-derived visuals, and paper claims.

Use explicit recall when a later section depends on an earlier definition or equation. Repeat the stable technical noun; do not hide continuity behind vague pronouns or ornamental synonyms. A reader should always know which object is being modified and why the topic has changed.

For a connected series, define the dependency chain before drafting. Give each installment one governing question and one explicit handoff to the next.

## Repo Shape

- Use `section: blog` and `/blog/YYYY/MM/DD/<postSlug>.html`.
- Use a short shelf summary rather than a year-prefixed paper label.
- Prefer `.md`; use `.mdx` only for imports, JSX, or an interactive component.
- Use `$...$` and `$$...$$` for math.
- Put local visuals in `public/assets/images/`; introduce and interpret each one.
