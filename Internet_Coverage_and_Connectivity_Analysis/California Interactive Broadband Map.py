import geopandas as gpd
import matplotlib.pyplot as plt

# Path to your shapefile
shapefile_path = r"C:\Users\Catalina Cifuentes H\Downloads\Fixed_Downstream_Consumer_Deployment\Fixed_Downstream_Consumer_Deployment.shp"

try:
    # Load shapefile
    gdf = gpd.read_file(shapefile_path)
    print("✅ Shapefile loaded successfully!\n")

    # Show basic info
    print("🧾 Columns available:", gdf.columns.tolist())
    print("\n📍 First 5 rows:\n", gdf.head())
    print("\n📏 CRS:", gdf.crs)

    # Plot full map
    gdf.plot(figsize=(12, 10), edgecolor='gray', alpha=0.6)
    plt.title("📡 Fixed Downstream Consumer Deployment (All California)")
    plt.show()

    # 🔹 1. Count by provider (ISP)
    print("\n🔹 Top Internet Providers (by number of deployments):")
    print(gdf['PROVNAME'].value_counts())

    # 🔹 2. Filter: only San Diego County
    san_diego = gdf[gdf['COUNTY'].str.upper() == 'SAN DIEGO']
    print("\n📍 San Diego records:", len(san_diego))
    print(san_diego.head())

    # 🔹 3. Filter: speeds ≥ 100 Mbps
    fast_connections = gdf[gdf['MAXADDOWN'] >= 100]
    print("\n⚡ Connections ≥ 100 Mbps:")
    print(fast_connections[['PROVNAME', 'MAXADDOWN']].head())

    # 🔹 4. Plot only San Diego
    san_diego.plot(figsize=(12, 8), edgecolor='black', alpha=0.5)
    plt.title("📍 Internet Coverage in San Diego County")
    plt.show()

except FileNotFoundError:
    print(f"❌ File not found: {shapefile_path}")
except Exception as e:
    print(f"🚨 Error: {e}")
