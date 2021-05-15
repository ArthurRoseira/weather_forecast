from google.cloud import bigquery
import pandas as pd
client = bigquery.Client()

query = """
    SELECT state, name, lat, lon
    FROM fh-bigquery.weather_gsod.stations
    WHERE country='BR' AND state='PR'
    LIMIT 30
"""
df = pd.read_gbq(query, dialect='standard')
print(df.head(10))
