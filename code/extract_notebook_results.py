"""Extract the machine-readable result tables from the experiment notebook.

The notebook `decomposition_ensemble_experiments.ipynb` writes its result tables
to a Google Drive folder while it runs, but it also stores every table in its own
cell outputs. This script reads those stored outputs and writes them to
`results/` as CSV, so the numbers behind the manuscript are available without
re-running the (GPU-hours long) experiment.

Only tables that pandas rendered in full are exported. Two tables — the per-seed
aggregate (`agg`) and the seed-averaged metrics (`savg`), both 76 rows — were
truncated by pandas' display limit when the notebook was saved, so they cannot be
recovered here; re-run the notebook to regenerate them.

Usage:
    python code/extract_notebook_results.py
"""

from __future__ import annotations

import io
import json
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
NOTEBOOK = REPO / "code" / "decomposition_ensemble_experiments.ipynb"
OUT_DIR = REPO / "results"

# (cell index, output index) -> output file name.
# Indices refer to the notebook as committed; see the module docstring.
EXPORTS = {
    (19, 2): "RMSE_mean_matrix.csv",
    (19, 4): "MAPE_mean_matrix.csv",
    (19, 6): "R2_mean_matrix.csv",
    (22, 1): "DM_seedavg.csv",
    (23, 1): "MCS_h1.csv",
    (23, 3): "MCS_h7.csv",
    (23, 5): "MCS_h14.csv",
    (23, 7): "MCS_h28.csv",
    (25, 1): "wilcoxon_seed.csv",
    (27, 0): "best_per_horizon.csv",
    (27, 2): "overall_rank.csv",
}


def _declared_rows(output: dict) -> int | None:
    """Row count Colab recorded for the DataFrame, if it recorded one."""
    meta = output.get("data", {}).get(
        "application/vnd.google.colaboratory.intrinsic+json", {}
    )
    if "summary" in meta:
        return json.loads(meta["summary"])["rows"]
    return None


def _flatten(levels: tuple, is_first: bool) -> str:
    """Collapse one MultiIndex column label into a single name.

    A pivot table rendered to HTML comes back with two header rows: the name of
    the column index (e.g. `h`) over the name of the row index (e.g. `Model`),
    and pandas fills the empty half of every other label with `Unnamed: N`. The
    leading column is the row index, so its name lives in the lower level; for
    every other column the name lives in the upper level.
    """
    named = [str(x) for x in levels if not str(x).startswith("Unnamed")]
    if not named:
        return str(levels[0])
    return named[-1] if is_first else named[0]


def _tidy(df: pd.DataFrame) -> pd.DataFrame:
    """Drop the artefacts of parsing a rendered DataFrame back out of HTML."""
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            _flatten(label, i == 0) for i, label in enumerate(df.columns)
        ]
    # A flat frame carries its integer index as a leading "Unnamed: 0" column.
    return df.loc[:, [c for c in df.columns if not str(c).startswith("Unnamed: 0")]]


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cells = notebook["cells"]
    OUT_DIR.mkdir(exist_ok=True)

    for (cell_idx, out_idx), name in EXPORTS.items():
        output = cells[cell_idx]["outputs"][out_idx]
        html = "".join(output["data"]["text/html"])
        df = _tidy(pd.read_html(io.StringIO(html))[0])

        declared = _declared_rows(output)
        if declared is not None and len(df) != declared:
            raise SystemExit(
                f"{name}: table was truncated when the notebook was saved "
                f"({len(df)} of {declared} rows); refusing to write a partial file."
            )

        df.to_csv(OUT_DIR / name, index=False)
        print(f"{name:<26} {df.shape[0]:>3} rows x {df.shape[1]} cols")


if __name__ == "__main__":
    main()
