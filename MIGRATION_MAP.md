# Migration Map

This map records the public-safe subset selected for a future `agentsec-preflight` standalone repo.

## Source To Standalone

- `src/ai_objective_index/agentsec_preflight/` -> `src/agentsec_preflight/`
- `agentsec_preflight/SampleAgentToolDescriptors_v0.1.json` -> `examples/`
- `agentsec_preflight/AgentSecPreflightReports_v0.1.json` -> `reports/`
- `agentsec_preflight/AgentSecPreflightReceiptSamples_v0.1.json` -> `reports/`
- `agentsec_preflight/AgentSecPreflightDeveloperQuickstart_v0.1.md` -> `docs/quickstart.md`
- `agentsec_preflight/AgentSecPreflightClaimCeiling_v0.1.md` -> `CLAIM_CEILING.md`

## Excluded

- private ranking weights
- hidden canaries
- private negative controls
- scorer calibration
- provider priors
- commercial routing policy
- customer data
- real feedback memory
- private strategy
- unrelated generated artifacts
- full internal AOI history ledgers
- flake-hardening receipts except the high-level provenance noted here

## Current Parity

The standalone pack uses a compact fixture-compatible implementation, not a full source-level mirror of the private AOI ecosystem repo. Keep parity checks manual until a future standalone repo creation package is explicitly approved.
