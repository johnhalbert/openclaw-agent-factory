# OpenClaw Workspace Quickstart

This guide is the preferred path for generating OpenClaw-ready workspaces from this repository.

## Goal

Produce a generated agent workspace that contains:

- `Dockerfile`
- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `TOOLS.md`
- `skills/`
- `scripts/`

under:

```text
generated/<agent>/
```

## 1. Clone and install

```bash
git clone https://github.com/johnhalbert/openclaw-agent-factory
cd openclaw-agent-factory

python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 2. Build a Docker OpenClaw workspace

```bash
python factory/openclaw_workspace_builder.py agents/docker-openclaw.yaml
```

This should produce:

```text
generated/docker/
  Dockerfile
  AGENTS.md
  SOUL.md
  IDENTITY.md
  TOOLS.md
  skills/
  scripts/
```

## 3. Build a Coordinator OpenClaw workspace

```bash
python factory/openclaw_workspace_builder.py agents/coordinator-openclaw.yaml
```

This should produce:

```text
generated/coordinator/
  Dockerfile
  AGENTS.md
  SOUL.md
  IDENTITY.md
  TOOLS.md
  skills/
  scripts/
```

## 4. Current gold-standard workspaces

- `agents/docker-openclaw.yaml`
- `agents/coordinator-openclaw.yaml`

These are the current recommended examples for the OpenClaw-first direction.

## 5. What makes these OpenClaw-first

The generated workspaces contain OpenClaw-native artifacts, especially:

- `AGENTS.md` for operating rules
- `TOOLS.md` for tool usage expectations
- `skills/*/SKILL.md` for reusable behaviors
- `scripts/*` for local helper utilities

## 6. Recommended next pattern

Use the Docker workspace as the model for other specialist agents.
Use the Coordinator workspace as the model for multi-agent delegation and synthesis.

## 7. Notes

- Support tooling in this repo remains valuable, but the main product is the generated OpenClaw workspace.
- The long-term direction is Slack-based coordination through a coordinator agent plus specialists.
