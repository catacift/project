import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Ruta a tu archivo Excel
file_path = r"C:\Users\Catalina Cifuentes H\OneDrive\Documents\all_breakdown.xlsx"

# Cargar datos
df = pd.read_excel(file_path, engine='openpyxl')

# Seleccionar columnas necesarias
df_prophet = df[['Date', 'Wind Total']].copy()

# Renombrar para Prophet
df_prophet.rename(columns={'Date': 'ds', 'Wind Total': 'y'}, inplace=True)

# Convertir 'ds' a datetime
df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])

# Verificar datos cargados
print(df_prophet.head())

# Crear y entrenar modelo Prophet
model = Prophet()
model.fit(df_prophet)

# Crear dataframe para predecir próximos 30 días
future = model.make_future_dataframe(periods=30)

# Realizar predicción
forecast = model.predict(future)

# Graficar pronóstico
model.plot(forecast)
plt.title('Pronóstico producción eólica (Wind Total)')
plt.show()

# Graficar componentes del modelo (tendencia, estacionalidad)
model.plot_components(forecast)
plt.show()
