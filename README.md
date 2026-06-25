<div align="center">

<img src="assets/show-cover.jpg" alt="Augmented Wellness" width="520" />

# Augmented Wellness

**Where we meet the people in pursuit of better.**

[![YouTube](https://img.shields.io/badge/YouTube-watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/l2tLdSlamIc)
[![Apple Podcasts](https://img.shields.io/badge/Apple_Podcasts-listen-A050F0?logo=applepodcasts&logoColor=white)](https://podcasts.apple.com/podcast/id1896935053)
[![Spotify](https://img.shields.io/badge/Spotify-listen-1DB954?logo=spotify&logoColor=white)](https://open.spotify.com/show/033zAkDQc1NpADnqP4OFzh)
[![Amazon Music](https://img.shields.io/badge/Amazon_Music-listen-25D1DA?logo=amazonmusic&logoColor=white)](https://music.amazon.com/podcasts/d3fcfba2-fded-460f-b818-1937d04d47db/augmented-wellness)
[![Website](https://img.shields.io/badge/betterness.ai-augmentedwellness-111827)](https://betterness.ai/augmentedwellness)

</div>

---

## This is not a podcast.

It's a build log.

Every episode pairs a real builder — founders, doctors, healers, coaches, operators — with the **things we actually build on the show**: starter kits, prompts, source maps, claim notes, and agent-readable companion files. This repo is the lab where those artifacts live. You don't just listen — you leave with something you can open, read, fork, and build on.

To be precise about what that means: an artifact here is a **starter kit**, not a finished product. Episode 001 ships a working *local* "observe → draft" prompt flow and a guarded **DRY-RUN** action gate. The parts that touch the outside world — live posting to X, real credentials — are **stubs you wire up yourself**. That is the deal, and we keep it honest.

---

## What lives where

Augmented Wellness has two homes. Keep them straight and everything else makes sense.

### What lives on the website — [betterness.ai/augmentedwellness](https://betterness.ai/augmentedwellness)

The polished hub. The place to **discover and watch**:

- Episode pages, video, and audio.
- Show notes, guest bios, and the story.
- Links out to every platform.

If you want to *experience* an episode, start there.

### What lives in this repo — the lab

The hands-on companion. The place to go **after** an episode, to **try / fork / inspect / build**:

- **Starter kits** — the forkable artifact from each episode (e.g. `better-x`).
- **Prompts** — the actual prompt flows the artifact runs.
- **Source maps** — how an artifact reads from your own context, with empty templates.
- **Claim notes** — what an episode asserts, and where it's grounded vs. paraphrased.
- **Agent-readable companion files** — so a coding agent can pick up an artifact and run it without a human re-explaining everything.

> This repo is **not** the marketing site. It's the workshop floor.

---

## Episodes

| # | Guest | Artifact | Episode folder | Watch / Listen |
|---|-------|----------|----------------|----------------|
| **001** | **Martin Varsavsky** — building Certuma, an AI physician whose *goal* is to pass the FDA (a doctor stays in the loop; it is **not approved today**), and *"Pedro,"* his **disclosed** AI agent that posts in his own voice on X, where two models must agree before anything goes out | **[`better-x`](./episodes/001-martin-varsavsky/better-x)** — a starter kit for a guarded, disclosed X agent | [episodes/001-martin-varsavsky](./episodes/001-martin-varsavsky) | [YouTube](https://youtu.be/l2tLdSlamIc) · [Apple](https://podcasts.apple.com/podcast/id1896935053) · [Spotify](https://open.spotify.com/show/033zAkDQc1NpADnqP4OFzh) · [Amazon](https://music.amazon.com/podcasts/d3fcfba2-fded-460f-b818-1937d04d47db/augmented-wellness) · [page](https://betterness.ai/augmentedwellness/001-martin-varsavsky) |
| **002** | **Ulisses Abbud** — former professional cyclist, high-performance coach, and physiology researcher on why recovery is not the reward after performance, but the adaptation mechanism that makes performance possible | **The Art of Recovery** — Ulisses's longevity deck, endurance-research synthesis, and a practical question bank for reading HRV, sleep, training load, and stress without overclaiming | [episodes/002-ulisses-abbud](./episodes/002-ulisses-abbud) | [YouTube](https://youtu.be/VA88-501Zvc) · [Apple](https://podcasts.apple.com/podcast/id1896935053) · [Spotify](https://open.spotify.com/show/033zAkDQc1NpADnqP4OFzh) · [Amazon](https://music.amazon.com/podcasts/d3fcfba2-fded-460f-b818-1937d04d47db/augmented-wellness) · [page](https://betterness.ai/augmentedwellness/002-ulisses-abbud) |

---

## How to use episode artifacts

Each episode folder is self-contained. The pattern is the same every time:

1. **Fork** this repo.
2. **Open the episode folder** — e.g. [`episodes/001-martin-varsavsky`](./episodes/001-martin-varsavsky) — and read its `README.md` for the episode-specific walkthrough.
3. **Open the artifact** inside it — e.g. [`better-x`](./episodes/001-martin-varsavsky/better-x).
4. **Fill in the blank vault.** Every template ships empty — drop in your own identity, topic, and sources. Nothing personal is pre-loaded.
5. **Run it locally behind the action gate** — autonomy **off**, review queue **on**, posting in **DRY-RUN** — until you trust it. Wiring up a live integration is a deliberate, opt-in step you take last.

For 001 specifically, the writer/reviewer prompt flow runs locally; the X-posting path is a stub you connect to your own developer credentials when (and if) you're ready.

---

## How to contribute

Artifacts get better when builders kick the tires. Bug reports, clearer prompts, new source-map templates, and *new episode artifacts* are all welcome.

→ Read **[CONTRIBUTING.md](./CONTRIBUTING.md)** before opening a PR. It covers the folder layout, the empty-vault rule (never commit personal data), and the disclosure requirements for any agent that acts on someone's behalf.

---

## Safety & medical disclaimer

- **Nothing in this repo is medical advice.** It is a build log and a set of developer artifacts. Talk to a clinician for anything health-related.
- **Certuma is not FDA-approved today.** Its stated *goal* is FDA approval, achieved with a physician kept in the loop. Nothing here describes — or should be built into — autonomous medical diagnosis or prescription without physician oversight.
- **Disclosed agents only.** `better-x` and any future "acts as you" artifact must **disclose** that they are AI-assisted. They must not deceptively impersonate a real person.
- Opinions expressed in episodes belong to our guests.

See **[SECURITY.md](./SECURITY.md)** for how to report a vulnerability and the boundary rules around credentials, sources, and secrets.

---

## For sponsors / partners

Augmented Wellness reaches builders, founders, clinicians, and operators who are actively shipping in AI and health. If you want to reach an audience that *opens the repo* — not just watches — reach out via [betterness.ai/augmentedwellness](https://betterness.ai/augmentedwellness).

## For builders

Start with the episode artifact that matches what you want to make. Fork it, gut the empty vault, and make it yours. Open a PR if you improve it — see **[CONTRIBUTING.md](./CONTRIBUTING.md)**.

## For agents: read [AGENTS.md](./AGENTS.md)

If you're a coding agent working in this repo, **[AGENTS.md](./AGENTS.md)** is your entry point: how the repo is laid out, the guardrails you must honor (disclosure, no medical advice, empty-vault privacy), and how artifacts and the website cross-link. The contract that keeps those links in sync lives at **[docs/CROSS-LINK-CONTRACT.md](./docs/CROSS-LINK-CONTRACT.md)**.

---

### About the show

Hosted by **Demian Bellumio** — co-founder and co-CEO of Betterness, longtime Miami tech entrepreneur — who has built across applied AI (his field is graph computing), media, telemedicine, and mental health. On Augmented Wellness he interviews from the inside: a builder comparing notes with the founders, healers, coaches, and operators on a mission to make the world better.

**Produced by Demian Bellumio with the support of agents from Betterness One** — the agentic studio inside Betterness.

This repo contains the things we build on the show: starter kits, prompts, source maps, claim notes, and agent-readable companion files.

Nothing here is medical advice. Opinions belong to our guests. · Licensed under **[LICENSE](./LICENSE)**. · *Intelligence in pursuit of better.*
