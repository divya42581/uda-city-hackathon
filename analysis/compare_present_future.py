from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PRESENT = ROOT / "analysis" / "risk_present.csv"
FUTURE = ROOT / "analysis" / "risk_future.csv"
DEFAULT_TABLE = ROOT / "analysis" / "risk_present_future_comparison.csv"
DEFAULT_PLOT = ROOT / "docs" / "present_future_comparison.png"


def build_comparison() -> pd.DataFrame:
    present = pd.read_csv(PRESENT)
    future = pd.read_csv(FUTURE)
    cols = [
        "gridiv",
        "name",
        "type",
        "dangerous_heat_hours",
        "hazard",
        "risk_index",
        "risk_rank",
    ]
    df = present[cols].merge(
        future[cols],
        on=["gridiv", "name", "type"],
        suffixes=("_present", "_future"),
    )
    df["dangerous_heat_hours_change"] = (
        df["dangerous_heat_hours_future"] - df["dangerous_heat_hours_present"]
    )
    df["risk_index_change"] = df["risk_index_future"] - df["risk_index_present"]
    df["risk_rank_change"] = df["risk_rank_future"] - df["risk_rank_present"]
    return df.sort_values(
        ["risk_rank_future", "risk_index_future", "dangerous_heat_hours_change"],
        ascending=[True, False, False],
    )


def save_plot(df: pd.DataFrame, out: Path) -> None:
    plot_df = df.sort_values("dangerous_heat_hours_change", ascending=True)
    labels = plot_df["name"] + " (" + plot_df["type"] + ")"

    fig, ax = plt.subplots(figsize=(10, 6.8))
    bars = ax.barh(
        labels,
        plot_df["dangerous_heat_hours_change"],
        color="#b2182b",
        height=0.62,
    )

    ax.set_xlabel("Increase in dangerous-heat hours (future - present)", fontsize=11)
    ax.set_title(
        "Increase in dangerous-heat hours under the future scenario",
        fontsize=14,
        weight="bold",
        pad=14,
    )
    ax.grid(axis="x", color="#dddddd", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", labelsize=10)

    for bar, value in zip(bars, plot_df["dangerous_heat_hours_change"]):
        ax.text(
            value + 4,
            bar.get_y() + bar.get_height() / 2,
            f"+{int(value)}",
            va="center",
            fontsize=9,
        )

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    fig.subplots_adjust(left=0.29, right=0.96, top=0.88, bottom=0.14)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=190)
    print(f"wrote {out}")


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--table-out", type=Path, default=DEFAULT_TABLE)
    parser.add_argument("--plot-out", type=Path, default=DEFAULT_PLOT)
    args = parser.parse_args()

    df = build_comparison()
    args.table_out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.table_out, index=False)
    save_plot(df, args.plot_out)
    print(f"wrote {args.table_out}")


if __name__ == "__main__":
    main()
