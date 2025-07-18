import os
import pandas as pd

# Step 1: List files in Downloads folder
downloads_folder = r"C:\Users\Catalina Cifuentes H\Downloads"
files = os.listdir(downloads_folder)

print("Files in your Downloads folder:")
for file in files:
    print(file)

# Step 2: Ask user to input the exact filename including extension
filename = input("\nEnter the exact filename (including extension) from the list above: ")

file_path = os.path.join(downloads_folder, filename)

# Step 3: Load file depending on extension
try:
    if filename.lower().endswith('.xlsx') or filename.lower().endswith('.xls'):
        df = pd.read_excel(file_path)
    elif filename.lower().endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file extension. Please use .xlsx, .xls, or .csv files.")

    # Step 4: Show first rows
    print("\nFile loaded successfully. Here are the first rows:")
    print(df.head())

except FileNotFoundError:
    print(f"\nError: File not found at path:\n{file_path}")
except Exception as e:
    print(f"\nAn error occurred while loading the file: {e}")

