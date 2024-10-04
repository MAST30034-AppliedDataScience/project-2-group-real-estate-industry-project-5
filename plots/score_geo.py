import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

# File paths
shapefile_path = './data/raw/SA2_2021_AUST_SHP_GDA2020/SA2_2021_AUST_GDA2020.shp'
liveability_scores_path = './data/curated/liveability_scores_with_pca_weights.csv'

# Load the shapefile with geometries
gdf_with_geometry = gpd.read_file(shapefile_path)

# Load the liveability scores data
liveability_data = pd.read_csv(liveability_scores_path)

# Merge the shapefile data with the liveability scores
merged_gdf_with_geometry = gdf_with_geometry.merge(liveability_data, on='SA2_NAME21')

# Convert the GeoDataFrame to Web Mercator (EPSG:3857) which is needed for basemap overlays
merged_gdf_with_geometry = merged_gdf_with_geometry.to_crs(epsg=3857)

# Create a larger, more visually appealing plot
fig, ax = plt.subplots(1, 1, figsize=(15, 12))

# Plot the liveability scores
merged_gdf_with_geometry.plot(column='Liveability Score', cmap='coolwarm', ax=ax, legend=True,
                              legend_kwds={'label': "Liveability Score", 'orientation': "vertical"})

# Use OpenStreetMap as a fallback for the basemap
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=10)

# Remove axis for a cleaner plot
ax.set_axis_off()

# Set the title with a larger font size
plt.title('Liveability Scores by SA2 Region (With Basemap)', fontsize=20)

# Save the plot to a file with high resolution
output_plot_path = './plots/liveability_scores_map_with_basemap.png'
plt.savefig(output_plot_path, bbox_inches='tight', dpi=300)

# Show the plot
plt.show()
