# OpenClaw Refocus Plan

## Why refocus

This repository started as an OpenClaw agent factory. Over time, it accumulated valuable support systems:

- documentation ingestion
- persistent retrieval
- troubleshooting memory
- routing / orchestration
- diagnostics

Those are still high-value, but they should support OpenClaw workspaces rather than become a separate runtime.

## Principle

The primary output of this repository should be complete OpenClaw-ready agent workspaces.

For each generated agent, the workspace should contain:

- `Dockerfile`
- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `TOOLS.md`
- `skills/`
- `scripts/`
- optional local docs/search helpers

All other code in this repository should be treated as build-time or support-time tooling for those workspaces.

## Keep and reposition

### Keep

- ingestion and persistent Chroma support
- self-learning troubleshooting case store
- routing ideas
- diagnostics modules

### Reposition

- `orchestrator/` becomes optional support tooling, not the main user experience
- memory becomes a capability that generated OpenClaw agents can use
- diagnostics become agent-specific scripts and/or skills

## Target repository structure

```text
openclaw-agent-factory/
  agents/                 # agent specs / catalog
  templates/
    base/                 # AGENTS/SOUL/TOOLS/IDENTITY/Dockerfile templates
    skills/               # reusable skill templates
    scripts/              # reusable script templates
    archetypes/           # infra / smart-home / support / media overlays
  generated/              # OpenClaw-ready workspaces
  support/
    ingest/               # indexing/build tooling
    memory/               # case storage / recall helpers
    routing/              # optional orchestration helpers
    diagnostics/          # shared diagnostics code or generators
  docs/
```

## OpenClaw-first design goals

### 1. Workspaces are the product

The main success criterion is:

> Does `generated/<agent>/` feel like a high-quality OpenClaw workspace?

### 2. Skills over sidecar orchestration

Whenever possible, behavior should live in OpenClaw-native files:

- `AGENTS.md`
- `TOOLS.md`
- `skills/*/SKILL.md`
- `scripts/*`

### 3. Ingestion is a workspace build step

Documentation ingestion should prepare data and helpers that the generated OpenClaw workspace uses.

### 4. Memory is agent memory

Troubleshooting memory should be available to the generated agent as a capability, not only through a standalone CLI.

## Slack orchestration vision

The routing idea is still valuable and can absolutely be pivoted toward OpenClaw model orchestration.

### Goal

A coordinating OpenClaw agent receives a user request in Slack, identifies which specialists are needed, and brings them together in a thread, group chat, or channel.

### Example

User asks in Slack:

> My Home Assistant container cannot reach my MQTT broker after I changed my Docker networking.

Coordinator behavior:

1. Detects this is multi-discipline
2. Invokes or summons:
   - Docker agent
   - Home Assistant agent
   - possibly Linux/Networking agent
3. Creates a shared troubleshooting thread / channel
4. Each specialist contributes findings
5. Coordinator synthesizes the answer back to the user

### Why this fits OpenClaw

This keeps the intelligence in OpenClaw agents rather than in an external Python-only orchestrator.

The repo should therefore support:

- specialist agent generation
- coordinator / orchestrator agent generation
- agent role descriptions and collaboration rules in `AGENTS.md` and skills
- support hooks for Slack-based group collaboration

## Proposed agent types

### Specialist agents

Examples:

- Docker
- Home Assistant
- AWS
- Debian
- Tailscale
- Plex

Responsibilities:

- domain expertise
- doc-grounded answers
- agent-specific troubleshooting skills
- memory recall for prior similar cases

### Coordinator agent

Responsibilities:

- triage incoming Slack requests
- determine whether a single specialist or multiple specialists are needed
- invite or invoke specialists
- maintain conversation state
- synthesize final answer

## What the coordinator needs

Generated workspace should include:

- routing heuristics or prompts
- collaboration skill
- thread / channel etiquette rules
- explicit delegation rules
- synthesis rules

Example coordinator rules:

- delegate when the problem spans more than one domain
- prefer specialists over general reasoning
- ask specialists for evidence, not just conclusions
- produce a final integrated answer with next steps

## Recommended next implementation steps

### Phase 1: OpenClaw workspace refactor

1. Move generic support systems under `support/`
2. Strengthen generated OpenClaw workspaces
3. Generate agent-specific skills and scripts into each workspace
4. Make Docker the gold-standard OpenClaw workspace
5. Repeat for Home Assistant and AWS

### Phase 2: OpenClaw-native memory and docs

1. Add generated skills for doc search
2. Add generated skills for memory recall
3. Add generated scripts for diagnostics
4. Make `TOOLS.md` and `AGENTS.md` require using those capabilities

### Phase 3: Coordinator agent

1. Add a `coordinator` agent spec
2. Generate OpenClaw workspace for coordinator
3. Add collaboration skill
4. Add routing / delegation heuristics
5. Define how specialists report back

### Phase 4: Slack orchestration

1. Define desired Slack interaction model
2. Map coordinator behavior to Slack threads / channels
3. Have coordinator summon specialists into a shared thread or channel
4. Coordinator synthesizes and replies to user

## Summary

Yes, the memory and ingestion improvements remain high-value.
Yes, the routing concept is still excellent.
And yes, the routing/orchestration concept can be pivoted toward OpenClaw model orchestration and Slack collaboration.

The right move is to make all of those capabilities support generated OpenClaw workspaces, with a coordinator agent as the collaboration hub.
