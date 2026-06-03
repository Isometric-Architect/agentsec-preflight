# AgentSec Preflight

Local PASS/HOLD/BLOCK reports before AI-agent tool calls.

AgentSec Preflight helps agents and developers check a tool before action: permissions, side effects, missing fields, stale metadata, source traces, and receipt requirements.

Run it locally. No network required.

## 5-Minute Local Path

```bash
python -m agentsec_preflight.cli --sample
python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json
python -m agentsec_preflight.cli --report
```

## Checks

- missing auth or scope
- missing required fields
- stale or deprecated metadata
- missing docs, source trace, or policy
- external, destructive, public, deploy, payment, or contract actions
- unsafe claim promotion
- no-match fallback to pretrained memory

## Output

- PASS for scoped discovery/read-only/draft paths
- HOLD with reason, safe next action, and repair path
- BLOCK with reason and blocked action
- receipt context for what happened and what must not be claimed

## Runtime Fixture Pack

The standalone pack includes synthetic runtime fixtures for local testing:

- `policies/` has OpenClaw-like, Hermes-like, and MCP-like default route policies.
- `examples/runtime_descriptors/` has synthetic runtime descriptors.
- `examples/action_requests/` has request examples for PASS/HOLD/BLOCK/no-match cases.
- `examples/capability_cards/` has compact capability cards.
- `reports/sample_agent_security_review.md` shows a concise review-style report.
- `canaries/runtime_basic_20.jsonl` contains public family-level negative controls.

These fixtures are not real OpenClaw, Hermes, or MCP integrations.

## Scope

AgentSec Preflight produces local preflight reports. Final deployment, security review, legal review, and action authorization stay with your team and approval workflow.

## Relationship

This repository is the standalone public AgentSec Preflight repo extracted from the private AOI / ResidualOps ecosystem master repo. The private AOI repo remains the internal ecosystem workspace; this repo contains the public-safe local CLI wedge.

## Start Here

- `src/agentsec_preflight/` contains the local CLI and report builder.
- The root checkout shim lets `python -m agentsec_preflight.cli ...` work before installation.
- `examples/` contains local synthetic descriptors.
- `reports/` contains sample PASS/HOLD/BLOCK/no-match reports.
- `docs/quickstart.md` gives the developer path.
- `docs/report_semantics.md` explains report fields.
- `CLAIM_CEILING.md` states the public claim boundary.
- `SECURITY.md` explains how to report vulnerabilities without public exploit details.
- `CONTRIBUTING.md` gives lightweight contribution rules for synthetic examples and scoped reports.
- `CODE_OF_CONDUCT.md` sets concise community behavior expectations.

## License

This standalone public repo is prepared under Apache-2.0.

No GitHub release, PyPI package, MCP Registry listing, Hugging Face upload, DNS change, site deployment, OpenClaw/Hermes install, live runtime execution, live MCP/tool call, or external action is performed by this pack.
