# Attribution

The persona-builder in this directory is **adapted, with gratitude, from the
Personal Context Portfolio** — a structured, markdown-first approach to giving any
AI agent a portable representation of who you are, which was shared and discussed on
the **AI Daily Brief** podcast.

## What we borrowed

- The core idea: a person's context as a set of small, human- and machine-readable
  markdown files that any agent can ingest — "an operating manual for any AI that
  works for you."
- The **interview-driven** way of building it: an interviewer agent that asks
  focused questions one at a time, drafts each file, and runs a reaction pass with
  the user before moving on.
- The discipline of their interview protocol: one question per message, push for
  concrete examples, keep files dense and short, treat them as living documents.

## What we changed, and why

The Personal Context Portfolio is general-purpose — ten files that serve any agent
for any task. better-x has one narrow job: drafting posts for a **guarded, disclosed
X agent** (the "Pedro" pattern Martin Varsavsky describes in Augmented Wellness 001).
So our [`interview-protocol.md`](./interview-protocol.md):

- narrows the interview to **voice fidelity** and the **disclosure / safety posture**
  rather than full work context;
- writes into better-x's **existing vault** (`runtime-vault-seed/vault/01-person/`
  and `02-style-memory/`) instead of producing standalone files; and
- folds the hard rules into the runtime's control layer (`vault/00-control/`) so the
  publication gate enforces them, not just the draft.

## License

The Personal Context Portfolio is published under the **MIT License** ("fork it,
customize it, use it however you want"), which is what makes this adaptation
possible. better-x is likewise MIT (see the repo root [`LICENSE`](../../../../LICENSE)).

If you find this useful, go look at the original — it is excellent, and a general
context portfolio is worth having well beyond posting on X.
