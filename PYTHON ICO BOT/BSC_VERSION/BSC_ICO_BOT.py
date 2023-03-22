from numpy import False_
from web3 import Web3
from pprint import pprint
import web3
import json
import asyncio
from time import sleep
from logging_module import logger
import requests
from decimal import Decimal,getcontext
getcontext().prec = 30
class ICO_BOT:
    quicknode_endpoint = 'https://black-clean-sheet.bsc.discover.quiknode.pro/1b46e9ba10cf7e3c9091a933b6e0c544d4d99909/'
    w3 = Web3(Web3.HTTPProvider(quicknode_endpoint))
    # uniswap_router = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
    pancakeswap_factory = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
    pancakeswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    contract = w3.eth.contract(address=pancakeswap_factory, abi=pancakeswap_factory_abi)
    ##my wallet in goerli
    my_address_in_bsc = '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
    private_key = 'ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'

    wbnb_buy_threshold = 30_000_000_000_000_000 #0.01 BNB = 10_000_000_000_000_000
    # weth_allowance_threshold = 10_000_000_000_000_000_000
    gas = 500000
    slippage_tolerance = .5  ### 1 - 0.3(30%)
    honeyspot_buy_value = 1_000_000_000_000

    wbnb_abi  = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
    wbnb_mainnet = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    wbnb_contact = w3.eth.contract(address = wbnb_mainnet,abi = wbnb_abi)

    my_contract_abi = json.loads('''[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMin","type":"uint256"}],"name":"buy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"pair_contract","type":"address"}],"name":"check_contract_liquidity","outputs":[{"internalType":"uint256","name":"wbnb_on_contract","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"}],"name":"getAmountOutMin","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"get_balance_token","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"get_token_decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMin","type":"uint256"}],"name":"sell","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address","name":"token","type":"address"}],"name":"send_token_to_wallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw_funds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]''')
    # my_contract_address = '0xefA94646aa7B069f68139946953AD8ACB1d965ec'
    my_contract_address = '0xFE31042679e31699555b97207369A47a4e2eDDd7'
    #the new one 0xFE31042679e31699555b97207369A47a4e2eDDd7
    my_contract = w3.eth.contract(address=my_contract_address,abi = my_contract_abi)


    def __init__(self):
        self.purchase_price = 0
        self.take_profit = 0
        self.stop_loss = 0

z
#######Adding funds to my contract ############################
    @classmethod
    def approve_contract_to_use_my_wbnb(cls):
        nonce = cls.w3.eth.get_transaction_count(cls.my_address_in_bsc)
        tx = cls.wbnb_contact.functions.approve(cls.my_contract_address,100000000).build_transaction({'nonce':nonce})
        signed_tx = cls.w3.eth.account.signTransaction(tx,ICO_BOT.private_key)
        cls.w3.eth.sendRawTransaction(signed_tx.rawTransaction)



    # def set_proper_weth_amount(self):
    #     if self.get_token_balance(ICO_BOT.wbnb_mainnet)<ICO_BOT.wbnb_buy_threshold:
    #         self.add_weth_to_contract()

    ######################CHECK TRANSACTION STATUS#####################

    def test_transaction_status(self, tx_hash):
        receipt = ICO_BOT.w3.eth.getTransactionReceipt(tx_hash)

        if receipt['status'] == 1:
            return True
        else:
            return False


    ######################FRAUD_DETECTION#####################

    def liquidity_check(self,pair):
        weth_on_contract = ICO_BOT.my_contract.functions.check_contract_liquidity(pair).call({'from': self.my_address_in_bsc})
        return Web3.fromWei(weth_on_contract,'ether')

    #Check tokens for honeypot attack
    # def honeypot_check(self,token_in,token_out):
    #     url = "https://honeypotapi.p.rapidapi.com/api/v1/scan/"
    #
    #     querystring = {"factory_address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    #                    "token_b": token_out, "chain": "eth",
    #                    "exchange": "Uniswap v2", "token_a": token_in,
    #                    "router_address": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", "fee": "3000"}
    #
    #     headers = {
    #         "X-RapidAPI-Key": "01c050f5ffmshd08a9f8299b780fp1022b1jsna01e808f5ffc",
    #         "X-RapidAPI-Host": "honeypotapi.p.rapidapi.com"
    #     }
    #     response = requests.request("GET", url, headers=headers, params=querystring)
    #     if response.json()['is_honeypot'] == False and response.json()['is_verified'] == True:
    #         return False
    #     else:
    #         return True

    def honeypot_check(self,token_in,token_out):
        tx_hash = self.buy_token(token_in,token_out,self.honeyspot_buy_value)
        if tx_hash is not None:
            while True:
                try:
                    if self.test_transaction_status(tx_hash):
                        break
                    else:
                        logger.warning(f'Waiting swap transaction to be completed: {tx_hash}')
                        sleep(1)
                except web3.exceptions.TransactionNotFound:
                    logger.warning(f'Transaction not in mempool.Waiting for transaction to be seen: {tx_hash}')
                    sleep(1)
        else:
            return True

        counter = 0
        token_in, token_out = token_out,token_in

        tx_hash = self.sell_token(token_in,token_out,self.get_token_balance(token_in))

        if tx_hash is not None:
            while True:
                try:
                    transaction_status = self.test_transaction_status(tx_hash)
                except web3.exceptions.TransactionNotFound:
                    logger.warning(f'Transaction not in mempool.Waiting for transaction to be seen: {tx_hash}')
                    sleep(1)
                else:
                    if transaction_status is True:
                        return False
                    elif transaction_status is False and counter >= 120:
                        logger.error(f'Seems like a transaction has failed')
                        return True
                    else:
                        logger.warning(f'Waiting swap transaction to be completed: {tx_hash}')
                        counter += 1
                        sleep(1)
        else:
            return True




