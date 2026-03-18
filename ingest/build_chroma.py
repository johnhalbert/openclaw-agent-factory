import chromadb
from pathlib import Path


def build_collection(name: str, chunks):
    client = chromadb.Client()
    collection = client.get_or_create_collection(name)

    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], ids=[str(i)])

    print(f"Built Chroma collection {name} with {len(chunks)} docs")
