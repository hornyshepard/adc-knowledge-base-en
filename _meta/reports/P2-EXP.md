# Report P2-EXP: integration of the experiential-marketing skill (EXP)

Agent P2-EXP-AIM, Phase 2. Skill: `20-skills/experiential-marketing/`. (The same agent also integrated AIM; see `P2-AIM.md`.)

## 1. Numbers

| | Before | After |
|---|---|---|
| Permanent notes | 33 | 31 (33 − 2 merged, 0 new) |
| Notes with `status: growing` | 0 | 31 |
| Notes with 2–6 typed links | 31 (EXP-1201 had 9, EXP-1202 had 8) | 31 |
| Notes with no typed link outside their own Phase 1 group | 7 | 0 |
| Notes with at least one link to another skill | 26 | 30 |
| Typed links, total | 121 | 162 |
| Body length (`kb.py`-style count) | 338–492 | 351–459 |

`kb.py check`: no problems in the EXP files at the last run. The remaining broken links that concern EXP come from other files (SRC-006 → EXP-0204, SRC-036 → EXP-1205, MKT-1201 → EXP-1205) and resolve at redirect.

## 2. Merges (in `merges-EXP.txt`)

| DROP | KEEP | What was integrated |
|---|---|---|
| EXP-1205 (CX has outgrown CRM, Batat) | EXP-0901 (CX = the sum of interactions, Zahay et al.) | A single definition note: Zahay et al. and Batat converge on the cumulative, multidimensional definition (both start from Lemon & Verhoef); Batat adds the critique of CRM, the change in the purpose of consumption and the historical landmarks (Holbrook & Hirschman, Pine & Gilmore, Schmitt); Zahay adds the Temkin grid and the distinction that experiential marketing is part of CX, not CX itself. Retitled, `kind: concept`, level 1. |
| EXP-0204 (multisensory, Kotler 6.0) | EXP-1210 (five sensory signatures, Batat) | A shared table sense × role × Batat example × Kotler example; "why now" (digital fatigue) and Kotler's three steps; the explicit disagreement about Abercrombie & Fitch (a model in Batat 2019; in Kotler 2024 its "Fierce" scent was too strong and was replaced by "Ellwood"); a warning about the "80% sight" figure, repeated without a source in both books. |

## 3. Restructuring without deletion (the Kotler 6.0 ↔ Batat overlap)

The Kotler 6.0 notes (EXP-0202, EXP-0203) each mixed two or three ideas that overlapped with the Batat and Parsons et al. notes. I made them atomic, moving content to where the paired note already existed:

- **EXP-1207** (immersion) receives the five elements of immersion from Kotler 6.0 (multisensory, interactive, participatory, frictionless, narrative), in a mapping table with Batat's five factors. Differences noted: Batat has the cognitive factor, Kotler stresses participation. Retitled.
- **EXP-0202** keeps only the four human-digital scenarios (from the checkout to hospitality), retitled; the PwC quote and Ritz-Carlton/Henn-na checked in the text.
- **EXP-0203** becomes the note on the **third place**: Oldenburg (Kotler 6.0) + homeyness (Parsons et al., pp. 153–154, who cite Rosenbaum, not Oldenburg; corrected) + designing the space as a story (physical evidence, process, people). The paragraph on spatial marketing was removed (it is already in DIG-0205).
- **EXP-1220** (phygital) receives Kotler 6.0's five ways of bringing the digital into the physical space (Fig. 6.2), set beside Batat's tools; Timberland appears in both books.
- **EXP-0401** keeps only the rite of passage (Dans le Noir?); the part on the third place moved into EXP-0203. Pages corrected (pp. 152–153, the case study pp. 159–160).
- **EXP-0301** (Pine & Gilmore) receives Batat's perspective: the two axes (absorption-immersion, passive-active), the realms turning into one another and her critique, from which ETM is born. The list of themes from Gottdiener / Schmitt & Simonson moved into EXP-1209 (with SRC-008, ch. 16).
- **EXP-1201** and **EXP-1202**: the links to the 7 Es moved inline into the table, so that 5–6 typed links remain; EXP-1201 notes the convergence with EP² (Wuebben).

Other convergences written explicitly: the Ritz-Carlton's Joshie the giraffe appears both in Kotler 4.0 (EXP-0201) and in Zahay et al. (EXP-0901); Batat's "cumulative" marker = Zahay's CX definition (EXP-1203); the break at delivery/unboxing appears both in Batat (EXP-1215) and in Pereira/Kellogg (EXP-0501).

## 4. New notes

None. I searched the library for material on planning and measuring events (*hors-média*, *événementiel*, street marketing, activation, peak-end): there are only short mentions in the French books (SRC-019, SRC-020), and the peak-end rule is already in PIT-1417, which I linked from EXP-1204 and EXP-1223.

## 5. Duplicates across skills (I did not touch them; linked)

| EXP note | Note in another skill | Relation |
|---|---|---|
| EXP-1220, EXP-0203 | DIG-0205 (contextual and spatial marketing, Kotler 5.0 + 6.0) | partial overlap on spatial marketing; removed from EXP-0203, linked `see` |
| EXP-1220 | DIG-0201 (omnichannel) | the same idea from experience design vs. from channels; `see` |
| EXP-1210 | ART-0502 (12 sensory cues, Kellogg) | convergence: all the cues must trigger the same associations; `see` |
| EXP-1206 | DIG-0905, MKT-0210, ADV-0501 | alternative models of the customer journey; `alternative` |
| EXP-1214 | SOC-1005 (contests by the effort required) | the same logic of the level of participation; `see` |
| EXP-1213 | MKT-0401 (co-creation as unpaid work) | `contradicts` |
| EXP-1201 | MKT-0128 (the 7P of services), MKT-0314 (EP²) | `alternative` |
| EXP-1212 | MKT-0124 (the service gaps, the same authors as SERVQUAL) | `foundation` |
| EXP-0901 | DIG-1010 (DCX, Morville's honeycomb) | related, not linked directly (EXP-0901 already has 6 links) |

## 6. What the orchestrator needs to know

- **Links from other skills whose reason has moved:** SOC-0202 → EXP-0202 ("five elements of immersion") should now lead to **EXP-1207**; DIG-0205 → EXP-0203 ("augmented physical space") would be more accurate toward **EXP-1220**. MKT-0215 → EXP-0202 and MKT-0216 → EXP-0203 remain correct.
- The file names were not changed, although the titles of EXP-0202, EXP-0203, EXP-0401, EXP-0901, EXP-1207, EXP-1210 and EXP-1220 changed; the slugs can be regenerated at `renumber`.
- In my notes, the links to notes merged by other agents were already redirected (INS-0445 → INS-1206) based on the `merges-*.txt` files that existed at the end. If new merges happen after me, the global redirect catches them.
- EXP-1301 (service conjoint, Struhl) stayed in EXP, as a measurement note; it could also sit in AIM or CLI.

## 7. Remaining gaps

- Planning and producing an event or an activation (budget, logistics, execution risks): the library has no dedicated source; only SOC-1129 (Fyre Festival) as a warning.
- Measured results of experiential campaigns: Batat's cases are descriptive, with no effects on sales or on the brand.
- Employee experience (EX) as a separate subject, accessibility and inclusion in experience design, B2B experiences and trade shows.
- The EXQUAL instrument cannot be reproduced: the table of items is missing from the text copy (flagged in EXP-1212).
