#!/usr/bin/env python3
"""kb.py: the maintenance tool for the ADC knowledge base (a Zettelkasten organized by skills).

No external dependencies (Python 3.9+).

Commands:
  check                 checks the notes; writes _meta/health.md
  build [--rename]      normalizes links, backlinks, indexes, catalog, graph, coverage
  suggest [--skill S] [--top N] [--min X]
                        suggests links between similar notes not yet linked (TF-IDF)
  merge KEEP DROP       redirects every link DROP→KEEP, merges sources/tags, deletes DROP
  redirect FILE         applies `DROP KEEP` redirects from a file (after manual merges)
  renumber [--dry-run]  final IDs (CODE-001…) in the order of the learning path in SKILL.md
  new CODE "Title"      creates a new permanent note from the template, with the next free ID
  stats                 statistics by skill, kind, level, status
"""
import csv
import datetime as _dt
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "_meta"
SKIP_DIRS = {"90-library", "tools", "templates", ".obsidian", ".git", ".claude", "reports"}

ID_RE = re.compile(r"^([A-Z]{3}-\d{3,4})\b")
LINK_RE = re.compile(r"\[\[([^\]|#\\]+)(#[^\]|\\]*)?(?:\\?\|([^\]]*))?\]\]")
TYPED_RE = re.compile(r"^\s*[-*]\s*\*\*([a-z]+)\*\*\s*\[\[([^\]|#]+)")
BACK_START, BACK_END = "<!-- backlinks:start -->", "<!-- backlinks:end -->"
AUTO_START, AUTO_END = "<!-- auto:notes:start -->", "<!-- auto:notes:end -->"

SKILLS = json.loads((META / "skills.json").read_text())
SKILL_BY_CODE = {s["code"]: s for s in SKILLS["skills"]}
SKILL_BY_SLUG = {s["slug"]: s for s in SKILLS["skills"]}
DOMAIN_OF = {c: d for d in SKILLS["domains"] for c in d["skills"]}
RELATIONS = set(SKILLS["relations"])
KINDS = set(SKILLS["kinds"])
LEVEL_NAMES = SKILLS["levels"]

REQUIRED = {
    "zettel": ["id", "title", "type", "kind", "skill", "level", "sources", "status"],
    "source": ["id", "title", "type", "authors", "skills", "relevance"],
    "map": ["id", "title", "type"],
    "skill": ["name", "description", "code", "type"],
}


# ---------------------------------------------------------------- parsing

def deaccent(s):
    s = s.replace("ș", "s").replace("ş", "s").replace("ț", "t").replace("ţ", "t")
    s = s.replace("Ș", "S").replace("Ş", "S").replace("Ț", "T").replace("Ţ", "T")
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slugify(title, maxlen=60):
    s = deaccent(title).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s


