from __future__ import annotations

from agentsec_preflight.models import CLAIM_CEILING


def test_claim_ceiling_blocks_overclaim_promotion():
    joined = " ".join(CLAIM_CEILING)
    assert "no_security_certification" in joined
    assert "no_product_readiness" in joined
    assert "no_external_action_authorization" in joined
