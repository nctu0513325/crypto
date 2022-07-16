from configparser import ConfigParser
from binance.client import Client
from binance_api import crypto_info

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

    crypto_list = [i.replace('\n', '') for i in open('crypto_pair.txt')]
    
    while keep_flag:
        if buy_flag:
            # only search for one crypto
            pass
        elif not buy_flag:
            for crypto in crypto_list:
                # info = client.get_symbol_info(crypto)
                # print(info)
                print(crypto)
                tmp = crypto_info(client, crypto)
                print(tmp.bars)
        keep_flag = 0