# better-x Social Graph Vault

Status: canonical private relationship context for this better-x runtime.

Purpose: better-x should understand who the operator is responding to before it drafts. A reply to a friend, mentor, advisor, investor, teammate, guest, customer, journalist, stranger, critic, or bot should not sound the same.

This folder is an Obsidian-style markdown vault. It stores durable relationship context, source provenance, and response rules.

## Required Files

- `relationship-index.md` - high-level map of people, organizations, and relationship classes.
- `relationship-schema.md` - fields and confidence rules.
- `response-rules.md` - how relationship context changes tone and risk.
- `people/` - one file per person when enough context exists.
- `organizations/` - one file per organization when enough context exists.
- `sources/` - source-specific imports and scan notes.

## Core Rule

Before drafting a reply, quote-post, DM, public mention, or post about a named person or organization, better-x must check this vault.

If the person is unknown, better-x should say `relationship_context: unknown` in the review artifact and avoid fake familiarity.

If the person is known, better-x should include the relationship class and relevant tone rule in the review artifact.

## Privacy

Store only what is useful for public interaction and relationship-aware tone.

Do not paste raw private Slack, Gmail, Telegram, DMs, phone numbers, private health information, or confidential investor/customer notes. Summarize private context as a relationship label with confidence and source class.
