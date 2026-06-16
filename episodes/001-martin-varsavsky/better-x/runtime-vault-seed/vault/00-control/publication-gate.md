# Publication Gate

No public action ships without a publication-gate artifact.

For each candidate, produce a review artifact (schema: `vault/05-runs/draft-queues/review-artifact.example.json`) recording:
- the exact text/action and the exact command;
- a **writer** pass and an adversarial **reviewer** pass (the reviewer hunts for reasons NOT to publish: voice, usefulness, timing, repetition, source support, medical-claims risk, private-data leakage, reputation risk);
- the operator approval;
- `final_decision: approved_for_execution` only when writer and reviewer agree AND the operator approved.

If they disagree, do not publish — revise or escalate. `scripts/betterx_action_gate.py` refuses anything not `approved_for_execution`.
