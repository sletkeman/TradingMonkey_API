from iexfinance.stocks import get_historical_data

def get_historical(symbol, start, end):
    data = get_historical_data(symbol, start, end, output_format="json").get(symbol)
    if data:
        return data.get('chart')
    return []
