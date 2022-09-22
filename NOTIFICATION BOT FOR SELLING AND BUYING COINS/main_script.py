from time import sleep
from binance import Client
import requests
import re
from pprint import pprint
import binance
from multiprocessing import Process
from LOGGER import exc_logger
from binance.enums import *
from threading import Thread
import talib
import pandas as pd
from datetime import datetime
def send_telegram_message(msg):
    TOKEN = "5466685853:AAFGq0oCH2aezZq5BtWROa13AlKpbkXKstk"
    chat_id = "-753462367"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    try:
        r = requests.get(url)
    except:
        print(f"Could't send a message via telegram")




class Buy_sell_notification:
    api_key='ICsom6L51EeTLXpP8l3K8vRM7Z7fiCQsUjKxnzaiJWzOeF111HpAI0UR1tyH1W58'
    api_secret='WPVX7PiQKLvJ07JKPQJC1tReYEAdE73UGnOqqBNSzL1yeMWb8qx1O45U4e7QpRRn'
    percent=0.2
    ammount_usdt=500
    RSI_threshold = 40
    def __init__(self,coin):
        self.coin = coin
        self.client = Client(Buy_sell_notification.api_key, Buy_sell_notification.api_secret)
        self.check_price()

    def get_current_price(self):
        return float(self.client.get_symbol_ticker(symbol=self.coin)['price'])

    def get_symbol_info(self):
        return self.client.get_symbol_info(self.coin)

    def get_quantity(self):
        qnt = round(Buy_sell_notification.ammount_usdt/self.get_current_price(),2)
        if len(str(qnt))>5:
            return round(Buy_sell_notification.ammount_usdt / self.get_current_price(), 1)
        else:
            return qnt


    def make_buy_order(self):
        #self.client.order_market_buy(symbol=self.coin, quantity=self.get_quantity())
        return self.client.create_order(symbol=self.coin, side='BUY', type='MARKET', quantity=self.get_quantity())

    def make_sell_order(self):
        try:
            return self.client.create_order(symbol=self.coin, side='SELL', type='MARKET', quantity=self.get_last_order()[-1])
        except binance.exceptions.BinanceAPIException as sell_err:
            if sell_err.code == -2010:
                send_telegram_message(f'Not enough {self.coin}. Need deposit account with {self.coin} to sell it')




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
            return self.client.get_my_trades(symbol=self.coin,)[-1]['isBuyer'],float(self.client.get_my_trades(symbol=self.coin)[-1]['price']),qty
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
            try:
                if self.get_last_order() is not None:##если актива не покупался ранее нужно дополнительное условие
                    buy_status, grid_price, _ = self.get_last_order()
                    current_price=self.get_current_price()
                    #продали и цена пошла на percent вниз => докупаем
                    if current_price<=grid_price-grid_price*Buy_sell_notification.percent and buy_status==False: #and self.get_balance('USDT')>=Buy_sell_notification.ammount_usdt:
                        self.make_buy_order()
                        self.send_notification('BUY')
                    # elif :
                    #     pass


                      #купили и цена пошла еще ниже на percent => еще докупаем
                    elif current_price<=grid_price-grid_price*Buy_sell_notification.percent and buy_status==True: #and self.get_balance('USDT')>=Buy_sell_notification.ammount_usdt:
                        self.make_buy_order()
                        self.send_notification('BUY')
                        #продали, но актив еще не перекуплен(RSI<40) тогда покупаем еще
                    elif buy_status==False and self.RSI()<=Buy_sell_notification.RSI_threshold: #and self.get_balance('USDT')>=Buy_sell_notification.ammount_usdt:
                        # try:
                        self.make_buy_order()
                        self.send_notification('BUY')
                    #купили и цена пошла вверх => Продаем
                    elif current_price>=grid_price+grid_price*Buy_sell_notification.percent and self.get_balance(str(self.coin))>=self.get_last_order()[-1]:#and buy_status==True :
                        self.make_sell_order()
                        self.send_notification('SELL')
                    else:
                        print(f'pending, current_price of {self.coin} is {current_price},grid_price {grid_price}, diff is {((current_price-grid_price)/grid_price)*100}')
                    sleep(300)
                else:#актив не покупался еще
                    if self.RSI()<=Buy_sell_notification.RSI_threshold:#можно добавить условие, что покупать только если rsi<какой-то цифры
                        # try:
                        self.make_buy_order()
                        self.send_notification('BUY')
                    sleep(300)

            except binance.exceptions.BinanceAPIException as err_binance:
                if err_binance.code == -2010:
                    send_telegram_message(f'Not enough USDT. Need deposit account to buy {self.coin}')
                    sleep(3600)
                elif err_binance.code == -1020:
                    send_telegram_message(f'Could not get response in recvWindow {self.coin}')
                    sleep(300)
                elif err_binance.code == -1003:
                    sleep(300)
                elif err_binance.code == -1013:
                    send_telegram_message(f'Lot size for {self.coin}')
                    sleep(300)
                elif err_binance.code == -2015:
                    send_telegram_message(f'API key is expired')
                    sleep(300)
                else:
                    send_telegram_message(f'any other errors connected with binance excepetions')
                    sleep(300)
            except requests.exceptions.ConnectionError as con_error:  ##were added but haven't tested yet
                print(f'connection error to binance')
                sleep(300)

            except binance.exceptions.BinanceAPIException as err_2010:
                if err_2010.code == -2010:
                    send_telegram_message(f'Not enough USDT. Need deposit account to buy {self.coin}')
                    sleep(3600)
            except binance.exceptions.BinanceAPIException as err_1020:
                if err_1020.code == -1020:
                    send_telegram_message(f'Could not get response in recvWindow {self.coin}')
                    sleep(300)
            except binance.exceptions.BinanceAPIException as err_1003:
                if err_1003.code == -1003:
                    sleep(300)
            except requests.exceptions.ConnectionError as con_error:##were added but haven't tested yet
                print(f'connection error to binance')
                sleep(300)




    def send_notification(self,action):
        if action=='BUY':
            send_telegram_message(f'Bot bought on {Buy_sell_notification.ammount_usdt}$ {self.coin} by price {self.get_current_price()}, last order {self.get_last_order()[1]}, diff in percentage {(self.get_current_price()/self.get_last_order()[1]-1)*100}')
        else:
            send_telegram_message(f'Bot sold {self.get_last_order()[-1]}  {self.coin} by price {self.get_current_price()}, last order {self.get_last_order()[1]}, diff in percentage {(self.get_current_price()/self.get_last_order()[1]-1)*100}')


    def get_historical_data(self):
        return self.client.get_historical_klines(symbol=self.coin,interval='1d',start_str="15 day ago UTC",limit=1000)

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
        try:
            df =self.dataframe_create()
        except:
            send_telegram_message(f'Could not get df for RSI for some of the reason {self.coin}')
            return 100# we don't buy/or get erro if we cannot get RSI
        else:
            if df is not None:
                rsi=talib.RSI(df['Close']).iloc[-1:,]
                return float(rsi.values[0])
            else:
                return 100# we don't buy/or get erro if we cannot get RSI
    #add buy coefficient using buy_flag
#if flag=buy then add coefficient for instance buy amount 300$ for first buy, for second amount=300$*1.1 for third amount*1.1
#grid_price take not from current_price,but the last purchase price(from binance)
# if __name__ ==  '__main__':
#     test_filusdt = Buy_sell_notification('FILUSDT')
#     test_filusdt.make_sell_order()


if __name__ == '__main__':
    coins=['AVAXUSDT','DOTUSDT','BTCUSDT','GLMRUSDT','MOVRUSDT','KSMUSDT','ETHUSDT','UNIUSDT','ATOMUSDT','BNBUSDT','NEARUSDT','FILUSDT']
    for c in coins:
        processes=[]
        p=Process(target=Buy_sell_notification,args=(c,))
        p.start()









