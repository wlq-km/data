import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Read the CSV files
temperature_df = pd.read_csv("temperature.csv")
humidity_df    = pd.read_csv("humidity.csv")
pressure_df    = pd.read_csv("pressure.csv")

temperature_df["time"] = pd.to_datetime(
    temperature_df["time"],
    format="mixed",
    utc=True
)

humidity_df["time"] = pd.to_datetime(
    humidity_df["time"],
    format="mixed",
    utc=True
)

pressure_df["time"] = pd.to_datetime(
    pressure_df["time"],
    format="mixed",
    utc=True
)


# Find the beginning of the complete acquisition
start_time = min(
    temperature_df["time"].min(),
    humidity_df["time"].min(),
    pressure_df["time"].min()
)

print("Beginning of acquisition:", start_time)


# Convert timestamps to days since the beginning
seconds_per_day = 24 * 60 * 60

temperature_days = (
    temperature_df["time"] - start_time
).dt.total_seconds().to_numpy() / seconds_per_day

humidity_days = (
    humidity_df["time"] - start_time
).dt.total_seconds().to_numpy() / seconds_per_day

pressure_days = (
    pressure_df["time"] - start_time
).dt.total_seconds().to_numpy() / seconds_per_day


# Convert measurements to NumPy arrays
temperature = temperature_df["temperature"].to_numpy()
humidity = humidity_df["humidity"].to_numpy()
pressure = pressure_df["pressure"].to_numpy()


# Generate the plots
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(temperature_days, temperature, ".-", markersize=2, linewidth=0.5)
plt.ylabel("Temperature / °C")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(humidity_days, humidity, ".-", markersize=2, linewidth=0.5)
plt.ylabel("Humidity / %")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(pressure_days, pressure, ".-", markersize=2, linewidth=0.5)
plt.xlabel("Time since beginning / days")
plt.ylabel("Pressure")
plt.grid()

plt.tight_layout()
plt.show()
