# Conventions of the ADC knowledge base

This file is the "constitution" of the knowledge base. Every new note, whether written by a person or by an AI agent, follows the rules here. `tools/kb.py check` checks most of them automatically.

## 1. The method: a Zettelkasten organized by skills

The base combines two ideas:

1. **Zettelkasten** (Niklas Luhmann): small, *atomic* notes (a single idea per note), written in your own words, each with a permanent ID and explicitly linked to other notes. The value is not in the notes but in the **links**.
2. **Skills**: every note has a "home", the main skill it develops. A skill is a folder with a hub file `SKILL.md` (meta-file) that says which competencies it covers, in what order the notes are learned and how an AI agent uses them.

The result: you can navigate **vertically** (by skill, as in a course) or **laterally** (by links, as in a Zettelkasten).

## 2. Note types

| Type (`type`) | What it is | Where it sits | ID |
|---|---|---|---|
| `fleeting` | Quick, unprocessed note (capture) | `00-inbox/` | no ID |
| `source` | Reading note: the sheet of a book | `10-sources/` | `SRC-001` |
| `zettel` | Permanent, atomic note | `20-skills/<skill>/notes/` | `BRD-001` |
| `skill` | The hub of a skill (meta-file) | `20-skills/<skill>/SKILL.md` | the skill code, e.g. `BRD` |
| `map` | Cross-cutting map (structure note / MOC) | `30-maps/` | `MAP-001` |

## 3. IDs and file names

- The ID of a permanent note = **the code of its main skill + a number**: `BRD-007`. The ID never changes after publication, even if the note changes its title.
- The skill codes are in `_meta/skills.json` (MKT, INS, BRD, ADV, BRF, IDE, CPY, ART, STO, DIG, SOC, EXP, AIM, PIT, PRT, CLI, HIS).
- File name = `ID-slug.md`, where the slug comes from the title, in lowercase, without diacritics, with hyphens, at most ~60 characters. Example: `BRD-007-positioning-is-a-distinct-place-in-the-mind.md`.
- *Temporarily*, during the construction phase, IDs may have 4 digits (`BRD-0503` = group 05, note 03). At launch, `kb.py renumber` turns them into final 3-digit IDs, in the order of the learning path in `SKILL.md`.

## 4. Links

- Syntax: a wikilink with the ID: `[[BRD-007]]`. `kb.py build` normalizes them to `[[BRD-007-slug|BRD-007]]` so they work both in Obsidian and for agents.
- Link to a skill: `[[BRD]]` (becomes a link to `20-skills/brand-strategy/SKILL`).
- Link to a source: `[[SRC-014]]`.
- **Every link has a reason.** In the "Links" section of a note, each line has the form:

  `- **relation** [[ID]]: why they are linked (one sentence)`

  The allowed relations (a controlled vocabulary, in `_meta/skills.json`):

  | relation | meaning |
  |---|---|
  | `foundation` | my note rests on the target (read the target first) |
  | `extends` | my note details / develops the target |
  | `application` | my note applies the target in a concrete context |
  | `example` | my note is a case / example for the target |
  | `contradicts` | my note is in tension with the target |
  | `alternative` | an alternative model to the target |
  | `see` | a general thematic link |

- Links can also appear in the text of the note (inline), but the ones in "Links" are the typed ones, used for the graph.
- Backlinks (who points to a note) are generated automatically by `kb.py build`, between the `<!-- backlinks:start -->` and `<!-- backlinks:end -->` markers. Do not write them by hand.

## 5. Frontmatter (YAML metadata)

A simple subset of YAML: `key: value`, inline lists `[a, b]` and lists with `- item`. No nested structures.

### Permanent note (`zettel`)

