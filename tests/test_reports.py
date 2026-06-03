from __future__ import annotations

from agentsec_preflight.descriptor_examples import by_id
from agentsec_preflight.report_builder import build_receipt, build_report


def test_report_and_receipt_do_not_authorize_action():
    report = build_report(by_id("email_send_missing_approval"))
    receipt = build_receipt(report)
    assert report["action_authorization"] is False
    assert report["security_certification"] is False
    assert receipt["action_taken"] is False
    assert receipt["external_action_performed"] is False
