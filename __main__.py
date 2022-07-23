from configparser import ConfigParser
from binance.client import Client
from binance_api import crypto_info
from trade_view import trade_view

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
        if buy_flag:
            # only search for one crypto
            pass
        elif not buy_flag:
            for crypto in all_pair:
                crypto_trade_view = trade_view(crypto)
                crypto_history    = crypto_info(client, crypto)
                
                if 'STRONG' in crypto_trade_view.analysis.summary['RECOMMENDATION']:
                    print('yes')
        keep_flag = 0