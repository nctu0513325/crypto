from configparser import ConfigParser
from binance.client import Client
import json

if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('API.ini')
    # read api key
    api_key    = cfg['main']['API_KEY']
    api_secret = cfg['main']['SECRET_KEY']
    
    # save api
    client = Client(api_key, api_secret)
    # initialize
    client.API_URL = 'https://api.binance.com/api'
    print(client.get_asset_balance(asset='BNB'))
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    
    timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
    bars = client.get_historical_klines('BTCUSDT', '5m', limit=1000)
    print(timestamp)
    with open('btc_bars.json', 'w') as e:
        json.dump(bars, e)
    
    # print(client.order_limit)
