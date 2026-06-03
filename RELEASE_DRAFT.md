# AgentSec Preflight preview: local PASS/HOLD/BLOCK reports before tool calls

AgentSec Preflight is a local, no-network CLI preview for checking AI-agent tool calls before action. It helps agents and developers inspect permissions, side effects, missing fields, stale metadata, source traces, and receipt requirements before wasting a tool call or creating unintended side effects.

## Who This Is For

- AI-agent developers
- MCP/tool maintainers
- developers experimenting with agent toolchains
- reviewers who want local PASS/HOLD/BLOCK reports before action

## Try It Locally

python -m agentsec_preflight.cli --sample
python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
python -m agentsec_preflight.cli --report

## Scope

AgentSec Preflight produces local preflight reports. Final deployment, security review, legal review, and action authorization stay with your team and approval workflow.

## Publish Status

This is a local release draft only. No GitHub release has been published, no tag has been created, no asset has been uploaded, no PyPI package has been published, and no separate repo has been created.
