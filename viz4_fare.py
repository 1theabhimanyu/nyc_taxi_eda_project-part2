import os
import pandas as pd
import matplotlib.pyplot as plt
from config import PLOTS_DIR

def plot_fare_anatomy(df: pd.DataFrame):
    """Renders a stacked horizontal bar chart breaking down trip revenue by borough."""
    borough_rev = df.groupby("pickup_borough", observed=True)[["fare", "tip", "tolls"]].mean()
    borough_rev = borough_rev.loc[["Queens", "Brooklyn", "Bronx", "Manhattan"]].copy()
    
    borough_total = df.groupby("pickup_borough", observed=True)["total"].mean()
    borough_rev["surcharges"] = (borough_total - borough_rev.sum(axis=1)).clip(lower=0)

    ax = borough_rev[["fare", "tip", "tolls", "surcharges"]].plot(
        kind="barh", stacked=True, figsize=(11, 5.5),
        color=["#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd"], edgecolor="black", width=0.65
    )

    for idx, total_val in enumerate(borough_rev.sum(axis=1)):
        ax.text(total_val + 0.5, idx, f"${total_val:.2f}", va="center", fontweight="bold", fontsize=10)

    plt.title("Visualization 4: Anatomy of a Taxi Fare — Revenue Breakdown by Pickup", fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Average Amount per Trip ($ USD)", fontsize=11, fontweight="bold")
    plt.ylabel("Pickup Borough", fontsize=11, fontweight="bold")
    plt.xlim(0, max(borough_rev.sum(axis=1)) * 1.15)
    plt.legend(["Base Meter Fare", "Recorded Tip", "Bridge/Tunnel Tolls", "Taxes & Surcharges"], loc="lower right")

    save_path = os.path.join(PLOTS_DIR, "week2_viz4_fare_anatomy.png")
    plt.tight_layout()
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {save_path}")