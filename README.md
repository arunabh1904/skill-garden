# Skill Garden

A public collection of personal agent skills. The repository keeps reusable judgment in base skills and places task-specific formats on top, so one rule has one canonical home.

## Writing

The writing stack lives in [`writing/`](writing/):

- `writing-style` — universal topic architecture, paragraph continuity, evidence discipline, and prose audit. Load this for every writing task.
- `write-paper-note` — source-grounded, decision-oriented single-paper notes.
- `write-blog-post` — short commentary, reflective essays, technical explainers, and long-form research surveys.
- `write-revision-notes` — faithful, retrieval-oriented notes from lectures and long-form sources.
- `write-code-practice-problem` — concise coding interview prompts, hints, and solutions.
- `add-blog-voice` — human-profile Blog narration, artifact auditing, and audio release checks.
- `publish-website-writing` — category routing, repository conventions, validation, and shipping for `arunabh1904.github.io`.

Every category skill loads `writing-style`; category skills contain only format and workflow differences. Use the [writing route map](writing/README.md) to choose by reading purpose, independently of length. The `.agents/skills/` symlinks make the collection discoverable when Codex works in this repository.

For global use, symlink the desired folders into `$HOME/.agents/skills`. Include their sibling dependencies: every category needs `writing-style`, and publishing needs the category skills plus `add-blog-voice` for narrated Blog releases. `github-pr-shipper` is an external installed dependency of the publishing workflow. Keep the complete canonical folders here so relative references resolve through the symlinks; avoid independent installed copies that can drift. Keep `writing-style` globally available for prose outside website work.

## Design rule

Put a rule at the narrowest layer where it is universally true:

- topic order, continuity, voice, and sentence craft belong in `writing-style`;
- category structure belongs in a category skill;
- file paths, validation, and GitHub flow belong in a publishing skill.

This separation avoids template drift and prevents a paper-note convention from leaking into a blog essay, tutorial, or survey.
