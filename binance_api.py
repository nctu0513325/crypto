import btalib
from configparser import ConfigParser
from binance.client import Client
import pandas as pd

class crypto_info:

    def __init__(self, client, pair):
        self.client = client
        self.pair = pair
        
        
        self.bars = client.get_historical_klines(self.pair, '5m', limit=300)
        for line in self.bars:
            del line[5:]

        self.df = pd.DataFrame(self.bars, columns=['date', 'open', 'high', 'low', 'close'])
        self.df.set_index('date', inplace=True)
        self.df.index = pd.to_datetime(self.df.index, unit='ms')
        self.df.to_csv(f'{self.pair}.csv')
        self.df = pd.read_csv(f'{self.pair}.csv', index_col=0)
        
        # calculate sma
        self.df['sma'] = btalib.sma(self.df.close, period=20).df
        # calculate RSI
        self.df['RSI'] = btalib.rsi(self.df.close, period = 14).df
        print(self.df.tail(10))

if __name__ == "__main__":
    # read api key
    cfg = ConfigParser()
    cfg.read('../API.ini')
    api_key    = cfg['main']['API_KEY']
    api_secret = cfg['main']['SECRET_KEY']
    
    # save api
    client = Client(api_key, api_secret)
    # initialize
    client.API_URL = 'https://api.binance.com/api'
    
    crypto_info(client, "BTCUSDT")