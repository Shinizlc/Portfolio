
from LOGGING_MODULE import logger
import requests as re
import pandas as pd
from pprint import pprint
import testnet_api_keys
import time
from collections import defaultdict
import hmac
import hashlib
from urllib.parse import urlencode
from datetime import datetime,timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import DataModels as dm
from statistics import stdev
from math import sqrt
class Binance:
    headers={'X-MBX-APIKEY':testnet_api_keys.API_KEY}
    def __init__(self,test_api_flag):
        if test_api_flag:
            self.rest_api='https://testnet.binancefuture.com'
        else:
            self.rest_api='https://fapi.binance.com'
        pd.options.display.max_rows = 999

    def generate_signature(self,data):
        return hmac.new(testnet_api_keys.API_SECRET.encode(), urlencode(data).encode(),hashlib.sha256).hexdigest()


    def get_request_data(self,method,address,param):
        if method=='GET':
            with re.get(self.rest_api+address,params=param,headers=Binance.headers) as link:
                if link.status_code == 200:
                    response = link.json()
                    return response
                else:
                     logger.error('There is an error in %s',link.status_code)

        elif method=='POST':
            with re.post(self.rest_api+address,params=param,headers=Binance.headers) as link:
                if link.status_code == 200:
                    response = link.json()
                    return response
                else:
                     logger.error('There is an error in %s',link.status_code)
        else:
            with re.delete(self.rest_api+address,params=param,headers=Binance.headers) as link:
                if link.status_code == 200:
                    response = link.json()
                    return response
                else:
                     logger.error('There is an error in %s',link.status_code)
        return None

    def exchangeInfo(self)->list:
        exchange_data = self.get_request_data('GET','/fapi/v1/exchangeInfo',None)
        symbol_list=[]
        if exchange_data is not None:
            for symbols_data in exchange_data['symbols']:
                 if dm.SymbolExchange(symbols_data).status=='TRADING':
                     symbol_list.append(dm.SymbolExchange(symbols_data).symbol)
        return symbol_list


    def order_book(self,symbol):
        data={}
        data['symbol']=symbol
        d=defaultdict(dict)
        order_book = self.get_request_data('GET','/fapi/v1/ticker/bookTicker',data)
        if order_book is not None:
            d[symbol]={'bidPrice':order_book['bidPrice'],'bidQty':order_book['bidQty'],'askPrice':order_book['askPrice'],'askQty':order_book['askQty']}
            return dict(d)


    def get_balance(self):
        data={}
        data['timestamp']=int(time.time()*1000)
        data['signature']=self.generate_signature(data)
        balance_data = self.get_request_data('GET', '/fapi/v2/account', data)
        for asset in balance_data['assets']:
            print(str(dm.Balance(asset).asset),' ',str(dm.Balance(asset).balance))

    def make_order(self,symbol, quantity,leverage, side='BUY',type='MARKET'):
        leverage_data={}
        leverage_data['symbol'] = symbol
        leverage_data['leverage'] = int(leverage)
        leverage_data['timestamp'] = int(time.time()*1000)
        leverage_data['signature'] = self.generate_signature(leverage_data)
        set_leverage = self.get_request_data('POST','/fapi/v1/leverage',leverage_data)
        if set_leverage is not None:
           data = {}
           data['symbol'] = symbol
           data['side'] = side
           data['type'] = type
           data['quantity'] = quantity
           data['timestamp'] = int(time.time()*1000)
           data['signature']=self.generate_signature(data)
           created_order = self.get_request_data('POST','/fapi/v1/order', data)
           if created_order is not None:
               print(created_order)
        else:
            logger.error('leverage was"not set properly')


    def close_all_orders(self,symbol):
        data={}
        data['symbol'] = symbol
        data['timestamp'] = int(time.time()*1000)
        data['signature'] =  self.generate_signature(data)
        close_order_data = self.get_request_data('DELETE','/fapi/v1/allOpenOrders', data)
        if close_order_data is not None:
            return close_order_data
        else:logger.error('The order was not closed')
        return None

    def historical_candlestick_info(self,symbol,interval):#,daysfromnow):
        data={}
        pd_df=pd.DataFrame(columns=['OpenTime','OpenPrice','HighPrice','LowPrice','ClosePrice','CloseTime'])
        data['symbol'] = symbol
        data['interval'] = interval
       # data['startTime'] = datetime.now()-timedelta(int(daysfromnow))
        #logger.info(data['startTime'])
        historical_data = self.get_request_data('GET','/fapi/v1/klines', data)
        if historical_data is not None:
            for i,candle in enumerate(historical_data):
                pd_df.loc[i,'OpenTime'] = datetime.fromtimestamp(candle[0]/1000)
                pd_df.loc[i,'OpenPrice'] = float(candle[1]) ###float doesn't work here. pd_df has dtypes =object need to fix this
                pd_df.loc[i,'HighPrice'] = float(candle[2])
                pd_df.loc[i,'LowPrice'] = float(candle[3])
                pd_df.loc[i,'ClosePrice'] = float(candle[4])
                pd_df.loc[i,'CloseTime'] = datetime.fromtimestamp(candle[6]/1000)
            return pd_df

        else:
            logger.error('Historical Data was not found')
            return None



    def close_price_df(self,ticker_list):
        close_price_df=pd.DataFrame(columns=['CloseTime',*ticker_list])
        for ticker in ticker_list:
            data=self.historical_candlestick_info(ticker,'1d')
            if data is not None:
                close_price_df['CloseTime'] = data['CloseTime']
                close_price_df[ticker] = data['ClosePrice'].astype(float) ###
                logger.info("ticker was loaded %s",ticker)

            else:logger.error('cannot load close price data %s',ticker)
        close_price_df.set_index('CloseTime', inplace=True)
        return close_price_df

    def return_calculation(self,ticker_list):
        return self.close_price_df(ticker_list).pct_change()


    def correlation_matrix(self,ticker_list):
        cor_matrix = self.return_calculation(ticker_list).corr()
        sns.heatmap(cor_matrix)
        plt.show()

    def annualized_volatility_calculation(self,ticker_list):
        returns = self.return_calculation(ticker_list)
        print(round(returns.std()*sqrt(252),2))





if __name__ == '__main__':
    binance_client = Binance(1)
#binance_client.exchangeInfo()
#print(binance_client.order_book('XRPUSDT'))
#binance_client.get_balance()
#binance_client.make_order('BTCUSDT',0.1,10)
#print(binance_client.close_order('BTCUSDT'))
#print(binance_client.get_request_data('GET','/fapi/v1/depth',{'symbol':'BTCUSDT'}))

    #print(binance_client.historical_candlestick_info('BTCUSDT','1d'))
    #print(binance_client.close_price_df(['BTCUSDT','BNBUSDT','XRPUSDT']))
    #print(binance_client.return_calculation(['BTCUSDT','BNBUSDT','XRPUSDT']))
    # df = binance_client.close_price_df(['BTCUSDT','BNBUSDT','XRPUSDT'])
    # df.pct_change()
    #print(binance_client.close_price_df(['BTCUSDT', 'BNBUSDT', 'XRPUSDT']).dtypes)
    # print(df.dtypes)
    #print(binance_client.historical_candlestick_info('BTCUSDT','1d').dtypes)
    #print(binance_client.correlation_matrix(['BTCUSDT','BNBUSDT','XRPUSDT']))
    #binance_client.get_balance()

    binance_client.annualized_volatility_calculation(binance_client.exchangeInfo())