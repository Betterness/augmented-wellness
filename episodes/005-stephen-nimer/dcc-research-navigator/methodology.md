# Methodology And Evidence Model

## Purpose

This artifact makes a public cancer-research network easier to understand. It
does not evaluate researchers, recommend care, or calculate the effect of an
individual donation.

## Evidence Tiers

### Tier 1: Explicitly Stated

The source directly names the researcher, institution, research area, event,
or funding relationship.

Permitted language:

- "Faces of the DCC lists..."
- "The public source describes the research as..."
- "The source states that DCC support..."

### Tier 2: Structured From The Source

The artifact groups source language into a cancer area, scientific theme, or
possible relevance category.

Permitted language:

- "This work is mapped to..."
- "The research may be relevant to..."
- "This theme appears across..."

These are navigational classifications, not causal claims.

### Tier 3: External Literature

A publication or external profile can add scientific context about a
researcher or topic. It does not prove DCC funding.

Permitted language:

- "The researcher has also published on..."
- "Related literature examines..."

Required caveat:

- "The available source does not establish that DCC funded this paper."

## Prohibited Shortcuts

Do not infer that:

- a paper authored by a DCC-highlighted researcher was DCC-funded;
- a DCC donation caused a specific discovery or patient outcome;
- a research theme is already a standard treatment;
- a promising trial result applies to every cancer or every patient;
- research education is medical advice.

## Graph Semantics

- `supports`: a source-stated program-to-institution relationship.
- `publicly_highlights`: the researcher appears in the source material.
- `affiliated_with`: the source associates the researcher with the
  institution.
- `works_on`: a mapped cancer area.
- `studies`: a mapped scientific theme.
- `may_impact`: a possible plain-language relevance category.

## Updating The Map

For every new node or edge:

1. Add a source URL and retrieval date.
2. Preserve the source's exact claim.
3. Assign the narrowest valid relationship.
4. Mark interpretive classifications separately.
5. Never upgrade a relationship from "related" to "funded by" without an
   explicit source.

