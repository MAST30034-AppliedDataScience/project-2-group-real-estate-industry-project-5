import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx
from adjustText import adjust_text

shapefile_path = './data/raw/SA2_2021_AUST_SHP_GDA2020/SA2_2021_AUST_GDA2020.shp'
increase_rates_path = './data/curated/arima_increase_rates_5_years.csv'

gdf_with_geometry = gpd.read_file(shapefile_path)

increase_rate_data = pd.read_csv(increase_rates_path)

merged_gdf_with_geometry = gdf_with_geometry.merge(increase_rate_data, left_on='SA2_NAME21', right_on='District')

merged_gdf_with_geometry = merged_gdf_with_geometry.to_crs(epsg=3857)

top_10 = merged_gdf_with_geometry.nlargest(10, 'Percentage_Increase').copy()
top_10['Rank'] = range(1, 11)  # Rank from 1 to 10

top_10['centroid'] = top_10.geometry.centroid

fig, ax = plt.subplots(1, 1, figsize=(15, 12))

merged_gdf_with_geometry.plot(column='Percentage_Increase', cmap='YlOrRd', ax=ax, legend=True,
                              legend_kwds={'label': "Increase Rate (5 Years)", 'orientation': "vertical"})

ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=10)

texts = []
for x, y, label, rank in zip(top_10.centroid.x, top_10.centroid.y, top_10['SA2_NAME21'], top_10['Rank']):
    # Add rank and label to the plot
    texts.append(plt.text(x, y, f'#{rank} {label}', fontsize=12, color='black', ha='right', 
                          bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')))

adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))

ax.set_axis_off()

plt.title('Top 10 Increase Rates by SA2 Region (With Basemap)', fontsize=20)

output_plot_path = './plots/increase_rates_map_with_basemap_top10_ranked.png'
plt.savefig(output_plot_path, bbox_inches='tight', dpi=800)

