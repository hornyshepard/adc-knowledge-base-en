# Agent protocol, Phase 1: reading books into the knowledge base

You are one of several agents working **in parallel** on the same knowledge base (KB). Each agent owns a group of books (G01…G15). Follow this protocol exactly so all output is consistent.

KB root: `/Users/dumitrubabara/Downloads/Books for ADC School/ADC-Knowledge-Base/`
(All paths below are relative to it. Quote paths in shell commands: the folder names contain spaces.)

## 0. Read first (mandatory)

1. `_meta/conventions.md`: the rules. They are binding.
2. `_meta/skills.json`: skill codes, slugs, scopes, kinds, levels, relations.
3. `_meta/templates/zettel.md` and `_meta/templates/source.md`.

Never open or modify anything outside the KB root. Book texts are COPIES in `90-library/text/`: read only those (never the original PDFs/EPUBs in the parent folder).

## 1. Read the book (really read it)

- Structure first: if `90-library/text/<slug>.toc.txt` exists, read it. Otherwise find chapters with `grep -n "^## \|=== \[section" "90-library/text/<slug>.txt" | head -200` (EPUB) or look at page markers `=== [page N] ===` (PDF).
- Then read the content with the Read tool in chunks (use `offset`/`limit`). Your notes must reflect **what this book actually says** (its own models, distinctions, examples, numbers and arguments) with chapter / page references. Do not write notes from general knowledge and attach the book as a fake source.
- Depth: books under ~120k words: read essentially all of it. Larger textbooks: read the TOC, the introductions and summaries of every chapter, and read in full the chapters most relevant to an advertising / creative school (strategy, insight, brand, creative, communication, digital, measurement). Skim the rest with targeted reads / grep.
- Write notes **incrementally**: finish one book (source note + its permanent notes) before starting the next, so work is saved even if you run out of context.

## 2. What to write

### 2a. One source note per book → `10-sources/SRC-0XX-<slug>.md`

Use the source template. Fill every section: bibliographic data (find the real authors/year/publisher in the front matter of the text), "At a glance", the central thesis, a chapter map table with the derived notes, "Key ideas → permanent notes", "What is missing / what to read critically" (be honest: thin self-published books, outdated data, unsupported claims), and at most ONE short quote (< 15 words) with its page. Relevance 1–5 for an advertising/creative school (ADC).

### 2b. Permanent notes (zettels) → `20-skills/<skill-slug>/notes/<ID>-<slug>.md`

- Temporary IDs: `<CODE>-<GG><NN>`: CODE = skill code of the note's PRIMARY skill, GG = your group number (two digits), NN = running number for that CODE within your group (01, 02, …). Example: group 05 writes `BRD-0501`, `BRD-0502`, `ART-0501`. Filename: `BRD-0501-<slug-of-title>.md` (lowercase ASCII, hyphens, no diacritics, ≤ 60 chars).
- Put the note in the folder of its primary skill. Use `also:` for other relevant skills (slugs).
- Follow the zettel template and the quality rules in conventions §6: title = a precise claim or concept; ONE idea per note; written in English (American spelling) in your own words, with the book's own terms; body 150–400 words; sections Explanation / Application / Example / Questions / Links / Sources.
- Prefer what is **distinctive and useful** in each book: its named models and frameworks, step-by-step methods, checklists, typologies, memorable cases and campaigns, strong claims, disagreements with other views. Skip generic filler that every book repeats ("social media is important").
- How many: proportional to substance. Rich, core book: 20–40 notes. Solid but narrower book: 10–20. Thin / generic / self-published book: 3–8. Quality over quantity.
- No duplicates inside your group: if a second book covers a concept you already noted, enrich the existing note and add the second source to its `sources:` list (that is valuable: it shows convergence or disagreement between authors).
- `kind`: concept | framework | principle | method | case | checklist | debate. Use `debate` for tensions between authors or schools. Use `case` for campaigns/brands worth remembering.
- `level`: 1 = foundation everyone must know; 2 = practice (methods, applied tools); 3 = advanced / nuanced.
- `status: seed` for all new notes.

### 2c. Links

- Every zettel needs **at least 2 typed links** to other zettels, in the "Links" section: `- **relation** [[ID]]: reason (one sentence)`. Relations: foundation, extends, application, example, contradicts, alternative, see.
- In Phase 1 you may only link to: notes **your group** created, source notes (`[[SRC-0XX]]`), and skill hubs (`[[BRD]]`, `[[ADV]]`, …). Do NOT guess IDs of notes created by other groups: another phase will add cross-group links using the catalog and similarity search.
- Each zettel ends with "Sources" listing `[[SRC-0XX]] Author, *Title*, chapter/page`.

### 2d. Copyright

Paraphrase. Never copy passages. At most one short quote (< 15 words) per note, in quotation marks, with its page. Reproducing the *structure* of a model (its named components) is fine.

## 3. Validate

At the end run: `cd "<KB root>" && python3 tools/kb.py check` and open `_meta/health.md`. Fix every problem in **your own files** (missing fields, wrong folder, broken links among your notes, notes with < 2 links, unknown relations). "Orphan" warnings for your notes mean no other zettel links to them: add a link from a related note of yours. Ignore problems in files of other groups.

Do NOT run `build`, `renumber`, `merge` or `redirect`: other agents are writing at the same time.

## 4. Report → `_meta/reports/G<GG>.md`

- Books processed, how deeply each was read (approx. % and which parts), relevance verdict.
- Notes created per skill code (counts) and the list of IDs + titles.
- **Likely overlaps with other groups**: concepts you noted that other books in this KB probably also cover (e.g., STP, positioning, customer journey, AIDA). This helps the merge phase.
- Taxonomy feedback: concepts that did not fit any skill well.

Your final reply to the orchestrator: ≤ 150 words (counts + anything that went wrong). The real output is the files.
