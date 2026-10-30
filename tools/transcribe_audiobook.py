"""Transcribes an audiobook locally (a folder of NN.mp3 files) with mlx-whisper (Apple Silicon).

Usage:
    pip install mlx-whisper
    python tools/transcribe_audiobook.py --src "/path/to/the/copy/Audiobook_..." --out 90-library/text/audiobook

Result: one file <out>/NN.txt per chapter. Resumes where it stopped if interrupted.
"""
import argparse
import time
from pathlib import Path

import mlx_whisper

ap = argparse.ArgumentParser()
ap.add_argument("--src", required=True, help="the folder with the COPIES of the mp3 files")
ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "90-library" / "text" / "audiobook"))
ap.add_argument("--model", default="mlx-community/whisper-large-v3-turbo")
ap.add_argument("--language", default="en")
args = ap.parse_args()

out = Path(args.out)
out.mkdir(parents=True, exist_ok=True)
files = sorted(Path(args.src).glob("*.mp3"), key=lambda p: int(p.stem) if p.stem.isdigit() else p.stem)
for f in files:
    dst = out / (f"{int(f.stem):02d}.txt" if f.stem.isdigit() else f"{f.stem}.txt")
    if dst.exists():
        continue
    t = time.time()
    r = mlx_whisper.transcribe(str(f), path_or_hf_repo=args.model, language=args.language)
    dst.write_text(r["text"].strip())
    print(f"{f.name}: {time.time() - t:.0f}s, {len(r['text'].split())} words", flush=True)
