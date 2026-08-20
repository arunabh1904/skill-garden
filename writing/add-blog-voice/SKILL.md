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
4. Prefer one synthetic narrator reference for the complete corpus. Use Qwen3-TTS Base ICL with the same reference WAV and transcript for every chunk. ICL anchors identity, but it does not retain a generation cache between chunks; do not redesign a VoiceDesign speaker for every chunk.
5. Use generated-only ICL decoding. Some non-streaming implementations decode reference and generated codes together, then estimate a waveform cut; that can leak the reference phrase before every article chunk. Use the generated-only streaming decoder with an interval longer than a bounded chunk, and verify its result flags before exporting.
6. Use low-temperature sampling (`0.05`, `top_p=0.9`) and a deterministic seed derived from post slug and chunk index. Do not force pure greedy decoding: in this runtime, awkward long passages can run to an unhelpful acoustic limit rather than stopping naturally.
7. Keep sentence-bounded chunks near the proven 360-character limit. Bigger 720- or 960-character chunks may reduce joins, but are not automatically more coherent and can make a full local corpus export impractically slow.
8. Keep the proportional acoustic-token cap, boundary trimming, and residual-silence pass. A delivery improvement is invalid if it reintroduces non-speech tails or multi-second gaps.
9. Validate every regenerated Blog asset: manifest freshness after the final source edit, no image/code/reference artifacts in narration, silence scan, and listening windows from the beginning, middle, and end. Inspect joins in the longest posts.
10. Update the technical audio post whenever a material model, chunking, narration, or validation decision changes. Explain the causal failure and the fix, not only the final configuration.
11. Run the site CI and ship through a PR only after the whole requested corpus uses one compatible narrator profile.

## Narration audit

Ask of each paragraph: what should the listener carry into the next one? Mark only the sentence that answers that question. If the emphasis cannot be located in the existing prose, improve the prose first or create an audio-only script that remains factually equivalent.

Use the deterministic exporter at `scripts/generate-blog-audio.py`. The committed synthetic reference belongs in `scripts/audio-assets/`; never use or imitate a real person's voice.
