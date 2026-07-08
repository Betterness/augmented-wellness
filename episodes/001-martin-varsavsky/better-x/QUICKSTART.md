---
title: better-x QUICKSTART
tags:
  - betterx
  - quickstart
status: active
---

# better-x in 5 minutes

better-x is a **starter kit** for participating in the conversation around your
chosen topic, in your own voice. It is a build-log artifact from the show: a
working local **observe -> draft -> review** prompt flow plus a guarded
**dry-run action gate**. Live posting is a stub you wire up later.

The core kit is runtime-agnostic: plain markdown/JSON files plus Python scripts.
Use it from a terminal, OpenClaw, Hermes, Codex, or another local agentic
platform. OpenClaw-specific files are optional adapters.

This is what the kit gives you on day one:

- A way to turn what's happening around your topic into a **drafting prompt** you
  paste into your own LLM (`scripts/betterx_radar.py`).
- A **review queue** — JSON artifacts that record the draft, the review notes,
  and the exact action that *would* run.
- A **dry-run action gate** that validates an artifact and prints the command it
  would execute, without sending anything (`scripts/betterx_action_gate.py`).
- A seed runtime vault (`runtime-vault-seed/`) holding identity, voice, topic,
  social-graph, and the control policies that keep it careful.

This is not "runnable code that posts for you." Nothing reaches X until you
add credentials and explicitly flip the write switches — and even then, every
write passes the gate.

## The 10-minute result

By the end of this quickstart you will have:

1. a private `~/.betterx/workspace` runtime folder;
2. a generated `radar-prompt.txt` grounded in the seed vault;
3. an example review artifact format for draft posts/replies/quotes;
4. a dry-run gate result that proves the kit refuses to post while STOP,
   write permissions, action allow-lists, or human approval are missing.

That is the point: first build a safe editorial loop, then decide later whether
you want to connect any live platform adapter.

## What it will NOT do by default

- **No autonomy.** `betterx.config.example.json` ships with
  `autonomy.stop_all_external_actions: true`.
- **Nothing posts, replies, likes, follows, reposts, or DMs.** `x.read_enabled`
  and `x.write_enabled` are both `false`.
- **No live X calls.** The bundled `bin/xurl` is a guard that *blocks* write
  verbs (exit code `73`) unless they come from the validated action gate. The
  real X adapter is something you install later.
- **No medical advice, no diagnosis, no autonomous prescriptions.** See
  [SAFETY.md](SAFETY.md).

## Run it in observe / draft mode

You don't need an X account or API key for this loop. You don't even need to be
online once you've copied the seed in.

1. **Copy the seed vault into a local runtime workspace.** Keep your real
   identity and any private files out of this repo folder.

   ```bash
   mkdir -p ~/.betterx/workspace
   cp -R runtime-vault-seed/. ~/.betterx/workspace/
   cp betterx.config.example.json ~/.betterx/workspace/betterx.config.json
   ```

2. **Fill in who you are and what you cover.** Edit, in your runtime workspace
   (not in this repo):

   - `USER.md` — your name, handles, role, themes.
   - `vault/01-person/profile.md` and `vault/02-style-memory/voice-profile.md` —
     so drafts sound like you, not like a bot.
   - `vault/04-topic-graph/` — rename the `{{primary-topic}}.md` placeholder to
     your topic and describe it.

   What to put where is spelled out in [CONFIGURATION.md](CONFIGURATION.md).

3. **Build a drafting prompt.** `scripts/betterx_radar.py` reads your vault
   (identity, voice, topic, social-graph rules, control policies) and assembles
   a single ready-to-paste prompt. It is offline — it never calls any API or
   touches X. Print it, or write it to a file:

   ```bash
   python3 scripts/betterx_radar.py \
     --workspace ~/.betterx/workspace \
     --out radar-prompt.txt
   ```

   You paste that prompt into your own model or agent runtime. Nothing is sent
   anywhere.

4. **Review the drafts.** The model's output becomes a review artifact in
   `vault/05-runs/draft-queues/`. See
   [`runtime-vault-seed/vault/05-runs/draft-queues/review-artifact.example.json`](runtime-vault-seed/vault/05-runs/draft-queues/review-artifact.example.json)
   for the shape.

A full concrete pass is in [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md).

## How to review drafts

Every candidate becomes a JSON **review artifact**, not a post. Open the file
and check:

- `final_text` — what would go out.
- `editorial_chain` — what the writer drafted, what the reviewers changed and
  why, and any unresolved objections.
- `relationship_context` — whether the kit knows who you're replying to (it
  defaults to `unknown` rather than faking familiarity).
- `checks` and `policy` — the rule passes (medical, reputation, private-data,
  cadence, quota).

You edit the artifact until you're happy. Your edits are the training signal —
the kit learns your voice from what you change.

## How the action gate works

When you want to act on an approved artifact, you run it through the gate. By
default you run it as a **dry run**, which validates the artifact and prints the
exact command it *would* execute — and stops there:

```bash
python3 scripts/betterx_action_gate.py \
  --workspace ~/.betterx/workspace \
  --artifact vault/05-runs/draft-queues/<candidate-review>.json \
  --action quote \
  --dry-run
```

`--dry-run` is the default. The gate refuses to execute if `STOP`/autonomy is
set, if the artifact failed a check, if quota or cadence isn't available, or if
the action type doesn't match. The opt-in `--execute` flag is what would run a
write — but only once you've wired up a real X adapter and flipped the write
switches. Out of the box that path is a stub; the guard in `bin/xurl` blocks raw
write verbs regardless.

The safety model behind all of this is in [SAFETY.md](SAFETY.md).

## Before you connect X (later)

Live posting is the last step, and it's optional. Before any post can reach X
you would need:

1. An X developer app and its credentials, kept **outside** this repo.
2. A real `xurl`-style adapter installed and pointed at by
   `x.real_xurl_bin` in your config.
3. `x.read_enabled` / `x.write_enabled` set to `true` and the relevant action
   class added to `x.allowed_actions` and allowed in your control policy.
4. AI-assistance disclosure decided up front (see [SAFETY.md](SAFETY.md)).

Until you do all of that, better-x stays an offline observe/draft tool.

## Sanity check

Confirm the runtime is wired up correctly (read-only, no network):

```bash
python3 scripts/betterx_smoke_check.py \
  --workspace ~/.betterx/workspace
```

## Where to go next

- [SAFETY.md](SAFETY.md) — autonomy-off model, the gate, disclosure, medical policy, STOP.
- [CONFIGURATION.md](CONFIGURATION.md) — every config field and where your data goes.
- [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md) — one concrete observe -> draft -> review pass.
- [FAQ.md](FAQ.md) — the short answers.
