from pathlib import Path


def chunk_text(text: str, size: int = 800):
    for i in range(0, len(text), size):
        yield text[i:i+size]


def chunk_file(path: Path):
    text = path.read_text(errors="ignore")
    return list(chunk_text(text))
