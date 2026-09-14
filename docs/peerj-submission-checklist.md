# PeerJ Computer Science — data and code availability checklist

Reference: PeerJ [Data and Materials policy](https://peerj.com/about/policies-and-procedures/#data-materials)
and [Author instructions](https://peerj.com/about/author-instructions/cs/).
Verify the wording against the current policy before submitting; this file is a
working checklist, not a substitute for the journal's own text.

## Required

- [ ] **Raw data deposited.** PeerJ requires the raw data underlying the article
      to be made available. Place it in [`../data/raw/`](../data/README.md) with
      its source, retrieval date and licence recorded.
- [ ] **Code deposited.** All analysis code that produced the reported figures,
      tables and statistics goes in [`../code/`](../code/README.md).
- [ ] **Open licence applied.** Content here is CC BY 4.0 and code is MIT —
      both satisfy the requirement for an open licence. Confirm the authors
      agree with this split.
- [ ] **Repository archived with a DOI.** GitHub alone is not a permanent
      archive. Create a release and archive it via
      [Zenodo](https://zenodo.org/) (or Figshare / Dryad) to mint a DOI, then
      cite that DOI in the Data Availability statement and add it to
      [`../CITATION.cff`](../CITATION.cff).
- [ ] **Data Availability statement written** in the manuscript, naming this
      repository and the archived DOI.
- [ ] **Author contributions statement** completed in
      [`../AUTHORS.md`](../AUTHORS.md) and in the submission form.
- [ ] **Competing interests and funding** declared in the manuscript.
- [ ] **Corresponding author confirmed** — Cuong H. Nguyen-Dinh,
      ndhcuong@ufm.edu.vn.

## Strongly recommended

- [ ] Exact package versions pinned in [`../requirements.txt`](../requirements.txt).
- [ ] Random seeds documented — the results are means over ten seeds.
- [ ] Hardware and runtime recorded, so reviewers can judge feasibility.
- [ ] A single entry point (`code/run_all.py`) that regenerates every reported
      number from the raw data.
- [ ] Figure and table files in the repository match the manuscript versions
      one to one, with identical numbering.
- [ ] ORCID iDs added for all three authors in `CITATION.cff` and at submission.

## Completeness against the manuscript

The submission package supplied only Figures 1–4 and Table 3. Before submitting,
confirm that every figure and table cited in the manuscript is present here:

- [ ] Figures 1–4 present — **done**.
- [ ] Table 3 present — **done**.
- [ ] Tables 1 and 2 (and any others) added.
- [ ] Supplemental files added — the `Supplemental/` folder in the submission
      package was empty.
