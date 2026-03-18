import subprocess
import sys

from orchestrator.orchestrator import handle


def run_search(collection, query):
    cmd = [
        "python",
        "tools/search_docs.py",
        collection,
        query
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def ask(question: str):
    agent, collection = handle(question)

    print(f"\n[Router] → {agent}")

    if not collection:
        print("No collection mapped. Cannot answer with docs.")
        return

    print(f"[Docs] → {collection}\n")

    docs = run_search(collection, question)

    if not docs.strip():
        print("No documentation found.\n")
        return

    print("--- Retrieved Documentation ---\n")
    print(docs)


if __name__ == "__main__":
    q = " ".join(sys.argv[1:])
    ask(q)
