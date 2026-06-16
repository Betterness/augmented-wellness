# Relationship Schema

Use this schema for people and organizations in the better-x social graph.

## Person Fields

- `name`
- `handles`
  - `x`
  - `linkedin`
  - `instagram`
  - `other`
- `relationship_classes`
  - friend
  - family
  - mentor
  - advisor
  - investor
  - teammate
  - cofounder
  - podcast_guest
  - customer
  - partner
  - prospect
  - journalist
  - public_figure
  - peer
  - critic
  - unknown
- `relationship_to_operator`
- `relationship_to_company`
- `public_context`
- `private_context_summary`
- `topics_to_engage`
- `topics_to_avoid`
- `tone_rules`
- `approval_required`
- `sources`
- `confidence`
  - confirmed
  - inferred
  - needs_review
  - stale

## Organization Fields

- `name`
- `handles`
- `relationship_classes`
  - owned
  - portfolio
  - partner
  - customer
  - prospect
  - investor
  - competitor
  - media
  - institution
  - unknown
- `relationship_to_operator`
- `relationship_to_company`
- `public_context`
- `tone_rules`
- `sources`
- `confidence`

## Source Classes

- `operator_confirmed`
- `public_web`
- `x_profile`
- `x_interaction`
- `podcast`
- `vault_memory`
- `slack_summary`
- `gmail_summary`
- `manual_research`

Never store raw private message bodies unless the operator explicitly asks and the file is clearly marked private.
