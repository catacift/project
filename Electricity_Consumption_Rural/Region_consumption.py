import os
import pandas as pd
import matplotlib.pyplot as plt

folder_path = r"C:\Users\Catalina Cifuentes H\Downloads\Electricityconsumption"
file_name = "sales2023.xlsx"
file_path = os.path.join(folder_path, file_name)

# Load Excel workbook and list sheets
excel_workbook = pd.ExcelFile(file_path)
print("Available sheets:", excel_workbook.sheet_names)

# Load the first sheet (or specify sheet name)
sheet_name = excel_workbook.sheet_names[0]
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Check columns to confirm
print("\nColumns available in dataset:")
print(df.columns)

# Group data by 'State' and sum the 'Megawatthours' consumption
state_consumption = df.groupby('State')['Megawatthours'].sum().reset_index()

print("\nTotal Megawatthours consumption by State:")
print(state_consumption)

# Plot total consumption by State
plt.figure(figsize=(12,6))
plt.bar(state_consumption['state'], state_consumption['Megawatthours'], color='skyblue')
plt.title('Total Megawatthours Consumption by State')
plt.xlabel('State')
plt.ylabel('Total Megawatthours')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
