"""Data-cleaning steps reproduced from the Sprint-I notebook."""
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "Dataset" / "raw_dataset.csv"
CLEAN_FILE = BASE_DIR / "Dataset" / "cleaned_dataset.csv"
RAINFALL_COL = "Telemetry Hourly Rainfall (mm)"


def clean_data(input_path=RAW_FILE, output_path=CLEAN_FILE):
    df = pd.read_csv(input_path)

    print("No. of rows and columns:", df.shape)
    print("Null values:\n", df.isnull().sum())
    print("Duplicate rows:", df.duplicated().sum())

    df["Data Acquisition Time"] = pd.to_datetime(
        df["Data Acquisition Time"], dayfirst=True, errors="coerce"
    )
    df[RAINFALL_COL] = pd.to_numeric(df[RAINFALL_COL], errors="coerce")

    df["Year"] = df["Data Acquisition Time"].dt.year
    df["Month"] = df["Data Acquisition Time"].dt.month
    df["Month_Name"] = df["Data Acquisition Time"].dt.month_name()
    df["Date"] = df["Data Acquisition Time"].dt.date

    columns_to_remove = [
        "Tehsil", "Block", "Village", "River", "Basin",
        "Tributary", "Subtributary", "SubSubtributary"
    ]
    df = df.drop(columns=columns_to_remove, errors="ignore")

    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to: {output_path}")
    print("Final shape:", df.shape)
    return df


if __name__ == "__main__":
    clean_data()
