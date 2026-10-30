# Report P2-PIT: Phase 2, pitch-presentation

Agent: P2-PIT-PRT-CLI · skill: `pitch-presentation` (PIT) · date: 2026-10-01

## 1. Notes before / after

| | Count |
|---|---|
| Notes before | 35 (32 from G14 (Colenso, Nishad); PIT-0501 from G05 (Peters); PIT-0601, PIT-0602 from G06) |
| Merges (DROP) | 0 |
| New notes | 1 (PIT-9901) |
| Notes after | **36** |
| `status: growing` | 35 (all except PIT-1432, checked and left as `seed`) |

`merges-PIT.txt` is empty: I found no real duplicates in the skill. The close pairs are concept + application, or sources that complement each other, and they stayed separate, linked to each other: PIT-1424 (nerves, Colenso) / PIT-1432 (the Colenso-Nishad debate), PIT-1420 (the stages of rehearsal) / PIT-1431 (the video loop), PIT-0602 (phrasing, Muller) / PIT-1425 (energy and voice, Colenso).

## 2. What I did

- **Links:** I added 47 typed links in 34 notes. Almost all Colenso notes had only internal PIT links. Now each note has 3–6 links, and 33 of 36 have at least one to another skill or another group (INS, CPY, STO, BRF, ADV, ART, MKT, CLI, PRT, IDE).
- **Convergences and disagreements written in the text** (with the source added to `sources`):
  - PIT-1408: the rule of three messages in Colenso and Nishad, plus Milavsky (SRC-021, CPY-0605);
  - PIT-1422: the P + + – P formula is grounded in the two-sided message (Fennis & Stroebe, SRC-012, CPY-0402);
  - PIT-1423: the "Relate" step, backed by Milavsky (SRC-021, INS-0607);
  - PIT-1407: Know-Feel-Do in tension with the critique of hierarchies of effects (SRC-012, ADV-0401, `contradicts`);
  - PIT-1416: "the hero is the client" in Colenso and in Richards & McLean (SRC-040, STO-1303);
  - PIT-0602: the shared Muller-Colenso diagnosis (SRC-043).
- **Links restored after other agents' merges:** PIT-0601 → ADV-1506 (replaces ADV-0612) and PIT-1407 → ADV-1502 (replaces ADV-0614), following `merges-ADV.txt`.
- **SKILL.md** written in full: 7 competencies, a path in 6 sections (Foundations → Discover → Distil & Design → Drill & Debrief → Deliver → Presenting creative work to the client), 7 sources with ratings, 6 neighboring skills, 6 playbooks. I checked with `kb.py renumber --dry-run` that the order of the future IDs follows the path (PIT-1401 → PIT-001 … PIT-0501 → PIT-036).

## 3. New note

| ID | Title | Sources |
|---|---|---|
| PIT-9901 | Presenting creative work to the client follows a ritual: the strategy reread, the idea revealed, questions instead of solutions, the next step asked for | SRC-021 ch. 7–8 (pp. 125–135); SRC-022 ch. 8; SRC-017 ch. 2; SRC-025 ch. 1 (Greg Hahn) |

Why: the brief asked for a clear path for "presenting creative work to the client", and G14 had flagged that it was missing. The note puts together four perspectives (the client-side manager, the client, the designer, the creative director) in five moves. It opens section 6 of the map, alongside PIT-0601 and PIT-0501 and the readings from other skills: BRF-0711, BRF-0712, CPY-0606, CLI-0602, CLI-0701, CLI-9905.

## 4. Duplicates and overlaps with other skills (not touched, only linked)

| My note | Note in another skill | Nature of the overlap |
|---|---|---|
| PIT-0501 | ART-0507 | Both describe the first presentation of the 15 marks (Peters). PIT keeps the selling and the feedback, ART the process. Linked through `foundation`. |
| PIT-1416 | STO-1303 | "The hero is the client, not the brand", from different sources (Colenso/Miller vs. Richards & McLean). Linked through `see`. |
| PIT-1407 | ADV-0401, ADV-1502, BRF-0719 | Know-Feel-Do versus think-feel-act and the communication effects. Related models, not duplicates. |
| PIT-1408 | CPY-0605, BRF-0707 | The rule of three messages or arguments and the single benefit. Converging principles. |
| PIT-1412 | INS-0440 | Social proof (Cialdini). |
| PIT-9901 | BRF-0711 | The same creative meeting seen from both sides. Complementary. |

## 5. Remaining gaps

- No source on the agency's **new business pitch** as a format: credentials, chemistry meeting, the procurement-led pitch. Colenso touches it only in passing (PIT-1403, PIT-1413, PIT-1414).
- **Presenting data** (charts, figures spoken on stage) is only in PIT-1418, principle 2.
- The peak-end rule and the study on first impressions in 33 ms come indirectly, through Colenso; INS has no source note for them.
- Nishad (SRC-044) is thin: it looks like the transcript of a video course. The notes based on it (PIT-1431, PIT-1432) use it only as a second voice.

## 6. For the orchestrator

- `kb.py check`: 0 problems in `20-skills/pitch-presentation/`.
- At the KB root there are two empty files (0 bytes), probably created by mistake: `ADV-0603.md` and `PRT-0501.md`. `kb.py` ignores them (they have no frontmatter), but they should be deleted. I did not touch them, because they are outside my folders.
- The map in SKILL.md also contains IDs from other skills, on "From other skills…" lines. `renumber` ignores them; I checked.
