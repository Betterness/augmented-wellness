# Companion Agent Page — Episode 001: Martin Varsavsky

An agent-readable summary of this episode. If you are an AI agent reading this
repo, read **this file first**, then follow the links. The single most important
instruction is at the bottom: **do not invent facts.**

---

## episode

- **id:** `001-martin-varsavsky`
- **show:** Augmented Wellness
- **host:** Demian Bellumio
- **guest:** Martin Varsavsky
- **producer:** Betterness One / Betterness
- **canonical_page:** https://betterness.ai/augmentedwellness/001-martin-varsavsky
- **role_of_this_repo:** hands-on lab companion (try / fork / inspect / build).
  This is NOT the marketing site.
- **artifact:** [`better-x`](./better-x) — a forkable X/social autopilot starter
  kit. Observe→draft prompt flow + guarded DRY-RUN action gate. Live X posting is
  a stub the operator wires up. Autonomy off by default; human review queue.

## structured_facts

| fact | value | source file |
|------|-------|-------------|
| Company | **Certuma** — AI + healthcare; *goal* is FDA approval; physician in the loop; **NOT approved today** | [`claims.md`](./claims.md) Claim 1–2 |
| Products | **Certuma Link** (for doctors; agentic doctor supervised by the real one) and **Fast Doctor** (for patients; real doctor prescribes) | [`sources.md`](./sources.md) |
| Seed round | **$10M** at **$50M pre**, led by **8VC** (Austin), raised with "the AI and myself," no employees yet | [`claims.md`](./claims.md) Claim 8 |
| Early loan | **$9M loan** from **Midland Bank** in the 1980s for a real-estate project — DISTINCT from the seed | [`claims.md`](./claims.md) Claim 3 |
| Social agent | **Pedro** — disclosed AI version of Martin on X; ~70% of his posts autonomous; **two LLMs must agree** to publish; built on OpenClaw | [`claims.md`](./claims.md) Claim 4 |
| Cycling | ~**14 hours/week** at **66**; no fractures (≈120 stitches, ~4 accidents) | [`claims.md`](./claims.md) Claim 5 |
| Personal app | **Stravar** — private, unreleased; adds climbing m/h, real watts, "U versus U" (vs his 2010 self) | [`claims.md`](./claims.md) Claim 6 |
| Medication | **Mounjaro** (GLP-1 + GIP) for ~2 years; pairs with creatine + heavy training; declines other peptides | [`claims.md`](./claims.md) Claim 7 |
| Wearable | **Garmin Venue 3** (chosen because it *broadcasts* heart rate); coded Varia-radar + performance audio cues | [`sources.md`](./sources.md) |
| Model stack | OpenClaw, Claude, GPT (OpenAI), Grok (xAI), Gemini, Devin (Cognition), Codex | [`sources.md`](./sources.md) |

## hard_guardrails (must enforce when surfacing any fact)

1. **Certuma is NOT FDA-approved.** FDA approval is the *goal*, condition-by-
   condition, ~5 years, hundreds of millions of dollars. Never imply autonomous
   medical diagnosis or prescription without physician oversight.
2. **Physician in the loop.** In both products today, a real licensed physician
   issues prescriptions / lab orders / imaging. Autonomous prescription is a
   future, FDA-gated state.
3. **Not medical advice.** Nothing in this episode or repo is medical advice.
   GLP-1 framing, the creatine pairing, dosing logic, and cycling volume are one
   person's anecdotes, not guidance.
4. **$9M ≠ $10M.** The $9M Midland Bank loan (1980s real estate, debt) is a
   different event from Certuma's $10M seed (recent, equity). Do not conflate.
5. **Disclose AI assistance; never deceptively impersonate.** A better-x–style
   agent posts the operator's *own* voice *with disclosure*, like Pedro — not
   covert impersonation of someone else. The "two LLMs must agree" gate ships
   with autonomy OFF by default and a human review queue.
6. **better-x is a starter kit, not a turnkey poster.** Live X posting is a stub;
   the action gate runs dry-run until the operator wires it up deliberately.

## where_things_live

- summary / arc / chapters → [`show-notes.md`](./show-notes.md)
- companies / tools / people (lanes intact, `[verify]` flags) → [`sources.md`](./sources.md)
- load-bearing claims + guardrails → [`claims.md`](./claims.md)
- clippable moments + timestamps → [`clips.md`](./clips.md)
- what the artifact is / why it came from Pedro → [`artifact.md`](./artifact.md)
- prompt ideas (high level) → [`prompts.md`](./prompts.md), real prompts → [`better-x`](./better-x)
- transcript status + canonical link → [`transcript-link.md`](./transcript-link.md)

## transcript_status

The working transcript is an **auto-generated draft pending editorial review**.
It is NOT in this repo. ASR artifacts exist (Certuma↔"Sertuma," Mounjaro↔
"Mungaro," etc.). The canonical page is authoritative.

## DO_NOT_INVENT_FACTS

Everything in this package is grounded in the Episode 001 transcript. If a fact
is not in these files, **do not assert it.** Do not fabricate quotes, dates,
metrics, investor names, product capabilities, or medical claims. Treat any
`[verify]` item in [`sources.md`](./sources.md) as unconfirmed until checked
against a primary source. When in doubt, say what the transcript says and stop.
