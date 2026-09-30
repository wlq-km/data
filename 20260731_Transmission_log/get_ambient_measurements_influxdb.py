from influxdb_client import InfluxDBClient
import pandas as pd

client = InfluxDBClient(
    url="http://134.157.35.7:8086",
    token="A-ZcHVGJsRSotigQICwj9sKeARx-Dv-JkwoFQQUKqL7xT8kpDiSqm0DfDP2VU9v748-cy6kPMqVX23xAA1LUSg==",
    org="Welinq"
)

# temperature
query = """
from(bucket: "Monitoring")
  |> range(start: -20d)
  |> filter(fn: (r) =>
      r["_measurement"] == "Data" and
      r["_field"] == "temperature" and
      r["Port"] == "brick_0_port_a")
  |> keep(columns: ["_time", "_value"])
"""

temp = client.query_api().query_data_frame(query)
temp = temp[["_time", "_value"]]
temp.columns = ["time", "temperature"]
temp.to_csv("temperature.csv", index=False)

# humidity
query = """
from(bucket: "Monitoring")
  |> range(start: -20d)
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
query = """
from(bucket: "Monitoring")
  |> range(start: -20d)
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
