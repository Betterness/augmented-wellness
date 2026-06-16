# better-x Tools

Configure local adapters here.

## X Adapter

Default adapter pattern:

```bash
xurl --app <app-alias> whoami
xurl --app <app-alias> timeline -n 5
xurl --app <app-alias> mentions -n 5
```

Write commands must be gated by `vault/00-control/STOP.md` and `vault/00-control/action-policy.md`.

All writes must go through the better-x action gate:

```bash
python3 scripts/betterx_action_gate.py --workspace . --artifact vault/05-runs/draft-queues/<candidate-review>.json --action quote --dry-run
python3 scripts/betterx_action_gate.py --workspace . --artifact vault/05-runs/draft-queues/<candidate-review>.json --action quote
```

Do not run raw `xurl` write commands directly.

## OpenClaw

Cron jobs should run through OpenClaw:

```bash
openclaw cron list
openclaw cron runs --id <job-id> --limit 20
openclaw tasks list
openclaw memory status
```

## Logs

Use:

- `logs/`
- `vault/05-runs/`
- `db/feedback-ledger.jsonl`
