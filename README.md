# Generic Real Estate Consulting Project
For the data part:
(data/raw/SA2_2021_AUST_SHP_GDA2020):Download from https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files

(data/raw/dv296-schoollocations2020.csv):Download from https://discover.data.vic.gov.au/dataset/school-locations-2020

(data/raw/shopping_centers_coordinates.csv): Manually made from wikipedia, https://en.wikipedia.org/wiki/List_of_largest_shopping_centres_in_Australia

(<data/raw/Moving annual rent by suburb - March quarter 2023.xlsx>): Download from provided link: https://www.dffh.vic.gov.au/moving-annual-rents-suburb-march-quarter-2023-excel

For the scripts part:
(scripts/scrape_1b.py)(scripts/scrape_2b.py)(scripts/scrape_3b.py)(scripts/scrape_4b.py)(scripts/scrape_5b.py)(scripts/merge_data.py): Scrape the data from Domain and merge them together.

(scripts/remove_duplicate.py): Remove the exact same property, convert the different price(etc. per annual, per month..) to per week.

(scripts/clean.py): Keep the name and price part. 

(scripts/geocode_v1.py): Transform the address to coordinates.

(scripts/closest_station.py)(scripts/school_distance.py): Find the closest train station and closest school of the property.

(scripts/SA2_district.py): Put the property into SA2 district.

(scripts/model_arima_5_years.py)(scripts/model_arima.py): 5 Years and 3 years ARIMA model.

(scripts/average.py): average distance.

(scripts/score.py): Calculate the liveability score.

For the plots part:
(plots/increase_rate_arima.py) (plots/increase_rate_geo.py) (plots/increase_rate_historical.py): plots for increase rate arima model, and geo plot, and historical model.

(plots/score_geo.py): liveability geospatial plot.
