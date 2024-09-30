import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

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

    forecast = model_fit.forecast(steps=20)

    forecast_dates = pd.date_range(start='2025-01-01', periods=20, freq='Q')
    forecast_df = pd.DataFrame({'District': district_name, 'Date': forecast_dates, 'Predicted_Rent': forecast})

    start_price = forecast_df['Predicted_Rent'].iloc[0]
    end_price = forecast_df['Predicted_Rent'].iloc[-1]
    percentage_increase = ((end_price - start_price) / start_price) * 100

    return forecast_df, percentage_increase

all_forecasts = []
increase_rates = []

for district in common_districts:
    forecast, percentage_increase = arima_predict_rentals(merged_data, district)
    all_forecasts.append(forecast)
    increase_rates.append({'District': district, 'Percentage_Increase': percentage_increase})

all_forecasts_df = pd.concat(all_forecasts)

output_file_forecasts = './data/curated/arima_5_years.csv'
all_forecasts_df.to_csv(output_file_forecasts, index=False)

increase_rates_df = pd.DataFrame(increase_rates)
output_file_increase_rates = './data/curated/arima_increase_rates_5_years.csv'
increase_rates_df.to_csv(output_file_increase_rates, index=False)