def parse_value(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    return v


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def parse_frontmatter(fm):
    data, key = {}, None
    for line in fm.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(m.group(1).strip().strip("'\""))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, raw = m.group(1), m.group(2)
            raw = re.sub(r"\s+#.*$", "", raw) if not raw.strip().startswith(("'", '"')) else raw
            data[key] = parse_value(raw) if raw.strip() else []
    return data


class Note:
    def __init__(self, path):
        self.path = path
        self.text = path.read_text(encoding="utf-8")
        fm, self.body = split_frontmatter(self.text)
        self.meta = parse_frontmatter(fm) if fm is not None else {}
        self.type = self.meta.get("type", "")
        if self.type == "skill":
            self.id = self.meta.get("code", "")
        else:
            self.id = self.meta.get("id", "") if isinstance(self.meta.get("id", ""), str) else ""
        self.title = self.meta.get("title") or self.meta.get("name") or path.stem
        if isinstance(self.title, list):
            self.title = " ".join(self.title)

    @property
    def rel(self):
        return self.path.relative_to(ROOT).as_posix()

    @property
    def link_target(self):
        return self.path.relative_to(ROOT).with_suffix("").as_posix() if self.type == "skill" else self.path.stem

    def body_without_auto(self):
        b = re.sub(re.escape(BACK_START) + r".*?" + re.escape(BACK_END), "", self.body, flags=re.S)
        return re.sub(re.escape(AUTO_START) + r".*?" + re.escape(AUTO_END), "", b, flags=re.S)

    def links(self):
        """[(target_id, relation_or_None)] from the note body (without the auto sections)."""
        out = []
        body = self.body_without_auto()
        typed = {}
        for line in body.splitlines():
            m = TYPED_RE.match(line)
            if m:
                tid = resolve_target(m.group(2))
                if tid:
                    typed.setdefault(tid, m.group(1))
        seen = set()
        for m in LINK_RE.finditer(body):
            tid = resolve_target(m.group(1))
            if tid and tid not in seen:
                seen.add(tid)
                out.append((tid, typed.get(tid)))
        return out

    def words(self):
        b = self.body_without_auto()
        b = re.sub(r"^## (Links|Sources)\b.*", "", b, flags=re.S | re.M)
        return len(re.findall(r"\w+", b))


def resolve_target(target):
    t = target.strip()
    m = ID_RE.match(t)
    if m:
        return m.group(1)
    if re.fullmatch(r"[A-Z]{3}", t) and t in SKILL_BY_CODE:
        return t
    m = re.match(r"^(?:20-skills/)?([a-z0-9-]+)/SKILL$", t)
    if m and m.group(1) in SKILL_BY_SLUG:
        return SKILL_BY_SLUG[m.group(1)]["code"]
    return None


def iter_md():
    for p in sorted(ROOT.rglob("*.md")):
        parts = set(p.relative_to(ROOT).parts[:-1])
        if parts & SKIP_DIRS:
            continue
        yield p


def load():
    notes = []
    for p in iter_md():
        n = Note(p)
        if n.type:
            notes.append(n)
    return notes


def index(notes):
    by_id = {}
    dups = defaultdict(list)
    for n in notes:
        if n.id:
            dups[n.id].append(n)
            by_id.setdefault(n.id, n)
    return by_id, {k: v for k, v in dups.items() if len(v) > 1}


def source_ids(n):
    srcs = n.meta.get("sources", [])
    if isinstance(srcs, str):
        srcs = [srcs]
    out = []
    for s in srcs:
        m = re.match(r"\s*(SRC-\d{3})", s)
        if m:
            out.append(m.group(1))
    return out


def as_list(v):
    if isinstance(v, list):
        return v
    return [v] if v else []


# ---------------------------------------------------------------- check

def cmd_check(quiet=False):
    notes = load()
    by_id, dups = index(notes)
    problems = defaultdict(list)
    incoming = Counter()  # only lateral links, from other permanent notes
    for n in notes:
        if n.type != "zettel":
            continue
        for tid, _ in n.links():
            if tid != n.id:
                incoming[tid] += 1

    for i, group in dups.items():
        problems["Duplicate ID"].append(f"{i}: " + ", ".join(x.rel for x in group))

    for n in notes:
        for f in REQUIRED.get(n.type, []):
            if f not in n.meta or n.meta.get(f) in ("", []):
                problems["Missing frontmatter field"].append(f"{n.rel}: `{f}`")
        if n.type == "zettel":
            if not n.path.name.startswith(n.id + "-") and n.path.stem != n.id:
                problems["File name ≠ ID"].append(f"{n.rel} (id {n.id})")
            code = n.id[:3]
            sk = SKILL_BY_CODE.get(code)
            if not sk:
                problems["Unknown skill code"].append(f"{n.rel}: {code}")
            else:
                if n.meta.get("skill") != sk["slug"]:
                    problems["`skill` does not match the code in the ID"].append(f"{n.rel}: skill={n.meta.get('skill')} cod={code}")
                if f"20-skills/{sk['slug']}/" not in n.rel:
                    problems["Note in the wrong folder"].append(n.rel)
            for a in as_list(n.meta.get("also")):
                if a not in SKILL_BY_SLUG:
                    problems["Unknown skill in `also`"].append(f"{n.rel}: {a}")
            if n.meta.get("kind") and n.meta.get("kind") not in KINDS:
                problems["Invalid `kind`"].append(f"{n.rel}: {n.meta.get('kind')}")
            if str(n.meta.get("level", "")) not in LEVEL_NAMES:
                problems["Invalid `level`"].append(f"{n.rel}: {n.meta.get('level')}")
            if n.meta.get("status") and n.meta.get("status") not in SKILLS["statuses"]:
                problems["Invalid `status`"].append(f"{n.rel}: {n.meta.get('status')}")
            sids = source_ids(n)
            if not sids:
                problems["No source"].append(n.rel)
            for s in sids:
                if s not in by_id:
                    problems["Source does not exist"].append(f"{n.rel}: {s}")
            out_links = [t for t, _ in n.links() if t != n.id and not t.startswith("SRC") and len(t) > 3]
            if len(out_links) < 2:
                problems["Fewer than 2 links to other notes"].append(f"{n.rel} ({len(out_links)})")
            if incoming[n.id] == 0:
                problems["Orphan (no permanent note links to it)"].append(n.rel)
            w = n.words()
            if w < 100 or w > 650:
                problems["Unusual length (body < 100 or > 650 words)"].append(f"{n.rel}: {w}")
        for tid, rel in n.links():
            if tid not in by_id:
                problems["Broken link"].append(f"{n.rel} → {tid}")
        if n.type == "zettel":
            for line in n.body_without_auto().splitlines():
                m = TYPED_RE.match(line)
                if m and m.group(1) not in RELATIONS:
                    problems["Unknown relation"].append(f"{n.rel}: **{m.group(1)}**")
                elif not m and re.match(r"^\s*[-*]\s*\*\*", line) and "[[" in line:
                    problems["Unknown relation"].append(f"{n.rel}: {line.strip()[:60]}")

    total = sum(len(v) for v in problems.values())
    zettels = [n for n in notes if n.type == "zettel"]
    lines = [
        "# Knowledge base health",
        "",
        f"_Generated by `tools/kb.py check` on {_dt.datetime.now():%Y-%m-%d %H:%M}._",
        "",
        f"- Total notes: **{len(notes)}** (permanent: {len(zettels)}, sources: {sum(n.type == 'source' for n in notes)}, "
        f"skills: {sum(n.type == 'skill' for n in notes)}, maps: {sum(n.type == 'map' for n in notes)})",
        f"- Problems: **{total}**",
        "",
    ]
    for k in sorted(problems, key=lambda k: -len(problems[k])):
        lines.append(f"## {k} ({len(problems[k])})")
        lines.append("")
        lines += [f"- {x}" for x in problems[k][:300]]
        if len(problems[k]) > 300:
            lines.append(f"- … {len(problems[k]) - 300} more")
        lines.append("")
    (META / "health.md").write_text("\n".join(lines), encoding="utf-8")
    if not quiet:
        print(f"{len(notes)} notes, {total} problems → _meta/health.md")
        for k in sorted(problems, key=lambda k: -len(problems[k])):
            print(f"  {len(problems[k]):>4}  {k}")
    return problems


# ---------------------------------------------------------------- build

def normalize_links(text, by_id):
    """[[ID]] → [[stem|ID]]; in table rows the separator becomes \\| (otherwise it breaks the table)."""
    def fix_line(line):
        sep = "\\|" if line.lstrip().startswith("|") else "|"

        def rep(m):
            target, anchor, alias = m.group(1), m.group(2) or "", m.group(3)
            tid = resolve_target(target)
            if not tid or tid not in by_id:
                return m.group(0)
            n = by_id[tid]
            label = alias if alias and not ID_RE.match(alias) and alias not in SKILL_BY_CODE else tid
            return f"[[{n.link_target}{anchor}{sep}{label}]]"
        return LINK_RE.sub(rep, line)
    return "\n".join(fix_line(l) for l in text.split("\n"))


def replace_block(text, start, end, content):
    block = f"{start}\n{content}\n{end}"
    if start in text and end in text:
        return re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    return text.rstrip() + "\n\n" + block + "\n"


def md_link(n, table=False):
    sep = "\\|" if table else "|"
    return f"[[{n.link_target}{sep}{n.id}]]"


def cmd_build(rename=False):
    notes = load()
    by_id, dups = index(notes)
    if dups:
        print("Warning: duplicate IDs. Run check.", file=sys.stderr)

    if rename:
        for n in notes:
            if n.type == "zettel" and n.id:
                want = f"{n.id}-{slugify(n.title)}.md"
                if n.path.name != want:
                    new = n.path.with_name(want)
                    if not new.exists():
                        n.path.rename(new)
                        n.path = new
        notes = load()
        by_id, _ = index(notes)

    backlinks = defaultdict(list)
    edges = []
    for n in notes:
        for tid, rel in n.links():
            if tid in by_id and tid != n.id:
                backlinks[tid].append((n, rel))
                edges.append({"source": n.id, "target": tid, "relation": rel or "inline"})

    zettels = sorted([n for n in notes if n.type == "zettel"], key=lambda n: n.id)
    by_skill = defaultdict(list)
    for z in zettels:
        by_skill[z.meta.get("skill")].append(z)

    for n in notes:
        text = n.text
        fm, body = split_frontmatter(text)
        body = normalize_links(body, by_id)
        if n.type in ("zettel", "source", "map"):
            bl = sorted(backlinks.get(n.id, []), key=lambda x: (x[0].type != "zettel", x[0].id))
            items = []
            for src, rel in bl:
                if src.type == "skill":
                    continue
                r = f" _{rel}_" if rel else ""
                items.append(f"- {md_link(src)}{r}: {src.title}")
            content = "## Backlinks\n\n" + ("\n".join(items) if items else "_No note links here yet._")
            body = replace_block(body, BACK_START, BACK_END, content)
        if n.type == "skill":
            code = n.id
            slug = SKILL_BY_CODE.get(code, {}).get("slug")
            own = by_skill.get(slug, [])
            also = [z for z in zettels if slug in as_list(z.meta.get("also"))]
            rows = ["| ID | Title | Kind | Level | Status |", "|---|---|---|---|---|"]
            for z in own:
                rows.append(f"| {md_link(z, table=True)} | {z.title} | {z.meta.get('kind', '')} | "
                            f"{LEVEL_NAMES.get(str(z.meta.get('level')), '')} | {z.meta.get('status', '')} |")
            content = f"_{len(own)} own notes._\n\n" + "\n".join(rows)
            if also:
                content += "\n\n**Notes from other skills that are also relevant here:**\n\n" + "\n".join(
                    f"- {md_link(z)}: {z.title}" for z in also)
            body = replace_block(body, AUTO_START, AUTO_END, content)
        new_text = f"---\n{fm}\n---\n{body}" if fm is not None else body
        if new_text != n.text:
            n.path.write_text(new_text, encoding="utf-8")

    srcs = sorted([n for n in notes if n.type == "source"], key=lambda n: n.id)
    # generated maps (frontmatter `auto: debates | library | curriculum`)
    for n in [x for x in notes if x.type == "map" and x.meta.get("auto")]:
        kind = n.meta.get("auto")
        if kind == "debates":
            parts = []
            for s in SKILLS["skills"]:
                ds = [z for z in by_skill.get(s["slug"], []) if z.meta.get("kind") == "debate"]
                if ds:
                    parts.append(f"### {s['code']} · {s['name']}\n")
                    parts += [f"- {md_link(z)}: {z.title}" for z in ds]
                    parts.append("")
            content = f"_{sum(1 for z in zettels if z.meta.get('kind') == 'debate')} debate notes._\n\n" + "\n".join(parts)
        elif kind == "library":
            cited = Counter(s for z in zettels for s in source_ids(z))
            rows_ = ["| Source | Title | Authors | Year | Relevance | Skills | Notes citing it |", "|---|---|---|---|---|---|---|"]
            for sn in sorted(srcs, key=lambda x: (-int(str(x.meta.get("relevance", 0)) or 0), x.id)):
                r = int(str(sn.meta.get("relevance", 0)) or 0)
                sk = ", ".join(SKILL_BY_SLUG[k]["code"] for k in as_list(sn.meta.get("skills")) if k in SKILL_BY_SLUG)
                rows_.append(f"| {md_link(sn, table=True)} | {sn.title} | {', '.join(as_list(sn.meta.get('authors')))} | "
                             f"{sn.meta.get('year', '')} | {'★' * r}{'☆' * (5 - r)} | {sk} | {cited[sn.id]} |")
            content = "\n".join(rows_)
        elif kind == "curriculum":
            parts = []
            for d in SKILLS["domains"]:
                parts.append(f"### {d['code']} · {d['name']}\n")
                for c in d["skills"]:
                    s = SKILL_BY_CODE[c]
                    hub = by_id.get(c)
                    own = [z.id for z in by_skill.get(s["slug"], [])]
                    first = (skill_order(hub, set(own)) if hub else [])[:3] or own[:3]
                    starts = ", ".join(md_link(by_id[i]) for i in first if i in by_id)
                    parts.append(f"- [[20-skills/{s['slug']}/SKILL|{c}]] **{s['name']}** ({len(own)} notes): start with {starts}")
                parts.append("")
            content = "\n".join(parts)
        else:
            continue
        text = n.path.read_text(encoding="utf-8")
        new = replace_block(text, AUTO_START, AUTO_END, content)
        if new != text:
            n.path.write_text(new, encoding="utf-8")

    # catalog
    rows = []
    for n in notes:
        rows.append({
            "id": n.id, "type": n.type, "title": n.title, "path": n.rel,
            "skill": n.meta.get("skill", n.meta.get("name", "")) if n.type != "source" else "",
            "also": as_list(n.meta.get("also")), "kind": n.meta.get("kind", ""),
            "level": n.meta.get("level", ""), "status": n.meta.get("status", ""),
            "tags": as_list(n.meta.get("tags")), "sources": source_ids(n),
            "out": [t for t, _ in n.links() if t != n.id], "in": [s.id for s, _ in backlinks.get(n.id, [])],
            "words": n.words(),
        })
    (META / "catalog.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(META / "catalog.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "type", "title", "skill", "kind", "level", "status", "sources", "in", "out", "path"])
        for r in rows:
            w.writerow([r["id"], r["type"], r["title"], r["skill"], r["kind"], r["level"], r["status"],
                        " ".join(r["sources"]), len(r["in"]), len(r["out"]), r["path"]])

    nodes = [{"id": n.id, "title": n.title, "type": n.type,
              "skill": n.meta.get("skill") if n.type == "zettel" else (SKILL_BY_CODE.get(n.id, {}).get("slug") if n.type == "skill" else None),
              "kind": n.meta.get("kind"), "level": n.meta.get("level"), "path": n.rel} for n in notes]
    (META / "graph.json").write_text(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1), encoding="utf-8")

    # coverage: skill × source
    srcs = sorted([n for n in notes if n.type == "source"], key=lambda n: n.id)
    cov = defaultdict(Counter)
    for z in zettels:
        for s in source_ids(z):
            cov[z.meta.get("skill")][s] += 1
    lines = ["# Coverage: skill × source", "", f"_Generated by `kb.py build` on {_dt.datetime.now():%Y-%m-%d %H:%M}._", "",
             "How many permanent notes from each skill cite each source.", "",
             "## By skill", "", "| Skill | Notes | Level 1/2/3 | Sources used | Top sources |", "|---|---|---|---|---|"]
    for s in SKILLS["skills"]:
        own = by_skill.get(s["slug"], [])
        lv = Counter(str(z.meta.get("level")) for z in own)
        top = ", ".join(f"{k} ({v})" for k, v in cov[s["slug"]].most_common(4))
        lines.append(f"| {s['code']} {s['name']} | {len(own)} | {lv['1']}/{lv['2']}/{lv['3']} | {len(cov[s['slug']])} | {top} |")
    lines += ["", "## By source", "", "| Source | Title | Notes citing it | Skills |", "|---|---|---|---|"]
    for sn in srcs:
        cnt = sum(cov[k][sn.id] for k in cov)
        sk = sorted({k for k in cov if cov[k][sn.id]})
        lines.append(f"| {sn.id} | {sn.title} | {cnt} | {', '.join(SKILL_BY_SLUG[k]['code'] for k in sk if k in SKILL_BY_SLUG)} |")
    thin = [s for s in SKILLS["skills"] if len(by_skill.get(s["slug"], [])) < 10]
    if thin:
        lines += ["", "## Gaps", ""] + [f"- **{s['code']}** {s['name']}: only {len(by_skill.get(s['slug'], []))} notes." for s in thin]
    (META / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # INDEX auto
    idx = ROOT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        parts = []
        for d in SKILLS["domains"]:
            parts.append(f"### {d['code']} · {d['name']}\n")
            for c in d["skills"]:
                s = SKILL_BY_CODE[c]
                own = by_skill.get(s["slug"], [])
                parts.append(f"- [[20-skills/{s['slug']}/SKILL|{c}]] **{s['name']}**: {len(own)} notes")
            parts.append("")
        parts.append(f"**Total:** {len(zettels)} permanent notes · {len(srcs)} sources · "
                     f"{len([n for n in notes if n.type == 'map'])} maps · {len(edges)} links")
        idx.write_text(replace_block(t, AUTO_START, AUTO_END, "\n".join(parts)), encoding="utf-8")

    print(f"build: {len(notes)} notes, {len(edges)} links. Catalog, graph and coverage updated.")


# ---------------------------------------------------------------- suggest

STOP = set("""a about above after again against all also am an and any are as at be because been before being
below between both but by can could did do does doing down during each few for from further had has have having he her
here hers him his how i if in into is it its itself just me more most my no nor not now of off on once only or other our
ours out over own same she should so some such than that the their theirs them then there these they this those through
to too under until up very was we were what when where which while who whom why will with would you your yours
one two three can may might must also even way ways make makes made use used using get gets like well much many often
note notes idea example application explanation questions links sources ch p pp see foundation extends src
""".split())


def tokenize(text):
    t = deaccent(text.lower())
    t = re.sub(r"\[\[[^\]]*\]\]", " ", t)
    return [w for w in re.findall(r"[a-z][a-z0-9-]{2,}", t) if w not in STOP]


def cmd_suggest(skill=None, top=6, min_sim=0.10):
    notes = [n for n in load() if n.type == "zettel"]
    docs = {}
    for n in notes:
        body = n.body_without_auto()
        body = re.split(r"^## (Links|Sources)\b", body, flags=re.M)[0]
        tags = " ".join(as_list(n.meta.get("tags")))
        docs[n.id] = tokenize((n.title + " ") * 3 + (tags + " ") * 2 + body)
    df = Counter()
    for toks in docs.values():
        df.update(set(toks))
    N = len(docs)
    vecs = {}
    for i, toks in docs.items():
        tf = Counter(toks)
        v = {w: (1 + math.log(c)) * math.log((N + 1) / (df[w] + 0.5)) for w, c in tf.items() if df[w] < N * 0.4}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vecs[i] = {w: x / norm for w, x in v.items()}
    linked = set()
    for n in notes:
        for t, _ in n.links():
            linked.add((n.id, t))
            linked.add((t, n.id))
    by_id = {n.id: n for n in notes}
    postings = defaultdict(list)
    for i, v in vecs.items():
        for w, x in v.items():
            postings[w].append((i, x))
    out = []
    for n in notes:
        if skill and n.meta.get("skill") != skill and skill not in as_list(n.meta.get("also")):
            continue
        scores = Counter()
        for w, x in vecs[n.id].items():
            for j, y in postings[w]:
                if j != n.id:
                    scores[j] += x * y
        cands = [(j, s) for j, s in scores.most_common(40) if s >= min_sim and (n.id, j) not in linked][:top]
        if cands:
            out.append((n, cands))
    lines = ["# Link suggestions", "",
             f"_Generated by `kb.py suggest` on {_dt.datetime.now():%Y-%m-%d %H:%M}. TF-IDF similarity; "
             "confirm only the links that have a clear reason and write them with a typed relation._", ""]
    for n, cands in out:
        lines.append(f"## {n.id}: {n.title}")
        for j, s in cands:
            o = by_id[j]
            same = "" if o.meta.get("skill") == n.meta.get("skill") else f" · _{o.meta.get('skill')}_"
            lines.append(f"- {s:.2f} [[{j}]] {o.title}{same}")
        lines.append("")
    name = f"link-suggestions-{skill}.md" if skill else "link-suggestions.md"
    (META / name).write_text("\n".join(lines), encoding="utf-8")
    print(f"suggest: {sum(len(c) for _, c in out)} suggestions for {len(out)} notes → _meta/{name}")


# ---------------------------------------------------------------- merge / renumber / new

def rewrite_ids(mapping, notes=None):
    """Replaces IDs in every .md file (a single pass, no chaining)."""
    if not mapping:
        return
    pat = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)) + r")\b(?!-\d)")
    for p in iter_md():
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith("_meta/") or rel in ("README.md", "CLAUDE.md"):
            continue  # the documentation holds example IDs, not real links
        t = p.read_text(encoding="utf-8")
        new = pat.sub(lambda m: mapping[m.group(1)], t)
        # links [[OLD-slug|...]] become [[NEW-slug|...]]; build rewrites them anyway
        if new != t:
            p.write_text(new, encoding="utf-8")


