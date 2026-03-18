# Quickstart

This guide shows the shortest happy path to:

1. create agent workspaces
2. ingest documentation
3. ask a grounded troubleshooting question with memory

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

## 2. Generate agent workspaces

Generate one agent:

```bash
python -m factory.cli generate agents/docker.yaml
```

Generate all catalog agents:

```bash
python factory/cli_generate_all.py
```

Generated workspaces will appear under:

```text
generated/
```

## 3. Ingest documentation

Build the Docker documentation collection:

```bash
python ingest/update_collections.py docker
```

Build the AWS documentation collection:

```bash
python ingest/update_collections.py aws
```

Build the Home Assistant documentation collection:

```bash
python ingest/update_collections.py home-assistant
```

## 4. Search docs directly

```bash
python tools/search_docs.py docker_docs "docker bind mount permissions"
python tools/search_docs.py aws_docs "IAM role trust policy"
python tools/search_docs.py home_assistant_docs "automation trigger"
```

## 5. Ask a grounded question

Basic routed retrieval:

```bash
python orchestrator/ask.py "why can't my docker container mount a volume"
```

Reasoning with Ollama:

```bash
python orchestrator/ask_reasoning.py "why can't my docker container mount a volume"
```

Reasoning + diagnostics + memory:

```bash
python orchestrator/ask_memory.py "why can't my docker container mount a volume"
```

## 6. What `ask_memory.py` does

For each question it will:

1. route to the best matching agent
2. select the mapped docs collection
3. retrieve matching docs
4. recall similar prior troubleshooting cases
5. run basic diagnostics for supported agents
6. send all of that to Ollama
7. save the new troubleshooting case under `memory/cases/`

## 7. Example happy path

```bash
# generate agents
python factory/cli_generate_all.py

# build Docker knowledge base
python ingest/update_collections.py docker

# ask a question with full reasoning and memory
python orchestrator/ask_memory.py "why can't my docker container mount a volume"
```

## 8. Notes

- The current reasoning CLI uses `ollama run mistral`.
- Diagnostics are currently most useful for Docker.
- Routing is currently simple keyword matching.
- Collections must exist before `ask.py`, `ask_reasoning.py`, or `ask_memory.py` can retrieve useful docs.
