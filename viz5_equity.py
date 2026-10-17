import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import PLOTS_DIR

def plot_payment_equity(df: pd.DataFrame):
    """Draws a split violin plot exposing tip disparities and bimodal distributions."""
    df_violin = df[
        df["pickup_borough"].isin(["Manhattan", "Queens", "Brooklyn", "Bronx"]) & (df["total"] <= 85)
    ].copy()
    
    if hasattr(df_violin["pickup_borough"], "cat"):
        df_violin["pickup_borough"] = df_violin["pickup_borough"].cat.remove_unused_categories()

    plt.figure(figsize=(12, 6))
    sns.violinplot(
        data=df_violin, x="pickup_borough", y="total", hue="payment",
        split=True, inner="quart", palette={"credit card": "#4daf4a", "cash": "#ff7f00"}, cut=0
    )

    plt.title("Visualization 5: Total Trip Cost Distribution by Borough & Payment Method", fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Pickup Borough", fontsize=11, fontweight="bold")
    plt.ylabel("Total Charged Amount ($ USD)", fontsize=11, fontweight="bold")
    plt.legend(title="Payment Method", loc="upper right")

    save_path = os.path.join(PLOTS_DIR, "week2_viz5_split_violin_equity.png")
    plt.tight_layout()
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {save_path}")