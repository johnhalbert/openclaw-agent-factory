# Quickstart (Hardened Path)

This guide uses the more reliable persistent-storage path for local testing.

## Prerequisites

- Python 3.11+
- `git`
- `ollama` installed and in `PATH`
- a local Ollama model available, currently `mistral`

## 1. Clone and install

```bash
git clone https://github.com/johnhalbert/openclaw-agent-factory
cd openclaw-agent-factory

python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 2. Generate agents

```bash
python factory/cli_generate_all.py
```

## 3. Build persistent documentation collections

Docker:

```bash
python ingest/update_collections_persistent.py docker
```

AWS:

```bash
python ingest/update_collections_persistent.py aws
```

Home Assistant:

```bash
python ingest/update_collections_persistent.py home-assistant
```

By default collections are stored under:

```text
.local/chroma
```

You can override that with:

```bash
export OPENCLAW_CHROMA_PATH=/path/to/chroma
```

## 4. Search persistent docs directly

```bash
python tools/search_docs_persistent.py docker_docs "docker bind mount permissions"
python tools/search_docs_persistent.py aws_docs "IAM role trust policy"
python tools/search_docs_persistent.py home_assistant_docs "automation trigger"
```

## 5. Ask with the hardened entrypoint

```bash
python orchestrator/ask_memory_hardened.py "why can't my docker container mount a volume"
```

This path uses:

1. improved routing
2. persistent doc search
3. prior case recall
4. stronger Docker diagnostics
5. Ollama reasoning
6. automatic case saving

## 6. Recommended first real test

```bash
python factory/cli_generate_all.py
python ingest/update_collections_persistent.py docker
python orchestrator/ask_memory_hardened.py "why can't my docker container mount a volume"
```

## 7. Notes

- This is currently strongest for Docker.
- Diagnostics for other agents are still minimal.
- Routing is improved but still keyword-based.
- `ollama run mistral` must work locally.
