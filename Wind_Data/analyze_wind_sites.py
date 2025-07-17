import os
import pandas as pd

# Mostrar directorio actual para confirmar
print("Current working directory:", os.getcwd())

csv_path = 'wtk_site_metadata.csv'

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    print("\nFile loaded successfully. Here are the first rows:\n")
    print(df.head())
else:
    print(f"The file '{csv_path}' was NOT found in the current directory.")
