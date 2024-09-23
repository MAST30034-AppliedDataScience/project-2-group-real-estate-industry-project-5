# Generic Real Estate Consulting Project
For the data part:
(data/raw/SA2_2021_AUST_SHP_GDA2020):Download from https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files

(data/raw/dv296-schoollocations2020.csv):Download from https://discover.data.vic.gov.au/dataset/school-locations-2020



For the scrape part:
(scripts/scrape_1b.py)(scripts/scrape_2b.py)(scripts/scrape_3b.py)(scripts/scrape_4b.py)(scripts/scrape_5b.py)(scripts/merge_data.py): Scrape the data from Domain and merge them together.

(scripts/remove_duplicate.py): Remove the exact same property, convert the different price(etc. per annual, per month..) to per week.

(scripts/clean.py): Keep the name and price part. 

(scripts/geocode_v1.py): Transform the address to coordinates.

(scripts/closest_station.py)(scripts/school_distance.py): Find the closest train station and closest school of the property.

(scripts/SA2_district.py): Put the property into SA2 district.