##################################################
    ###############MAIN PART######################

    def handle_event(self,event):
        token0,token1,pair = json.loads(Web3.toJSON(event))['args']['token0'],json.loads(Web3.toJSON(event))['args']['token1'],json.loads(Web3.toJSON(event))['args']['pair']
        if token0==ICO_BOT.wbnb_mainnet:
            token_in = token0
            token_out = token1
        elif token1==ICO_BOT.wbnb_mainnet:
            token_in = token1
            token_out = token0
        else:
            return None
        logger.warning(f'token0 :{token0},token1: {token1},pair: {pair}')
        logger.warning(f'WBNB is {token_in},other token is {token_out}')
        return token_in, token_out, pair


    def log_loop(self,event_filter, poll_interval):
        while True:

            for PairCreated in event_filter.get_new_entries():
                try:
                    token_in, token_out,pair = self.handle_event(PairCreated)
                    logger.warning(f'token_in :{token_in}, token_out :{token_out}, pair :{pair}')
                except:
                    logger.error(f'Handle_event function return something bad')
                else:
                    # check the liquidity of the pair
                    liquidity = self.liquidity_check(pair)
                    decimals = self.get_token_decimals(token_out)
                    logger.warning(f'DECIMALS: {decimals}')
                    logger.warning(f'Liquidity: {liquidity}')
                    if liquidity >= 1:
                        state = self.honeypot_check(token_in, token_out)

                        if state is True:
                            logger.warning(f'The token {token_out} of a pair {pair} is a honeypot' )
                        else:
                            logger.warning(f'The token {token_out} of a pair {pair} is not a honeypot')

                            logger.warning(f'token {token_in} will be swapped to {token_out}')

                            # Swap WBNB to token

                            tx_hash = self.buy_token(token_in, token_out,ICO_BOT.wbnb_buy_threshold)

                            if tx_hash is not None:
                                while True:
                                    try:
                                        if self.test_transaction_status(tx_hash):
                                            break
                                        else:
                                            logger.warning(f'Waiting swap transaction to be completed: {tx_hash}')
                                            sleep(1)
                                    except web3.exceptions.TransactionNotFound:
                                        logger.warning(f'Transaction not in mempool.Waiting for transaction to be seen: {tx_hash}')
                                        sleep(1)


                                try:
                                    # update purchase price

                                    # self.get_purchase_price(token_out)
                                    start_price = self.get_pair_price(token_in, token_out)
                                    # self.set_stop_loss()
                                    # self.set_take_profit()



                                except:

                                    logger.error(f'Cannot get purchase_price')

                                else:
                                    totalwork = 0
                                    ATH = 0
                                    #check the status every 2 seconds
                                    while True:
                                        end_price = self.get_pair_price(token_in, token_out)
                                        price_diff = round((1-(start_price / end_price)) * 100,2)
                                        if float(end_price) > float(ATH):
                                            ATH = end_price
                                            # logger.warning(f'ATH is equal:{ATH},end price is {float(end_price)}')

                                        logger.warning(f'difference between prices is:{price_diff}')
                                        if totalwork>=250 or price_diff<=-10 or price_diff>=70 or end_price <= ATH - ATH * Decimal(.2):
                                            # change tokens position for swapping trading pair back
                                            token_in, token_out = token_out, token_in
                                            logger.warning(f'token {token_in} will be swapped back to {token_out}')

                                            if self.get_token_balance(token_in)>0:

                                                logger.warning(f'token {token_in} will be swapped back to {token_out}')

                                                tx_hash = self.sell_token(token_in, token_out,self.get_token_balance(token_in))

                                                while True:
                                                    try:
                                                        if self.test_transaction_status(tx_hash):
                                                            break
                                                        else:
                                                            logger.warning(f'Waiting the new token will be swapped back : {tx_hash}')
                                                            sleep(1)

                                                    except web3.exceptions.TransactionNotFound:
                                                        logger.warning(f'Transaction not in mempool.Waiting for transaction to be seen: {tx_hash}')
                                                        sleep(1)

                                            else:
                                                logger.warning(f'either we did"t buy anything or balance ==0')
                                                break
                                        else:
                                            totalwork += 1
                                            sleep(1)

                    else:
                        logger.error(f'We don"t swap because liquidity is equal to :{liquidity}')

            sleep(poll_interval)
            # await asyncio.sleep(poll_interval)


    def get_min_amount_to_buy(self,token_in,token_out, amount_to_buy):
        try:
            res = ICO_BOT.my_contract.functions.getAmountOutMin(token_in,token_out,amount_to_buy).call({'from': self.my_address_in_bsc})
            res = int(res * self.slippage_tolerance)
            logger.warning(f'It should return about {res} of token {token_out} for {amount_to_buy} of {token_in} token')
            return res
        except web3.exceptions.ContractLogicError:
            logger.error(f'Not enough liquidity. Try another pair or another amount')
            return None

    def buy_token(self,token_in,token_out,amount_to_buy):
        min_amount_out = self.get_min_amount_to_buy(token_in, token_out, amount_to_buy)
        # Check if there is enough liquidity to perform the swap
        if min_amount_out is not None and min_amount_out != 0:
            nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_bsc)
            tx = ICO_BOT.my_contract.functions.buy(token_in,token_out,amount_to_buy,min_amount_out).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas,'gasPrice':self.get_gas_price()})
            signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
            tx_hash = ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return ICO_BOT.w3.toHex(tx_hash)
        else:
            logger.warning(f'We cannot swap these tokens due to the lack of liquidity')
            return None

    def sell_token(self,token_in,token_out,amount_to_buy):
        min_amount_out = self.get_min_amount_to_buy(token_in, token_out, amount_to_buy)
        # Check if there is enough liquidity to perform the swap
        if min_amount_out is not None and min_amount_out != 0:
            nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_bsc)
            tx = ICO_BOT.my_contract.functions.sell(token_in,token_out,amount_to_buy,min_amount_out).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas,'gasPrice':self.get_gas_price()})
            signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
            tx_hash = ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return ICO_BOT.w3.toHex(tx_hash)
        else:
            logger.warning(f'We cannot swap these tokens due to the lack of liquidity')
            return None

    @staticmethod
    def get_gas_price():
        API_KEY = 'V8XIA4BCZEPVEGGA878D4CKNVUY3D4TTH5'
        GAS_PRICE_URL = f'https://api.bscscan.com/api?module=gastracker&action=gasoracle&apikey={API_KEY}'
        with requests.get(GAS_PRICE_URL) as link:
            data = int(link.json()['result']['FastGasPrice'])
            return int(data * (10 ** 9))

    def get_token_balance(self,token):
        balance =  ICO_BOT.my_contract.functions.get_balance_token(token).call({'from': self.my_address_in_bsc})
        decimals = self.get_token_decimals(token)
        logger.warning(decimals)
        # #Prepare balance data for swaping function by converting to smallest units
        # scaling_factor = 10 ** (18 - decimals)
        # adjusted_amount_to_buy = balance * scaling_factor
        # #Convert into readable human format
        readable_balance = balance / (10 ** decimals)
        logger.warning(f'The balance of token {token} is {readable_balance}')
        # return round(adjusted_amount_to_buy)
        return balance#,readable_balance

