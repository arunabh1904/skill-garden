---
name: write-paper-note
description: "Add or revise a self-contained, source-grounded, decision-oriented Arxiv Note in arunabh1904.github.io. Use when the reader needs an explanatory reconstruction of one paper, including paper-summary cleanup and literature-field placement. A Blog argument about one paper stays in Blog. Do not use this compact format for multi-paper survey blogs."
---

# Write Paper Note

Read and apply [the universal writing style](../writing-style/SKILL.md), then read [paper taxonomy and note format](references/paper-note-format.md).

For a scoped edit, preserve the requested scope. A typo, title, or caption fix does not require rebuilding the field timeline or normalizing the whole note. Use the complete workflow for new notes and substantive paper audits.

## Workflow

1. Work in `src/content/posts`; paper notes use `section: paper-shorts`.
2. Inspect the existing note and nearby notes in the same `field`. Preserve frontmatter, `postSlug`, `legacyPath`, imports, equations, source links, useful headings, figures, tables, captions, and interactive components unless the task changes them. The `field` value also drives the site's automatic earlier/later paper reading path, so change it only when the taxonomy is genuinely wrong.
3. For a new or substantive note, inspect the closest relevant papers in its field to establish the comparison. Build a full chronological field timeline only for a requested lineage or field audit. Use paper publication dates and verified technical relationships; chronology alone does not establish influence.
4. Inspect the canonical paper source, preferably the arXiv PDF plus official project or code pages. Cover the contribution, method, training/data setup, evaluation, main results, ablations, limitations, and figure/table captions. Do not rely on memory for technical claims.
5. Follow the source block, three-section shell, and takeaway format in [the note format](references/paper-note-format.md). Lead the summary with the most decision-relevant finding, its evidence, and its boundary. Do not open with generic importance, a field recap, or an unsupported verdict.
6. In `Core Insights`, explain the mechanism, reported evidence, central trade-off, and the paper-specific change relative to the closest relevant prior work: inherited problem -> changed mechanism or assumption -> reported evidence -> consequence for the research line. Name the comparison axis and link to an existing earlier or later site note when that relationship is direct. If the source does not support a priority or influence claim, describe the technical contrast without claiming lineage.
7. Use paper-specific subheadings inside `Core Insights` only when they materially improve a longer note. Prefer headings that name the object or question (`Why sparse queries replace a dense grid`, `What the matched-compute ablation shows`) over template labels or slogans. Do not use `Paper Insights` or `Decision Lens`.
8. Select and caption images using [the image contract](references/paper-note-format.md#images-and-captions). Preserve the existing one-to-three-image publication requirement. Verify asset existence and legibility at desktop and mobile widths.
9. Finish with the base prose audit and [the completeness check](references/paper-note-format.md#completeness-check). Run the lineage audit below for a requested field-wide review; check only relevant comparisons for a single note. Use the publishing skill for site validation and shipping when requested.

## Depth That Earns The Extra Space

Default to enough room for the reader to understand why the method works, what the decisive experiment isolates, and where the attractive conclusion breaks. The user's CounterAlign note is a useful depth reference: it traces a training example, distinguishes actor and critic supervision, interprets gains and regressions, and exposes appendix compute costs. Its length is an outcome of that explanation, not a word quota.

For a substantive revision, read the method and appendix before adding insight. Follow one concrete example through the representation, objective, and output when that makes an unfamiliar step intelligible. Explain why a design choice was necessary and what would happen under the plausible simpler alternative. Use exact ablations to distinguish that explanation from intuition. Spend additional space on a paper-specific surprise, failure, cost, or limitation instead of repeated field background or a generic scaling caveat.

Introduce each source figure with a question, then walk through the relevant path or comparison in prose. Name what to notice and explain why it matters. Choose readable panels over an illegible full-page architecture montage; preserve source figure numbers and disclose crops. A caption alone does not supply deep intuition.

For a whole-corpus request, keep a per-note ledger of source review, figure review, substantive changes, validation, and release state. Inventory or automated checks do not count as having read a paper. Preserve already complete notes when further expansion would add repetition.

## Lineage Audit

For a requested field or research-line audit, run this one field at a time in chronological order:

1. Read only the title, date, `Summary`, paper-specific change in `Core Insights`, and `High-Level Takeaways` of each note. Together they should form a cumulative technical history rather than a sequence of abstracts.
2. Check that every paper-specific comparison uses one controlled axis: representation, prediction target, objective, architecture, data, compute, evaluation, or deployment contract.
3. Distinguish three kinds of statement: the paper reports a result; the mechanism differs from earlier work; the note author infers a research trend. Cite the first, state the second precisely, and label the third as synthesis.
4. Compress repeated field background while retaining the minimum context needed to understand each note on its own. Link to earlier notes for extended background; spend the recovered space on the paper-specific change, evidence, trade-off, and unresolved question.
5. Run a chronology check against canonical publication dates. Never use the website post date as evidence of research priority, and never say a later paper caused an earlier one.
6. Run the swap test on every summary and takeaway. If another paper in the field could use the sentence unchanged, replace it with the distinctive mechanism, result, or boundary.

## Guardrails

- Keep the note self-contained and selective. Allow a somewhat longer explanation when mechanism, experiments, and source figures earn it; do not compress away the insight to satisfy the historical `paper-shorts` label.
- Preserve useful specialized material as subheadings or artifacts inside the three-section shell when creating or restructuring a note. A scoped edit does not authorize a format migration.
- Keep the canonical links, opening summary, and paper-specific change easy to find. Use the three-section shell consistently, but do not force identical subheadings or paragraph counts inside it.
- Do not hand-maintain previous/next navigation links. Assign the correct `field`; the shared paper template links the note to its same-field chronological reading path. Add inline links to other notes only when the prose discusses a direct technical relationship.
- Use tables for exact evidence and diagrams for mechanisms; use both when they answer different questions.
- Never infer exact loss weights, mixture ratios, compression rates, scaling laws, metrics, datasets, or motivations.
- Never claim that one paper influenced, enabled, solved, or superseded another solely because of publication order or architectural similarity.
- For ambiguous paper titles, resolve against canonical metadata and label any remaining mapping uncertainty.
