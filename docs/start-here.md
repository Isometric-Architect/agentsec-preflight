# Start Here

AgentSec Preflight is a local CLI preview for PASS/HOLD/BLOCK reports before AI-agent tool calls.

## Quickest Local Run

```bash
PYTHONPATH=src python -m agentsec_preflight.cli --sample
PYTHONPATH=src python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
PYTHONPATH=src python -m agentsec_preflight.cli --report
```

No PyPI package has been published yet. Use the source tree or a local editable install.

## Where To Look

- `examples/` has synthetic tool descriptors.
- `examples/runtime_descriptors/` has OpenClaw-like, Hermes-like, and MCP-like synthetic runtime descriptors.
- `reports/` has sample PASS/HOLD/BLOCK/no-match reports.
- `receipts/` has sample run receipts.
- `docs/report_semantics.md` explains fields and decisions.
- `CLAIM_CEILING.md` states the public claim boundary.
- `SECURITY.md` explains vulnerability reporting.

## What Is Intentionally Not Included

- No GitHub Release has been published.
- No PyPI, MCP Registry, or Hugging Face package/listing has been published.
- No active GitHub workflow is installed.
- No live OpenClaw, Hermes, or MCP runtime integration is claimed.
- No external action is authorized by a PASS/HOLD/BLOCK report.

The root includes some governance and release-planning files for transparency. Start with README, this file, examples, reports, and report semantics before reading operator or decision notes.
