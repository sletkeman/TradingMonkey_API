from iexfinance.stocks import get_historical_data
import json

def get_historical(symbol, start, end):
    data = get_historical_data(symbol, start, end)
    raw = data.to_json(orient="table")
    return json.loads(raw).get('data', [])