def set_list_field(text, field, values):
    fm, body = split_frontmatter(text)
    if fm is None:
        return text
    lines = fm.splitlines()
    out, i, done = [], 0, False
    while i < len(lines):
        line = lines[i]
        if re.match(rf"^{field}:", line):
            done = True
            i += 1
            while i < len(lines) and re.match(r"^\s+-\s", lines[i]):
                i += 1
            if field == "sources":
                out.append(f"{field}:")
                out += [f"  - {v}" for v in values]
            else:
                out.append(f"{field}: [{', '.join(values)}]")
            continue
        out.append(line)
        i += 1
    if not done:
        out.append(f"{field}: [{', '.join(values)}]" if field != "sources" else f"{field}:\n" + "\n".join(f"  - {v}" for v in values))
    return f"---\n" + "\n".join(out) + f"\n---\n{body}"


def cmd_merge(keep, drop):
    notes = load()
    by_id, _ = index(notes)
    if keep not in by_id or drop not in by_id:
        sys.exit(f"No such ID: {keep if keep not in by_id else drop}")
    k, d = by_id[keep], by_id[drop]
    text = k.text
    for field in ("sources", "tags", "also"):
        kv, dv = as_list(k.meta.get(field)), as_list(d.meta.get(field))
        merged = kv + [x for x in dv if x not in kv and not (field == "also" and x == k.meta.get("skill"))]
        if field == "also" and d.meta.get("skill") != k.meta.get("skill") and d.meta.get("skill") not in merged:
            merged.append(d.meta.get("skill"))
        if merged != kv:
            text = set_list_field(text, field, merged)
    k.path.write_text(text, encoding="utf-8")
    d.path.unlink()
    rewrite_ids({drop: keep})
    # remove self-links created by the redirect
    t = k.path.read_text(encoding="utf-8")
    t = re.sub(rf"^\s*[-*]\s*\*\*\w+\*\*\s*\[\[{re.escape(keep)}[^\]]*\]\].*\n", "", t, flags=re.M)
    k.path.write_text(t, encoding="utf-8")
    log = META / "merges.log"
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"{_dt.datetime.now():%Y-%m-%d %H:%M}\t{drop} → {keep}\t{d.title}\n")
    print(f"merge: {drop} → {keep}. Every link to {drop} now points to {keep}. Run build.")


