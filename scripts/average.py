import pandas as pd
from tqdm import tqdm

tqdm.pandas()

file_path = './data/curated/properties_with_sa2_districts.csv'
data = pd.read_csv(file_path)

data['Distance (km)'] = pd.to_numeric(data['Distance (km)'], errors='coerce')
data['School Distance (km)'] = pd.to_numeric(data['School Distance (km)'], errors='coerce')

data['Price'] = data['cost_text'].str.extract(r'(\d+[\.,]?\d*)').replace(',', '', regex=True).astype(float)

grouped_avg_data = data.groupby('SA2_NAME21').agg({
    'Distance (km)': 'mean',
    'School Distance (km)': 'mean',
    'Price': 'mean'
}).reset_index()

output_file_path = './data/curated/grouped_avg_data_sa2.csv'
grouped_avg_data.to_csv(output_file_path, index=False)
