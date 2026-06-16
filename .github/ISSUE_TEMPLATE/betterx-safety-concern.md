---
name: better-x safety concern
about: A safety, disclosure, privacy, or guardrail concern with better-x (or another agent artifact).
title: "[safety] <artifact> — <short summary>"
labels: ["safety", "needs-triage"]
---

<!-- For a sensitive disclosure you'd rather not file publicly, see SECURITY.md for a private channel.
     Do not include secrets, credentials, cookies, or anyone's personal data in this issue. -->

**Artifact**
e.g. `better-x` (episode `001-martin-varsavsky`).

**Concern type**
- [ ] Autonomy / guardrail bypass (something can act without approval)
- [ ] Disclosure (AI acting as a person without disclosing assistance, or impersonation)
- [ ] Privacy / data leakage (private or personal data exposed or written to tracked files)
- [ ] Prompt injection (untrusted/fetched input treated as instructions)
- [ ] Medical-safety (medical advice, or implication of autonomous diagnosis/prescription)
- [ ] Other:

**What you observed**
Describe the behavior. What guardrail is weakened or missing?

**How to reproduce (if applicable)**
1.
2.

**Suggested fix (optional)**
What would close the gap (e.g. a check to add to the review artifact, a default to flip off).

**Severity (your read)**
- [ ] Low — cosmetic / docs
- [ ] Medium — guardrail weak but not bypassable in default config
- [ ] High — guardrail bypassable / could cause real harm
