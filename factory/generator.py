import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class AgentGenerator:
    def __init__(self, root):
        self.root = root
        self.env = Environment(loader=FileSystemLoader(root / "templates" / "base"))

    def generate(self, spec_path):
        spec = yaml.safe_load(open(spec_path))
        out = self.root / "generated" / spec["agent_id"]
        out.mkdir(parents=True, exist_ok=True)

        ctx = {
            "agent_id": spec["agent_id"],
            **spec["profile"]
        }

        for f in ["Dockerfile","IDENTITY.md","AGENTS.md","SOUL.md","TOOLS.md"]:
            tpl = self.env.get_template(f + ".j2")
            open(out / f, "w").write(tpl.render(**ctx))

        return out
