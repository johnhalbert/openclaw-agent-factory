from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class AgentProfile:
    display_name: str
    role: str
    domain: str
    primary_mode: str
    scope: str
    non_goals: str

@dataclass
class AgentSpec:
    agent_id: str
    archetype: str
    profile: AgentProfile
    packages: Dict[str, List[str]] = field(default_factory=dict)
    skills: List[str] = field(default_factory=list)
    scripts: List[str] = field(default_factory=list)
    sources: Dict[str, List[str]] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]):
        return cls(
            agent_id=raw["agent_id"],
            archetype=raw["archetype"],
            profile=AgentProfile(**raw["profile"]),
            packages=raw.get("packages", {}),
            skills=raw.get("skills", []),
            scripts=raw.get("scripts", []),
            sources=raw.get("sources", {}),
        )
