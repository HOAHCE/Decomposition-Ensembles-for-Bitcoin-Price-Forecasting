# PeerJ Computer Science — data and code availability checklist

Reference: PeerJ [Data and Materials policy](https://peerj.com/about/policies-and-procedures/#data-materials)
and [Author instructions](https://peerj.com/about/author-instructions/cs/).
Verify the wording against the current policy before submitting; this file is a
working checklist, not a substitute for the journal's own text.

## Required

- [x] **Raw data deposited** — [`../data/raw/BTC_USD_daily_2014-09-17_2025-06-11.csv`](../data/README.md),
      3,921 daily records. Still to record: the download source, the retrieval
      date and the terms of use of that source.
- [x] **Code deposited** — [`../code/decomposition_ensemble_experiments.ipynb`](../code/README.md),
      committed with its cell outputs intact, plus the extraction script that
      produced [`../results/`](../results/README.md).
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
      TensorFlow is pinned at 2.20.0 from the notebook's own output; the rest came
      from the Colab image and still need pinning.
- [x] Random seeds documented — 42–51, set in the notebook's `CONFIG` cell.
- [x] Hardware recorded — Google Colab, T4 GPU, roughly 485 s per seed.
- [x] A single entry point — the notebook runs end to end from the raw CSV;
      two `CONFIG` paths must be changed to run it outside Colab.
- [ ] Figure and table files in the repository match the manuscript versions
      one to one, with identical numbering.
- [ ] ORCID iDs added for all three authors in `CITATION.cff` and at submission.

## Completeness against the manuscript

The submission package supplied only Figures 1–4 and Table 3. Before submitting,
confirm that every figure and table cited in the manuscript is present here:

- [x] Figures 1–4 present.
- [x] Table 3 present, and cross-checked against `results/RMSE_mean_matrix.csv`:
      75 of 76 values agree exactly. Fix the one rounding slip in the manuscript —
      STL-ARIMA-LSTM at *h* = 14 is 3,249, printed as 3,250.
- [ ] Tables 1 and 2 (and any others) added.
- [ ] Supplemental files added — the `Supplemental/` folder in the submission
      package was empty.
