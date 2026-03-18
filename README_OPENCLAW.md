# openclaw-agent-factory

OpenClaw-first agent factory for generating specialist and coordinator workspaces.

The primary product of this repository is a generated OpenClaw-ready workspace under:

```text
generated/<agent>/
```

Each generated workspace is intended to contain:

- `Dockerfile`
- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `TOOLS.md`
- `skills/`
- `scripts/`

## Recommended OpenClaw Path

### Build a specialist workspace

Docker specialist:

```bash
python factory/openclaw_workspace_builder.py agents/docker-openclaw-tools.yaml
```

Home Assistant specialist:

```bash
python factory/openclaw_workspace_builder.py agents/home-assistant-openclaw-tools.yaml
```

### Build a coordinator workspace

Slack-oriented coordinator:

```bash
python factory/openclaw_workspace_builder.py agents/coordinator-openclaw-slack.yaml
```

## Current recommended specs

### Specialist workspaces

- `agents/docker-openclaw-tools.yaml`
- `agents/home-assistant-openclaw-tools.yaml`

### Coordinator workspace

- `agents/coordinator-openclaw-slack.yaml`

## Generated output locations

After building, inspect:

```text
generated/docker/
generated/home-assistant/
generated/coordinator/
```

## Supporting docs

Start here next:

- `docs/OPENCLAW_RECOMMENDED_PATH.md`
- `docs/OPENCLAW_WORKSPACE_QUICKSTART.md`
- `docs/SLACK_COORDINATION_DESIGN.md`
- `docs/OPENCLAW_REFOCUS.md`

## What this repo is not centered on

The Python orchestration, memory, ingestion, and diagnostics code in this repository is still valuable, but it is support tooling behind the generated OpenClaw workspaces.

The main path is:

1. choose an OpenClaw spec
2. build the workspace
3. use that workspace in OpenClaw

## Recommended first run

```bash
python factory/openclaw_workspace_builder.py agents/docker-openclaw-tools.yaml
python factory/openclaw_workspace_builder.py agents/coordinator-openclaw-slack.yaml
```

Then inspect:

```text
generated/docker/
generated/coordinator/
```

## Direction

This repository is being steered back toward its original purpose:

> generate high-quality OpenClaw specialist and coordinator workspaces,
> while keeping ingestion, memory, routing, and diagnostics as supporting capabilities behind those workspaces.
