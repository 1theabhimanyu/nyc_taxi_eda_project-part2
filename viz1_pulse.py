import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import PLOTS_DIR

def plot_temporal_pulse(df: pd.DataFrame):
    """Generates a 2D heatmap showing weekly vs. weekend transit rhythms."""
    temporal_pivot = df.pivot_table(
        index="day_of_week", columns="pickup_hour", values="total", aggfunc="count", fill_value=0
    )

    plt.figure(figsize=(14, 5.5))
    sns.heatmap(
        temporal_pivot, cmap="YlOrRd", annot=True, fmt="d",
        cbar_kws={"label": "Total Number of Trips"}, linewidths=0.5, annot_kws={"size": 8}
    )

    plt.title("Visualization 1: The Pulse of NYC Transit — Hourly Ride Demand Across the Week", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Hour of Day (0 = Midnight, 12 = Noon, 23 = 11:00 PM)", fontsize=11, fontweight="bold")
    plt.ylabel("Day of the Week", fontsize=11, fontweight="bold")
    plt.yticks(rotation=0)

    save_path = os.path.join(PLOTS_DIR, "week2_viz1_temporal_heatmap.png")
    plt.tight_layout()
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {save_path}")