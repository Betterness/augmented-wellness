# better-x scripts

Three small, stdlib-only Python 3 scripts. No pip installs, no network calls
except where you explicitly wire one in later. They turn the vault + config into
a safe observe/draft/queue loop and a guarded execution gate.

This is a STARTER KIT. The radar is an offline prompt assembler, and LIVE X
posting is a STUB you wire up yourself. Nothing here gives medical advice, and
any published post must disclose that it is AI-assisted.

Run everything from this `scripts/` directory (the defaults assume that).

## betterx_radar.py — offline radar prompt assembler

Reads the local vault (profile, voice/style memory, topic graph, social-graph
rules, source graph, control policies) and assembles ONE ready-to-paste prompt.
You run that prompt in your own LLM to get a daily "Augmented Wellness Radar"
plus draft posts/replies/quotes formatted for review. It calls no API and never
touches X. Missing vault files are reported as `(missing)` rather than failing.

```bash
# Print the assembled prompt to stdout
python3 betterx_radar.py --workspace ../runtime-vault-seed

# Or write it to a file
python3 betterx_radar.py --workspace ../runtime-vault-seed --out radar-prompt.txt
```

The drafts it asks for are set to `final_decision: needs_operator_approval` with
an empty `operator_approval` — so the action gate will refuse them until a human
reviews and approves.

## betterx_action_gate.py — DRY-RUN action gate

The single chokepoint for every public write. It validates a review-artifact
JSON against the kit schema, checks the STOP file and the `autonomy` /
`x.write_enabled` config, and REFUSES execution unless ALL of these hold:

- `final_decision == approved_for_execution`
- `operator_approval` is present and non-empty
- every entry in `checks` and `policy` is `pass`
- `autonomy.stop_all_external_actions` is false (or the action is an allowed exception)
- `x.write_enabled` is true
- the STOP file is clear (or absent, with the autonomy block governing)

Default is `--dry-run`. Even with `--execute` on an allowed artifact, posting is
a STUB that only prints "would post …" until you wire a real adapter into
`_post_to_x()`. Every run appends one JSONL line to `logs/action-gate-decisions.jsonl`.

```bash
# See options
python3 betterx_action_gate.py --help

# Dry-run the bundled example artifact (never posts)
python3 betterx_action_gate.py \
  --config ../betterx.config.example.json \
  --artifact ../runtime-vault-seed/vault/05-runs/draft-queues/review-artifact.example.json

# Attempt execution (still refused unless write_enabled + approval + clear STOP)
python3 betterx_action_gate.py \
  --config ../betterx.config.example.json \
  --artifact <your-review>.json --execute
```

Exit code is `0` when the gate ALLOWs, `1` when it REFUSEs, `2` on bad input.
Use `--now "2026-01-01T00:00:00"` if your runtime forbids reading the wall clock.

## betterx_smoke_check.py — setup validation

Confirms the kit is ready: config present and parseable, required vault files
exist, the review-artifact schema parses with all gate-required fields, and
STOP/autonomy are readable. Seed-stage placeholders (TODO / `{{...}}`) are
reported as `WARN`, real problems as `FAIL`. Exits nonzero if there is any FAIL.

```bash
python3 betterx_smoke_check.py \
  --config ../betterx.config.example.json \
  --workspace ../runtime-vault-seed
```

## Typical loop

1. `betterx_smoke_check.py` — confirm the kit is wired up.
2. `betterx_radar.py` — assemble the prompt, run it in your LLM, save approved
   drafts as review-artifact JSON in `vault/05-runs/draft-queues/`.
3. A human reviews each artifact, sets `operator_approval` and
   `final_decision: approved_for_execution`.
4. `betterx_action_gate.py --execute` — the gate re-checks everything; only then
   would a (wired) poster act.
