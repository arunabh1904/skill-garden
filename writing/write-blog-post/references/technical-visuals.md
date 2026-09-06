# Technical Visuals For Blog Posts

Read this only when creating or substantially revising technical figures, comparisons, or animation. A short or text-only post does not require a visual. The prose system owns setup and interpretation; this reference adds visual-specific design and inspection rules.

## Figures And Comparisons

Define notation before an equation and explain what its result changes. Add a table when several exact mappings need one frame. Add a figure when a mechanism, comparison, or state transition is easier to inspect than to describe. Give a comparison one controlled axis and reuse the same input or scene across panels. Separate inherited infrastructure from the paper's contribution; show where evidence is assigned, discarded, fused, reweighted, carried, or removed. Preserve source figures unchanged with paper and figure citations.

For a custom explainer, label its status literally, such as `Proposed implementation` or `Author's interpretation`; do not use generic labels such as `Design synthesis`. When it follows a source figure, preserve the source figure's reading direction and component order unless the prose explicitly explains why the layout changes. Verify every claim against primary sources.

## Sequences And Animation

Use `setup -> object -> interpretation -> consequence` for code, equations, tables, and visuals.

For animation, storyboard `input -> operation -> output -> failure`. Ground the loop in one concrete event whose state visibly changes over time: name the actor or object, show the motion or state transition, display the relevant measurements or uncertainty, and reuse that event across method comparisons. A model name, token motion, generic feature map, or unlabeled box is not a scene; show what the mechanism changes for the concrete event, such as a radar range closing across sweeps or an occluded cyclist being predicted and then corrected. Keep that event visible in the final comparison or takeaway frame; never replace the explained scene with a text-only checklist.

In every literature comparison, put the paper or system name inside its frame beside the exact mechanism being illustrated; do not make the reader recover the attribution from surrounding prose or a caption. Mark generic baselines and author synthesis literally, and make the final frame map each compared paper to its distinct representation, intervention point, supervision, or deployment contract.

For an information-dense sequence, publish complete storyboard states as a manual frame-stepper with a visible range slider, previous and next buttons, and left/right arrow-key control while the figure is focused; do not autoplay. Use timing only when continuous motion itself carries information.

If autoplay is justified, assign dwell time per scene from its reading load instead of using one global duration: finish the reveal, then hold the complete state for roughly 3 seconds for one short sentence, 5–7 seconds for several labels or a comparison, and 8–12 seconds for a dense summary. Keep transitions brief and separate from reading time, record timing beside each storyboard step, and split a scene when added dwell does not make it easy to restate before the cut.

Audit every visible word before rendering: each label must name an input, operation, output, measurement, or constraint; replace slogans, compressed metaphors, and unexplained abstractions with the literal mechanism. Reject a visual whose motion cannot be summarized precisely, changes several axes at once, or implies an unsupported paper claim.

Inspect the full sequence at the Blog's default article width first, then at desktop and mobile sizes, for readable type without opening the source asset, keyboard operability, clear focus state, legibility, contrast, wrapping, aspect ratio, overflow, and reduced-size use.
