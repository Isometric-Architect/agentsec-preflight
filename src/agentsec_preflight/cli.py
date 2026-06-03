from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .descriptor_examples import by_id, sample_descriptors
from .report_builder import build_receipt, build_report, sample_reports


def _load_descriptor(path: str | None) -> dict[str, Any] | None:
    if not path:
        return by_id("email_send_missing_approval")
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Local AgentSec Preflight PASS/HOLD/BLOCK reports.")
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--preflight", nargs="?", const="examples/email_send_missing_approval.json")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--descriptors", action="store_true")
    args = parser.parse_args(argv)

    if args.descriptors:
        payload: Any = {"descriptors": sample_descriptors()}
    elif args.report:
        payload = {"reports": sample_reports(), "receipts": [build_receipt(report) for report in sample_reports()]}
    elif args.preflight is not None:
        report = build_report(_load_descriptor(args.preflight))
        payload = {"report": report, "receipt": build_receipt(report)}
    else:
        payload = {
            "decision": "PASS_AGENTSEC_PREFLIGHT_SAMPLE_READY",
            "commands": [
                "python -m agentsec_preflight.cli --sample",
                "python -m agentsec_preflight.cli --preflight examples/email_send_missing_approval.json",
                "python -m agentsec_preflight.cli --report",
            ],
            "no_network_required": True,
            "external_action_performed": False,
        }

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
