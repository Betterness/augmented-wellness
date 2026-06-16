# better-x Owner-Agent-Native Architecture

Status: replacement architecture.

This supersedes the earlier "separate better-x agent" design.

## Why The First Design Failed

The first design created a split authority boundary:

- The owner agent was the operator-facing assistant in the messaging channel.
- A separate `betterx` agent had the better-x vault and crons.
- The owner agent could still act from conversation context and direct tools.
- better-x rules lived in files, but the active operator-facing agent could bypass them.

That is not the right OpenClaw shape for a reputationally sensitive social system.

## OpenClaw Pattern To Follow

OpenClaw best practice is:

- put durable operating authority in the owner agent's `AGENTS.md` as standing orders;
- use cron as a trigger for those standing orders, not as a duplicate instruction source;
- use background tasks and Task Flow for auditability and durable multi-step work;
- use deterministic preflight/executor scripts for policy gates;
- use hooks or plugin hooks only when runtime interception/blocking is required.

For better-x, the owner agent is the operator-facing `main` agent.

## Target Shape

```text
main
  AGENTS.md
    Program: better-x
  programs/betterx/
    betterx.config.json
    vault/
    scripts/
    logs/
    db/
  cron jobs targeting main
    agent:main:betterx-radar
    agent:main:betterx-learning
    agent:main:betterx-metrics
```

The `betterx` isolated agent may exist only as an optional specialist lane for local drafting or analysis. It must not own cron, approval, or execution authority.

## Authority Model

The owner agent owns:

- conversation with the operator;
- standing order execution;
- selection of better-x tasks;
- delivery of summaries to the messaging channel;
- escalation decisions.

better-x program files own:

- memory and style;
- source graph;
- social graph;
- action policy;
- review artifacts;
- logs and metrics.

Deterministic scripts own:

- STOP enforcement;
- cost preflight;
- quota and cadence checks;
- action-type integrity;
- model-chain completeness;
- product-link checks;
- relationship context requirement;
- final X command execution.

## Required Public-Action Flow

No public action starts from "post this."

Every public action starts as a workflow item:

1. `intake`: classify requested action and risk.
2. `preflight`: check STOP, cost, quota, cadence, account, and tool availability.
3. `source`: read only approved sources and store provenance.
4. `draft`: Grok writer when available; fallback model only if configured.
5. `mechanical_review`: Haiku or configured fast reviewer.
6. `editorial_review`: Sonnet or configured strong editor.
7. `artifact`: write JSON artifact with all outputs and objections.
8. `approval`: require operator approval unless standing authority exists.
9. `execute`: only `scripts/betterx_action_gate.py`.
10. `verify`: read back result when possible.
11. `learn`: update memory from approval, edit, rejection, metric, or failure.

## Cron Shape

Cron prompts should reference the standing order, not restate the whole workflow.

Example:

```bash
openclaw cron add \
  --name betterx-owner-hourly-radar \
  --every 1h \
  --agent main \
  --session isolated \
  --session-key agent:main:betterx-radar \
  --timeout-seconds 900 \
  --message "Execute Program: better-x hourly radar from AGENTS.md using programs/betterx. Draft/review/log only unless STOP is false and the action gate passes."
```

## Packaging Rule

The generic better-x package must install as an owner-agent program by default.

It should not create a separate OpenClaw agent unless the installer is explicitly run with an advanced `--create-specialist-agent` flag.

## Safety Rule

Direct `xurl` write commands are implementation details of `betterx_action_gate.py`, not actions that the owner agent or a cron prompt should call.

If an operator wants stronger runtime enforcement, package a plugin hook that blocks direct better-x X write commands unless the caller is the approved action gate.
