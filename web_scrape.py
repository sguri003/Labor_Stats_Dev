import json
import requests
import seaborn

with requests("'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo") as response:
    source = response.read()

data = json.loads(source)
print(data)