###############################################################
    ######OPERATIONS WITH BALANCE #####

    def withdraw_token(self,amount,token='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'):
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_bsc)
        tx = ICO_BOT.my_contract.functions.send_token_to_wallet(amount,token).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas,'gasPrice':self.get_gas_price()})
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx,ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)


    def get_token_decimals(self,token):
        return ICO_BOT.my_contract.functions.get_token_decimals(token).call({'from': self.my_address_in_bsc})

    def get_purchase_price(self,token):
        self.purchase_price = (ICO_BOT.wbnb_buy_threshold/10**18)/(self.get_token_balance(token)/10**self.get_token_decimals(token))
        logger.warning(f'purchase price is equal to {Decimal(self.purchase_price)}')

    def get_pair_price(self,token_in,token_out)->int:
        amount_tk_per_1eth  = self.get_min_amount_to_buy(token_in, token_out, 1000000000000000000)
        amount_tk_per_1eth = amount_tk_per_1eth/(10**self.get_token_decimals(token_out))
        # logger.warning(f'amount that we are getting selling 0.01 ETH :{amount_tk_per_1eth}')
        # logger.warning(f'Price will be {Decimal(1/amount_tk_per_1eth)}')
        logger.warning(f'Price will be {Decimal(1) / Decimal(amount_tk_per_1eth)}')
        return Decimal(1) / Decimal(amount_tk_per_1eth)

    # def set_take_profit(self):
    #     self.take_profit = self.purchase_price+self.purchase_price*.5
    #     logger.warning(f'Take profit price is equal to price: {self.take_profit}')
    #
    # def set_stop_loss(self):
    #     self.stop_loss = self.purchase_price-self.purchase_price*.2
    #     logger.warning(f'Stop loss price is equal to price: {self.stop_loss}')
    #
    # def trailing_implemetation(self):
    #     if self.get_pair_price()>self.purchase_price:
    #         self.set_take_profit()
    #         self.set_stop_loss()
    #     else:
    #         pass



    def main(self):
        while True:
            event_filter = ICO_BOT.contract.events.PairCreated.createFilter(fromBlock='latest')
            try:
                self.log_loop(event_filter, 2)
            except ValueError:
                print(f'filter is incorrect')

