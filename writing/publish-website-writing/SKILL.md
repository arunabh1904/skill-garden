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
3. For a broad batch request such as “ship the relevant papers,” treat every queued external paper as candidate scope. Before drafting, compare its `blog_path` with current `origin/main`: if a finished, source-grounded note has already landed, classify it as published and do not regenerate or reship it merely because Paper Radar still says `drafted`. For a request naming one paper, keep that paper in scope and report other queued candidates without silently adding them.
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

For a corpus-wide editorial or visual pass, inventory every authored section before editing: `paper-shorts`, `blog`, `revision-notes`, and Code practice. Do not treat Arxiv Notes as the complete writing corpus. For callouts specifically, preserve ordinary prose and mark only existing summaries, theses, takeaways, decision rules, or recommendations that already have standalone emphasis value. Confirm that each in-scope category has been reviewed and add a regression check when the convention should persist.

## Validate And Ship

1. Run any category-specific or targeted checks required by the overlay, then run the shared `git diff --check` and `npm run ci` after content changes.
2. Inspect the rendered target route when layout, math, images, links, or interactive behavior changed. For Arxiv Notes, require one to three local images, verify every asset exists, and check that each image and caption is legible at desktop and mobile widths.
3. Use the installed `github-pr-shipper` skill for each fresh `codex/...` branch, focused commit, push, PR, checks, merge, deployment, and live-route verification.
4. After the release is live, run the post-ship cleanup below. A merged PR with a dirty or stale primary checkout is not a completed shipping handoff.
5. Report inferred category, tags, date, title/slug cleanup, file type, source gaps, and the final primary-checkout status. For paper notes only, also report the inferred `field`, image count, and each image's explanatory job. There is no zero-image publication path.

## Post-Ship Cleanup

Run cleanup only after the PR is merged, the deployment succeeds, and the intended live routes and assets are verified. For a Blog release with narration, wait until the audio follow-up PR and live MP3 checks finish; the interval between PRs is not a cleanup boundary.

1. Fetch `origin/main`, inspect the primary checkout with `git status --short --branch`, and compare every dirty path with both `origin/main` and the merged release. Classify each path as landed exactly, superseded by a later landed version, still queued or unshipped, or unrelated.
2. Clean only paths proven to be landed or superseded by the landed release. Restore tracked paths from `origin/main`; remove an untracked draft only when its intended replacement is confirmed on `origin/main` and live. Preserve still-queued drafts and unrelated work. If provenance is uncertain, leave the path untouched and report it.
3. Fast-forward the primary `main` checkout with `git merge --ff-only origin/main` when the remaining preserved work does not conflict. Never use a hard reset or stash unrelated work merely to make the checkout look clean.
4. Inventory all repository worktrees with `git worktree list --porcelain` and inspect each candidate's status. Remove a task-created worktree and its local topic branch only when the worktree is clean and its remote PR is confirmed merged or closed without work to preserve. Never remove an unrelated or dirty worktree to tidy the list. Run `git worktree prune --dry-run` first, then prune only administrative entries whose paths are already gone and whose work is proven disposable.
5. For a Paper Radar-originated release, refresh `publishing-queue --json` after cleanup. Use a supported published-state transition if Paper Radar provides one. Never edit its SQLite database ad hoc; if no supported transition exists and a live note remains labeled `drafted`, report that stale queue state and rely on the `origin/main` guard above to prevent duplicate publication.
6. Finish by checking the primary `git status --short --branch` and `git worktree list`. The desired handoff is a current, clean primary `main`; otherwise name every preserved path and why it remains.

## Ship Blog Audio In A Follow-Up PR

Treat a new or changed Blog post as a two-PR release. Keep audio generation out of the writing PR so narration is compiled from the exact source that reached `origin/main`.

Read and apply [add-blog-voice](../add-blog-voice/SKILL.md) before generating or validating narration. Its human narrator profile, bounded-paragraph policy, and chunk-level artifact gate are the release contract. Assign every new or changed Blog post to that profile; do not fall back to the legacy Qwen Base path, redesign a speaker per post, accelerate the finished speech, or weaken the audit thresholds to make a file pass.

1. Ship the Blog source and ordinary page assets first. Wait for its PR checks, merge, Pages deployment, and live-route verification. Do not call the Blog release complete yet.
2. Start a clean worktree from the resulting `origin/main`. Generate audio only for each changed `postSlug` with `scripts/generate-blog-audio.py`; never use an older or dirty checkout as the source.
3. Keep the full article as the default narration. Skip raw markup, tables, captions, references, and visual-only labels only when the surrounding prose carries the complete argument. If the exporter rejects a post for duration, make the editorial choice explicit: add a narrow reviewed per-post cap for complete narration, or create a source-SHA-pinned audio view that preserves every authored H2 section, governing claim, motive, evidence, and conclusion. Never truncate or accelerate the MP3 to fit.
4. Run targeted freshness, human-profile, source-coverage, beginning/end, duration, waveform-integrity, and chunk-level ASR checks. Reject multi-word insertions and high-error chunks even when whole-file WER is acceptable. Then run `git diff --check` and `npm run ci`.
5. Open a second PR containing only the regenerated Blog MP3s, `public/assets/audio/manifest.json`, and any necessary narration sidecar. Include exporter code or tests only when the compiler, profile assignment, or extraction contract changed.
6. Merge the audio PR only after checks pass and verify its Pages deployment. Fetch every changed live MP3 with a cache-busting query, compare its SHA-256 with the committed asset, and recheck every changed live Blog route.

The short interval between PRs is an incomplete release, not a failure to be hidden. Finish the audio PR in the same task unless the user explicitly requests text-only publication or asks to defer narration.
