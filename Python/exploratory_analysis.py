"""Exploratory analysis reproduced from the Sprint-I notebook."""
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "Dataset" / "cleaned_dataset.csv"
RAINFALL_COL = "Telemetry Hourly Rainfall (mm)"


def run_eda(path=DATA_FILE):
    df = pd.read_csv(path)
    df["Data Acquisition Time"] = pd.to_datetime(df["Data Acquisition Time"], errors="coerce")

    year_summary = df.groupby("Year")[RAINFALL_COL].agg(
        Records="count", Average="mean", Median="median", Maximum="max"
    ).round(2)

    month_summary = df.groupby("Month")[RAINFALL_COL].agg(
        Records="count", Average="mean", Median="median", Maximum="max"
    ).round(2)

    district_summary = df.groupby("District")[RAINFALL_COL].agg(
        Records="count", Average="mean", Median="median", Maximum="max"
    ).sort_values("Average", ascending=False).round(2)

    station_summary = df.groupby("Station")[RAINFALL_COL].agg(
        Records="count", Average="mean", Median="median", Maximum="max"
    ).sort_values("Average", ascending=False).round(2)

    extreme_100 = df[df[RAINFALL_COL] >= 100]
    extreme_1000 = df[df[RAINFALL_COL] >= 1000]
    extreme_year = extreme_100.groupby("Year").size().sort_index()
    station_coverage = df.groupby("Station").size().sort_values(ascending=False)
    year_coverage = df.groupby("Year").size()

    print("\nYEAR SUMMARY\n", year_summary)
    print("\nMONTH SUMMARY\n", month_summary)
    print("\nTOP DISTRICTS\n", district_summary.head(10))
    print("\nTOP STATIONS\n", station_summary.head(10))
    print("\nRainfall >= 100 mm:", len(extreme_100))
    print("Rainfall >= 1000 mm:", len(extreme_1000))
    print("\nEXTREME EVENTS BY YEAR\n", extreme_year)
    print("\nTOP STATION COVERAGE\n", station_coverage.head(15))
    print("\nYEAR COVERAGE\n", year_coverage)

    return {
        "year_summary": year_summary,
        "month_summary": month_summary,
        "district_summary": district_summary,
        "station_summary": station_summary,
        "extreme_100": extreme_100,
        "extreme_1000": extreme_1000,
        "extreme_year": extreme_year,
        "station_coverage": station_coverage,
        "year_coverage": year_coverage,
    }


if __name__ == "__main__":
    run_eda()
