import pandas as pd
from geopy.distance import geodesic
from tqdm import tqdm

closest_stations_path = './data/curated/closest_stations.csv'
school_locations_path = './data/raw/dv296-schoollocations2020.csv'

closest_stations = pd.read_csv(closest_stations_path)
school_locations = pd.read_csv(school_locations_path)

def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers

closest_schools = []
school_distances = []

# Iterate over each property with tqdm progress bar
for index, row in tqdm(closest_stations.iterrows(), total=closest_stations.shape[0], desc="Processing properties"):
    property_lat = row['Property Latitude']
    property_lon = row['Property Longitude']

    school_locations['Distance'] = school_locations.apply(
        lambda x: calculate_distance(property_lat, property_lon, x['Y'], x['X']), axis=1
    )

    closest_school = school_locations.loc[school_locations['Distance'].idxmin()]

    closest_schools.append(closest_school['School_Name'])
    school_distances.append(closest_school['Distance'])

# Add the closest school name and distance to the closest_stations DataFrame
closest_stations['Closest School'] = closest_schools
closest_stations['School Distance (km)'] = school_distances

output_path = './data/curated/updated_closest_stations.csv'
closest_stations.to_csv(output_path, index=False)


