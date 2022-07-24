from configparser import ConfigParser
from binance.client import Client
from binance_api import crypto_info
from trade_view import trade_view
from datetime import datetime

def buy_and_sell(client, crypto):
    # buy
    money = client.get_asset_balance(asset='USDT')['free']
    price = client.get_symbol_ticker(symbol = crypto)
    buy = client.create_test_order(symbol = crypto, side = 'BUY', type = 'MARKET', quantity = (price/money*0.98))
    
    

if __name__ == '__main__':
    buy_flag  = 0
    keep_flag = 1
    
    # read api key
    cfg = ConfigParser()
    cfg.read('../API.ini')
    api_key    = cfg['main']['API_KEY']
    api_secret = cfg['main']['SECRET_KEY']
    
    # save api
    client = Client(api_key, api_secret)
    # initialize
    client.API_URL = 'https://api.binance.com/api'
    
    # get all trading pair
    all_pair = []
    for info in client.get_margin_all_pairs():
        if 'USDT' in info['symbol']:
            all_pair.append(info['symbol'])
    
    while keep_flag:
        print(datetime.now())
        for crypto in all_pair:
            crypto_trade_view = trade_view(crypto)
            crypto_history    = crypto_info(client, crypto)
            # Buy signal : tradeview -> strong buy, past 30m decrease 2%
            if 'STRONG_BUY' in crypto_trade_view.analysis.summary['RECOMMENDATION'] and crypto_history.change < -0.002:
                buy_and_sell(client, crypto,)
                break
        print(datetime.now())
        keep_flag = 0