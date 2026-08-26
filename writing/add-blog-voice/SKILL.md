---
name: add-blog-voice
description: "Create, audit, and export coherent static narration for Blog posts in arunabh1904.github.io. Use when a Blog post needs a listen/read-aloud experience, narration-safe prose, audio generation, or a voice-artifact quality pass."
---

# Add Blog Voice

Use this after `writing-style` and `write-blog-post` for Blog narration. Keep the visible article authoritative. Narration is a compiled rendering of its argument, not permission to invent a looser script.

## Workflow

1. Freeze the article source first. Read it as a listener and confirm that headings, paragraphs, and useful lists still carry the argument after figures, code, equations, captions, tables, and references are omitted. Any prose edit requires a new export from the landed source digest.
2. Preserve facts, names, numbers, uncertainty, and technical vocabulary. Improve a missing transition in the article before synthesis; never ask the voice model to fabricate one.
3. For each new or changed Blog post, use the repository's human narration profile in `scripts/generate-blog-audio.py`. Add the `postSlug` to `HUMAN_NARRATION_POSTS` when it is not already assigned. Existing legacy assets may remain unchanged until their source changes; never put new work back on the legacy Qwen Base path merely to avoid a profile migration.
4. Use the fixed human profile unless the user explicitly chooses and revalidates another voice: `mlx-community/Voxtral-4B-TTS-2603-mlx-bf16`, preset `hi_female`, seed `1904`, temperature `0.65`, `top_k=50`, `top_p=0.9`, and speed `1.0`. Keep the model and supplied-voice license in scope; the current Voxtral model card states CC BY-NC 4.0.
5. Treat model controls as executable inputs, not descriptive metadata. Confirm the chosen checkpoint supports every requested control and that generation receives it. Qwen3-TTS Base is a voice-cloning checkpoint without instruction control; a stored style string does not change its delivery.
6. Generate bounded authored paragraphs, splitting only beyond the exporter's 1,200-character limit. Preserve punctuation timing inside each chunk. Add the exporter-defined `350 ms` pause after paragraphs and `650 ms` after headings. Do not apply tempo acceleration or a silence filter across finished speech.
7. Stream through the model's overlap-aware decoder and trim only chunk boundaries. Reject a chunk that reaches its token cap, is silent, or is implausibly short or long for its word count. A clean waveform is necessary but does not prove correct speech.
8. Keep pronunciation repairs audio-only. Preserve published spelling and add a targeted post-specific override when a shared phonetic spelling fails in a short heading or proper name. Include each override in the digest and manifest.
9. Keep accepted synthesis reproducible. When ASR or listening rejects one deterministic sample, reroll only that chunk, record its reviewed seed in `HUMAN_CHUNK_SEED_OVERRIDES`, regenerate the assembled MP3, and rerun the complete audit. Never accept an unrecorded lucky reroll.
10. Keep full-source narration as the default. A duration limit is a compiler policy, not permission to crop, accelerate, or silently abridge. If a post crosses its limit, make an explicit editorial choice: raise a narrow per-post limit for complete narration, or create a reviewed source-SHA-pinned audio view that covers every authored H2 section, governing claim, motive, evidence, and conclusion.
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

    Keep the committed thresholds unless a reviewed evaluation justifies changing them: aggregate WER at most `0.08`, no insertion longer than two words, and no chunk above `0.50` WER. The gate normalizes harmless spelled acronyms but must preserve long repeated-letter runs as artifacts.
13. Listen to the opening, paragraph and heading joins, every rerolled chunk, difficult pronunciations, and the ending. Run waveform integrity checks for NaNs, infinities, denormals, and clipping. ASR and sample statistics support listening; neither replaces it.
14. Update the technical audio Blog post whenever a material model, voice, chunking, pacing, pronunciation, duration, freshness, validation, licensing, or deployment decision changes. Explain the observed failure, its cause, the rejected fixes, and the release check that prevents regression.
15. Run `git diff --check` and site CI, then use the follow-up audio PR required by `publish-website-writing`. After deployment, fetch every changed MP3 with a cache-busting query and require its SHA-256 to match the committed asset.

## Narration audit

Ask of each paragraph: what should the listener carry into the next one? Keep the main path linear, use stable technical nouns, and verbalize any relationship that would otherwise depend on a figure or table position.

Treat `scripts/generate-blog-audio.py`, `scripts/audit-blog-audio.py`, and `public/assets/audio/manifest.json` as one versioned release contract. Do not redesign the speaker or weaken the artifact gate per post.
