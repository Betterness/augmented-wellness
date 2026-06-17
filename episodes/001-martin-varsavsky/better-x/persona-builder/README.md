# better-x Persona Builder

better-x can post in your voice. This is the part that teaches it what your voice
actually is — so a draft reads like *you*, and the review queue + two-model
publication gate can catch the ones that don't.

In Augmented Wellness 001, Martin Varsavsky describes "Pedro," a disclosed agent
that posts in his own voice on X — trained on years of his activity, gated so two
models must agree before anything goes out, to the point that his wife often can't
tell whether he or the agent wrote a given post. The persona builder is how you get
to *your* version of that, honestly and on purpose.

## What it does

It's an **interview**, not a form. You point a capable model at
[`interview-protocol.md`](./interview-protocol.md), and it walks you through a short
set of questions — who you are, how you actually sound, the phrases people recognize,
real posts that are unmistakably you, the posts that never are, and the lines the
agent must never cross. As you answer, it fills the persona files in your vault.

## Where the answers go

The interview writes into better-x's existing vault seed (it does **not** create a
parallel set of files):

| Interview block | Fills |
|---|---|
| Who you are / your domain | `runtime-vault-seed/vault/01-person/profile.md`, `domain-knowledge.md` |
| How you sound (the core) | `runtime-vault-seed/vault/02-style-memory/voice-profile.md` |
| Phrases people recognize | `runtime-vault-seed/vault/02-style-memory/signature-phrases.md` |
| Posts that are unmistakably you | `runtime-vault-seed/vault/02-style-memory/positive-examples.md` |
| Posts that never are | `runtime-vault-seed/vault/02-style-memory/negative-examples.md` |
| Hard rules + disclosure | `runtime-vault-seed/vault/01-person/preferences-and-constraints.md` (mirrored into `vault/00-control/`) |
| Context shifts (reply vs post) | `runtime-vault-seed/vault/01-person/communication-style.md` |

[`example-voice-profile.md`](./example-voice-profile.md) shows what a filled
`voice-profile.md` looks like for a generic founder, so you know the target before
you start.

## How to run it

1. Open a session with the model you run better-x on (Claude, GPT, a terminal agent).
2. Paste the contents of [`interview-protocol.md`](./interview-protocol.md) as the
   system prompt, and tell it where your `runtime-vault-seed/vault/` lives.
3. Answer its questions. **Paste real posts** — yours, good and bad. That's the
   highest-signal thing you can give it.
4. Review each drafted file. Tell it what's off. It revises, then moves on.

When you're done, the seed TODOs are replaced with you. Then — and only then — read
[`SAFETY.md`](../SAFETY.md) before you touch the autonomy setting. better-x ships
with autonomy **off** and a human review queue on purpose, and disclosure is not
optional.

## It's a living thing

A persona is never "done." Every time you approve, edit, or kill a draft, the agent
should update `positive-examples.md`, `negative-examples.md`, and
`edits-and-lessons.md`. Re-run the interview whenever your voice or your boundaries
shift.

## Credit

This is adapted, with gratitude, from the **Personal Context Portfolio** shared on
the **AI Daily Brief** podcast (MIT-licensed). See [`ATTRIBUTION.md`](./ATTRIBUTION.md).
