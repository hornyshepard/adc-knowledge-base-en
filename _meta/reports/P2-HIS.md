# Report P2-HIS: integration of the Advertising history and culture skill

Agent: P2-CPY-ART-HIS (also owns CPY, ART). Date: 2026-10-01.

## 1. Numbers

| | Before | After |
|---|---|---|
| HIS permanent notes | 28 | 29 (+1 new, no merges) |
| Notes with `status: growing` | 0 | 29 |
| Typed links per note | 3–6 | 5–6 (all have at least one link to another book group or another skill) |

`kb.py check`: no problems in the HIS files.

## 2. Merges

None (`merges-HIS.txt` contains only a comment). 27 notes come from a single group (G08: Richards + Watkins), so they were already coherent with each other, but linked almost only to each other. For each one I added links to ADV, INS, CPY, ART, DIG, SOC, STO, MKT, CLI, PRT, AIM.

## 3. Ethics and regulation: grouped in a single section

The G01, G04, G06, G07, G08, G09, G10 and G11 reports flagged that ethics and regulation had no home. In `SKILL.md`, **section 6, "Ethics, regulation and the limits of advertising"**, gathers the nine HIS notes on the topic, in the order of an argument: HIS-0806 (miracle cures), HIS-0807 (self-regulation), HIS-0808 (the FTC standard), HIS-0825 (the real demonstration), HIS-0820 (disguised advertising), HIS-0817 (the subliminal), HIS-0818 (shock), HIS-0824 (tobacco), HIS-0823 (diversity). The section starts with the list of related notes in other skills (CPY-0401, ADV-0108, SOC-1118, DIG-0930, STO-0709, ADV-0302, INS-0420, AIM-1305), as a starting point for the cross-cutting ethics map.

## 4. New note (Phase 2)

- **HIS-9901**: Every new medium first refuses advertising, then lives on it, until the clutter breeds the technology to avoid it. Sources: SRC-027 ch. 11, pp. 242–243; ch. 14, pp. 302–304; ch. 15, pp. 347–354; SRC-032 for today's CTR. The gap was the radio-TV-internet era: the skill practically stopped at the 1960s–1990s. The note links HIS-0804 (the press), HIS-0820 (native), ART-1001 (the banner) and ADV-1528 (Percy's skepticism about digital).

## 5. Content revisions

- **HIS-0810** (the genealogy of styles): I kept it on the historical angle, as requested. The note points explicitly to CPY-0601 and CPY-0803 for craft and to ADV-0607 and ADV-0604 for strategy (USP vs. image).
- **HIS-0817** (the subliminal): I added the disagreement between sources. Percy & Rosenbaum-Elliott (INS-1511) declare it an invented myth. Fennis & Stroebe (INS-0439) admit a narrow effect, in people who already have the goal. I also noted that Vicary's figures appear reversed from one book to another. I added SRC-012 and SRC-049 to the sources.
- HIS-0601: linked to ADV-1519, where Percy argues the same thing: new jargon does not change the mechanism.
- I replaced the links to hubs with links to notes. I fixed relations used backwards (for example `example`/`application` set from the target's point of view).

## 6. Duplicates across skills

| HIS note | Note in another skill | Relation |
|---|---|---|
| HIS-0817 the subliminal (history) | INS-0439 (narrow effect), INS-1511 (myth), INS-0601 (motivation research) | the same subject, three positions; linked with `contradicts` / `see` |
| HIS-0815 AIDA (genealogy) | ADV-0401, ADV-1302, ADV-1503, MKT-0210 | the history of the model vs. its critique and alternatives |
| HIS-0820 disguised advertising | DIG-0930 (DIG-1036 merged into it), ADV-0408, SOC-1118 | history vs. current rules |
| HIS-0810 copy styles | ADV-0607 (Reeves vs. Ogilvy), CPY-0601, CPY-0803 | history / strategy / craft |
| HIS-0818 shockvertising | IDE-0710 (the debate on shock) | historical cases for the debate |
| HIS-0823 diversity | ADV-0302, STO-0709, ADV-0411 | history vs. current checklists |
| HIS-0601 recurring invention | ADV-1519 | the same thesis, different sources |
| HIS-0816 account planning | ADV-0620 (strategic planning) | history vs. method |

## 7. Remaining gaps

- **European and Romanian context**: the library is centered on the US (Richards, Watkins). The history of advertising in Romania, ARPP/RAC and EU legislation (UCPD, the average consumer) are missing. HIS-0807 and HIS-0808 mention the RAC Code and the EU standard only in passing.
- **The history of television as a creative medium** (the TV spot, the 1980s–1990s) and **the history of holding agencies**: covered only tangentially.
- **The critique of advertising** (Packard, Galbraith, materialism): only through HIS-0817 and INS-0420.

## 8. For the orchestrator

- The renumbering order is the one in `SKILL.md`: HIS-0801 becomes HIS-001, HIS-9901 becomes HIS-005, the ethics section takes the last nine positions.
- In my notes I already redirected DIG-1036 → DIG-0930. The resulting duplicate link in HIS-0820 was removed.
