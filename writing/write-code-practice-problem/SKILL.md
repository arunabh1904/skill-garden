---
name: write-code-practice-problem
description: "Add or revise a coding interview practice problem in the Code section of arunabh1904.github.io from a screenshot, pasted prompt, or rough notes. Use for concise problem statements, requirements, examples, hints, solution explanations, and runnable starter/solution code without redesigning the shared CodeMirror interface."
---

# Write Code Practice Problem

Read and apply [the universal writing style](../writing-style/SKILL.md), then read [the problem schema and template](references/problem-template.md).

## Workflow

1. Inspect the current schema, aggregation, and owning data module through `src/lib/code-practice.ts`; follow its imports for specialized exercise collections.
2. Transcribe the supplied source before inferring. Preserve function names, signatures, dimensions, constraints, error conditions, numeric examples, and approximate results.
3. For a new problem, complete the required fields; for a revision, change only the requested fields:
   - derive a lowercase hyphen-case `id` and place it in the progressive order by prerequisites
   - write a specific one-sentence `summary` and one or two compact `prompt` paragraphs
   - write concrete requirements and two to four hints that nudge without revealing the answer
   - explain the solution in one or two claim-led paragraphs
   - keep `starterCode` runnable and use `NotImplementedError` rather than leaking the solution
   - keep solution comments sparse, above-line, and limited to non-obvious logic
   - infer difficulty; default to `Medium` when ambiguous
   - add packages only when needed and use precise tags
4. Add or revise the object in its owning data module using the surrounding formatting. For additions, update the progressive order and required visual registry/assets together.
5. Preserve the derived index/detail-page flow and shared CodeMirror interface.
6. Run the targeted Code tests plus the repository checks described in the reference.
7. Report assumptions caused by incomplete source material.

## Guardrails

- Preserve supplied examples and shapes. Derive and verify additional examples when needed; distinguish inferred assumptions from supplied constraints and error semantics.
- Keep the full answer in solution-only fields such as `solutionCode`, `solutionNotes`, and the supported walkthrough or NumPy reference; do not leak it through the starter or hints.
- Do not narrate obvious code line by line.
- Limit changes to the owning data module, ordering, and required visual assets. Touch templates, components, or tests only when the schema or a real behavior change requires it.
