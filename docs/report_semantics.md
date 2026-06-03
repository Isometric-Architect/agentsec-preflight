# Report Semantics

AgentSec Preflight reports use PASS/HOLD/BLOCK to avoid wasting the next tool-call turn before action.

## Fields

- `decision`: PASS, HOLD, or BLOCK route.
- `reason_codes`: local explanation for the route.
- `safe_next_action`: what to do next without external side effects.
- `repair_path`: how to fix a HOLD when possible.
- `blocked_next_action`: what must not be done after a BLOCK.
- `run_receipt_stub`: records that no action was taken by local preflight.
- `claim_ceiling`: what the report must not be promoted into.

The report is local metadata review only. It is not a live probe, runtime guarantee, deployment approval, or action authorization.
