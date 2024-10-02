import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

shapefile_path = './data/raw/SA2_2021_AUST_SHP_GDA2020/SA2_2021_AUST_GDA2020.shp'
increase_rates_path = './data/curated/arima_increase_rates_5_years.csv'

gdf_with_geometry = gpd.read_file(shapefile_path)

increase_rate_data = pd.read_csv(increase_rates_path)

merged_gdf_with_geometry = gdf_with_geometry.merge(increase_rate_data, left_on='SA2_NAME21', right_on='District')

merged_gdf_with_geometry = merged_gdf_with_geometry.to_crs(epsg=3857)

fig, ax = plt.subplots(1, 1, figsize=(15, 12))

merged_gdf_with_geometry.plot(column='Percentage_Increase', cmap='YlOrRd', ax=ax, legend=True,
                              legend_kwds={'label': "Increase Rate (5 Years)", 'orientation': "vertical"})

ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=10)

ax.set_axis_off()

plt.title('Increase Rates by SA2 Region (With Basemap)', fontsize=20)

output_plot_path = './plots/increase_rates_map_with_basemap.png'
plt.savefig(output_plot_path, bbox_inches='tight', dpi=800)

