#!/usr/bin/env python3
"""better-x action gate (DRY-RUN by default).

This is the single chokepoint every public write action in the better-x kit must
pass through. It loads the runtime config, validates a review-artifact JSON
against the kit's review-artifact schema, checks the STOP file and the autonomy /
write_enabled settings, and REFUSES execution unless write is explicitly enabled
AND an operator approval is present in the artifact.

LIVE platform posting is a STUB. Even when the gate ALLOWs an --execute run, the
poster only prints "would post ..." unless a real poster is wired in. Wiring a
real poster is left to the operator; see _post_to_x() below.

Standard library only (argparse, json, pathlib, sys, datetime). No pip installs.

Examples
--------
    # See options
    python3 betterx_action_gate.py --help

    # Dry-run the example artifact (default; never posts)
    python3 betterx_action_gate.py \
        --config ../betterx.config.example.json \
        --artifact ../runtime-vault-seed/vault/05-runs/draft-queues/review-artifact.example.json

    # Attempt execution (still refused unless write_enabled + approval + clear STOP)
    python3 betterx_action_gate.py \
        --config ../betterx.config.example.json \
        --artifact <review>.json --execute
"""

import argparse
import json
import sys
from pathlib import Path

# datetime is imported but every wall-clock read is guarded: some runtimes
# forbid reading the system clock, so the gate must degrade gracefully.
import datetime


# --- field names below MUST match runtime-vault-seed/.../review-artifact.example.json ---
REQUIRED_ARTIFACT_FIELDS = (
    "candidate_id",
    "action_type",
    "final_text",
    "operator_approval",
    "checks",
    "policy",
    "final_decision",
)

# final_decision value that signals the editorial pipeline cleared the candidate.
APPROVED_DECISION = "approved_for_execution"

# Action classes the gate understands. Posting is a stub for all of them.
KNOWN_ACTION_TYPES = ("post", "reply", "quote", "repost", "like", "follow", "dm")


def _now(now_arg):
    """Return an ISO-ish timestamp string.

    Prefer an operator-supplied --now value. Otherwise try the wall clock, but
    guard it: the runtime may forbid datetime.now(). Fall back to a placeholder
    so the decision log line is always writable.
    """
    if now_arg:
        return now_arg
    try:
        return datetime.datetime.now().isoformat(timespec="seconds")
    except Exception:
        return "TIMESTAMP_UNAVAILABLE"


def _load_json(path, label):
    p = Path(path).expanduser()
    if not p.exists():
        return None, "%s not found at %s" % (label, p)
    try:
        with p.open("r", encoding="utf-8") as fh:
            return json.load(fh), None
    except (ValueError, OSError) as exc:
        return None, "%s could not be parsed: %s" % (label, exc)


def _resolve_workspace(args, config_path):
    """Workspace root is where the STOP file lives. Default to the config's dir."""
    if args.workspace:
        return Path(args.workspace).expanduser()
    return Path(config_path).expanduser().resolve().parent


def _stop_state(workspace, override_path):
    """Inspect the STOP control file.

    Returns (stop_active, detail). A missing STOP file is NOT treated as
    "clear" by itself; the autonomy block in the config is the real kill switch.
    A present STOP file whose body is non-empty (and not an explicit clear)
    means STOP is active and all external actions are blocked.
    """
    stop_path = Path(override_path).expanduser() if override_path else (
        workspace / "vault" / "00-control" / "STOP.md"
    )
    if not stop_path.exists():
        return False, "STOP file absent (%s); relying on autonomy block" % stop_path
    try:
        body = stop_path.read_text(encoding="utf-8").strip()
    except OSError as exc:
        # If we cannot read the kill switch, fail safe: treat as STOP active.
        return True, "STOP file unreadable (%s); failing safe" % exc
    lowered = body.lower()
    cleared = (not body) or ("status: clear" in lowered) or ("stop: false" in lowered)
    if cleared:
        return False, "STOP file present and explicitly clear"
    return True, "STOP file present and active (external actions blocked)"


