import subprocess
from pathlib import Path


def clone(url: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    name = url.split("/")[-1].replace(".git", "")
    target = out_dir / name

    if target.exists():
        return target

    subprocess.run(["git", "clone", "--depth", "1", url, str(target)], check=True)

    return target
