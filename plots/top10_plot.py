import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx
from adjustText import adjust_text

# File paths
shapefile_path = './data/raw/SA2_2021_AUST_SHP_GDA2020/SA2_2021_AUST_GDA2020.shp'
liveability_scores_path = './data/curated/liveability_scores.csv'

# Load the shapefile with geometries
gdf_with_geometry = gpd.read_file(shapefile_path)

# Load the liveability scores data
liveability_data = pd.read_csv(liveability_scores_path)

# Merge the shapefile data with the liveability scores
merged_gdf_with_geometry = gdf_with_geometry.merge(liveability_data, on='SA2_NAME21')

# Convert the GeoDataFrame to Web Mercator (EPSG:3857) which is needed for basemap overlays
merged_gdf_with_geometry = merged_gdf_with_geometry.to_crs(epsg=3857)

# Sort and select the top 10 regions by liveability score and assign ranks
top_10 = merged_gdf_with_geometry.nlargest(10, 'Liveability Score').copy()
top_10['Rank'] = range(1, 11)  # Rank from 1 to 10

# Calculate the centroids of the polygons for labeling
top_10['centroid'] = top_10.geometry.centroid

# Create a larger, more visually appealing plot
fig, ax = plt.subplots(1, 1, figsize=(15, 12))

# Plot the liveability scores
merged_gdf_with_geometry.plot(column='Liveability Score', cmap='coolwarm', ax=ax, legend=True,
                              legend_kwds={'label': "Liveability Score", 'orientation': "vertical"})

# Use OpenStreetMap as a fallback for the basemap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=10)

# Prepare text labels with rank for adjustment
texts = []
for x, y, label, rank in zip(top_10.centroid.x, top_10.centroid.y, top_10['SA2_NAME21'], top_10['Rank']):
    texts.append(plt.text(x, y, f'#{rank} {label}', fontsize=12, color='black', ha='right', 
                          bbox=dict(facecolor='white', alpha=0.5, edgecolor='none')))

# Adjust text positions to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))

# Remove axis for a cleaner plot
ax.set_axis_off()

# Set the title with a larger font size
plt.title('Top 10 Liveability Scores by SA2 Region (With Basemap)', fontsize=20)

output_plot_path = './plots/liveability_scores_map_with_basemap_top10_ranked.png'
plt.savefig(output_plot_path, bbox_inches='tight', dpi=300)
