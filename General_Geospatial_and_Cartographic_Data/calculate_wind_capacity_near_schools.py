import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load turbines CSV
turbines_df = pd.read_csv(r"C:\Users\Catalina Cifuentes H\PycharmProjects\New Project 9_7_2025\General_Geospatial_and_Cartographic_Data\uswtdb_V8_1_20250522.csv")

# Create geometry for turbines from xlong and ylat
turbines_geometry = [Point(xy) for xy in zip(turbines_df['xlong'], turbines_df['ylat'])]
turbines_gdf = gpd.GeoDataFrame(turbines_df, geometry=turbines_geometry)

# Load schools CSV (replace with your actual schools CSV path)
schools_df = pd.read_csv(r"C:\Users\Catalina Cifuentes H\PycharmProjects\New Project 9_7_2025\General_Geospatial_and_Cartographic_Data\uswtdb_V8_1_20250522.csv")

# Create geometry for schools from x

import matplotlib.pyplot as plt

# Set the coordinate reference system (CRS)
turbines_gdf.set_crs(epsg=4326, inplace=True)

# Plot the turbines
fig, ax = plt.subplots(figsize=(10, 10))
turbines_gdf.plot(ax=ax, markersize=1, color='red', alpha=0.6, label='Wind Turbines')

# Customize plot
ax.set_title('Wind Turbine Locations in the US', fontsize=14)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# Load schools CSV (replace with correct path)
schools_df = pd.read_csv(r"C:\path\to\your\schools.csv")

# Create geometry for schools from longitude and latitude columns
schools_geometry = [Point(xy) for xy in zip(schools_df['longitude_column'], schools_df['latitude_column'])]
schools_gdf = gpd.GeoDataFrame(schools_df, geometry=schools_geometry)
schools_gdf.set_crs(epsg=4326, inplace=True)

# Load schools CSV (replace with correct path)
schools_df = pd.read_csv(r"C:\path\to\your\schools.csv")

# Create geometry for schools from longitude and latitude columns
schools_geometry = [Point(xy) for xy in zip(schools_df['longitude_column'], schools_df['latitude_column'])]
schools_gdf = gpd.GeoDataFrame(schools_df, geometry=schools_geometry)
schools_gdf.set_crs(epsg=4326, inplace=True)
