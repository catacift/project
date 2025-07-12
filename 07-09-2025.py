import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# ✅ Load your dataset (update path as needed)
file_path = "C://Users//Catalina Cifuentes H//OneDrive//all_breakdown.csv"
df = pd.read_csv(file_path)

# Convert TIMESTAMP to datetime
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df = df.sort_values('TIMESTAMP').reset_index(drop=True)

# Create the target variable: wind production one hour ahead
df['WIND_NEXT_HOUR'] = df['WIND TOTAL'].shift(-1)

# Select features and drop NaNs
features = ['BIOGAS', 'BIOMASS', 'GEOTHERMAL', 'Hour', 'SMALL HYDRO', 'SOLAR']
df_clean = df.dropna(subset=features + ['WIND TOTAL', 'WIND_NEXT_HOUR'])

# Define feature matrix and target vector
X = df_clean[features]
y = df_clean['WIND_NEXT_HOUR']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"MAE: {mae:.2f}")

# Plot actual vs predicted for the last 24 hours
plt.figure(figsize=(12, 6))
plt.plot(y_test.values[-24:], label='Actual', marker='o')
plt.plot(y_pred[-24:], label='Predicted', marker='x')
plt.title(f'Next-Hour Wind Energy Prediction (MAE: {mae:.2f})')
plt.xlabel('Hour')
plt.ylabel('Wind Energy (MWh)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
