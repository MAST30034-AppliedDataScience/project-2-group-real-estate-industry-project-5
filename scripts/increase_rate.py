import pandas as pd

file_path = './data/curated/expanded_cleaned_properties.csv'
df = pd.read_csv(file_path)

df['Mar 2017 to Jun 2017 % Increase'] = ((df['Jun 2017 Median Rent'] - df['Mar 2017 Median Rent']) / df['Mar 2017 Median Rent']) * 100
df['Jun 2017 to Sep 2017 % Increase'] = ((df['Sep 2017 Median Rent'] - df['Jun 2017 Median Rent']) / df['Jun 2017 Median Rent']) * 100
df['Sep 2017 to Dec 2017 % Increase'] = ((df['Dec 2017 Median Rent'] - df['Sep 2017 Median Rent']) / df['Sep 2017 Median Rent']) * 100
df['Dec 2017 to Mar 2018 % Increase'] = ((df['Mar 2018 Median Rent'] - df['Dec 2017 Median Rent']) / df['Dec 2017 Median Rent']) * 100

df['Mar 2018 to Jun 2018 % Increase'] = ((df['Jun 2018 Median Rent'] - df['Mar 2018 Median Rent']) / df['Mar 2018 Median Rent']) * 100
df['Jun 2018 to Sep 2018 % Increase'] = ((df['Sep 2018 Median Rent'] - df['Jun 2018 Median Rent']) / df['Jun 2018 Median Rent']) * 100
df['Sep 2018 to Dec 2018 % Increase'] = ((df['Dec 2018 Median Rent'] - df['Sep 2018 Median Rent']) / df['Sep 2018 Median Rent']) * 100
df['Dec 2018 to Mar 2019 % Increase'] = ((df['Mar 2019 Median Rent'] - df['Dec 2018 Median Rent']) / df['Dec 2018 Median Rent']) * 100

df['Mar 2019 to Jun 2019 % Increase'] = ((df['Jun 2019 Median Rent'] - df['Mar 2019 Median Rent']) / df['Mar 2019 Median Rent']) * 100
df['Jun 2019 to Sep 2019 % Increase'] = ((df['Sep 2019 Median Rent'] - df['Jun 2019 Median Rent']) / df['Jun 2019 Median Rent']) * 100
df['Sep 2019 to Dec 2019 % Increase'] = ((df['Dec 2019 Median Rent'] - df['Sep 2019 Median Rent']) / df['Sep 2019 Median Rent']) * 100
df['Dec 2019 to Mar 2020 % Increase'] = ((df['Mar 2020 Median Rent'] - df['Dec 2019 Median Rent']) / df['Dec 2019 Median Rent']) * 100

df['Mar 2020 to Jun 2020 % Increase'] = ((df['Jun 2020 Median Rent'] - df['Mar 2020 Median Rent']) / df['Mar 2020 Median Rent']) * 100
df['Jun 2020 to Sep 2020 % Increase'] = ((df['Sep 2020 Median Rent'] - df['Jun 2020 Median Rent']) / df['Jun 2020 Median Rent']) * 100
df['Sep 2020 to Dec 2020 % Increase'] = ((df['Dec 2020 Median Rent'] - df['Sep 2020 Median Rent']) / df['Sep 2020 Median Rent']) * 100
df['Dec 2020 to Mar 2021 % Increase'] = ((df['Mar 2021 Median Rent'] - df['Dec 2020 Median Rent']) / df['Dec 2020 Median Rent']) * 100

df['Mar 2021 to Jun 2021 % Increase'] = ((df['Jun 2021 Median Rent'] - df['Mar 2021 Median Rent']) / df['Mar 2021 Median Rent']) * 100
df['Jun 2021 to Sep 2021 % Increase'] = ((df['Sep 2021 Median Rent'] - df['Jun 2021 Median Rent']) / df['Jun 2021 Median Rent']) * 100
df['Sep 2021 to Dec 2021 % Increase'] = ((df['Dec 2021 Median Rent'] - df['Sep 2021 Median Rent']) / df['Sep 2021 Median Rent']) * 100
df['Dec 2021 to Mar 2022 % Increase'] = ((df['Mar 2022 Median Rent'] - df['Dec 2021 Median Rent']) / df['Dec 2021 Median Rent']) * 100

df['Mar 2022 to Jun 2022 % Increase'] = ((df['Jun 2022 Median Rent'] - df['Mar 2022 Median Rent']) / df['Mar 2022 Median Rent']) * 100
df['Jun 2022 to Sep 2022 % Increase'] = ((df['Sep 2022 Median Rent'] - df['Jun 2022 Median Rent']) / df['Jun 2022 Median Rent']) * 100
df['Sep 2022 to Dec 2022 % Increase'] = ((df['Dec 2022 Median Rent'] - df['Sep 2022 Median Rent']) / df['Sep 2022 Median Rent']) * 100
df['Dec 2022 to Mar 2023 % Increase'] = ((df['Mar 2023 Median Rent'] - df['Dec 2022 Median Rent']) / df['Dec 2022 Median Rent']) * 100

output_file_path = './data/curated/increase_rates.csv'
df.to_csv(output_file_path, index=False)

output_file_path
