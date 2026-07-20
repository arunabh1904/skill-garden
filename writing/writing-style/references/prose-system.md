# Shared Prose System

Apply these rules to essays, surveys, paper notes, explainers, revision notes, code-practice copy, summaries, and editorial text. Preserve code, equations, names, quotations, and established technical terms.

## Build A Topic Spine

Coherence starts before sentence editing. A piece can contain strong paragraphs and still feel arbitrary when its topics do not form a route.

1. Write the controlling question in one sentence.
2. List the smallest set of concepts a reader must acquire to answer it.
3. Draw prerequisite arrows between those concepts. Order the main path by dependency, not by the order in which sources were read.
4. Put the canonical mechanism on the main path. Move variants, applications, historical notes, and edge cases beneath the concept they modify.
5. Give every section a contract:
   - **input:** what the reader already understands;
   - **question:** what this section resolves;
   - **output:** the concept, distinction, or evidence the next section can use.
6. Read only the title and headings. The outline should tell a compressed version of the argument without the body.

Prefer headings that name the actual concept and its role. A clever claim can work when the body proves it, but several metaphorical or slogan-like headings in sequence hide the hierarchy. Keep sibling headings at comparable granularity: do not place a broad field, a narrow paper, and a deployment caveat at the same level.

Choose one primary organizing logic for each stretch of the piece: derivation, system decomposition, decision tree, causal sequence, or chronology. Switch logics only with an explicit bridge that tells the reader why the view must change.

For technical tutorials, a reliable dependency ladder is:

`motivation -> minimal object -> canonical mechanism -> derivation or training objective -> variants -> consequences -> limits`

Use only the rungs the topic needs. The value comes from dependency order, not from forcing a template.

## Plain Language Without Lost Precision

- Prefer a short familiar word when it carries the same meaning.
- Cut words that do not change the claim, qualification, evidence, or rhythm.
- Prefer active constructions when the actor matters or is known. Keep the passive when the actor is unknown, irrelevant, or the object is the real subject.
- Replace stale metaphors, stock transitions, and ornamental framing with the mechanism or consequence.
- Replace jargon only when precision survives. Never simplify a scientific term, benchmark, architecture, or mathematical distinction into an inaccuracy.
- Break any style rule when following it would make the sentence awkward, vague, misleading, or less human.

These are judgment rules, not a blacklist. Em dashes, long words, passive clauses, and technical language remain available when they do real work.

## Argument-Led Paragraphs

- Give each paragraph one governing claim or turn. Let every sentence develop, qualify, test, or draw a consequence from it.
- Make paragraphs cumulative. The first sentence should either pick up a concrete noun or unresolved question from the prior paragraph, or clearly announce a necessary change of level.
- Put the claim or concrete situation early. Do not open by announcing that a topic is important, complex, or fast-moving.
- Name actors and forces in causal explanations: a model shares parameters, a mixture changes the gradient budget, or an evaluation hides a control.
- Use qualification to sharpen a claim, not evade one. State the judgment, acknowledge the strongest live alternative, and explain what evidence keeps the judgment intact.
- Use first person to locate judgment or experience: `my read`, `I suspect`, `I would choose`. Do not use it as filler or false intimacy.
- Start a new paragraph when the causal step, level of analysis, or argumentative job changes.
- Vary sentence length by function. Use a short sentence to orient or land a consequence; use a longer one when real dependencies belong together.
- Treat a one-sentence paragraph as emphasis, a reset, or a deliberate hinge. Do not let several short paragraphs in a row fragment one explanation; merge them when they share a claim.
- Do not end a paragraph merely because a fact, citation, equation, list, or example has been stated. Add the interpretation: what changed in the reader's model, why the fact matters here, or which question it creates next.
- Use a landing sentence with one of five jobs: consequence, contrast, synthesis, scope boundary, or handoff. Avoid generic recap.
- Prefer paragraphs when ideas depend on one another. Use bullets only for genuinely parallel material.
- Treat density as relationships per paragraph, not jargon per sentence. Dense prose tells the reader what caused what, under which condition, and why it matters.

