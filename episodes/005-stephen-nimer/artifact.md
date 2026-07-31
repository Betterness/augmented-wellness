# Artifact: DCC Research Navigator

> A source-aware map and model-neutral agent kit for understanding the cancer
> research ecosystem publicly highlighted by Faces of the DCC.

## What it is

The Dolphins Cancer Challenge is visible as a ride and fundraiser. The DCC
Research Navigator makes the research network behind it easier to explore.
It connects researchers to cancer areas, scientific themes, and possible
patient relevance while preserving the difference between a public
relationship and a verified funding claim.

## What actually ships

- A browser-readable map of all 35 entries in the public Research Funding List
  across 14 cancer areas.
- Structured JSON with 68 nodes and 215 typed relationships.
- A GitHub-renderable Mermaid map.
- A model-neutral prompt for Claude, ChatGPT, Codex, local agents, or another
  capable LLM.
- An evidence protocol for explaining research without inventing paper-level
  funding or clinical causality.
- Question banks for riders, donors, patients, families, researchers, and Dr.
  Nimer.

## How to use it

1. Open
   [`dcc-research-navigator/dcc-research-map.html`](./dcc-research-navigator/dcc-research-map.html)
   for the visual overview.
2. Read
   [`dcc-research-navigator/methodology.md`](./dcc-research-navigator/methodology.md)
   before making or extending claims.
3. Upload the navigator folder to an LLM project and use
   [`dcc-research-navigator/agent-prompt.md`](./dcc-research-navigator/agent-prompt.md)
   as its operating instructions.
4. Ask one of the questions in
   [`dcc-research-navigator/questions.md`](./dcc-research-navigator/questions.md).

## What it does not establish

- It does not prove that DCC funded a specific paper, grant, experiment, drug,
  or patient outcome.
- It does not rank researchers or treatments.
- It does not provide diagnosis, prognosis, or treatment advice.
- It does not contain private patient, donor, rider, or account data.

## Connect it to Betterness

The public graph can provide research context to a Betterness agent. Personal
health, wearable, lab, and lifestyle context should enter only through a
permissioned Betterness connection. The agent must keep personal data separate
from public research claims and bring medical decisions back to a qualified
care team.
