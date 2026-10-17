from config import ensure_directories, apply_storytelling_style, DATA_URL
from preprocessing import load_and_prep_story_data
from viz1_pulse import plot_temporal_pulse
from viz2_flow import plot_commuter_flow
from viz3_congestion import plot_congestion_penalty
from viz4_fare import plot_fare_anatomy
from viz5_equity import plot_payment_equity

def main():
    print("=" * 60)
    print("STARTING WEEK 2: VISUAL NARRATIVE & STORYTELLING PIPELINE")
    print("=" * 60)

    ensure_directories()
    apply_storytelling_style()

    df_clean = load_and_prep_story_data(DATA_URL)

    print("\n[INFO] Generating Data Storytelling Visualizations...")
    plot_temporal_pulse(df_clean)
    plot_commuter_flow(df_clean)
    plot_congestion_penalty(df_clean)
    plot_fare_anatomy(df_clean)
    plot_payment_equity(df_clean)

    print("\n" + "=" * 60)
    print("WEEK 2 PIPELINE COMPLETED SUCCESSFULLY!")
    print("Check the 'outputs/week2_plots/' folder for your deliverables.")
    print("=" * 60)

if __name__ == "__main__":
    main()