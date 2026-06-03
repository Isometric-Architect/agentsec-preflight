from __future__ import annotations

from agentsec_preflight.descriptor_examples import by_id
from agentsec_preflight.preflight_engine import preflight_descriptor


def test_engine_emits_pass_hold_block_and_no_match():
    assert preflight_descriptor(by_id("readonly_db_query"))["decision"].startswith("PASS")
    assert preflight_descriptor(by_id("email_send_missing_approval"))["decision"].startswith("HOLD")
    assert preflight_descriptor(by_id("github_merge_forbidden"))["decision"].startswith("BLOCK")
    assert preflight_descriptor(None)["no_match_guard_triggered"] is True
