---
name: writing-style
description: "Apply the user's shared voice, clarity, and evidence standards when drafting or editing prose. Preserve the requested scope and scale the process to the artifact, from a short message to a long technical article. Load this base before any writing category skill; it does not select a category or authorize publishing."
---

# Writing Style

This skill owns voice, paragraph craft, continuity, evidence discipline, and the prose audit. Category skills own reading format; the publishing skill owns site integration and releases.

Read [the prose system](references/prose-system.md) for the shared editorial rules. For authored technical essays and Blog posts, also read [the local voice examples](references/voice-examples.md) to calibrate cadence and judgment without copying their subject matter or sentence patterns.

## Set The Editing Scope

The user's explicit instructions govern the category defaults and shared style. Choose the applicable mode before editing:

- **Light cleanup or redundancy removal:** preserve the author's sentences; default to deletion. Repair grammar, factual errors, and the specific confusion the user identified with the smallest necessary change. Delete the weaker repetition instead of synthesizing both passages into new prose.
- **Cadence or clarity revision:** split, shorten, or locally reorder sentences where requested. Preserve meaning, voice, evidence, and coverage; do not turn it into a whole-post expansion.
- **Structural revision:** reorganize the requested material to repair dependencies, repetition, or inconsistent instructions. Preserve useful content and explain material changes.
- **New draft or requested expansion:** build the needed explanation and supporting evidence within the requested topic and depth.

Keep facts, citations, links, names, numbers, code, equations, frontmatter, tables, and asset paths intact unless the task changes them. Preserve characteristic phrasing, real motives, emotional register, and point of view. Never invent the author's experiences or reactions. In an existing authored piece, the draft is the primary voice reference; examples and editorial defaults are secondary. Treat loss of recognizable voice as a regression even when facts, links, and sentence-length metrics survive.

## Scale The Process

A short message, caption, blurb, or brief answer needs a clear purpose and a direct prose check. It does not need an article outline, headings, source ledger, callout, diagram, or audio workflow. Use this base alone when no category template applies.

For an article, identify its audience, controlling question, evidence boundary, and payoff. Build or inspect the topic order before polishing sentences. Apply the prose system's editorial passes only within the authorized editing scope: an audit can identify a structural problem without silently rewriting it during a light edit.

Make each explanatory paragraph answer one question and connect it to the next. Keep brief hinges, captions, retrieval bullets, and conclusions proportionate to their job; they do not each need a miniature argument. Add a table, equation, diagram, or figure only when it clarifies the subject, subject to an explicit category requirement. Verbalize the key relationship around technical objects so the explanation survives without their layout. Generating audio is a separate task.

For a material revision to an article, preserve the actual starting draft and use [audit_prose.py](scripts/audit_prose.py) to compare cadence and scope. Run from the article repository with `--baseline <git-revision> --check <file>` only when that revision represents the starting draft; otherwise save the draft and use `--baseline-file <saved-draft> --check <file>`. Metrics are warning signals, not proof of coherence or quotas. They are not a useful release gate for short copy or skill instructions.

## Finish Within Scope

- Run the relevant silent prose audits. For a cleanup, inspect the diff sentence by sentence and undo substitutions that do not fix the requested defect.
- Separate reported evidence from synthesis. Verify missing technical claims against primary sources when needed; never invent facts to improve the prose.
- Category rules may adapt format, depth, and reading mode. They do not override user intent, factual accuracy, or the editing scope.
- Keep different forms distinct: a shared voice does not require identical structures or lengths.
- When returning prose directly, lead with the revised text; explain material choices only when useful.
