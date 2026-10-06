"""Create the main visualizations from the Sprint-I EDA."""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "Dataset" / "cleaned_dataset.csv"
OUT_DIR = BASE_DIR / "Visualizations"
RAINFALL_COL = "Telemetry Hourly Rainfall (mm)"


def create_visualizations(path=DATA_FILE):
    OUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(path)

    # Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df[RAINFALL_COL].dropna(), bins=50)
    plt.xlabel("Rainfall (mm)")
    plt.ylabel("Number of Observations")
    plt.title("Rainfall Distribution")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "distribution_analysis.png", dpi=150)
    plt.close()

    # Yearly trend
    year_summary = df.groupby("Year")[RAINFALL_COL].mean()
    year_summary.plot(kind="bar", figsize=(8, 5))
    plt.xlabel("Year")
    plt.ylabel("Average Rainfall (mm)")
    plt.title("Average Rainfall by Year")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "trend_analysis.png", dpi=150)
    plt.close()

    # District/category analysis
    district_summary = df.groupby("District")[RAINFALL_COL].mean().sort_values(ascending=False).head(10)
    district_summary.sort_values().plot(kind="barh", figsize=(8, 5))
    plt.xlabel("Average Rainfall (mm)")
    plt.ylabel("District")
    plt.title("Top 10 Districts by Average Rainfall")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "category_analysis.png", dpi=150)
    plt.close()

    # Extreme rainfall analysis
    extreme = df[df[RAINFALL_COL] >= 100]
    extreme_year = extreme.groupby("Year").size().sort_index()
    extreme_year.plot(kind="bar", figsize=(8, 5))
    plt.xlabel("Year")
    plt.ylabel("Number of Events")
    plt.title("Extreme Rainfall Events by Year")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "extreme_rainfall_analysis.png", dpi=150)
    plt.close()

    print(f"Visualizations saved in: {OUT_DIR}")


if __name__ == "__main__":
    create_visualizations()
