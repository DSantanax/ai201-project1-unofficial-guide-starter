"""Milestone 3 — Document ingestion and fixed-size chunking.

Turns the OMSCentral course-review .txt files in documents/ into a flat list of
overlapping fixed-size character chunks, ready to embed into ChromaDB in Milestone 4.
"""

import re
from glob import glob
from pathlib import Path

try:
    import config

    DEFAULT_DOCS_PATH = config.DOCS_PATH
except ModuleNotFoundError:
    # config pulls in optional Milestone 4+ deps (python-dotenv). Milestone 3 only
    # needs the documents path, so fall back to it when those aren't installed yet.
    DEFAULT_DOCS_PATH = "./documents"


def _course_name(filename: str) -> str:
    """Derive a clean course name from a filename.

    Uses the filename stem with '-' and '_' replaced by spaces, then collapses
    repeated whitespace. e.g. "artificial-intelligence.txt" -> "artificial intelligence".
    """
    stem = Path(filename).stem.replace("-", "").replace("_", "").replace("=", "")
    return re.sub(r"\s+", " ", stem).strip()


def load_docs(docs_path: str = DEFAULT_DOCS_PATH) -> list[dict]:
    """Load every .txt file in ``docs_path`` into a list of document dicts.

    Returns one dict per file with the filename, full text, and derived course name.
    """
    docs = []
    for path in sorted(glob(str(Path(docs_path) / "*.txt"))):
        text = Path(path).read_text(encoding="utf-8")
        filename = Path(path).name
        docs.append(
            {
                "filename": filename,
                "text": text,
                "course": _course_name(filename),
            }
        )
    return docs


def chunk_documents(
    docs: list[dict], chunk_size: int = 600, overlap: int = 50
) -> list[dict]:
    """Split each document's text into overlapping fixed-size character chunks.

    A sliding window of ``chunk_size`` characters advances by ``chunk_size - overlap``
    each step over the entire file text. The final (shorter) tail chunk is included.
    """
    step = chunk_size - overlap
    if step <= 0:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    for doc in docs:
        text = doc["text"]
        stem = Path(doc["filename"]).stem
        index = 0
        start = 0
        while start < len(text):
            piece = text[start : start + chunk_size]
            piece = piece.replace("-", "").replace("=", "")
            if piece.strip():
                chunks.append(
                    {
                        "chunk_id": f"{stem}_{index}",
                        "chunk": piece,
                        "course": doc["course"],
                        "filename": doc["filename"],
                    }
                )
                index += 1
            start += step
    return chunks
