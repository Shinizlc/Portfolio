from time import sleep
from binance import Client
import requests
import re
from pprint import pprint
from multiprocessing import Process
from LOGGER import exc_logger
from binance.enums import *
from threading import Thread
import talib
import pandas as pd

def send_telegram_message(msg):
    TOKEN = "5466685853:AAFGq0oCH2aezZq5BtWROa13AlKpbkXKstk"
    chat_id = "-753462367"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    r = requests.get(url)



class Buy_sell_notification:
    api_key='ICsom6L51EeTLXpP8l3K8vRM7Z7fiCQsUjKxnzaiJWzOeF111HpAI0UR1tyH1W58'
    api_secret='WPVX7PiQKLvJ07JKPQJC1tReYEAdE73UGnOqqBNSzL1yeMWb8qx1O45U4e7QpRRn'
    percent=0.2
    ammount_usdt=350
    def __init__(self,coin):
        self.coin = coin
        self.client = Client(Buy_sell_notification.api_key, Buy_sell_notification.api_secret)
        self.check_price()

    def get_current_price(self):
        return float(self.client.get_symbol_ticker(symbol=self.coin)['price'])


    def get_quantity(self):
        return round(Buy_sell_notification.ammount_usdt/self.get_current_price(),2)


    def make_buy_order(self):
        #self.client.order_market_buy(symbol=self.coin, quantity=self.get_quantity())
        return self.client.create_order(symbol=self.coin, side='BUY', type='MARKET', quantity=self.get_quantity())

    def make_sell_order(self):
        return self.client.create_order(symbol=self.coin, side='SELL', type='MARKET', quantity=self.get_last_order()[-1])


    def technical_indicators(self):
        pass
        #btalib.rsi()



    def get_last_order(self):
        try:
            max_order_id = self.client.get_my_trades(symbol=self.coin)[-1]['orderId']
            self.client.get_my_trades(symbol=self.coin)
            qty=0
            for order in self.client.get_my_trades(symbol=self.coin):
                for k,v in order.items():
                    if k == 'orderId' and v == max_order_id:
                        qty += float(order['qty'])
            return self.client.get_my_trades(symbol=self.coin)[-1]['isBuyer'],float(self.client.get_my_trades(symbol=self.coin)[-1]['price']),qty
        except IndexError:
             exc_logger.info('First purchase of the asset')
             return None

    def get_balance(self,coin):
        try:
            if re.search(r"([a-zA-Z]+)USDT",coin):
                 coin = re.findall(r"([a-zA-Z]+)USDT",coin)[0]
                 return float(self.client.get_asset_balance(asset=coin)['free'])
            else:
                return float(self.client.get_asset_balance(asset=coin)['free'])
        except:
            return 0




    def check_price(self):
        while True:
            if self.get_last_order() is not None:##если актива не покупался ранее нужно дополнительное условие
                buy_status, grid_price, _ = self.get_last_order()
                current_price=self.get_current_price()
                #продали и цена пошла на percent вниз => докупаем
                if current_price<=grid_price-grid_price*Buy_sell_notification.percent and buy_status==False and self.get_balance('USDT')>=Buy_sell_notification.ammount_usdt:
                    self.make_buy_order()
                    self.send_notification('BUY')
                  #купили и цена пошла еще ниже на percent => еще докупаем
                elif current_price<=grid_price-grid_price*Buy_sell_notification.percent and buy_status==True and self.get_balance('USDT')>=Buy_sell_notification.ammount_usdt:
                    self.make_buy_order()
                    self.send_notification('BUY')
                    #продали, но актив еще не перекуплен(RSI<50) тогда покупаем еще
                elif buy_status==False and self.RSI()<50:
                    self.make_buy_order()
                    self.send_notification('BUY')
                #купили и цена пошла вверх => Продаем
                elif current_price>=grid_price+grid_price*Buy_sell_notification.percent and buy_status==True and self.get_balance(str(self.coin))>=self.get_last_order()[-1]:
                    self.make_sell_order()
                    self.send_notification('SELL')
                else:
                    print(f'pending, current_price of {self.coin} is {current_price},grid_price {grid_price}, diff is {((current_price-grid_price)/grid_price)*100}')
                sleep(300)
            else:
                if self.RSI()<50:#можно добавить условие, что покупать только если rsi<какой-то цифры
                    self.make_buy_order()
                sleep(300)





    def send_notification(self,action):
        if action=='BUY':
            send_telegram_message(f'Bot bought on {Buy_sell_notification.ammount_usdt}$ {self.coin} by price {self.get_current_price()}, last order {self.get_last_order()[1]}, diff in percentage {(self.get_current_price()/self.get_last_order()[1]-1)*100}')
        else:
            send_telegram_message(f'Bot sold {self.get_last_order()[-1]}  {self.coin} by price {self.get_current_price()}, last order {self.get_last_order()[1]}, diff in percentage {(self.get_current_price()/self.get_last_order()[1]-1)*100}')


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
#add buy coefficient using buy_flag
#if flag=buy then add coefficient for instance buy amount 300$ for first buy, for second amount=300$*1.1 for third amount*1.1
#grid_price take not from current_price,but the last purchase price(from binance)
# if __name__ ==  '__main__':
#     Buy_sell_notification('BNBUSDT')

#pprint(avax.get_last_order())
#
if __name__ == '__main__':
    coins=['AVAXUSDT','DOTUSDT','BTCUSDT','GLMRUSDT','MOVRUSDT','KSMUSDT','ETHUSDT','UNIUSDT','ATOMUSDT','BNBUSDT']
    for c in coins:
        processes=[]
        p=Process(target=Buy_sell_notification,args=(c,))
        p.start()









