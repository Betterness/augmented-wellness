# Prompts for the DCC Research Navigator

Load the `dcc-research-navigator` folder and its
[`agent-prompt.md`](./dcc-research-navigator/agent-prompt.md) before using these.

## Understand the network

```text
Show me the cancer areas represented in this graph. For each one, explain the
scientific themes in plain language and cite the graph relationships you used.
```

## Follow a research theme

```text
Trace immunology and immunotherapy across the network. Separate researchers,
cancer areas, mechanisms, and possible patient relevance. Do not infer
paper-level DCC funding.
```

## Prepare for a DCC ride

```text
I am riding in the Dolphins Cancer Challenge. Help me choose three parts of
the research map to learn about before the event, then give me one thoughtful
question for a researcher or Sylvester leader.
```

## Read a research claim critically

```text
Evaluate this claim using the methodology in this folder. Tell me what the
available evidence establishes, what remains uncertain, and what source would
be required to make a stronger funding or clinical-impact claim:

[PASTE CLAIM]
```

## Add external literature safely

```text
I found this paper by a researcher in the graph. Summarize its research
question, method, and findings. Label it as related literature unless an
explicit source proves DCC funded this paper:

[PASTE DOI, PMID, ABSTRACT, OR PAPER]
```

## Connect permissioned Betterness context

```text
Use only the Betterness data I explicitly authorized. Keep my personal health
context separate from public research evidence. Help me formulate questions
for my qualified care team; do not diagnose or recommend treatment.
```

