"""Redraw Figures 2-5 from the result CSVs in `results/`.

Figure 2: R² by forecast horizon        (results/R2_mean_matrix.csv)
Figure 3: RMSE by forecast horizon      (results/RMSE_mean_matrix.csv)
Figure 4: MAPE by forecast horizon      (results/MAPE_mean_matrix.csv)
Figure 5: RMSE reduction relative to ARIMA, 100 * (1 - RMSE_model / RMSE_ARIMA)

The figures are written to `outputs/figures/` by default so that the published
files in `figures/` are never overwritten. Pass `--results outputs` to plot the
CSVs of a fresh notebook run instead of the published ones.

Usage:
    python code/make_figures.py [--results results] [--out outputs/figures]
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
HORIZONS = [1, 7, 14, 28]

# manuscript label -> (notebook name, colour, line style, marker, bar hatch)
MODELS = {
    "STL-Auto":       ("STL-Auto",             "#0072B2", "-",  "o", ""),
    "STL-EnsWgt":     ("STL-EnsWgt",           "#D55E00", "--", "s", "//"),
    "rSTL-EnsAvg":    ("RobustSTL-EnsAvg",     "#009E73", "-.", "D", ".."),
    "STL-ARIMA-LSTM": ("STL-ARIMA-LSTM",       "#E69F00", ":",  "^", "xx"),
    "ARIMA":          ("ARIMA",                "#7F7F7F", (0, (6, 2)), "v", "--"),
    "TCN (direct)":   ("TCN(direct)",          "#333333", (0, (3, 1.5)), "P", "++"),
}
ENSEMBLES = ["STL-Auto", "STL-EnsWgt", "rSTL-EnsAvg"]

plt.rcParams.update({
    "font.family": "serif", "font.size": 12, "axes.labelsize": 14,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#E5E5E5", "grid.linewidth": 0.8,
    "legend.frameon": False, "savefig.dpi": 300, "savefig.bbox": "tight",
})


def load(results: Path, name: str) -> pd.DataFrame:
    df = pd.read_csv(results / name, index_col="Model")
    df.columns = [int(c) for c in df.columns]
    return df


def line_figure(df: pd.DataFrame, labels: list[str], ylabel: str, path: Path,
                ylim: tuple | None = None, legend_loc: str = "best") -> None:
    fig, ax = plt.subplots(figsize=(10, 6.25))
    for label in labels:
        name, colour, ls, marker, _ = MODELS[label]
        ax.plot(HORIZONS, df.loc[name, HORIZONS], color=colour, linestyle=ls, marker=marker,
                markersize=8, markeredgecolor="white", linewidth=2.2, label=label)
    ax.set_xticks(HORIZONS)
    ax.set_xlabel("Forecast horizon $h$ (days)")
    ax.set_ylabel(ylabel)
    if ylim:
        ax.set_ylim(*ylim)
    ax.legend(ncol=2, loc=legend_loc)
    fig.savefig(path)
    plt.close(fig)


def bar_figure(df: pd.DataFrame, path: Path) -> None:
    labels = list(MODELS)
    width = 0.8 / len(labels)
    fig, ax = plt.subplots(figsize=(10, 6.25))
    for k, label in enumerate(labels):
        name, colour, _, _, hatch = MODELS[label]
        xs = [i + (k - (len(labels) - 1) / 2) * width for i in range(len(HORIZONS))]
        ax.bar(xs, df.loc[name, HORIZONS], width, color=colour, hatch=hatch,
               edgecolor="black", linewidth=0.6, label=label)
    ax.set_xticks(range(len(HORIZONS)), [f"$h={h}$" for h in HORIZONS])
    ax.grid(axis="x", visible=False)
    ax.set_axisbelow(True)
    ax.set_ylabel("RMSE (USD)")
    ax.legend(ncol=3, loc="upper left")
    fig.savefig(path)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Redraw Figures 2-5 from result CSVs.")
    parser.add_argument("--results", type=Path, default=REPO / "results")
    parser.add_argument("--out", type=Path, default=REPO / "outputs" / "figures")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    r2 = load(args.results, "R2_mean_matrix.csv")
    rmse = load(args.results, "RMSE_mean_matrix.csv")
    mape = load(args.results, "MAPE_mean_matrix.csv")
    reduction = 100 * (1 - rmse / rmse.loc["ARIMA"])

    line_figure(r2, list(MODELS), "$R^2$", args.out / "Figure_2.png",
                ylim=(0.5, 1.005), legend_loc="lower left")
    bar_figure(rmse, args.out / "Figure_3.png")
    line_figure(mape, list(MODELS), "MAPE (%)", args.out / "Figure_4.png", legend_loc="upper left")
    line_figure(reduction, ENSEMBLES, "RMSE reduction vs. ARIMA (%)", args.out / "Figure_5.png",
                ylim=(0, None), legend_loc="upper left")

    print("RMSE reduction relative to ARIMA (%):")
    print(reduction.loc[[MODELS[m][0] for m in ENSEMBLES], HORIZONS].round(1).to_string())
    print(f"\nWrote Figures 2-5 to {args.out}")


if __name__ == "__main__":
    main()
