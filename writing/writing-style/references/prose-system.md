# Shared Prose System

Apply these rules to essays, surveys, paper notes, explainers, revision notes, code-practice copy, summaries, and editorial text. Preserve code, equations, names, quotations, and established technical terms.

The target style combines three modes:

- **Simple technical English carries the explanation.** Use familiar words, stable technical nouns, explicit actors, and direct syntax.
- **Cadence carries attention.** Vary sentence length by function. Let short sentences orient or land. Let a longer sentence gather a real chain of dependencies.
- **Insight earns emphasis.** Isolate only the inference, tension, or decision boundary that changes how a technical reader sees the subject.

This is a pragmatic adaptation of Simplified Technical English, not a claim of strict ASD-STE100 compliance. Strict vocabulary control and a fixed 25-word ceiling are useful for maintenance instructions but too restrictive for all research prose. Default to short sentences; exceed that length only when splitting the sentence would hide a causal chain or damage an intentional cadence.

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

## Make Every Paragraph Answer One Question

Write a private margin question for every paragraph. The question can ask what an object is, how it works, why a result follows, what evidence supports it, where it fails, or what decision it changes. If two questions need different answers, split the paragraph. If adjacent paragraphs answer the same question, merge them unless the separation creates a deliberate hinge.

A complete explanatory paragraph usually has four moves:

1. **Answer:** state the claim or concrete situation early.
2. **Develop:** explain the mechanism, dependency, evidence, or counterpressure.
3. **Interpret:** say what the details change in the reader's model.
4. **Land:** state the consequence, limit, or question that hands off to the next paragraph.

Do not force all four moves into four sentences. Combine them when the paragraph stays clear. The governing test is whether every sentence works on the same question.

## Plain Language Without Lost Precision

- Prefer a short familiar word when it carries the same meaning.
- Cut words that do not change the claim, qualification, evidence, or rhythm.
- Put the real subject and verb near the start. In a causal sentence, make the mechanism, model, dataset, or researcher the grammatical subject instead of `readers`, `there`, or an abstract placeholder.
- Prefer active constructions when the actor matters or is known. Keep the passive when the actor is unknown, irrelevant, or the object is the real subject.
- Prefer simple present or simple past. Use a complex tense only when the timing distinction matters.
- Give one object one stable name. Do not rotate among ornamental synonyms. Expand an uncommon acronym the first time it appears.
- Keep noun clusters short when an `of`, possessive, or short clause is clearer. Preserve established technical names even when they are long.
- Keep one topic per paragraph and usually no more than six sentences. A paragraph can be longer when one technical derivation cannot be split without breaking the argument.
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

## Write The Music, Not The Ornament

Rhythm must clarify the argument. It is not permission for lyrical filler.

- Use short sentences for orientation, contrast, and consequence. Use medium sentences for the normal explanatory load.
- Reserve a long sentence for a genuine crescendo: several dependencies accumulate, the reader can still track the subject, and the final clause lands the point.
- Avoid several sentences with the same length and syntax. Also avoid a mechanical alternation of short and long sentences.
- Read punctuation as timing. A period closes a unit. A colon opens an explanation. Parentheses lower the volume. An em dash makes a sharp aside or turn. Use each because the relationship calls for it.
- Repeat a key phrase when repetition builds the idea. Do not replace purposeful repetition merely to vary vocabulary.
- Use a one-sentence paragraph or callout as silence around an important line. If the line does not contain a non-obvious inference, decision boundary, or mental-model correction, return it to the paragraph or delete it.
- Never write a fake-profound kicker. A sentence that sounds quotable but adds no mechanism, evidence, consequence, or honest judgment is filler.

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

## Earn The Insight

A deep insight compresses understanding; it does not decorate it. Add one only when the prior explanation supports at least one of these moves:

- reverse the obvious causal story;
- expose the hidden unit of optimization, cost, or failure;
- connect mechanisms that are usually discussed separately;
- identify the decision boundary where a method stops being the right choice;
- state a falsifiable synthesis that the sources do not state directly;
- correct a mental model that would otherwise cause a technical mistake.

Write the insight in one to three sentences. Name the objects and the reasoning. Mark synthesis as synthesis when the source does not report it. A callout is not a quota; many short pieces need none.

## Explain Papers Without Requiring The Link

When a paper is load-bearing, give the reader enough context to understand its role without opening it:

