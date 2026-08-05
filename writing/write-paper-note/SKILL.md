---
name: write-paper-note
description: "Add or revise a self-contained, source-grounded, decision-oriented Arxiv Note in arunabh1904.github.io. Use for one-paper notes, paper-summary cleanup, literature-field placement, Decision Lens analysis, and selecting explanatory paper figures or evidence tables. Do not use this compact format for multi-paper survey blogs."
---

# Write Paper Note

Read and apply [the universal writing style](../writing-style/SKILL.md), then read [paper taxonomy and note format](references/paper-note-format.md).

## Workflow

1. Work in `src/content/posts`; paper notes use `section: paper-shorts`.
2. Inspect the existing note and nearby notes in the same `field`. Preserve frontmatter, `postSlug`, `legacyPath`, imports, equations, source links, useful headings, figures, tables, captions, and interactive components unless the task changes them.
3. Build the field timeline before revising prose. Order nearby papers by the paper's publication date, identify the prior assumption or bottleneck each paper inherits, and note which later paper reuses, rejects, or exposes a boundary in its result. Do not infer influence from chronology alone.
4. Inspect the canonical paper source, preferably the arXiv PDF plus official project or code pages. Cover the contribution, method, training/data setup, evaluation, main results, ablations, limitations, and figure/table captions. Do not rely on memory for technical claims.
5. Use three recurring top-level sections: `Summary`, `Core Insights`, and `High-Level Takeaways`. Put `Summary` immediately after the canonical source links. Lead with the paper's most decision-relevant finding and the evidence that supports it, then state the setting and boundary. Do not open with generic importance, a field recap, or an unsupported verdict.
6. In `Core Insights`, explain the minimal mechanism, reported evidence, central trade-off, and the paper-specific change relative to the closest relevant prior work: inherited problem -> changed mechanism or assumption -> reported evidence -> consequence for the research line. Name the comparison axis and link to an existing earlier or later site note when that relationship is direct. If the source does not support a priority or influence claim, describe the technical contrast without claiming lineage.
7. Use paper-specific subheadings inside `Core Insights` only when they materially improve a longer note. Prefer headings that name the object or question (`Why sparse queries replace a dense grid`, `What the matched-compute ablation shows`) over template labels or slogans. Do not use `Paper Insights` or `Decision Lens`.
8. In `High-Level Takeaways`, synthesize what the evidence should change, the field-level trend it supports, the concrete boundary, and the unresolved object handed to later work. Carry applicable decision questions from the reference through the prose rather than exposing a checklist. Separate reported facts from research judgment and write `not reported` when an important source detail is missing.
9. Select figures and tables by explanatory job. Prefer source figures with attribution when appropriate; create a focused local schematic only when the source artifact is unavailable, illegible, unsafe to rehost, or less clear.
10. Store local assets in `public/assets/images/`, use descriptive alt text, and caption what the reader should notice plus source attribution.
11. End `High-Level Takeaways` with a concrete boundary and handoff: what the evidence does not establish, which later direction addresses that gap when known, and what result would reverse the note's decision implication.
12. Run the base prose audit, the lineage audit below, then validate with the repository's canonical content checks.

## Lineage Audit

Run this audit one field at a time, in chronological order:

1. Read only the title, date, `Summary`, `What Changed`, evidence claim, and `Takeaway` of each note. Together they should form a cumulative technical history rather than a sequence of abstracts.
2. Check that every `What Changed` section uses one controlled comparison axis: representation, prediction target, objective, architecture, data, compute, evaluation, or deployment contract.
3. Distinguish three kinds of statement: the paper reports a result; the mechanism differs from earlier work; the note author infers a research trend. Cite the first, state the second precisely, and label the third as synthesis.
4. Remove repeated field background once an earlier linked note already establishes it. Spend that space on the paper-specific delta, evidence, trade-off, and new unresolved question.
5. Run a chronology check against canonical publication dates. Never use the website post date as evidence of research priority, and never say a later paper caused an earlier one.
6. Run the swap test on every summary and takeaway. If another paper in the field could use the sentence unchanged, replace it with the distinctive mechanism, result, or boundary.

## Guardrails

- Keep the note compact but complete; do not produce a paper-length rewrite.
- Preserve useful specialized sections instead of forcing every note into identical labels.
- Keep the canonical links, opening summary, and paper-specific change easy to find. Use the three-section shell consistently, but do not force identical subheadings or paragraph counts inside it.
- Use tables for exact evidence and diagrams for mechanisms; use both when they answer different questions.
- Never infer exact loss weights, mixture ratios, compression rates, scaling laws, metrics, datasets, or motivations.
- Never claim that one paper influenced, enabled, solved, or superseded another solely because of publication order or architectural similarity.
- For ambiguous paper titles, resolve against canonical metadata and label any remaining mapping uncertainty.
