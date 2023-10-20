import API
from ta.trend import SMAIndicator
import pandas as pd
import time

MARKET = 'TRXUSD_PERP'
TIMEFRAME = '1m'

# Loading initial candles
velas = API.getVelas(MARKET, TIMEFRAME, 200)

while True:
    # Loading the closes
    closes = map(lambda vela: vela['close'], velas)
    closes_series = pd.Series(closes)

    # Loading the EMA
    ma10 = SMAIndicator(closes_series, 10)
    ma100 = SMAIndicator(closes_series, 100)

    # Computing the EMA values
    ma10_v = list(ma10.sma_indicator())
    ma100_v = list(ma100.sma_indicator())

    # Checking the buy cross
    if ma10_v[-2] < ma100_v[-2] and ma10_v[-1] > ma100_v[-1]:
        API.new_trade(MARKET, 'BUY', 1)

    # Checking the sell cross
    elif ma10_v[-2] > ma100_v[-2] and ma10_v[-1] < ma100_v[-1]:
        API.new_trade(MARKET, 'SELL', 1)

    time.sleep(3)
    API.anadirVela(MARKET, TIMEFRAME, velas)
