# Prompts — Episode 001: Martin Varsavsky

This is a **high-level map** of the prompt ideas that surfaced in the episode's
artifact. It is *not* the prompt pack itself — the real, runnable prompts live in
the kit, under **[`better-x`](./better-x)** (start with its README and the
`runtime-vault-seed/`).

> No prompts are invented here. The ideas below are drawn from what Martin
> describes doing with Pedro and from the structure `better-x` actually ships.
> Where a prompt is the kit's interpretation rather than Martin's literal words,
> it's labeled as such.

---

## The shape Martin described

From the transcript, Pedro's design has four moves worth turning into prompts:

1. **Learn the voice from real history.** Martin trained on "maybe four years of
   my activity on [X]." Early on "Pedro didn't sound like me… it really was like
   a fake me," and only "if you find unit [tune it]… it gets to a point that it
   is like you." → a *voice-grounding* step that reads your own corpus before it
   drafts.
2. **Draft in that voice.** Produce posts and replies that match your style, not
   generic thought-leadership.
3. **Two models must agree before publishing.** "There has to be an agreement of
   two different LLMs… in order to post something." → a *review/gate* step.
4. **Disclose, and keep authorship honest.** Pedro is disclosed; memory (not
   content alone) is what lets Martin know which posts were his. → disclosure and
   logging are part of the prompt contract, not an afterthought.

## How `better-x` turns that into prompts (high level)

The kit separates roles so one model never drafts, approves, and executes its own
work. Each role is a prompt with a narrow job — see
`better-x/runtime-vault-seed/vault/02-style-memory/adversarial-review-process.md`
for the canonical version:

| Role | Prompt's job (high level) |
|------|---------------------------|
| **Voice / identity seed** | Establish who the operator is and how they sound, from *their own* sources. (`runtime-vault-seed/SOUL.md`, `vault/02-style-memory/voice-profile.md`) |
| **Observe** | Read the timeline / topic radar and decide what's worth responding to. |
| **Writer** | Draft a platform-native post or reply + a short rationale. |
| **Mechanical reviewer** | Catch automation tells: numbered lists, repeated templates, staccato fragments, missing links, length problems. |
| **Adversarial editor** | Improve the draft, make it more specific, strip generic positioning, reduce risk, preserve voice, and look for reasons to reject. |
| **Policy gate** | Enforce STOP rules, disclosure, sensitive-claims policy, privacy, and the untrusted-input / prompt-injection policy — then emit the JSON publication artifact and the exact (dry-run) action command. |

This multi-role review is the kit's analogue of Martin's "two LLMs must agree."

## What you will NOT find here

- **No copy-paste "post like Martin" prompt.** Pedro is trained on *his* history;
  your kit should be grounded in *yours*. Dropping someone else's voice in would
  be exactly the deceptive impersonation the guardrails forbid.
- **No prompt that posts live by itself.** Live X posting is a stub; the gate
  runs dry-run until you wire it up and turn autonomy on deliberately.
- **No invented prompt text.** For the actual, maintained prompt content, go to
  the kit.

## Go to the real thing

→ **[`better-x`](./better-x)** — the runnable starter kit, prompt roles, vault
seed, and the action gate. See also [`artifact.md`](./artifact.md) for what the
kit is and isn't, and [`claims.md`](./claims.md) for the guardrails.
