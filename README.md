# 🚕 Week 2: The Anatomy of Urban Transit — A Visual Narrative

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Pandas](https://img.shields.io/badge/Library-Pandas%20%7C%20NumPy-orange.svg)
![Seaborn](https://img.shields.io/badge/Visualization-Matplotlib%20%7C%20Seaborn-green.svg)
![Status](https://img.shields.io/badge/Milestone-Week%202%20Complete-brightgreen.svg)

## 📌 1. Project Overview & Storytelling Objective
This repository contains the **Week 2 Data Visualization and Storytelling** pipeline for the New York City Taxi & Limousine Commission (TLC) Trip Record Dataset. Moving beyond basic exploratory data analysis (EDA), this project transforms complex, multi-dimensional transit telemetry into a cohesive visual narrative tailored for non-technical stakeholders (urban planners, fleet managers, and city officials). 

The analysis is structured around a four-part narrative arc:
1. **Temporal Rhythm:** When does the city move?
2. **Geospatial Flow:** Where do commuters travel?
3. **Operational Friction:** How does traffic congestion impact transit speed?
4. **Trip Economics:** How is revenue generated and distributed across boroughs?

---

## 📂 2. Modular VS Code Architecture

The codebase is organized into highly modular, single-responsibility Python scripts to maintain clean architecture:

```text
nyc_taxi_eda_project/
│
├── README.md                     # This documentation file
├── week2_config.py               # Shared paths, URLs, and global storytelling styling
├── week2_preprocessing.py        # Cleaning, imputation, and feature engineering
├── week2_viz1_pulse.py           # Viz 1: 2D Temporal Heatmap
├── week2_viz2_flow.py            # Viz 2: Origin-Destination Transition Matrix
├── week2_viz3_congestion.py      # Viz 3: Joint Hexbin Speed/Congestion Plot
├── week2_viz4_fare.py            # Viz 4: Stacked Revenue Composition Bar Chart
├── week2_viz5_equity.py          # Viz 5: Split Violin Equity & Tip Distribution Plot
├── week2_main.py                 # Main execution orchestrator
│
└── outputs/
    └── week2_plots/              # Auto-generated high-resolution PNGs
        ├── week2_viz1_temporal_heatmap.png
        ├── week2_viz2_borough_flow_matrix.png
        ├── week2_viz3_congestion_jointplot.png
        ├── week2_viz4_fare_anatomy.png
        └── week2_viz5_split_violin_equity.png
