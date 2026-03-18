from pathlib import Path


def extract_markdown_files(root: Path):
    return list(root.glob("**/*.md"))


def read_markdown(path: Path):
    return path.read_text(errors="ignore")