```yaml
---
id: BRD-007
title: Positioning is a distinct place in the consumer's mind
type: zettel
kind: concept            # concept | framework | principle | method | case | checklist | debate
skill: brand-strategy    # the slug of the main skill (the folder the note sits in)
also: [advertising-strategy, consumer-insight]   # other skills where it is relevant (optional)
level: 1                 # 1 Foundation | 2 Practice | 3 Advanced
tags: [positioning, differentiation]
sources:
  - SRC-014 | ch. 2, pp. 31–40
  - SRC-003 | ch. 4
status: seed             # seed | growing | evergreen
---
```

### Reading note (`source`)

```yaml
---
id: SRC-014
title: Kellogg on Branding in a Hyper-Connected World
type: source
authors: [Alice M. Tybout, Tim Calkins]
year: 2019
language: en
file: Kellogg on Branding.pdf
text: 90-library/text/kellogg-on-branding.txt
skills: [brand-strategy, marketing-fundamentals]
relevance: 5             # 1-5, how useful the book is for an advertising school
level: 2
---
```

## 6. What a good permanent note looks like

1. **The title is a precise claim or concept**, not a vague subject. Good: "A good brief has a single central proposition". Bad: "About the brief".
2. **Atomicity**: one idea per note. If you catch yourself writing "and also…", split the note in two and link them.
3. **In your own words**: paraphrase, do not copy. At most one short verbatim quote (under 15 words) per note, in quotation marks, with the source.
4. **Self-contained**: the note can be understood without having read the book.
5. **Applicable**: the "Application" section says what a student / a creative / a strategist concretely does with the idea.
6. **Anchored in sources**: every note cites at least one source (`SRC-…`), with a chapter or page where possible.
7. **Linked**: at least 2 typed links (no orphan note).
8. Length: 150–400 words in the body of the note. Complex models can have a table.

The full template: `_meta/templates/zettel.md`.

## 7. Language and style

- The notes are written in **English**, with American spelling (color, behavior, analyze), except in book titles, quotes and proper names.
- Use the books' own terms, model names, labels and examples, in the book's exact wording: "frame of reference", "points of parity", "the Rossiter-Percy grid", "the CBBE pyramid (Keller)". Industry terms (brief, insight, pitch, big idea, KPI) stay as they are.
- At most one verbatim quote per note, under 15 words, in straight double quotes. For the French sources, give the original French term in italics at its first mention, e.g. "the copy strategy (*copy-stratégie*)"; a quote from them stays in French, followed by an English translation in square brackets.
- No em dashes in our own prose: use a colon, a comma, parentheses or a full stop. En dashes only in number ranges (pp. 6–7).
- Tone: clear, direct, useful for a student who wants to work in an agency.

## 8. The CEQRC workflow (how the base grows)

| Step | What you do | Where |
|---|---|---|
| **C**apture | You quickly note the idea / the quote / the page | `00-inbox/` (a `fleeting` note) |
| **E**xplain | You rewrite it in your own words, as an atomic note | `20-skills/<skill>/notes/` |
| **Q**uestion | You add questions: where does it not apply? who contradicts it? | the "Questions" section |
| **R**efine | You shorten, sharpen the title, check the source, raise the `status` | the note itself |
| **C**onnect | You add typed links, you place it in the map in `SKILL.md` | "Links" + `SKILL.md` |

Then you run `python3 tools/kb.py build` (backlinks, indexes, graph) and `python3 tools/kb.py suggest` (proposals for links you have not made yet).

## 9. Automatically generated meta-files (do not edit them by hand)

| File | Content |
|---|---|
| `_meta/catalog.json`, `_meta/catalog.csv` | all notes with their metadata |
| `_meta/graph.json` | the graph: nodes (notes) + edges (typed links) |
| `_meta/coverage.md` | the skill × source matrix and the coverage gaps |
| `_meta/link-suggestions.md` | pairs of similar notes, not yet linked |
| `_meta/health.md` | the `check` report: broken links, orphans, missing fields |
| the `<!-- auto:... -->` sections in `SKILL.md` and `INDEX.md` | generated note lists |
