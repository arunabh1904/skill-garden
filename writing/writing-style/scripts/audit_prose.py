#!/usr/bin/env python3
"""Report cadence and scope deltas for Markdown prose.

The audit is deliberately heuristic. It excludes frontmatter, code fences, math
blocks, tables, headings, and image-only lines so a technical post is measured
mostly by the sentences a reader or narrator encounters as prose.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


WORD_RE = re.compile(r"\b[\w]+(?:[-'’][\w]+)*\b", re.UNICODE)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])(?:[\"'’”)]*)\s+(?=[A-Z0-9\"'“‘(])")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
INLINE_MATH_RE = re.compile(r"\$[^$]*\$")
HTML_RE = re.compile(r"<[^>]+>")


@dataclass(frozen=True)
class Metrics:
    words: int
    paragraphs: int
    sentences: int
    mean_sentence_words: float
    median_sentence_words: float
    short_sentences: int
    short_sentence_share: float
    long_sentences: int
    long_sentence_share: float
    mean_paragraph_words: float
    max_paragraph_words: int


def prose_blocks(markdown: str) -> list[str]:
    lines = markdown.splitlines()
    blocks: list[str] = []
    current: list[str] = []
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_fence = False
    in_math = False

    def flush() -> None:
        if current:
            text = " ".join(current).strip()
            if text:
                blocks.append(text)
            current.clear()

    for index, raw in enumerate(lines):
        stripped = raw.strip()
        if in_frontmatter:
            if index > 0 and stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped == "$$":
            flush()
            in_math = not in_math
            continue
        if in_math:
            continue
        if not stripped:
            flush()
            continue
        if stripped.startswith("#"):
            flush()
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush()
            continue
        if re.fullmatch(r"[-:| ]+", stripped):
            flush()
            continue
        if re.fullmatch(r"!?\[[^\]]*\]\([^)]*\)", stripped):
            flush()
            continue
        if stripped.startswith("<") and stripped.endswith(">"):
            flush()
            continue

        cleaned = re.sub(r"^\s*(?:[-*+] |\d+[.)] )", "", raw)
        cleaned = re.sub(r"^\s*>\s?", "", cleaned)
        cleaned = LINK_RE.sub(lambda match: match.group(1), cleaned)
        cleaned = INLINE_CODE_RE.sub("", cleaned)
        cleaned = INLINE_MATH_RE.sub("", cleaned)
        cleaned = HTML_RE.sub("", cleaned)
        cleaned = re.sub(r"[*_~]", "", cleaned).strip()
        if cleaned:
            current.append(cleaned)

    flush()
    return blocks


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def analyze(markdown: str) -> Metrics:
    paragraphs = prose_blocks(markdown)
    sentence_lengths: list[int] = []
    paragraph_lengths = [count_words(block) for block in paragraphs]

    for paragraph in paragraphs:
        for sentence in SENTENCE_SPLIT_RE.split(paragraph):
            length = count_words(sentence)
            if length:
                sentence_lengths.append(length)

    words = sum(paragraph_lengths)
    sentences = len(sentence_lengths)
    short = sum(length <= 8 for length in sentence_lengths)
    long = sum(length >= 25 for length in sentence_lengths)
    return Metrics(
        words=words,
        paragraphs=len(paragraphs),
        sentences=sentences,
        mean_sentence_words=round(statistics.fmean(sentence_lengths), 1) if sentence_lengths else 0.0,
        median_sentence_words=round(statistics.median(sentence_lengths), 1) if sentence_lengths else 0.0,
        short_sentences=short,
        short_sentence_share=round(short / sentences, 3) if sentences else 0.0,
        long_sentences=long,
        long_sentence_share=round(long / sentences, 3) if sentences else 0.0,
        mean_paragraph_words=round(statistics.fmean(paragraph_lengths), 1) if paragraph_lengths else 0.0,
        max_paragraph_words=max(paragraph_lengths, default=0),
    )


def git_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip()).resolve()


def read_from_revision(revision: str, path: Path) -> str:
    root = git_root()
    relative = path.resolve().relative_to(root)
    result = subprocess.run(
        ["git", "show", f"{revision}:{relative.as_posix()}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def delta(current: Metrics, baseline: Metrics) -> dict[str, float | int]:
    return {
        field: round(getattr(current, field) - getattr(baseline, field), 3)
        for field in asdict(current)
    }


def regression_reasons(
    current: Metrics,
    baseline: Metrics,
    allow_expansion: bool,
    allow_restructure: bool,
) -> list[str]:
    reasons: list[str] = []
    if baseline.words and not allow_expansion:
        growth = (current.words - baseline.words) / baseline.words
        if growth > 0.05 and current.words - baseline.words > 250:
            reasons.append(f"prose grew {growth:.1%} (+{current.words - baseline.words} words)")
    if current.long_sentence_share - baseline.long_sentence_share > 0.05:
        reasons.append(
            "long-sentence share rose "
            f"{baseline.long_sentence_share:.1%} -> {current.long_sentence_share:.1%}"
        )
    if (
        current.mean_sentence_words - baseline.mean_sentence_words > 2.5
        and current.mean_sentence_words > 18
    ):
        reasons.append(
            "mean sentence length rose "
            f"{baseline.mean_sentence_words:.1f} -> {current.mean_sentence_words:.1f} words"
        )
    if baseline.paragraphs and not allow_restructure:
        paragraph_drop = (baseline.paragraphs - current.paragraphs) / baseline.paragraphs
        paragraph_growth = (
            (current.mean_paragraph_words - baseline.mean_paragraph_words)
            / baseline.mean_paragraph_words
            if baseline.mean_paragraph_words
            else 0.0
        )
        if paragraph_drop > 0.15 and paragraph_growth > 0.20:
            reasons.append(
                f"paragraphs collapsed {baseline.paragraphs} -> {current.paragraphs} "
                f"while mean paragraph length rose {paragraph_growth:.1%}"
            )
    return reasons


def render(label: str, metrics: Metrics) -> str:
    return (
        f"{label}: {metrics.words} words, {metrics.paragraphs} paragraphs, "
        f"{metrics.sentences} sentences; sentence mean/median "
        f"{metrics.mean_sentence_words:.1f}/{metrics.median_sentence_words:.1f}; "
        f"short <=8 {metrics.short_sentences} ({metrics.short_sentence_share:.1%}); "
        f"long >=25 {metrics.long_sentences} ({metrics.long_sentence_share:.1%}); "
        f"paragraph mean/max {metrics.mean_paragraph_words:.1f}/{metrics.max_paragraph_words}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    baseline = parser.add_mutually_exclusive_group()
    baseline.add_argument("--baseline", metavar="GIT_REVISION")
    baseline.add_argument("--baseline-file", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--allow-expansion", action="store_true")
    parser.add_argument("--allow-restructure", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.baseline_file and len(args.files) != 1:
        parser.error("--baseline-file requires exactly one current file")

    reports = []
    failed = False
    for path in args.files:
        current = analyze(path.read_text(encoding="utf-8"))
        baseline_metrics = None
        reasons: list[str] = []
        if args.baseline:
            baseline_metrics = analyze(read_from_revision(args.baseline, path))
        elif args.baseline_file:
            baseline_metrics = analyze(args.baseline_file.read_text(encoding="utf-8"))

        if baseline_metrics:
            reasons = regression_reasons(
                current,
                baseline_metrics,
                allow_expansion=args.allow_expansion,
                allow_restructure=args.allow_restructure,
            )
            failed = failed or bool(reasons)

        reports.append(
            {
                "file": str(path),
                "current": asdict(current),
                "baseline": asdict(baseline_metrics) if baseline_metrics else None,
                "delta": delta(current, baseline_metrics) if baseline_metrics else None,
                "regressions": reasons,
            }
        )

    if args.json:
        print(json.dumps(reports, indent=2))
    else:
        for report in reports:
            print(report["file"])
            if report["baseline"]:
                print(render("  baseline", Metrics(**report["baseline"])))
            print(render("  current ", Metrics(**report["current"])))
            if report["delta"]:
                word_delta = report["delta"]["words"]
                sentence_delta = report["delta"]["sentences"]
                print(f"  delta: {word_delta:+} words, {sentence_delta:+} sentences")
            for reason in report["regressions"]:
                print(f"  regression: {reason}")

    return 1 if args.check and failed else 0


if __name__ == "__main__":
    sys.exit(main())
