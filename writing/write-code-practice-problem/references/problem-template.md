# Code Practice Schema And Validation

Read the live files before editing in case the schema has changed.

## Primary Files

- `src/lib/code-practice.ts`: schema and problem entries
- `src/components/CodePracticeLab.tsx`: shared renderer and workspace
- `src/lib/code-editor.ts`: editor behavior
- `src/pages/code.astro`: index
- `src/pages/code/[id].astro`: derived detail route

## Schema

```ts
interface CodePracticeProblem {
  id: string;
  order: number;
  title: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  summary: string;
  prompt: string[];
  signature: string;
  requirements: string[];
  examples: { label: string; lines: string[]; result: string }[];
  hint: string[];
  solutionNotes: string[];
  solutionCode: string;
  starterCode: string;
  packages?: readonly string[];
  tags?: readonly string[];
}
```

## Safe Defaults

- `difficulty`: `Medium`
- `starterCode`: import only needed packages, define the function, add a focused TODO, then raise `NotImplementedError`
- `solutionNotes`: explain the core trick and why it works
- `tags`: prefer domain labels such as `Arrays`, `Dynamic Programming`, `Binary Search`, `NumPy`, `Graphs`, or `Strings`

The index and detail routes derive automatically from the shared data file. Preserve CodeMirror shortcuts: `Tab`, `Shift+Tab`, and `Cmd/Ctrl + /`.

## Validation

Run:

```bash
npm run test -- tests/code-editor.test.ts tests/code-practice-lab.test.tsx
npm run check
npm run build
```
