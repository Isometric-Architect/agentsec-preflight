# Contributing

Thanks for helping improve AgentSec Preflight.

Useful contribution types include:

- bug reports
- documentation improvements
- synthetic descriptors
- sample PASS/HOLD/BLOCK reports
- policy examples
- test fixtures

## Contribution Rules

- Do not include real credentials, tokens, private keys, customer data, or private runtime logs.
- Do not add copied proprietary descriptors or private negative-control bodies.
- Do not claim live OpenClaw, Hermes, or MCP integration support.
- Do not claim security certification, product readiness, legal clearance, market validation, deployment approval, or action authorization.
- Every new example should include a `claim_ceiling` and `must_not_claim` boundary.
- Keep examples synthetic unless a future approved package explicitly adds verified public data.
- Tests should pass locally before a change is proposed.

## PR Checklist

- Examples are synthetic and scoped.
- Reports are local preflight reports, not readiness or approval claims.
- Receipts mark `action_taken=false` unless a local dry-run test explicitly defines a different no-external-action meaning.
- No private negative-control seeds or hidden canary bodies are included.
- No tokens, credentials, or active workflows are added.
