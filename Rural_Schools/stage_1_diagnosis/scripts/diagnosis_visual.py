import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, 'cleaned_data', 'schools_sandiego.csv')

# Load the CSV data
df = pd.read_csv(input_path)

# Check if FundingType column exists
if 'FundingType' in df.columns:
    # Count schools by FundingType
    funding_counts = df['FundingType'].value_counts()

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    funding_counts.plot(kind='bar', color='skyblue')
    plt.title('Count of Schools by Funding Type in San Diego County')
    plt.xlabel('Funding Type')
    plt.ylabel('Number of Schools')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("❌ 'FundingType' column not found in the dataset.")
