from influxdb_client import InfluxDBClient
import pandas as pd
from datetime import datetime, timezone

# Convert Unix time stamps to iso time for the influxDB query
timestamp_start = 1785505110
timestamp_stop = 1786975920
iso_time_start = (
    datetime
    .fromtimestamp(timestamp_start, timezone.utc)
    .strftime("%Y-%m-%dT%H:%M:%SZ")
)
iso_time_stop = (
    datetime
    .fromtimestamp(timestamp_stop, timezone.utc)
    .strftime("%Y-%m-%dT%H:%M:%SZ")
)

# influxDB info
client = InfluxDBClient(
    url="http://134.157.35.7:8086",
    token="A-ZcHVGJsRSotigQICwj9sKeARx-Dv-JkwoFQQUKqL7xT8kpDiSqm0DfDP2VU9v748-cy6kPMqVX23xAA1LUSg==",
    org="Welinq"
)


# Get the data
# temperature
query = f"""
from(bucket: "Monitoring")
  |> range(start: {iso_time_start}, stop: {iso_time_stop})
  |> filter(fn: (r) =>
      r["_measurement"] == "Data" and
      r["_field"] == "temperature" and
      r["Port"] == "brick_2_port_d")
  |> keep(columns: ["_time", "_value"])
"""
temp = client.query_api().query_data_frame(query)
temp = temp[["_time", "_value"]]
temp.columns = ["time", "temperature"]
temp.to_csv("temperature.csv", index=False)

# humidity
query = f"""
from(bucket: "Monitoring")
  |> range(start: {iso_time_start}, stop: {iso_time_stop})
  |> filter(fn: (r) =>
      r["_measurement"] == "Data" and
      r["_field"] == "humidity" and
      r["Port"] == "brick_1_port_a")
  |> keep(columns: ["_time", "_value"])
"""
temp = client.query_api().query_data_frame(query)
temp = temp[["_time", "_value"]]
temp.columns = ["time", "humidity"]
temp.to_csv("humidity.csv", index=False)

# pressure
query = f"""
from(bucket: "Monitoring")
  |> range(start: {iso_time_start}, stop: {iso_time_stop})
  |> filter(fn: (r) =>
      r["_measurement"] == "Data" and
      r["_field"] == "pressure" and
      r["Port"] == "brick_2_port_b")
  |> keep(columns: ["_time", "_value"])
"""
temp = client.query_api().query_data_frame(query)
temp = temp[["_time", "_value"]]
temp.columns = ["time", "pressure"]
temp.to_csv("pressure.csv", index=False)
