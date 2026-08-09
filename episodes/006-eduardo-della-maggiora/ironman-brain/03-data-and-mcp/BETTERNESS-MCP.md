---
title: Betterness MCP Setup
tags:
  - ironman-brain/mcp
  - betterness
---

# Connect Betterness

Betterness can provide permissioned health context to an MCP-compatible AI
without placing raw exports or API keys in this vault.

## Before Connecting

1. Create or sign in to your account at [betterness.ai](https://betterness.ai).
2. Connect only the wearable and health sources you choose.
3. Generate a personal MCP key.
4. Treat that key like a password.

## MCP Server

- URL: `https://api.betterness.ai/mcp`
- Authentication header: `Authorization: Bearer <YOUR_BETTERNESS_MCP_KEY>`
- Personal keys begin with `bk_`.

Use your AI client's secure MCP configuration or credential store. Never paste
the real key into a prompt, screenshot, note, issue, or Git commit.

### Generic Configuration Shape

```json
{
  "mcpServers": {
    "betterness": {
      "url": "https://api.betterness.ai/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_BETTERNESS_MCP_KEY>"
      }
    }
  }
}
```

The exact file and syntax vary across Claude, Codex, ChatGPT, OpenClaw, Cursor,
and other clients. Use the client's current MCP documentation.

## First Connection Test

Ask the agent to:

1. Discover available Betterness MCP tools.
2. Call `listConnectedDevices`.
3. Report available sources and date coverage without interpreting performance.
4. Query a short, explicit range with the athlete's IANA timezone.
5. Cite the tools, dates, timezone, and sources returned.

## Recommended Pull Cadence

| Context | Typical window | Why |
|---|---:|---|
| Daily decision | 7 days + 28-day comparison | Recent load with baseline context |
| Weekly review | 7, 28, and sometimes 90 days | Separate noise from a persistent pattern |
| Race block | Block start through today | Keep the review tied to the actual build |
| Biomarkers | Latest plus comparable prior tests | Labs usually move on a slower cadence |
| Body composition | Trend, not daily reaction | Reduce noise and harmful overinterpretation |

> [!important]
> MCP access is permissioned context, not permission for the agent to make medical
> decisions or silently change a training plan.
