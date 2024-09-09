import json
import re
import os


# Function to normalize the price to per week
def normalize_price(price_text):
    # Check if the price is per annum (annual), indicated by "p.a."
    if "p.a." in price_text.lower():
        # Extract the numeric part using regex
        price_match = re.search(r'\$?([\d,]+)', price_text)
        if price_match:
            annual_price = int(price_match.group(1).replace(',', ''))
            weekly_price = annual_price / 52  # Convert to per week
            return f"${weekly_price:.2f} per week"
    
    # If the price is already weekly, return it
    elif "pw" in price_text.lower() or "per week" in price_text.lower():
        return price_text
    
    # Handle other formats that may not be weekly or annual
    else:
        return price_text

# Load the JSON file
with open('./data/raw/merged_domaindata.json', 'r') as file:
    data = json.load(file)

# Track the number of original entries
original_count = len(data)

# Create a set to track unique addresses
unique_addresses = set()

# Dictionary to store the cleaned data
cleaned_data = {}

# Iterate over the entries in the data
for key, entry in data.items():
    address = entry['name']  # The address field to check for duplicates
    price_text = entry.get('cost_text', '')  # Get the price field

    # Check if price_text contains any numbers (skip if it doesn't)
    if re.search(r'\d+', price_text):
        # Normalize the price to per week
        normalized_price = normalize_price(price_text)
    
        # Update the price in the entry
        entry['cost_text'] = normalized_price

        # If the address is unique, add it to the cleaned_data and mark it as seen
        if address not in unique_addresses:
            unique_addresses.add(address)
            cleaned_data[key] = entry

cleaned_count = len(cleaned_data)

entries_removed = original_count - cleaned_count

os.makedirs('./data/curated', exist_ok=True)
output_path = './data/curated/cleaned_domaindata_with_prices.json'

with open(output_path, 'w') as outfile:
    json.dump(cleaned_data, outfile, indent=4)

print(f"Cleaned data with normalized prices saved to 'cleaned_domaindata_with_prices.json'.")
print(f"Original entries: {original_count}")
print(f"Cleaned entries: {cleaned_count}")
print(f"Entries removed: {entries_removed}")
