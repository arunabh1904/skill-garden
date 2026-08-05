---
name: publish-website-writing
description: "Route, format, validate, and ship writing for every authored category of arunabh1904.github.io: Arxiv Notes, Blog, Revision Notes, and Code practice. Use when the user asks to add, publish, or ship website writing. Route to exactly one category template, which loads writing-style, then use the GitHub PR shipping workflow."
---

# Publish Website Writing

This skill owns routing, repo conventions, validation, and shipping. It does not duplicate prose or category rules.

## Route Before Editing

Read exactly one primary category skill; that template loads [the universal writing style](../writing-style/SKILL.md):

| Visible category | Trigger | Skill | Storage |
| --- | --- | --- | --- |
| Arxiv Notes | one paper | [write-paper-note](../write-paper-note/SKILL.md) | `section: paper-shorts` |
| Blog | essay, mental-model explainer, commentary, or multi-paper survey | [write-blog-post](../write-blog-post/SKILL.md) | `section: blog` |
| Revision Notes | lecture, course, book, or source notes | [write-revision-notes](../write-revision-notes/SKILL.md) | `section: revision-notes` |
| Code | interview practice problem | [write-code-practice-problem](../write-code-practice-problem/SKILL.md) | `src/lib/code-practice.ts` |

Respect the user's category. Infer only when absent, and report the inference. A multi-paper technical survey belongs in Blog; do not route it to Arxiv Notes.

## Resolve The Paper Radar Queue

Before scoping a paper-publishing request, check `/Users/arunabhmishra/Code/paper-radar` when it exists:

1. Run `.venv/bin/paper-radar sync-actions` from that repository to import signed phone actions queued in Gmail.
2. Run `.venv/bin/paper-radar publishing-queue --json` and inspect `out/publishing-queue.json`.
3. For a broad batch request such as “ship the relevant papers,” treat every queued external paper as candidate scope. For a request naming one paper, keep that paper in scope and report other queued candidates without silently adding them.
4. Route each selected paper through `write-paper-note`. A `drafted` queue entry is source metadata, not finished writing; read the canonical paper, verify claims and figures, and complete the normal editorial workflow before publishing.
5. After shipping, report any queue entries that remain unprocessed. Do not interpret an existing website note or imported blog training example as a queued external paper.

## Inspect And Create

1. Work from the repo root and inspect `git status` before editing. Preserve unrelated work.
2. For a new post, inspect `src/content.config.ts`, `src/lib/post-utils.ts`, `tests/content.test.ts`, and two or three recent pieces in the target category if conventions may have drifted.
3. Write posts to `src/content/posts/<postSlug>.md`; use `.mdx` only for imports, JSX, or interaction. Match filename and `postSlug`.
4. Use full ISO timestamps, sparse tags, a specific shelf `summary`, and the category's `legacyPath` convention.
5. For Blog posts, verify that the title and every section heading are simple and direct. Remove ornamental wordplay and metaphorical framing unless the user explicitly requested them; preserve the existing `postSlug` and `legacyPath` during title-only cleanup.
6. Use `$...$` and `$$...$$` for math. Put new local images in `public/assets/images/`.
7. Add only the post file for Arxiv Notes and Blog unless an asset is needed. Revision Notes also requires `src/pages/revision_notes.astro`. Code follows its data-file overlay.
8. Leave the homepage untouched unless explicitly requested; collection shelves update automatically.

## Validate And Ship

1. Run any category-specific or targeted checks required by the overlay, then run the shared `git diff --check` and `npm run ci` after content changes.
2. Inspect the rendered target route when layout, math, images, links, or interactive behavior changed.
3. Use the installed `github-pr-shipper` skill for a fresh `codex/...` branch, focused commit, push, PR, checks, merge, deployment, and live-route verification.
4. Report inferred category, tags, date, title/slug cleanup, file type, and source gaps. For paper notes only, also report the inferred `field` and any intentionally omitted paper visual.
