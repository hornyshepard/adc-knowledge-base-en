# Report P2-DIG: integration of the digital-marketing skill (DIG)

## 1. Totals

| | Notes |
|---|---|
| Before (Phase 1) | 87 (G01: 4, G02: 5, G03: 5, G09: 35, G10: 36, G11: 1, G13: 1) |
| Merged (deleted) | 12 |
| New notes (Phase 2) | 2 (DIG-9901, DIG-9902) |
| **After** | **77** |

All 77 notes now have `status: growing`, 4–6 typed links and at least one link to another book group or another skill. `kb.py check` reports no problems in the DIG files (the broken links left in the KB come from other folders and point to IDs merged by other agents or by me; see §6).

`SKILL.md` is fully rewritten: a description with the trigger situations, 8 competencies, the map of the 77 notes in 6 sections (strategy → customer and journey → owned media → paid media → data, privacy and post-cookie → measurement and attribution), the table of sources with ★, 12 neighboring skills and 6 playbooks for agents. The `auto:notes` markers are kept.

## 2. Merges (full list in `merges-DIG.txt`)

| DROP → KEEP | What was integrated, where the authors converge or diverge |
|---|---|
| DIG-1013 → **DIG-0918** Ad Rank | Zahay and Sachdev describe the same mechanism; Sachdev adds the economics of keywords (a cheap long tail, actual CPC below the maximum), SRC-032 adds negative keywords, sitelinks, Bing. |
| DIG-1029 → **DIG-0922** programmatic | The chain ad server → network → exchange → DSP/SSP/DMP (Zahay) + RTB, 87% programmatic, Lammenett's critique (data, large budgets, loss of control) from SRC-032. Explicit divergence: an operational standard (Zahay) vs. a tool with limits (Schwarz-Musch). |
| DIG-1033 → **DIG-0934** attribution | Now a `debate`: Connors sees multi-touch as the solution; SRC-032 shows that after cookies, tracking the early stages becomes impossible; both measure correlation → incrementality, brand lift. |
| DIG-1035 → **DIG-0924** retargeting | The stage-by-stage method (Connors, Zahay) + post-cookie exposure (SRC-032), the consent requirements (Sachdev) and the contrast with Nishad's Facebook "recipe" without consent. |
| DIG-1036 → **DIG-0930** native advertising | Now a `debate`: a shared definition (NAI/CMI); SRC-032 praises the ambiguity (XXXL Sports), Zahay and Sachdev ask for labeling (FTC, the "net impression"). |
| DIG-1017 → **DIG-0910** third-party cookies | Mechanism + what they made possible + why they are disappearing (e-Privacy, GDPR, ATT with figures). Divergence: Zahay/Sachdev announce the phase-out in Chrome, SRC-032 records Google's reversal of July 2024. |
| DIG-0305 → **DIG-1021** first-party strategy | The three-question cycle (SRC-032) + the five consent-based collection practices (Ejeke) at question 3; SRC-032's warning about false data from contests. |
| DIG-1031 → **DIG-0906** metric vs. KPI | Kaushik (in Zahay) + the three tiers and the composite score (SRC-032) + the data → insight ladder (Sachdev). |
| DIG-1005 → **DIG-0905** journey | Sachdev keeps the AIDA funnel as a map read non-linearly (the Seema case); Zahay changes the model (decision journey, loyalty loop). |
| DIG-0912 → **DIG-1006** persona | The persona/target group distinction (SRC-032) + the persona as a design tool, storyboard (Zahay) + dosage (Sachdev). Divergence: biographical persona vs. decision-oriented persona. |
| DIG-1011 → **DIG-0920** landing page | The MarketingExperiments criteria + the homepage mistake (Zahay, Sachdev) + context matching (SRC-032) + consistency across channels (Sachdev). |
| DIG-0303 → **DIG-0201** omnichannel | Kotler's method (touchpoints, critical scenarios, silos) + the definition and measurement through CLV (DX Review) + the Salesforce figures (Wuebben); Ejeke's figures marked as unverified. |

**Re-atomization (no deletion):** DIG-0907 keeps only the chain SMART objective → metrics → diagnosis; the table of metrics by stage moved into DIG-1032, which now also integrates the loyalty stage from Zahay (fig. 5.6) alongside Aware/Appeal/Ask from SRC-032.

**New tensions, flagged with `contradicts`:** DIG-0926 ↔ DIG-1022 (opt-out as the "minimum acceptable" in Zahay vs. mandatory unticked boxes under GDPR; a sentence was also added to the body of DIG-0926), DIG-1001 ↔ MKT-0314 (the 7A complete the 4P vs. EP² replaces them), DIG-1025 ↔ INS-1503 (involvement as a category attribute vs. perceived risk), DIG-1101 ↔ DIG-1025 (a short journey vs. the long phase at high involvement), DIG-0933 ↔ ADV-1301 (A/B vs. conjoint), DIG-0932 ↔ EXP-0901 (CRM vs. CX).

