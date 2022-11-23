import requests
from pprint import pprint
from main_bot_script import ICO_BOT
from web3 import Web3
class Fraud_Contract(ICO_BOT):

    ##все данные указываю для mainnet так как проще тестировать
    def __init__(self,token_a,token_b,pair):
        self.token_a = token_a
        self.token_b = token_b
        self.pair = pair
    def honeypot_check(self):
        from web3 import Web3
        url = "https://honeypotapi.p.rapidapi.com/api/v1/scan/"

        querystring = {"factory_address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
                       "token_b": self.token_b, "chain": "eth",
                       "exchange": "Uniswap v2", "token_a": self.token_a,
                       "router_address": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", "fee": "3000"}

        headers = {
            "X-RapidAPI-Key": "01c050f5ffmshd08a9f8299b780fp1022b1jsna01e808f5ffc",
            "X-RapidAPI-Host": "honeypotapi.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        pprint(response.json())


    def liquidity_check(self):
        weth_on_contract = super().my_contract.functions.check_contract_liquidity(self.pair).call()
        if Web3.fromWei(weth_on_contract,'ether')>=.5:
            return True





##we make all checks, if all checks passed return True else False
check_pair = Fraud_Contract('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0xd54f26a537C15738bf88645fD6B9806F8C9a0f9F')
# check_pair.honeypot_check()
print(check_pair.liquidity_check())