def _checks_all_pass(mapping):
    """True only if every value in a checks/policy mapping is the string 'pass'."""
    if not isinstance(mapping, dict) or not mapping:
        return False, []
    failing = [k for k, v in mapping.items() if v != "pass"]
    return (len(failing) == 0), failing


def evaluate(artifact, config, workspace, stop_override):
    """Run the gate. Returns (allow: bool, reasons: list[str])."""
    reasons = []
    allow = True

    # 1. Artifact shape: required fields present.
    missing = [f for f in REQUIRED_ARTIFACT_FIELDS if f not in artifact]
    if missing:
        allow = False
        reasons.append("REFUSE: artifact missing required field(s): %s" % ", ".join(missing))
        # Without the core fields we cannot reason further; bail with what we have.
        return allow, reasons

    # 2. Action type recognized.
    action_type = artifact.get("action_type")
    if action_type not in KNOWN_ACTION_TYPES:
        allow = False
        reasons.append("REFUSE: unknown action_type %r (known: %s)"
                       % (action_type, ", ".join(KNOWN_ACTION_TYPES)))

    # 3. Editorial pipeline cleared the candidate.
    decision = artifact.get("final_decision")
    if decision != APPROVED_DECISION:
        allow = False
        reasons.append("REFUSE: final_decision is %r, expected %r"
                       % (decision, APPROVED_DECISION))
    else:
        reasons.append("OK: final_decision == %s" % APPROVED_DECISION)

    # 4. Operator approval string must be present and non-empty.
    approval = artifact.get("operator_approval")
    if not (isinstance(approval, str) and approval.strip()):
        allow = False
        reasons.append("REFUSE: operator_approval is empty (operator must approve in the artifact)")
    else:
        reasons.append("OK: operator_approval present")

    # 5. Editorial checks all pass.
    checks_ok, checks_failing = _checks_all_pass(artifact.get("checks"))
    if not checks_ok:
        allow = False
        reasons.append("REFUSE: editorial checks not all pass: %s"
                       % (", ".join(checks_failing) or "checks block missing/empty"))
    else:
        reasons.append("OK: all editorial checks pass")

    # 6. Policy checks all pass.
    policy_ok, policy_failing = _checks_all_pass(artifact.get("policy"))
    if not policy_ok:
        allow = False
        reasons.append("REFUSE: policy checks not all pass: %s"
                       % (", ".join(policy_failing) or "policy block missing/empty"))
    else:
        reasons.append("OK: all policy checks pass")

    # 7. Autonomy kill switch in config (stop_all_external_actions).
    autonomy = config.get("autonomy", {}) if isinstance(config, dict) else {}
    stop_all = autonomy.get("stop_all_external_actions", True)
    exceptions = autonomy.get("allowed_action_exceptions", []) or []
    if stop_all and action_type not in exceptions:
        allow = False
        reasons.append("REFUSE: autonomy.stop_all_external_actions is true and %r "
                       "is not in allowed_action_exceptions" % action_type)
    elif stop_all and action_type in exceptions:
        reasons.append("OK: autonomy stop is on but %r is an allowed exception" % action_type)
    else:
        reasons.append("OK: autonomy.stop_all_external_actions is false")

    # 8. write_enabled must be true.
    x_cfg = config.get("x", {}) if isinstance(config, dict) else {}
    write_enabled = bool(x_cfg.get("write_enabled", False))
    if not write_enabled:
        allow = False
        reasons.append("REFUSE: config x.write_enabled is false (writes disabled)")
    else:
        reasons.append("OK: config x.write_enabled is true")

    # 9. STOP control file.
    stop_active, stop_detail = _stop_state(workspace, stop_override)
    if stop_active:
        allow = False
        reasons.append("REFUSE: %s" % stop_detail)
    else:
        reasons.append("OK: %s" % stop_detail)

    return allow, reasons


def _post_to_x(artifact, config):
    """STUB. Real platform posting is intentionally not wired here.

    Wire a real adapter (e.g. the kit's `xurl` bin) by replacing the body below.
    Until then this only reports what it *would* do, even on an allowed --execute.
    """
    exact = artifact.get("exact_command")
    target = " ".join(exact) if isinstance(exact, list) else (
        "%s -> %r" % (artifact.get("action_type"), artifact.get("final_text"))
    )
    print("STUB: would post via X adapter: %s" % target)
    print("STUB: no live poster is wired; nothing was sent.")
    return True


