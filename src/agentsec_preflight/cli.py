from __future__ import annotations

"""Command-line entry point for local AgentSec Preflight reports."""

import argparse
import json
from pathlib import Path
from typing import Any

from .descriptor_examples import by_id, sample_descriptors
from .report_builder import build_receipt, build_report, sample_reports


DEFAULT_DESCRIPTOR_ID = "email_send_missing_approval"
DEFAULT_DESCRIPTOR_PATH = "examples/email_send_missing_approval.json"
CLI_MODE = "local_no_network_no_action"


def _read_json_file(path: str) -> dict[str, Any]:
    file_path = Path(path)
    return json.loads(file_path.read_text(encoding="utf-8"))


def _load_descriptor(path: str | None) -> dict[str, Any]:
    if path:
        return _read_json_file(path)
    return by_id(DEFAULT_DESCRIPTOR_ID)


def _sample_payload() -> dict[str, Any]:
    return {
        "decision": "PASS_AGENTSEC_PREFLIGHT_SAMPLE_READY",
        "commands": [
            "python -m agentsec_preflight.cli --sample",
            f"python -m agentsec_preflight.cli --preflight {DEFAULT_DESCRIPTOR_PATH}",
            "python -m agentsec_preflight.cli --report",
        ],
        "no_network_required": True,
        "live_tool_call_performed": False,
        "external_action_performed": False,
        "claim_ceiling": [
            "local_preflight_report_only",
            "no_security_certification",
            "no_product_readiness",
            "no_action_authorization",
        ],
    }


def _descriptors_payload() -> dict[str, Any]:
    return {
        "descriptors": sample_descriptors(),
        "no_network_required": True,
        "synthetic_examples_only": True,
    }


def _report_payload() -> dict[str, Any]:
    reports = sample_reports()
    return {
        "reports": reports,
        "receipts": [build_receipt(report) for report in reports],
        "no_network_required": True,
        "external_action_performed": False,
    }


def _preflight_payload(path: str | None) -> dict[str, Any]:
    report = build_report(_load_descriptor(path))
    return {
        "report": report,
        "receipt": build_receipt(report),
        "no_network_required": True,
        "external_action_performed": False,
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Local AgentSec Preflight PASS/HOLD/BLOCK reports.",
    )
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--preflight", nargs="?", const=DEFAULT_DESCRIPTOR_PATH)
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--descriptors", action="store_true")
    return parser


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    if args.descriptors:
        return _descriptors_payload()
    if args.report:
        return _report_payload()
    if args.preflight is not None:
        return _preflight_payload(args.preflight)
    return _sample_payload()


def main(argv: list[str] | None = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)
    payload = build_payload(args)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
