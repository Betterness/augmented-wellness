---
title: better-x
tags:
  - betterx
  - agent-runtime
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

It is not tied to one agent runtime. The core kit is plain files plus Python
scripts, so it can run from a terminal, OpenClaw, Hermes, Codex, or another
local agentic platform. The OpenClaw plugin is included as an
experimental adapter, not as a requirement.

## What you get in 10 minutes

After the quickstart you should have:

- a private runtime folder with a seed identity, voice, topic graph, and safety
  policies;
- a generated `radar-prompt.txt` you can paste into your own model;
- one example review artifact shape for drafts;
- a gate command that refuses to post until STOP is clear, writes are enabled,
  the action is allow-listed, and a human approval is present.

The useful output is not a live bot. It is a safer editorial loop you can adapt:
**watch a topic, draft in your voice, review adversarially, then decide what
deserves to go out.**

Start here:

1. [QUICKSTART.md](QUICKSTART.md) — run it in observe/draft mode in ~5 minutes.
2. [SAFETY.md](SAFETY.md) — autonomy-off model, the gate, disclosure, medical policy, STOP.
3. [CONFIGURATION.md](CONFIGURATION.md) — config fields and the runtime vault layout.
4. [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md) — one concrete observe -> draft -> review pass.
5. [FAQ.md](FAQ.md) — the short answers.
6. [AGENT_NATIVE_ARCHITECTURE.md](AGENT_NATIVE_ARCHITECTURE.md) — the owner-agent-native design.

## Make it sound like you

The kit can draft in your voice, but only as well as it knows your voice. The
[persona-builder/](persona-builder/) is a short interview that fills the vault's
voice and boundary files — the calibration behind the "Pedro" effect Martin
describes in the episode: a disclosed agent tuned well enough that his wife often
can't tell who wrote a post. It's adapted, with credit, from the Personal Context
Portfolio shared on the AI Daily Brief podcast.

## Try it (offline, no X account)

Copy the seed into a private workspace and run the loop:

```bash
mkdir -p ~/.betterx/workspace
cp -R runtime-vault-seed/. ~/.betterx/workspace/
cp betterx.config.example.json ~/.betterx/workspace/betterx.config.json
```

Build a drafting prompt, paste it into your own LLM, capture the draft as a
review artifact, then dry-run the gate:

```bash
python3 scripts/betterx_radar.py \
  --workspace ~/.betterx/workspace --out radar-prompt.txt

python3 scripts/betterx_action_gate.py \
  --workspace ~/.betterx/workspace \
  --artifact vault/05-runs/draft-queues/<candidate-review>.json \
  --action quote \
  --dry-run
```

Sanity-check the runtime at any time:

```bash
python3 scripts/betterx_smoke_check.py \
  --workspace ~/.betterx/workspace
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

better-x should become a reproducible agent-runtime kit:

- a public runtime vault seed;
- an owner-agent standing-order program contract;
- optional runtime jobs targeting the owner agent for hourly radar, engagement monitoring, and daily learning;
- explicit action policies and STOP exceptions;
- explicit cost budgets for X API reads/actions and model usage;
- an untrusted-input policy for prompt-injection safety;
- a platform-native writer / fast mechanical reviewer / strong editorial reviewer process;
- an Obsidian-style social graph vault so replies and quote posts know whether someone is a friend, mentor, advisor, customer, journalist, stranger, or critic;
- a JSON publication artifact and executable action gate;
- cadence and reporting policies so the prototype does not batch-post or bury the operator in unusable reports;
- one canonical program workspace owned by the operator-facing agent;
- a feedback ledger pattern for self-learning from edits, approvals, rejections, and metrics.
