# Writing skill coherence audit

Audited September 6, 2026. This review covers the seven writing skills, every supporting reference, their discovery metadata, the prose audit helper, both repository guides, and local/global discovery links. It audits the instructions that produce the writing; it does not claim to have audited every published website article.

The cleanup keeps one shared voice while separating reading purpose, length, editing scope, and release stage. The maintained route map is in [writing/README.md](writing/README.md).

## Findings and changes

| Finding in the starting files | Consequence | Cleanup |
| --- | --- | --- |
| The universal style imposed an article outline, opening contract, and full editorial process on every prose task. | Short copy could expand into an article-shaped response. | Added proportional processing and a base-only path for messages, captions, blurbs, and ordinary summaries. |
| Deletion-only cleanup coexisted with unconditional instructions to merge paragraphs, reorganize sections, and expand missing explanation. | A light edit could become a rewrite. | Defined light cleanup, cadence/clarity revision, structural revision, and new-draft/expansion modes; subordinated all passes to that scope. |
| The publisher routed “one paper” to Arxiv Notes while Blog included research commentary. | A short argument about one paper could receive the wrong template. | Route by the reader's job and honor explicit category selection. |
| Blog described essays, tutorials, and surveys without distinguishing short and long treatment. | A narrow reflection could inherit survey-scale planning and structure. | Added short- and long-form settings within the same Blog skill; no separate competing style skill. |
| Blog allowed precise witty titles; publishing rejected wordplay unless explicitly requested. The base opening rule also conflicted with its own concrete-opening example. | Later workflow layers could undo legitimate editorial choices. | Blog owns title judgment; an opening scene can establish the subject and tension itself. Existing slugs and routes remain protected. |
| The Blog entrypoint embedded a long animation workflow in the ordinary writing process. | Text-only and short posts loaded unrelated visual instructions. | Moved the existing visual refinements into a conditional reference and made it readable in separate paragraphs. |
| Paper shape and image rules appeared in both the entrypoint and reference, with additional copies in publishing. | Revisions could change one copy while leaving another inconsistent. | Made the paper-format reference authoritative for the shell, images, and captions; retained the one-to-three-image publication policy. |
| Every paper revision demanded a field timeline, while lineage cleanup could remove context needed to read a note independently. | Small edits could expand into field audits; notes could depend too heavily on prior links. | Scoped full timelines to field reviews and preserved minimum standalone context. |
| The publisher imported Paper Radar actions before any paper task and described exactly one category for the entire task. | Named-paper work could access an unrelated queue; mixed batches had ambiguous routing. | Queue processing applies to queue requests; primary category selection is per artifact. |
| Audio extraction and quality rules were repeated in publishing, and narration work could trigger an unrelated explanatory article update. | Export and release instructions could drift or expand editorial scope. | The audio skill owns the technical contract; publishing owns release order. Documentation changes follow the task's scope. |
| Code Practice copied an old interface and assumed a single data file and next-integer order. | New exercises could miss specialized modules, progressive order, visuals, or supported solution fields. | Referenced the authoritative live interface and current file ownership; added ordering and visual integration guidance. |
| The Blog discovery prompt demanded insight callouts, and the repository lacked the audio skill discovery link. | Optional emphasis could become a default requirement; local discovery was incomplete. | Updated Blog/base prompts and added the missing repository symlink. |

## Coverage

