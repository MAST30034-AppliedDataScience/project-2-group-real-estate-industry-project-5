import pandas as pd
import geopandas as gpd
from geopy.distance import geodesic
from tqdm import tqdm

closest_stations_path = './data/curated/updated_closest_stations.csv'
sa2_shapefile_path = './data/raw/SA2_2021_AUST_SHP_GDA2020/SA2_2021_AUST_GDA2020.shp'

closest_stations = pd.read_csv(closest_stations_path)

sa2_districts = gpd.read_file(sa2_shapefile_path)

closest_stations_gdf = gpd.GeoDataFrame(
    closest_stations, 
    geometry=gpd.points_from_xy(closest_stations['Property Longitude'], closest_stations['Property Latitude']),
    crs="EPSG:4326"
)

vic_sa2_districts = sa2_districts[sa2_districts['STE_NAME21'] == 'Victoria']

if vic_sa2_districts.crs != "EPSG:4326":
    vic_sa2_districts = vic_sa2_districts.to_crs(epsg=4326)

properties_with_sa2 = gpd.sjoin(closest_stations_gdf, vic_sa2_districts, how="left", predicate="within")

properties_with_sa2 = properties_with_sa2[['Property Name', 'Property Latitude', 'Property Longitude', 
                                           'Closest Station', 'Distance (km)', 'cost_text', 'Closest School', 
                                           'School Distance (km)', 'SA2_NAME21']]

output_sa2_path = './data/curated/properties_with_sa2_districts.csv'
properties_with_sa2.to_csv(output_sa2_path, index=False)

