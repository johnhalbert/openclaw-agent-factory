import subprocess
import sys
import json

from orchestrator.orchestrator import handle


def run_search(collection, query):
    cmd = ["python", "tools/search_docs.py", collection, query]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def run_llm(question, docs):
    """Send retrieved docs + question to an LLM (Ollama if available)."""

    prompt = f"""
You are a technical assistant. Use the provided documentation excerpts to answer the question.

QUESTION:
{question}

DOCUMENTATION:
{docs}

INSTRUCTIONS:
- Base your answer on the documentation
- If the docs are incomplete, say so
- Provide a clear explanation and possible fix
"""

    cmd = ["ollama", "run", "mistral", prompt]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return "Ollama not installed or not in PATH."


def ask(question: str):
    agent, collection = handle(question)

    print(f"\n[Router] → {agent}")

    if not collection:
        print("No collection mapped. Cannot answer with docs.")
        return

    print(f"[Docs] → {collection}\n")

    docs = run_search(collection, question)

    if not docs.strip():
        print("No documentation found.")
        return

    print("--- Retrieved Documentation ---\n")
    print(docs)

    print("\n--- Reasoned Answer ---\n")

    answer = run_llm(question, docs)
    print(answer)


if __name__ == "__main__":
    q = " ".join(sys.argv[1:])
    ask(q)
