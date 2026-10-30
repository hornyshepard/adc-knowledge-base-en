# Report P2-IDE: integration of the creative-ideation skill (IDE)

Agent P2-BRF-IDE, Phase 2. Skill: `20-skills/creative-ideation/`. (The same agent also integrated BRF; see `P2-BRF.md`.)

## 1. Numbers

| | Before | After |
|---|---|---|
| Permanent notes | 22 | 25 (22 + 3 new, no merges) |
| Notes with `status: growing` | 0 | 25 |
| Typed links per note | 3–5 | 5–6 |
| Notes with no typed link outside their own Phase 1 group and skill | 4 | 0 |
| Notes without the "Example" section | 12 | 0 |
| Body length (`kb.py words`) | 341–493 | 375–497 (no note over the 650 threshold) |

`kb.py check` (last run): **no problems in the `creative-ideation` files**. `renumber --dry-run` (display only) confirms the order in the map: IDE-0701 → IDE-001 … IDE-0710 → IDE-025.

There are no IDE merges, so I did not create `merges-IDE.txt`.

## 2. Merges

None. The close pairs stayed separate, with typed links, because they are different models or ideas:
- IDE-0702 (Ingledew's 16 stages) ↔ IDE-0716 (Ahmed's 7 steps): `alternative`.
- IDE-0501 (inspiration from outside the bubble, Peters + Moffat) ↔ IDE-0712 (the inspiration bank, Ingledew): `extends` (where you look vs. the habit of collecting).
- IDE-0301 (three myths, von Scheel) ↔ IDE-0802 (solitude/pair/meeting, the classics): `contradicts` in both directions.
- IDE-0708 (inversion) ↔ IDE-0714 (reframing): `extends` (inversion is a special case).

**Refinements:** IDE-0301 moved from `debate` to `principle` (a single author against some myths, not a dispute between authors). IDE-1501 retitled (the old title held two ideas; "at least six ideas" moved into IDE-9903): "The creative idea must first dramatize the key benefit, then get attention, speed up processing and support many executions". I fixed the direction of wrong relations from Phase 1 (e.g. IDE-0701 "extends" IDE-0702, IDE-0704 "extends" IDE-0707, IDE-0708 "example" INS-0702).

## 3. New notes (checked in `90-library/text/`)

I first looked at what HIS/CPY (G08) and *Shareworthy* already cover: the "big idea" is covered by IDE-0801 (+ ADV-1303, CPY-0808, HIS-0810), the "shareworthy" idea by STO-0701/STO-0704, and the Wallas/Webb Young process is mentioned in IDE-0703 (the library has only a few lines on it, not enough for a note). Three real gaps remained:

