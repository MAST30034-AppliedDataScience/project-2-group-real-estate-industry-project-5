import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
file_path = './data/curated/grouped_avg_properties_sa2.csv'
data = pd.read_csv(file_path)

scaler = MinMaxScaler()
data[['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)', 'Price']] = scaler.fit_transform(
    data[['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)', 'Price']]
)

# Weights for the factors
weights = {
    'Distance (km)': 0.3,
    'School Distance (km)': 0.3,
    'Distance to Closest Shopping Center (km)': 0.1,
    'Price': 0.3
}

# Calculate liveability score (lower distances and price contribute positively)
data['Liveability Score'] = (
    weights['Distance (km)'] * (1 - data['Distance (km)']) +
    weights['School Distance (km)'] * (1 - data['School Distance (km)']) +
    weights['Distance to Closest Shopping Center (km)'] * (1 - data['Distance to Closest Shopping Center (km)']) +
    weights['Price'] * (1 - data['Price'])
)


output_file_path = './data/curated/liveability_scores.csv'
data[['SA2_NAME21', 'Liveability Score']].sort_values(by='Liveability Score', ascending=False).to_csv(output_file_path, index=False)

