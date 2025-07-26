import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, 'raw_data', 'pubschls.xlsx')
output_path = os.path.join(BASE_DIR, 'cleaned_data', 'schools_sandiego.csv')


df = pd.read_excel(input_path, skiprows=5)

print("✅ File loaded successfully. First few rows:")
print(df.head())

print("\n📌 Column names:")
print(df.columns.tolist())


if 'County' in df.columns:
    df_sandiego = df[df['County'].str.strip().str.upper() == 'SAN DIEGO']
    df_sandiego.to_csv(output_path, index=False)
    print(f"\n✅ Found {len(df_sandiego)} schools in San Diego County.")
    print(f"📁 File saved to: {output_path}")
else:
    print("❌ Column 'County' not found. Please check column names above.")