def cmd_redirect(path):
    """Applies redirects from a file: `DROP KEEP` (or `DROP → KEEP`) on each line."""
    mapping = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        ids = re.findall(r"[A-Z]{3}-\d{3,4}", line)
        if len(ids) >= 2 and not line.lstrip().startswith("#"):
            mapping[ids[0]] = ids[1]
    # resolve chains A→B, B→C
    for k in list(mapping):
        seen = {k}
        while mapping[k] in mapping and mapping[k] not in seen:
            seen.add(mapping[k])
            mapping[k] = mapping[mapping[k]]
    rewrite_ids(mapping)
    with open(META / "merges.log", "a", encoding="utf-8") as f:
        for a, b in mapping.items():
            f.write(f"{_dt.datetime.now():%Y-%m-%d %H:%M}\t{a} → {b}\t(redirect)\n")
    print(f"redirect: {len(mapping)} IDs redirected. Run build.")


def skill_order(skill_note, own_ids):
    body = skill_note.body_without_auto()
    order = []
    for m in LINK_RE.finditer(body):
        tid = resolve_target(m.group(1))
        if tid in own_ids and tid not in order:
            order.append(tid)
    return order


def cmd_renumber(dry=False):
    notes = load()
    by_id, dups = index(notes)
    if dups:
        sys.exit("Duplicate IDs; resolve them first (kb.py check).")
    mapping = {}
    for s in SKILLS["skills"]:
        own = sorted([n for n in notes if n.type == "zettel" and n.id.startswith(s["code"] + "-")],
                     key=lambda n: (int(n.meta.get("level", 9) or 9), n.id))
        own_ids = [n.id for n in own]
        hub = by_id.get(s["code"])
        order = skill_order(hub, set(own_ids)) if hub else []
        order += [i for i in own_ids if i not in order]
        for k, old in enumerate(order, 1):
            new = f"{s['code']}-{k:03d}"
            if new != old:
                mapping[old] = new
    if dry:
        for a, b in mapping.items():
            print(f"{a} → {b}")
        return
    rewrite_ids(mapping)
    for n in load():
        if n.type == "zettel":
            want = f"{n.id}-{slugify(n.title)}.md"
            if n.path.name != want:
                n.path.rename(n.path.with_name(want))
    (META / "renumber-map.json").write_text(json.dumps(mapping, indent=1), encoding="utf-8")
    print(f"renumber: {len(mapping)} IDs changed → _meta/renumber-map.json. Now run build.")


