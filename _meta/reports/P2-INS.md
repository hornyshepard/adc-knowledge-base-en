# Report P2-INS: integration of the consumer-insight skill (INS)

Agent P2-INS, Phase 2. Skill: `20-skills/consumer-insight/`.

## 1. Numbers

| | Before | After |
|---|---|---|
| Permanent notes | 98 | 95 (98 − 4 merged + 1 new) |
| Notes with `status: growing` | 0 | 95 |
| Notes with 2–6 typed links and at least one to another book group or another skill | 76 | 95 |
| Notes with no link outside their own Phase 1 group (e.g. INS-04xx only to INS-04xx) | 22 | 0 |
| Body length (`kb.py`) | 282–516 words | 303–526 words |

`kb.py check`: no problems in the `consumer-insight` files at the last run.

## 2. Merges (in `merges-INS.txt`)

| DROP | KEEP | What was integrated |
|---|---|---|
| INS-0107 (ELM, Grewal-Levy) | INS-0430 (ELM/HSM, Fennis-Stroebe) | The textbook version of ELM (Laura/Macy's), Percy's reading (low risk: the execution is enough; high risk: the argument must be believed), plus a "where the authors converge" paragraph; sources SRC-012 + SRC-001 + SRC-049. The three types of decision (extended, limited/impulse, habit) were moved into **INS-0109**, retitled "Involvement and perceived differences between brands set the type of decision…". |
| INS-0446 (psychoanalysis, Parsons et al.) | INS-0601 (motivation research, Fernández Gómez) | Dichter (three layers of motives, the convertible as "mistress", "moral permission to have fun without guilt"), Bernays, the Packard/Vicary critique, the rehabilitation as "sensitising concepts" (Williamson, Klein). The note was retitled and moved to `kind: debate`; the explicit disagreement: Fernández Gómez (a sales machine) vs. Parsons et al. (a useful vocabulary) vs. Fennis-Stroebe (without an experiment it is not evidence). The examples of projective tasks went into **INS-1209**. |
| INS-0501 (Braig, the insistent "why" and frictions) | INS-0702 (McTigue, "what" → "why") | Braig's frictions (KABOOM, Clorox), "why does it matter?" repeated, the Ford/Jobs critique; the convergence of the three sources and the tension about focus groups (Braig vs. McTigue). The part on the persona went into **INS-1306** (source SRC-014 added). |
| INS-0445 (postmodern consumption, Brown via Parsons) | INS-1206 (the postmodern consumer, Firat & Venkatesh via Batat) | A single table with the two lists of traits, linking value, solid/liquid consumption, the Parsons et al. critique and post-postmodernism; level 3 → 2. |

## 3. New notes

- **INS-9901**: *The insight checklist: eight checks before a "truth about the target" goes into the brief* (checklist, level 2). The gap: the final step of the path (checking the wording) was scattered across INS-0701, INS-0602, BRF-0715, BRF-0719. The note gathers the tests from SRC-022 (ch. 4: Grand Furniture, Luvs, the meat packaging, Stark revised), SRC-019 (outil 19, the dilemma), SRC-025 (ch. 6: Bullmore, Angear, fixed/dynamic insight) and SRC-023 (Singleton "helpful insight", the Euro RSCG triangulation). All passages were checked in `90-library/text/`. It forms the bridge INS → BRF ([[BRF-0702]], [[BRF-0703]]).

## 4. Links and integration across authors

The main gain: the notes of G04 (Fennis & Stroebe), G15 (Percy & Rosenbaum-Elliott), G06 (Milavsky, *La boîte à outils*), G01 (Grewal & Levy), G12 (Batat), G13 (Struhl) and G07 (McTigue) now cite each other. Convergences and disagreements written explicitly in the body of the notes:

- **Involvement** belongs to the person, not the product: Fennis-Stroebe (INS-0401), Grewal-Levy (INS-0109), Percy (INS-1503). INS-1503 `contradicts` ADV-0402: the Fennis-Stroebe critique of the Rossiter-Percy grid hits its use by category, not Percy's definition.
- **Attitude**: Grewal-Levy (ABC, INS-0106) vs. Percy (no conation, INS-1506): a `contradicts` link in both directions.
- **Subliminal/unconscious**: INS-0439 (small, conditional effects) ↔ INS-1511 (no effect) ↔ INS-0402/0412/0414/0421: `contradicts`, with a tension paragraph.
- **Fear**: INS-0433 (the meta-analysis: more fear, more persuasion) ↔ INS-1507 and ADV-1532 (moderate fear, inverted U).
- **Source credibility**: INS-0606 (Milavsky) ≈ INS-0432 (Fennis) ≈ INS-1505 (VisCAP).
- **Focus groups and recall**: four sources converge (INS-1303, INS-0419, INS-0412, ADV-1530, INS-0702).
- **The brake as an insight**: INS-0417 (alpha/omega) ≈ ADV-0609 (Joannis) ≈ INS-0602 (the dilemma) ≈ BRF-0714 (Stark).
- **Motivation**: three typologies linked as `alternative` (INS-0102, INS-0428, INS-1504).
- **Working memory and the Google effect**: INS-0411 ↔ INS-1510; INS-0443 ↔ INS-1509.

## 5. Duplicates across skills (linked, not merged)

| INS note | Note in another skill | Relation set |
|---|---|---|
| INS-0406 (the pioneer sets the attribute agenda) | BRD-0514 (pioneer, follower, late entrant): the same Carpenter & Nakamoto research | `see` + a paragraph in INS-0406 |
| INS-0439, INS-1511 (subliminal) | HIS-0817 (the subliminal myth) | `see` in both |
| INS-1306 (personas, not segments) | DIG-1006 (buyer persona ≠ target group), DIG-0912 | `see` |
| INS-0427 (expectancy-value) | BRD-1503 (the positioning benefit with expectancy-value) | `application` |
| INS-0417 (alpha/omega) | ADV-0609 (Joannis's psychological axis) | `alternative` |
| INS-1303, INS-0412 | ADV-1530 (the pretest without focus groups and without recall) | `application` |
| INS-0603 (quantitative vs. qualitative) | MKT-0126 | `see` |
| INS-0605 (the fast brain) | ART-0501 (design works in System 1) | `see` |

## 6. Remaining gaps

- **Loss aversion, prospect theory, the endowment effect**: absent from the library (grep with no results in SRC-001, 012, 013, 021), so I did not create a note.
- **Neuroscience in brand research** (*Kellogg on Branding*, ch. 14): the library covers it, but there is no note; a candidate for INS or AIM.
- **Useful cross-cutting maps** (for `30-maps/`): "Research and measurement" (INS-05 + the ADV pretest + the AIM trade-off + DIG A/B) and "The ethics of persuasion" (INS-0420, 0434, 0438, 0105, 1509; CPY-0401; BRD-0402), as the G04 report also proposed.

## 7. For the orchestrator

- The order of the "Note map" in `SKILL.md` (6 sections, 18 + 24 + 23 + 10 + 16 + 4 = 95 notes) is the intended renumbering order.
- Titles changed (the file slug is kept until `renumber`): INS-0109, INS-0601, INS-0702.
- Targets already re-pointed in my notes, following `merges-ADV/BRD/EXP.txt`: ADV-0102 → ADV-0401, ADV-0106 → ADV-0604 (in INS I chose better-fitting targets: CPY-0403, ADV-1513, ADV-1511), BRD-0104 → BRD-0512, BRD-0205/BRD-0401 → BRD-0606, EXP-0204 → EXP-1210, EXP-1205 → EXP-0901. If other skills merge more after this report, the final redirect will cover them.
- Links from other skills to my merged notes (to be redirected): ADV-0106 and DIG-0104 → INS-0107; ADV-0501 and ADV-0502 → INS-0501; EXP-0401 and MKT-0401 → INS-0445; SRC-001, SRC-013, SRC-014 → the merged notes.
- The `<!-- backlinks -->` sections in the rewritten notes were emptied; `kb.py build` regenerates them.
