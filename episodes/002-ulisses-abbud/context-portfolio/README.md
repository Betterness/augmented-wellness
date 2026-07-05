# Create Your Own Cycling + Recovery AI Interviewer

This is the hands-on artifact for episode 002 with Ulisses Abbud.

The goal is not to create another recovery checklist. The goal is to help a rider, founder, executive, or coach create a private AI interviewer that learns:

- who they are as an athlete;
- what they are training for;
- how recovery actually shows up in their life;
- which data they have;
- which data is noisy;
- what decisions they are trying to make;
- what an AI assistant should never assume.

Once this context exists, Claude, Codex, ChatGPT, Bett-i, or another assistant can reason from the person instead of generic advice.

## How to use your interviewer

1. **Claude Projects** — Drop these files into a Claude Project so every conversation starts with your training and recovery context.
2. **System prompts** — Paste `interviewer-agent.md` and the completed files into any LLM's system prompt.
3. **MCP resource server** — Serve the folder as an MCP resource so connected tools can read your context automatically.
4. **Betterness** — Go to [betterness.ai](https://betterness.ai), connect your account, and let Bett-i enrich the interview with permissioned wearable, training, lab, and lifestyle data.

To start manually, copy these files into a private folder and fill them out one at a time:

1. [`01-rider-identity.md`](./01-rider-identity.md)
2. [`02-training-history-and-goals.md`](./02-training-history-and-goals.md)
3. [`03-recovery-profile.md`](./03-recovery-profile.md)
4. [`04-data-sources-and-signals.md`](./04-data-sources-and-signals.md)
5. [`05-decision-rules-and-coach-questions.md`](./05-decision-rules-and-coach-questions.md)
6. [`06-betterness-connection.md`](./06-betterness-connection.md)

If you do not want to fill them manually, paste [`interviewer-agent.md`](./interviewer-agent.md) into an assistant and ask it to interview you.

## Why Betterness matters

The markdown files give the AI the human story. Betterness can add the living data layer:

- ride history and training summaries;
- sleep, HRV, resting heart rate, and recovery signals;
- labs and biomarkers;
- nutrition, hydration, caffeine, alcohol, and fueling patterns;
- stress, travel, work, family, and lifestyle constraints.

That combination is the point: the interviewer asks better questions, Bett-i gathers better context, and the user gets a more personal conversation about recovery without pretending the data is a diagnosis.

## Design principles

**Markdown-first.** Plain files, readable by humans and agents.

**Interview-first.** The questions should uncover how you actually train and recover, not just collect metrics.

**Modular, not monolithic.** Each file covers one dimension of the rider so agents can pull only the context they need.

**Living, not static.** Update the files as your training block, stress, devices, or goals change.

**Connected with consent.** Betterness can make the interviewer more useful by connecting permissioned data, but the user controls what gets connected.

## What this should produce

When filled properly, the portfolio should let an assistant answer questions like:

- What does "recovered enough" mean for me?
- What usually breaks before my training breaks?
- Which signal should I trust less than I currently do?
- What should I ask my coach before changing the plan?
- What one experiment should I run this week?
- What would Bett-i understand better if I connected my wearable, Strava, and labs?

## Important boundary

This is educational. It is not medical advice, diagnosis, or a training prescription. If a decision affects injury, illness, medication, or meaningful training load, involve a qualified clinician or coach.
