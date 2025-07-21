import geopandas as gpd
import pandas as pd

# Load CAI data (adjust path if needed)
cai_path = r"C:\Users\Catalina Cifuentes H\Downloads\Community_Anchor_Institutions_2022 (1)\Community_Anchor_Institutions_2022.shp"
gdf_cai = gpd.read_file(cai_path)

# Show general info
print("=== Community Anchor Institutions (CAI) ===")
print(f"Total number of institutions: {len(gdf_cai)}")
print("\nList of columns:")
print(gdf_cai.columns)

# Statistical summary for numerical columns
print("\n=== Statistical Description of Numerical Columns ===")
print(gdf_cai.describe())

# Categorical value distributions (top 10)
print("\n=== Categorical Value Distributions ===")
for col in gdf_cai.select_dtypes(include='object').columns:
    print(f"\nTop values in column '{col}':")
    print(gdf_cai[col].value_counts().head(10))

# Save report to text file
report_path = "cai_statistical_report.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("=== Community Anchor Institutions (CAI) ===\n")
    f.write(f"Total number of institutions: {len(gdf_cai)}\n\n")

    f.write("=== Statistical Description of Numerical Columns ===\n")
    f.write(gdf_cai.describe().to_string() + "\n\n")

    f.write("=== Categorical Value Distributions ===\n")
    for col in gdf_cai.select_dtypes(include='object').columns:
        f.write(f"\nTop values in column '{col}':\n")
        f.write(gdf_cai[col].value_counts().head(10).to_string() + "\n")

print(f"\nStatistical report saved as: {report_path}")