| Reviewed material | Result |
| --- | --- |
| `writing-style/SKILL.md` | Scope modes, proportional workflow, and accurate baseline guidance added. |
| `writing-style/references/prose-system.md` | Conflicting scope/opening rules resolved; duplicate paragraph checklist consolidated. |
| `writing-style/references/voice-examples.md` | Original examples retained; opening guidance aligned with them. |
| `writing-style/scripts/audit_prose.py` | Read in full and left unchanged. Its word/sentence metrics are heuristics, not a semantic coherence test. |
| `write-blog-post/SKILL.md` | Short/long treatment and category boundary clarified. |
| `write-blog-post/references/technical-visuals.md` | Existing visual guidance extracted into this conditional reference. |
| `write-paper-note/SKILL.md` and its format reference | Format ownership, field-audit scope, and standalone readability clarified. |
| `write-revision-notes/SKILL.md` | Retrieval forms, preservation during edits, and listing-update scope clarified. |
| `write-code-practice-problem/SKILL.md` and its reference | Live schema ownership, progressive ordering, visual assets, and validation guidance updated. |
| `add-blog-voice/SKILL.md` | Technical policy preserved; audit/export/release boundaries and source-version check clarified. |
| `publish-website-writing/SKILL.md` | Per-artifact routing, queue scope, title ownership, release scope, and audio responsibilities aligned. |
| All seven `agents/openai.yaml` files | Read and validated; only Blog and base-style prompts needed edits. |
| Root and writing READMEs | Updated route map, rule ownership, and dependency/discovery guidance. |
| Repository and global skill links | All fourteen resolve to the canonical garden folders after adding the repository audio link. No independent installed writing copies were found in the inspected locations. |

## Manual request walkthroughs

These are instruction-level walkthroughs, not independent model evaluations or generated publication tests.

| Example request | Resolved behavior |
| --- | --- |
| “Tighten this two-sentence caption.” | Base style only; local wording changes, no outline, headings, audio, or release. |
| “Remove repeated points from this essay; keep my wording.” | Deletion-first cleanup; broader structural issues can be identified without rewriting them. |
| “Repair the structure and coherence of these writing instructions.” | Structural revision is within scope; reconcile contradictory guidance while preserving useful policy. |
| “Write a 400-word Blog argument about this paper.” | Short-form Blog, one supported argument, no Arxiv Note shell or automatic shipping. |
| “Write a long survey comparing these papers.” | Long-form Blog organized by mechanisms or decisions; explain sources in proportion to their role. |
| “Add an Arxiv Note for this one paper.” | Paper template and its image contract; no automatic Paper Radar import. Release follows the user's task context. |
| “Fix the caption in this paper note.” | Verify the caption and its source; do not rebuild the field timeline or normalize unrelated sections. |
| “Turn these lecture notes into recall cards.” | Revision Notes retrieval format; no essay suspense or mandatory paragraph landing for each card. |
| “Add this PyTorch architecture exercise.” | Inspect the owning module and interface; preserve tensor flow, add progressive ordering and required visuals, validate the implementation. |
| “Audit whether this Blog reads well aloud.” | Prose continuity review; no synthesis or publishing implied. |
| “Ship this Blog, text only.” | Website release with the explicit audio exception respected. |
| “Ship a Blog and an Arxiv Note together.” | One primary category per artifact, shared release coordination, and Blog narration unless deferred. |
| “Publish the relevant papers from Paper Radar.” | Process that queue, guard against already-landed notes, and apply the paper workflow to selected entries. |

## Verification and limits

- All seven skills pass the bundled skill validator. All seven metadata files parse and retain their invocation settings; prompts name their corresponding skills.
- Local Markdown links and section anchors resolve. All fourteen repository/global discovery links point to the canonical folders.
- `git diff --check` passes. The unchanged prose helper's command-line and baseline-comparison paths were checked.
- Code Practice guidance was compared with the local site's interface, imported modules, visual registry, and available tests. Revision Notes listing guidance was checked against its hand-maintained shelf.
- The local website checkout is behind its cached `origin/main`. The cached revision `011d32c` has the documented `casual_female` voice, temperature `0.3`, 900-character chunk limit, and whole-request human decode; the primary checkout still has older settings. The skill now requires checking the release source before generation. No remote refresh or production verification was performed for this audit.
- Existing local garden edits were saved before the cleanup and preserved in intent, including the visual refinements, paper-image policy, narration profile, and artifact thresholds. No website files were changed, no audio was generated, and no skill changes were committed or published.

The remaining maintenance risk is operational drift: site schemas and the audio exporter can change independently of these skills. The updated references direct future tasks to verify the relevant live code instead of treating copied instructions as proof of current behavior. Structural validation and these walkthroughs cannot guarantee the quality of every future draft.
