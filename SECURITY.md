# Security Policy

## Why this matters here

This repo ships a starter kit, `better-x`, for building a **disclosed AI agent
that can act on a social account (X)**. Even though live posting ships as a
**stub you wire up yourself**, the moment a builder connects real credentials
the kit is touching a real account. That makes the safety of these patterns —
the action gate, the autonomy-off default, the two-model publication gate,
credential handling — worth disclosing responsibly.

We want to hear about:

- ways the **action gate / dry-run gate can be bypassed** so an agent posts
  without human approval;
- credential, token, or cookie handling that could **leak secrets** (in code,
  examples, logs, or committed data);
- patterns that could let an agent **deceptively impersonate a human** without
  the required AI disclosure;
- any secret, key, cookie, or personal data **accidentally committed** to this
  repository's history.

## Reporting a vulnerability

**Email: partners@betterness.ai**

Please include:

- a description of the issue and the impact you see;
- the file(s) / commit(s) involved;
- steps to reproduce, or a minimal proof of concept;
- whether the issue is already public anywhere.

Please **do not open a public GitHub issue** for a security problem, and please
do not include live secrets in your report — describe the leak and we'll rotate.

We'll acknowledge your report, work with you on a fix and disclosure timeline,
and credit you if you'd like.

## Scope

**In scope**

- The artifacts and kits in this repo (e.g. `episodes/*/better-x`): the policy
  plugin, action gate, config examples, and seed templates.
- Anything in repo history that leaks a secret, token, cookie, or personal data.

**Out of scope**

- The marketing site **betterness.ai/augmentedwellness** (report site issues to
  the same address, but it's a separate property).
- The hosted podcast audio/video on YouTube, Apple, Spotify, or Amazon.
- Third-party tools the kit references (OpenClaw, model providers, the X API,
  etc.) — report those to their respective maintainers.
- Vulnerabilities that require a builder to first commit their own secrets or
  disable the shipped guardrails.

## A note on the guardrails

The medical and reputation guardrails (Certuma is not FDA-approved today; a
physician stays in the loop; nothing here is medical advice; agents disclose
that they are AI) are intentional and load-bearing. A change that removes them
is treated as a defect, not a feature — see [`AGENTS.md`](./AGENTS.md).
