# Metrics Policy

Status: mandatory for engagement monitoring and learning.

Purpose: prevent better-x from learning from misleading platform metrics or reporting source popularity as operator performance.

## Core Rule

Separate three metric classes:

1. `owned_post_metrics`: performance on posts authored by the operator.
2. `operator_action_metrics`: the effect of the operator's action, when measurable.
3. `source_post_metrics`: public performance of another user's original post.

Do not aggregate `source_post_metrics` into operator performance.

## Reposts

If the operator reposts another account:

- the original post's repost, like, reply, and quote counts are source metrics;
- they do not mean the operator generated that engagement;
- reports may mention source popularity only under `source_post_metrics`;
- owned aggregate engagement should exclude these counts unless the platform provides a metric specifically for the operator's repost impression/action.

## Quote Posts

For quote posts:

- owned metric = engagement on the operator's quote post;
- source metric = engagement on the quoted post;
- keep both, but never sum them.

## Original Posts

For original posts by the operator:

- likes, replies, reposts, quotes, bookmarks, and impressions are owned metrics;
- use these for learning and strategy.

## Reports

Every engagement report should include:

- owned original posts count;
- quote posts count;
- reposts count;
- owned-post impressions;
- owned-post likes/replies/reposts/quotes/bookmarks;
- source-post metrics separately for reposted or quoted content;
- clear note when source metrics are excluded from owned aggregates.

## Learning Loop

Only owned metrics should update voice/performance learning by default.

Source metrics can update source-selection learning, for example: "this source was high-signal/popular," but not "the operator's post got 941 reposts."
