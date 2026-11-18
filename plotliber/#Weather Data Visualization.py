#Weather Data Visualization
"""Task: Plot a line chart of average daily temperature over a month for your city.
Data: Use dummy or real weather data (e.g., from OpenWeatherMap API).
Skills: Line plots, axes labeling, grid, date formatting.
✅ Bonus: Add a second line for humidity on the same plot using twin axes (twinx())."""
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Create dates as list of datetime objects
start_date = datetime(2025, 7, 1)
dates = [start_date + timedelta(days=i) for i in range(7)]

# Convert dates to strings for plotting labels
date_labels = [d.strftime('%Y-%m-%d') for d in dates]

# Dummy weather data (7 days)
temperature = np.array([30, 32, 29, 28, 31, 33, 34])
humidity = np.array([60, 55, 65, 70, 50, 45, 40])
rainfall = np.array([0, 5, 2, 8, 0, 0, 1])
wind_speed = np.array([10, 12, 9, 11, 14, 13, 10])
condition = ["Sunny", "Partly Cloudy", "Rainy", "Rainy", "Sunny", "Sunny", "Partly Cloudy"]
plt.figure(figsize=(10, 5))

plt.plot(date_labels, temperature, marker='o', label="Temperature (°C)", color='red')
plt.plot(date_labels, humidity, marker='s', label="Humidity (%)", color='blue')

plt.title("Temperature and Humidity Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
