import pandas as pd

def load_and_prep_story_data(data_url: str) -> pd.DataFrame:
    """Loads raw data, cleans it, and engineers storytelling features."""
    print("[INFO] Fetching and prepping dataset for Week 2 visual narrative...")
    df = pd.read_csv(data_url).drop_duplicates()
    
    # 1. Base Cleaning & Imputation
    df = df.dropna(subset=["pickup_zone", "dropoff_zone", "pickup_borough", "dropoff_borough"]).copy()
    df.loc[df["payment"].isnull() & (df["tip"] > 0), "payment"] = "credit card"
    df["payment"] = df["payment"].fillna(df["payment"].mode()[0])

    # 2. Datetime Parsing & Temporal Engineering
    df["pickup"] = pd.to_datetime(df["pickup"])
    df["dropoff"] = pd.to_datetime(df["dropoff"])
    df["trip_duration_mins"] = (df["dropoff"] - df["pickup"]).dt.total_seconds() / 60.0
    df["pickup_hour"] = df["pickup"].dt.hour

    # 3. Order days chronologically for temporal heatmaps
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df["day_of_week"] = pd.Categorical(df["pickup"].dt.day_name(), categories=day_order, ordered=True)

    # 4. Filter Physics Anomalies
    valid_mask = (
        (df["distance"] > 0.1) & 
        (df["trip_duration_mins"] > 0.5) & 
        (df["trip_duration_mins"] <= 180.0) & 
        (df["passengers"] > 0) & 
        (df["fare"] > 0)
    )
    df_clean = df[valid_mask].copy()

    # 5. Engineer Traffic Speed (MPH)
    df_clean["speed_mph"] = df_clean["distance"] / (df_clean["trip_duration_mins"] / 60.0)
    df_clean = df_clean[df_clean["speed_mph"] <= 65.0].copy()

    print(f"[INFO] Storytelling dataset ready: {len(df_clean)} validated trips.")
    return df_clean