## Transitions Without Filler

Transitions should expose a relationship, not merely announce motion. Prefer:

- **cause:** the previous mechanism creates the next problem;
- **contrast:** the next method changes one assumption or tradeoff;
- **zoom:** the argument moves from system to component, or component to consequence;
- **dependency:** the next section needs an object just established;
- **open question:** the prior evidence leaves one specific issue unresolved.

Repeat the important noun when continuity matters. A precise repeated term is clearer than replacing it with `this`, `it`, or a decorative synonym. Use explicit recall phrases sparingly but usefully: `the forward process above`, `that compression choice`, or `the same matched-compute test`.

Around technical objects, use the sequence `setup -> object -> interpretation -> consequence`. Introduce an equation or figure before it appears, explain the important terms or pattern after it, then state what it enables. Never stack equations, figures, or paper summaries without connective prose.

## Distinctiveness And Evidence

- Make one concrete, contestable claim at a time. Replace generic praise with a mechanism, observation, number, constraint, or decision.
- Run the swap test on titles, openings, shelf blurbs, headings, takeaways, and major claims: if an unrelated paper, product, or competitor could use the line unchanged, rewrite or delete it.
- Separate reported evidence from synthesis. Calibrate uncertainty without smothering a supported claim in hedges.
- Preserve facts, numbers, citations, proper names, technical distinctions, and scope boundaries during a style pass.
- Avoid achievement language such as `comprehensive`, `robust`, `powerful`, `successful`, or `important` unless the text immediately establishes the relevant dimension and evidence.
- Avoid canned contrast and hype such as `not just`, `more than`, `game changer`, `cuts through`, `unlocks`, `revolutionary`, or `a key step` unless a concrete mechanism or result earns the phrase.
- Resolve vague `this`, `that`, `these`, and `those` when the referent is not immediate.
- Preserve useful signposting, intentional repetition, and parallel structure. Do not sand every sentence into the same polished cadence.

## Structure And Continuity Audit

Run these passes before sentence-level cleanup:

1. **Outline pass:** read only headings. Remove orphan topics, repair mixed granularity, and check that the order follows prerequisites.
2. **Section-contract pass:** for each section, state its input, question, and output. Move or cut sections whose output is unused.
3. **Opening pass:** read the first sentence of every paragraph in sequence. They should form a recognizable argument rather than a list of unrelated claims.
4. **Handoff pass:** read each paragraph's final sentence beside the next paragraph's first. Add or repair the relationship when the jump is implicit.
5. **Fragmentation pass:** inspect runs of one- or two-sentence paragraphs. Keep deliberate hinges; merge fragments that belong to one explanatory unit.
6. **Object-continuity pass:** track the main technical nouns. Define each once, reuse it consistently, and make viewpoint changes explicit.

## Final Prose Audit

Run silently unless the user requests editorial diagnostics:

1. Replace decorative framing and stale phrases with the intended claim.
2. Shorten abstract language when an exact simpler phrase exists.
3. Cut sentences and words that add no fact, qualification, causal link, or useful rhythm.
4. Rewrite passive constructions when naming the actor improves clarity.
5. Replace avoidable jargon while protecting technical precision.
6. Check that every paragraph has one governing claim, a developed middle, and a landing that advances the piece.
7. Check every adjacent paragraph pair for an explicit causal, contrastive, zoom, dependency, or open-question relationship.
8. Run the swap test on the opening, conclusion, headings, summary, and other high-salience lines.
9. Check that every visual, table, and equation has an explanatory job and is interpreted in the prose.
10. Read for cadence. Undo edits that make every sentence equally short, polished, or predictable.

The plain-language rules adapt George Orwell's durable editing principles. The topic-spine and technical-object rules borrow the useful editorial mechanics of cumulative research tutorials: dependency-ordered headings, local definitions, explicit recall, worked mathematical objects, and primary references. They do not imitate another writer's voice.
