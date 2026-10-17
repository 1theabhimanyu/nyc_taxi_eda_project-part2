import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import PLOTS_DIR

def plot_commuter_flow(df: pd.DataFrame):
    """Generates an origin-destination percentage matrix to map commuter corridors."""
    borough_order = ["Manhattan", "Queens", "Brooklyn", "Bronx"]
    df_flow = df[df["pickup_borough"].isin(borough_order) & df["dropoff_borough"].isin(borough_order)]

    flow_counts = pd.crosstab(df_flow["pickup_borough"], df_flow["dropoff_borough"])
    flow_counts = flow_counts.reindex(index=borough_order, columns=borough_order, fill_value=0)
    flow_pct = flow_counts.div(flow_counts.sum(axis=1), axis=0) * 100

    plt.figure(figsize=(9, 6.5))
    ax = sns.heatmap(
        flow_pct, cmap="Blues", annot=True, fmt=".1f",
        cbar_kws={"label": "Share of Pickups Ending in Destination Borough (%)"},
        linewidths=1.5, annot_kws={"size": 11, "weight": "bold"}
    )

    for t in ax.texts:
        t.set_text(t.get_text() + "%")

    plt.title("Visualization 2: Inter-Borough Commuter Flows (Origin vs. Destination %)", fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Destination (Dropoff Borough)", fontsize=11, fontweight="bold")
    plt.ylabel("Origin (Pickup Borough)", fontsize=11, fontweight="bold")
    plt.yticks(rotation=0)

    save_path = os.path.join(PLOTS_DIR, "week2_viz2_borough_flow_matrix.png")
    plt.tight_layout()
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {save_path}")