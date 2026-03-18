from pathlib import Path
from memory.case_store import CaseStore
from memory.retrieve_cases import retrieve_similar_cases


def learn_from_run(agent: str, question: str, findings: dict, answer: str):
    store = CaseStore()
    return store.save_case(agent, question, findings, answer)


def recall(question: str, limit: int = 3):
    return retrieve_similar_cases(question, Path("memory/cases"), limit=limit)
