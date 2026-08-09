---
title: Start Here
tags:
  - ironman-brain/setup
---

# Build Your Ironman Brain

You can set up the first useful version in about 20 minutes. The deeper interview
can continue over several sessions.

## 1. Make This Your Private Vault

Download or clone the episode folder, then copy `ironman-brain` somewhere private.
Open that folder in Obsidian. Do not work from a public Git repository once you
begin adding personal information.

## 2. Choose an AI Workspace

Use any agent that can read and write local Markdown. Examples include Claude,
Codex, ChatGPT with local tooling, OpenClaw, or another MCP-capable system.

Give it this instruction:

> Read `AGENTS.md`, then interview me using
> `01-athlete-context/INTERVIEW-ME.md`. Ask one question at a time. Preserve
> uncertainty and update `01-athlete-context/ATHLETE-PROFILE.md` only after I
> confirm each section.

## 3. Connect Betterness

1. Create or sign in to your account at [betterness.ai](https://betterness.ai).
2. Connect the wearable and health sources you choose.
3. Generate a personal MCP key in Betterness.
4. Configure your AI client using [[../03-data-and-mcp/BETTERNESS-MCP]].
5. Keep the key in the client's credential store or environment configuration.

## 4. Run a Capability Check

Ask the agent:

> Discover the Betterness MCP tools available to me. List my connected devices,
> state which training and health domains have data, and identify coverage gaps.
> Do not interpret performance yet.

The first check should produce a coverage note, not a training recommendation.

## 5. Create Your First Review

Complete [[../02-training-loop/DAILY-CHECK-IN]], then ask the agent to run
[[../02-training-loop/WEEKLY-REVIEW]]. Inspect its source ranges and assumptions.

> [!warning]
> A polished answer can still be wrong. Verify dates, devices, units, and source
> coverage before changing training or health behavior.
