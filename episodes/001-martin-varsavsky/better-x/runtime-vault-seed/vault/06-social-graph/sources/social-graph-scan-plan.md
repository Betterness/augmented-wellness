# Social Graph Scan Plan

Status: design contract. Do not run broad scans without explicit source permission and cost budget.

Purpose: build a durable Obsidian-style relationship graph from the operator's public and approved private social context.

## Sources

### X Public/API

Potential imports:

- following list;
- followers list;
- recent mentions and replies;
- recent likes/reposts if access and policy allow;
- historical posts where the operator repeatedly mentions or replies to the same people.

Cost caution:

- X user reads can be charged per returned user resource.
- X post reads can be charged per returned post resource.
- Use small pages, caching, and dedupe before enrichment.
- Do not scan the whole graph in one run.

### better-x Vault

Potential imports:

- `vault/03-source-graph/watchlist.md`
- imported account lists
- profile files
- follow logs
- executed action logs
- draft/rejection logs

### Public Web

Potential imports:

- company/advisor pages;
- podcast pages and transcripts;
- public bios.

### Private Sources

Only with explicit operator permission for each source and purpose:

- Slack summaries;
- Gmail summaries;
- Telegram summaries;
- CRM/customer/investor/team docs.

Never import raw private message bodies by default.

## Pipeline

1. Collect candidate identities into `sources/import-candidates/YYYY-MM-DD.md`.
2. Normalize handles and URLs.
3. Dedupe against `relationship-index.md`.
4. Assign provisional relationship class with source and confidence.
5. Create or update person/organization profile files.
6. Add only high-confidence entries to the top-level index.
7. Log cost estimate and actual API resources used.
8. Ask the operator to correct uncertain high-impact relationships.
