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
import os
import geopandas as gpd
import matplotlib.pyplot as plt

# Define the base path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the shapefile
districts = gpd.read_file(os.path.join(BASE, 'raw_data', 'tl_2023_06_unsd.shp'))

# Basic visualization with geopandas
districts.plot(figsize=(12, 8), edgecolor='black', facecolor='lightblue')

# Add title and axis labels, then show
plt.title("School Districts Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
import os
import geopandas as gpd
import matplotlib.pyplot as plt

# ... your code to load data and create the plot ...

# Define the base path (adjust if your folder structure changes)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE, 'stage_1_diagnosis', 'outputs')

# Create the folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Create the figure and plot
fig, ax = plt.subplots(figsize=(12, 8))
districts.plot(ax=ax, edgecolor='black', facecolor='lightblue')
ax.set_title("School Districts Map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Save the image
plt.savefig(os.path.join(output_dir, 'school_districts_map.png'), dpi=300)
# ... your code to load data ...

fig, ax = plt.subplots(figsize=(12, 8))
districts.plot(ax=ax, edgecolor='black', facecolor='lightblue')
ax.set_title("School Districts Map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Save the image and print confirmation here
output_path = os.path.join(output_dir, 'school_districts_map.png')
plt.savefig(output_path, dpi=300)
print(f"✅ Image saved at: {output_path}")

plt.show()

plt.show()
output_path = os.path.join(output_dir, 'school_districts_map.png')
print("Saving image to:", output_dir)
plt.savefig(output_path, dpi=300)
print(f"✅ Image saved at: {output_path}")
