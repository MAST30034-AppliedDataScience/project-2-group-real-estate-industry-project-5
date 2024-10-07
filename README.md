# Generic Real Estate Consulting Project - Group 5

## Data Sources

- **SA2 Boundaries**:  
  File Path: `data/raw/SA2_2021_AUST_SHP_GDA2020`  
  [Download from ABS](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)

- **School Locations (2020)**:  
  File Path: `data/raw/dv296-schoollocations2020.csv`  
  [Download from Data Vic](https://discover.data.vic.gov.au/dataset/school-locations-2020)

- **Shopping Centers Coordinates**:  
  File Path: `data/raw/shopping_centers_coordinates.csv`  
  Manually compiled from [Wikipedia](https://en.wikipedia.org/wiki/List_of_largest_shopping_centres_in_Australia)

- **Moving Annual Rent by Suburb (March 2023)**:  
  File Path: `data/raw/Moving annual rent by suburb - March quarter 2023.xlsx`  
  [Download from Vic Government](https://www.dffh.vic.gov.au/moving-annual-rents-suburb-march-quarter-2023-excel)

---

## Scripts

- **Data Scraping and Merging**:
  - `scripts/scrape_1b.py`, `scripts/scrape_2b.py`, `scripts/scrape_3b.py`, `scripts/scrape_4b.py`, `scripts/scrape_5b.py`: Scripts to scrape data from Domain.
  - `scripts/merge_data.py`: Script to merge the scraped data together.

- **Data Cleaning**:
  - `scripts/remove_duplicate.py`: Removes duplicate properties and converts prices (e.g., per annum, per month) to weekly rates.
  - `scripts/clean.py`: Retains the relevant fields such as property name and price.
  - `scripts/clean_hist_data.py`: Cleans historical rent data for consistency.

- **Geocoding**:
  - `scripts/geocode_v1.py`: Converts property addresses into geographical coordinates.

- **Proximity Calculations**:
  - `scripts/closest_station.py`: Identifies the closest train station to each property.
  - `scripts/school_distance.py`: Finds the nearest school for each property.
  - `scripts/closest_shopping_center.py`: Calculates the distance to the closest shopping center for each property.

- **SA2 District Assignment**:
  - `scripts/SA2_district.py`: Assigns properties to their respective SA2 districts.

- **ARIMA Models**:
  - `scripts/model_arima_5_years.py`: ARIMA model to predict rent increases over 5 years.
  - `scripts/model_arima.py`: ARIMA model to predict rent increases over 3 years.

- **Model Evaluation**:
  - `scripts/evaluation_metrics.py`: Provides metrics to evaluate the performance of ARIMA models.

- **Averaging and Scoring**:
  - `scripts/average.py`: Calculates the average distances from properties to amenities.
  - `scripts/score.py`: Computes the liveability score for each property.
  
- **Correlation and Analysis**:
  - `scripts/corr_income.py`: Correlates income data with rental data for better prediction accuracy.

---

## Plotting Scripts

- **Increase Rate Plots**:
  - `plots/increase_rate_arima.py`: Plot for rent increase rates based on the ARIMA model.
  - `plots/increase_rate_geo.py`: Geospatial plot for rent increase rates.
  - `plots/increase_rate_historical.py`: Plot for rent increases based on historical data.

- **Liveability Score Plot**:
  - `plots/score_geo.py`: Geospatial plot showing liveability scores.

- **Model Plots**:
  - `plots/plot_for_model_notebook.py`: Script to generate plots for model results (LSTM and XGboost) in the notebook.

---

## Notebooks

- **Checkpoint Notebook**:
  - `notebooks/notebook_week10.ipynb`: Notebook for the Week 10 checkpoint.

- **Final Deliverable Notebook**:
  - `notebooks/notebook_final.ipynb`: Final deliverable notebook for assessment.

- **Data Loading and Cleaning**:
  - `Load&Clean_Data.ipynb`: Notebook responsible for loading and cleaning the data.

- **Random Forest Model**:
  - `RF.ipynb`: Random Forest for feature selection.