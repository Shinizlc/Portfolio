from numpy import False_
from web3 import Web3
import web3
import json
import asyncio
from time import sleep
from logging_module import logger
import requests
from decimal import *
class ICO_BOT:
    #infura_url = 'https://mainnet.infura.io/v3/6cda95a972fe4e168a9057235825b257'
    goerli_url = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
    w3 = Web3(Web3.HTTPProvider(goerli_url))
    uniswap_router = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
    uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
    uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    weth_goerli = '0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'
    eth_goerli = '0x8d27431c473E83611847D195d325972e80D1F4c1'
    contract = w3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)
    ##my wallet in goerli
    my_address_in_goeri = '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
    private_key = 'ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
    ######my contract address
    my_contract_address = '0xC70BCB40dB7cb5fb72fB0A6E95A15E46edE45E60'
    weth_buy_threshold = 10_000_000_000_000_000
    weth_allowance_threshold = 100000000000000000
    gas = 250000
    weth_abi  = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
    weth_contact = w3.eth.contract(address = weth_goerli,abi = weth_abi)
    my_contract_abi = json.loads('''[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"address","name":"_token_in","type":"address"},{"internalType":"address","name":"_token_out","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMin","type":"uint256"}],"name":"_swap_token","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"pair_contract","type":"address"}],"name":"check_contract_liquidity","outputs":[{"internalType":"uint256","name":"weth_on_contract","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"}],"name":"getAmountOutMin","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"get_balance_token","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"get_token_decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address","name":"token","type":"address"}],"name":"send_token_to_wallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw_funds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]''')
    my_contract = w3.eth.contract(address=my_contract_address,abi = my_contract_abi)
    slippage_tolerance = .9

    def __init__(self):
        self.purchase_price = 0
        self.take_profit = 0
        self.stop_loss = 0
        # self.approve_contract_to_use_my_weth()

#######Adding funds to my contract ############################
    def approve_contract_to_use_my_weth(self):
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.weth_contact.functions.approve(ICO_BOT.my_contract_address,1000000000000000000).build_transaction({'nonce':nonce})
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx,ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    def add_weth_to_contract(self):
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.my_contract.functions.send_WETH_to_contract(ICO_BOT.weth_buy_threshold).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas})
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx,ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
#########Check allowance and additional allowance if needed

    # def add_approve_to_uniswap(self):
    #     nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
    #     tx = ICO_BOT.my_contract.functions.approve_WETH_to_Uniswap(ICO_BOT.weth_allowance_threshold).build_transaction({'nonce': nonce, 'gas': ICO_BOT.gas})
    #     signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
    #     ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)



