# Quickstart

Run locally from the future standalone repo root:

python -m agentsec_preflight.cli --sample
python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
python -m agentsec_preflight.cli --report

No network, credentials, live runtime, live MCP/tool call, GitHub API, PyPI publish, or external action is required.

## Interpret Decisions

- PASS: scoped discovery, read-only, or draft path only.
- HOLD: reason, safe next action, and repair path are required before action.
- BLOCK: stop the action and use the blocked action reason.

PASS does not mean security certification, product readiness, legal clearance, deployment approval, or action authorization.
