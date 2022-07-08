from configparser import ConfigParser
from binance.client import Client


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
    # print(client.get_asset_balance(asset='BTC'))
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    print(btc_price)
