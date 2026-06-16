# Website ↔ Repo Cross-Link Contract

*Augmented Wellness* lives in two places that must always point at each other:

- the **polished episode page** on **betterness.ai/augmentedwellness** (the
  marketing + listening surface), and
- this **GitHub companion repo** (the hands-on lab: kits, prompts, source maps,
  claim notes, agent-readable companion files).

Neither is complete without the other. This contract defines the links each
side owes the other so a listener can always cross from "I just heard it" to
"let me go build it," and back. Treat it as load-bearing: if you add or edit an
episode on either side, satisfy both directions here.

## Direction 1 — Website → Repo

Every episode page on betterness.ai **must** link to that episode's
counterparts in this repo. Specifically, the page should expose links to:

- the **episode artifact** (the buildable kit, e.g. `better-x`);
- the **sources / claim notes** for the episode (`sources/`, where present);
- the **prompts** used in the artifact;
- the **transcript** (`transcript/`, where present);
- the episode's **`companion-agent-page.md`** (the agent-readable index).

Anchor target (Episode 001):

| Target | URL |
|--------|-----|
| Episode 001 folder | https://github.com/Betterness/augmented-wellness/tree/main/episodes/001-martin-varsavsky |
| Artifact (`better-x`) | https://github.com/Betterness/augmented-wellness/tree/main/episodes/001-martin-varsavsky/better-x |
| Companion agent page | https://github.com/Betterness/augmented-wellness/blob/main/episodes/001-martin-varsavsky/companion-agent-page.md |

## Direction 2 — Repo → Website + listening + brand

Every episode in this repo **must** link back out. Each episode's `README.md`
(and its `companion-agent-page.md`) carries the full set:

- the **full episode page** on betterness.ai,
- **YouTube**, **Apple Podcasts**, **Spotify**, **Amazon Music**,
- **Betterness** (the company), and
- **Betti** (the product/agent) *only when it's actually relevant to that
  episode* — don't add it by reflex.

### Canonical URLs (Episode 001 — Martin Varsavsky)

| Destination | URL |
|-------------|-----|
| Episode page | https://betterness.ai/augmentedwellness/001-martin-varsavsky |
| Show page | https://betterness.ai/augmentedwellness |
| YouTube | https://youtu.be/l2tLdSlamIc |
| Apple Podcasts | https://podcasts.apple.com/podcast/id1896935053 |
| Spotify | https://open.spotify.com/show/033zAkDQc1NpADnqP4OFzh |
| Amazon Music | https://music.amazon.com/podcasts/d3fcfba2-fded-460f-b818-1937d04d47db/augmented-wellness |
| Betterness | https://betterness.ai |
| Betti *(only when relevant)* | https://betterness.ai |

> The Apple / Spotify / Amazon links above are **show-level** feeds. As
> per-episode deep links become available, add them to the episode without
> dropping the show-level fallback.

## Naming on the page (public facts only)

On the website episode page and in this repo's README/episode docs you may name
the public facts: host **Demian Bellumio**, producer **Betterness One** /
**Betterness**, guest **Martin Varsavsky**. Inside a kit directory (e.g.
`better-x/`) name **none** of them — kits stay generic (see
[`../AGENTS.md`](../AGENTS.md)).

## Adding a new episode (checklist)

When episode `NNN` ships, do all of the following before calling it done:

- [ ] Repo: create `episodes/NNN-<guest-slug>/` with `README.md`, the
      artifact, and a `companion-agent-page.md`.
- [ ] Repo: the episode `README.md` links to page + YouTube + Apple + Spotify +
      Amazon + Betterness (+ Betti only if relevant).
- [ ] Repo: add the row to the root [`README.md`](../README.md) episode table.
- [ ] Website: the episode page links to the repo folder, artifact, sources,
      prompts, transcript, and `companion-agent-page.md`.
- [ ] Both: links resolve (no 404s) and the URLs match this contract.

## When a URL changes

Update **both** sides in the same change, and update the canonical table above
so this file stays the single source of truth. A one-sided link edit is a bug.
