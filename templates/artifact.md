<!--
TEMPLATE: episodes/<NNN>-<guest-slug>/artifact.md
Replace every {{PLACEHOLDER}}. This is the build-log entry for the episode's artifact —
the honest "what we built, what ships, what's a stub" record.

RULES:
- Right-size the promise. Be explicit about what runs today vs. what is a stub/TODO.
  Do not call something "runnable" beyond what actually executes.
- Inside the artifact directory itself, write ZERO personal/internal data — no real names,
  org names, handles, absolute home paths, audience metrics, secrets, or cookies. Generic
  paths (e.g. ~/.config/...) and generic tool names are fine.
- If the artifact is an AI that acts as a person, it must disclose AI assistance.
- Nothing here is medical advice.
-->

# Artifact: `{{artifact-name}}`

> {{One sentence: what this artifact is and who it's for.}}

## What it is

{{2–4 sentences. The shape of the thing. Where it came from in the episode.}}

## What actually ships today

<!-- Be precise. This is the part people will hold you to. -->
- {{Concretely runnable piece #1 — e.g. "a local observe/draft prompt flow"}}
- {{Concretely runnable piece #2 — e.g. "a guarded DRY-RUN action gate"}}

## What is a stub / TODO (you wire this up)

- {{Stub #1 — e.g. "LIVE posting/API calls are stubbed; bring your own credentials and enable explicitly"}}
- {{Stub #2}}

## Guardrails baked in

<!-- The defaults that keep it safe out of the box. -->
- {{e.g. "autonomy OFF by default"}}
- {{e.g. "review queue — nothing acts without approval"}}
- {{e.g. "two-model gate — a writer and an adversarial reviewer must agree"}}
- {{e.g. "disclosure — discloses AI assistance; does not impersonate"}}

## Quickstart

```bash
# 1. Fork / copy the artifact folder
{{command}}

# 2. Fill in the blank vault/config with your own identity + sources
{{command}}

# 3. Run in dry-run / review-only mode first
{{command}}
```

## Folder map

```text
{{artifact-name}}/
  {{file or dir}}        # {{what it is}}
  {{file or dir}}        # {{what it is}}
```

## Configuration

<!-- Point at the example config; never commit a real one. -->
- Copy `{{config.example.json}}` → `{{config.json}}` and fill it in.
- Secrets/credentials live OUTSIDE the repo (ignored paths or your own secret store).

## Safety & scope notes

- {{Risk class of this artifact and the boundary it must not cross.}}
- If health-related: not medical advice; no autonomous diagnosis/prescription; physician in the loop.

---

This artifact is a starter kit / build-log artifact. It does only what the "What actually ships" section says.
