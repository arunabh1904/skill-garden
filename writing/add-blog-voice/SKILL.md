---
name: add-blog-voice
description: "Create, audit, and export expressive but coherent static narration for Blog posts in arunabh1904.github.io. Use when a Blog post needs a listen/read-aloud experience, narration-specific prose shaping, Qwen3-TTS export, or an audio quality pass."
---

# Add Blog Voice

Use this after `writing-style` and `write-blog-post` when the task concerns a Blog post. Keep the visible article authoritative; narration is a second rendering of its argument, not a looser rewrite.

## Workflow

1. Freeze the article source first. Read it as a listener and confirm headings, paragraphs, and lists still carry the argument after figures, code, equations, captions, and references are omitted. Any final prose edit requires a new audio export; never ship an MP3 that predates its source digest.
2. Preserve facts, names, numbers, uncertainty, and technical vocabulary. Do not fabricate connective prose, examples, or emotional stakes for audio.
3. Shape delivery only at contrast, consequence, and payoff. Use punctuation and short sentence boundaries; never caps, filler, celebrity imitation, or theatrical direction.
4. Use the committed corpus narrator at `scripts/assets/blog-narrator-warm-indian-english-reference.mp3`: a warm Indian English female voice with a low-mid pitch, composed and slightly sombre delivery, controlled energy, precise diction, and restrained inflection. This selected voice remains the default until the user explicitly chooses another one. Never imitate a real person.
5. Use `mlx-community/Qwen3-TTS-12Hz-1.7B-Base-8bit` with the fixed anchor, narrator seed `1904`, temperature `0.3`, `top_p=0.9`, repetition penalty `1.05`, and final tempo `1.10x`. Record the anchor hash and complete profile in the manifest so a profile change makes every affected asset stale.
6. Decode generated codes only through Qwen's streaming ICL path. Some non-streaming implementations decode the anchor and generated codes together, then estimate a waveform cut; that leaked the spoken anchor before article chunks. Do not use that proportional-cut path. Do not add spoken-reference or ICL transcript fields to the public manifest.
7. Group synthesis by authored heading section, with a practical maximum of 4,000 characters per request. Keep the streaming decoder continuous inside each section and reuse the same anchor between sections. Do not return to sentence-sized requests: those resets caused audible changes in pitch, energy, timing, and volume.
8. Let the model carry sentence and paragraph timing from punctuation and structural newlines. Add only the exporter-defined `650 ms` pause between heading sections, then apply the final `1.10x` tempo once. Trim only whole-file or section boundaries; never run a silence filter that removes pauses inside speech.
9. Keep pronunciation repairs audio-only. The current lexicon says `cyclist` as `sike-list`, `LiDAR` as `lie-dar`, and `timestamp` as `time stamp`; preserve the published prose and add a targeted test for each new exception.
10. Refuse an export that reaches its acoustic-token cap, ends implausibly early for its word count, exceeds 30 minutes, or omits the article ending. If a full article exceeds 30 minutes, use a reviewed source-SHA-pinned sidecar that preserves every H2 section, governing claim, authored motive, evidence, and conclusion while removing repeated examples and visual-only material. Never crop an MP3 to the limit.
11. Validate every regenerated Blog asset after the final source edit: manifest freshness, one fixed narrator profile, section coverage, duration, no anchor phrase, and beginning/end completeness. Use full-file ASR to catch spoken leakage and missing endings, then listen at the beginning, at section joins, around reported trouble spots, and at the end.
12. Update the technical audio post whenever a material model, voice, sectioning, pacing, pronunciation, duration, freshness, validation, or deployment decision changes. Explain the observed failure, its cause, the rejected fixes, and the release check that prevents regression.
13. Run `git diff --check` and the site CI, then ship narration in the follow-up audio PR required by `publish-website-writing`. After deployment, fetch each changed MP3 with a cache-busting query and require its SHA-256 to match the committed asset.

## Narration audit

Ask of each paragraph: what should the listener carry into the next one? Mark only the sentence that answers that question. If the emphasis cannot be located in the existing prose, improve the prose first or create an audio-only script that remains factually equivalent.

Use the deterministic exporter at `scripts/generate-blog-audio.py`. Treat the committed anchor and manifest profile as one versioned narrator contract, not as an invitation to redesign the speaker during each release.
