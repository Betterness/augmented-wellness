# Action Policy

Which action classes the agent may take, and under what conditions. Default: NONE (observe/draft only).

## Action classes
`post`, `reply`, `like`, `follow`, `repost`, `quote`, `dm`, `block` — all OFF by default.

## An action may execute only if ALL hold
1. `STOP.md` is INACTIVE.
2. `x.write_enabled=true` and the class is in `x.allowed_actions` (betterx.config).
3. A publication-gate artifact for that exact item is `approved_for_execution` (see `publication-gate.md`).
4. The two-model writer/reviewer check passed.

No action is permitted on operator approval alone. Observe and draft freely; never act without the gate.
