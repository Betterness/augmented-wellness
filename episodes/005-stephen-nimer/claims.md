# Episode 005 - Claim Notes

What this package asserts, how each assertion is grounded, and what it does not
establish.

## Claim ledger

| # | Claim | Status | Grounding | Boundary |
|---|---|---|---|---|
| 1 | Dr. Stephen Nimer leads Sylvester Comprehensive Cancer Center. | GROUNDED | `sources.md` S1-S2 | Public professional role. |
| 2 | The episode describes Sylvester's growth from a local powerhouse to an NCI-designated national cancer center. | GUEST_OPINION / GROUNDED CONTEXT | Episode 24:59-25:50; `sources.md` S2 | The episode language is Dr. Nimer's framing. |
| 3 | Dr. Nimer says every dollar raised for the DCC goes directly to Sylvester for cancer research and care. | GUEST_OPINION | Episode 25:10-25:31 | Attribute this wording to Dr. Nimer unless independently citing DCC financial reporting. |
| 4 | The episode discusses AI-assisted drug design as an emerging part of cancer research. | GUEST_OPINION / PARAPHRASE | Episode 28:33-29:04 | Not a claim that every AI-designed drug is safe, effective, or clinically available. |
| 5 | Dr. Nimer says a doctor's first role is to listen. | GROUNDED QUOTE | Episode 37:05-37:28 | A statement of clinical philosophy. |
| 6 | The public graph contains 68 nodes and 215 typed relationships. | GROUNDED | `dcc-research-navigator/data/graph-data.json` | Counts describe this artifact, not the entire Sylvester research enterprise. |
| 7 | The graph represents all 35 entries in the public Research Funding List, 14 mapped cancer areas, and 11 scientific themes. | GROUNDED / STRUCTURED | `sources.md` S3; graph data; researcher source index | Cancer areas and themes are navigational classifications. |

## Health and research boundaries

| Topic | What is supported here | What is not claimed |
|---|---|---|
| Cancer advances | The episode discusses progress in immunotherapy, pancreatic-cancer research, and AI-assisted drug design. | No treatment recommendation, prognosis, or universal cure claim. |
| DCC relationships | Faces of the DCC publicly connects DCC, Sylvester, and the listed researchers or research areas. | No paper, grant, drug, or patient outcome is labeled DCC-funded without an explicit source. |
| Personal data | A permissioned Betterness agent may combine public research context with data a person chooses to connect. | The graph does not diagnose or determine whether research applies to an individual. |

## Deliberately excluded

- Paper-level DCC funding attribution without an explicit source.
- Claims that a donation caused a specific discovery or patient outcome.
- Rankings of researchers, cancers, treatments, or institutions.
- Medical recommendations derived from the graph.

Nothing here is medical advice.
