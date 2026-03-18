import subprocess
import sys

from memory.learn import recall, learn_from_run
from orchestrator.router_better import route_question
from orchestrator.troubleshooter_docker_plus import troubleshoot


COLLECTIONS = {
    "docker": "docker_docs",
    "home-assistant": "home_assistant_docs",
    "aws": "aws_docs",
}


def run_search(collection: str, query: str) -> str:
    cmd = ["python", "tools/search_docs_persistent.py", collection, query]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def run_llm(question: str, docs: str, prior_cases: list, findings: dict) -> str:
    cases_text = "\n\n".join(
        [
            f"Case {idx + 1}:\nQuestion: {case.get('question', '')}\nAnswer: {case.get('answer', '')}"
            for idx, case in enumerate(prior_cases)
        ]
    )

    prompt = f"""
You are a technical troubleshooting assistant.
Use the provided documentation excerpts, prior similar cases, and diagnostic findings to answer the question.

QUESTION:
{question}

DOCUMENTATION:
{docs}

PRIOR CASES:
{cases_text if cases_text else 'None'}

DIAGNOSTIC FINDINGS:
{findings}

INSTRUCTIONS:
- Base your answer primarily on the documentation
- Use prior cases only as supporting evidence
- Use diagnostic findings to narrow the likely cause
- If the docs are incomplete, say so
- Give the most likely cause first
- Provide concrete next steps
"""

    cmd = ["ollama", "run", "mistral", prompt]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip() or "No response from Ollama."
    except FileNotFoundError:
        return "Ollama not installed or not in PATH."


def ask(question: str):
    agent = route_question(question)
    collection = COLLECTIONS.get(agent)

    print(f"\n[Router] -> {agent}")

    docs = ""
    if collection:
        print(f"[Docs] -> {collection}")
        docs = run_search(collection, question)
    else:
        print("[Docs] -> none")

    prior_cases = recall(question, limit=3)
    print(f"[Memory] -> {len(prior_cases)} similar case(s)")

    findings = troubleshoot(agent)
    print(f"[Diagnostics] -> collected for {agent}")

    print("\n--- Retrieved Documentation ---\n")
    print(docs if docs.strip() else "No documentation found.\n")

    if prior_cases:
        print("--- Similar Prior Cases ---\n")
        for idx, case in enumerate(prior_cases, start=1):
            print(f"[{idx}] {case.get('question', '')}")
            print(f"    answer: {case.get('answer', '')}\n")

    print("--- Diagnostic Findings ---\n")
    print(findings)

    print("\n--- Reasoned Answer ---\n")
    answer = run_llm(question, docs, prior_cases, findings)
    print(answer)

    saved = learn_from_run(agent, question, findings, answer)
    print(f"\n[Memory] saved case -> {saved}")


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]).strip()
    if not q:
        raise SystemExit("Usage: python orchestrator/ask_memory_hardened.py \"your question\"")
    ask(q)
