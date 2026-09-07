---
name: write-blog-post
description: "Create or revise Blog posts for arunabh1904.github.io, including short commentary, reflective essays, technical explainers, and long-form research surveys. Use when section is blog, when a draft teaches a durable mental model, or when it synthesizes a field into an argument. Do not apply the compact one-paper Arxiv Note template."
---

# Write Blog Post

Read and apply [the universal writing style](../writing-style/SKILL.md).

## Choose Length Separately From Category

Blog is defined by its reading job, not its length or number of cited papers. A short argument about one paper can be a Blog post; a compact reconstruction of that paper belongs in Arxiv Notes. Follow an explicit category choice.

- **Short form:** answer one narrow question or develop one observation. Include the minimum example or evidence and the limit needed to support it. Headings, a formal conclusion, callouts, figures, and a source ledger are optional; stop when the point is complete.
- **Long form:** develop the question through a dependency-ordered explanation. Use sections, worked examples, derivations, and comparisons where they are needed. A research survey organizes papers by mechanism or decision, with enough detail to support its synthesis.

Follow the requested length. Otherwise choose the shortest treatment that delivers the promised understanding; do not stretch a brief reflection into a tutorial. For edits, the base skill's scope contract controls which workflow steps may change the draft.

## Edit The Author Before Applying A Workflow

For an existing Blog, start from the author's draft. Identify what makes this particular piece sound like them: enthusiasm, conversational bridges, asides, examples, first-person bets, or an uneven rhythm that fits the thought. Preserve those passages by default. Name the actual defect before changing one: a false claim, missing link in the explanation, repetition, or a confusing reference. A more formal alternative is not by itself an improvement.

Use the workflow below to diagnose and fill gaps, not to rebuild a clear draft into an impersonal research note. Do not add a thesis, caveat, decision rule, and polished landing to every paragraph. Keep the author's existing degree of informality; never manufacture personal experience or sprinkle in mannerisms as a substitute for preserving their words. When asked for more humanity after a rejected rewrite, return to the original and carry forward only useful repairs.

## One Blog Workflow

Use the relevant steps at the chosen length and editing scope. Essay, tutorial, and survey are settings inside the same process, not separate templates. Keep planning notes private unless the user asks to review them.

1. **Set the contract.** Write the audience, controlling question, intended payoff, evidence boundary, and one-sentence thesis. Choose the dominant reading job: reflect on an experience, build a technical mental model, or synthesize research. This choice changes the evidence and depth, not the workflow.
2. **Map the route.** List the minimum concepts needed to answer the controlling question and order them by dependency. Give every proposed heading one private question and one output. Remove a heading when its output is unused; demote a variant, application, or historical note beneath the concept it changes. For a connected series, define each installment's question and handoff before drafting.
3. **Choose depth and evidence.** For fast-moving research, state the evidence cutoff. For technical teaching, choose intuition-only, key-derivation, or full-derivation depth. Keep prerequisites clear when moving between levels. For a substantial research synthesis, build a source ledger that separates reported evidence from synthesis; a short commentary needs only the sources that support its claims. In reflective writing, use first person to locate experience or judgment and qualify memory when needed; do not turn recollection into universal evidence.
4. **Write the title, opening, and headings.** Open on the live tension: a result, constraint, misconception, failure, scene, or concrete question. Make the subject and payoff clear early. Preserve an authored opening that gets there through enthusiasm, a scene, or a conversational lead-in; it need not state a formal thesis in its first paragraph. Use short headings that name the next question, mechanism, or turn. A title may be witty or punchy when it remains precise and tells a technical reader what the post is about; reject clickbait and vague intrigue.
5. **Develop the explanation.** Give a technical paragraph a clear question and enough support to answer it. Vary its shape with the thought; a reaction, aside, or transition need not become a miniature analytical argument. Match the audience established in the contract; define paper-specific objects, notation, and uncommon acronyms. Move from the smallest useful example to the general mechanism when teaching. Use worked examples, counterexamples, boundary cases, or small simulations only when they change what the reader can predict.
6. **Make sources self-contained.** Scale explanation to a source's role. A citation cameo usually needs only one precise sentence or clause. For a load-bearing paper, explain `inherited problem -> minimal mechanism -> reported evidence -> decision implication`, plus the strongest live limit when it changes the conclusion. Classify paper variants by the axis they change before comparing them. Never create a parade of abstracts or make the reader open a link to understand the post.
7. **Use technical objects when they help.** Follow the prose system for notation and the prose around code, equations, tables, and figures. When creating or revising technical visuals, read [the visual reference](references/technical-visuals.md); its comparison and animation guidance is conditional, not a requirement to add animation.
8. **Add insight and make it audio-native.** Use a sparse Markdown callout only for an earned synthesis, decision boundary, or mental-model correction. Prefer a literal label that names its job; no post needs a callout merely to satisfy this workflow. Keep the main path linear, repeat stable technical nouns, announce changes of level, and use short recall phrases after long gaps. Do not depend on `above`, `below`, color, or panel position without naming and verbalizing the relationship. A listener should follow the complete argument without scrubbing backward.
9. **Run the universal editorial passes.** Apply the ordered context, explanation, simple-English, insight-and-music, de-slop, and audio-and-deletion passes in the prose system. Preserve purposeful repetition, signposting, parallel structure, declarative openings, and em dashes when they carry meaning.
10. **Choose an ending that fits the piece.** Preserve an authored ending that works; a useful historical recap can consolidate a survey. Do not replace it merely to manufacture a more analytical conclusion. A reflective post should advance the claim or leave an honest tension. A tutorial should give a transfer test, limits, and the next answer the reader can now derive. A survey should state what the evidence does not establish, give a decision guide when useful, and end with a falsifiable synthesis or research question.

The finished post must remain self-contained, cumulative, source-grounded, and proportionate: its contribution must repay its length.

## Repo Shape

- For a new site post, use `section: blog` and `/blog/YYYY/MM/DD/<postSlug>.html`. Preserve existing `postSlug` and `legacyPath` during edits unless URL migration is requested.
- Use a short shelf summary that names the post's question or payoff rather than a year-prefixed paper label.
- Prefer `.md`; use `.mdx` only for imports, JSX, or an interactive component.
- Use `$...$` and `$$...$$` for math.
- Put local visuals in `public/assets/images/`; introduce and interpret each one.

Use [publish-website-writing](../publish-website-writing/SKILL.md) when site integration or release is requested. Drafting or revising a Blog post alone does not initiate publishing or audio generation.
