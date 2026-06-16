# Edits And Lessons

Use this file to teach better-x.

## Template

```markdown
## YYYY-MM-DD

### AI Draft

### Operator Edit

### Lesson

### Future Rule
```

## Seed Lesson - Avoid Cost Waste

Label: `blocked`

Lesson:

better-x should optimize for high-signal candidate selection, not volume. Broad timeline/search scans can waste API credits and model tokens without producing useful candidates.

Future rule:

Before any radar run, apply `vault/00-control/cost-policy.md`. Prefer curated watchlists, owned reads, cached candidates, and small query limits. If a run would exceed the read budget, stop and ask or queue a lower-cost plan. Log estimated API cost as part of every run summary.
