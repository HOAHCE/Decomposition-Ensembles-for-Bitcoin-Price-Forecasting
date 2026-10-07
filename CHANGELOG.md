# Changelog

All versions are archived on Zenodo under the concept DOI
[10.5281/zenodo.22740176](https://doi.org/10.5281/zenodo.22740176), which always
resolves to the latest version.

## 1.1.0 — 7 October 2026 (version for review)

[10.5281/zenodo.23202090](https://doi.org/10.5281/zenodo.23202090) · GitHub
release [`v1.1.0`](https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting/releases/tag/v1.1.0).
This version supersedes 1.0.0 and is the one that accompanies the PeerJ
Computer Science submission. No computation was changed: the computed results
are identical to version 1.0.0.

### Language
- The experiment notebook `code/decomposition_ensemble_experiments.ipynb` is
  entirely in English: markdown text, code comments, docstrings, printed
  messages, table headers and plot labels, including the stored outputs. In
  version 1.0.0 the comments and text were still in Vietnamese.

### Documentation
- `README.md` rewritten with the sections requested by the journal: title,
  description, dataset information, code information, usage instructions,
  requirements, methodology, citations, and license and contribution
  guidelines.
- `data/README.md` (data dictionary), `code/README.md`, `results/README.md`,
  `tables/README.md` and `figures/README.md` updated.

### Data
- Raw data kept in `data/raw/` (Yahoo Finance `BTC-USD` data, unmodified from
  the file used in the study).
- Processed data added in `data/processed/`: the curated OHLCV series with the
  development/test split, and the log inputs with STL and robust STL components.

### Code
- Notebook paths made repository-relative (Google Colab still supported) and a
  `QUICK_MODE` switch added for a short end-to-end test.
- New scripts: `prepare_data.py` (raw → processed data, with `--check`),
  `descriptive_statistics.py` (Table 1), `verify_tables.py` (checks Tables 1
  and 3–7) and `make_figures.py` (Figures 2–5).

### Results, tables and figures
- Tables 1–7 added as PeerJ-format `.docx` files with Markdown renderings, and
  Figure 5 added.
- Table 3: STL-ARIMA-LSTM at h = 14 corrected from 3,250 to 3,249 (rounding of
  3,249.4973).
- `results/*.csv` re-exported with English column names (values unchanged);
  `results/descriptive_statistics.csv` added.

### Metadata
- Title aligned with the article; all three authors listed with their
  affiliations; corresponding-author email corrected to cuongndh@ufm.edu.vn.
- Zenodo DOI recorded in `README.md`, `CITATION.cff` and `LICENSE-DATA.md`.

## 1.0.0 — September 2026 (superseded)

10.5281/zenodo.22740177. Initial
snapshot: experiment notebook with Vietnamese comments, raw data, extracted
result CSVs, Figures 1–4 and Table 3. **Superseded by version 1.1.0; please do
not use it for review.**
