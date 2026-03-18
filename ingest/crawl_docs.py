import requests
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin


def crawl(start_url: str, out_dir: Path, limit: int = 50):
    out_dir.mkdir(parents=True, exist_ok=True)

    visited = set()
    queue = [start_url]

    while queue and len(visited) < limit:
        url = queue.pop(0)

        if url in visited:
            continue

        visited.add(url)

        try:
            r = requests.get(url, timeout=20)
            r.raise_for_status()
        except Exception:
            continue

        filename = url.replace("https://", "").replace("/", "_")
        (out_dir / f"{filename}.html").write_text(r.text)

        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.select("a[href]"):
            link = urljoin(url, a["href"])
            if link.startswith(start_url) and link not in visited:
                queue.append(link)
