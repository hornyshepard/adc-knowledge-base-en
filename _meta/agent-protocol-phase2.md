# Agent protocol, Phase 2: integrating a skill

Phase 1 agents read the books and wrote source notes (`10-sources/`) and permanent notes (`20-skills/<slug>/notes/`) with temporary IDs (`BRD-0501`, `BRD-1402` …). Notes about the same skill came from different book groups, so a skill folder now contains duplicates, uneven depth, and no links between groups.

You own one or more skills. Your job: turn each skill folder into a coherent, deduplicated, richly linked unit with a proper hub file `SKILL.md`. Several agents run in parallel, each owning different skills.

KB root: `/Users/dumitrubabara/Downloads/Books for ADC School/ADC-Knowledge-Base/` (quote paths: they contain spaces).

## 0. Read first

1. `_meta/conventions.md`, `_meta/skills.json`, `_meta/templates/zettel.md`, `_meta/templates/skill.md`.
2. `_meta/catalog.csv`: every note in the KB (id, title, skill, kind, level, sources, path). Use it to find notes in OTHER skills you can link to.
3. `_meta/link-suggestions-<slug>.md` for each of your skills: machine-generated similarity candidates (TF-IDF). Treat them as hints only.
4. `_meta/reports/G*.md`: Phase 1 reports, especially the "likely overlaps" sections.
5. Every note in your skill folder(s), in full.

## 1. Ownership rules (parallel safety)

- You may create, edit and delete files **only inside your own skill folders** (`20-skills/<your-slug>/…`) and write your report `_meta/reports/P2-<CODE>.md` and your merge list `_meta/reports/merges-<CODE>.txt`.
- You may READ anything in the KB. Do not edit source notes, other skills' notes, or files in `_meta/` other than the two above.
- Do NOT run `kb.py build`, `renumber`, `merge` or `redirect`. You MAY run `kb.py check` and `kb.py suggest --skill <slug>`.
- If you write helper scripts or scratch files, put them in a folder named after your agent (e.g. `…/scratchpad/P2-DIG/`): the scratchpad is shared with other agents running in parallel.
- `kb.py check` also writes `_meta/health.md`, which other agents overwrite; read it right after your own run.

## 2. Deduplicate inside your skill

When two or more notes in your skill cover the same idea:

1. Pick the KEEP note (best title/content). Rewrite it so it integrates the best of all versions: the union of sources (in `sources:`), the strongest explanation, the clearest example, and (very valuable) **where authors agree or disagree** ("Kotler and Tybout & Calkins converge here; Fennis & Stroebe add…").
2. Merge the `tags` and `also`, and keep all typed links that still make sense.
3. Delete the DROP file(s).
4. Append one line per dropped note to `_meta/reports/merges-<CODE>.txt`: `DROP_ID KEEP_ID` (e.g. `BRD-1403 BRD-0502`). The orchestrator will redirect every link in the KB after all agents finish, so links pointing to DROP from elsewhere will not break.

Notes that are related but not identical (e.g. a concept and its application) stay separate and get linked instead. When a note in ANOTHER skill duplicates one of yours, do not touch it: link to it (`see` / `alternative`) and list the pair in your report under "Cross-skill duplicates".

## 3. Link across the whole KB

For every note you keep, make sure it has **2–6 typed links** in "Links", including at least one link to a note from a *different book group* or a *different skill* where a sensible one exists (use the catalog and the suggestion file). Every link line: `- **relation** [[ID]]: reason`. Use only existing IDs from the catalog (or your own new notes). Relations: foundation, extends, application, example, contradicts, alternative, see. Prefer specific relations over `see`.

## 4. Fill critical gaps (sparingly)

If a concept that a student of this skill obviously needs is missing, you may write a new note, but only if the library covers it: search `90-library/text/` with grep, read the passage, and cite the real source and location. New note IDs: `<CODE>-99NN` (99 = Phase 2; NN = 01, 02 …). Keep it to the few that matter most (typically 0–6 per skill).

## 5. Refine

- Fix titles that are vague; make sure each note is atomic, in English with American spelling and the book's own terms, 150–400 words, with all sections.
- Check that `level` (1/2/3) and `kind` are right.
- Set `status: growing` on notes you revised and linked; keep `seed` on notes you did not touch.

## 6. Write the hub `20-skills/<slug>/SKILL.md`

Use `_meta/templates/skill.md`. It is both the human hub of the skill and a Claude Code skill file, so:

- Frontmatter: `name: <slug>`, `description:` (English, 1–3 sentences: what the skill covers AND when to use it, with concrete trigger tasks, e.g. "Use when you write or evaluate a creative brief, …"), `code`, `domain`, `type: skill`.
- **Competencies** ("What mastering this skill means"): 5–8 observable "You can…" statements (C1…C8).
- **Note map (learning path)**: ALL notes of the skill, grouped in 3–6 meaningful sections, ordered as a learning path (fundamentals first). Each entry: `- [[ID]] short title: one clause on why it is here`. The order matters: final IDs will be renumbered in this order.
- **Main sources**: a table of the sources most used by this skill, with what each is good for and a ★ rating (take the ratings from the source notes).
- **Neighboring skills**: links to neighboring skill hubs (`[[ADV]]`, …) with one clause each.
- **How an AI agent uses this skill**: 3–6 concrete task playbooks ("When you are asked for X: read [[…]], apply [[…]], check with [[…]]; cite the IDs"), plus the reminder that the full texts are in `90-library/text/`.
- Keep the `<!-- auto:notes:start -->` / `<!-- auto:notes:end -->` markers at the end (generated later).

## 7. Validate and report

Run `python3 tools/kb.py check`, open `_meta/health.md`, and fix problems in your files. Broken links pointing to IDs you dropped are expected until the redirect step, but links *you* write must point to existing IDs.

Write `_meta/reports/P2-<CODE>.md` (one per skill): notes before/after, merges done, new notes, cross-skill duplicates found, remaining gaps, and anything the orchestrator should know.

Your final reply: ≤ 150 words.
