from __future__ import annotations

"""Synthetic descriptors used by local AgentSec Preflight smoke checks."""

from typing import Any

from .models import CLAIM_CEILING


SAMPLE_SCHEMA = "AgentSecPreflightInput/v0.1"


def _base() -> dict[str, Any]:
    return {
        "schema": SAMPLE_SCHEMA,
        "source_trace_count": 1,
        "docs_url_present": True,
        "input_schema_present": True,
        "required_fields_present": True,
        "auth_scope_present": True,
        "approval_required": False,
        "external_action": False,
        "destructive_action": False,
        "public_post_action": False,
        "deprecated_signal": False,
        "claim_overreach_terms": [],
        "claim_ceiling": CLAIM_CEILING,
    }


def descriptor(**kwargs: Any) -> dict[str, Any]:
    item = _base()
    item.update(kwargs)
    return item


def sample_descriptors() -> list[dict[str, Any]]:
    descriptors = [
        descriptor(descriptor_id="email_draft_tool", name="Email Draft Tool", tool_type="draft_generation"),
        descriptor(
            descriptor_id="email_send_missing_approval",
            name="Email Send Missing Approval",
            tool_type="email_send",
            auth_scope_present=False,
            approval_required=True,
            external_action=True,
        ),
        descriptor(
            descriptor_id="github_merge_forbidden",
            name="GitHub Merge Forbidden",
            tool_type="github_merge",
            approval_required=True,
            external_action=True,
            destructive_action=True,
            public_post_action=True,
        ),
        descriptor(descriptor_id="readonly_db_query", name="Read-Only DB Query", tool_type="readonly_query"),
        descriptor(
            descriptor_id="destructive_db_update_missing_preflight",
            name="Destructive DB Update Missing Preflight",
            tool_type="database_update",
            approval_required=True,
            destructive_action=True,
        ),
        descriptor(
            descriptor_id="mcp_server_no_source_trace",
            name="MCP Server No Source Trace",
            tool_type="mcp_server",
            source_trace_count=0,
        ),
        descriptor(
            descriptor_id="stale_deprecated_candidate",
            name="Stale Deprecated Candidate",
            tool_type="legacy_connector",
            deprecated_signal=True,
        ),
        descriptor(
            descriptor_id="certified_safe_mcp_overclaim",
            name="Certification Overclaim MCP Fixture",
            tool_type="mcp_claim_review",
            claim_overreach_terms=["certified safe", "product ready", "action authorized"],
        ),
    ]
    return descriptors


def by_id(descriptor_id: str) -> dict[str, Any] | None:
    for item in sample_descriptors():
        if item["descriptor_id"] == descriptor_id:
            return item
    return None
