# CLAUDE.md: how an AI agent works with this knowledge base

This is the knowledge base of the ADC school: a Zettelkasten in English (the English edition of a Romanian original), organized into 17 skills, built from 49 sources (books on marketing, advertising, brand, creative, digital, AI, pitching, portfolios). The full rules are in `_meta/conventions.md`.

## Navigation

1. The entry point: `INDEX.md` → domains → skills.
2. Each skill: `20-skills/<slug>/SKILL.md`: competencies, learning path, playbooks for agents.
3. Permanent notes: `20-skills/<slug>/notes/<ID>-<slug>.md`. A link `[[BRD-007]]` or `[[BRD-007-…|BRD-007]]` = the file that starts with `BRD-007-`. Find it with `ls 20-skills/*/notes/BRD-007-*`.
4. Book sheets: `10-sources/SRC-0XX-*.md`. The full text (an extracted copy) is in `90-library/text/`: use it to check a claim or to go deeper (search with `grep -n`).
5. Cross-cutting maps (workflows, model comparisons, curriculum): `30-maps/`.
6. Generated metadata: `_meta/catalog.csv` (all notes), `_meta/graph.json` (links), `_meta/coverage.md`.

## When you answer a question or do a task (strategy, brief, ideas, pitch…)

- Start from the relevant `SKILL.md` and follow the playbook in its "How an AI agent uses this skill" section.
- Ground your answer in the notes, not in general memory. **Cite the IDs** of the notes you use (e.g. "according to [[BRD-007]] and [[INS-012]]"), so the answer can be checked.
- Follow the typed links: `foundation` = what has to be understood first; `contradicts` = where the authors disagree (mention the tension).
- If the base does not cover the subject, say so explicitly and propose a new note in `00-inbox/`.

## When you add knowledge (the CEQRC flow)

1. **Capture**: a quick note in `00-inbox/` (template `_meta/templates/fleeting.md`).
2. **Explain**: `python3 tools/kb.py new <CODE> "Claim-title"` creates the permanent note with the next ID; write it in your own words, following the template.
3. **Question**: the "Questions" section: where it does not apply, who contradicts it.
4. **Refine**: a precise title, a single idea, a source with a page, `status: growing`.
5. **Connect**: 2–6 typed links; add the note to the map in `SKILL.md`; run:

```bash
python3 tools/kb.py suggest --skill <slug>   # candidate links
python3 tools/kb.py build                    # backlinks, indexes, catalog, graph
python3 tools/kb.py check                    # health → _meta/health.md
```

## Rules

- IDs are permanent: do not renumber after the launch; merge with `kb.py merge KEEP DROP`.
- Do not edit by hand the sections between the `<!-- backlinks:… -->` and `<!-- auto:… -->` markers.
- Do not copy passages from the books: paraphrase; at most one short verbatim quote (under 15 words) per note.
- English with American spelling, using the books' own terms, model names and examples; no em dashes in our own prose.