Lightly shortened notes (redundant details): DIG-0103, 0202, 0204, 0205, 0926, 0931; DIG-1019 received a sentence of convergence with Zahay.

## 3. New notes

| ID | Title (short) | Sources checked in `90-library/text/` |
|---|---|---|
| DIG-9901 | Digital accessibility: a UX condition and a legal risk (alt text, captions, color, screen readers) | SRC-031 ch. 4 pp. 122-123, ch. 7 p. 238, ch. 8 p. 283, ch. 11 pp. 375-377; SRC-029 ch. 6 p. 176 (the Target case, $6 million) |
| DIG-9902 | Intellectual property in digital content: trademarks, domains, copyright, fair use, Creative Commons | SRC-031 ch. 4 p. 122, ch. 11 pp. 370-375 (the NCAA / UDRP case) |

DIG-9902 is complemented by STO-9901 (the STO agent), which gives the production rules on social; the two notes link to each other.

## 4. Duplicates across skills (I did not touch them; linked through `see` / `alternative`)

| DIG | Other skill | Remark |
|---|---|---|
| DIG-0925 owned/earned/paid | ADV-0617 (now includes PESO, after the ADV-1101 merge) | the same typology; a candidate for merging or for a shared map |
| DIG-0930 native advertising | ADV-0408, HIS-0820 | three angles (digital, psychological, historical) on the same form |
| DIG-0929 personalization and reactance | AIM-0301, ADV-0410 | the same tension; AIM-0301 is the closest |
| DIG-1015 ten privacy practices | AIM-1305 | AIM-1305 is a short version of the same list |
| DIG-1006 persona ≠ target group | INS-1306 | the same thesis, another source (SRC-040) |
| DIG-0921 display | ART-1001 | IAB formats in both; ART-1001 has the design rules |
| DIG-0905 journey | MKT-0210 (5A), ADV-0501 | three journey models, linked as alternatives |
| DIG-0931 demand generation / DIG-1007 buying center | CLI-9902 | the B2B buying center appears in both skills |

## 5. Remaining gaps

- **Incrementality and marketing mix modeling**: only mentioned (DIG-0934, pointing to AIM-1323 and INS-0419); the library has no dedicated chapter.
- **Retail media, social commerce, TikTok ads, affiliate marketing**: not covered by the sources.
- **SEO for AI answer engines** (zero-click search): only seminar questions in DIG-0302, DIG-0917.
- **Analytics setup** (GA4 events, tag manager): only at the level of concepts (DIG-0907, DIG-0934).
- **Recent EU legislation** (the DSA, the European Accessibility Act): not in the sources; the notes cite GDPR, e-Privacy, ADA, FTC.
- Advertising on Meta/Facebook sits in SOC (SOC-1004, SOC-1006); DIG points there from DIG-0919 and DIG-0924.

## 6. For the orchestrator

- `merges-DIG.txt` has 12 lines. Notes in other folders that still point to the merged DIG IDs (to be redirected): AIM-0301, ART-1001, BRD-0301, CPY-1001, MKT-1001, SOC-0901, SOC-1002/SOC-1118, SOC-1004, SOC-1008, STO-0903/STO-0202 and the source sheets SRC-029, SRC-031.
- In the DIG notes I already redirected the links to IDs merged by other agents, following the `merges-*.txt` files that existed at the end (e.g. ADV-0102→ADV-0401, ADV-1001→ADV-0103, ADV-1101→ADV-0617, AIM-0205→AIM-1303, BRF-1001→BRF-1501, EXP-1205→EXP-0901, INS-0107→INS-0430, SOC-0101→SOC-1115, SOC-1002→SOC-1118, STO-0903→STO-0202). If other agents merge more after me, the automatic redirect covers them.
- The KEEP files keep their old names even where the title changed; `renumber` will rename them. The backlinks blocks and `auto:notes` in SKILL.md still contain old entries until `build`.
- The pages in the G09/G10 notes are PDF pages (the `=== [page N] ===` markers); for SRC-029 printed = PDF − 14, for SRC-031 printed ≈ PDF − 19.
- Suggested maps for `30-maps/`: "Data, privacy and law in advertising" (DIG-0910, 1015, 1016, 1021, 1022, 9902, AIM-1305, SOC-1118, STO-9901) and "Measurement and effectiveness" (DIG-0906, 0934, 1032, ADV-0103, ADV-1528, INS-0419, AIM-1323), as the G09/G10 reports also proposed.
