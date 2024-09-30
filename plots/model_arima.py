import pandas as pd
import matplotlib.pyplot as plt

file_path = './data/curated/arima_2025_2027.csv'
output_file_path = './plots/predicted_rent.png'

df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 6))
for district in df['District'].unique():
    district_data = df[df['District'] == district]
    plt.plot(district_data['Date'], district_data['Predicted_Rent'], label=district)

plt.title('Predicted Rent Over Time by District')
plt.xlabel('Date')
plt.ylabel('Predicted Rent')
plt.grid(True)
plt.xticks(rotation=45)

plt.legend(title='District', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.subplots_adjust(right=0.8)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.savefig(output_file_path, bbox_inches='tight')
