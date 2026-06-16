# Artifact — `better-x`

Every episode of Augmented Wellness leaves behind something you can actually try.
The host says it plainly in this one: "one of the points of [the] mental wellness
podcast is we want to leave people with something actionable… maybe we could…
post in our GitHub… some of the LLM strategies… so people could try to replicate
it." Episode 001's artifact is **[`better-x`](./better-x)**.

## Where it came from in the episode

The seed is **Pedro** — Martin's disclosed AI version of himself on X. In his
words: "I program[med] an agentic version of myself for social media… it took me
maybe two months… with many mistakes." He built it "with [OpenClaw] and with
[Claude] terminal," also using Devin and Codex. Crucially, he didn't just let it
post: "now I have two LLMs there has to be an agreement of two different LLMs… in
order to post something," and he's clear it's **disclosed** — "this is not a
secret I've disclosed it."

`better-x` takes that *shape* — an agent that drafts in your voice, gets reviewed,
and only acts behind a gate — and turns it into a fork-it-yourself starter kit.

## What `better-x` actually is (and is not)

**It is** a starter kit / build-log artifact:

- a **runtime vault seed** — identity, voice memory, social-graph, and control
  policies you fill in with *your own* context;
- an **observe → draft** prompt flow that produces a platform-native draft plus
  a rationale;
- a **multi-role editorial review** (writer → mechanical reviewer → adversarial
  editor → policy gate) so one model never drafts, approves, and ships its own
  work — the kit's analogue of Pedro's "two LLMs must agree";
- a **guarded action gate** with **autonomy OFF by default** and a **human
  review queue**, plus a JSON publication artifact recording every decision;
- explicit **cost budgets**, an **untrusted-input / prompt-injection policy**,
  and a **feedback ledger** that turns your edits and rejections into lessons.

**It is not** "runnable actionable code" beyond what ships. Specifically:

- **Live X posting is a STUB you wire up yourself.** Out of the box the action
  gate runs **dry-run**: it produces the artifact and the exact action command
  but does not broadcast. You connect your own X developer app and flip autonomy
  on deliberately, at your own risk.
- It is **not** Pedro, not Martin's account, and ships with **zero** personal or
  internal data — you drop in your own identity and sources.

## Why this is the honest version of "replicate it"

Pedro took Martin "maybe two months… with many mistakes," running for years on
four years of his own X history. `better-x` gives you the *scaffolding and the
guardrails* so your version starts careful: drafts before autonomy, a review
queue before live posting, disclosure baked into the soul of the kit. The promise
is right-sized on purpose — a working local observe/draft flow plus a guarded
dry-run gate — not a turnkey autonomous poster.

## Guardrails that travel with this artifact

- **Disclose AI assistance.** Like Pedro, a `better-x` agent must not deceptively
  impersonate anyone. It posts *your* voice, *with disclosure* — never covert
  impersonation of someone else.
- **Autonomy is earned, not default.** Keep it in draft/queue until enough
  reviewed examples justify acting; flip live posting on yourself.
- **Nothing here is medical advice**, and `better-x` is a social-content tool —
  it has nothing to do with Certuma's clinical path or any health claim.

## Start here

- Kit root: [`./better-x`](./better-x)
- The prompt ideas, framed: [`prompts.md`](./prompts.md)
- The claims this episode rests on: [`claims.md`](./claims.md)
