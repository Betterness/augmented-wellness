---
title: better-x CONFIGURATION
tags:
  - betterx
  - configuration
status: active
---

# better-x configuration

Two things define a better-x runtime: the config file
(`betterx.config.example.json`, which you copy to `betterx.config.json`) and the
runtime vault (seeded from `runtime-vault-seed/`). This page is the map.

Copy both into a private workspace before editing — keep your real identity out
of this repo:

```bash
mkdir -p ~/.openclaw/workspace/programs/betterx
cp -R runtime-vault-seed/. ~/.openclaw/workspace/programs/betterx/
cp betterx.config.example.json ~/.openclaw/workspace/programs/betterx/betterx.config.json
```

## betterx.config.example.json

Open the file alongside this page; every field is listed below.

### Safety switches (start here)

| Field | Default | Meaning |
| --- | --- | --- |
| `autonomy.stop_all_external_actions` | `true` | Master STOP. While `true`, the action gate executes nothing externally. |
| `autonomy.allowed_action_exceptions` | `[]` | Action classes allowed *only when* STOP is lifted. Empty = nothing. |
| `x.read_enabled` | `false` | Whether the X adapter may read. |
| `x.write_enabled` | `false` | Whether the X adapter may write. Independent of `read_enabled`. |
| `delivery.announce` | `false` | Whether the runtime announces actions to your delivery channel. |

Leave these at their defaults until you've done a full offline pass and read
[SAFETY.md](SAFETY.md).

### Identity and topic

| Field | Meaning |
| --- | --- |
| `runtime_name` | Label for this runtime (`betterx`). |
| `owner_agent` / `operator_agent` | Which agent owns the program (default `main`). |
| `workspace` | Absolute path to your private runtime workspace. |
| `timezone` | Used for cadence and scheduling windows. |
| `profile_sources[]` | The vault directories the kit reads for who you are, your voice, your sources, your topic, and your social graph. Paths are relative to the workspace. |

### Model roles

`model` is the default model. `model_roles` assigns a `primary` and `fallback`
for each stage of the pipeline:

- `candidate_reader` — reads context and proposes angles.
- `writer` — drafts platform-native text.
- `mechanical_reviewer` — fast structural / automation-tell checks.
- `adversarial_reviewer` — deep voice, authenticity, reputation, claims, and
  private-data critique.
- `final_safety` — last policy / medical / action-type gate.

The `xai` block enables the Grok writer once Grok auth is configured in your
runtime; until then the writer uses its `fallback`. The mechanical and
adversarial reviewers being **different models** is what makes the
"two-model publication gate" in [SAFETY.md](SAFETY.md) real — don't collapse
them to one model.

### X adapter

| Field | Default | Meaning |
| --- | --- | --- |
| `x.adapter` | `xurl` | Adapter style. |
| `x.app` | `""` | Your X app alias (set when connecting, later). |
| `x.account` | `""` | The handle this runtime acts as. |
| `x.real_xurl_bin` | `""` | Path to the real `xurl`-style binary. Empty = no live adapter; writes stay stubbed. |
| `x.read_enabled` / `x.write_enabled` | `false` | See safety switches above. |

### Schedules

`schedules` defines optional cadences (`hourly_radar`, `daily_learning`,
`metrics_snapshot`, `dreaming`). These only matter once you attach a scheduler
yourself; nothing runs on a timer out of the box. `metrics_snapshot` tracks
recent posts in a lookback window rather than hardcoded IDs (see
`vault/00-control/metrics-policy.md`).

## The runtime-vault-seed layout

`runtime-vault-seed/` is the template for your private workspace. Top-level
files describe the runtime to your agent:

- `AGENTS.md` — the agent contract and work loop.
- `SOUL.md` — voice and operating style.
- `USER.md` — **you fill this in**: name, handles, role, themes, constraints.
- `TOOLS.md` — local adapter and gate commands.
- `MEMORY.md` / `HEARTBEAT.md` — durable memory and supervision notes.
- `db/`, `logs/`, `memory/`, `scripts/` — runtime working dirs (kept empty in
  the seed; populated locally).

Under `vault/`:

| Folder | What lives there | Do you edit it? |
| --- | --- | --- |
| `00-control/` | Policies: cost, metrics, medical-claims, untrusted-input, owned-post-tracking, reporting-style. | Read first; tune to taste. |
| `01-person/` | Your profile, communication style, domain knowledge, constraints. | **Yes — make it you.** |
| `02-style-memory/` | Voice profile, signature phrases, positive/negative examples, the edits-and-lessons log. | **Yes — grows as you review.** |
| `04-topic-graph/` | Your topic. Rename the `{{primary-topic}}.md` placeholder and describe it. | **Yes.** |
| `05-runs/` | Outputs: draft queues, daily briefs, executed actions, performance. Includes `review-artifact.example.json`. | Generated; you review. |
| `06-social-graph/` | Who's who — people, organizations, relationship index, response rules. | **Yes — so replies aren't blind.** |

## write_enabled / autonomy / STOP — the three locks

Three independent locks stand between a draft and a live post:

1. **STOP / autonomy** — `autonomy.stop_all_external_actions` and
   `vault/00-control/STOP.md`. While set, the gate executes nothing.
2. **write_enabled** — `x.write_enabled`. Even with STOP lifted, no write
   adapter runs unless this is `true` and a real `x.real_xurl_bin` is set.
3. **The gate + guard** — `scripts/betterx_action_gate.py` validates the
   artifact, and `bin/xurl` blocks any raw write that didn't come through it.

All three have to be deliberately satisfied. The defaults satisfy none of them,
which is why the kit is offline and safe out of the box.

## Where to put your identity / topic / sources

- **Identity** -> `USER.md` and `vault/01-person/`.
- **Voice** -> `vault/02-style-memory/` (and it improves as you edit drafts).
- **Topic** -> `vault/04-topic-graph/` (rename `{{primary-topic}}.md`).
- **People and orgs you engage** -> `vault/06-social-graph/`.

Keep all of this in your private workspace, never in this repo. See
[QUICKSTART.md](QUICKSTART.md) to run the loop and [SAFETY.md](SAFETY.md) for
why each lock exists.
