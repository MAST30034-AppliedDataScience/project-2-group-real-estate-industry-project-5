import pandas as pd
from geopy.distance import geodesic
from tqdm import tqdm

tqdm.pandas()

shopping_centers_file_path = './data/raw/shopping_centers_coordinates.csv'
shopping_centers_df = pd.read_csv(shopping_centers_file_path)

properties_file_path = './data/curated/properties_with_sa2_districts.csv'
properties_df = pd.read_csv(properties_file_path)

def calculate_distance(property_lat, property_long, shopping_center_lat, shopping_center_long):
    return geodesic((property_lat, property_long), (shopping_center_lat, shopping_center_long)).kilometers

closest_centers = []

for _, property_row in tqdm(properties_df.iterrows(), total=len(properties_df), desc="Processing Properties"):
    property_coords = (property_row['Property Latitude'], property_row['Property Longitude'])
    min_distance = float('inf')
    closest_center = None
    
    for _, center_row in shopping_centers_df.iterrows():
        center_coords = (center_row['Latitude'], center_row['Longitude'])
        distance = calculate_distance(property_coords[0], property_coords[1], center_coords[0], center_coords[1])
        
        if distance < min_distance:
            min_distance = distance
            closest_center = center_row['Name']
    
    closest_centers.append({
        'Property Name': property_row['Property Name'],
        'Closest Shopping Center': closest_center,
        'Distance (km)': min_distance
    })

closest_centers_df = pd.DataFrame(closest_centers)

properties_with_closest_center = properties_df.copy()
properties_with_closest_center['Closest Shopping Center'] = closest_centers_df['Closest Shopping Center']
properties_with_closest_center['Distance to Closest Shopping Center (km)'] = closest_centers_df['Distance (km)']

output_properties_file = './data/curated/properties_with_closest_shopping_centers.csv'
properties_with_closest_center.to_csv(output_properties_file, index=False)


