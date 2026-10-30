# Report P2-BRF: integration of the creative-brief skill (BRF)

Agent P2-BRF-IDE, Phase 2. Skill: `20-skills/creative-brief/`. (The same agent also integrated IDE; see `P2-IDE.md`.)

## 1. Numbers

| | Before | After |
|---|---|---|
| Permanent notes | 26 | 27 (26 − 1 merged + 2 new) |
| Notes with `status: growing` | 0 | 27 |
| Typed links per note | 3–5 | 5–6 |
| Notes with no typed link outside their own Phase 1 group and skill | 7 | 0 |
| Notes without the "Example" section | 9 | 0 |
| Body length (`kb.py words`) | 345–465 | 386–527 (tables inflate the count; no note is over the 650 threshold) |

`kb.py check` (last run): **no problems in the `creative-brief` files**. The only broken link related to BRF is `10-sources/SRC-032 → BRF-1001`, expected until the redirect. I ran `kb.py renumber --dry-run` once (display only, no writing) to check that the order in the `SKILL.md` map is the intended one: BRF-0701 → BRF-001 … BRF-0708 → BRF-027.

## 2. Merges (in `merges-BRF.txt`)

| DROP | KEEP | What was integrated |
|---|---|---|
| BRF-1001 (the digital campaign brief, Schwarz-Musch et al., SRC-032) | BRF-1501 (the briefing document, Percy & Rosenbaum-Elliott, SRC-049) | I checked in the text: SRC-032 (ch. 2.2.1, pp. 40–41) explicitly builds its four blocks on Percy & Rosenbaum-Elliott. The KEEP now has both sources: the table of Percy's five areas, the rearrangement into four blocks, the digital addition (buyer persona, customer journey, objectives for each phase), the Davis quote ("There are as many methods of briefing as there are people"), the e-mountain bike example. Retitled: "The briefing document precedes the strategy: product, market, source of business, competition and objectives, plus the persona and its journey in digital"; `also` + digital-marketing. |

