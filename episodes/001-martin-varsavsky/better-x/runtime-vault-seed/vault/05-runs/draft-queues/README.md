# Draft Queues

Store review queues here.

Filename pattern:

```text
YYYY-MM-DD.md
YYYY-MM-DD-<candidate-id>-review.json
```

Each queue item should include:

- source/context
- why it matters
- draft/action
- risk level
- approval required
- writer output
- edited output
- editorial rationale and objections
- relationship context from `vault/06-social-graph`
- rule-check result
- what memory file to update after approval, edit, or rejection

Markdown queue files are for human review. JSON review artifacts are for execution through `scripts/betterx_action_gate.py`.
