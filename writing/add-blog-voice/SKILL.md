---
name: add-blog-voice
description: "Create, audit, and export coherent static narration for Blog posts in arunabh1904.github.io. Use for audio generation, export, or a voice-artifact quality pass. A prose-only read-aloud or continuity edit belongs in writing-style and write-blog-post."
---

# Add Blog Voice

Use this for Blog narration after [writing-style](../writing-style/SKILL.md) and, when revising the article, [write-blog-post](../write-blog-post/SKILL.md). An audio audit alone does not require rewriting the article or starting a release. Keep the visible article authoritative. Narration is a compiled rendering of its argument, not permission to invent a looser script.

Before generation, compare the profile and exporter contract below with the clean release source, including the cached or fetched `origin/main` as appropriate. A stale primary checkout may still carry an older voice or decoder. If the release source differs, resolve the version mismatch before synthesis; do not silently claim that a documented control was applied.

## Workflow

1. Freeze the article source first. Read it as a listener and confirm that headings, paragraphs, and useful lists still carry the argument after figures, code, equations, captions, tables, and references are omitted. Any prose edit requires a new export from the landed source digest.
2. Preserve facts, names, numbers, uncertainty, and technical vocabulary. Improve a missing transition in the article before synthesis; never ask the voice model to fabricate one.
3. For each new or changed Blog post, use the repository's human narration profile in `scripts/generate-blog-audio.py`. Add the `postSlug` to `HUMAN_NARRATION_POSTS` when it is not already assigned. Existing legacy assets may remain unchanged until their source changes; never put new work back on the legacy Qwen Base path merely to avoid a profile migration.
4. Use the fixed human profile unless the user explicitly chooses and revalidates another voice: `mlx-community/Voxtral-4B-TTS-2603-mlx-bf16`, preset `casual_female`, seed `1904`, temperature `0.3`, `top_k=50`, `top_p=0.9`, speed `1.0`, and output gain `-1 dB`. The casual preset already supplies expressive delivery; higher acoustic sampling made short prompts improvise fillers, elongated sounds, and laughter. Treat language- or accent-specific preset names as meaningful product choices, not opaque IDs. Keep the model and supplied-voice license in scope; the current Voxtral model card states CC BY-NC 4.0.
5. Treat model controls as executable inputs, not descriptive metadata. Confirm the chosen checkpoint supports every requested control and that generation receives it. Qwen3-TTS Base is a voice-cloning checkpoint without instruction control; a stored style string does not change its delivery.
6. Pack each heading with the prose that follows it in a bounded request of at most 900 characters. Keep consecutive headings with their first real paragraph; never synthesize a heading as a tiny standalone prompt when prose follows. Preserve authored newlines inside the request. Add the exporter-defined `240 ms` pause between bounded paragraph continuations and `550 ms` between authored sections; let the model render the heading-to-prose pause inside one decode. The 900-character ceiling leaves acoustic-token headroom that 1,200-character technical requests did not reliably preserve. Do not apply tempo acceleration or a silence filter across finished speech.
7. Decode each bounded static-export request as one waveform. Do not request low-latency streaming and directly concatenate its intermediate waveforms: audible decoder joins can appear inside a paragraph even when overlap-aware streaming is available. Normalize only request-edge silence, then leave one decibel of headroom before MP3 encoding. Reject a request that reaches its token cap, is silent, is implausibly short or long for its word count, or contains a suspicious internal seam. A clean waveform is necessary but does not prove correct speech.
8. Keep pronunciation repairs audio-only. Preserve published spelling and add a targeted post-specific override when a shared phonetic spelling fails in a short heading or proper name. Include each override in the digest and manifest.
9. Keep accepted synthesis reproducible. When ASR or listening rejects one deterministic sample, reroll only that chunk, record its reviewed seed in `HUMAN_CHUNK_SEED_OVERRIDES`, regenerate the assembled MP3, and rerun the complete audit. Never accept an unrecorded lucky reroll.
10. Keep full-source narration: retain headings and authored prose in source order. Omit only raw markup, tables, figure and diagram captions, alt text, references, code blocks, and equations. Pronunciation and prosody transforms may change synthesis input, not the extracted narration. A duration limit does not permit cropping, acceleration, abridgment, or a shorter narration sidecar. If a complete post crosses its limit, use a narrow reviewed compiler or per-post limit change. Revise article length only when the user requests that editorial change.
11. Generate from a clean worktree based on the exact `origin/main` source:

    ```bash
    uv run --with 'mlx-audio[tts]' \
      python scripts/generate-blog-audio.py --post <postSlug>
    python scripts/generate-blog-audio.py --check --post <postSlug>
    ```

12. Run the chunk-level local ASR gate after the final generation:

    ```bash
    uv run --with mlx-whisper --with jiwer \
      python scripts/audit-blog-audio.py --post <postSlug>
    ```

    Keep the committed thresholds unless a reviewed evaluation justifies changing them: aggregate WER at most `0.08`, no insertion longer than two words, no inserted filler or non-lexical token even when it is one word, no chunk above `0.50` WER, and no unaligned prefix, suffix, or internal region longer than `1.5` seconds. The gate normalizes harmless spelled acronyms but must preserve long repeated-letter runs as artifacts. Treat `um`, `uh`, `hmm`, `yeah`, laughter-like tokens, and elongated repeated-letter sounds as release failures when the source did not contain them.
13. When a voice, sampling profile, or chunk policy changes, render and listen to a short heading-plus-prose canary before paying for the full long-form batch. After the full generation, listen to the opening, inside long requests, at paragraph and section joins, around every rerolled request, at difficult pronunciations, and at the ending. Run waveform integrity checks for NaNs, infinities, denormals, clipping, and suspicious internal silence. ASR and sample statistics support listening; neither replaces it.
14. When the task includes changing the audio pipeline and its explanatory Blog post, update that post with the observed failure, cause, rejected fixes, and release check. For a single-post narration task, report any documentation drift without silently adding another article to scope.
15. For a release, run `git diff --check` and site CI, then follow [the publishing workflow](../publish-website-writing/SKILL.md#ship-blog-audio-in-a-follow-up-pr) for PR order and live asset verification. For an audit or local export, report the result at the requested stage.

## Narration audit

Ask of each paragraph: what should the listener carry into the next one? Keep the main path linear, use stable technical nouns, and verbalize any relationship that would otherwise depend on a figure or table position.

Treat `scripts/generate-blog-audio.py`, `scripts/audit-blog-audio.py`, and `public/assets/audio/manifest.json` as one versioned release contract. Do not redesign the speaker or weaken the artifact gate per post.
