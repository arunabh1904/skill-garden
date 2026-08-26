# Skill Garden

A public collection of personal agent skills. The repository keeps reusable judgment in base skills and places task-specific formats on top, so one rule has one canonical home.

## Writing

The writing stack lives in [`writing/`](writing/):

- `writing-style` — universal topic architecture, paragraph continuity, evidence discipline, and prose audit. Load this for every writing task.
- `write-paper-note` — source-grounded, decision-oriented single-paper notes.
- `write-blog-post` — reflective essays, intuition-first technical explainers, and mechanism-first multi-paper surveys.
- `write-revision-notes` — faithful, retrieval-oriented notes from lectures and long-form sources.
- `write-code-practice-problem` — concise coding interview prompts, hints, and solutions.
- `add-blog-voice` — human-profile Blog narration, chunk-level speech audits, and audio release checks.
- `publish-website-writing` — category routing, repository conventions, validation, and shipping for `arunabh1904.github.io`.

Every category skill loads `writing-style`; category skills contain only format and workflow differences. The `.agents/skills/` symlinks make the collection discoverable when Codex works in this repository.

For global use, symlink the desired folders into `$HOME/.agents/skills`. Keep `writing-style` globally available so it can be invoked for all prose, not only website work.

## Design rule

Put a rule at the narrowest layer where it is universally true:

- topic order, continuity, voice, and sentence craft belong in `writing-style`;
- category structure belongs in a category skill;
- file paths, validation, and GitHub flow belong in a publishing skill.

This separation avoids template drift and prevents a paper-note convention from leaking into a blog essay, tutorial, or survey.
