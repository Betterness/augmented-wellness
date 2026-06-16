<!--
TEMPLATE: episodes/<NNN>-<guest-slug>/claims.md
Replace every {{PLACEHOLDER}}. This is the claim-notes file: every assertion the package
makes, its grounding, and its risk class. It exists so a reader (or an agent) can audit
exactly what we said and how confident we are.

RULES:
- One row per claim. A claim is anything a reader could treat as fact.
- Status is one of: GROUNDED (cited in sources.md), GUEST_OPINION (the guest's view,
  marked as such), PARAPHRASE (our wording of what was said), UNVERIFIED (said but not
  independently confirmed).
- Health-adjacent claims get extra scrutiny. Nothing here is medical advice, and no claim
  may imply autonomous medical diagnosis or prescription without a physician in the loop.
- If a tool/agent is described as AI acting in a person's voice, the claim must note that
  AI assistance is disclosed.
-->

# Episode {{NNN}} — Claim Notes

What this package asserts, and how each assertion is grounded.

## Claim ledger

| # | Claim (as stated in the package) | Status | Grounding (sources.md row / timestamp) | Notes |
|---|----------------------------------|--------|----------------------------------------|-------|
| 1 | {{the claim, in plain words}} | {{GROUNDED / GUEST_OPINION / PARAPHRASE / UNVERIFIED}} | {{source ref}} | {{caveats, scope, risk}} |
| 2 | {{...}} | {{...}} | {{...}} | {{...}} |
| 3 | {{...}} | {{...}} | {{...}} | {{...}} |

## Health & safety claims (extra scrutiny)

<!-- Anything touching medicine, supplements, diagnostics, biological age, longevity, etc.
     If there are none, write "None in this episode." -->
| Claim | What's actually supported | What we are NOT claiming |
|-------|---------------------------|--------------------------|
| {{e.g. a product/tool described}} | {{the narrow, supportable version}} | {{the over-promise we explicitly avoid — e.g. "not FDA-approved; not autonomous diagnosis; physician in the loop"}} |

## Disclosure check (AI-acting-as-person artifacts)

<!-- If the artifact involves an AI posting/speaking as a person, confirm: -->
- [ ] The artifact discloses AI assistance.
- [ ] The artifact does not deceptively impersonate the person.
- [ ] Any "voice" cloning is framed as assistive, not autonomous deception.

## Things we deliberately left out

<!-- Claims that came up but we chose not to publish, and why. Keeps future editors honest. -->
- {{Claim}} — left out because {{reason: unverifiable / off-topic / privacy / risk}}.

---

Nothing here is medical advice.
