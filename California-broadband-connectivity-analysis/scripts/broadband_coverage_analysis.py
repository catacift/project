import geopandas as gpd

# Paths to the shapefiles
fixed_coverage_path = r"C:\Users\Catalina Cifuentes H\Downloads\Fixed_Downstream_Consumer_Deployment (1)\Fixed_Downstream_Consumer_Deployment.shp"
anchor_institutions_path = r"C:\Users\Catalina Cifuentes H\Downloads\Community_Anchor_Institutions_2022 (1)\Community_Anchor_Institutions_2022.shp"

# Load shapefiles
gdf_fixed_coverage = gpd.read_file(fixed_coverage_path)
gdf_anchors = gpd.read_file(anchor_institutions_path)

# Ensure both GeoDataFrames use the same CRS
if gdf_fixed_coverage.crs != gdf_anchors.crs:
    gdf_anchors = gdf_anchors.to_crs(gdf_fixed_coverage.crs)

# Perform spatial join: find anchors within broadband coverage polygons
joined_gdf = gpd.sjoin(gdf_anchors, gdf_fixed_coverage, how='left', predicate='within')

# Mark anchors that have coverage (those with a match in the coverage polygons)
joined_gdf['has_coverage'] = ~joined_gdf['index_right'].isna()

# Filter anchors without coverage
anchors_without_coverage = joined_gdf[joined_gdf['has_coverage'] == False].copy()

# Save institutions without coverage to CSV
anchors_without_coverage.to_csv("anchors_without_coverage.csv", index=False)

# Print summary
print(f"Total anchor institutions: {len(gdf_anchors)}")
print(f"Anchor institutions with coverage: {joined_gdf['has_coverage'].sum()}")
print(f"Anchor institutions without coverage: {len(anchors_without_coverage)}")
print("CSV file 'anchors_without_coverage.csv' generated successfully.")
