# AGENTS.md — Augmented Wellness (companion repo)

> If you are an AI coding agent (Claude, Codex, OpenClaw, Devin, Cursor, etc.)
> working in this repository, read this file first. The human-facing overview
> lives in [`README.md`](./README.md); this file is the contract for agents.

## What this repo is

This is the **hands-on lab companion** to the *Augmented Wellness* podcast. The
polished marketing site lives at **betterness.ai/augmentedwellness**. This
GitHub repo is where people go **after** an episode to try, fork, inspect, and
build the things discussed on the show.

> This repo contains the things we build on the show: **starter kits, prompts,
> source maps, claim notes, and agent-readable companion files.**

It is **not** the marketing site, and it does not host the audio/video. Treat
everything here as a build-log artifact, not a product.

## What lives where

```
.
├── README.md                      # human landing page (badges, episode index)
├── AGENTS.md                      # this file — contract for AI agents
├── CONTRIBUTING.md                # how builders submit artifacts / solutions
├── SECURITY.md                    # responsible disclosure
├── LICENSE                        # MIT, © Betterness 2026
├── CITATION.cff                   # how to cite the show / repo
├── docs/
│   └── CROSS-LINK-CONTRACT.md     # website <-> repo cross-link rules
├── assets/                        # show cover art (committed, public)
└── episodes/
    └── <NNN>-<guest-slug>/
        ├── README.md              # episode overview + chapters + links
        ├── companion-agent-page.md  # agent-readable index for this episode
        ├── <artifact>/            # the buildable thing (e.g. better-x/)
        ├── sources/               # claim notes + source maps (where present)
        └── transcript/            # episode transcript (where present)
```

When you need to know what an episode ships, what claims it makes, or where the
prompts and sources are, start at that episode's
**`companion-agent-page.md`** — it is the per-episode index written for you.

## Hard rules (do not break these)

### 1. Preserve the medical + reputation guardrails
These are load-bearing. Do not soften, remove, or route around them.

- **Certuma is not FDA-approved today.** Its stated *goal* is FDA approval,
  with a **physician kept in the loop**. Never write copy or code that implies
  autonomous medical diagnosis or prescription without physician oversight.
- **Nothing in this repo is medical advice.** Do not generate health
  recommendations as if they were clinical guidance.
- **Disclosed AI only.** Any agent that posts as a person (the `better-x`
  pattern) must **disclose that it is AI** and must not deceptively impersonate
  a real human. Keep the disclosure; keep the human-in-the-loop gate.

### 2. Do not invent episode facts
Anything attributed to a guest or an episode must be grounded in that episode's
transcript and source notes. **Quote verbatim or clearly mark a paraphrase.**
If a fact is not in the transcript or the episode's `sources/`, do not assert
it. When unsure, say so rather than filling the gap.

### 3. Right-size every promise
The buildable artifacts are **starter kits / build-log artifacts**, not turnkey
products. For the `better-x` kit specifically: it is a working local
*observe / draft* prompt flow plus a guarded **dry-run** action gate. **Live
posting is a stub you wire up yourself.** Do not describe it as more capable
than what actually ships.

### 4. Never commit private data or secrets
Do not add — and actively keep out of any diff — the following:

- raw audio/video or other raw media,
- secrets, API keys, tokens, `.env*` files,
- cookies / session files / `*.har` captures,
- exported social data (e.g. X/Twitter archive dumps),
- private runtime logs or local databases,
- personal vaults or anyone's private profile data.

Inside the kit directories (e.g. `better-x/`) write **zero** personal or
internal data — no real names, employer names, absolute home paths, real social
handles, audience metrics, secrets, or cookies. The kit ships with **blank
seed templates only** (e.g. `runtime-vault-seed/`). If you need an example,
use a clearly fake placeholder. See [`.gitignore`](./.gitignore) for the
enforced exclusions and [`SECURITY.md`](./SECURITY.md) for disclosure.

## House style

- Match the tone already in `README.md` and the episode READMEs: plain,
  builder-to-builder, no hype.
- Keep cross-links intact. If you touch an episode page, honor
  [`docs/CROSS-LINK-CONTRACT.md`](./docs/CROSS-LINK-CONTRACT.md).
- Make surgical changes. Don't refactor or reformat files you weren't asked to
  touch.

*Nothing here is medical advice. Intelligence in pursuit of better.*
