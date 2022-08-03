from binance import Client
import btalib
import talib
import pandas as pd
from main_script import *

class RSI(Buy_sell_notification):
    # def __init__(self,test1):
        # super().__init__(coin)
        # self.test1= test1

    def get_historical_data(self):
        return self.client.get_historical_klines(symbol=self.coin,interval='1d',start_str="30 day ago UTC",limit=1000)

    def dataframe_create(self):
        try:
            bar_df = pd.DataFrame(self.get_historical_data(),columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
            bar_df = bar_df.drop(['Close time','Ignore','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy base asset volume','Taker buy quote asset volume'],axis=1)
            bar_df['Close']=pd.to_numeric(bar_df['Close'])
            bar_df.set_index('Open time',inplace=True)
            return bar_df
        except:
            return None

    def RSI(self):
        if self.dataframe_create() is not None:
            df =self.dataframe_create()
            #sma = btalib.sma(df,period=9)
            rsi=talib.RSI(df['Close']).iloc[-1:,]
            return float(rsi.values[0])







rsi = RSI('BTCUSDT')
print(rsi.RSI())


#print(rsi.get_historical_data())