import pandas as pd
from sklearn.linear_model import LinearRegression

# Mock Meteorological Data
# Features: Humidity (%), Pressure (hPa). Target: Temp (C)
df = pd.DataFrame({
    'Humidity': [80, 60, 75, 40, 90],
    'Pressure': [1012, 1015, 1010, 1020, 1008],
    'Temperature': [28, 32, 29, 35, 26]
})

X = df[['Humidity', 'Pressure']]
y = df['Temperature']

model = LinearRegression()
model.fit(X, y)

# Predict weather for 70% humidity and 1014 hPa pressure
new_data = pd.DataFrame({'Humidity': [70], 'Pressure': [1014]})
predicted_temp = model.predict(new_data)
print(f"Predicted Temperature: {predicted_temp[0]:.2f}°C")