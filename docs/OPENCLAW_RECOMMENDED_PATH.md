# Recommended OpenClaw Path

This is the single recommended front door for using this repository as an OpenClaw agent factory.

## What this repo is for

The primary product of this repository is:

```text
generated/<agent>/
```

Each generated workspace should be OpenClaw-ready and contain:

- `Dockerfile`
- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `TOOLS.md`
- `skills/`
- `scripts/`

## Use this path first

### 1. Build an OpenClaw specialist workspace

Docker specialist:

```bash
python factory/openclaw_workspace_builder.py agents/docker-openclaw-tools.yaml
```

Home Assistant specialist:

```bash
python factory/openclaw_workspace_builder.py agents/home-assistant-openclaw-tools.yaml
```

### 2. Build an OpenClaw coordinator workspace

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

These are the current best examples of the OpenClaw-first direction.

## Generated output locations

After building, look under:

```text
generated/docker/
generated/home-assistant/
generated/coordinator/
```

## Supporting docs to read next

### OpenClaw workspace builder path

Read:

```text
docs/OPENCLAW_WORKSPACE_QUICKSTART.md
```

### Slack coordination behavior

Read:

```text
docs/SLACK_COORDINATION_DESIGN.md
```

### Refocus rationale

Read:

```text
docs/OPENCLAW_REFOCUS.md
```

## Current direction in one sentence

This repository should generate high-quality OpenClaw specialist and coordinator workspaces, while keeping ingestion, memory, routing, and diagnostics as supporting capabilities behind those workspaces.

## What not to treat as the main path

The Python orchestration and memory tooling in the repository is still valuable, but it is not the primary user-facing path.

The primary path is:

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

## Summary

If you are unsure where to start, start here:

- build Docker specialist workspace
- build Slack-oriented Coordinator workspace
- read the Slack coordination design

That is the clearest current OpenClaw-first path through the repository.
