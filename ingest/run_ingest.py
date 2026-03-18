import yaml
from pathlib import Path
from ingest.fetch_docs import fetch
from ingest.chunk_markdown import chunk_file
from ingest.build_chroma import build_collection


def run(config_name: str):
    root = Path(__file__).resolve().parent
    config_path = root / "configs" / f"{config_name}.yaml"

    config = yaml.safe_load(config_path.read_text())

    collection = config["collection"]
    sources = config["sources"]

    tmp_dir = root / "_tmp" / config_name

    all_chunks = []

    for url in sources:
        fetch(url, tmp_dir)

    for file in tmp_dir.glob("**/*"):
        if file.is_file():
            all_chunks.extend(chunk_file(file))

    build_collection(collection, all_chunks)


if __name__ == "__main__":
    import sys
    run(sys.argv[1])
