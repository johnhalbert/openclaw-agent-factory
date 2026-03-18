from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader


class DocAwareGenerator:
    def __init__(self, root):
        self.root = root
        self.env = Environment(loader=FileSystemLoader(root / "templates" / "base"))

    def generate(self, spec_path):
        spec = yaml.safe_load(open(spec_path))

        agent_id = spec["agent_id"]
        profile = spec["profile"]

        out = self.root / "generated" / agent_id
        out.mkdir(parents=True, exist_ok=True)

        ctx = {
            "agent_id": agent_id,
            **profile
        }

        files = {
            "Dockerfile": "Dockerfile.j2",
            "IDENTITY.md": "IDENTITY.md.j2",
            "AGENTS.md": "AGENTS.md.j2",
            "SOUL.md": "SOUL.md.j2",
            "TOOLS.md": "TOOLS_DOC_AWARE.md.j2",
        }

        for out_name, tpl_name in files.items():
            tpl = self.env.get_template(tpl_name)
            (out / out_name).write_text(tpl.render(**ctx))

        return out