#####check approve for this token 0xC0Cadce2E6809d996959216bcCB1CF3C4c449e8e
    def add_approve_to_uniswap(self,amount,token):
        # try:
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.my_contract.functions.approve_token_to_Uniswap(token,amount).build_transaction({'nonce': nonce, 'gas': ICO_BOT.gas})#ICO_BOT.weth_allowance_threshold
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
        tx_hash = ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        logger.warning(f' transaction hash: {ICO_BOT.w3.toHex(tx_hash)}')
        return ICO_BOT.w3.toHex(tx_hash)
        # except:
        #     print(f'{token} wasn"t approved for usage to Uniswap')### уходит сюда
        # else:
        #     print(f'the {amount} of {token} wasn"t approved for usage to Uniswap')

    #####check if we have enough money on the contract(haven"t checked yet?)
    # def check_allowance_for_uniswap(self):
    #     wei_allowed = ICO_BOT.my_contract.functions.check_approval_for_contract().call()
    #     print(f'uniswap allowed to use {ICO_BOT.w3.fromWei(wei_allowed,"ether")} from my contract')
    #     if wei_allowed<ICO_BOT.weth_buy_threshold:
    #         return False
    #     else:
    #         return True



    def set_proper_weth_amount(self):
        if self.get_token_balance(ICO_BOT.weth_goerli)<ICO_BOT.weth_buy_threshold:
            self.add_weth_to_contract()

    ######################CHECK TRANSACTION STATUS#####################

    def test_transaction_status(self, tx_hash):
        receipt = ICO_BOT.w3.eth.getTransactionReceipt(tx_hash)

        if receipt['status'] == 1:
            return True
        else:
            return False


    ######################FRAUD_DETECTION#####################

    def liquidity_check(self,pair):
        weth_on_contract = ICO_BOT.my_contract.functions.check_contract_liquidity(pair).call({'from': self.my_address_in_goeri})
        return Web3.fromWei(weth_on_contract,'ether')

    #Check tokens for honeypot attack
    def honeypot_check(self,token_in,token_out):
        url = "https://honeypotapi.p.rapidapi.com/api/v1/scan/"

        querystring = {"factory_address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
                       "token_b": token_out, "chain": "eth",
                       "exchange": "Uniswap v2", "token_a": token_in,
                       "router_address": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", "fee": "3000"}

        headers = {
            "X-RapidAPI-Key": "01c050f5ffmshd08a9f8299b780fp1022b1jsna01e808f5ffc",
            "X-RapidAPI-Host": "honeypotapi.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        logger.warning(response.json())

##################################################
    ###############MAIN PART######################

    def handle_event(self,event):
        token0,token1,pair = json.loads(Web3.toJSON(event))['args']['token0'],json.loads(Web3.toJSON(event))['args']['token1'],json.loads(Web3.toJSON(event))['args']['pair']
        if token0==ICO_BOT.weth_goerli or token0==ICO_BOT.eth_goerli:
            token_in = token0
            token_out = token1
        elif token1==ICO_BOT.weth_goerli or token1==ICO_BOT.eth_goerli:
            token_in = token1
            token_out = token0
        else:
            return None
        logger.warning(f'token0 :{token0},token1: {token1},pair: {pair}')
        logger.warning(f'ETH or WETH is {token_in},other token is {token_out}')
        return token_in, token_out, pair


    def log_loop(self,event_filter, poll_interval):
        while True:

            for PairCreated in event_filter.get_new_entries():
                try:
                    token_in, token_out,pair = self.handle_event(PairCreated)

                except:
                    logger.error(f'Handle_event function return something bad')
                else:
                    # check that liquidity of the pair
                    liquidity = self.liquidity_check(pair)
                    logger.warning(liquidity)
                    if liquidity >= 0.02:
                        logger.warning(f'token {token_in} will be swapped to {token_out}')

                            #CHECK THAT WE HAVE ENOUGH ALLOWANCE
                        # if not self.check_allowance_for_uniswap():
                        #     tx_hash = self.add_approve_to_uniswap(ICO_BOT.weth_allowance_threshold,ICO_BOT.weth_goerli)
                        #
                        #     while True:
                        #         try:
                        #             if self.test_transaction_status(tx_hash):
                        #                 break
                        #             else:
                        #                 logger.warning(f'Waiting for approval for transaction: {tx_hash}')
                        #                 sleep(1)
                        #
                        #         except web3.exceptions.TransactionNotFound:
                        #             logger.warning(f'Transaction not in mempool.Waiting for transaction to be seen: {tx_hash}')
                        #             sleep(1)




                        tx_hash = self.swap_token(token_in, token_out,ICO_BOT.weth_buy_threshold)


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
                            self.get_pair_price(token_in, token_out)
                            # self.set_stop_loss()
                            # self.set_take_profit()



                        except:

                            logger.error(f'Cannot get purchase_price')

                        else:
                            # change tokens position for swapping trading pair back

                            token_in, token_out = token_out, token_in

                            # give an approval for new token to  Uniswap Dex

                            # tx_hash = self.add_approve_to_uniswap(self.get_token_balance(token_in), token_in)
                            #
                            #
                            # while True:
                            #     try:
                            #         if self.test_transaction_status(tx_hash):
                            #             break
                            #         else:
                            #             logger.warning(f'Waiting for approval to Uniswap for new token : {tx_hash}')
                            #             sleep(1)
                            #     except web3.exceptions.TransactionNotFound:
                            #         logger.warning(f'Transaction not in mempool.Waiting for transaction to be seen: {tx_hash}')
                            #         sleep(1)
                            sleep(30)
                            if self.get_token_balance(token_in)>0:

                                logger.warning(f'token {token_in} will be swapped back to {token_out}')

                                tx_hash = self.swap_token(token_in, token_out,self.get_token_balance(token_in))

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
                    else:
                        logger.error(f'We don"t swap because liquidity is equal to :{liquidity}')


            sleep(poll_interval)


    def get_min_amount_to_buy(self,token_in,token_out, amount_to_buy):
        try:
            res = ICO_BOT.my_contract.functions.getAmountOutMin(token_in,token_out,amount_to_buy).call({'from': self.my_address_in_goeri})
            res = int(res * self.slippage_tolerance)
            logger.warning(f'It should return about {res} of token {token_out} for {amount_to_buy} of {token_in} token')
            return res  #ICO_BOT.weth_buy_threshold
        except web3.exceptions.ContractLogicError:
            logger.error(f'Not enough liquidity. Try another pair or another amount')
            return None

    def swap_token(self,token_in,token_out,amount_to_buy):
        min_amount_out = self.get_min_amount_to_buy(token_in, token_out, amount_to_buy)
        # Check if there is enough liquidity to perform the swap
        if min_amount_out is not None and min_amount_out != 0:
            nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
            tx = ICO_BOT.my_contract.functions._swap_token(token_in,token_out,amount_to_buy,min_amount_out).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas})
            signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
            tx_hash = ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return ICO_BOT.w3.toHex(tx_hash)
        else:
            logger.warning(f'We cannot swap these tokens due to the lack of liquidity')
            return None
    #
    def get_token_balance(self,token):
        balance =  ICO_BOT.my_contract.functions.get_balance_token(token).call({'from': self.my_address_in_goeri})
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




    def get_gas_price(self):
        return ICO_BOT.w3.eth.gas_price
