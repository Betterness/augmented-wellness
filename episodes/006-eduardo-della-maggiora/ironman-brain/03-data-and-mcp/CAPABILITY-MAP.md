---
title: Betterness Capability Map
tags:
  - ironman-brain/mcp
status: verified-2026-08-09
---

# What the Agent Can Use

This map reflects the verified public Betterness MCP contract on August 9, 2026.
The agent must discover the live tool catalog at runtime because capabilities can
change.

## Available Foundation

| Domain | Verified MCP capability | Ironman Brain use |
|---|---|---|
| Devices | `listConnectedDevices` | Establish source and coverage before analysis |
| Activity | `getActivityData` | Steps, distance, calories, VO2 max, and workout sessions across supported sources |
| Vitals | `getVitals` | Heart rate, HRV, blood pressure, SpO2, glucose, and respiratory rate |
| Sleep | `getSleepData`, `getSleepStages` | Nightly summaries and detailed stage transitions |
| Body composition | `getBodyComposition` | Weight and composition trends |
| Health profile | `getHealthProfile` | Goals, history, preferences, and relevant context |
| Biomarkers | `searchBiomarkers`, `getBiologicalAge` | Lab trends and longitudinal context |
| Lab records | `getUserLabRecords`, `getLabRecordDetail` | Uploaded and ordered laboratory results |

Supported activity sources described by the current MCP include Apple HealthKit,
Strava, Garmin, Peloton, and Wahoo. Connected sources differ by user.

## Product Expansion in Progress

Recent Betterness product work adds richer workout detail, telemetry continuity,
typed metric analysis, correlations, and event-conditioned health experiments.
Those product surfaces should not be described as public MCP tools until they
appear in runtime discovery.

Ironman Brain is ready to use them when exposed, with likely future capabilities
such as:

- detailed workout streams and stages;
- intraday telemetry with source coverage and gaps;
- saved health correlations;
- personal experiments and event context;
- a consolidated training-context query.

Until then, the agent must use verified tools, athlete-authored notes, and honest
coverage statements. It must never fabricate a richer stream from a daily summary.

## Capability Preflight Prompt

> Discover the live Betterness MCP tool catalog. Compare it with this capability
> map. Tell me what is available, what data sources are connected, what date ranges
> have coverage, and which desired analysis cannot yet be supported. Do not fill
> missing capabilities with assumptions.
