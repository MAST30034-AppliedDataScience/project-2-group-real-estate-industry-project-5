import json

# File paths for all the JSON files you want to merge
file_paths = [
    './data/raw/domaindata_new.json',
    './data/raw/domaindata_new_2.json',
    './data/raw/domaindata_new_3.json',
    './data/raw/domaindata_new_4.json',
    './data/raw/domaindata_new_5.json'
]

# Initialize a dictionary to hold merged data
merged_data = {}

# Loop through the file paths, load the data, and merge it
for file_path in file_paths:
    with open(file_path, 'r') as f:
        data = json.load(f)
        merged_data.update(data)

# Save the merged data to a new JSON file
output_path = './data/raw/merged_domaindata.json'
with open(output_path, 'w') as output_file:
    json.dump(merged_data, output_file)

print(f"Merged file saved to {output_path}")
