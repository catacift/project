import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# ✅ Step 1: Set the correct path to your file
file_path = r"C:\Users\Catalina Cifuentes H\OneDrive\Documents\all_breakdown.xlsx"

# ✅ Step 2: Load the Excel file
df = pd.read_excel(file_path, engine='openpyxl')
print(df.head())
print(df.columns)

# ✅ Step 3: Make sure the correct datetime column is used — check your actual column name!
# Replace 'Date' with the real datetime column from print(df.columns) output
df['Date'] = pd.to_datetime(df['Date'])  # <-- CHANGE THIS if your column is e.g. 'Timestamp'
df = df.set_index('Date')
df = df.sort_index()

# ✅ Step 4: Choose the column you want to predict (e.g., temperature, wind speed)
target = 'Wind Total'  # <-- change this to match the column name in your file

# ✅ Step 5: Create "next hour" prediction target
df['target'] = df[target].shift(-1)

# ✅ Step 6: Drop rows with missing target
df = df.dropna()

# ✅ Step 7: Define features (X) and label (y)
X = df.drop('target', axis=1)
y = df['target']

# ✅ Step 8: Split into train/test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

# ✅ Step 9: Train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Step 10: Predict the next hour
y_pred = model.predict(X_test)

# ✅ Step 11: Plot the results
plt.figure(figsize=(12, 6))
plt.plot

plt.plot(y_test.values, label='Real')
plt.plot(y_pred, label='Predicción')
plt.xlabel('Time')
plt.ylabel('Wind Power (MW)')
plt.title('Wind Power Prediction (Next Hour)')
plt.legend(labels=['Actual', 'Prediction'])
plt.show()

from sklearn.metrics import r2_score, mean_squared_error

print("🔍 R2 Score:", r2_score(y_test, y_pred))
print("🔍 Error cuadrático medio (MSE):", mean_squared_error(y_test, y_pred))

importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(10, 5))
plt.barh(features, importances)
plt.title('Feature Importance for Wind Power Prediction')
plt.xlabel('Importance Level')
plt.ylabel('Features')
plt.tight_layout()
plt.show()
plt.barh(features, importances)
plt.title('Feature Importance for Wind Power Prediction')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.show()

