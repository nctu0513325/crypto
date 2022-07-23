from configparser import ConfigParser
from binance.client import Client
import json
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta

class trade_view:
    def __init__(self, crypto ):
        self.handler = TA_Handler(
            symbol= crypto,
            exchange= "binance",
            screener= "crypto",
            interval= "1m",
            timeout=None
            )
        self.analysis = self.handler.get_analysis()