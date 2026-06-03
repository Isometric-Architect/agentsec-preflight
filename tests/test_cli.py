from __future__ import annotations

from agentsec_preflight.cli import main


def test_cli_sample_runs(capsys):
    main(["--sample"])
    out = capsys.readouterr().out
    assert "PASS_AGENTSEC_PREFLIGHT_SAMPLE_READY" in out
    assert "external_action_performed" in out
