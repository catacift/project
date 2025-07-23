import pandas as pd
import geopandas as gpd
import folium

# Load the processed CSV with distance info
csv_path = r"C:\Users\Catalina Cifuentes H\Downloads\schools_with_distances.csv"
df = pd.read_csv(csv_path)

# Create GeoDataFrame from longitude and latitude columns
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]),
    crs="EPSG:4326"
)

# Initialize Folium map centered roughly in California
m = folium.Map(location=[36.7783, -119.4179], zoom_start=6, tiles="CartoDB positron")

# Define color mapping for distance categories
color_dict = {
    "near (<5 km)": "green",
    "medium (5-10 km)": "orange",
    "far (>10 km)": "red"
}

# Add school points to the map with color-coded markers
for _, row in gdf.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=4,
        color=color_dict.get(row["distance_category"], "blue"),
        fill=True,
        fill_opacity=0.7,
        popup=(
            f"School: {row['School']}<br>"
            f"Distance to Turbine: {row['distance_km']:.2f} km<br>"
            f"Category: {row['distance_category']}"
        )
    ).add_to(m)

# Save the map to an HTML file
map_output_path = r"C:\Users\Catalina Cifuentes H\Downloads\schools_wind_turbines_map.html"
m.save(map_output_path)

print(f"Interactive map saved to: {map_output_path}")
