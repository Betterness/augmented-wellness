# Cost Policy

Status: mandatory.

X API reads can be more expensive than writes. better-x must treat read volume as a budgeted resource.

## Defaults

- Prefer owned-account reads when possible.
- Avoid broad home-timeline scans.
- Avoid repeated search queries that return many posts.
- Deduplicate candidate reads inside the local workspace before fetching again.
- Keep hourly radar small by default.
- Metrics snapshots should read only recent operator posts, not the full timeline.

## Default Budgets

Per hourly radar run:

- home timeline: max 10 posts;
- search results: max 10 posts per query;
- search queries: max 3;
- detailed post reads: max 5;
- user/profile lookups: max 10;
- writes/actions: controlled separately by `action-policy.md`.

Per day:

- total non-owned post reads: target under 200 unless the operator approves more;
- total follows/user interactions: target under 50 unless the operator approves more.

## Before Any Expanded Scan

Ask for approval or require a scoped exception when a run would exceed:

- 50 non-owned post reads in one run;
- 200 non-owned post reads in one day;
- 20 follows in one hour;
- any unknown endpoint with unclear pricing.

## Logging

Every run should log estimated usage:

- endpoint class;
- resources returned;
- estimated unit cost;
- estimated total cost;
- whether the read is owned-read eligible.

## Design Rule

better-x should optimize for high-signal candidate selection, not volume. A cheap bad scan is still a bad scan, and an expensive bad scan is worse.
