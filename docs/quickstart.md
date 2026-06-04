# Quickstart

Run locally from a clean checkout with the root shim:

```bash
python -m agentsec_preflight.cli --sample
python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
python -m agentsec_preflight.cli --report
```

No network, credentials, live runtime, live MCP/tool call, GitHub API, PyPI publish, or external action is required.

Canonical clone-without-install path:

```bash
git clone https://github.com/Isometric-Architect/agentsec-preflight.git
cd agentsec-preflight
PYTHONPATH=src python -m agentsec_preflight.cli --sample
PYTHONPATH=src python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
PYTHONPATH=src python -m agentsec_preflight.cli --report
```

Optional local editable install:

```bash
python -m pip install -e .
agentsec-preflight --sample
agentsec-preflight --preflight examples/email_send_missing_approval.json
agentsec-preflight --report
```

No PyPI package has been published yet.

## Interpret Decisions

- PASS: scoped discovery/read-only/draft-only path.
- HOLD: reason, safe next action, and repair path.
- BLOCK: reason and blocked action.
- Receipt: what happened, what did not happen, and what must not be claimed.

PASS does not mean security certification, product readiness, legal clearance, deployment approval, or action authorization.
