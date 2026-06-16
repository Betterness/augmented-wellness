---
title: better-x
tags:
  - betterx
  - openclaw
  - social-autopilot
status: active
---

# better-x

better-x is a public, forkable **starter kit** for participating in the
conversation around your chosen topic, in your own voice.

It is a build-log artifact from the show: a working local **observe -> draft ->
review** prompt flow plus a guarded **dry-run action gate**. Live X posting is a
**stub** you wire up later — out of the box the kit is offline, autonomy is off,
and nothing posts. Fork it, drop in your own identity, and run the loop.

Start here:

1. [QUICKSTART.md](QUICKSTART.md) — run it in observe/draft mode in ~5 minutes.
2. [SAFETY.md](SAFETY.md) — autonomy-off model, the gate, disclosure, medical policy, STOP.
3. [CONFIGURATION.md](CONFIGURATION.md) — config fields and the runtime vault layout.
4. [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md) — one concrete observe -> draft -> review pass.
5. [FAQ.md](FAQ.md) — the short answers.
6. [AGENT_NATIVE_ARCHITECTURE.md](AGENT_NATIVE_ARCHITECTURE.md) — the owner-agent-native design.

## Try it (offline, no X account)

Copy the seed into a private workspace and run the loop:

```bash
mkdir -p ~/.openclaw/workspace/programs/betterx
cp -R runtime-vault-seed/. ~/.openclaw/workspace/programs/betterx/
cp betterx.config.example.json ~/.openclaw/workspace/programs/betterx/betterx.config.json
```

Build a drafting prompt, paste it into your own LLM, capture the draft as a
review artifact, then dry-run the gate:

```bash
python3 scripts/betterx_radar.py \
  --workspace ~/.openclaw/workspace/programs/betterx --out radar-prompt.txt

python3 scripts/betterx_action_gate.py \
  --workspace ~/.openclaw/workspace/programs/betterx \
  --artifact vault/05-runs/draft-queues/<candidate-review>.json \
  --action quote \
  --dry-run
```

Sanity-check the runtime at any time:

```bash
python3 scripts/betterx_smoke_check.py \
  --workspace ~/.openclaw/workspace/programs/betterx
```

Full walkthrough in [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md).

## What it will NOT do by default

- **No autonomy** — `autonomy.stop_all_external_actions: true`.
- **Nothing posts** — `x.read_enabled` and `x.write_enabled` are both `false`,
  and there's no live X adapter installed.
- **No medical advice / no autonomous diagnosis or prescription** — see
  [SAFETY.md](SAFETY.md).

## Boundary

This folder contains tracked instructions and public-safe seed summaries.

Raw X exports, cookies, sessions, credentials, browser profiles, action logs, and scraped payloads must stay under ignored `_sources/betterx/` folders or another private non-git storage location.

## Packaging Goal

better-x should become a reproducible OpenClaw kit:

- a public runtime vault seed;
- an owner-agent standing-order program contract;
- native OpenClaw cron jobs targeting the owner agent for hourly radar, engagement monitoring, and daily learning;
- explicit action policies and STOP exceptions;
- explicit cost budgets for X API reads/actions and model usage;
- an untrusted-input policy for prompt-injection safety;
- a Grok-writer / Haiku-mechanical / Sonnet-editor review process;
- an Obsidian-style social graph vault so replies and quote posts know whether someone is a friend, mentor, advisor, customer, journalist, stranger, or critic;
- a JSON publication artifact and executable action gate;
- cadence and reporting policies so the prototype does not batch-post or bury the operator in unusable reports;
- one canonical program workspace owned by the operator-facing OpenClaw agent;
- a feedback ledger pattern for self-learning from edits, approvals, rejections, and metrics.
