# 90-library: the full texts (local only)

This folder holds, **only on your computer**, the text extracted from the copies of the books (`text/<slug>.txt`) and the transcript of the audiobook (`text/audiobook/NN.txt`). AI agents use them to check a note or to go deeper into a chapter.

The texts are **not in the repository** (see `.gitignore`): they are copyrighted books. The repository contains only the notes (paraphrased, with references to chapters/pages) and the tools.

## How to regenerate the texts

Work on a **copy** of the books folder, not on the originals.

```bash
pip install -r tools/requirements.txt
```

```bash
python tools/extract_texts.py --src "/path/to/the/copy/Books for ADC School" --out 90-library/text
```

The audiobook (Apple Silicon, local Whisper model):

```bash
pip install mlx-whisper
```

```bash
python tools/transcribe_audiobook.py --src "/path/to/the/copy/Audiobook_Strategic Advertising Management 6th Edition"
```

The mapping between the source IDs (`SRC-0XX`) and the files is in `_meta/sources.json`.
