# Report P2-PRT: Phase 2, portfolio

Agent: P2-PIT-PRT-CLI · skill: `portfolio` (PRT) · date: 2026-10-01

## 1. Notes before / after

| | Count |
|---|---|
| Notes before | 27 (26 from G14 (Fenn, Kubišová, Morgan); PRT-0501 from G05 (Peters)) |
| Merges (DROP) | 0 |
| New notes | 0 |
| Notes after | **27** |
| `status: growing` | 22; left as `seed` after checking (they were already well linked): PRT-1401, PRT-1406, PRT-1417, PRT-1418, PRT-1423 |

`merges-PRT.txt` is empty. The closest pairs are principle + method, and they stayed separate, linked to each other:

- PRT-1405 (quality beats volume) / PRT-1422 (the YES-NO-MAYBE method);
- PRT-1402 (two documents) / PRT-1423 (three types of portfolio);
- PRT-1409 (the structure of the case study) / PRT-1424 (the text on the page);
- PRT-1417 (the visual CV, Morgan) / PRT-1426 (the functional CV, Kubišová): two philosophies, with the tension noted in PRT-1418.

## 2. What I did

- **Links:** I added 24 typed links in 22 notes (23 of the 27 notes now have at least one link to another skill or another book group). Each note now has 3–6 links; the target skills are PIT, CLI, ART, CPY, STO, BRD, MKT, IDE, SOC, HIS and BRF.
- **Convergence written in the text:** PRT-0501: Peters (personal projects) and Fenn (show only the work you want to do) say the same thing. I added SRC-048 to `sources`.
- **SKILL.md** written in full: 7 competencies, a path in 6 sections (Foundations → Raw material and selection → Structure, rhythm, format → Writing and page design → The application package → Distribution, personal brand, critique), 5 sources with ratings, 6 neighboring skills, 6 playbooks. The renumbering order is checked with `renumber --dry-run` (PRT-1401 → PRT-001 … PRT-1413 → PRT-027).

## 3. New notes

None. The skill covers portfolio building well. The real gaps (below) have no coverage in the library.

## 4. Duplicates and overlaps with other skills (not touched, only linked)

| My note | Note in another skill | Nature of the overlap |
|---|---|---|
| PRT-1419 | CLI-1402 | The "Dream 10" list of agencies is Dream 100 applied to a career. Linked. |
| PRT-1403 | IDE-0712 | The work journal and the inspiration bank: the same discipline of collecting. |
| PRT-1402 | PIT-1418 (principle 6) | The presentation deck ≠ the document left behind. The same rule, in Fenn and in Colenso. |
| PRT-1409 | PIT-1416 | Brief/What I did/Results versus SOLVE: alternative structures for a case. `alternative` in both directions. |
| PRT-0501 | IDE-0501 | Peters's personal inspiration projects. Related, not duplicates. |
| PRT-1414 | BRD-0503 | Hoffman's sentence is a positioning statement. There is no other personal branding note in BRD. |

## 5. Remaining gaps

- **No advertising-specific source** for the portfolio: the copywriter's or art director's book, the festival case film, the strategist's portfolio. The notes transfer from UX and architecture, and the questions in the notes flag the transfer explicitly (PRT-1407, PRT-1409).
- **The interview itself** (typical questions, salary negotiation, the practical test) is not covered.
- **The physical production of the printed portfolio** (SRC-046, steps 5–7) was not turned into notes. It is technical and belongs rather to ART.
- Morgan (SRC-047, 2014) has outdated data and platforms (Google+, Klout). The notes flag them, and the PRT-1418 debate puts them in context.

## 6. For the orchestrator

- `kb.py check`: 0 problems in `20-skills/portfolio/`.
- A few notes have 450–520 words by the `kb.py` count (PRT-1407, PRT-1411, PRT-1412, PRT-1418, PRT-1426): above the target of 400, below the threshold of 650. I left them whole, because each remains atomic.
- The empty file `PRT-0501.md` at the KB root (0 bytes) is not the real note, which is in `20-skills/portfolio/notes/`. It should be deleted.
- Taxonomy suggestion, taken from G14: the PRT scope in `skills.json` could explicitly mention "career and employability" (CV, LinkedIn, network), because PRT-1414, PRT-1419, PRT-1420 and PRT-1426 belong to it.
