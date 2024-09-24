import pandas as pd
from tqdm import tqdm

tqdm.pandas()

properties_file_path_updated = './data/curated/properties_with_closest_shopping_centers.csv'
properties_updated_df = pd.read_csv(properties_file_path_updated)

properties_updated_df['Price'] = properties_updated_df['cost_text'].str.extract(r'(\d+[\.,]?\d*)').replace(',', '', regex=True).astype(float)


grouped_avg_properties = properties_updated_df.groupby('SA2_NAME21').agg({
    'Distance (km)': 'mean',  # Distance to station
    'School Distance (km)': 'mean',  # Distance to school
    'Distance to Closest Shopping Center (km)': 'mean',  # Distance to shopping center
    'Price': 'mean'  # Average price
}).reset_index()


output_file_path = './data/curated/grouped_avg_properties_sa2.csv'
grouped_avg_properties.to_csv(output_file_path, index=False)
