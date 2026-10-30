# Report P2-STO: Phase 2, integration of the storytelling-content skill

Agent: P2-SOC-STO (also owns SOC; see `P2-SOC.md`). Date: 2026-10-01.

## 1. Totals

| | Before | After |
|---|---|---|
| Own STO notes | 41 | **41** (40 kept + 1 new) |
| Merges (DROP → KEEP) | n/a | 1 (`merges-STO.txt`) |
| New notes | n/a | 1 (STO-9901) |
| Status | 41 seed | 41 growing |
| Levels | n/a | 10 × 1, 30 × 2, 1 × 3 |
| `SKILL.md` | provisional hub | rewritten: 7 competencies, a map in 6 sections (all 41 notes), sources with ★, neighbors, 5 playbooks |

All notes have 2–6 typed links and at least one to another skill or another book group. `kb.py check`: no problems in the STO files.

## 2. Merges and restructuring

| DROP | KEEP | What was integrated |
|---|---|---|
| STO-0903 | STO-0202 | The content marketing strategy cycle: Kotler's eight steps (4.0) + Zahay's four steps + the six-step variant of Barre & Gayrard-Carrera. The note says where they converge (the evaluation-restart loop) and where they differ (the order: objectives before the idea in Kotler, creation first in Zahay; amplification through influencers vs. curation). The principle that content "contains information customers want to use" moved into STO-0901, the Google study on unskipped ads into STO-1104. |

**The "hero's journey" cluster.** The pointer in the task named STO-0902, but STO-0902 is the Chaffey content matrix, not a note about the hero. The real cluster: STO-1201, STO-1303, STO-0702, STO-1101, STO-1103 (plus STO-0501 and STO-0905, close by). No note was a clean duplicate, so I made **one core note and application notes**, without deleting anything:

- **STO-1201** became the core note (level 1): Campbell/Vogler, the versions from five books (Batat, Mueller & Rajaram, Braun & Landa, Richards & McLean, Sawhney), why it works (narrative transportation, transformation through the brand) and the "who is the hero" debate (the customer for Richards & McLean, Sawhney, Braun & Landa; also the founder for Batat; the guide instead of the hero on social, in Mueller & Rajaram).
- Applications, with `foundation` toward the core: **STO-0702** (the spot: C.O.W. + B → T and three acts), **STO-1303** (content: the acts as a buying cycle, the B2B variant), **STO-1103** (social: the seven turning points as questions); **STO-1101** stays a `debate` and `contradicts` the core.
- Batat's four ingredients of a story moved into **STO-0905**, compared with the Kindra Hall grid and with the Kotler 3.0 model (STO-0201).

**Other integrations:** STO-1112 (UGC) now brings together Mueller & Rajaram, Barre & Gayrard-Carrera, Labrecque (5C), Nishad and Glenister, with the debate "implicit call vs. explicit mechanics"; STO-0601 lost the list of steps (a duplicate of STO-0202) and keeps the rules of legitimacy and renewal.

## 3. Checking STO-0702 ("C.O.W.")

I searched in `90-library/text/shareworthy-robin-landa.txt` (lines ~1712–1729, ch. 5, p. ~104). The book gives the map "Protagonist (represents the target audience) → Obstacle (conflict) → Want or need or desire + Brand (facilitator) → Transformation → Resolution and call-to-action" and right below it writes **"C.O.W. + B→T"**, but **does not explain any letter**. The rewritten note says only what follows from the text: O, W, B and T correspond to the capitalized terms in the map (*Obstacle, Want, Brand, Transformation*); for C the book gives no key (the first element is called *Protagonist*), so the formula is used as shorthand for the map. The title no longer suggests that C = protagonist. I also checked in the text the three acts (25/50/25%), the apotheosis, Orchard Thieves and Reddit (pp. 103–118).

## 4. New note

- **STO-9901**: *On social media, other people's content is taken over through the share function or with written permission, and the people filmed keep the right to their own image* (SRC-034, ch. 2.5, pro tip by D. Mrkaja, pp. 82–85 in the PDF pagination used by G11). The gap had been flagged by G11 (§4). In parallel, the DIG agent wrote **DIG-9902** (Sachdev: trademarks, copyright, fair use, CC); I narrowed STO-9901 to the rules of social production (sharing vs. reposting, written permission, music, the right to one's image, minors) and linked it `foundation` → DIG-9902.

## 5. Duplicates across skills (linked, not touched)

- **STO-0709** (representation checklist, *Shareworthy*) ↔ **ADV-0302** (inclusive advertising on three axes, Ejeke): parallel lists; `alternative`.
- **STO-9901** ↔ **DIG-9902**: partial overlap on Creative Commons licenses (see §4).
- **STO-0601** ↔ **BRD-1201** (from brand content to brand culture, Batat).
- **STO-0901** ↔ **ADV-0301** (the content vs. advertising debate, Wuebben): `contradicts`.
- **STO-1115** ↔ **ADV-0504** (virality comes from mass broadcasting): `contradicts`.
- **STO-0701 / STO-0704 / STO-1115** ↔ **INS-0444** (high-arousal emotions get shared): `foundation`.
- **STO-1201 / STO-1101** ↔ **PIT-1416** (in a pitch, the hero is the client).
- **STO-0707 / STO-1114** ↔ **BRD-0402**, **BRD-0509** (purpose, greenwashing).
- **STO-1109** ↔ **ART-0705** (word and image create tension, they do not repeat each other); **STO-1102** ↔ **ART-0803**.
- **STO-1105** ↔ **CPY-0815** (Burma-Shave, serial copy).

## 6. Remaining gaps

- **Content production with a smartphone** (framing, sound, editing, aspect ratio): a large part of SRC-034, tutorial-like, between STO and ART; no note.
- **Audio/podcast storytelling** and **the story in B2B** beyond STO-1303.
- **Booker's seven plots** appear only in STO-0501; the Pixar "story spine" is only in PRT-1416.
- **Romanian law** (copyright, the right to one's image): STO-9901 describes the German rules from the book and asks for the local law to be checked.

## 7. For the orchestrator

- Links from other skills to STO-0903 (to be redirected to STO-0202): DIG-0925, DIG-0930 (DIG-0912 was merged by DIG), plus SRC-029.
- In my files I already redirected the links to other agents' merges (BRD-0205→BRD-0606, DIG-0912→DIG-1006). Still, run `redirect` for later merges.
- `SKILL.md` cites no IDs in "Competencies", so that `renumber` follows the map (STO-0701, STO-1201, STO-0702 … STO-0710).
- STO-0202, STO-0702 and STO-1201 have 440–445 words by the `kb.py` counter (long H1 title + tables); the prose is around 400.
