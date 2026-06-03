from __future__ import annotations

"""Small validation helpers and public claim ceilings."""

from typing import Any


DESCRIPTOR_REQUIRED_FIELDS = [
    "descriptor_id",
    "name",
    "tool_type",
    "source_trace_count",
    "docs_url_present",
    "input_schema_present",
    "required_fields_present",
    "auth_scope_present",
    "approval_required",
    "external_action",
    "destructive_action",
    "public_post_action",
    "deprecated_signal",
    "claim_overreach_terms",
]

REPORT_REQUIRED_FIELDS = [
    "report_id",
    "decision",
    "reason_codes",
    "safe_next_action",
    "claim_ceiling",
]

RECEIPT_REQUIRED_FIELDS = [
    "receipt_id",
    "preflight_decision",
    "action_taken",
    "external_action_performed",
    "claim_ceiling",
]

CLAIM_CEILING = [
    "standalone_extraction_pack_only",
    "no_external_repo_creation",
    "no_release_publish",
    "no_live_probe",
    "no_live_runtime_integration",
    "no_product_readiness",
    "no_security_certification",
    "no_legal_privacy_compliance_clearance",
    "no_market_validation",
    "no_external_action_authorization",
]

MUST_NOT_CLAIM = [
    "PASS is not security certification.",
    "PASS is not product readiness.",
    "PASS is not legal clearance.",
    "PASS is not action authorization.",
    "No-match is not proof that no tool exists globally.",
    "Negative-cache examples are not final truth.",
]


def _missing_fields(payload: dict[str, Any], fields: list[str]) -> list[str]:
    return [f"missing_{field}" for field in fields if field not in payload]


def validate_descriptor(descriptor: dict[str, Any]) -> list[str]:
    return _missing_fields(descriptor, DESCRIPTOR_REQUIRED_FIELDS)


def validate_report(report: dict[str, Any]) -> list[str]:
    return _missing_fields(report, REPORT_REQUIRED_FIELDS)


def validate_receipt(receipt: dict[str, Any]) -> list[str]:
    return _missing_fields(receipt, RECEIPT_REQUIRED_FIELDS)
