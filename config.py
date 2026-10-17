import os
import matplotlib.pyplot as plt
import seaborn as sns

# File Paths & URLs
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
PLOTS_DIR = os.path.join(OUTPUT_DIR, "week2_plots")

def ensure_directories():
    """Creates the necessary output folders if they do not exist."""
    os.makedirs(PLOTS_DIR, exist_ok=True)

def apply_storytelling_style():
    """Sets global Matplotlib and Seaborn visual styling for non-technical audiences."""
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams["figure.dpi"] = 140
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.edgecolor"] = "#cccccc"
    plt.rcParams["axes.linewidth"] = 0.8