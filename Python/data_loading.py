"""Load the Tamil Nadu rainfall dataset used by the project."""
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "Dataset" / "raw_dataset.csv"


def load_data(path=RAW_FILE):
    df = pd.read_csv(path)
    print("Dataset loaded successfully")
    print("Rows and columns:", df.shape)
    return df


if __name__ == "__main__":
    load_data()
