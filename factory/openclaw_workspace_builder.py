from pathlib import Path
import shutil
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined


class OpenClawWorkspaceBuilder:
    def __init__(self, root: Path):
        self.root = root
        self.template_root = root / "templates" / "base"
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_root)),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def build(self, spec_path: Path) -> Path:
        spec = yaml.safe_load(spec_path.read_text())
        agent_id = spec["agent_id"]
        profile = spec["profile"]
        out = self.root / "generated" / agent_id
        out.mkdir(parents=True, exist_ok=True)

        context = {
            "agent_id": agent_id,
            "display_name": profile["display_name"],
            "role": profile["role"],
            "domain": profile["domain"],
            "primary_mode": profile["primary_mode"],
            "scope": profile["scope"],
            "non_goals": profile["non_goals"],
            "skills": spec.get("skills", []),
            "scripts": spec.get("scripts", []),
            "sources": spec.get("sources", {}),
        }

        self._render("Dockerfile.j2", out / "Dockerfile", context)
        self._render("IDENTITY.md.j2", out / "IDENTITY.md", context)
        self._render("AGENTS.md.j2", out / "AGENTS.md", context)
        self._render("SOUL.md.j2", out / "SOUL.md", context)

        tools_template = "TOOLS_DOC_AWARE.md.j2" if (self.template_root / "TOOLS_DOC_AWARE.md.j2").exists() else "TOOLS.md.j2"
        self._render(tools_template, out / "TOOLS.md", context)

        skills_dir = out / "skills"
        scripts_dir = out / "scripts"
        skills_dir.mkdir(exist_ok=True)
        scripts_dir.mkdir(exist_ok=True)

        for skill_name in spec.get("skills", []):
            src = self.template_root / "skills" / skill_name / "SKILL.md.j2"
            if src.exists():
                rendered = self.env.get_template(f"skills/{skill_name}/SKILL.md.j2").render(**context)
                target_dir = skills_dir / skill_name
                target_dir.mkdir(parents=True, exist_ok=True)
                (target_dir / "SKILL.md").write_text(rendered)

        for script_name in spec.get("scripts", []):
            src = self.template_root / "scripts" / f"{script_name}.j2"
            if src.exists():
                target = scripts_dir / script_name
                target.write_text(src.read_text())
                target.chmod(0o755)

        return out

    def _render(self, template_name: str, out_path: Path, context: dict):
        template = self.env.get_template(template_name)
        out_path.write_text(template.render(**context))


if __name__ == "__main__":
    import sys
    root = Path.cwd()
    builder = OpenClawWorkspaceBuilder(root)
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python factory/openclaw_workspace_builder.py <spec-path>")
    output = builder.build(Path(sys.argv[1]))
    print(f"Built OpenClaw workspace: {output}")
