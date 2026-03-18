import json
from pathlib import Path
from datetime import datetime


class CaseStore:
    def __init__(self, root: Path | None = None):
        self.root = root or Path("memory/cases")
        self.root.mkdir(parents=True, exist_ok=True)

    def save_case(self, agent: str, question: str, findings: dict, answer: str) -> Path:
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        safe_agent = agent.replace("/", "-")
        path = self.root / f"{timestamp}_{safe_agent}.json"
        payload = {
            "timestamp": timestamp,
            "agent": agent,
            "question": question,
            "findings": findings,
            "answer": answer,
        }
        path.write_text(json.dumps(payload, indent=2))
        return path

    def list_cases(self):
        return sorted(self.root.glob("*.json"))
