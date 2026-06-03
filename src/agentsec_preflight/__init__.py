from __future__ import annotations

"""AgentSec Preflight public package.

The package exposes a small local/no-network API for producing scoped
PASS/HOLD/BLOCK reports before AI-agent tool calls.
"""

from .descriptor_examples import sample_descriptors
from .preflight_engine import preflight_descriptor
from .report_builder import build_receipt, build_report

__version__ = "0.1.0.dev0"

__all__ = [
    "__version__",
    "build_receipt",
    "build_report",
    "preflight_descriptor",
    "sample_descriptors",
]
