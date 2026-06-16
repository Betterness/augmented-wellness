#!/usr/bin/env python3
"""better-x kit smoke check.

Validates that the kit is set up correctly enough to run the offline radar and
the action gate. Distinguishes FAIL (kit is broken / unsafe) from WARN (seed-stage
placeholders the operator still needs to fill in).

Exits nonzero if there is any FAIL.

Standard library only (argparse, json, pathlib, sys).

Examples
--------
    python3 betterx_smoke_check.py
    python3 betterx_smoke_check.py --config ../betterx.config.example.json \
        --workspace ../runtime-vault-seed
"""

import argparse
import json
import sys
from pathlib import Path


# Files that MUST exist and parse for the kit to function. Relative to workspace.
REQUIRED_VAULT_FILES = (
    "vault/05-runs/draft-queues/review-artifact.example.json",
    "vault/00-control/untrusted-input-policy.md",
    "vault/00-control/medical-claims-policy.md",
    "vault/01-person/profile.md",
    "vault/02-style-memory/voice-profile.md",
    "vault/06-social-graph/response-rules.md",
)

# Schema fields the action gate depends on (must be present in the example artifact).
SCHEMA_FIELDS = (
    "candidate_id",
    "action_type",
    "final_text",
    "operator_approval",
    "checks",
    "policy",
    "final_decision",
)

# Markers that indicate a file is still an unfilled seed template.
PLACEHOLDER_MARKERS = ("TODO", "{{", "}}")


class Report:
    def __init__(self):
        self.fails = []
        self.warns = []
        self.oks = []

    def ok(self, msg):
        self.oks.append(msg)

    def warn(self, msg):
        self.warns.append(msg)

    def fail(self, msg):
        self.fails.append(msg)

    def emit(self):
        for m in self.oks:
            print("OK   %s" % m)
        for m in self.warns:
            print("WARN %s" % m)
        for m in self.fails:
            print("FAIL %s" % m)
        print("---")
        print("summary: %d ok, %d warn, %d fail"
              % (len(self.oks), len(self.warns), len(self.fails)))


def _check_config(report, config_path):
    p = Path(config_path).expanduser()
    if not p.exists():
        report.fail("config not found: %s" % p)
        return None
    try:
        cfg = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        report.fail("config not parseable (%s): %s" % (p, exc))
        return None
    report.ok("config present and parseable: %s" % p)

    # Autonomy block must be present and readable; it is the kill switch.
    autonomy = cfg.get("autonomy")
    if not isinstance(autonomy, dict) or "stop_all_external_actions" not in autonomy:
        report.fail("config.autonomy.stop_all_external_actions missing (no kill switch)")
    else:
        report.ok("autonomy.stop_all_external_actions = %s"
                  % autonomy["stop_all_external_actions"])

    # x.write_enabled must exist (default-closed is fine).
    x_cfg = cfg.get("x")
    if not isinstance(x_cfg, dict) or "write_enabled" not in x_cfg:
        report.fail("config.x.write_enabled missing")
    else:
        we = x_cfg["write_enabled"]
        report.ok("x.write_enabled = %s" % we)
        if we:
            report.warn("x.write_enabled is TRUE — live writes are armed; "
                        "ensure STOP + operator approval discipline is in place")
    return cfg


def _check_required_files(report, workspace):
    for rel in REQUIRED_VAULT_FILES:
        p = workspace / rel
        if not p.exists():
            report.fail("required vault file missing: %s" % rel)
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as exc:
            report.fail("required vault file unreadable (%s): %s" % (rel, exc))
            continue
        report.ok("present: %s" % rel)
        # Seed placeholders are not failures, just not-yet-calibrated.
        if any(marker in text for marker in PLACEHOLDER_MARKERS):
            report.warn("still a seed template (has TODO/{{...}}): %s" % rel)


def _check_schema(report, workspace):
    p = workspace / "vault" / "05-runs" / "draft-queues" / "review-artifact.example.json"
    if not p.exists():
        # Already FAILed in required-files; avoid duplicate noise.
        return
    try:
        artifact = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        report.fail("review-artifact example not parseable: %s" % exc)
        return
    missing = [f for f in SCHEMA_FIELDS if f not in artifact]
    if missing:
        report.fail("review-artifact example missing schema field(s): %s"
                    % ", ".join(missing))
    else:
        report.ok("review-artifact example has all gate-required fields")


def _check_topic_graph(report, workspace):
    tdir = workspace / "vault" / "04-topic-graph"
    if not tdir.exists():
        report.warn("topic-graph dir missing: vault/04-topic-graph")
        return
    mds = sorted(tdir.glob("*.md"))
    if not mds:
        report.warn("topic-graph dir has no .md files")
        return
    templated = [m.name for m in mds if "{{" in m.name]
    if templated:
        report.warn("topic-graph still templated (rename + fill): %s"
                    % ", ".join(templated))
    else:
        report.ok("topic-graph populated: %s" % ", ".join(m.name for m in mds))


def _check_stop(report, workspace):
    p = workspace / "vault" / "00-control" / "STOP.md"
    if not p.exists():
        report.warn("STOP file absent (vault/00-control/STOP.md); the autonomy "
                    "block is the active kill switch until you add one")
        return
    try:
        p.read_text(encoding="utf-8")
    except OSError as exc:
        report.fail("STOP file present but unreadable: %s" % exc)
        return
    report.ok("STOP file present and readable")


def build_parser():
    p = argparse.ArgumentParser(
        prog="betterx_smoke_check.py",
        description="Validate that the better-x kit is set up: config parses, "
                    "required vault files exist, review-artifact schema parses, "
                    "STOP/autonomy are readable. Exits nonzero on any FAIL.",
    )
    p.add_argument("--config", default="../betterx.config.example.json",
                   help="path to betterx.config JSON "
                        "(default: ../betterx.config.example.json)")
    p.add_argument("--workspace", default="../runtime-vault-seed",
                   help="workspace root containing vault/ "
                        "(default: ../runtime-vault-seed)")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    workspace = Path(args.workspace).expanduser()
    report = Report()

    if not (workspace / "vault").exists():
        report.fail("no vault/ under workspace %s" % workspace)
        report.emit()
        return 1

    _check_config(report, args.config)
    _check_required_files(report, workspace)
    _check_schema(report, workspace)
    _check_topic_graph(report, workspace)
    _check_stop(report, workspace)

    report.emit()
    return 1 if report.fails else 0


if __name__ == "__main__":
    sys.exit(main())
