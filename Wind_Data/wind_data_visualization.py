import os
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Create folder to save plots
output_dir = 'winddata_visualizations_NREL'
os.makedirs(output_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv('wtk_site_metadata.csv')

# 1. Histogram of wind speed
plt.figure()
plt.hist(df['wind_speed'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Wind Speed')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Number of Sites')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'histogram_wind_speed.png'))
plt.close()

# 2. Scatter plot: Latitude vs Wind Speed
plt.figure()
plt.scatter(df['latitude'], df['wind_speed'], alpha=0.6, color='green')
plt.title('Latitude vs Wind Speed')
plt.xlabel('Latitude')
plt.ylabel('Wind Speed (m/s)')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'scatter_latitude_wind_speed.png'))
plt.close()

# 3. Boxplot: Wind Speed by State
plt.figure(figsize=(12,6))
df.boxplot(column='wind_speed', by='State', grid=False, rot=45)
plt.title('Wind Speed by State')
plt.suptitle('')  # Remove automatic subtitle
plt.xlabel('State')
plt.ylabel('Wind Speed (m/s)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'boxplot_wind_speed_by_state.png'))
plt.close()

# 4. Geospatial plot of sites colored by Wind Speed
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
ax = gdf.plot(column='wind_speed', cmap='viridis', legend=True, markersize=20)
plt.title('Wind Speed by Site Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'map_wind_speed_by_location.png'))
plt.close()
