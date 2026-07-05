# Artifact — Create Your Own Healthspan AI Interviewer

The useful artifact from Dr. Lloyd Camper's episode is not a lab checklist.

It is a way to create your own AI interviewer for healthspan: an assistant that asks the right questions until it understands who you are, what you are trying to prevent or improve, what data you already have, what is missing, and what a qualified clinician should help interpret.

Start here:

**[`context-portfolio/`](./context-portfolio)**

## What it does

The interviewer helps someone prepare for a more useful healthspan conversation:

- Why does building a baseline matter now?
- What data do I actually have?
- What am I guessing about?
- What changed recently?
- What should not be interpreted without clinical context?
- What should I bring to my doctor?

## How to use your interviewer

1. **Claude Projects** — Drop the portfolio files into a Claude Project so every healthspan conversation starts with full context.
2. **System prompts** — Paste the interviewer prompt and key files into any LLM's system prompt for immediate personalization.
3. **MCP resource server** — Serve the portfolio as an MCP resource so connected tools can read your context automatically.
4. **Betterness** — Go to [betterness.ai](https://betterness.ai), connect your account, and let Bett-i enrich the interview with permissioned labs, wearables, goals, reports, and lifestyle context.

## Design principles

**Markdown-first.** Every useful AI system can read markdown. The portfolio should be easy for a human to edit and easy for an agent to ingest.

**Interview-first.** The artifact should feel like a thoughtful clinician-prep interview, not a lab dashboard. The questions are designed to surface goals, history, uncertainty, and context before data interpretation.

**Modular, not monolithic.** Health identity, risk, reports, habits, and clinician questions live in separate files so an agent can use the right context for the right task.

**Living, not static.** A healthspan baseline changes as labs, habits, reports, symptoms, and goals change. The portfolio should be updated over time.

**Connected with consent.** The markdown files are the human layer. Betterness can add the live data layer only when the user connects an account and grants permission.

## What is included

- [`context-portfolio/01-healthspan-identity.md`](./context-portfolio/01-healthspan-identity.md)
- [`context-portfolio/02-history-goals-and-risk.md`](./context-portfolio/02-history-goals-and-risk.md)
- [`context-portfolio/03-labs-dexa-vo2-and-reports.md`](./context-portfolio/03-labs-dexa-vo2-and-reports.md)
- [`context-portfolio/04-habits-recovery-and-metabolism.md`](./context-portfolio/04-habits-recovery-and-metabolism.md)
- [`context-portfolio/05-clinician-visit-brief.md`](./context-portfolio/05-clinician-visit-brief.md)
- [`context-portfolio/06-betterness-connection.md`](./context-portfolio/06-betterness-connection.md)
- [`context-portfolio/interviewer-agent.md`](./context-portfolio/interviewer-agent.md)

## Why Betterness makes this different

The markdown portfolio works anywhere: Claude, Codex, ChatGPT, or a local agent.

The stronger version happens when you connect it to Betterness. Bett-i can help the interview become a living system by gathering context across dimensions that usually stay disconnected:

- labs, biomarkers, and historical trends;
- DEXA, VO2 max, and body-composition reports;
- sleep, HRV, recovery, and activity data;
- medications, supplements, nutrition, and habits the user chooses to provide;
- family history, symptoms, goals, and risk questions;
- stress, travel, work, family, and lifestyle constraints.

As Bett-i moves into betterness.ai, this is the intended direction: your baseline becomes a living context layer, not a pile of disconnected reports.

## Boundary

This is educational. It is not medical advice, diagnosis, treatment, or a replacement for a physician. Use it to organize information and prepare better clinician questions.