**Kept separate, linked as `alternative`** (different models, not the same idea):
- BRF-0705 (positioning in four pieces, McTigue-Rucker) ↔ BRF-1502 (three variables, Percy). Both now have a comparison paragraph: the same formula in Tybout & Calkins (BRD-0503); Percy drops the RTB and replaces the frame of reference with category need; a difference of school ("why would they choose me?" vs. "what is it? / what does it offer?").
- BRF-0702 (six components) ↔ BRF-1503 (Percy's three blocks).
- BRF-0601 (client brief vs. creative brief, Barre) ↔ BRF-1501 (the briefing document).

## 3. New notes

- **BRF-9901**: *Receiving the brief: you reduce it to its essence, check it component by component, ask the naive questions and agree any change in writing* (method, level 2). The gap: the skill's scope asks for "how to receive a brief, debriefing", but no note looked at the brief from the side of the person who receives it. Sources checked in `90-library/text/`: SRC-024, "Strategies for solving a creative brief", stages 1–2 (`a-to-z-visual-ideas.txt` lines 520–600: naive questions, deliverables, a 10-page brief reduced to 15 words); SRC-022 ch. 1, Myths (the brief as a map, not a contract, lines 143–145) and ch. 8 (the account person rereads the brief in the meeting, lines 851–857); SRC-019 outils 1–2 (triage, a 50-page brief that leaves out the crucial information, the Publicis flow with the "débrief créatif", lines 1028–1034, 1314–1330); SRC-025 ch. 6 ("Don't Forget the Insight", "Reframing").
- **BRF-9902**: *Ten red flags in a brief: from an objective that cannot be falsified to measurement decided after the campaign* (checklist, level 2). The gap: the typical mistakes were scattered across seven notes; the tool for quickly assessing a brief was missing (competency C6). Sources checked: SRC-022, all the "Why Brands Fail and How to Succeed" sections (ch. 1–7, lines 109–128, 217–224, 321–334, 423–438, 545–554, 663–686, 769–792); SRC-049 ch. 14 (a one-page brief, accepted by everyone, `audiobook/28.txt`); SRC-019 outil 1.

## 4. Convergences and disagreements written explicitly in the notes

- **The communication objective** (BRF-0703): McTigue-Rucker (the barrier) ≈ Barre (a single communication problem, ADV-0613) ≈ Percy (four effects, ADV-1502; numerical targets, ADV-1505).
- **The target** (BRF-0704): needs / Own-Attract-Accept (McTigue) vs. groups of buyers by their relationship with the brand (Percy, ADV-1507, MKT-1501).
- **The benefit** (BRF-0706): McTigue's "So what?" ladder ≈ Milavsky (ADV-0624, plus dropping category benefits) vs. the expectancy-value model (Percy, BRD-1503).
- **A single benefit** (BRF-0707): the convergence of the templates + new empirical evidence: ease of recall (INS-0410, Fennis & Stroebe) and support points limited to "a maximum of three" (CPY-0605, Milavsky).
- **Emotional vs. functional** (BRF-0708): Fennis & Stroebe (CPY-0403) prove McTigue-Rucker right; the historical form of the dispute, Reeves-Ogilvy (ADV-0607); the "Loretta" example checked in the text.
- **Measurement** (BRF-0710): McTigue accepts the focus group for the "why" vs. Percy, who excludes it from pretesting (ADV-1530, `contradicts`); Struhl (INS-1303) sides with McTigue.
- **Feedback** (BRF-0711): Milavsky's rules (CPY-0606) are almost identical to McTigue-Rucker's, from the agency side.
- **ADPLAN** (BRF-0712) extends Sternthal's three-step strategy (ADV-0503), also from Kellogg.
- **Mandatories** (BRF-0709): Percy (logo and tagline untouched, style manuals suspect) ≈ McTigue (mandatories that write the ad).
- **Templates** (BRF-0720): besides the five, the comparison mentions Percy's brief (BRF-1503) and Barre's Publicis template (BRF-0601). Singleton O&M (the sensory proof) is backed by Milavsky's hierarchy of promises (ADV-0623).

## 5. Duplicates across skills (linked, not merged)

| BRF | Other skill | Nature of the overlap |
|---|---|---|
| BRF-0705 | BRD-0503 | the same four-piece positioning statement (the Kellogg school); BRF-0705 is the "in the brief" version |
| BRF-0706 | ADV-0624 | the attribute → end benefit ladder with the "so what?" test (Milavsky vs. McTigue) |
| BRF-0712 | ADV-0503 | ADPLAN contains Sternthal's three steps (attention, amplification, linkage) |
| BRF-0601 | ADV-0603 | the copy strategy is the heart of the creative brief; partial overlap |
| BRF-0716 | PIT-1407 | think/feel/do ≈ Know/Feel/Do/Why now |
| BRF-1101 | SOC-1117, SOC-1133 | the brief for creators sits on the BRF-SOC border |
| (the insight component) | INS-0701, INS-0702 | the "Insights" chapter of SRC-022 was written up in INS; the BRF map points there explicitly, with no duplicate note |

## 6. Remaining gaps

- **Briefing as a presentation** (how you "sell" the brief to the creative team, the briefing meeting) appears only as a paragraph in BRF-1503 (Percy) and in BRF-9901; the library has no more material.
- **The counter-brief / reverse brief** (the agency sends the client its own rewording) has no source in the library beyond the "débrief créatif" (Barre) and McTigue's recommendation to rewrite and approve the brief; I did not write a note.
- **Briefs for other types of projects** (activations, products, partnerships) remain an open question in BRF-0720.

## 7. For the orchestrator

- Redirect needed: `BRF-1001 → BRF-1501` (references from SRC-032, from DIG-1004, DIG-1006 and DIG-1024 (in backlinks) and from `digital-marketing/SKILL.md`).
- I replaced my links to ADV-0614 (merged by P2-ADV into ADV-1502) and INS-0501 (merged into INS-0702) with the KEEPs.
- A global problem I noticed, not only in BRF: many Phase 1 notes have wikilinks in table cells; after `build`, the form `[[ID-slug|ID]]` introduces a `|` that breaks the Markdown table (e.g. BRF-0702). It would be worth having `normalize_links` escape the pipe (`\|`) in table rows. In the new notes I avoided links in tables.
- `SKILL.md`: the competencies contain no IDs of their own, so that the order for `renumber` is given only by the map.