1. Name the inherited problem or assumption.
2. Explain the smallest mechanism that changes that assumption.
3. State the reported evidence that matters here, with the comparison and condition when available.
4. Interpret the decision implication or limit.

Scale this explanation to the paper's importance. Add detail where the mechanism is meaty or easy to misunderstand. Do not inflate a citation cameo into a summary, and do not replace a load-bearing explanation with an adjective such as `strong`, `novel`, or `effective`. Say `not reported` when the evidence is absent.

## Keep The Prose Audio-Native

A listener cannot scan backward, inspect a nearby panel, or hold several unresolved pronouns in working memory.

- Keep the main path linear. Move optional branches after the core explanation or label the detour before taking it.
- Use stable names and explicit recall: `the group-relative baseline`, not `this`; `the projection in the previous section`, not `the above method`.
- Announce a necessary change of level: system to component, training to inference, mechanism to evidence, or paper result to synthesis.
- Introduce tables, equations, figures, and code blocks before they appear. Afterward, state the one conclusion the listener needs.
- Do not make a later section depend on column position, color, or spatial language alone. Name the compared object and verbalize the relation.
- Read headings and first sentences aloud in sequence. They should sound like one explanation, not shuffled notes.

## Structure And Continuity Audit

Run these passes before sentence-level cleanup:

1. **Outline pass:** read only headings. Remove orphan topics, repair mixed granularity, and check that the order follows prerequisites.
2. **Section-contract pass:** for each section, state its input, question, and output. Move or cut sections whose output is unused.
3. **Opening pass:** read the first sentence of every paragraph in sequence. They should form a recognizable argument rather than a list of unrelated claims.
4. **Handoff pass:** read each paragraph's final sentence beside the next paragraph's first. Add or repair the relationship when the jump is implicit.
5. **Fragmentation pass:** inspect runs of one- or two-sentence paragraphs. Keep deliberate hinges; merge fragments that belong to one explanatory unit.
6. **Object-continuity pass:** track the main technical nouns. Define each once, reuse it consistently, and make viewpoint changes explicit.

## Required Editorial Passes

Run these passes in order. Later passes must not repair a structural problem with prettier sentences.

1. **Context pass:** read the whole piece paragraph by paragraph. Recover the governing question, remove orphan material, and reorder sections by dependency. Write a private question for each paragraph.
2. **Explanation pass:** expand unclear steps. For a load-bearing paper, mechanism, result, equation, or code path, add the missing context needed to understand it without an external click. Do not add background that the technical audience already has.
3. **Simple-English pass:** shorten syntax, put the real subject and verb early, use simple tenses, keep one name per object, resolve pronouns, and split paragraphs that answer more than one question.
4. **Insight-and-music pass:** vary sentence length by function. Add only earned hinge lines or callouts backed by the explanation. Remove ornamental metaphors and fake crescendos.
5. **De-slop pass:** find empty summary sentences, bullet overuse, flat rhythm, wrong grammatical subjects, low information density, vagueness, ambiguous demonstratives, and fluent sentences that assume the understanding they claim to provide. Preserve useful repetition, signposting, parallel structure, declarative openings, and em dashes.
6. **Audio-and-deletion pass:** listen to the path through headings, paragraphs, and technical objects. Repair backward jumps and visual-only references. Delete every sentence that adds no fact, qualification, causal link, decision, or useful rhythm.

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
11. Ask the private question for each paragraph and confirm that every sentence helps answer it.
12. Listen for references that require the page layout. Name the object or relationship so the prose survives audio.
13. Compare the contribution with the length. Cut until every remaining paragraph repays the reader's attention.

The plain-language rules adapt the public principles of [ASD Simplified Technical English](https://www.asd-ste100.org/), the user's [Amazon writing reference](https://github.com/ksindi/managers-playbook/blob/main/images/write-like-an-amazonian.jpg), and George Orwell's durable editing principles. The cadence rules use the sentence-length lesson in the user's [write music reference](https://github.com/ksindi/managers-playbook/blob/main/images/write-music.png). The de-slop pass applies Shreya Shankar's [analysis of LLM writing](https://www.sh-reya.com/blog/ai-writing/): remove empty conclusions, list abuse, flat rhythm, wrong subjects, low density, vagueness, ambiguous demonstratives, and fluency without understanding while retaining rhetorical devices that do real work. These are editorial mechanics, not an imitation of another writer's persona or signature phrases.
