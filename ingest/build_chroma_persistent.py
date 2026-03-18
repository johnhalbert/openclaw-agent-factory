from pathlib import Path
import os
import chromadb


def get_client(path: str | None = None):
    base = path or os.environ.get("OPENCLAW_CHROMA_PATH") or str(Path(".local/chroma"))
    Path(base).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=base)


def build_collection(name: str, chunks, path: str | None = None):
    client = get_client(path)
    collection = client.get_or_create_collection(name)

    ids = []
    docs = []
    for i, chunk in enumerate(chunks):
        ids.append(str(i))
        docs.append(chunk)

    if docs:
        collection.upsert(documents=docs, ids=ids)

    print(f"Built persistent Chroma collection {name} with {len(docs)} docs")
