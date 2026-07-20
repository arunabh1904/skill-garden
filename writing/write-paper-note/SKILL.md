---
name: write-paper-note
description: "Add or revise a self-contained, source-grounded, decision-oriented Arxiv Note in arunabh1904.github.io. Use for one-paper notes, paper-summary cleanup, literature-field placement, Decision Lens analysis, and selecting explanatory paper figures or evidence tables. Do not use this compact format for multi-paper survey blogs."
---

# Write Paper Note

Read and apply [the universal writing style](../writing-style/SKILL.md), then read [paper taxonomy and note format](references/paper-note-format.md).

## Workflow

1. Work in `src/content/posts`; paper notes use `section: paper-shorts`.
2. Inspect the existing note and nearby notes in the same `field`. Preserve frontmatter, `postSlug`, `legacyPath`, imports, equations, useful headings, and interactive components unless the task changes them.
3. Inspect the canonical paper source, preferably the arXiv PDF plus official project or code pages. Cover the contribution, method, training/data setup, evaluation, main results, ablations, limitations, and figure/table captions. Do not rely on memory for technical claims.
4. State the actual contribution early. Explain the problem, minimal mechanism, evidence, and boundary well enough that the reader does not need to reopen the paper for the central argument.
5. Add a prose `Decision Lens` using only applicable dimensions from the reference. Separate reported facts from research judgment and write `not reported` when an important source detail is missing.
6. Select figures and tables by explanatory job. Prefer source figures with attribution when appropriate; create a focused local schematic only when the source artifact is unavailable, illegible, unsafe to rehost, or less clear.
7. Store local assets in `public/assets/images/`, use descriptive alt text, and caption what the reader should notice plus source attribution.
8. Run the base prose audit, then validate with the repository's canonical content checks.

## Guardrails

- Keep the note compact but complete; do not produce a paper-length rewrite.
- Preserve useful specialized sections instead of forcing every note into identical labels.
- Use tables for exact evidence and diagrams for mechanisms; use both when they answer different questions.
- Never infer exact loss weights, mixture ratios, compression rates, scaling laws, metrics, datasets, or motivations.
- For ambiguous paper titles, resolve against canonical metadata and label any remaining mapping uncertainty.
