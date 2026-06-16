---
title: better-x EXAMPLE_WORKFLOW
tags:
  - betterx
  - workflow
status: active
---

# Example workflow: observe -> draft -> review (no live posting)

This is one concrete pass through the kit, start to finish, entirely offline.
Nothing here posts to X. The point is to feel the loop: build a prompt, draft
with your own LLM, turn the draft into a review artifact, and run the gate as a
dry run.

Assumptions:

- You copied the seed into a private workspace and filled in `USER.md`,
  `vault/01-person/profile.md`, `vault/02-style-memory/voice-profile.md`, and
  your `vault/04-topic-graph/` topic file (see [CONFIGURATION.md](CONFIGURATION.md)).
- `betterx.config.json` is still at defaults: autonomy STOP on, read/write off.

Throughout, `$WS` is your workspace:

```bash
WS=~/.openclaw/workspace/programs/betterx
```

## 1. Observe — build a drafting prompt

`betterx_radar.py` reads your vault and assembles a single ready-to-paste
prompt. It is offline — it does not call any API and does not touch X. Print it,
or write it to a file:

```bash
python3 scripts/betterx_radar.py \
  --workspace "$WS" \
  --out "$WS/vault/05-runs/draft-queues/radar-prompt.md"
```

The output is a prompt: who you are, how you sound, what your topic is, the
context to react to, and the rules (no medical claims, no faked familiarity, no
automation tells). It is just text — read it before you use it.

## 2. Draft — paste into your own LLM

Open `radar-prompt.md`, paste it into your LLM of choice (Claude, etc.), and let
it draft. There's no API wiring in this step on purpose — your model, your call.

A reasonable draft for this episode's topic space might be a reaction to the
idea Martin describes in the transcript — that he built an agentic version of
himself for social and that, after enough training, it can sound like him while
he discloses the assistance. A *good* better-x draft engages that idea as a
builder, links nothing it can't support, and makes no health claims.

## 3. Capture — turn the draft into a review artifact

Drop the model's output into a review artifact in the draft queue. Copy the
example and edit it:

```bash
cp "$WS/vault/05-runs/draft-queues/review-artifact.example.json" \
   "$WS/vault/05-runs/draft-queues/candidate-001.json"
```

Fill in:

- `action_type` (`post`, `reply`, `quote`, ...);
- `editorial_chain.writer_output` (the raw draft) and the reviewer notes;
- `relationship_context` — leave `status: "unknown"` if you don't actually know
  the person; do not fake familiarity;
- `final_text` — what would go out;
- `checks` and `policy` — your honest pass/fail per rule.

The artifact, not a post, is the unit of work.

## 4. Review — read it like an editor

Open `candidate-001.json` and ask:

- Does `final_text` sound like *me*, or like a generic thread?
- Did both reviewers (mechanical + adversarial) actually look at it, and are
  there unresolved `objections`?
- Any medical claim that needs a source or needs to come out?
- Any private detail, handle, or relationship label that shouldn't be public?

Edit until you'd be comfortable putting your name on it. Your edits are the
training signal — record what you changed and why in
`vault/02-style-memory/edits-and-lessons.md` so the kit learns your voice.

## 5. Gate — dry run only

Validate the artifact and see the exact command it *would* run. `--dry-run`
prints and stops; it sends nothing:

```bash
python3 scripts/betterx_action_gate.py \
  --workspace "$WS" \
  --artifact vault/05-runs/draft-queues/candidate-001.json \
  --action quote \
  --dry-run
```

`--dry-run` is the default, so you can also just omit it. Expected outcome on a
default install: the gate reports that STOP/autonomy is on (and write is
disabled), shows the command it would have executed, and exits without acting.
That's the system working as designed — a dry run is the end of the line until
you deliberately wire up X. (The opt-in `--execute` flag is the only thing that
would run a write, and only once an adapter is installed and the write switches
are on.)

If you want to confirm the runtime is healthy at any point:

```bash
python3 scripts/betterx_smoke_check.py --workspace "$WS"
```

## What you did NOT do

- You did not post, reply, like, follow, or DM anything.
- You did not call the X API or need an X account.
- You did not lift STOP or enable writes.

That's the whole offline loop. Going live (the optional last step) is described
in [QUICKSTART.md](QUICKSTART.md) under "Before you connect X" and gated by
everything in [SAFETY.md](SAFETY.md).
