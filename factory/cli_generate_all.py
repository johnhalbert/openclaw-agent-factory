from pathlib import Path
import yaml

from factory.generator import AgentGenerator


def generate_all():
    root = Path.cwd()
    generator = AgentGenerator(root)

    catalog_path = root / "agents" / "catalog.yaml"
    catalog = yaml.safe_load(catalog_path.read_text())

    agents = catalog.get("agents", {})

    for agent_id, archetype in agents.items():
        spec_path = root / "agents" / f"{agent_id}.yaml"

        if not spec_path.exists():
            spec_path.write_text(f"""agent_id: {agent_id}
archetype: {archetype}
profile:
  display_name: {agent_id.replace('-', ' ').title()}
  role: Specialist
  domain: {agent_id}
  primary_mode: Technical
  scope: Auto-generated agent
  non_goals: Do not assume unknown state
""")

        out = generator.generate(spec_path)
        print(f"Generated: {out}")


if __name__ == "__main__":
    generate_all()
