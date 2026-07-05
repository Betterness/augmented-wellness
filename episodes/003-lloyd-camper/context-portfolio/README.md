# Create Your Own Healthspan AI Interviewer

This is the hands-on artifact for episode 003 with Dr. Lloyd Camper.

The goal is not to turn an AI assistant into a doctor. The goal is to create a private AI interviewer that helps a person organize enough healthspan context that their next clinician conversation becomes more useful.

Most people have fragments:

- blood work in one portal;
- a DEXA PDF somewhere;
- a VO2 max report;
- sleep data;
- medications and supplements;
- family history;
- habits that work until travel or stress breaks them.

This interviewer turns those fragments into a structured baseline.

## How to use your interviewer

1. **Claude Projects** — Drop these files into a Claude Project so every healthspan conversation starts with your baseline context.
2. **System prompts** — Paste `interviewer-agent.md` and the completed files into any LLM's system prompt.
3. **MCP resource server** — Serve the folder as an MCP resource so connected tools can read your context automatically.
4. **Betterness** — Go to [betterness.ai](https://betterness.ai), connect your account, and let Bett-i enrich the interview with permissioned labs, wearables, reports, goals, and lifestyle context.

To start manually, copy these files into a private folder and fill them out one at a time:

1. [`01-healthspan-identity.md`](./01-healthspan-identity.md)
2. [`02-history-goals-and-risk.md`](./02-history-goals-and-risk.md)
3. [`03-labs-dexa-vo2-and-reports.md`](./03-labs-dexa-vo2-and-reports.md)
4. [`04-habits-recovery-and-metabolism.md`](./04-habits-recovery-and-metabolism.md)
5. [`05-clinician-visit-brief.md`](./05-clinician-visit-brief.md)
6. [`06-betterness-connection.md`](./06-betterness-connection.md)

If you do not want to fill them manually, paste [`interviewer-agent.md`](./interviewer-agent.md) into an assistant and ask it to interview you.

## Why Betterness matters

The markdown files give the AI the human story. Betterness can add the living data layer:

- labs, biomarkers, and historical trends;
- DEXA, VO2 max, and body-composition reports;
- sleep, HRV, recovery, and activity data;
- medications, supplements, nutrition, and habits the user chooses to provide;
- family history, symptoms, goals, and risk questions;
- stress, travel, work, family, and lifestyle constraints.

That combination is the point: the interviewer gets to know the person, Bett-i gathers better context, and the user can prepare a smarter clinician conversation without asking AI to practice medicine.

## Design principles

**Markdown-first.** Plain files, readable by humans and agents.

**Interview-first.** The questions should uncover goals, history, uncertainty, and real-life constraints before an assistant talks about data.

**Modular, not monolithic.** Each file covers one dimension of the baseline so agents can pull only the context they need.

**Living, not static.** Update the files as labs, reports, habits, medications, symptoms, or goals change.

**Connected with consent.** Betterness can make the interviewer more useful by connecting permissioned data, but the user controls what gets connected.

## What this should produce

When filled properly, the portfolio should let an assistant help you prepare:

- what you know;
- what is missing;
- what changed;
- what should be interpreted by a clinician;
- what habits are realistic;
- what questions to bring to a medical visit.

## Important boundary

This is educational. It is not medical advice, diagnosis, or treatment. Do not use it to start, stop, or change medication, supplements, procedures, or care without a qualified clinician.
