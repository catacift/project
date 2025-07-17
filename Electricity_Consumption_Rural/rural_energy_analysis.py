import os
import pandas as pd
import matplotlib.pyplot as plt

# Define relative path to the data file
file_name = 'eia861_data.csv'

# Build full file path (useful if running from another location)
file_path = os.path.join(os.path.dirname(__file__), file_name)

# Load the dataset
try:
    df = pd.read_csv(file_path)
    print(f"File '{file_name}' loaded successfully.\n")
except FileNotFoundError:
    print(f"File '{file_name}' not found in directory {os.path.dirname(__file__)}")
    exit()

# Show first rows to verify data load
print("Preview of the data:")
print(df.head())

# Check column names to adapt if needed
print("\nColumns in dataset:")
print(df.columns)

# FILTER: Example filtering data for California (adjust 'STATE' if column name differs)
state_code = 'CA'
if 'STATE' in df.columns:
    df_state = df[df['STATE'] == state_code]
else:
    print("Column 'STATE' not found. Please check column names.")
    exit()

print(f"\nData filtered for state: {state_code}")
print(df_state.head())

# ANALYSIS: Sum of sales/consumption by sector (adjust 'SECTOR' and 'SALES' if needed)
if {'SECTOR', 'SALES'}.issubset(df_state.columns):
    consumption_by_sector = df_state.groupby('SECTOR')['SALES'].sum()
    print("\nTotal electricity sales by sector:")
    print(consumption_by_sector)

    # Bar plot of consumption by sector
    consumption_by_sector.plot(kind='bar', title=f'Electricity Sales by Sector in {state_code}')
    plt.ylabel('Sales (MWh or dataset units)')
    plt.tight_layout()
    plt.show()
else:
    print("Columns 'SECTOR' and/or 'SALES' not found. Please check column names.")
