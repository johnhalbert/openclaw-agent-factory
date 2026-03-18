import argparse
from pathlib import Path
import chromadb


def search(collection_name: str, query: str, limit: int = 5):
    client = chromadb.Client()
    collection = client.get_or_create_collection(collection_name)

    results = collection.query(query_texts=[query], n_results=limit)

    docs = results.get("documents", [[]])[0]

    for i, doc in enumerate(docs, start=1):
        print(f"[{i}] {doc[:500]}\n")


def main():
    parser = argparse.ArgumentParser(description="Search ingested documentation")
    parser.add_argument("collection")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=5)

    args = parser.parse_args()

    search(args.collection, args.query, args.limit)


if __name__ == "__main__":
    main()
