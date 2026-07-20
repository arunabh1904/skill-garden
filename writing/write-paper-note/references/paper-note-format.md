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

## Flexible Note Shape

Most notes should contain:

1. Year/title heading and canonical source links.
2. A compact opening or `Summary` that names the method, setting, and result.
3. `Paper Insights` covering the problem, mechanism, evidence, and main tradeoff.
4. A figure, compact table, algorithm, or qualitative example when it materially carries the mechanism or evidence.
5. `Context` for the paper's position in the research line.
6. `Limits` for a specific cost, failure, missing comparison, or scope boundary.
7. `Decision Lens` for the decision the evidence should change.
8. A falsifiable `Takeaway` or take-home message.

Omit filler sections. Preserve useful existing material such as derivations, implementation sketches, playgrounds, or benchmark tables.

## Decision Lens

Write two or three connected paragraphs, never a labeled Q&A checklist. Cover only material dimensions:

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

## Completeness Check

Verify the note names the problem, minimal method, data, evaluation, main result and baseline, concrete boundary, expensive decision, evidence that would reverse that decision, and the boundary between reported facts and synthesis.
