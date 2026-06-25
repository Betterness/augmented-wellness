# Starter Prompts — Ride + Recovery Intelligence

These prompts are meant to turn the episode into something builders, coaches, and athletes can use.

## 1. Build a recovery summary from raw context

```text
Create a daily recovery summary from these signals: [HRV trend], [resting heart rate], [sleep duration/quality], [training load], [subjective fatigue], [work stress].
Do not diagnose.
Return: signal summary, likely stressors, confidence level, and one small action for today.
```

## 2. Convert a ride file into coaching questions

```text
I uploaded a ride/run summary: [distance, duration, elevation, power/pace, HR zones, temperature, RPE].
Generate 5 coaching questions about pacing, fueling, recovery, and next-session planning.
Tie each question to one measurable signal.
```

## 3. Design a Betterness One coach agent

```text
Design an agent for an endurance coach.
The agent should ingest athlete goals, weekly training, HRV/sleep trends, subjective readiness, and recent injuries.
Define: voice, boundaries, allowed advice, escalation rules, and weekly report format.
```

## 4. Make the science useful

```text
Summarize the endurance research corpus around [sleep / hydration / injury / HRV / fueling / cardiac risk] for a smart non-scientist.
Give me: what seems solid, what is still uncertain, what an athlete can track, and what needs a professional.
Cite PMIDs.
```
