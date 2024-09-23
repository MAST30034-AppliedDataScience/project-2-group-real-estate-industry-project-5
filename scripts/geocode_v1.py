import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep
from tqdm import tqdm

file_path = './data/curated/cleaned_domaindata_name_price.csv'
df = pd.read_csv(file_path)

geolocator = Nominatim(user_agent="geoapi")

def get_geocode(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return (None, None)
    except Exception as e:
        return (None, None)

# tqdm progress bar
tqdm.pandas()
df['geocode'] = df['name'].progress_apply(get_geocode)

df['latitude'] = df['geocode'].apply(lambda x: x[0] if x else None)
df['longitude'] = df['geocode'].apply(lambda x: x[1] if x else None)

df.drop(columns=['geocode'], inplace=True)

output_file_path = './data/curated/cleaned_domaindata_with_geocode.csv'
df.to_csv(output_file_path, index=False)