# ADC knowledge base

A knowledge base for the ADC school (advertising, brand, creative, digital), built from 49 sources: books on marketing, advertising, consumer psychology, branding, briefs and creative ideas, advertising history, digital marketing, social media, experiential marketing, AI, pitching, portfolios and B2B sales.

This is the English edition of [hornyshepard/adc-knowledge-base](https://github.com/hornyshepard/adc-knowledge-base) (the Romanian original).

**In numbers:** 49 sources · 778 permanent notes · 17 skills in 6 domains · 6 cross-cutting maps · ~7,700 links · 52 debate notes (where the authors disagree).

## The method: Zettelkasten + skills + AI

| Idea | How it is applied here |
|---|---|
| **Atomic, linked notes** (Zettelkasten) | One idea per note, written in English in our own words with the books' own terms, with a permanent ID (`BRD-007`) and typed links that give a reason (`foundation`, `extends`, `contradicts`…). |
| **Organized by skills** | 17 skills in 6 domains. Each skill has a hub `SKILL.md` (meta-file): competencies, learning path, sources, playbooks for agents. |
| **Automatic linking** | `tools/kb.py suggest` proposes links between similar notes (TF-IDF), which a person or an agent confirms. |
| **The CEQRC flow** | Capture → Explain → Question → Refine → Connect, described in `_meta/conventions.md` and `CLAUDE.md`. |
| **Agentic execution** | Claude Code reads the folder: `CLAUDE.md` tells it how to navigate, and every `SKILL.md` is compatible with the Claude skill format. |

## Structure

```
ADC-Knowledge-Base/
├── INDEX.md                 # the entry point: domains → skills
├── CLAUDE.md                # instructions for AI agents
├── 00-inbox/                # quick, unprocessed notes (Capture)
├── 10-sources/              # one reading sheet per book (SRC-001 … SRC-049)
├── 20-skills/
│   └── <skill>/
│       ├── SKILL.md         # the skill hub (meta-file + Claude skill)
│       └── notes/           # atomic permanent notes (BRD-001-….md)
├── 30-maps/                 # 6 cross-cutting maps (see below)
├── 90-library/              # the extracted full texts (local only, not in git)
├── .claude/skills/          # links to the 17 skills, for Claude Code
├── _meta/
│   ├── conventions.md       # the rules of the base
│   ├── reports/             # reports of the agents that read the books
│   ├── skills.json          # the taxonomy: domains, skills, kinds, relations
│   ├── sources.json         # the source register
│   ├── templates/           # templates: zettel, source, skill, map, fleeting
│   ├── catalog.json/.csv    # generated: all notes
│   ├── graph.json           # generated: nodes + typed links
│   ├── coverage.md          # generated: skill × source coverage
│   └── health.md            # generated: broken links, orphans, missing fields
└── tools/
    ├── kb.py                # check, build, suggest, merge, redirect, renumber, new, stats
    ├── extract_texts.py     # PDF/EPUB/AZW3/DOCX → text
    └── transcribe_audiobook.py
```

## The skills

| Domain | Skills |
|---|---|
| D1 Strategic thinking | MKT Marketing fundamentals and strategy · INS Consumer psychology and insight · BRD Brand strategy · ADV Advertising and communication strategy · BRF The creative brief |
| D2 Creative | IDE Ideation and creative thinking · CPY Copywriting and message · ART Art direction and visual identity · STO Storytelling and content |
| D3 Channels and execution | DIG Digital and performance marketing · SOC Social media and influencer marketing · EXP Experiential marketing |
| D4 AI and the future of marketing | AIM AI in marketing and advertising |
| D5 Profession and career | PIT Pitch and presentation · PRT Portfolio and personal branding · CLI Client, sales and business |
| D6 Advertising culture | HIS Advertising history and culture |

## The cross-cutting maps

| Map | What it is for |
|---|---|
| MAP-001 The agency workflow | the path of a project, from the business problem to the pitch and measurement: the backbone of the course |
| MAP-002 Effect models and customer journey models | AIDA, FCB, Rossiter-Percy, 5A, the digital journey, 7A… compared, with their limits |
| MAP-003 Ethics and regulation | truth and proof, the limits of persuasion, native advertising, data and AI, representation, rights |
| MAP-004 Debates | all the notes where the authors contradict each other: seminar material |
| MAP-005 Library guide | the 49 sources ranked by relevance (★1–5), with what to read in full and what to avoid |
| MAP-006 The ADC course path | four modules + the professional skills in parallel, with the starting point in each skill |

## How to use it

**As a person (Obsidian or any Markdown editor):** open the folder as a vault in Obsidian and start from `INDEX.md`. The Obsidian graph shows the links between notes.

**With Claude Code:** open a session in this folder. Claude reads `CLAUDE.md`, and the 17 skills are exposed in `.claude/skills/`, so they activate on their own when a request matches their description. Claude starts from the right `SKILL.md` and cites the IDs of the notes it uses. Example requests:
- "Write a creative brief for … using the creative-brief skill."
- "Compare the customer journey models in the base and say where the authors disagree."
- "Prepare the structure of a 10-minute pitch for …"

**Maintenance:**

```bash
python3 tools/kb.py check
```

```bash
python3 tools/kb.py build
```

```bash
python3 tools/kb.py suggest --skill brand-strategy
```

## Copyright

The notes are our own summaries and syntheses, with references to chapter and page. The repository does not contain the books or their full text. The texts are regenerated locally from your own copies of the books (see `90-library/README.md`).
