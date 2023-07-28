import websocket as ws 
from LOGGING_MODULE import logger
import threading
import json
from pprint import pprint
# import DataModels as dm
# import json
# import threading
# class websocket:
#     def __init__(self):
#         self.wss_url = 'wss://stream.binancefuture.com'
#         self.ws_conn  = None
#         self.id = 0
#         wss_thread = threading.Thread(self.wss_connect())
#         wss_thread.start()
#
#     def wss_connect(self):
#         self.ws_conn = WebSocketApp(self.wss_url,on_open=self.on_open,on_close=self.on_close,on_message=self.on_message)
#         self.ws_conn.run_forever()
#
#
#     def on_open(self,ws_conn):
#         print(logger.info('Connection was opened'))
#         d={}
#         d['method'] = 'SUBSCRIBE'
#         d['params'] = ['btcusdt@markPrice']
#         d['id'] = self.id+1
#         self.ws_conn.send(json.dumps(d).encode('utf-8'))
#
#
#     def on_close(self,ws_conn):
#         print(logger.info('Connection was closed'))
#
#     def on_message(self,ws_conn,msg):
#         print(logger.info('The following information was recieved:%s',msg))
#
#     # def on_error(self,msg):
#     #     print(logger.error('The follling error occurred:%s',msg))
#
#
#
# websocket = websocket()
#

class Websocket_binance:
    def __init__(self):
        self.url = 'wss://stream.binancefuture.com'
        self.ws = None
        self.id=0
        thread=threading.Thread(self.ws_connect())
        thread.run()
        logger.info('Binance websocket was initiated')

    def ws_connect(self):
        ws.enableTrace(True)
        self.ws = ws.WebSocketApp(self.url,on_open=self.on_open,on_message=self.on_message, on_error=self.on_error)
        while True:
            try:
                self.ws.run_forever()
            except:
                logger.debug('Error occured')


    def on_error(self,ws,err):
        logger.error('the following error %s occured',err)

    def on_message(self,ws,msg):
        logger.info(f'we"ve got a message{msg}')
        json.loads(msg)

    def on_open(self,ws):
        logger.debug(f'Socket was opened')
        self.subsribe_channel()

    def subsribe_channel(self):
        param = {}
        param['method'] = 'SUBSCRIBE'
        param['params'] = ['btcusdt@bookTicker']
        param['id'] = self.id+1
        pprint(param)
        self.ws.send(json.dumps(param))
if __name__ == '__main__':
    web_s = Websocket_binance()
