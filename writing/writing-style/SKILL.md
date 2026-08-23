---
name: writing-style
description: "Apply the user's universal writing standard to every drafting, rewriting, editing, summarizing, or publishing task. Use for all prose, especially technical writing and content for arunabh1904.github.io, to preserve requested scope, make each paragraph answer one question, keep technical English simple and exact, vary cadence with intent, surface earned insight, and remove AI-writing residue. Always load this base before any paper, blog, Revision Notes, or Code-practice template."
---

# Writing Style

Apply this skill to every writing task. It owns topic architecture, continuity, voice, paragraph craft, evidence discipline, audio continuity, and the final prose audit. It does not own category templates, frontmatter, file placement, or publishing.

Read and apply [the prose system](references/prose-system.md) before drafting or revising.

For authored technical essays and Blog posts, also read [the local voice examples](references/voice-examples.md). Use them as calibration for compression, cadence, and judgment. Do not copy their subject matter or force their exact sentence patterns onto a different piece.

## Workflow

1. Set the scope contract before editing: requested passages, allowed structural change, facts that must survive, and whether the user asked for compression, expansion, or a neutral rewrite. A request to tighten cadence, remove wordiness, or "rewrite a bit" does not authorize a whole-post expansion.
2. Identify the audience, purpose, governing question, factual claims, and intended decision or takeaway. For a material revision, record the baseline with `scripts/audit_prose.py` before changing prose.
3. Build the article spine before polishing sentences. Write one sentence that states the piece's controlling question, then arrange the minimum topic blocks in dependency order. Each block must inherit an object or question from the previous one and produce what the next block needs.
4. Earn the title in the opening. The first paragraph should name the actual subject and explain the promise or distinction carried by the title before a vivid example, anecdote, or hyperbole asks the reader to infer it. For authored Blog posts, also locate the live motive: why this question matters now, what prompted it, or what the author finds surprising, difficult, exciting, or consequential.
5. Test the outline alone. Headings should reveal a coherent route through the subject, keep siblings at the same level of abstraction, and separate the main mechanism from optional branches, applications, and history.
6. Preserve the author's meaning, technical confidence, emotional register, and point of view. Preserve facts, citations, links, names, numbers, code, equations, frontmatter, tables, and asset paths unless the task explicitly changes them. Do not delete a personal trigger, a source that prompted the piece, or an earned reaction merely because a cleaner impersonal sentence can replace it.
7. Draft or revise one paragraph at a time. Write the private question that the paragraph must answer. Keep only sentences that answer, qualify, evidence, interpret, or hand off that question.
8. Run the editorial passes in this order: context and structure; missing explanation; pragmatic Simplified Technical English; earned insight and cadence; de-slop; audio continuity and deletion. Do not polish a sentence that belongs in a paragraph or section that should be cut.
9. Separate source-reported evidence from synthesis and judgment. Research missing facts from canonical or first-party sources when the task authorizes research. Never strengthen prose by inventing facts, citations, measurements, motivations, or emotions.
10. Prefer connected prose when ideas depend on one another. Use bullets only for parallel, independently scannable facts, options, checks, or artifacts.
11. Add a table, equation, diagram, figure, or callout only when it answers a question more clearly than ordinary prose. Turn a genuine multi-stage process—usually four or more named stages, branches, or a feedback loop—into a compact diagram instead of leaving an inline arrow chain to impersonate one. Keep equations, two-item comparisons, and incidental directional notation in text. Introduce what the reader should notice, keep a complete verbal path for audio, and interpret the object afterward.
12. Run the silent structure, continuity, audio, and prose audits in `references/prose-system.md`. For a material revision, compare the final file with its baseline using `scripts/audit_prose.py --baseline <git-revision> --check <file>`, or use `--baseline-file` for a supplied draft. Resolve regressions or document why the requested scope requires them.

## Boundaries

- Follow the matching category skill for format and repo mechanics; category rules override this base only where the reading task genuinely differs.
- Do not make every category sound alike. The shared voice should survive different reading modes and levels of depth.
- Do not imitate another writer's persona, anecdotes, signature phrases, or sentence patterns. Borrow durable editorial mechanics only.
- Keep file diffs reviewable. Do not rewrite unrelated passages during a scoped edit.
- When returning prose directly, lead with the revised text and briefly state material editorial choices only when useful.
