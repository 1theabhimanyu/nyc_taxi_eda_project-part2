import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import PLOTS_DIR

def plot_congestion_penalty(df: pd.DataFrame):
    """Creates a joint hexbin plot contrasting trip distance vs. speed and duration."""
    g = sns.jointplot(
        data=df[df["distance"] <= 20],
        x="distance", y="trip_duration_mins",
        kind="hex", cmap="viridis", height=7.5,
        marginal_kws=dict(bins=35, fill=True, color="#2b83ba")
    )

    x_vals = np.linspace(0.1, 20, 100)
    g.ax_joint.plot(x_vals, (x_vals / 10.0) * 60, "r--", linewidth=1.8, label="10 MPH (Gridlock Regime)")
    g.ax_joint.plot(x_vals, (x_vals / 25.0) * 60, "g--", linewidth=1.8, label="25 MPH (Express Regime)")

    g.ax_joint.set_ylim(0, 80)
    g.ax_joint.set_xlabel("Trip Distance (Miles)", fontsize=11, fontweight="bold")
    g.ax_joint.set_ylabel("Trip Duration (Minutes)", fontsize=11, fontweight="bold")
    g.ax_joint.legend(loc="upper left", frameon=True)

    plt.subplots_adjust(top=0.92)
    g.fig.suptitle("Visualization 3: The Congestion Penalty — Trip Distance vs. Duration & Speed", fontsize=13, fontweight="bold")

    save_path = os.path.join(PLOTS_DIR, "week2_viz3_congestion_jointplot.png")
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {save_path}")