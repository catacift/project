import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 1. Load public schools CSV, skipping initial metadata rows
schools_csv_path = r"C:\Users\Catalina Cifuentes H\Downloads\pubschls.csv"
schools_df = pd.read_csv(schools_csv_path, skiprows=5, encoding='utf-8-sig', dtype={'CDSCode': str})

# 2. Clean latitude and longitude columns
schools_df = schools_df.dropna(subset=["Latitude", "Longitude"])
schools_df["Latitude"] = pd.to_numeric(schools_df["Latitude"], errors='coerce')
schools_df["Longitude"] = pd.to_numeric(schools_df["Longitude"], errors='coerce')
schools_df = schools_df.dropna(subset=["Latitude", "Longitude"])

# 3. Create GeoDataFrame for schools
schools_gdf = gpd.GeoDataFrame(
    schools_df,
    geometry=gpd.points_from_xy(schools_df["Longitude"], schools_df["Latitude"]),
    crs="EPSG:4326"
)

# 4. Load wind turbines CSV
turbines_csv_path = r"C:\Users\Catalina Cifuentes H\Downloads\uswtdb_V8_1_20250522.csv"
turbines_df = pd.read_csv(turbines_csv_path)
turbines_df = turbines_df.dropna(subset=["ylat", "xlong"])
turbines_df["ylat"] = pd.to_numeric(turbines_df["ylat"], errors='coerce')
turbines_df["xlong"] = pd.to_numeric(turbines_df["xlong"], errors='coerce')
turbines_df = turbines_df.dropna(subset=["ylat", "xlong"])

turbines_gdf = gpd.GeoDataFrame(
    turbines_df,
    geometry=gpd.points_from_xy(turbines_df["xlong"], turbines_df["ylat"]),
    crs="EPSG:4326"
)

# 5. Reproject to projected CRS for accurate distance calculations (meters)
schools_gdf_proj = schools_gdf.to_crs(epsg=3310)   # California Albers
turbines_gdf_proj = turbines_gdf.to_crs(epsg=3310)

# 6. Calculate minimum distance to nearest turbine in kilometers
def distance_to_nearest_turbine(point, turbines_gdf_proj):
    return turbines_gdf_proj.distance(point).min() / 1000  # meters to km

schools_gdf_proj["distance_km"] = schools_gdf_proj.geometry.apply(
    lambda point: distance_to_nearest_turbine(point, turbines_gdf_proj)
)

# 7. Categorize schools by distance
def categorize_distance(distance):
    if distance <= 5:
        return "near (<5 km)"
    elif distance >= 10:
        return "far (>10 km)"
    else:
        return "medium (5-10 km)"

schools_gdf_proj["distance_category"] = schools_gdf_proj["distance_km"].apply(categorize_distance)

# 8. Save results to CSV
output_csv_path = r"C:\Users\Catalina Cifuentes H\Downloads\schools_with_distances.csv"
schools_gdf_proj.to_csv(output_csv_path, index=False)

# 9. Print summary
print("Schools classified by distance to nearest wind turbine:")
print(schools_gdf_proj["distance_category"].value_counts())
