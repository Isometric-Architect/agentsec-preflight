from __future__ import annotations

"""Deterministic PASS/HOLD/BLOCK routing for synthetic descriptors."""

from typing import Any

from .models import CLAIM_CEILING


TURN_SAVING_REASON = (
    "Preflight before action avoids a likely wasted or unsafe next tool-call turn."
)
ENGINE_MODE = "deterministic_local"


def _result(
    *,
    decision: str,
    reason_codes: list[str],
    safe_next_action: str,
    repair_path: str = "",
    blocked_next_action: str = "",
    no_match_guard_triggered: bool = False,
) -> dict[str, Any]:
    return {
        "decision": decision,
        "reason_codes": reason_codes,
        "turn_saving_reason": TURN_SAVING_REASON,
        "negative_cache_labels": [f"NEG_{code}" for code in reason_codes if not decision.startswith("PASS")],
        "no_match_guard_triggered": no_match_guard_triggered,
        "safe_next_action": safe_next_action,
        "repair_path": repair_path,
        "blocked_next_action": blocked_next_action,
        "claim_ceiling": CLAIM_CEILING,
    }


def _has_external_boundary(descriptor: dict[str, Any]) -> bool:
    return bool(
        descriptor.get("external_action")
        or descriptor.get("public_post_action")
        or descriptor.get("approval_required")
    )


def preflight_descriptor(descriptor: dict[str, Any] | None) -> dict[str, Any]:
    if descriptor is None:
        return _result(
            decision="HOLD_NO_USABLE_CAPABILITY_FOUND",
            reason_codes=["NO_USABLE_CAPABILITY_FOUND", "RUNTIME_TOOL_SCHEMA_REQUIRED"],
            safe_next_action="Inspect current runtime tools or ask the user for a current descriptor.",
            repair_path="Provide a current descriptor, narrow the objective, or use a draft/no-action fallback.",
            blocked_next_action="Do not invent a tool call from pretrained memory.",
            no_match_guard_triggered=True,
        )

    if descriptor.get("claim_overreach_terms"):
        return _result(
            decision="BLOCK_OVERCLAIM",
            reason_codes=["UNSUPPORTED_CLAIM_OVERREACH"],
            safe_next_action="Rewrite the claim as a scoped local preflight report.",
            blocked_next_action="Do not claim safe, certified, product-ready, or action-authorized.",
        )
    if descriptor.get("source_trace_count", 0) <= 0:
        return _result(
            decision="BLOCK_NO_SOURCE_TRACE",
            reason_codes=["NO_SOURCE_TRACE"],
            safe_next_action="Ask for a current source trace before reconsidering.",
            blocked_next_action="Do not rely on unsupported descriptor metadata.",
        )
    if descriptor.get("destructive_action") and descriptor.get("external_action"):
        return _result(
            decision="BLOCK_FORBIDDEN_ACTION",
            reason_codes=["FORBIDDEN_ACTION", "DESTRUCTIVE_ACTION_PREFLIGHT_REQUIRED"],
            safe_next_action="Prepare a local review packet with diff, rollback, policy, and approval.",
            blocked_next_action="Do not perform the external destructive action.",
        )
    if descriptor.get("destructive_action"):
        return _result(
            decision="BLOCK_DESTRUCTIVE_ACTION_PREFLIGHT_REQUIRED",
            reason_codes=["DESTRUCTIVE_ACTION_PREFLIGHT_REQUIRED"],
            safe_next_action="Create dry-run, diff, rollback, and approval packet first.",
            blocked_next_action="Do not run the destructive action.",
        )
    if not descriptor.get("auth_scope_present"):
        return _result(
            decision="HOLD_MISSING_AUTH_OR_SCOPE",
            reason_codes=["MISSING_AUTH_OR_SCOPE"],
            safe_next_action="Request explicit scope and approval before action.",
            repair_path="Add auth/scope metadata and rerun preflight.",
        )
    if not descriptor.get("required_fields_present") or not descriptor.get("input_schema_present"):
        return _result(
            decision="HOLD_MISSING_REQUIRED_FIELDS",
            reason_codes=["MISSING_REQUIRED_FIELDS"],
            safe_next_action="Fill missing fields and rerun preflight.",
            repair_path="Add input schema and required field metadata.",
        )
    if not descriptor.get("docs_url_present"):
        return _result(
            decision="HOLD_MISSING_DOCS_OR_POLICY",
            reason_codes=["MISSING_DOCS_OR_POLICY"],
            safe_next_action="Request current docs and policy before use.",
            repair_path="Add docs or policy reference.",
        )
    if descriptor.get("deprecated_signal"):
        return _result(
            decision="HOLD_STALE_METADATA",
            reason_codes=["STALE_OR_DEPRECATED_METADATA"],
            safe_next_action="Refresh metadata or choose a current candidate.",
            repair_path="Update source trace and stale/deprecated status.",
        )
    if _has_external_boundary(descriptor):
        return _result(
            decision="HOLD_HUMAN_APPROVAL_REQUIRED",
            reason_codes=["EXTERNAL_APPROVAL_REQUIRED"],
            safe_next_action="Prepare a local draft and ask for explicit approval.",
            repair_path="Add approval receipt and current policy.",
        )
    if descriptor.get("tool_type") == "readonly_query":
        return _result(
            decision="PASS_READONLY_SCOPED",
            reason_codes=["READONLY_METADATA_SUFFICIENT"],
            safe_next_action="Use only inside read-only scope.",
        )
    return _result(
        decision="PASS_DISCOVERY_OR_DRAFT_ONLY",
        reason_codes=["DRAFT_OR_DISCOVERY_METADATA_SUFFICIENT"],
        safe_next_action="Use only for scoped discovery or draft generation.",
    )
