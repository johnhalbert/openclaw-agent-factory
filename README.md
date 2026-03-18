# openclaw-agent-factory

Agent factory for building specialized OpenClaw agents with consistent templates, tooling, and local RAG ingestion.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .

python -m factory.cli generate agents/docker.yaml
```

## Structure

- factory/        Generator code
- templates/      Base templates
- agents/         Agent specs
- ingest/         RAG ingestion
- generated/      Output agents
