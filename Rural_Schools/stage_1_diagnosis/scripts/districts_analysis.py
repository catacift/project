import os
import geopandas as gpd

# Define the base path to the stage_1_diagnosis folder
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load shapefile (if using the Census TIGER/Line data)
districts = gpd.read_file(os.path.join(BASE, 'raw_data', 'tl_2023_06_unsd.shp'))

# 👉 If you're using a GeoJSON instead, use this line instead:
# districts = gpd.read_file(os.path.join(BASE, 'raw_data', 'districts_2018.geojson'))

# Preview data
print("✅ School districts loaded:", len(districts))
print("📌 Available columns:", districts.columns.tolist())

# Optional: Save as GeoJSON to make it easier to use later
output_path = os.path.join(BASE, 'cleaned_data', 'districts.geojson')
districts.to_file(output_path, driver='GeoJSON')
print("📁 File saved to:", output_path)
