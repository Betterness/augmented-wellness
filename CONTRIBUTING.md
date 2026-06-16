# Contributing to Augmented Wellness

Thanks for building with us. This repo is the **hands-on lab** that pairs with
the *Augmented Wellness* podcast: starter kits, prompts, source maps, claim
notes, and agent-readable companion files. Contributions come in two flavors:

1. **Episode artifacts** — improving a kit, prompt set, or companion page for an
   episode that already exists.
2. **Challenge solutions** — your own fork / build of an episode's artifact that
   you want to share back.

Either way, read the guardrails below before opening a pull request. They are
non-negotiable; a PR that breaks one will be sent back regardless of how good
the code is.

## The guardrails you must keep

These are the same rules every agent and human follows here (see
[`AGENTS.md`](./AGENTS.md)):

1. **Medical + reputation safety.**
   - Certuma is **not FDA-approved today**; its *goal* is FDA approval with a
     **physician kept in the loop**. Never imply autonomous diagnosis or
     prescription without physician oversight.
   - **Nothing here is medical advice.** Don't add content that reads as
     clinical guidance.
   - Agents that post as a person (the `better-x` pattern) must **disclose that
     they are AI** and must not deceptively impersonate a real human. Keep the
     disclosure and the human-in-the-loop gate.

2. **Don't invent episode facts.** Anything you attribute to a guest or episode
   must trace to that episode's transcript / `sources/`. **Quote verbatim or
   clearly mark a paraphrase.** Cite where it came from.

3. **Right-size the promise.** Describe what actually ships. The kits are
   starter kits / build-log artifacts. For `better-x`, live posting is a stub
   you wire up — don't market it as turnkey.

4. **No secrets, no PII, no private data.** This is the big one (see below).

## No secrets / no PII — ever

Do not commit, and actively keep out of your diff:

- secrets, API keys, tokens, `.env*` files;
- cookies, session files, `*.har` captures;
- exported social data (e.g. an X/Twitter archive);
- raw audio/video or other raw media;
- private runtime logs, local databases, or browser profiles;
- anyone's personal vault or private profile data.

Inside a kit directory (e.g. `better-x/`), write **zero** personal or internal
data: no real names, employer names, absolute home paths, real social handles,
audience numbers, or credentials. Ship **blank seed templates**; if you need an
example, use an obvious placeholder. The repo's [`.gitignore`](./.gitignore)
enforces most of this — but it is your responsibility, not the safety net's.

If you accidentally commit a secret, treat it as compromised: rotate it
immediately and tell us (see [`SECURITY.md`](./SECURITY.md)).

## How to submit

### Improving an existing episode artifact
1. **Fork** the repo and branch from `main`.
2. Make a **surgical** change scoped to one episode's directory.
3. Keep the episode's `companion-agent-page.md` accurate if your change affects
   what the artifact does or what it claims.
4. Open a PR. In the description, say which episode, what changed, and confirm
   you've kept the four guardrails above.

### Sharing a challenge solution / your own build
1. Fork the artifact (e.g. `episodes/001-martin-varsavsky/better-x`) into your
   own repo and build there.
2. To share it back, open a PR that adds a short link + one-paragraph writeup to
   the relevant episode's README under a "Community builds" section (or open an
   issue with the link). Don't dump your whole fork into this repo.
3. Strip every secret and personal detail before you share. Disclosed-AI builds
   must keep their AI disclosure.

## PR checklist

- [ ] Change is scoped to one episode (or one root doc) and is surgical.
- [ ] No invented episode facts; quotes are verbatim or marked as paraphrase.
- [ ] Medical / reputation guardrails preserved (FDA-goal, physician-in-loop,
      not medical advice, AI disclosed).
- [ ] Promises are right-sized to what actually ships.
- [ ] No secrets, cookies, raw media, social exports, logs, or PII.
- [ ] Cross-links honored per [`docs/CROSS-LINK-CONTRACT.md`](./docs/CROSS-LINK-CONTRACT.md).

Questions? **partners@betterness.ai**.

*Nothing here is medical advice. Intelligence in pursuit of better.*
