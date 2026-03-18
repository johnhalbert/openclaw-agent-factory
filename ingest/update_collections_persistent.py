import yaml
from pathlib import Path

from ingest.crawl_docs import crawl
from ingest.clone_repo import clone
from ingest.parse_markdown import extract_markdown_files, read_markdown
from ingest.chunk_markdown import chunk_text
from ingest.build_chroma_persistent import build_collection


def update(config_name: str):
    root = Path(__file__).parent
    config = yaml.safe_load((root / "configs" / f"{config_name}.yaml").read_text())

    collection = config["collection"]
    sources = config.get("sources", [])
    tmp = root / "_crawl" / config_name
    chunks = []

    for src in sources:
        if src.startswith("http") and "github.com" not in src:
            crawl(src, tmp)
        elif src.startswith("http") and "github.com" in src:
            repo_url = src if src.endswith(".git") else src + ".git"
            repo = clone(repo_url, tmp)
            for md in extract_markdown_files(repo):
                text = read_markdown(md)
                chunks.extend(list(chunk_text(text)))

    build_collection(collection, chunks)
    print(f"Indexed {len(chunks)} chunks into persistent collection {collection}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python ingest/update_collections_persistent.py <config-name>")
    update(sys.argv[1])
