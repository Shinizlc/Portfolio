from binance import Client
from tqdm import tqdm
from time import sleep
from LOGGER_BOT import logger
from pprint import pprint
import API_KEYS
class BinanceConnection:
    client = Client(API_KEYS.API_KEY, API_KEYS.API_SECRET, testnet=True)
    def __init__(self,ticker):
        self.ticker = ticker

    def last_prices(self):
        tickers = BinanceConnection.client.get_all_tickers()
        return tickers
    def get_kline(self):
        return BinanceConnection.client.get_klines(symbol=self.ticker,interval=Client.KLINE_INTERVAL_30MINUTE)

    def get_current_price(self,ticker):
        for prices in self.last_prices():
            if ticker==prices['symbol']:
                return prices['price']


    def create_base_order(self,leverage,qnt):
        BinanceConnection.client.futures_change_leverage(symbol=self.ticker, leverage=leverage)
        BinanceConnection.client.futures_create_order(symbol=self.ticker,type='LIMIT',timeInForce='GTC',price=self.get_current_price(self.ticker), side='BUY', quantity=qnt)



    def create_bunch_safe_orders(self,qnt,n_safe_orders=3,leverage = 10,levinterval=.05):#levinterval - interval in % between safety orders
        price_for_order=round(float(self.get_current_price(self.ticker)),2)
        for _ in range(n_safe_orders):
            price_for_order-=round((price_for_order*levinterval),2)
            logger.info('Safety order price is %s',{price_for_order})
            BinanceConnection.client.futures_change_leverage(symbol=self.ticker, leverage=leverage)
            BinanceConnection.client.futures_create_order(symbol=self.ticker, type='LIMIT', timeInForce='GTC',
                                                          price=round(price_for_order,2), side='BUY',
                                                          quantity=qnt)


    def _calculate_avg_all_orders(self):
        order_list = BinanceConnection.client.futures_get_open_orders(symbol=self.ticker)
        
        for order in order_list:
            order[]




    def calculate_sell_price(self):
        pass



if __name__ == '__main__':
    connection = BinanceConnection('BNBUSDT')
    #pprint(connection.last_prices())
    # print(connection.get_current_price('BNBUSDT'))
    # connection.create_base_order('BNBUSDT',10,1)
    # connection.create_bunch_safe_orders('BNBUSDT',1)
    #pprint(connection.get_kline('BTCUSDT'))
    pprint(connection._calculate_avg_all_orders())
