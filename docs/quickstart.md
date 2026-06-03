# Quickstart

Run locally from the standalone repo root after a local install:

```bash
python -m agentsec_preflight.cli --sample
python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
python -m agentsec_preflight.cli --report
```

No network, credentials, live runtime, live MCP/tool call, GitHub API, PyPI publish, or external action is required.

From a fresh clone without installing, use the source tree explicitly:

```bash
PYTHONPATH=src python -m agentsec_preflight.cli --sample
PYTHONPATH=src python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
PYTHONPATH=src python -m agentsec_preflight.cli --report
```

The root checkout shim also makes the shorter `python -m` form work from a clean checkout before installation.

## Interpret Decisions

- PASS: scoped discovery, read-only, or draft path only.
- HOLD: reason, safe next action, and repair path are required before action.
- BLOCK: stop the action and use the blocked action reason.

PASS does not mean security certification, product readiness, legal clearance, deployment approval, or action authorization.
