# Archiving this repository on Zenodo to mint a DOI

PeerJ requires that the data and code behind an article be deposited somewhere
permanent. GitHub is not a permanent archive — a repository can be renamed,
made private or deleted — so the repository is archived on
[Zenodo](https://zenodo.org/), which stores a snapshot and issues a DOI that
resolves forever.

**The order of these steps matters.** Zenodo only archives releases created
*after* the repository is switched on in its GitHub settings. A release made
before that is invisible to Zenodo and has to be deleted and recreated.

## Prerequisites — already satisfied

| Requirement | Status |
| :--- | :--- |
| Repository is public | Yes — Zenodo cannot see private repositories. |
| An open licence is present | Yes — MIT (`LICENSE`) for code, CC BY 4.0 (`LICENSE-DATA.md`) for data, figures and tables. |
| Deposit metadata is in the repository | Yes — [`../.zenodo.json`](../.zenodo.json): title, all three authors with affiliations, description, keywords and licence. Zenodo reads this file at release time instead of guessing from the repository. |
| Archiving happens from the default branch | Yes — `claude/adoring-dijkstra-5l61zx` is the repository's default branch. |

## Step 1 — Connect Zenodo to GitHub

Only the repository owner (the `HOAHCE` GitHub account) can do this.

1. Go to <https://zenodo.org/> and select **Log in → GitHub**.
2. Authorise Zenodo when GitHub asks. Zenodo needs permission to read your
   repositories and to add a release webhook.

## Step 2 — Switch the repository on

1. Go to <https://zenodo.org/account/settings/github/>.
2. Find **HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting** in the
   list. If it is not there, use **Sync now** — newly created repositories can
   take a few minutes to appear.
3. Set its toggle to **ON**.

Zenodo installs a webhook on the repository at this point. Nothing is archived
yet.

## Step 3 — Create a GitHub release

Only now create the release. Suggested values for the first one:

| Field | Value |
| :--- | :--- |
| Tag | `v1.0.0` |
| Target | `claude/adoring-dijkstra-5l61zx` (the default branch) |
| Title | `v1.0.0 — PeerJ submission` |

GitHub notifies Zenodo, which downloads a snapshot of the repository at that tag
and mints a DOI. This usually takes a minute or two; the deposit then appears at
<https://zenodo.org/account/settings/github/> next to the repository.

## Step 4 — Record the DOI

Zenodo issues **two** DOIs, and the difference matters:

| DOI | Meaning | Where to use it |
| :--- | :--- | :--- |
| **Concept DOI** | Always resolves to the newest version of the deposit. | The Data Availability statement in the manuscript, and `CITATION.cff`. |
| **Version DOI** | Pins version 1.0.0 specifically. | Anywhere the exact reviewed snapshot must be cited. |

Cite the **concept DOI** in the article, so the link stays correct if a revision
is released during review.

Then:

1. Add it to [`../CITATION.cff`](../CITATION.cff) — uncomment the `doi:` line and
   fill in the concept DOI.
2. Add the Zenodo DOI badge to the top of [`../README.md`](../README.md):

   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
   ```

3. Write the Data Availability statement in the manuscript, for example:

   > The data and code underlying this article are available on GitHub at
   > https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting
   > and are archived on Zenodo at https://doi.org/10.5281/zenodo.XXXXXXX.

## If the manuscript changes during review

Push the changes, then create a new release (`v1.1.0`, and so on). Zenodo
archives it automatically as a new version under the same concept DOI, so the
link printed in the article keeps working.

## Before releasing, check

- [ ] ORCID iDs added for all three authors in `.zenodo.json` (field `orcid` on
      each creator) — optional, but it links the deposit to the authors' records.
- [ ] Author name order in `.zenodo.json` verified. The entries use
      `"Family, Given"` form matching the manuscript byline; confirm that the
      family names are split correctly.
- [ ] Tables 1 and 2 and any remaining supplemental files added, so the archived
      snapshot is the complete deposit.
