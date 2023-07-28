class SymbolExchange:
    def __init__(self,symbol_info):
        self.symbol=symbol_info['symbol']
        self.status=symbol_info['status']

class OrderBook:
    def __init__(self,order_book_info):
        self.bidPrice = order_book_info['bidPrice']
        self.bidQty = order_book_info['bidQty']
        self.askPrice = order_book_info['askPrice']
        self.askQty = order_book_info['askQty']
class Balance:
    def __init__(self,balance_info):
        self.asset = balance_info['asset']
        self.balance = balance_info['availableBalance']
        self.PnL =  balance_info['crossUnPnl']
        self.InitialMargin = balance_info['initialMargin']
        self.MaintananceMargin = balance_info['maintMargin']
        self.MarginBalance = balance_info['marginBalance']
