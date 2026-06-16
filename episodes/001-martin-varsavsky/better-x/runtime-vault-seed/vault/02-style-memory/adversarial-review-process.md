# Editorial Review Process

Status: required for public-facing actions.

better-x uses separate roles so one model does not draft, approve, and execute its own work.

## Roles

1. **Writer**
   - Preferred: a fast non-reasoning model when configured.
   - Fallback: configured fast writer model.
   - Job: produce a platform-native draft and short rationale.

2. **Mechanical Reviewer**
   - Preferred: a fast low-cost model.
   - Job: catch numbered lists, repeated templates, awkward capitalization, all-lowercase voice, staccato fragment stacks, missing required links, length problems, and automation tells.

3. **Editor / Adversarial Reviewer**
   - Preferred: a strong reasoning/editorial model.
   - Job: improve the draft, explain the changes, and look for reasons to reject it.

4. **Policy Gate**
   - Job: enforce STOP, action policy, reputation rules, sensitive-claims policy, privacy rules, untrusted-input policy, cadence, and action-type integrity.

## Required Editorial Artifact

Every public action must write a JSON artifact with:

- source or prompt;
- writer model, raw writer output, and writer rationale;
- mechanical reviewer result;
- editor model, edited output, and editorial rationale;
- remaining objections;
- final selected text;
- operator approval reference;
- policy and safety checks;
- exact action command.

## Why The Editor Edits Instead Of Only Reviews

A pass/fail reviewer can let mediocre drafts through. The editor must add value:

- make the post more specific;
- show the operator's actual thinking;
- remove generic positioning;
- reduce legal, sensitive-claims, reputation, and privacy risk;
- preserve the operator's voice;
- explain what changed so the learning loop can improve.

## Decision Values

- `approve`: ready for operator approval or execution if already authorized.
- `approve_with_notes`: acceptable, but include notes.
- `request_revision`: not good enough yet; revise and rerun checks.
- `reject`: archive and learn from the rejection.
- `block`: policy or safety issue; do not publish.

## Learning Loop

After operator approval, edit, rejection, or performance review:

- append lessons to `vault/02-style-memory/edits-and-lessons.md`;
- add strong negative patterns to `negative-examples.md`;
- add strong positive patterns to `positive-examples.md`;
- update future prompts and publication artifacts.
