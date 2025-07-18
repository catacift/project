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

    # Create geometry for schools from xlong and ylat (since your columns are named like that)
    schools_geometry = [Point(xy) for xy in zip(schools_df['xlong'], schools_df['ylat'])]
    schools_gdf = gpd.GeoDataFrame(schools_df, geometry=schools_geometry)

    # Create 5 km buffer around schools
    schools_gdf['buffer_5km'] = schools_gdf.geometry.buffer(5000)

    # Set buffer as active geometry for spatial join
    schools_buffer = schools_gdf.set_geometry('buffer_5km')

    # Perform spatial join: turbines within 5 km buffer of schools
    joined = gpd.sjoin(turbines_gdf, schools_buffer, how='inner', predicate='intersects')

    # Sum capacity of turbines within 5 km of schools
    total_capacity_near_schools = joined['t_cap'].sum()  # Note: using 't_cap' based on your columns

    print(f"Total wind turbine capacity within 5 km of schools: {total_capacity_near_schools} MW")
