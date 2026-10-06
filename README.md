# Rainfall Intelligence: Data Cleaning and Exploratory Analysis of Tamil Nadu Rainfall

## Sprint-I — Data Cleaning & EDA

This project analyzes Tamil Nadu rainfall telemetry data using **Python, Pandas, NumPy and Matplotlib**. The analysis follows the uploaded Sprint-I notebook and focuses on data quality, rainfall patterns, spatial comparisons, extreme rainfall events, and data coverage.

## Project Structure

```text
Rainfall-Intelligence/
│
├── README.md
├── Dataset/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
├── Notebook/
│   └── Rainfall_Data_Analysis_EDA.ipynb
├── Python/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── data_visualization.py
├── Visualizations/
│   ├── distribution_analysis.png
│   ├── trend_analysis.png
│   ├── category_analysis.png
│   └── extreme_rainfall_analysis.png
└── Documentation/
    └── Project_Report.pdf
```

> **Dataset note:** The notebook references `rainfall_2021-2025.csv`, but that raw CSV was not included with the uploaded notebook. Therefore, the repository package does not fabricate or modify dataset values. Place the original CSV in `Dataset/raw_dataset.csv` before running the Python scripts.

## Analysis Performed

### Data Cleaning
- Loaded the rainfall CSV with Pandas.
- Checked dataset shape and first records.
- Inspected data types and descriptive statistics.
- Checked missing values and duplicate rows.
- Converted `Data Acquisition Time` to datetime.
- Converted `Telemetry Hourly Rainfall (mm)` to numeric.
- Extracted Year, Month and Month Name.
- Created a Date field for station-day coverage analysis.
- Removed the notebook's listed location/hydrology hierarchy columns when present.
- Exported the cleaned dataset.

### Exploratory Data Analysis
- Overall rainfall statistics.
- Rainfall distribution.
- Average rainfall by year.
- Monthly rainfall pattern.
- District-level rainfall comparison.
- Station-level rainfall comparison.
- Extreme rainfall events at ≥100 mm and ≥1000 mm.
- Top extreme rainfall observations.
- Extreme rainfall events by year.
- Station data coverage.
- Yearly data coverage.
- Unique station-day combinations.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## How to Run

1. Put the source dataset at `Dataset/raw_dataset.csv`.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the cleaning script:

```bash
python Python/data_cleaning.py
```

4. Run EDA:

```bash
python Python/exploratory_analysis.py
```

5. Generate visualizations:

```bash
python Python/data_visualization.py
```

6. Or open the notebook in Jupyter/VS Code and run it from top to bottom.

## Project Status

**Sprint-I completed:** Data Cleaning + Exploratory Data Analysis.

The next stage can extend this project into rainfall prediction / machine learning after the cleaned dataset and EDA findings are finalized.
