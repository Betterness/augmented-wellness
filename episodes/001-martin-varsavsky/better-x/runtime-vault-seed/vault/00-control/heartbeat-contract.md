# Heartbeat Contract

How often the agent runs and what each cycle does.

- Each cycle: refresh the radar (`scripts/betterx_radar.py`), update the draft queue. Never auto-publish.
- Cadence is set by your scheduler/runtime, not this kit. A daily observe -> draft cycle is a sensible default.
- A heartbeat NEVER bypasses STOP, the action policy, or the publication gate.
- Placeholder — wire to your own scheduler.
