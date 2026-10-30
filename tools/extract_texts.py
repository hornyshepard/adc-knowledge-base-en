"""Extracts the text (with page/section markers) from the COPIES of the books (PDF, EPUB, AZW3, DOCX).

Always work on a copy of the books folder, not on the originals.

Usage:
    pip install -r tools/requirements.txt
    python tools/extract_texts.py --src "/path/to/the/copy/of/the/books" --out 90-library/text

Result: <out>/<slug>.txt, <slug>.toc.txt (for PDFs with a table of contents) and _manifest.json.
"""
import argparse
import json
import os
import re
import sys
import zipfile
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

import pymupdf
from bs4 import BeautifulSoup

_ap = argparse.ArgumentParser()
_ap.add_argument("--src", required=True, help="the folder with the COPIES of the books")
_ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "90-library" / "text"))
_args = _ap.parse_args()
SRC = Path(_args.src)
OUT = Path(_args.out)
OUT.mkdir(parents=True, exist_ok=True)


def slugify(name: str) -> str:
    name = re.sub(r"\.(pdf|epub|azw3|docx)$", "", name, flags=re.I)
    name = name.lower().replace("&", "and")
    name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return name[:70]


def html_to_text(html: bytes) -> str:
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style"]):
        t.decompose()
    for h in soup.find_all(re.compile(r"^h[1-4]$")):
        h.insert_before("\n\n## ")
        h.insert_after("\n")
    for br in soup.find_all(["br"]):
        br.replace_with("\n")
    for p in soup.find_all(["p", "div", "li", "tr"]):
        p.insert_after("\n")
    text = soup.get_text()
    text = re.sub(r"[ \t\xa0]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def epub_spine(z: zipfile.ZipFile):
    container = z.read("META-INF/container.xml")
    opf_path = BeautifulSoup(container, "xml").find("rootfile")["full-path"]
    base = os.path.dirname(opf_path)
    opf = BeautifulSoup(z.read(opf_path), "xml")
    meta = {}
    for k in ["title", "creator", "date", "publisher", "language"]:
        el = opf.find(k)
        if el is not None:
            meta[k] = el.get_text(strip=True)
    manifest = {i["id"]: i["href"] for i in opf.find_all("item") if i.get("href")}
    spine = [manifest[i["idref"]] for i in opf.find_all("itemref") if i.get("idref") in manifest]
    paths = []
    for href in spine:
        p = os.path.normpath(os.path.join(base, href)).replace("\\", "/")
        p = re.sub(r"#.*$", "", p)
        from urllib.parse import unquote
        p = unquote(p)
        paths.append(p)
    return meta, paths


def extract_epub(path: Path):
    z = zipfile.ZipFile(path)
    meta, paths = epub_spine(z)
    names = set(z.namelist())
    parts = []
    for i, p in enumerate(paths):
        if p not in names:
            continue
        t = html_to_text(z.read(p))
        if t:
            parts.append(f"\n\n=== [section {i}] ===\n{t}")
    return meta, "".join(parts), None


def extract_pdf(path: Path):
    doc = pymupdf.open(path)
    meta = {k: v for k, v in (doc.metadata or {}).items() if v}
    toc = doc.get_toc(simple=True)
    parts = []
    for i, page in enumerate(doc):
        t = page.get_text("text")
        parts.append(f"\n\n=== [page {i + 1}] ===\n{t}")
    meta["pages"] = doc.page_count
    return meta, "".join(parts), toc


def extract_azw3(path: Path):
    import mobi
    tmpdir, filepath = mobi.extract(str(path))
    fp = Path(filepath)
    if fp.suffix.lower() == ".epub":
        return extract_epub(fp)
    if fp.suffix.lower() in (".html", ".htm"):
        return {}, html_to_text(fp.read_bytes()), None
    # mobi7 fallback: find any html in tmpdir
    htmls = sorted(Path(tmpdir).rglob("*.htm*"))
    return {}, "\n\n".join(html_to_text(h.read_bytes()) for h in htmls), None


def extract_docx(path: Path):
    import docx
    d = docx.Document(str(path))
    lines = [p.text for p in d.paragraphs]
    for table in d.tables:
        for row in table.rows:
            lines.append(" | ".join(c.text for c in row.cells))
    return {}, "\n".join(lines), None


def main():
    manifest = {}
    mf = OUT / "_manifest.json"
    if mf.exists():
        manifest = json.loads(mf.read_text())
    files = sorted(p for p in SRC.rglob("*") if p.suffix.lower() in (".pdf", ".epub", ".azw3", ".docx"))
    for p in files:
        rel = str(p.relative_to(SRC))
        prefix = "brief-" if p.parent.name == "Brief Models" else ""
        slug = prefix + slugify(p.name)
        if slug in manifest and (OUT / f"{slug}.txt").exists():
            continue
        try:
            ext = p.suffix.lower()
            fn = {".pdf": extract_pdf, ".epub": extract_epub, ".azw3": extract_azw3, ".docx": extract_docx}[ext]
            meta, text, toc = fn(p)
            (OUT / f"{slug}.txt").write_text(text)
            if toc:
                (OUT / f"{slug}.toc.txt").write_text("\n".join(f"{'  ' * (l - 1)}{t} (p.{pg})" for l, t, pg in toc))
            words = len(text.split())
            manifest[slug] = {"file": rel, "format": ext[1:], "words": words, "meta": meta, "has_toc": bool(toc)}
            print(f"OK  {words:>8} words  {slug}", flush=True)
        except Exception as e:  # keep going, report at the end
            manifest[slug] = {"file": rel, "error": repr(e)}
            print(f"ERR {slug}: {e!r}", flush=True)
        mf.write_text(json.dumps(manifest, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
