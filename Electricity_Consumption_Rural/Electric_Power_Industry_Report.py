import os
import pandas as pd

folder_path = r"C:\Users\Catalina Cifuentes H\Downloads\Electricityconsumption"
file_to_load = "sales2023.xlsx"  # Change if the name has uppercase letters or spaces
file_path = os.path.join(folder_path, file_to_load)

# Open workbook to see sheets
excel_workbook = pd.ExcelFile(file_path)

print("Sheets in the file:")
print(excel_workbook.sheet_names)

# Load the first sheet
sheet_name = excel_workbook.sheet_names[0]
df = pd.read_excel(file_path, sheet_name=sheet_name)

print(f"\nFirst rows of the sheet '{sheet_name}':")
print(df.head())

print("\nStatistical summary:")
print(df.describe(include='all'))
