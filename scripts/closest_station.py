import pandas as pd
from math import radians, sin, cos, sqrt, atan2

property_data_path = './data/curated/cleaned_domaindata_with_geocode.csv'
station_data_path = './data/curated/station_location.csv'

property_data = pd.read_csv(property_data_path)
station_data = pd.read_csv(station_data_path)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

closest_stations_with_coords = []

for _, property_row in property_data.dropna(subset=['latitude', 'longitude']).iterrows():
    min_distance = float('inf')
    closest_station = None
    closest_station_lat = None
    closest_station_lon = None

    for _, station_row in station_data.iterrows():
        distance = haversine(
            property_row['latitude'], property_row['longitude'],
            station_row['latitude'], station_row['longitude']
        )
        if distance < min_distance:
            min_distance = distance
            closest_station = station_row['STATION_NAME']
            closest_station_lat = station_row['latitude']
            closest_station_lon = station_row['longitude']

    closest_stations_with_coords.append({
        'Property Name': property_row['name'],
        'Property Latitude': property_row['latitude'],
        'Property Longitude': property_row['longitude'],
        'Closest Station': closest_station,
        'Station Latitude': closest_station_lat,
        'Station Longitude': closest_station_lon,
        'Distance (km)': min_distance
    })

closest_stations_with_coords_df = pd.DataFrame(closest_stations_with_coords)

# Add the price column to the DataFrame
closest_stations_with_coords_df_with_price = closest_stations_with_coords_df.merge(
    property_data[['name', 'cost_text']], 
    left_on='Property Name', 
    right_on='name', 
    how='left'
).drop(columns=['name'])

output_with_coords_path = './data/curated/closest_stations.csv'
closest_stations_with_coords_df_with_price.to_csv(output_with_coords_path, index=False)

output_with_coords_path
