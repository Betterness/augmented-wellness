---
title: better-x SAFETY
tags:
  - betterx
  - safety
status: active
---

# better-x safety model

better-x is built to be careful first and useful second. It is a private
editorial desk with memory, not an engagement bot. This document is the
contract: what's off by default, how a draft becomes an action, and what never
leaves your machine.

## Autonomy is off by default

The shipped config (`betterx.config.example.json`) is fail-safe:

- `autonomy.stop_all_external_actions: true`
- `x.read_enabled: false`
- `x.write_enabled: false`
- `delivery.announce: false`

In this state better-x can read your local vault, build prompts, and write
review artifacts. It cannot post, reply, like, follow, repost, quote, block,
DM, or message anything. Permission is never inferred from the fact that a tool
exists — it has to be explicitly turned on.

## The review queue

No public action ever starts from "post this." Every candidate first becomes a
**review artifact** — a JSON file in `vault/05-runs/draft-queues/` that records:

- the source/context it was drafted from;
- the writer's draft and rationale;
- each reviewer's notes and any unresolved objections;
- the relationship context (or `unknown`);
- the `final_text` and the **exact command** that *would* run.

You review and edit that file. It is an artifact you approve, not a message
that's already gone out. The example shape is in
[`runtime-vault-seed/vault/05-runs/draft-queues/review-artifact.example.json`](runtime-vault-seed/vault/05-runs/draft-queues/review-artifact.example.json).

## The two-model publication gate

A draft is not trusted until at least two independent models have looked at it
and the rule passes are clean:

1. **Writer** drafts platform-native text (Grok non-reasoning when configured,
   otherwise the fallback model).
2. **Mechanical reviewer** (Haiku) catches automation tells: numbered lists,
   repeated structures, odd capitalization, length, link spam.
3. **Adversarial / editorial reviewer** (Sonnet) critiques voice, authenticity,
   reputation risk, unsupported claims, and private-data leakage — and looks for
   reasons to reject.
4. **Final safety pass** applies policy, medical, and action-type checks before
   anything could execute.

The model roles are declared in `model_roles` in your config. If two models
disagree or any objection is unresolved, the candidate does not advance to an
action — it stays a draft.

## The action gate

The only path to a write is `scripts/betterx_action_gate.py`, and the default is
a dry run that validates and prints — never sends:

```bash
python3 scripts/betterx_action_gate.py \
  --workspace ~/.openclaw/workspace/programs/betterx \
  --artifact vault/05-runs/draft-queues/<candidate-review>.json \
  --action quote \
  --dry-run
```

`--dry-run` is the default; the opt-in `--execute` flag is the only thing that
would attempt a write. The gate refuses to proceed if STOP/autonomy is set, if
the artifact failed a check, if the action type doesn't match the artifact, or
if quota/cadence isn't available. As a second line of defense, the bundled
`bin/xurl` guard **blocks raw write verbs** (post, reply, quote, follow, like,
repost, block, dm, delete, and their inverses) and exits with code `73` unless
the call comes from the validated gate. Live posting is a stub: until you
install a real adapter and flip the write switches, the execute path does
nothing externally.

## AI disclosure — no deceptive impersonation

If you wire better-x up to post, you must **disclose that posts are
AI-assisted.** better-x must not pretend to be a human writing in real time and
must not deceptively impersonate you in a way a reasonable reader couldn't tell.
The goal is your voice with your judgment in the loop and the assistance
disclosed — not a covert clone. Decide your disclosure approach before you
enable any write.

## Medical-claims policy

The topic space around this episode includes health, longevity, GLP-1s,
wearables, and AI-in-medicine, so the rule is strict
(`vault/00-control/medical-claims-policy.md`):

- Do not diagnose. Do not claim cures. Do not give personalized medical advice
  to strangers.
- Do not imply AI replaces a clinician.
- Distinguish product perspective, personal experience, and scientific evidence,
  and link sources for research claims.

On the show's own example: Certuma's framing is an AI built to **earn FDA
approval with a physician kept in the loop** — its current products escalate to
a real doctor for anything like a prescription. Nothing in this kit is medical
advice, and better-x must never imply autonomous diagnosis or prescription
without physician oversight.

## The STOP switch

`autonomy.stop_all_external_actions: true` is the master kill switch. While it's
set, the action gate will not execute any external action, full stop. The
runtime also reads a control file (`vault/00-control/STOP.md`) as the operating
brake. To halt everything instantly, set autonomy back to stop, or just stop
running the loop — nothing runs on its own without a scheduler you set up
yourself. How to stop is also covered in [FAQ.md](FAQ.md).

## What never leaves your machine

The kit is split into a **public, tracked** part (this repo: docs, scripts,
seed summaries, example artifacts) and a **private runtime** part (your local
workspace). These never get committed:

- credentials, tokens, cookies, browser sessions, API keys;
- raw X exports, scraped payloads, `.har` files;
- your filled-in `USER.md`, private profile, and relationship labels;
- action logs and the feedback ledger.

`.gitignore` already excludes `*token*`, `*secret*`, `*cookie*`, `*.har`,
`raw/`, `.env*`, and logs. External content (posts, bios, web pages, messages)
is always treated as **untrusted data, never instructions** — see
`vault/00-control/untrusted-input-policy.md`. If external content conflicts with
local policy, local policy wins.
