import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path_latest_increase_rates = './data/curated/increase_rates.csv'
df_increase_rates_latest = pd.read_csv(file_path_latest_increase_rates)

rental_price_columns = [
    'Mar 2017 Median Rent', 'Jun 2017 Median Rent', 'Sep 2017 Median Rent', 'Dec 2017 Median Rent',
    'Mar 2018 Median Rent', 'Jun 2018 Median Rent', 'Sep 2018 Median Rent', 'Dec 2018 Median Rent',
    'Mar 2019 Median Rent', 'Jun 2019 Median Rent', 'Sep 2019 Median Rent', 'Dec 2019 Median Rent',
    'Mar 2020 Median Rent', 'Jun 2020 Median Rent', 'Sep 2020 Median Rent', 'Dec 2020 Median Rent',
    'Mar 2021 Median Rent', 'Jun 2021 Median Rent', 'Sep 2021 Median Rent', 'Dec 2021 Median Rent',
    'Mar 2022 Median Rent', 'Jun 2022 Median Rent', 'Sep 2022 Median Rent', 'Dec 2022 Median Rent',
    'Mar 2023 Median Rent'
]

years = [
    'Mar 2017', 'Jun 2017', 'Sep 2017', 'Dec 2017',
    'Mar 2018', 'Jun 2018', 'Sep 2018', 'Dec 2018',
    'Mar 2019', 'Jun 2019', 'Sep 2019', 'Dec 2019',
    'Mar 2020', 'Jun 2020', 'Sep 2020', 'Dec 2020',
    'Mar 2021', 'Jun 2021', 'Sep 2021', 'Dec 2021',
    'Mar 2022', 'Jun 2022', 'Sep 2022', 'Dec 2022',
    'Mar 2023'
]

plt.figure(figsize=(14, 8))

for region in df_increase_rates_latest.index: 
    plt.plot(years, df_increase_rates_latest.loc[region, rental_price_columns].values, label=f'Region {region}')

plt.title('Rental Price Trends for Every Region (2017-2023)')
plt.xlabel('Year')
plt.ylabel('Rental Prices')
plt.xticks(rotation=90)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
plt.tight_layout()

plt.savefig('./plots/rental_price_trends.png', dpi=300, bbox_inches='tight')

plt.show()
