from configparser import ConfigParser
from binance.client import Client
import json
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta

if __name__ == '__main__':
    handler = TA_Handler(
    symbol="BTCUSDT",
    exchange="binance",
    screener="crypto",
    interval="1m",
    timeout=None
    )
    analysis = handler.get_analysis()
    print(analysis.summary)
    # print(client.order_limit)
