import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

properties_df = pd.read_csv('./data/curated/grouped_avg_properties_sa2.csv')
increase_rates_df = pd.read_csv('./data/curated/increase_rates.csv')

properties_df['SA2_NAME21_lower'] = properties_df['SA2_NAME21'].str.lower()
increase_rates_df['District_lower'] = increase_rates_df['District'].str.lower()
merged_df = pd.merge(properties_df, increase_rates_df, left_on='SA2_NAME21_lower', right_on='District_lower', how='inner')

time_periods = np.arange(1, 26)
future_periods = np.arange(26, 38)

future_quarters_years = [
    '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4',
    '2026 Q1', '2026 Q2', '2026 Q3', '2026 Q4',
    '2027 Q1', '2027 Q2', '2027 Q3', '2027 Q4'
]

predictions = {}
for region in merged_df['SA2_NAME21']:
    region_data = merged_df[merged_df['SA2_NAME21'] == region]

    X_time = time_periods.reshape(-1, 1)
    X_distances = np.tile(region_data[['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)']].values, (25, 1))

    X_combined = np.hstack([X_time, X_distances])

    y = region_data[[ 
        'Mar 2017 Median Rent', 'Jun 2017 Median Rent', 'Sep 2017 Median Rent', 'Dec 2017 Median Rent',
        'Mar 2018 Median Rent', 'Jun 2018 Median Rent', 'Sep 2018 Median Rent', 'Dec 2018 Median Rent',
        'Mar 2019 Median Rent', 'Jun 2019 Median Rent', 'Sep 2019 Median Rent', 'Dec 2019 Median Rent',
        'Mar 2020 Median Rent', 'Jun 2020 Median Rent', 'Sep 2020 Median Rent', 'Dec 2020 Median Rent',
        'Mar 2021 Median Rent', 'Jun 2021 Median Rent', 'Sep 2021 Median Rent', 'Dec 2021 Median Rent',
        'Mar 2022 Median Rent', 'Jun 2022 Median Rent', 'Sep 2022 Median Rent', 'Dec 2022 Median Rent',
        'Mar 2023 Median Rent'
    ]].values.flatten()

    model = LinearRegression()
    model.fit(X_combined, y)

    future_X_time = future_periods.reshape(-1, 1)
    future_X_distances = np.tile(region_data[['Distance (km)', 'School Distance (km)', 'Distance to Closest Shopping Center (km)']].values, (12, 1))

    future_X_combined = np.hstack([future_X_time, future_X_distances])

    future_predictions = model.predict(future_X_combined)
    predictions[region] = future_predictions

predictions_df = pd.DataFrame(predictions, index=future_quarters_years)

output_file_path = './data/curated/model_lr_distances.csv'
predictions_df.to_csv(output_file_path)

output_file_path