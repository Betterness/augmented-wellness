---
title: better-x
tags:
  - betterx
  - openclaw
  - social-autopilot
status: active
---

# better-x

better-x is a public, forkable X/social autopilot starter kit.

It helps an operator participate in the conversation around their chosen
topic through their own lens, while learning from their context sources, X,
and their own edits. Fork it, drop in your own identity, and it becomes your
social operating system.

Start here:

1. [AGENT_NATIVE_ARCHITECTURE.md](AGENT_NATIVE_ARCHITECTURE.md)
2. [OPENCLAW_QUICKSTART.md](OPENCLAW_QUICKSTART.md)
3. [ARCHITECTURE_2026_OPENCLAW.md](ARCHITECTURE_2026_OPENCLAW.md)
4. [CODEX_QUICKSTART.md](CODEX_QUICKSTART.md)
5. [X_DEVELOPER_SETUP.md](X_DEVELOPER_SETUP.md)
6. [COSTS_AND_BUDGETS.md](COSTS_AND_BUDGETS.md)
7. [PACKAGE_MANIFEST.md](PACKAGE_MANIFEST.md)
8. [[better-x Starter Vault Spec]]

Reference notes:

- [[better-x OpenClaw Prompts]]

## Install

From this repository:

```bash
python3 scripts/betterx_install.py \
  --workspace ~/.openclaw/workspace/programs/betterx \
  --owner-agent main \
  --model anthropic/claude-haiku-4-5
```

With X configured:

```bash
python3 scripts/betterx_install.py \
  --workspace ~/.openclaw/workspace/programs/betterx \
  --owner-agent main \
  --x-app betterx-<handle> \
  --x-account @<handle> \
  --delivery-channel telegram \
  --delivery-target <telegram-chat-id>
```

Validate:

```bash
python3 ~/.openclaw/workspace/programs/betterx/scripts/betterx_smoke_check.py \
  --workspace ~/.openclaw/workspace/programs/betterx \
  --check-openclaw
```

## Codex Mode

To run better-x from a Codex session instead of OpenClaw, use:

```bash
python3 scripts/betterx_codex_runner.py \
  --workspace ~/.betterx/runtime \
  --mode status
```

See [CODEX_QUICKSTART.md](CODEX_QUICKSTART.md).

## Build Artifact

Create the GitHub/release artifact locally:

```bash
python3 scripts/build_artifact.py
```

Outputs:

- `dist/betterx-openclaw-kit.zip`
- `dist/betterx-openclaw-kit.sha256`

The GitHub workflow `.github/workflows/betterx-artifact.yml` builds the same zip and uploads it as an Actions artifact.

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
