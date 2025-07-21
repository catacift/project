import geopandas as gpd
import pandas as pd

fixed_path = r"C:\Users\Catalina Cifuentes H\Downloads\Fixed_Downstream_Consumer_Deployment (1)\Fixed_Downstream_Consumer_Deployment.shp"
cai_path = r"C:\Users\Catalina Cifuentes H\Downloads\Community_Anchor_Institutions_2022 (1)\Community_Anchor_Institutions_2022.shp"

gdf_fixed = gpd.read_file(fixed_path)
gdf_cai = gpd.read_file(cai_path)

if gdf_fixed.crs != gdf_cai.crs:
    gdf_cai = gdf_cai.to_crs(gdf_fixed.crs)

# Spatial join
gdf_join = gpd.sjoin(gdf_cai, gdf_fixed, how="left", predicate="within")

# Eliminar duplicados para mantener solo una fila por institución ancla
gdf_join_unique = gdf_join.drop_duplicates(subset=gdf_cai.index.name)

print(f"Total CAI originales: {len(gdf_cai)}")
print(f"CAI con cobertura asignada (únicos): {gdf_join_unique['index_right'].notna().sum()}")
print(f"CAI sin cobertura asignada (únicos): {gdf_join_unique['index_right'].isna().sum()}")

# Explorar columnas para encontrar posibles datos de velocidad o calidad
print("\nColumnas disponibles en Fixed Downstream Deployment:")
print(gdf_fixed.columns)

# Revisar algunas filas para entender datos
print(gdf_fixed.head())

import geopandas as gpd
import pandas as pd

# Set file paths
fixed_path = r"C:\Users\Catalina Cifuentes H\Downloads\Fixed_Downstream_Consumer_Deployment (1)\Fixed_Downstream_Consumer_Deployment.shp"
cai_path = r"C:\Users\Catalina Cifuentes H\Downloads\Community_Anchor_Institutions_2022 (1)\Community_Anchor_Institutions_2022.shp"

# Load shapefiles
gdf_fixed = gpd.read_file(fixed_path)
gdf_cai = gpd.read_file(cai_path)

# Match CRS if necessary
if gdf_fixed.crs != gdf_cai.crs:
    gdf_cai = gdf_cai.to_crs(gdf_fixed.crs)

# Spatial join to find which CAIs are within coverage areas
gdf_join = gpd.sjoin(gdf_cai, gdf_fixed, how="left", predicate="within")

# Remove duplicates to get one row per CAI
gdf_join_unique = gdf_join.drop_duplicates(subset=gdf_cai.index.name)

# Basic summary printout
print(f"Total original CAIs: {len(gdf_cai)}")
print(f"CAIs with coverage assigned (unique): {gdf_join_unique['index_right'].notna().sum()}")
print(f"CAIs without coverage assigned (unique): {gdf_join_unique['index_right'].isna().sum()}")

# Explore available columns in fixed dataset
print("\nColumns in Fixed Downstream Deployment:")
print(gdf_fixed.columns)
print("\nExample rows:")
print(gdf_fixed.head())

# Print general stats for both datasets
print("\n=== Fixed Downstream Consumer Deployment ===")
print(f"Total records: {len(gdf_fixed)}")
print("\nNumerical statistics:")
print(gdf_fixed.describe())

print("\n=== Community Anchor Institutions ===")
print(f"Total institutions: {len(gdf_cai)}")
print("\nNumerical statistics:")
print(gdf_cai.describe())

# Optional coverage summary
if 'index_right' in gdf_join_unique.columns:
    with_coverage = gdf_join_unique['index_right'].notna().sum()
    without_coverage = gdf_join_unique['index_right'].isna().sum()
else:
    with_coverage = without_coverage = None

# Explore categorical columns
print("\nTop categories in CAIs:")
for col in gdf_cai.select_dtypes(include=['object']).columns:
    print(f"\nTop values for '{col}':")
    print(gdf_cai[col].value_counts().head(10))

# Save report to file
with open("statistical_report.txt", "w", encoding="utf-8") as f:
    f.write("=== Fixed Downstream Consumer Deployment ===\n")
    f.write(f"Total records: {len(gdf_fixed)}\n\n")
    f.write(str(gdf_fixed.describe()) + "\n\n")

    f.write("=== Community Anchor Institutions ===\n")
    f.write(f"Total institutions: {len(gdf_cai)}\n\n")
    f.write(str(gdf_cai.describe()) + "\n\n")

    if with_coverage is not None:
        f.write(f"CAIs with coverage assigned: {with_coverage}\n")
        f.write(f"CAIs without coverage assigned: {without_coverage}\n\n")

    for col in gdf_cai.select_dtypes(include=['object']).columns:
        f.write(f"Top values for '{col}':\n")
        f.write(str(gdf_cai[col].value_counts().head(10)) + "\n\n")

print("\nStatistical report generated: statistical_report.txt")
