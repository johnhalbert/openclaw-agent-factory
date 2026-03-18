import json
from pathlib import Path


def score_case(question: str, payload: dict) -> int:
    q_words = set(question.lower().split())
    case_words = set((payload.get("question") or "").lower().split())
    return len(q_words & case_words)


def retrieve_similar_cases(question: str, root: Path | None = None, limit: int = 3):
    root = root or Path("memory/cases")
    if not root.exists():
        return []

    scored = []
    for path in root.glob("*.json"):
        try:
            payload = json.loads(path.read_text())
        except Exception:
            continue
        scored.append((score_case(question, payload), path, payload))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[2] for item in scored[:limit] if item[0] > 0]
