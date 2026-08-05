---
name: write-blog-post
description: "Create or revise Blog posts for arunabh1904.github.io, including reflective essays, intuition-first technical explainers, research commentary, and tutorial-depth multi-paper surveys. Use when section is blog, when a draft teaches a durable mental model, or when it synthesizes a field into an argument. Do not apply the compact one-paper Arxiv Note template."
---

# Write Blog Post

Read and apply [the universal writing style](../writing-style/SKILL.md).

Before drafting, make a section map. Write one question and one output for every proposed heading. Remove a heading if its output is never used later; demote it if it is a variant or application of another topic. The heading sequence should remain intelligible without body text.

Use simple, direct titles and headings. Name the subject, mechanism, question, comparison, or decision plainly; do not add wordplay, slogans, or metaphorical framing unless the user explicitly asks for it. Keep established technical terms intact, and prefer a descriptive noun phrase or concrete question over a clever claim.

## Choose The Form

- Use an essay form for reflection, experience, research commentary, or a single thesis that does not need a literature tutorial.
- Use a technical tutorial form when the main job is to build one durable mental model through examples, derivation, diagrams, or interaction.
- Use a survey form when the post synthesizes multiple papers, a training stage, a mechanism family, or a research lineage.

## Essay Form

1. State the concrete situation or claim early; do not begin with generic importance framing.
2. Use first person to locate experience or judgment, not as filler.
3. Develop fair qualifications and concrete consequences instead of flattening the essay into certainty or recap.
4. Use headings only when they help argument or pacing. Do not impose a rigid template on reflective writing.
5. Link sections through the pressure created by the previous section: a consequence, contradiction, or unresolved question.
6. End by advancing the claim, decision, or unresolved tension rather than summarizing headings.

## Technical Tutorial Form

1. Name the misconception, missing intuition, or practical question that makes the mechanism hard to use.
2. State the core mental model early enough that readers can use it to interpret every later detail.
3. Move from the smallest concrete example to the general mechanism. Preserve the same named objects as the explanation gains notation or abstraction.
4. Define notation before using it. Explain what each equation changes in the reader's model and what the result allows them to predict.
5. Use worked examples, counterexamples, boundary cases, or small simulations to expose where the intuition holds and where it fails.
6. Add diagrams, tables, or interactive components only when they let the reader inspect a relationship that prose cannot show as clearly. Frame the task before the object and interpret the result after it.
7. End major sections with a transfer question or consequence that requires the next concept. End the post with a compact transfer test, the model's limits, and the next question the reader is equipped to answer.

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

## Figure-First Long-Form Workflow

Use this workflow when a mechanism, comparison, or state transition is easier to understand visually. Do not add a figure merely to decorate a section.

1. Plan the explanation before drawing. Write the reader's exact confusion, the invariant objects, the variable that changes, the paper-specific operation, and the conclusion the reader should be able to predict after seeing the figure.
2. Separate inherited infrastructure from the paper's contribution. If a model uses an existing backbone, feature pyramid, optimizer, or representation, label it as inherited and animate the new projection, carrier, loss, state update, or supervision contract.
3. Give comparison figures one controlled axis. Reuse the same scene, inputs, task gradients, sensor failure, or frame transition across panels so differences come from the methods rather than from different examples.
4. Show the irreversible decision. Animate where evidence is assigned, discarded, densified, fused, reweighted, carried through time, or removed from the deployment graph. Prefer the variable that explains the method's characteristic failure over a generic sequence of boxes and arrows.
5. Keep titles literal and compact. State the mechanism or comparison directly, and retain paper names in panel labels or captions. Use minimal on-canvas text; move qualifications, lineage, and evidence into the surrounding prose.
6. Distinguish visual provenance. Preserve original paper figures without modification and cite the paper and figure number. Label custom diagrams or GIFs as explanatory synthesis, and verify every depicted mechanism against the primary paper before publishing.
7. Write around the visual in the order `setup -> figure -> interpretation -> consequence`. Before the figure, name what remains constant and what to watch. After it, explain the literature progression, the inherited component, the core insight, the trade-off, and the next unresolved question.
8. Inspect the rendered asset at desktop and mobile sizes. Check title wrapping, legibility, contrast, animation timing, aspect ratio, overflow, and reduced-size use. Link dense GIFs or diagrams to the full-resolution asset when mobile rendering makes labels small.

For an animated comparison, storyboard one sentence per panel before implementation:

- **input:** the shared evidence or state;
- **operation:** the exact paper mechanism;
- **output:** what survives or changes;
- **failure:** what the representation can no longer recover.

Reject a figure when its motion cannot be explained in one precise caption, when panels change several variables at once, when the title names a broad topic rather than the displayed mechanism, or when the visual implies a paper claim that the source does not establish.

Use explicit recall when a later section depends on an earlier definition or equation. Repeat the stable technical noun; do not hide continuity behind vague pronouns or ornamental synonyms. A reader should always know which object is being modified and why the topic has changed.

For a connected series, define the dependency chain before drafting. Give each installment one governing question and one explicit handoff to the next.

## Repo Shape

- Use `section: blog` and `/blog/YYYY/MM/DD/<postSlug>.html`.
- Use a short shelf summary that names the post's question or payoff rather than a year-prefixed paper label.
- Prefer `.md`; use `.mdx` only for imports, JSX, or an interactive component.
- Use `$...$` and `$$...$$` for math.
- Put local visuals in `public/assets/images/`; introduce and interpret each one.
