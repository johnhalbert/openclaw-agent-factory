import yaml
from pathlib import Path

from ingest.crawl_docs import crawl
from ingest.clone_repo import clone
from ingest.parse_markdown import extract_markdown_files, read_markdown
from ingest.chunk_markdown import chunk_text
from ingest.embed_docs import embed_chunks


def update(config_name: str):
    root = Path(__file__).parent

    config = yaml.safe_load((root / "configs" / f"{config_name}.yaml").read_text())

    collection = config["collection"]
    sources = config.get("sources", [])

    tmp = root / "_crawl" / config_name

    chunks = []

    for src in sources:
        if src.startswith("http"):
            crawl(src, tmp)

        if src.endswith(".git"):
            repo = clone(src, tmp)

            for md in extract_markdown_files(repo):
                text = read_markdown(md)
                chunks.extend(list(chunk_text(text)))

    count = embed_chunks(collection, chunks)

    print(f"Indexed {count} chunks into {collection}")


if __name__ == "__main__":
    import sys
    update(sys.argv[1])