def cmd_new(code, title):
    s = SKILL_BY_CODE.get(code)
    if not s:
        sys.exit(f"Unknown code: {code}")
    notes = load()
    nums = [int(n.id.split("-")[1]) for n in notes if n.type == "zettel" and n.id.startswith(code + "-")]
    nid = f"{code}-{(max(nums) + 1 if nums else 1):03d}"
    tpl = (META / "templates" / "zettel.md").read_text(encoding="utf-8")
    tpl = tpl.replace("XXX-000", nid, 1).replace("skill-slug", s["slug"])
    tpl = tpl.replace("The title is a precise claim or concept", title)
    p = ROOT / "20-skills" / s["slug"] / "notes" / f"{nid}-{slugify(title)}.md"
    p.write_text(tpl, encoding="utf-8")
    print(p.relative_to(ROOT))


def cmd_stats():
    notes = load()
    z = [n for n in notes if n.type == "zettel"]
    print(f"Notes: {len(notes)} · permanent: {len(z)} · sources: {sum(n.type == 'source' for n in notes)} · maps: {sum(n.type == 'map' for n in notes)}")
    by = Counter(n.meta.get("skill") for n in z)
    for s in SKILLS["skills"]:
        print(f"  {s['code']} {s['slug']:24} {by[s['slug']]:>4}")
    print("kind:", dict(Counter(n.meta.get("kind") for n in z)))
    print("level:", dict(Counter(str(n.meta.get("level")) for n in z)))
    print("status:", dict(Counter(n.meta.get("status") for n in z)))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, args = argv[0], argv[1:]

    def opt(name, default=None, cast=str):
        if name in args:
            i = args.index(name)
            return cast(args[i + 1])
        return default

    if cmd == "check":
        cmd_check()
    elif cmd == "build":
        cmd_build(rename="--rename" in args)
    elif cmd == "suggest":
        cmd_suggest(skill=opt("--skill"), top=opt("--top", 6, int), min_sim=opt("--min", 0.10, float))
    elif cmd == "merge" and len(args) == 2:
        cmd_merge(args[0], args[1])
    elif cmd == "redirect" and len(args) == 1:
        cmd_redirect(args[0])
    elif cmd == "renumber":
        cmd_renumber(dry="--dry-run" in args)
    elif cmd == "new" and len(args) == 2:
        cmd_new(args[0], args[1])
    elif cmd == "stats":
        cmd_stats()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
