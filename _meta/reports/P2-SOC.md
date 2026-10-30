# Report P2-SOC: Phase 2, integration of the social-influencer skill

Agent: P2-SOC-STO (also owns STO; see `P2-STO.md`). Date: 2026-10-01.

## 1. Totals

| | Before | After |
|---|---|---|
| Own SOC notes | 53 | **49** |
| Merges (DROP → KEEP) | n/a | 4 (`merges-SOC.txt`) |
| New notes (`SOC-99NN`) | n/a | 0 |
| Status | 53 seed | 46 growing, 3 seed (SOC-1006, SOC-1109, SOC-1130: not touched, they already had good links) |
| Levels | n/a | 13 × 1, 32 × 2, 4 × 3 (SOC-1121 lowered from 3 to 2) |
| `SKILL.md` | provisional hub | rewritten: 7 competencies, a map in 6 sections (all 49 notes, in learning order), sources with ★, neighbors, 5 playbooks |

All kept notes have 2–6 typed links and at least one to another skill or another book group. `kb.py check`: no problems in the SOC files.

## 2. Merges

| DROP | KEEP | What was integrated |
|---|---|---|
| SOC-0101 | SOC-1115 | The two "4R" models (Grewal-Levy: relevance, reach, response, return; Onalytica in Glenister: relevance, resonance, reference, reach) in a single comparative note: where they converge (relevance as the first criterion) and where they differ (selection before vs. evaluation after the campaign). The Grewal-Levy typology with costs and the LaCroix case moved into SOC-1114; ethics (fraud, disclosure, sincerity) into SOC-1116 and SOC-1118. |
| SOC-1002 | SOC-1118 | Disclosure from Sachdev (the FTC material connection, "clear and conspicuous", liability for pseudo-advice, the Teami case) + Grewal-Levy (sincerity, the "spontaneous" marriage proposal) + Glenister (ASA/CMA/EASA, accepted and risky labels, Molly-Mae). Three sources converge almost word for word. |
| SOC-1301 | SOC-1116 | The AI criteria for selection (Iroegbu, SRC-042; visual listening, SRC-041) joined with Glenister's fraud checklist: the same signals; the difference is Glenister's insistence on real statistics and manual checking. |
| SOC-1126 | SOC-1007 | The role of platforms in influencer marketing (Glenister, Sbai) joined with the four-question test for social ads (Schwarz-Musch): a single table platform × role × advertising specifics. |

## 3. New notes

None. The gaps identified (§5) are partly covered by notes in other skills or are too tutorial-like.

## 4. Duplicates across skills (I did not touch them; they are linked)

- **SOC-1112** (a viral hashtag without a values fit) ↔ **IDE-0715** ("culture surfing" only when the brand's values allow it): the same rule from two books; linked `alternative`.
- **SOC-0906** (crisis plan on social) ↔ **ADV-0622** (crisis communication: acknowledge, do not deny): partial overlap; linked.
- **SOC-0901** (POST) ↔ **DIG-0103** (listen-analyze-act, the social campaign in five steps): alternative frameworks.
- **SOC-0902** (the 5Cs) ↔ **DIG-0102** (the engagement wheel): alternative explanations of engagement.
- **SOC-0401 / SOC-1102** ↔ **BRD-0519** (the ideal brand community): the same theme from three books.
- **SOC-1125** (ER, CPE, CPM) ↔ **DIG-1012** (media payment models): the same acronyms.
- **SOC-1113 / SOC-1114** ↔ **INS-0432**, **INS-1505**, **HIS-0821** (the celebrity as a source): complementary perspectives.
- **SOC-1118** ↔ **DIG-0930** (native advertising clearly labeled) and **DIG-9902** (rights in digital content, a new note by the DIG agent, which still points to SOC-1002 → redirect to SOC-1118).
- The brief for influencers sits in **BRF-1101**; SOC points to it from SOC-1110, SOC-1118, SOC-1133 and from the playbook.

## 5. Remaining gaps

- **Social listening** as a method in its own right (today it appears only in SOC-0903, SOC-1133 and in DIG-0103, INS-0203).
- **Social commerce and live shopping**: only as a micro-trend in SOC-0201.
- **Romanian/EU regulation** of disclosure and promotions: the notes only say "check the local rules"; the library has no Romanian source.
- **Virtual influencers and AI-generated creators**: only mentions (SOC-1114, SOC-1132).
- **Brand lift** as a measurement method: it appears only in cases (SOC-1130).

## 6. For the orchestrator

- Notes in other skills that point to my merged IDs (to be redirected): ADV-0109, DIG-0102, MKT-0119 → SOC-0101; DIG-1016, DIG-9902 (and DIG-1036, merged by DIG) → SOC-1002; AIM-1318, AIM-1325 → SOC-1301; plus the source notes SRC-001, SRC-031, SRC-034, SRC-035, SRC-041, SRC-042.
- In my files I already redirected the links to IDs merged by other agents, following the `merges-*.txt` files that existed at the end (ADV-1101→ADV-0617, BRD-0401→BRD-0606, DIG-0912→DIG-1006, DIG-1031→DIG-0906, DIG-1035→DIG-0924, DIG-1036→DIG-0930). Still, run `redirect` for the merges made after me.
- `SKILL.md` cites no IDs in "Competencies", so that `renumber` follows the order of the map.
- A few merged notes have 420–490 words by the `kb.py` counter (which includes the long H1 title and the tables); the prose is around 400.
- The scripts used (applying the rewrites while keeping the backlinks, links, redirect) are in `scratchpad/P2-SOC-STO/`, with a backup of the folders from before the change.
