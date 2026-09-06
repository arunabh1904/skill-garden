# Paper Taxonomy And Note Format

## Frontmatter

- Use `section: paper-shorts`.
- Use `legacyPath: /paper shorts/YYYY/MM/DD/<postSlug>.html`.
- Match the filename to `postSlug`.
- Set `summary` to `YYYY – <paper title>`, optionally retaining a common alias.
- Assign the narrowest durable `field` by the paper's primary technical decision:
  - `Language Models`
  - `Alignment & Post-Training`
  - `Reinforcement Learning`
  - `Vision Foundations`
  - `Generative Modeling`
  - `Vision-Language Models`
  - `Omni-Model Architectures`
  - `Multimodal Scaling & Data Mixtures`
  - `Video & Interactive World Models`
  - `Vision-Language-Action & Robotics`
  - `Robot Post-Training & Evaluation`
  - `Training Systems & Reliability`
  - `BEV Perception & Mapping`
  - `Motion Forecasting & Planning`
  - `Autonomous Driving: VLMs & Evaluation`
  - `Autonomous Driving: VLA & Planning`

Do not recreate broad catch-all fields such as `BEV`, `Omni-Models`, or `Autonomous Driving`.

## Note Shape

For new notes and requested format migrations, use this top-level shell with flexible detail inside it:

1. Year/title heading and a compact source block: canonical paper first, followed by useful project, code, data, or venue links.
2. A compact `Summary` that leads with the most decision-relevant result, names the method and setting, and states the evidence boundary.
3. `Core Insights` covering the minimal mechanism, reported evidence, main trade-off, and one paper-specific delta from the closest relevant prior work: inherited problem, changed mechanism or assumption, reported evidence, and consequence.
4. Explanatory images and other supporting artifacts in `Core Insights`, following the image contract below. Add literal, paper-specific subheadings only when they improve navigation.
5. `High-Level Takeaways` as three to five concise bullets connecting the paper to the research line, stating the decision implication and concrete boundary, and identifying the unresolved object handed to later work.

Omit filler sections. Preserve useful existing material such as source links, images and captions, derivations, implementation sketches, playgrounds, or benchmark tables. Keep those supporting artifacts in `Core Insights`; reserve `High-Level Takeaways` for the scan-friendly conclusion list. Use `Summary`, `Core Insights`, and `High-Level Takeaways` as the top-level reading path; do not add template sections beneath them when connected prose is clearer.

## Images And Captions

Published notes require one to three local explanatory images. A table, equation, or code block does not count toward that requirement. Include the smallest complete set of figures needed to understand the paper; each must carry a distinct explanatory job. Method, decisive evidence, and a live boundary are common jobs, not mandatory slots. Do not add every figure, raw ablation, or appendix panel by default; use one when it supplies essential evidence.

Prefer attributed source figures. Use a focused local schematic only when the source artifact is unavailable, illegible, unsafe to rehost, or less clear; label it as the author's explanation and cite the supporting source. Use a focused composite if necessary panels would exceed the image cap, preserving labels and disclosing crops or rearrangements. Do not alter the scientific meaning or imply the author-created layout came from the paper.

Store assets in `public/assets/images/`. Add descriptive alt text and a caption in the form `*<what the figure shows>. source: [<paper>](<canonical URL>)*`. Retain figure numbers and license information when available. Verify files exist and remain legible in the rendered desktop and mobile note. Do not publish a note with missing assets or zero images.

## Takeaway Bullets

Write three to five bullets, not a labeled Q&A checklist. Each bullet should make a claim rather than name a category, and together they should cover only the material dimensions:

- expensive architecture, data, systems, evaluation, or research decision
- atomic training unit: token, patch, latent, frame, clip, transition, action chunk, or trajectory
- parameter or representation sharing
- loss balance or normalization
- data mixture or curriculum
- visual or action compression
- measured scaling evidence within the fitted range
- missing matched-control ablation
- likely 10x-scale bottleneck
- matched-budget falsification experiment and rejection condition

Treat the last three as the note author's research judgment. For surveys or benchmarks, analyze the evaluation artifact rather than pretending the paper trains a model. Omit irrelevant modality, scaling, or compression dimensions.

## Links And Reading Paths

- Put stable external sources at the top of the note. Prefer the canonical paper, official project page, official code repository, and primary dataset page.
- Link an earlier or later site note inline when the sentence explains a verified technical relationship. Do not link papers merely because they share a field or publication order.
- Keep `field` accurate. The shared site template uses it to place the note between the earlier and later papers in that field and links back to the filtered chronological index.
- Do not duplicate that automatic navigation inside the Markdown body.

## Completeness Check

Verify the note names the problem, minimal method, data, evaluation, main result and baseline, concrete boundary, paper-specific change from prior work, expensive decision, evidence that would reverse that decision, and the boundary between reported facts and synthesis. Verify the image contract above, including explanatory coverage and source-aware captions. Across a field, verify that chronological summaries expose real changes in mechanisms and evidence without turning publication order into an unsupported influence claim.
