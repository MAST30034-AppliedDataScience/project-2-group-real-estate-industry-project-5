import pandas as pd

rent_price_file_path = './data/raw/Moving annual rent by suburb - March quarter 2023.xlsx'
all_properties_data = pd.read_excel(rent_price_file_path, sheet_name='All properties')

cleaned_all_properties_data = all_properties_data[['Unnamed: 1', 'Unnamed: 179', 'Unnamed: 181', 'Unnamed: 183', 'Unnamed: 185', 'Unnamed: 187']]

cleaned_all_properties_data.columns = ['District', 'Mar 2022 Median Rent', 'Jun 2022 Median Rent', 'Sep 2022 Median Rent', 'Dec 2022 Median Rent', 'Mar 2023 Median Rent']

cleaned_all_properties_data['Mar 2017 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2017 Median Rent'], errors='coerce')
cleaned_all_properties_data['Jun 2017 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Jun 2017 Median Rent'], errors='coerce')
cleaned_all_properties_data['Sep 2017 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Sep 2017 Median Rent'], errors='coerce')
cleaned_all_properties_data['Dec 2017 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Dec 2017 Median Rent'], errors='coerce')

cleaned_all_properties_data['Mar 2018 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2018 Median Rent'], errors='coerce')
cleaned_all_properties_data['Jun 2018 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Jun 2018 Median Rent'], errors='coerce')
cleaned_all_properties_data['Sep 2018 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Sep 2018 Median Rent'], errors='coerce')
cleaned_all_properties_data['Dec 2018 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Dec 2018 Median Rent'], errors='coerce')

cleaned_all_properties_data['Mar 2019 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2019 Median Rent'], errors='coerce')
cleaned_all_properties_data['Jun 2019 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Jun 2019 Median Rent'], errors='coerce')
cleaned_all_properties_data['Sep 2019 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Sep 2019 Median Rent'], errors='coerce')
cleaned_all_properties_data['Dec 2019 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Dec 2019 Median Rent'], errors='coerce')

cleaned_all_properties_data['Mar 2020 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2020 Median Rent'], errors='coerce')
cleaned_all_properties_data['Jun 2020 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Jun 2020 Median Rent'], errors='coerce')
cleaned_all_properties_data['Sep 2020 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Sep 2020 Median Rent'], errors='coerce')
cleaned_all_properties_data['Dec 2020 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Dec 2020 Median Rent'], errors='coerce')

cleaned_all_properties_data['Mar 2021 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2021 Median Rent'], errors='coerce')
cleaned_all_properties_data['Jun 2021 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Jun 2021 Median Rent'], errors='coerce')
cleaned_all_properties_data['Sep 2021 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Sep 2021 Median Rent'], errors='coerce')
cleaned_all_properties_data['Dec 2021 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Dec 2021 Median Rent'], errors='coerce')

cleaned_all_properties_data['Mar 2022 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2022 Median Rent'], errors='coerce')
cleaned_all_properties_data['Jun 2022 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Jun 2022 Median Rent'], errors='coerce')
cleaned_all_properties_data['Sep 2022 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Sep 2022 Median Rent'], errors='coerce')
cleaned_all_properties_data['Dec 2022 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Dec 2022 Median Rent'], errors='coerce')
cleaned_all_properties_data['Mar 2023 Median Rent'] = pd.to_numeric(cleaned_all_properties_data['Mar 2023 Median Rent'], errors='coerce')

cleaned_all_properties_data = cleaned_all_properties_data.dropna(subset=['District'])
cleaned_all_properties_data.head()

output_file_path = './data/curated/cleaned_all_properties1.csv'
cleaned_all_properties_data.to_csv(output_file_path, index=False)