def _append_decision_log(workspace, log_override, record):
    """Append one JSONL line to the decision log. Best-effort; never crashes the gate."""
    log_path = Path(log_override).expanduser() if log_override else (
        workspace / "logs" / "action-gate-decisions.jsonl"
    )
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        return str(log_path), None
    except OSError as exc:
        return str(log_path), str(exc)


def build_parser():
    p = argparse.ArgumentParser(
        prog="betterx_action_gate.py",
        description="better-x DRY-RUN action gate. Refuses public writes unless "
                    "write is enabled, the operator approved the artifact, all "
                    "checks pass, and STOP is clear.",
    )
    p.add_argument("--config", default="../betterx.config.example.json",
                   help="path to betterx.config JSON (default: ../betterx.config.example.json)")
    p.add_argument("--artifact", required=True,
                   help="path to a review-artifact JSON to evaluate")
    p.add_argument("--workspace", default=None,
                   help="workspace root (where vault/ and logs/ live); "
                        "defaults to the config file's directory")
    p.add_argument("--action", default=None,
                   help="expected action class; if set, must match artifact.action_type")
    p.add_argument("--stop-file", default=None,
                   help="override path to the STOP control file")
    p.add_argument("--log-file", default=None,
                   help="override path to the JSONL decision log")
    p.add_argument("--now", default=None,
                   help="timestamp string for the log line (use when the runtime "
                        "forbids reading the wall clock)")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", dest="dry_run", action="store_true", default=True,
                      help="evaluate only; never post (DEFAULT)")
    mode.add_argument("--execute", dest="dry_run", action="store_false",
                      help="attempt execution if and only if the gate ALLOWs "
                           "(posting is still a stub unless a poster is wired)")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    config, cfg_err = _load_json(args.config, "config")
    if cfg_err:
        print("REFUSE: %s" % cfg_err)
        return 2
    artifact, art_err = _load_json(args.artifact, "artifact")
    if art_err:
        print("REFUSE: %s" % art_err)
        return 2

    # Optional action-class consistency check.
    if args.action and artifact.get("action_type") != args.action:
        print("REFUSE: --action %r does not match artifact.action_type %r"
              % (args.action, artifact.get("action_type")))
        return 2

    workspace = _resolve_workspace(args, args.config)
    allow, reasons = evaluate(artifact, config, workspace, args.stop_file)

    mode = "dry-run" if args.dry_run else "execute"
    decision = "ALLOW" if allow else "REFUSE"

    print("=== better-x action gate ===")
    print("artifact:   %s" % args.artifact)
    print("candidate:  %s" % artifact.get("candidate_id"))
    print("action:     %s" % artifact.get("action_type"))
    print("mode:       %s" % mode)
    print("decision:   %s" % decision)
    print("reasons:")
    for r in reasons:
        print("  - %s" % r)

    posted = False
    if allow and not args.dry_run:
        posted = _post_to_x(artifact, config)
    elif allow and args.dry_run:
        print("DRY-RUN: gate ALLOWs but --dry-run is set; nothing was posted.")
    else:
        print("Gate REFUSEd; nothing was posted.")

    record = {
        "ts": _now(args.now),
        "candidate_id": artifact.get("candidate_id"),
        "action_type": artifact.get("action_type"),
        "mode": mode,
        "decision": decision,
        "posted": posted,
        "reasons": reasons,
        "artifact": str(Path(args.artifact).expanduser()),
    }
    log_path, log_err = _append_decision_log(workspace, args.log_file, record)
    if log_err:
        print("WARN: could not write decision log to %s: %s" % (log_path, log_err))
    else:
        print("logged:     %s" % log_path)

    # Exit 0 when the gate ALLOWs, 1 when it REFUSEs (lets callers branch on it).
    return 0 if allow else 1


if __name__ == "__main__":
    sys.exit(main())
