from finvizfinance.quote import finvizfinance as fnv
from pprint import pprint
import yfinance as yfin
ticker='AAPL'
aapl_fnv = fnv(ticker)
pprint(aapl_fnv.ticker_fundament())

aapl_yfin = yfin.Ticker(ticker)
aapl_yfin.

