# Artifact — Create Your Own Cycling + Recovery AI Interviewer

The useful artifact from Ulisses Abbud's episode is not a generic recovery checklist.

It is a way to create your own AI interviewer for cycling, recovery, and performance: an assistant that asks the right questions until it understands the person behind the data.

Instead of asking a generic model, "What does my HRV mean?", you teach an interviewer who you are: why you ride, what you are training for, how stress shows up, which signals you trust, where you overreach, and what a coach should know before changing the plan.

Start here:

**[`context-portfolio/`](./context-portfolio)**

## What it does

The interviewer helps a rider answer deeper questions:

- What does recovery mean for me, not in general?
- What am I asking my body to adapt to this week?
- Which signal do I over-trust?
- Which signal do I under-trust?
- What is my smallest useful experiment for the next 7 days?
- What should I ask my coach before I push harder?

## How to use your interviewer

1. **Claude Projects** — Drop the portfolio files into a Claude Project so every training, recovery, and wearable conversation starts with full context.
2. **System prompts** — Paste the interviewer prompt and key files into any LLM's system prompt for immediate personalization.
3. **MCP resource server** — Serve the portfolio as an MCP resource so connected tools can read your context automatically.
4. **Betterness** — Go to [betterness.ai](https://betterness.ai), connect your account, and let Bett-i enrich the interview with permissioned health, wellness, training, wearable, lab, and lifestyle data.

## Design principles

**Markdown-first.** Every useful AI system can read markdown. The portfolio should be easy for a human to edit and easy for an agent to ingest.

**Interview-first.** The artifact should feel like a smart coach interviewing you, not a spreadsheet asking for data. The questions are designed to reveal the person behind the metrics.

**Modular, not monolithic.** Training identity, recovery, devices, goals, and decision rules live in separate files so an agent can pull the context it needs without reading everything.

**Living, not static.** Recovery changes week to week. The portfolio should be corrected and updated as your training, stress, sleep, and goals evolve.

**Connected with consent.** The markdown files are the human layer. Betterness can add the live data layer only when the user connects an account and grants permission.

## What is included

- [`context-portfolio/01-rider-identity.md`](./context-portfolio/01-rider-identity.md)
- [`context-portfolio/02-training-history-and-goals.md`](./context-portfolio/02-training-history-and-goals.md)
- [`context-portfolio/03-recovery-profile.md`](./context-portfolio/03-recovery-profile.md)
- [`context-portfolio/04-data-sources-and-signals.md`](./context-portfolio/04-data-sources-and-signals.md)
- [`context-portfolio/05-decision-rules-and-coach-questions.md`](./context-portfolio/05-decision-rules-and-coach-questions.md)
- [`context-portfolio/06-betterness-connection.md`](./context-portfolio/06-betterness-connection.md)
- [`context-portfolio/interviewer-agent.md`](./context-portfolio/interviewer-agent.md)

## Why Betterness makes this different

The markdown portfolio works anywhere: Claude, Codex, ChatGPT, or a local agent.

The stronger version happens when you connect it to Betterness. Bett-i can help the interview become a living system by gathering context across dimensions that usually stay disconnected:

- training and ride history;
- sleep, HRV, resting heart rate, and recovery signals;
- labs and biomarkers;
- nutrition, hydration, caffeine, alcohol, and fueling patterns;
- stress, travel, work, family, and lifestyle constraints;
- goals, preferences, prior answers, and coach questions.

As Bett-i moves into betterness.ai, this is the intended direction: your interviewer becomes a living context layer, not a static form.

## Boundary

This is educational. It is not a medical device, diagnosis, training prescription, or replacement for a coach or clinician. Wearable data is useful, but noisy. The artifact is designed to improve questions, not pretend certainty.
