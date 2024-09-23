import pandas as pd

# Load the JSON file
file_path = './data/curated/cleaned_domaindata_with_prices.json'
data = pd.read_json(file_path)

# Transpose the data to handle URLs as keys
transposed_data = data.T

# Keep only 'name' and 'cost_text' columns
cleaned_data = transposed_data[['name', 'cost_text']]

# Save the cleaned dataset to a CSV file
cleaned_file_path = './data/curated/cleaned_domaindata_name_price.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
