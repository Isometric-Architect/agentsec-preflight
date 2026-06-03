# No Active CI Decision

Decision: `HOLD_ACTIVE_CI_DECISION`

Active GitHub Actions workflows are intentionally not included in the first standalone repo pack.

Developers can run local tests manually:

python -m pytest

CI activation requires later explicit approval. This pack does not install `.github/workflows/`, does not trigger GitHub Actions, and does not add an active automation surface.
