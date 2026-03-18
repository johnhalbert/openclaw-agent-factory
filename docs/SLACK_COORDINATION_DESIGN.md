# Slack Coordination Design

## Goal

Define how an OpenClaw coordinator agent should work with specialist agents in Slack.

This document is intended to make the coordinator behavior explicit, testable, and understandable.

## User experience goal

A user asks for help in Slack.

The coordinator agent should:

1. understand the request
2. decide whether one specialist or multiple specialists are needed
3. involve those specialists in a thread or collaboration channel
4. gather evidence-backed findings
5. synthesize one final answer for the user

## Primary interaction model

### Preferred model: one user thread, many specialists behind it

1. User asks in a Slack channel or DM thread
2. Coordinator replies in that thread
3. Coordinator determines which specialists are needed
4. Specialists contribute findings in the same thread or in a linked coordination thread/channel
5. Coordinator posts the integrated summary in the original thread

This keeps the user experience coherent.

## When to use one specialist

Use one specialist when the issue is clearly bounded to one domain.

Examples:
- Docker bind mount permissions
- AWS IAM trust policy syntax
- Home Assistant automation trigger issue with no infra symptoms

## When to use multiple specialists

Use multiple specialists when the issue crosses boundaries.

Examples:
- Home Assistant container cannot reach MQTT broker after Docker network change
- Plex media path issue caused by host filesystem permissions
- Tailscale connectivity problem affecting self-hosted services in containers

## Example specialist combinations

- Docker + Home Assistant
- Docker + Debian
- Home Assistant + Networking
- Docker + Tailscale
- Debian + Omada

## Coordinator responsibilities

The coordinator should:

- triage the request
- identify domains involved
- summon the right specialists
- keep each specialist focused on its domain
- ask specialists for evidence, not just conclusions
- synthesize the final answer
- preserve a clean user-facing thread

The coordinator should not:

- pretend to be the deepest specialist when a domain expert is available
- let multiple specialists produce fragmented user-facing replies without synthesis
- lose track of the original user question

## Specialist responsibilities

A specialist should:

- stay within its domain
- provide evidence-backed findings
- name relevant docs, diagnostics, or prior cases
- clearly mark uncertainty
- avoid overreaching into another specialist's domain unless explicitly asked

## Suggested thread behavior

### In-thread collaboration

Best when the problem is understandable by humans following along.

Advantages:
- transparent
- easy to audit
- easy for user to see progress

Disadvantages:
- can get noisy if too many specialists participate directly

### Linked coordination thread or channel

Best when multiple specialists need to work without overwhelming the user.

Pattern:
- coordinator acknowledges user in original thread
- coordinator opens or uses a linked coordination thread/channel
- specialists work there
- coordinator returns a concise synthesis to the original thread

## Evidence model

Specialists should contribute evidence from:

- official documentation
- local diagnostics
- prior similar cases
- configuration or logs provided by the user

Priority order:
1. current docs and direct diagnostics
2. user-provided config/log evidence
3. prior cases
4. general knowledge

## Message pattern

### Coordinator opening reply

- acknowledge scope
- say which specialists are being involved
- set expectation that a synthesized answer will follow

### Specialist reply pattern

- domain-specific finding
- supporting evidence
- uncertainty if any
- suggested next step or verification step

### Coordinator final reply

- most likely root cause
- what evidence supports it
- concrete next steps
- note any unresolved uncertainty

## Example flow

User says:

> My Home Assistant container cannot reach my MQTT broker after I changed my Docker networking.

Coordinator:
- identifies Docker + Home Assistant
- asks Docker specialist to inspect container/network boundary
- asks Home Assistant specialist to inspect integration/config side

Docker specialist finds:
- HA container not attached to expected network

Home Assistant specialist finds:
- MQTT integration is configured for broker hostname that depends on Docker network resolution

Coordinator final synthesis:
- root cause is likely Docker network attachment / name resolution
- explains why
- provides step-by-step fix

## What the repo should support

To make this real, generated OpenClaw workspaces should include:

### Coordinator workspace
- collaboration triage skill
- coordinator collaboration skill
- Slack coordination rules skill
- evidence synthesis skill
- memory recall skill

### Specialist workspaces
- domain triage skill
- official doc triage skill
- memory recall skill
- domain helper scripts where useful

## Future implementation ideas

- explicit specialist roster for the coordinator
- delegation templates in `AGENTS.md`
- Slack-specific response formatting conventions
- coordinator memory of prior multi-agent incidents
- automated specialist mention / invocation hooks if OpenClaw supports them

## Summary

The best Slack orchestration model is:

- user asks once
- coordinator triages and delegates
- specialists gather evidence
- coordinator synthesizes one final answer

This preserves a clean user experience while still benefiting from specialist depth.