####проблемы с получением баланса на некоторых монетах

if __name__ == '__main__':
#     #it works
    ico_bot1 = ICO_BOT()
    ico_bot1.buy_token('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c','0x6886ed8Da98caFe10a5BFd3Dc23F8c207e7BDc22',ICO_BOT.honeyspot_buy_value)
    # print(ico_bot1.get_token_balance('0x4E4F479d99520EaFBd8F553675909E3C615A5178'))



    # ico_bot1.sell_token('0x4E4F479d99520EaFBd8F553675909E3C615A5178','0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c',1028827)
    # print(ico_bot1.get_min_amount_to_buy('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c','0x4E4F479d99520EaFBd8F553675909E3C615A5178',10000000))
    # ico_bot1.approve_contract_to_use_my_wbnb()
    # print(ico_bot1.get_token_balance('0x6B5aA42bEB98Eb01904227F95852239942F22072'))
    # ico_bot1.main()
    # ico_bot1.honeypot_check('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c','0x6839D258153933fBE77cc076b2573444C06532A2')

    # print(ico_bot1.liquidity_check('0x1A1D645f245583e7C47547521D4189EC07822907'))
    # print(ico_bot1.get_min_amount_to_buy('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2','0x00bb18aB17cf52DF123d0598fA56a5324b51A998',ICO_BOT.wbnb_buy_threshold))


    # ico_bot1.approve_contract_to_use_my_weth()
    # ico_bot1.sell_token('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2','0x0A58153a0CD1cfaea94cE1f7FdC5D7E679eCa936',ico_bot1.get_token_balance('0x0A58153a0CD1cfaea94cE1f7FdC5D7E679eCa936'))

    # ico_bot1.get_min_amount_to_buy('0x91acAA613da5e553aD5e02339f01A233F75727c8', '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',ico_bot1.get_token_balance('0x91acAA613da5e553aD5e02339f01A233F75727c8'))
    # print(ico_bot1.get_gas_price())
    # print(ico_bot1.swap_token('0x91acAA613da5e553aD5e02339f01A233F75727c8', '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',ico_bot1.get_token_balance('0x91acAA613da5e553aD5e02339f01A233F75727c8')))
    # print(ico_bot1.get_min_amount_to_buy('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2','0x32DebF31D5ED90ca2e287D306fc23FaFAD9361c6',ICO_BOT.wbnb_buy_threshold))
    # ico_bot1.main()
    # print(ico_bot1.swap_token('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', '0xB11AB8Cc44B16E8388714b21846ac17b1a2725Bb',ICO_BOT.wbnb_buy_threshold))
    # print(ico_bot1.get_gas_price())


# 11952083772400000000