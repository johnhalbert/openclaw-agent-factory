import argparse
from pathlib import Path
import os
import chromadb


def get_client(path: str | None = None):
    base = path or os.environ.get("OPENCLAW_CHROMA_PATH") or str(Path(".local/chroma"))
    Path(base).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=base)


def search(collection_name: str, query: str, limit: int = 5, path: str | None = None):
    client = get_client(path)
    collection = client.get_or_create_collection(collection_name)
    results = collection.query(query_texts=[query], n_results=limit)

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0] if results.get("metadatas") else []

    for i, doc in enumerate(docs, start=1):
        print(f"[{i}] {doc[:500]}\\n")
        if i - 1 < len(metas) and metas[i - 1]:
            print(f"    meta: {metas[i - 1]}\\n")


def main():
    parser = argparse.ArgumentParser(description="Search persistent Chroma documentation collections")
    parser.add_argument("collection")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--path", default=None)
    args = parser.parse_args()

    search(args.collection, args.query, args.limit, args.path)


if __name__ == "__main__":
    main()