- **IDE-9901**: *Osborn's brainstorming has four rules (quantity, deferred judgment, wild ideas, combination) and requires generating to be kept separate from evaluating* (method, level 1). Sources: SRC-025 ch. 6, "The Ideation Process" (`shareworthy-robin-landa.txt` lines 2106–2110, the four rules); SRC-027 ch. 10, p. 207 (Osborn, BBDO, *How to "Think Up"*, 1942; Braun & Landa give 1953, *Applied Imagination*: a dating disagreement noted in the text); SRC-001 ch. 12, p. 444 (brainstorming in product development, the vote at the end); SRC-026 ch. 3 and ch. 6 (time limit, facilitator); SRC-028 (Campbell's "Soup on the Rocks").
- **IDE-9902**: *Idea evaluation grids converge on three questions (does it serve the strategy, does it stand out, does it stay linked to the brand) but apply at different moments* (framework, level 2). The gap: the scope asks for "judging ideas", and the five grids (Percy Table 14.1, A.L.T.E.R., Milavsky, ADPLAN, the Ahmed matrix) were in four skills with no comparison. Sources: SRC-049 ch. 14 (`audiobook/28.txt`, including the sentence about the brilliant execution that does not respect the strategy), SRC-022 ch. 8, SRC-025 ch. 6, SRC-021 ch. 5 and 7, SRC-026 ch. 3 and 7.
- **IDE-9903**: *Volume comes before quality: the good idea comes out of a large number of attempts, most of them bad* (principle, level 1). Convergence across six independent sources: SRC-049 ("random creativity", at least six ideas), SRC-017 ch. 2 (the sketch phase: "Quantity is more important than quality", 50 sketches), SRC-028 (Spier 40–50 approaches, Metcalf 25–30 rewrites, checked in the text), SRC-022 ch. 8 (teams generate many ideas, most of them bad), SRC-025 (Osborn's rule 1), SRC-026 ch. 3.

## 4. Convergences and disagreements written explicitly in the notes

- **The "aha" mechanism**: Ingledew's brainjack (IDE-0701) = the resolved incongruity of the Kroeber-Riel model in Percy (IDE-1501).
- **Big Idea** (IDE-0801): Richards/Watkins + Percy (dramatize the benefit) + Braun & Landa (North Star) + Aly Richards & McLean (Long Idea, ADV-1303).
- **Humor** (IDE-0709): Ingledew's enthusiasm `contradicts` the Fennis & Stroebe data (CPY-0404: humor steals brand memory).
- **Shock** (IDE-0710): + the history of shockvertising (HIS-0818) and the meta-analyses on fear (INS-0433).
- **Unexpected places / word of mouth** (IDE-0711): `contradicts` ADV-0504 (virality comes from mass broadcasting, not from gossip).
- **The cliché reversed** (IDE-0706) ≈ BDDP's Disruption method (ADV-0619), at the level of strategy.
- **Incubation** (IDE-0703) confirmed by the stories of the classics (Rubicam, Spier; IDE-0802); the Spier example checked in SRC-028.
- **Culture surfing** (IDE-0715): the BlackBerry "May the 4th" example from Percy (IDE-1501).
- **Generating kept separate from evaluating**: Osborn (IDE-9901) ≈ Ahmed (IDE-0716) ≈ the convergent strategist / divergent creative (BRF-1503).

## 5. Duplicates across skills (linked, not merged)

| IDE | Other skill | Nature of the overlap |
|---|---|---|
| IDE-0801 | CPY-0808, HIS-0810, ADV-1303 | Big Idea: the same Watkins preface in CPY-0808; the genealogy in HIS-0810 |
| IDE-0710 | HIS-0818 | shock as an attention strategy |
| IDE-0709 | CPY-0404, CPY-0813 | humor in advertising (experimental data vs. history vs. technique) |
| IDE-0706 | ADV-0619 | breaking convention (execution vs. strategy) |
| IDE-0802 | HIS-0811 | the copywriter-art director creative team |
| IDE-0713 / IDE-9902 | BRF-0712, CPY-0606 | evaluation grids for ideas and for executions |
| Ingledew's techniques | ART-0702…0706, CPY-0701 | the same source chapter (SRC-024), split between IDE (mechanisms) and ART/CPY (visual and verbal language); the IDE map lists them on a separate line |

## 6. Remaining gaps

- **The classic models of the creative process** (Wallas, Webb Young): the library has only a list of the stages (SRC-025) and one quote (SRC-024); they stay in IDE-0703 and IDE-9901.
- **Lateral thinking (de Bono)** appears only as the random word technique (IDE-0703) and as the six hats (IDE-0717).
- **AI as an ideation partner**: no IDE note; a possible subject for AIM (SRC-039 has passages on brainstorming with ChatGPT).
- **Divergent vs. convergent thinking** as a separate concept: insufficient material (only Percy/O'Malley in BRF-1503 and a mention in Colenso).

## 7. For the orchestrator

- No IDE note was deleted, so no redirect is needed for IDE.
- IDE-1501 changed its title; the file kept the old slug (`build --rename` or `renumber` will align it).
- I checked the links to notes merged by other agents (INS-0501 → INS-0702 used directly).
