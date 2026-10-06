# Rainfall Intelligence: Data Cleaning and Exploratory Analysis of Tamil Nadu Rainfall

## Project Overview

**Rainfall Intelligence** is a Python-based data analysis project focused on **data cleaning and exploratory data analysis (EDA) of Tamil Nadu rainfall data from 2021–2025**.

The project focuses on transforming rainfall telemetry data into a cleaner and more structured dataset and performing exploratory analysis to understand rainfall patterns across **time, districts, and monitoring stations**.

This project is part of the **Sprint-I Data Analysis phase**. Machine learning and rainfall prediction are outside the scope of this sprint.

---

## Industry

**Industry / Domain:**  
Water Resource Management / Agriculture / Climate Analytics

**Related Organization:**  
Tamil Nadu Surface Water & Ground Water Department

---

## Problem Statement

Rainfall data collected from monitoring stations contains information across different locations and time periods. Raw rainfall telemetry data can be difficult to directly analyze because it requires data preparation, validation, transformation, and organization before meaningful analysis can be performed.

The project addresses the problem of making rainfall data more suitable for analysis by performing data cleaning and exploratory analysis.

The analysis focuses on understanding:

- Rainfall distribution
- Year-wise rainfall patterns
- Month-wise rainfall patterns
- District-level rainfall information
- Station-level rainfall information
- Extreme rainfall observations
- Station and yearly data coverage

The project creates a structured analytical foundation that can be used for further rainfall analysis and future machine-learning work.

---

## Proposed Solution

The proposed solution is to use Python-based data analysis techniques to:

1. Load the rainfall dataset.
2. Inspect the structure and quality of the data.
3. Identify missing and duplicate records.
4. Convert date and rainfall columns into appropriate data types.
5. Create additional time-related fields such as year and month.
6. Analyze rainfall statistics.
7. Analyze rainfall patterns by year, month, district, and station.
8. Identify extreme rainfall observations.
9. Examine station and yearly data coverage.
10. Export the processed analysis dataset for further use.

The project uses **Pandas, NumPy, and Matplotlib** to perform the data preparation and exploratory analysis.

---

## Dataset

### Dataset Name

**Rainfall (Telemetry - Hourly), Tamil Nadu SW GW**

The project uses Tamil Nadu rainfall data covering the **2021–2025** period.

### Dataset Source

**National Water Data Portal**

The dataset is associated with the **Tamil Nadu Surface Water & Ground Water** rainfall telemetry data.

> The original raw CSV is not included in this GitHub repository because of its large file size.

---

## Tools & Technologies

- **Python**
- **Jupyter Notebook**
- **NumPy**
- **Pandas**
- **Matplotlib**

---

## Project Workflow

```text
Industry Selection
        ↓
Problem Identification
        ↓
Dataset Collection
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Data Analysis
        ↓
Data Visualization
        ↓
Insights
        ↓
Recommendations
```

---

## Data Cleaning

The notebook performs the following data preparation and cleaning activities:

- Dataset shape inspection
- Initial data inspection using `head()`
- Dataset structure inspection using `info()`
- Statistical summary using `describe()`
- Missing-value checking
- Duplicate-record checking
- Date/time conversion
- Rainfall column conversion to numeric format
- Identification of dataset start and end dates
- Identification of monitoring stations
- Identification of districts
- Creation of a `Year` column
- Creation of month-related fields
- Preparation of rainfall summary statistics
- Removal of selected unnecessary geographic hierarchy columns for the analysis dataset

The following columns were removed from the final analysis dataset:

```text
Tehsil
Block
Village
River
Basin
Tributary
Subtributary
SubSubtributary
```

---

## Data Analysis & Visualization

The notebook performs the following analyses and visualizations.

### 1. Rainfall Distribution Analysis

Rainfall values are analyzed using descriptive statistics including:

- Minimum
- Average
- Median
- Maximum
- 25th percentile
- 75th percentile

A histogram is used to examine the distribution of rainfall observations.

### 2. Year-wise Analysis

The project creates yearly summaries containing:

- Number of records
- Average rainfall
- Median rainfall
- Maximum rainfall

A yearly average rainfall visualization is also created.

### 3. Month-wise Analysis

Monthly rainfall is analyzed using:

- Number of records
- Average rainfall
- Median rainfall
- Maximum rainfall

A monthly average rainfall line chart is used for time-based analysis.

### 4. District-wise Analysis

The project creates a district-level rainfall summary and analyzes district rainfall information.

A visualization is created for the top 10 districts based on the analysis performed in the notebook.

### 5. Station-wise Analysis

Rainfall information is summarized at the monitoring-station level.

A visualization is created for the top 10 stations based on the analysis performed in the notebook.

### 6. Extreme Rainfall Analysis

The project identifies rainfall observations meeting the following thresholds:

```text
Rainfall >= 100 mm
Rainfall >= 1000 mm
```

The analysis includes:

- Extreme rainfall observations
- Top extreme rainfall observations
- Extreme rainfall events by year

### 7. Data Coverage Analysis

The project examines:

- Number of records by station
- Number of records by year
- Unique station-day combinations

These analyses help understand the coverage of the available rainfall observations.

---

## Key Insights

The current Sprint-I project focuses on **data preparation and exploratory analysis** rather than producing a predictive model.

The analysis performed in the notebook is designed to identify:

- How rainfall observations are distributed.
- How rainfall varies across years.
- How rainfall varies across months.
- How rainfall differs between districts.
- How rainfall differs between monitoring stations.
- Where extreme rainfall observations occur in the dataset.
- How rainfall data coverage varies by station and year.

### Important Note

Numerical findings and specific conclusions are intentionally not reproduced in this README because the original raw CSV dataset is not included in the GitHub project package.

---

## Recommendations

This Sprint-I project establishes the cleaned and analyzed dataset as a foundation for further work.

Specific data-driven recommendations are not listed here because they should be derived from the verified results of the complete dataset analysis rather than assumed from the project topic.

The cleaned dataset and EDA results can be used as the foundation for future analysis and machine-learning work.

---

## Visualization Screenshots

The project notebook contains the visualizations generated during the exploratory analysis.

The GitHub repository can include the exported visualization screenshots when they are added to the `Visualizations/` folder.

### Planned Visualization Categories

- Rainfall Distribution
- Yearly Average Rainfall
- Monthly Average Rainfall
- District-wise Analysis
- Station-wise Analysis
- Extreme Rainfall by Year
- Station Coverage
- Yearly Data Coverage

> Screenshot filenames are not listed here because the final GitHub package does not currently contain exported visualization image files.

---

## Project Folder Structure

```text
Rainfall-Intelligence/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── Dataset/
│   └── README.md
│
├── Notebook/
│   └── Rainfall_Data_Analysis_EDA.ipynb
│
├── Python/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── data_visualization.py
│
├── Visualizations/
│   └── README.md
│
└── Documentation/
    ├── Project_Report.pdf
    └── README.md
```

---

## Project Scope

### Sprint-I

The current project focuses on:

- Data loading
- Data inspection
- Data cleaning
- Data transformation
- Exploratory data analysis
- Data visualization
- Data coverage analysis

### Future Scope

The cleaned and analyzed rainfall dataset can serve as a foundation for future machine-learning and predictive analysis.

Machine-learning prediction is **not part of the current Sprint-I implementation**.

---

## Author

**Name:** M Anavartha Vishwaraj  
**Student ID:** AF05320063  
**Organization:** Anudip Foundation  
**Course:** AIML  
**Batch Code:** ANP-D7444
