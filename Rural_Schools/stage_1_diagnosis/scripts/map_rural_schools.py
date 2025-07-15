import os
import pandas as pd
import folium

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, 'cleaned_data', 'schools_sandiego.csv')
results_folder = os.path.join(BASE_DIR, 'results')
output_map = os.path.join(results_folder, 'map_schools_rural.html')

# Crear carpeta results si no existe
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

df = pd.read_csv(input_path)

rural_zips = ['91962', '91963', '91977', '92036', '92061', '92065', '92067', '92078', '92082', '92083']

df_rural = df[df['Zip'].astype(str).isin(rural_zips)]

print(f"Number of rural schools found: {len(df_rural)}")

map_rural = folium.Map(location=[32.7157, -117.1611], zoom_start=9)

for _, row in df_rural.iterrows():
    try:
        lat = float(row['Latitude'])
        lon = float(row['Longitude'])
        folium.Marker(
            location=[lat, lon],
            popup=f"{row['School']} ({row['Zip']})",
            icon=folium.Icon(color='green', icon='school', prefix='fa')
        ).add_to(map_rural)
    except (ValueError, TypeError):
        continue

map_rural.save(output_map)
print(f"Map saved at: {output_map}")
