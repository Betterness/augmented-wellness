# DCC Research Navigator

The Dolphins Cancer Challenge is visible as a ride. Behind it is a much larger
research ecosystem.

This artifact maps the researchers, cancer areas, and scientific themes
publicly highlighted by Faces of the DCC. It is designed for people who want
to understand what the community is supporting without pretending that every
research relationship can be reduced to a single headline or paper.

## What Is Included

- `dcc-research-map.html`: open locally for a visual overview.
- `dcc-research-map.md`: a Mermaid map that renders in compatible Markdown
  tools.
- `data/graph-data.json`: 68 nodes and 215 typed relationships for use in an
  LLM, notebook, graph tool, or local agent.
- `data/researcher-source-index.json`: all 35 entries in the public Research
  Funding List, with roles, affiliations, and source provenance.
- `agent-prompt.md`: turn the data into a research navigator in Claude,
  ChatGPT, Codex, or another capable LLM.
- `questions.md`: high-value questions for riders, donors, patients, families,
  and researchers.
- `methodology.md`: the evidence model and the claims the artifact permits.
- `sources.md`: source provenance and update boundaries.

## Three Ways To Use It

### 1. Explore The Map

Download this folder and open `dcc-research-map.html`. Use it to see which
cancer areas have multiple researchers and where themes such as clinical
trials, immunotherapy, precision radiation, prevention, and drug resistance
appear across the network.

### 2. Create Your Own Research Navigator

Upload `data/graph-data.json`, `methodology.md`, and `agent-prompt.md` to an
LLM project. Ask it to explain a research area in plain language, compare
themes, or help prepare questions for a physician-scientist.

### 3. Connect It To Betterness

Use the same files as a knowledge resource for a Betterness agent. The public
map supplies research context; your own Betterness account can add the health,
wearable, lab, and lifestyle context you explicitly choose to share. The agent
must keep public research evidence separate from private personal data and
must never turn research education into diagnosis.

## Start Here

Try these questions:

1. Which DCC-highlighted research areas are closest to patient-facing clinical
   trials?
2. Which researchers work on prevention versus treatment?
3. What does precision radiation mean for a patient or donor?
4. What evidence would be needed before saying DCC funded a particular paper?
5. What should I ask Dr. Nimer about the path from philanthropic support to a
   clinical advance?

## Evidence Rule

An edge in this graph can mean that DCC publicly highlights a researcher or
that a researcher works in a stated area. It does **not** prove that DCC funded
a particular publication, grant, experiment, drug, or patient outcome.

Read [methodology.md](methodology.md) before extending the graph.