###############################################################
    ######OPERATIONS WITH BALANCE #####

    def withdraw_token(self,amount,token='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'):
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.my_contract.functions.send_token_to_wallet(amount,token).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas})
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx,ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)


    def get_token_decimals(self,token):
        return ICO_BOT.my_contract.functions.get_token_decimals(token).call({'from': self.my_address_in_goeri})

    # def get_purchase_price(self,token):
    #     self.purchase_price = (ICO_BOT.weth_buy_threshold/10**18)/(self.get_token_balance(token)/10**self.get_token_decimals(token))
    #     logger.warning(f'purchase price is equal to {Decimal(self.purchase_price)}')

    def get_pair_price(self,token_in,token_out)->int:
        amount_tk_per_1eth  = self.get_min_amount_to_buy(token_in, token_out, 1000000000000000000)
        amount_tk_per_1eth = amount_tk_per_1eth/(10**self.get_token_decimals(token_out))
        # logger.warning(f'amount that we are getting selling 0.01 ETH :{amount_tk_per_1eth}')
        # logger.warning(f'Price will be {Decimal(1/amount_tk_per_1eth)}')
        logger.warning(f'Price will be {Decimal(1) / Decimal(amount_tk_per_1eth)}')
        return Decimal(1) / Decimal(amount_tk_per_1eth)

    #
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
            # try:
            self.log_loop(event_filter, 2)
            # except ValueError:
            #     print(f'filter is incorrect')



if __name__ == '__main__':
    ico_bot1 = ICO_BOT()
    # ico_bot1.main()
    # ico_bot1.get_token_balance('0xd4FDAc1B8c96ffB8A494254D1Bc5b94d7735684e')
    ico_bot1.swap_token(ICO_BOT.weth_goerli,'0x48a4F1664FB574a6728D60F681307cdc5C922355',ico_bot1.get_token_balance('0x48a4F1664FB574a6728D60F681307cdc5C922355'))
    # print(ico_bot1.liquidity_check('0xbeEC23cE00bae639fcDE575075bE37ca433e7fD0'))

