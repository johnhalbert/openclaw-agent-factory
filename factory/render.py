from pathlib import Path
from jinja2 import Environment, FileSystemLoader, StrictUndefined


def build_environment(template_root: Path) -> Environment:
    """Create a Jinja environment for rendering templates."""
    return Environment(
        loader=FileSystemLoader(str(template_root)),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
