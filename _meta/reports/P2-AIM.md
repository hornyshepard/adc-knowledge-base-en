# Report P2-AIM: integration of the ai-marketing skill (AIM)

Agent P2-EXP-AIM, Phase 2. Skill: `20-skills/ai-marketing/`. (The same agent also integrated EXP; see `P2-EXP.md`.)

## 1. Numbers

| | Before | After |
|---|---|---|
| Permanent notes | 33 | 34 (33 − 1 merged + 2 new) |
| Notes with `status: growing` | 0 | 34 |
| Notes with 2–6 typed links | 33 | 34 |
| Notes with no typed link outside their own Phase 1 group | 11 | 0 |
| Notes with at least one link to another skill | 22 | 34 |
| Typed links, total | 108 | 178 |
| Body length (`kb.py`-style count) | 304–485 | 305–490 |

`kb.py check`: no problems in the AIM files at the last run (the only "unknown relation", an inline link in a bold line in AIM-0206, was fixed). The broken link SRC-005 → AIM-0205 resolves at redirect.

I also fixed the direction of relations: many G02/G13 notes used `application`/`extends`/`example` the wrong way round (for example, a concept note marked "application" toward the note that applies it). I changed them to `see` or reversed them where needed.

## 2. Merges (in `merges-AIM.txt`)

| DROP | KEEP | What was integrated |
|---|---|---|
| AIM-0205 (predictive marketing, Kotler 5.0) | AIM-1303 (predictive analytics as a cycle, Noil) | A shared table: Kotler's three areas (customers, products, brands) × Noil's typical uses (CLV, lead scoring, churn, recommendations, campaign optimization); the five-step cycle (Noil) and the three techniques (regression, collaborative filtering, neural networks, Kotler). The explicit disagreement: Kotler et al. see the opacity of the "black box" as an advantage, Struhl does not (AIM-1314, now with a `contradicts` link in both directions); neither of the two sources asks for validation on unseen data or for incrementality. Level 1. |

Other integrations across authors: AIM-0301 gets the empirical evidence from Fennis & Stroebe (ADV-0410) and the convergence with Zahay et al. (DIG-0929); AIM-0206 notes that Noil (AIM-1304) and Najafov (AIM-1320) reach the same hybrid human-bot model; AIM-1305 notes the convergence with Sachdev's list (DIG-1015) and sends bias to the new note; AIM-1326 adds the position of Kotler 5.0 and the real cases; AIM-0202 adds the leap in language AI from Marketing 6.0 (SRC-006).

## 3. New notes

- **AIM-9901**: *In award-winning AI campaigns, the idea comes from human insight and AI gives it scale: Cadbury, Nike "Never Done Evolving", Jardim Sonoro* (case, level 2). The gap: the section "Generative AI in creative work" had no real case (the AI books give no cases). Sources checked in the text: SRC-006, ch. 5 (Cadbury #NotJustACadburyAd, 130,000 ads, 94 million views); SRC-025, ch. 6 (Nike/AKQA, Jardim Sonoro with Midjourney and an "A.I. prompt master" in the credits, Area 23 "Sick Beats") and ch. 8 (Guan Hin Tay).
- **AIM-9902**: *Bias in AI marketing has two sources: the data the model learns from and people's blind trust in the recommendation* (concept, level 2). The gap: bias was only one sentence in AIM-1305, although the required path ends with "ethics, bias, privacy". Sources checked: SRC-037 ch. 12 (12.1.2, 12.3), SRC-039 ch. 2 (pp. 20–22), SRC-005 ch. 4 (automation bias) and ch. 7 (David Dao), SRC-038 ch. 1 (the default images of a person).

**Prompting.** I checked whether the library supports better-grounded notes on prompting. It does not: Najafov has five simple examples (ch. 1) and generic chapters on tone and multilingualism; Noil only lists tools (Jasper, Persado, Phrasee); Zahay et al. have one paragraph on DALL-E. I did not write new prompting notes. I enriched AIM-1317 with the only prompting example from a real creative team (Jardim Sonoro, SRC-025) and with the link to Get/To/By (BRF-0716), and SKILL.md says openly that prompting technique is a gap.

## 4. Duplicates across skills (I did not touch them; linked)

| AIM note | Note in another skill | Relation |
|---|---|---|
| AIM-0301, AIM-1301 | DIG-0929 (personalization and reactance), ADV-0410 (fit + intrusion) | almost the same limit of personalization; `see`, convergence written in the text |
| AIM-1305 | DIG-1015 (ten privacy practices), DIG-1022 (valid consent) | lists that largely overlap; `see` |
| AIM-1303 | DIG-1020 (predictive targeting) | the same principle applied in media; `see` |
| AIM-1302 | DIG-0204 (the segment of one) | the same idea taken to the limit; `see` |
| AIM-1317 | CPY-1301 (brand voice with AI) | complementary (prompt → voice cycle) |
| AIM-1320, AIM-1306 | DIG-0933 (A/B testing) | the same experimental discipline; `see` |
| AIM-1325 | SOC-1116 (influencer vetting, includes the merged SOC-1301) | `see` |
| AIM-9902 | STO-0709, ADV-0302 (representation check) | the same vigilance, on images and texts; `see` |
| AIM-1314 | DIG-0922 (programmatic: efficiency vs. control) | `see` |

## 5. What the orchestrator needs to know

- In my notes I already redirected the links to notes merged by other agents (DIG-0305 → DIG-1021, SOC-1301 → SOC-1116; for programmatic I linked DIG-0922 directly, not DIG-1029, which was merged), based on the `merges-*.txt` files that existed at the end.
- EXP-1301 (service conjoint, Struhl) is in EXP, not in AIM; it is linked from AIM-1310.
- G13 recommended marking the notes AIM-1310–1315 as an "advanced/planning" path: in SKILL.md they are grouped in section 2, and AIM-1314, AIM-1315, AIM-1323 are level 3.

## 6. Remaining gaps

- A rigorous prompting method (text and image): the library does not contain one.
- Current generative tools and workflows; AI regulation (for example, the AI Act); copyright over generated content; consent for synthetic faces and voices beyond the Cadbury case.
- Measuring the effectiveness of AI-generated creative work, and creative "wearout" when all brands use the same models.
- The figures in Noil, Najafov, James and Iroegbu remain unverifiable; the notes flag them as such.
