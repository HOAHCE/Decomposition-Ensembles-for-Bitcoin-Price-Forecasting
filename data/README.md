# Data

> **Status: not yet deposited.** No data files were present in the
> `PeerJ_Computer_Science_Submission_Package` folder this repository was built
> from. PeerJ requires that the raw data underlying the article be made
> available, so this directory must be populated before submission.

## Layout

| Directory | Contents |
| :--- | :--- |
| `raw/` | The daily Bitcoin OHLCV series, 2014–2025, exactly as downloaded — unmodified, with the retrieval date recorded. |
| `processed/` | Derived files produced by the code: log-transformed series, the STL / rSTL components, and the chronological development / validation / test splits. |

## Documentation to supply with the data

For each file in `raw/`, record in this README:

- the exact source (provider, API endpoint or URL) and the retrieval date;
- the licence or terms of use of that source, and confirmation that
  redistribution here is permitted;
- the column dictionary (name, units, dtype), the date range and the row count;
- how missing values and exchange outages were handled.

The test period is described in Table 3 as the final 365 days; state the exact
start and end dates of the development, validation and test blocks here so the
splits can be reconstructed independently.

If the raw series cannot be redistributed for licensing reasons, place a
download script in [`../code/`](../code) that reconstructs it byte for byte, and
record the checksum of the expected file here.
