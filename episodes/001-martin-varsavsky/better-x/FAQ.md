---
title: better-x FAQ
tags:
  - betterx
  - faq
status: active
---

# better-x FAQ

## What is this?

A **starter kit** from the show — a build-log artifact, not a product. It's a
local **observe -> draft -> review** prompt flow plus a guarded **dry-run action
gate**, with a seed runtime vault for your identity, voice, topic, and social
graph. It helps you participate in the conversation around your topic, in your
voice, with a human in the loop. Start at [QUICKSTART.md](QUICKSTART.md).

## Does it post for me?

**No — not by default, and not without real work from you.** Out of the box
autonomy is set to STOP, X read and write are both off, and there's no live X
adapter installed. Live posting is a **stub** you wire up later. Even after you
wire it up, every write has to pass the action gate, and the bundled `bin/xurl`
guard blocks raw write commands that don't come through that gate. See
[SAFETY.md](SAFETY.md).

## Do I need OpenClaw?

**No.** The offline observe/draft/review loop runs with plain `python3` and your
own LLM — you paste the radar prompt into whatever model you use. OpenClaw is
one nice way to run it on a schedule with an owner agent later, but it's
optional. The kit's docs reference generic `~/.openclaw/...` paths only as a
convenient workspace location; any directory works.

## Do I need the X API?

**Only if you eventually want to actually post.** Everything up to and including
the dry-run gate works with no X account and no API key. To go live you'd add an
X developer app, install a real `xurl`-style adapter, point `x.real_xurl_bin` at
it, and flip the write switches — see "Before you connect X" in
[QUICKSTART.md](QUICKSTART.md).

## Is any of this medical advice?

**No.** Nothing in this kit is medical advice. The medical-claims policy
(`vault/00-control/medical-claims-policy.md`) forbids diagnosis, cure claims,
and personalized advice to strangers, and requires sources for research claims.
The show's own example, Certuma, is framed as an AI built to **earn FDA approval
with a physician kept in the loop** — not autonomous diagnosis or prescription.
better-x must never imply otherwise. Details in [SAFETY.md](SAFETY.md).

## How do I make it sound like me?

Three places, and one habit:

- `USER.md` and `vault/01-person/profile.md` — who you are.
- `vault/02-style-memory/voice-profile.md`, `signature-phrases.md`, and the
  positive/negative examples — how you sound.
- `vault/04-topic-graph/` — what you cover.
- The habit: every time you edit a draft in review, log what you changed in
  `vault/02-style-memory/edits-and-lessons.md`. Your edits are the training
  signal. (Per the episode, this is the part that takes real iteration before it
  stops sounding like a generic bot.)

You must also **disclose AI assistance** if you post, and never deceptively
impersonate yourself — see [SAFETY.md](SAFETY.md).

## How do I stop it?

- Set `autonomy.stop_all_external_actions` back to `true` in `betterx.config.json`
  (it's the default). The action gate then executes nothing externally.
- Or set the brake in `vault/00-control/STOP.md`.
- Or simply don't run the loop / detach any scheduler you attached — nothing in
  this kit runs on its own.

## What gets committed vs. kept private?

This repo holds public, tracked things: docs, scripts, seed summaries, and the
example artifact. Your real identity, credentials, tokens, cookies, raw exports,
logs, and the feedback ledger stay in your private workspace and are excluded by
`.gitignore`. See "What never leaves your machine" in [SAFETY.md](SAFETY.md).

## Is this "production-ready agent code"?

No, and it doesn't claim to be. It's a starter kit and a build log: working
prompts, a dry-run gate, source maps, claim notes, and agent-readable companion
files. The live-posting path is intentionally a stub. Right-size your
expectations and read [QUICKSTART.md](QUICKSTART.md) first.
