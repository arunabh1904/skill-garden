# Code Practice Schema And Validation

Read the live files before editing. The repository interface is authoritative; do not maintain a second complete schema here.

## Primary Files

- `src/lib/code-practice.ts`: `CodePracticeProblem`, aggregation, `PROGRESSIVE_ORDER`, and shared visual mapping
- `src/lib/code-practice-architectures.ts`, `code-practice-attention.ts`, and `code-practice-latitude.ts`: specialized entries or enrichments; inspect the imports in the main file for current ownership
- `src/lib/code-practice-visuals.json`: visual specifications
- `public/assets/images/code-glance-<id>.svg`: corresponding visual assets
- `src/components/CodePracticeLab.tsx`: shared renderer and workspace
- `src/lib/code-editor.ts`: editor behavior
- `src/pages/code.astro` and `src/pages/code/[id].astro`: derived index and detail routes

## Entry Contract

Read `CodePracticeProblem` and comparable entries for exact types and supported fields. Preserve supplied signatures, dimensions, constraints, and results. Explain every inferred assumption. Required content includes identity, difficulty, summary, prompt, signature, requirements, examples, hints, solution notes, starter code, and solution code.

Check the current optional fields before using them: `walkthroughCode`, `visual`, `solutionDiagram`, `numpyAlternative`, `track`, `editorStart`, `interview`, `reasoning`, `packages`, and `tags`. Preserve an existing direct constructor and tensor flow when supplied. For PyTorch exercises, make device, dtype, shape changes, broadcasting, and training or inference state explicit where they affect correctness. Keep editor solution comments focused; use the supported walkthrough field for a fuller annotated reference when requested.

For a new entry, update its owning data module and the progressive order together. Place it by prerequisites and difficulty instead of assigning the next integer blindly. Follow the repository's current visual coverage convention: update the registry and corresponding asset when required. A content addition does not require redesigning the renderer.

## Safe Defaults

- Infer difficulty from the actual contract; use `Medium` only when the source leaves it ambiguous.
- Keep a scaffold runnable with required imports, the supplied signature, and `NotImplementedError`; preserve a requested blank editor mode.
- Explain the core mechanism and why it works in `solutionNotes`; show concrete intermediate shapes when layout or broadcasting is central.
- Derive small examples from the stated contract when needed and verify their results. Do not present invented constraints or error semantics as supplied requirements.
- Preserve CodeMirror shortcuts: `Tab`, `Shift+Tab`, and `Cmd/Ctrl + /`.

## Validation

Inspect the current package scripts and tests. For changed exercises, run the relevant solution, primitive, and visual checks, such as `tests/code-solution.test.ts`, `tests/code-practice-primitives.test.ts`, and `tests/code-practice-visuals.test.ts`. Use editor and component tests when those behaviors change. Execute meaningful numerical or shape examples for changed implementations when the existing checks do not cover them.

Then run `git diff --check` and `npm run ci` once for the final content change. The publishing skill owns release steps; do not repeat the same unchanged checks merely because multiple skills reference them.
