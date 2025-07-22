import pandas as pd
import matplotlib.pyplot as plt

# Full file path
file_path = r'C:\Users\Catalina Cifuentes H\OneDrive\Desktop\sales2023.xlsx'

# Read the file with multiple header rows (3 rows)
df = pd.read_excel(file_path, header=[0, 1, 2])

# Flatten hierarchical columns and clean names
df.columns = [' '.join([str(i).strip() for i in col if str(i) != 'nan']) for col in df.columns]

# Print the flattened columns to confirm
print("Flattened columns:\n", df.columns.tolist())

# Filter necessary columns
state_col = [col for col in df.columns if 'State' in col][0]
sales_col = [col for col in df.columns if 'TOTAL Sales Megawatthours' in col][0]

# Group by state and sum sales
df_grouped = df.groupby(state_col)[sales_col].sum().sort_values(ascending=False)

# Print summary
print("\nTotal sales by state:\n", df_grouped)

# Plot
plt.figure(figsize=(12, 6))
df_grouped.plot(kind='bar', color='skyblue')
plt.title('Total Electricity Sales by State (MWh)')
plt.ylabel('Megawatt-hours')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
