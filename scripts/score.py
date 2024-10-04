import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

# Load the dataset
file_path = './data/curated/grouped_avg_properties_sa2.csv'
data = pd.read_csv(file_path)

# Standardize the features using MinMaxScaler
scaler = MinMaxScaler()
data[['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)', 'Price']] = scaler.fit_transform(
    data[['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)', 'Price']]
)

# Select the features for PCA
features = ['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)', 'Price']
X = data[features]

# Apply PCA
pca = PCA(n_components=1)  # We are interested in the first principal component
pca.fit(X)

# Get the explained variance ratio for the first principal component
explained_variance_ratio = pca.components_[0]

# Normalize the explained variance ratio to get the weights
total_variance = sum(explained_variance_ratio)
pca_weights = [var / total_variance for var in explained_variance_ratio]

# Assign the PCA-based weights to each feature
weights_dict = dict(zip(features, pca_weights))

# Output the calculated PCA weights for review
print("Calculated PCA-based weights for liveability score:")
for feature, weight in weights_dict.items():
    print(f"{feature}: {weight}")

# Calculate the liveability score using the PCA-based weights
data['Liveability Score'] = (
    weights_dict['Distance (km)'] * (1 - data['Distance (km)']) +
    weights_dict['School Distance (km)'] * (1 - data['School Distance (km)']) +
    weights_dict['Distance to Closest Shopping Center (km)'] * (1 - data['Distance to Closest Shopping Center (km)']) +
    weights_dict['Price'] * (1 - data['Price'])
)

# Save the results to a new CSV
output_file_path = './data/curated/liveability_scores_with_pca_weights.csv'
data[['SA2_NAME21', 'Liveability Score']].sort_values(by='Liveability Score', ascending=False).to_csv(output_file_path, index=False)
