# Context Bridge

How this social agent shares context with your main agent / scheduler.

- Read shared context from the locations your runtime exposes (`betterx.config` -> `context_sources`).
- Write outputs (radar, draft queue, decisions) to `runtime-vault-seed/vault/05-runs/`.
- Never pull private or raw data across the bridge into public drafts.
- Placeholder — adapt to your own stack.
