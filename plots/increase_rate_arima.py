import pandas as pd
import matplotlib.pyplot as plt

file_path = './data/curated/arima_increase_rates_2025_2027.csv'
increase_data = pd.read_csv(file_path)

sorted_increase_data = increase_data.sort_values(by='Percentage_Increase', ascending=False)
plt.figure(figsize=(10, 12))
plt.barh(sorted_increase_data['District'], sorted_increase_data['Percentage_Increase'], color='lightgreen')
plt.xlabel('Percentage Increase')
plt.ylabel('District')
plt.title('Percentage Increase in Rent by District (2025-2027)')
plt.gca().invert_yaxis()
plt.tight_layout()

output_path = './plots/increase_2025_2027.png'
plt.savefig(output_path)

