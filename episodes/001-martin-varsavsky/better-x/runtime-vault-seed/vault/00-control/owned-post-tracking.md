# Owned Post Tracking

Status: mandatory for engagement monitoring.

Purpose: do not lose owned-post metrics when high-volume reposting pushes original posts out of the latest timeline window.

## Required Method

Every engagement monitor run must:

1. Read previous `logs/metrics/*snapshot*.json` files.
2. Build a list of known owned post IDs from the lookback window.
3. Directly re-read those known owned post IDs when possible.
4. Then scan the mixed timeline for newly discovered owned posts.
5. Store newly discovered owned post IDs in the current snapshot.
6. Report owned-post metrics from direct owned-post tracking, not only from the mixed timeline window.

## Plain-English Summary

For operator-facing reports, use:

- "Your posts" for originals, replies, and quote posts by the operator.
- "Your curation" for reposts/retweets by the operator.
- "Source popularity" for engagement on posts by other people.

Do not bury this in endpoint or pagination language unless the operator asks.
