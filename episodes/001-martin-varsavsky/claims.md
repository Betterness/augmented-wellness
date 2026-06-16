# Claims & Guardrails — Episode 001: Martin Varsavsky

The load-bearing claims from this episode, each paired with **what was actually
said** and **the guardrail** that must travel with it. This file exists so that
nobody — human or agent — repeats a claim from this episode without its context.

> **Nothing in this episode or this repo is medical advice.** Opinions are
> Martin's own. Companies and products described are at the stage the transcript
> describes them, not beyond it.

---

## Claim 1 — Certuma's *goal* is FDA approval. It is NOT approved.

**What was said.** Martin describes becoming "obsessed with… building an AI that
passes the FDA that goes through clinical trials." He is explicit about scope and
timeline: "we need to do the trials with the FDA illness by illness condition by
condition this will be probably hundreds will probably cost hundreds of millions
of dollars and we'll take maybe five years."

**Guardrail.** Certuma is **NOT FDA-approved today.** FDA approval is the stated
**goal**, pursued condition-by-condition through clinical trials over a multi-year
horizon. Never describe Certuma — or any product in this episode — as an approved
or autonomous medical authority. Do not imply autonomous diagnosis or
prescription without physician oversight.

## Claim 2 — There is always a physician in the loop (today).

**What was said.** On Certuma Link: "it has doctors in the loop… an agentic
doctor… supervised by Dr. Joe Smith in real life," who "intervenes" for anything
"like a prescription or like an intervention." On Fast Doctor: "when the patients
want to interact with a real doctor to get a prescription then a real doctor
shows up… prescribe[d] by a human doctor." The unifying design: "an AI that
escalates to a human."

**Guardrail.** Present both products as **human-in-the-loop** systems. The
prescription / lab order / imaging order is issued by a **real, licensed
physician**, not the AI. The fully-autonomous prescription is a *future* state
gated on FDA trials (see Claim 1), not the current product.

## Claim 3 — Two distinct money facts: a $9M loan and a $10M seed.

**What was said.**
- *Loan:* "The same bank, Midland Bank rejected me for a job and gave me a 9
  million dollar loan… my first breakthrough in life" — for a loft building he
  was developing as a student. This was **debt**, decades ago.
- *Seed:* "I ended up raising the 10 million seed at a 50 million pre without any
  employees… the AI and myself." This was **equity** for **Certuma**, recently.

**Guardrail.** These are **different events, different decades, different
instruments.** Do not conflate them, average them, or imply the $9M was Certuma
funding. The $9M = 1980s real-estate debt from Midland Bank. The $10M = Certuma's
seed at a $50M pre-money, led by 8VC.

## Claim 4 — "Pedro" is a *disclosed* AI persona; two LLMs must agree to post.

**What was said.** "I program[med] an agentic version of myself for social
media… Pedro is my agent… because of Peter Levels… the creator of [OpenClaw]."
On the safety gate: "now I have two LLMs there has to be an agreement of two
different LLMs… a [Grok] [and] GPT… in order to post something." On disclosure:
"this is not a secret I've disclosed it… I do think AI can find your voice." His
wife Nina "many times can[not] tell if I posted or Pedro posted." He estimates
"maybe 70% of what you see of my [X] is autonomous."

**Guardrail.** Any better-x–style agent must **disclose AI assistance** and must
**not deceptively impersonate** a real person. Pedro is presented as *disclosed*
authorship of one's *own* voice — not covert impersonation of someone else. The
two-model agreement is a **publication gate**, and in [`better-x`](./better-x) it
ships alongside **autonomy off by default** and a **human review queue**. The
"my wife can't tell" line is a vivid quote about *voice fidelity*, not a license
to drop disclosure.

## Claim 5 — Cycling ~14 hours a week at 66, with no fractures.

**What was said.** "I cycle maybe 14 hours a week" (the host estimates "like 60 a
month… 15 a week"). "At 66, I don't have any pains or aches or injuries… I had
maybe four accidents… I never broke anything… maybe 120 stitches… but not
fractures." He attributes durability partly to riding "in places where there are
very few cars" and alternating "mountain and road and gravel."

**Guardrail.** This is **one person's anecdote**, not a training prescription or
a health claim. "14 hours/week" and "no fractures at 66" are *his* numbers.
Don't generalize to a recommendation. Not medical advice.

## Claim 6 — He built "Stravar" on top of / alongside Strava, for himself.

**What was said.** "I coded an app for myself that instead of Strava is called
Stravar because of Varsavsky… a private app I haven't put it in the app store."
It adds metrics Strava lacks: climbing meters-per-hour ("momentum while you're
climbing"), real watts "with sensors on the bike" (vs. Strava's *guess*), and
"U versus U" — his performance on a given climb "better than my average… worse
than my average," ranking him "against myself since 2010." He "started building
it with AI on Xcode and Swift" before "vibe coding was… called vibe coding."

**Guardrail.** Stravar is a **personal, private, unreleased** app — not a product
you can download and not affiliated with Strava. It is a *build-log artifact*,
the same spirit as [`better-x`](./better-x). Don't describe it as available,
official, or a Strava feature.

## Claim 7 — Mounjaro is GLP-1 + GIP; he pairs it with creatine and training.

**What was said.** "I take [Mounjaro] which is GLP and GIP… I weigh the same
without effort… I don't have the food noise." He cautions: "if you take it and
you're not overweight… it doesn't eat in your muscles, so I also take creatine,
but I basically work out a lot, and I cycle maybe 14 hours a week… it's not the
[Mounjaro] alone."

**Guardrail.** **Not medical advice.** This is Martin's personal regimen and his
own mechanistic framing of GLP-1/GIP. GLP-1 medications are prescription drugs;
any decision belongs with a licensed clinician. Do not present his dosage logic,
the creatine pairing, or "no food noise" as guidance for anyone else.

## Claim 8 — He raised the seed with "the AI and myself" — no employees.

**What was said.** "It had never happened to me that I was able to have a
pre-money valuation fund raised without employees in [the] first meeting… the
whole company was the AI and myself at that point. And then of course, I hired a
great team." The AI also advised which VC to pitch (8VC).

**Guardrail.** True as stated **at the moment of the raise** — solo founder +
AI, no employees yet. He explicitly notes he then "hired a great team." Don't
imply Certuma *operates* with no humans; the no-employees fact is about the
fundraising moment, not the company today.

---

## The one-line rule for agents

If you surface any fact from this episode, surface its guardrail with it.
Certuma's status (goal, not approved; human in the loop), the $9M-vs-$10M
distinction, Pedro's disclosure requirement, and "not medical advice" are
non-negotiable context — see [`companion-agent-page.md`](./companion-agent-page.md).
