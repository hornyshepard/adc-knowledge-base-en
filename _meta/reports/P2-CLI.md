# Report P2-CLI: Phase 2, client-business

Agent: P2-PIT-PRT-CLI · skill: `client-business` (CLI) · date: 2026-10-01

## 1. Notes before / after

| | Count |
|---|---|
| Notes before | 10 (6 from G14 (Nishad, B2B); CLI-0301 from G03; CLI-0601, CLI-0602 from G06; CLI-0701 from G07) |
| Merges (DROP) | 0 |
| New notes | 7 (CLI-9901 … CLI-9907) |
| Notes after | **17** |
| `status: growing` | all 17 |

`merges-CLI.txt` is empty. The closest pairs are CLI-1403 (the 3-way introduction) / CLI-1404 (Person of Influence) and CLI-1401 (stage selling) / CLI-9903 (the complete personal selling process). Each pair links a tool to the system it belongs to, or two variants of the same model, so I kept them separate and linked.

## 2. What I did

- **I searched the library**, as the brief asked, for well-documented material on the agency-client relationship, presenting to the client, account management, negotiation and the agency business. I checked: `logos-that-last.txt`, `overcome-ad-versity.txt` (ch. 7, 8, 10), `the-creative-brief-blueprint.txt` (ch. 1, 2, 7, 8), `a-history-of-advertising.txt` (ch. 10, 17), `la-boite-a-outils-de-la-publicite-dunod-2015.txt` (dossiers 1 and 9), `marketing.txt` (Grewal & Levy, ch. 7 and 20; G01 had read only their table of contents), `shareworthy-robin-landa.txt` (the Hahn interview), the Percy transcript (`audiobook/09.txt`, `28.txt`), `cut-through-…txt` (procurement). `strategic-advertising-mechanisms.txt` has no material on the client. Material that already existed in notes (the approval circuit, feedback, historical compensation) I did not rewrite; I linked it.
- **Links:** 16 new links in the 10 old notes. All 17 notes now have 3–6 links and at least one to another skill or another group.
- **Convergence written in the text:** CLI-1401: Nishad, Colenso and Grewal & Levy say the same thing about the first meeting. I added SRC-001 to `sources`.
- **SKILL.md** written in full: 6 competencies; a path in 4 sections (Foundations → Working on the account → New business → The agency business), each with the readings from other skills that the brief asked for (PIT-9901, BRF-9901, BRF-0711, BRF-0712, PIT-1423, PRT-1412, ADV-0622, PIT-1403, PIT-1410, PIT-1421, PIT-0601, DIG-0931, SOC-1124, HIS-0805, HIS-0816, SOC-1128, SOC-1119, MKT-0105); 9 sources with ratings and the attribution caveat for SRC-045; 6 playbooks, including the instruction to say explicitly when the base does not cover the topic. The renumbering order is checked (CLI-9902 → CLI-001 … CLI-0301 → CLI-017).

## 3. New notes

| ID | Title (short) | Sources and location |
|---|---|---|
| CLI-9901 | The account manager sells in both directions | SRC-019 outils 55, 58, 59, pp. 176–185; SRC-022 ch. 8; SRC-049 ch. 4 (audio 09) |
| CLI-9902 | The B2B client decides as a buying center: six roles, four cultures, three situations | SRC-001 ch. 7, pp. 232–234, 237–239 |
| CLI-9903 | Personal selling in five steps, aligned with the buying stage | SRC-001 ch. 20, pp. 624–633; ch. 7, pp. 228–231; SRC-045 |
| CLI-9904 | In-house, partner agency or roster: the criterion is effectiveness, not cost | SRC-049 ch. 14 (audio 28); SRC-027 ch. 17, p. 412 (Reinhard); SRC-019 outil 55; SRC-017; SRC-022 ch. 1 |
| CLI-9905 | An agency competition is expensive for both sides: qualification, a contractual framework, one winner | SRC-019 dossier 1, p. 10, outil 55, pp. 176–177; SRC-021 ch. 10, pp. 150–151; SRC-022 ch. 8; SRC-043 ch. 1 |
| CLI-9906 | The agency sells time; an unclear brief eats its margin; retainer + bonus on communication objectives | SRC-022 ch. 1, 2, 7; SRC-019 p. 10; SRC-027 ch. 10, pp. 217–218 |
| CLI-9907 | Global holding companies and boutiques; the account conflict | SRC-027 ch. 10, pp. 213–217 |

All are paraphrased, with at most one short quote, and have 3–6 links. The new notes give the skill three pillars it lacked: **who decides at the client** (9902), **who works on the account** (9901) and **the economics of the agency** (9904–9907). In Phase 1, CLI meant almost nothing but prospecting.

## 4. Duplicates and overlaps with other skills (not touched, only linked)

| My note | Note in another skill | Nature of the overlap |
|---|---|---|
| CLI-9906 | HIS-0805 | Agency compensation. HIS covers the history (commission → fee → performance), CLI today's economics (time, margin, retainer + bonus). Linked through `foundation`. |
| CLI-9902 | INS-1501 | The roles in the buying decision: B2B (Grewal & Levy) versus the consumer (Percy). `alternative`. |
| CLI-0602 | CPY-0817 | Both cite Milavsky's argument: the client and the agency get bored with the campaign before the public does. Linked. |
| CLI-9904 | SOC-1128 | The same question, "who owns the work?", asked in influencer marketing. |
| CLI-0701 | BRF-0711 | The same McTigue & Rucker chapter: the relationship (CLI) and the feedback technique (BRF). Complementary. |
| CLI-1401 | PIT-1410 | Stage selling and the "logical next step". Convergence noted in both. |

## 5. Remaining gaps (the library does not cover them)

- **Negotiation**: contract, price, scope, concessions. No book in the library covers it; the only note is SOC-1119 (negotiating with creators). The playbook in SKILL.md asks the agent to say so explicitly.
- **Estimating and pricing a project** for an agency or a freelancer, scope creep.
- **Account retention and growth**, the client's evaluation of the agency: it appears only as a stage in CLI-9903 and as an anecdote in CLI-0602 / CLI-9905.
- **Intellectual property in pitch ideas**: there are only the questions in PRT-1412.
- Prospecting still depends on SRC-045 (★★, probably the transcript of Eric Lofholm's course). I recommend a dedicated source on account management or agency new business.

## 6. For the orchestrator

- `kb.py check`: 0 problems in `20-skills/client-business/`.
- I also linked two new notes by the BRF agent that were orphans: BRF-9901 (from CLI-9901) and BRF-9902 (from CLI-9906).
- Taxonomy suggestion, taken from G14: the CLI scope in `skills.json` could explicitly mention "prospecting and new business" and "industry structure / compensation".
- Two empty files at the KB root (`ADV-0603.md`, `PRT-0501.md`, 0 bytes) should be deleted; they are not mine.
