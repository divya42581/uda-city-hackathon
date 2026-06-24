from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis" / "risk_present.csv"
OUT = ROOT / "docs" / "present_hazard_risk_bar.png"


def main() -> None:
    df = pd.read_csv(DATA).sort_values(["risk_rank", "risk_index"], ascending=[True, False])
    df["label"] = df["name"] + " (" + df["type"] + ")"

    y = range(len(df))
    height = 0.36

    fig, ax = plt.subplots(figsize=(10, 6.6))
    ax.barh(
        [i - height / 2 for i in y],
        df["hazard"],
        height=height,
        label="Heat hazard",
        color="#e66101",
    )
    ax.barh(
        [i + height / 2 for i in y],
        df["risk_index"],
        height=height,
        label="Final risk",
        color="#2c3e50",
    )

    ax.set_yticks(list(y))
    ax.set_yticklabels(df["label"], fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0, 1.05)
    ax.set_xlabel("Scaled score (0 = lowest, 1 = highest)", fontsize=11)
    ax.set_title(
        "Present heat hazard and final risk by UDA-city neighbourhood",
        fontsize=14,
        weight="bold",
        pad=14,
    )
    ax.grid(axis="x", color="#dddddd", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.17), ncol=2, frameon=False)

    for i, (hazard, risk) in enumerate(zip(df["hazard"], df["risk_index"])):
        ax.text(min(hazard + 0.025, 1.02), i - height / 2, f"{hazard:.2f}", va="center", fontsize=9)
        ax.text(min(risk + 0.025, 1.02), i + height / 2, f"{risk:.2f}", va="center", fontsize=9)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    fig.subplots_adjust(left=0.29, right=0.97, top=0.88, bottom=0.18)
    fig.savefig(OUT, dpi=190)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
