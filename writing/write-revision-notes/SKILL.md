---
name: write-revision-notes
description: "Create or revise Revision Notes for arunabh1904.github.io from lectures, courses, books, talks, or long-form sources. Use when the output should support fast later recall through faithful structure, derivations, examples, source links, and explicit uncertainties."
---

# Write Revision Notes

Read and apply [the universal writing style](../writing-style/SKILL.md).

## Workflow

1. Identify the source, learning objectives, prerequisite concepts, and scope of the note.
2. Preserve the source's technical claims while reorganizing for retrieval. Distinguish direct source material, clarification, and the author's own interpretation.
3. Open with a quick overview that names what the reader should be able to explain or derive afterward.
4. Organize sections by concept or dependency. Use descriptive headings and stable terminology rather than decorative narrative headings.
5. Keep derivations complete enough to reconstruct. Define symbols, state assumptions, and explain why each step follows.
6. Use examples, compact tables, diagrams, or code only when they improve recall or expose a boundary case.
7. End sections with a concise memory hook, unresolved question, or connection to the next concept when useful.
8. Cite upstream lectures, slides, course pages, papers, or chapters. Mark unclear or missing source details instead of filling gaps from memory.

## Repo Shape

- Use `section: revision-notes` and `/revision notes/YYYY/MM/DD/<postSlug>.html`.
- Prefer `.md`; use `.mdx` only when imports, JSX, or interaction are necessary.
- Use `$...$` and `$$...$$` for math.
- Add the entry and upstream source links to `src/pages/revision_notes.astro`, which is hand maintained.

These notes optimize for faithful retrieval, not essay-like suspense or survey completeness.
