from __future__ import annotations

"""Build local preflight reports and receipts without external calls."""

from datetime import UTC, datetime
from typing import Any

from .descriptor_examples import by_id
from .models import CLAIM_CEILING, MUST_NOT_CLAIM
from .preflight_engine import preflight_descriptor


REPORT_SCHEMA = "AgentSecPreflightReport/v0.1"
RECEIPT_SCHEMA = "AgentSecPreflightReceipt/v0.1"
RECEIPT_MODE = "local_no_network"


def build_report(descriptor: dict[str, Any] | None) -> dict[str, Any]:
    preflight = preflight_descriptor(descriptor)
    descriptor_id = descriptor["descriptor_id"] if descriptor else "NO_MATCH"
    return {
        "schema": REPORT_SCHEMA,
        "report_id": f"report_{descriptor_id}",
        "descriptor_id": descriptor_id,
        **preflight,
        "run_receipt_stub": {
            "action_taken": False,
            "external_action_performed": False,
            "live_probe_performed": False,
            "external_api_called": False,
        },
        "action_authorization": False,
        "security_certification": False,
        "product_readiness": False,
        "must_not_claim": MUST_NOT_CLAIM,
    }


def build_receipt(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": RECEIPT_SCHEMA,
        "receipt_id": f"receipt_{report['descriptor_id']}",
        "input_descriptor_ref": report["descriptor_id"],
        "preflight_decision": report["decision"],
        "action_taken": False,
        "action_not_taken": report.get("blocked_next_action") or "No external action performed by local preflight.",
        "external_action_performed": False,
        "live_probe_performed": False,
        "external_api_called": False,
        "reason_codes": report["reason_codes"],
        "safe_next_action": report["safe_next_action"],
        "claim_ceiling": CLAIM_CEILING,
        "must_not_claim": MUST_NOT_CLAIM,
        "generated_at": datetime.now(UTC).isoformat(),
    }


def sample_reports() -> list[dict[str, Any]]:
    ids = [
        "email_draft_tool",
        "email_send_missing_approval",
        "github_merge_forbidden",
        None,
    ]
    return [build_report(by_id(item) if item else None) for item in ids]
