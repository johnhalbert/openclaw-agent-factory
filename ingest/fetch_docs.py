import requests
from pathlib import Path


def fetch(url: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = url.split("/")[-1] or "index.html"
    target = out_dir / filename

    r = requests.get(url, timeout=30)
    r.raise_for_status()

    target.write_bytes(r.content)
    print(f"Fetched {url} -> {target}")
