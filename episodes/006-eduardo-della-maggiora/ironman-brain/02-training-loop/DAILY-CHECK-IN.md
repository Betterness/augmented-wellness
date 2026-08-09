---
title: Daily Check-In
tags:
  - ironman-brain/daily
---

# Daily Check-In

## Athlete Input

- Sleep as experienced, 1-5:
- Energy, 1-5:
- Motivation, 1-5:
- Soreness or pain, location and 1-10:
- Illness symptoms:
- Work/family/travel load today:
- Planned session:
- What decision needs help:

## Agent Workflow

1. Read [[../01-athlete-context/ATHLETE-PROFILE]].
2. Pull only the minimum relevant MCP data, usually the previous 7 days plus a
   28-day baseline.
3. Check source coverage and timezone.
4. Compare the athlete's subjective report with activity, sleep, and vitals.
5. If relevant, check body composition or biomarkers on an appropriate slower
   cadence rather than treating them as daily readiness scores.
6. Return:
   - what the signals agree on;
   - what conflicts;
   - one to three reasonable options;
   - confidence and downside for each;
   - what requires a coach or clinician.

## Output Prompt

> Help me decide what changes today. Use my confirmed profile, today's check-in,
> and permissioned Betterness data. Do not create false precision. Separate facts,
> my report, and your inference. If the data do not justify a change, say so.
