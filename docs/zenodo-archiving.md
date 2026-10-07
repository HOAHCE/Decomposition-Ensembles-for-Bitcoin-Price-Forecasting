# Zenodo archive (DOI) and how to add a new version

PeerJ requires the data and code behind an article to be deposited in a
permanent archive. GitHub is not one — a repository can be renamed, made
private or deleted — so the repository is archived on
[Zenodo](https://zenodo.org/), which stores a snapshot and issues a DOI.

## Current record

| | DOI | Contents |
| :--- | :--- | :--- |
| **Concept DOI** (all versions) | [10.5281/zenodo.22740176](https://doi.org/10.5281/zenodo.22740176) | Always resolves to the newest version. Cite this one in the article and in `CITATION.cff`. |
| Version 1.0.0 (September 2026) | [10.5281/zenodo.22740177](https://doi.org/10.5281/zenodo.22740177) | Early snapshot with Vietnamese notebook comments. **Superseded.** |
| Version 1.1.0 (October 2026) | assigned by Zenodo when the version is published | The version for review (GitHub release `v1.1.0`). |

The record was created by a manual upload of a ZIP of the repository, not by
the Zenodo–GitHub integration. New versions are therefore added **manually, as
a new version of the same record**, so that they share the concept DOI above.
Do not create a fresh upload and do not switch on the GitHub integration for
this repository: either would create a second, unrelated concept DOI.

## Adding a new version

Only the owner of the Zenodo record can do this.

1. **GitHub release.** On GitHub, open *Releases → Draft a new release*:
   tag `v1.1.0` (create it on publish), target `main`, title
   `v1.1.0 — PeerJ resubmission (version for review)`, and publish. Download
   *Source code (zip)* from the release page.
2. **New version on Zenodo.** Log in to Zenodo, open
   <https://zenodo.org/records/22740177> and click **New version**.
3. **Files.** Upload the ZIP from step 1. Do not import the files of the
   previous version.
4. **Metadata.** Fill in the form from [`../.zenodo.json`](../.zenodo.json):

   | Field | Value |
   | :--- | :--- |
   | Resource type | Software |
   | Title | Validation-Guided Decomposition Ensembles for Direct Multi-Horizon Bitcoin Price Forecasting: code, raw data and results |
   | Publication date | date of the release |
   | Creators | Tran Thai, Hoa — University of Economics, Hue University · Manh Le, Thanh — University of Sciences, Hue University · Nguyen-Dinh, Cuong H. — University of Finance and Marketing (contact person) |
   | Description | the `description` field of `.zenodo.json` |
   | Version | 1.1.0 |
   | Licenses | MIT License (code) and Creative Commons Attribution 4.0 International (data, tables, figures, results) |
   | Keywords | the `keywords` of `.zenodo.json` |
   | Related works | *Is supplement to* — URL — `https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting` |

5. **Publish**, then note the new version DOI shown on the record page and
   add it to the table above and to [`../CHANGELOG.md`](../CHANGELOG.md).
6. **Mark the old version.** Open version 1.0.0, click **Edit**, add at the top
   of its description *"Superseded by version 1.1.0. Please use
   https://doi.org/10.5281/zenodo.22740176 (latest version)."* and publish the
   metadata change. Files of a published version cannot be changed, but its
   description can.

## Data availability statement

> The code, raw data and results underlying this article are available on
> GitHub at
> https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting
> and archived on Zenodo at https://doi.org/10.5281/zenodo.22740176
> (version 1.1.0).

## Before each release, check

- [ ] `python code/prepare_data.py --check` and `python code/verify_tables.py`
      pass on `main`.
- [ ] The version number is updated in `CITATION.cff`, `.zenodo.json` and
      `CHANGELOG.md`.
- [ ] Authors, affiliations and the corresponding-author email agree in
      `README.md`, `AUTHORS.md`, `CITATION.cff` and `.zenodo.json`.
