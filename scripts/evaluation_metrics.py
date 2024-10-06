import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

file1_path = './data/curated/grouped_avg_properties_sa2.csv'
file2_path = './data/curated/increase_rates.csv'

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

df1_districts = df1['SA2_NAME21'].unique()
df2_districts = df2['District'].unique()
common_districts = set(df1_districts).intersection(set(df2_districts))

df1_filtered = df1[df1['SA2_NAME21'].isin(common_districts)]
df2_filtered = df2[df2['District'].isin(common_districts)]

df1_filtered.rename(columns={'SA2_NAME21': 'District'}, inplace=True)
merged_data = pd.merge(df1_filtered, df2_filtered, on='District')

def arima_predict_rentals(df, district_name):
    district_data = df[df['District'] == district_name]
    rental_data = district_data[['Mar 2022 Median Rent', 'Jun 2022 Median Rent', 'Sep 2022 Median Rent', 'Dec 2022 Median Rent',
                                 'Mar 2023 Median Rent']].T.reset_index(drop=True)
    rental_data.columns = ['y']

    model = ARIMA(rental_data, order=(1, 1, 1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=12)

    forecast_dates = pd.date_range(start='2025-01-01', periods=12, freq='Q')
    forecast_df = pd.DataFrame({'District': district_name, 'Date': forecast_dates, 'Predicted_Rent': forecast})

    start_price = forecast_df['Predicted_Rent'].iloc[0]
    end_price = forecast_df['Predicted_Rent'].iloc[-1]
    percentage_increase = ((end_price - start_price) / start_price) * 100

    # Calculate in-sample predictions for model evaluation
    in_sample_predictions = model_fit.predict(start=1, end=len(rental_data)-1, dynamic=False)

    # Return both forecast and in-sample predictions
    return forecast_df, percentage_increase, rental_data[1:], in_sample_predictions

all_forecasts = []
increase_rates = []
true_values = []
predicted_values = []

for district in common_districts:
    forecast, percentage_increase, y_true, y_pred = arima_predict_rentals(merged_data, district)
    all_forecasts.append(forecast)
    increase_rates.append({'District': district, 'Percentage_Increase': percentage_increase})

    # Collect true and predicted values for calculating overall metrics
    true_values.extend(y_true.values.flatten())
    predicted_values.extend(y_pred)

# Calculate evaluation metrics
mae_overall = mean_absolute_error(true_values, predicted_values)
mse_overall = mean_squared_error(true_values, predicted_values)
rmse_overall = np.sqrt(mse_overall)
mape_overall = np.mean(np.abs((np.array(true_values) - np.array(predicted_values)) / np.array(true_values))) * 100

# Calculate R-squared
mean_true = np.mean(true_values)
ss_total = np.sum((np.array(true_values) - mean_true) ** 2)
ss_residual = np.sum((np.array(true_values) - np.array(predicted_values)) ** 2)
r_squared = 1 - (ss_residual / ss_total)

print(f"MAE: {mae_overall}")
print(f"MSE: {mse_overall}")
print(f"RMSE: {rmse_overall}")
print(f"MAPE: {mape_overall}%")
print(f"R-squared: {r_squared}")
