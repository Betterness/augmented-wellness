# Reporting Style

Status: mandatory for operator-facing better-x reports.

Purpose: better-x reports should be easy to understand in 30 seconds. Do not dump internal API mechanics unless the operator asks.

## Default Format

Use this structure:

```text
better-x update — <time>

Bottom line:
<one sentence with the actual meaning>

What happened:
- <plain fact>
- <plain fact>

What it means:
- <interpretation>
- <risk or signal>

What we know:
- <confirmed metric or observation>

What we do not know yet:
- <limitation, if relevant>

Next:
- <one concrete next step>
```

## Metrics Reports

Separate these clearly:

- `Your posts`: original posts, quote posts, and replies authored by the operator.
- `Your curation`: reposts/retweets made by the operator.
- `Source popularity`: engagement on the original source posts. This is not the operator's engagement.

Do not say "48 retweets" when that could mean either:

- the operator retweeted 48 posts; or
- other people retweeted the operator.

Use precise language:

- "You reposted/retweeted 48 items."
- "Your two original posts had 34 impressions in the prior snapshot."
- "The reposted source posts were popular, but that is not your engagement."

## Avoid

- long separator lines;
- raw endpoint names unless needed;
- emoji-heavy dashboards;
- huge category breakdowns before the bottom line;
- ambiguous phrases like "Total Interactions" when source metrics are mixed in.
