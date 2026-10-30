# Report P2-CPY: integration of the Copywriting and message skill

Agent: P2-CPY-ART-HIS (also owns ART, HIS). Date: 2026-10-01.

## 1. Numbers

| | Before | After |
|---|---|---|
| CPY permanent notes | 37 | 38 (−1 merged, +2 new) |
| Notes with `status: growing` | 0 | 38 |
| Typed links per note | 2–5 | 4–6 (all notes have at least one link to another book group or another skill) |

`kb.py check`: no problems in the CPY files. The only broken link related to CPY is in `10-sources/SRC-027` and `SRC-028` (→ CPY-0802, merged), which resolves at redirect.

## 2. Merges (`merges-CPY.txt`)

- **CPY-0802 → CPY-0601** (reason-why). Both notes described Kennedy's "salesmanship in print" formula and the Hopkins method. CPY-0601 (G06, Fernández Gómez) kept the line of descent to the copy strategy and the USP. From CPY-0802 (G08, Richards + Watkins) it took the Ivory, Pepsodent, Sears and Canada Dry examples, plus MacManus's attack. The sources are now SRC-018, SRC-027 and SRC-028, and the angle is craft: how you write concrete reasons. The historical genealogy stays in HIS-0810, linked.

## 3. New notes (Phase 2)

- **CPY-9901**: The anatomy of the print ad: visual, headline, subhead, body copy, signature (SRC-001 ch. 19, pp. 604–605, with SRC-049 and SRC-021). The basic vocabulary of a copywriter was missing. The note shows the convergence of Grewal & Levy, Percy & Rosenbaum-Elliott and Milavsky on the order image → headline.
- **CPY-9902**: The brand's voice stays constant, the tone adapts (SRC-031 ch. 3 and 8; SRC-016 ch. 7, the interview with Myra El-Bayoumi; SRC-039 ch. 2). "Tone and voice" was in scope, but had no concept note. The three sources give the same distinction.

## 4. Content revisions

- Explicit convergences and disagreements added: CPY-0401 (Carlsberg: misleading inference in Fennis & Stroebe vs. modest irony in Percy, ADV-1523), CPY-0402 (the refutational approach in Percy), CPY-0605 (INS-0410 and BRF-0707), CPY-0806 (the meta-analyses on fear, INS-0433), CPY-0813 (the data on humor from CPY-0404 and Milavsky), CPY-0817 (perseverance, ADV-0606, and wearout, ADV-0407), CPY-1502 (Milavsky reaches the same rules). The new sources were added to `sources:`.
- CPY-0701 was missing the "Example" section; I added it.
- Titles shortened (too long, not vague): CPY-1502, CPY-1001.
- I cut the text of CPY-0605, CPY-1502, CPY-0806 and CPY-0813. I replaced the links to hubs (`[[…/SKILL|CPY]]`) with links to notes.

## 5. Duplicates across skills (I did not touch other agents' notes, I only linked)

| CPY note | Note in another skill | Relation |
|---|---|---|
| CPY-0601 reason-why | ADV-0603 (copy strategy), ADV-0604 (USP), HIS-0810 (the genealogy) | the same family of ideas; craft in CPY, strategy in ADV, history in HIS |
| CPY-0817 consistency | ADV-0606 (the principle of perseverance) | the same idea, different sources (Watkins vs. Fernández Gómez/Milavsky): a candidate for a shared map |
| CPY-0605 one single reason | BRF-0707 (a single benefit), INS-0410 (ease of recall) | convergence across three sources |
| CPY-0806 social fear | INS-0433 (fear appeals) | historical case vs. meta-analysis |
| CPY-0404 / CPY-0813 humor | IDE-0709 (humor, irony, satire) | effect vs. history vs. idea technique |
| CPY-0607 the formats | INS-1505 (VisCAP), HIS-0821 (characters vs. celebrities) | the choice of presenter |
| CPY-0401 misleading inferences | ADV-0108 (puffery), HIS-0808 (FTC) | the ethics of wording |

## 6. Remaining gaps

- **Writing for social media** (captions, text over video, microcopy, UX writing) has no CPY note. SRC-034 (*Social Media Storytelling*) has material on captions. It is probably partly covered in STO/SOC; to be checked in the cross-cutting map.
- **Naming**: it is in BRD (BRD-0524, BRD-0525), but it is also a copywriter's task. A link from the identity map would help.
- **Classic text structures** (PAS, FAB) appear only in the pitch book (SRC-043); I did not write a note.
- **The ethics of wording**: CPY-0401, CPY-0406, CPY-0806 and CPY-0405 are candidates for the cross-cutting ethics map.

## 7. For the orchestrator

- The renumbering order is the one in `SKILL.md`: CPY-9901 becomes CPY-001, CPY-9902 falls in section 4.
- In my notes I already redirected the links to IDs merged by other skills (ADV-0106 → ADV-0604, DIG-0912 → DIG-1006, DIG-1013 → DIG-0918, DIG-1011 → DIG-0920), following the `merges-*.txt` files that existed at the time of the run.
- About 20 CPY notes have 405–445 words by the `check` metric (which also counts the H1 title, tables and headers). I cut only where the overrun was large.
