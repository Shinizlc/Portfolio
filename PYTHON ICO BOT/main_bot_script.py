from numpy import False_
from web3 import Web3
import web3
import json
import asyncio
from time import sleep
class ICO_BOT:
    infura_url = 'https://mainnet.infura.io/v3/6cda95a972fe4e168a9057235825b257'
    goerli_url = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
    w3 = Web3(Web3.HTTPProvider(goerli_url))
    uniswap_router = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
    uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
    uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    weth_goerli = '0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'
    # eth_goerli = '0x8d27431c473E83611847D195d325972e80D1F4c1'
    contract = w3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)
    ##my wallet in goerli
    my_address_in_goeri = '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
    private_key = 'ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
    ######my contract address
    my_contract_address='0x4e89D33D630521ede732057548602007b7b828fa'
    weth_buy_threshold = 10000000000000000
    weth_allowance_threshold = 100000000000000000
    gas = 300000
    weth_abi  = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
    weth_contact = w3.eth.contract(address = weth_goerli,abi = weth_abi)
    my_contract_abi=json.loads('''[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_token_in",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_token_out",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amountIn",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_amountOutMin",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			}
		],
		"name": "_swap_token",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_amount_to_send",
				"type": "uint256"
			}
		],
		"name": "approve_WETH_to_Uniswap",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_amount_to_send",
				"type": "uint256"
			}
		],
		"name": "send_WETH_to_contract",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "send_weth_to_wallet",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [],
		"name": "withdraw_funds",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	},
	{
		"inputs": [],
		"name": "check_approval_for_contract",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "pair_contract",
				"type": "address"
			}
		],
		"name": "check_contract_liquidity",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "weth_on_contract",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "get_balance_WETH",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_tokenIn",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_tokenOut",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amountIn",
				"type": "uint256"
			}
		],
		"name": "getAmountOutMin",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]''')
    my_contract = w3.eth.contract(address=my_contract_address,abi = my_contract_abi)


    # def __init__(self):
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

    def add_approve_to_uniswap(self,amount,token):
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.my_contract.functions.approve_WETH_to_Uniswap(amount,token).build_transaction({'nonce': nonce, 'gas': ICO_BOT.gas})#ICO_BOT.weth_allowance_threshold
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    #####check if we have enough money on the contract(haven"t checked yet?)
    def check_allowance_for_uniswap(self):
        wei_allowed = ICO_BOT.my_contract.functions.check_approval_for_contract().call()
        print(f'uniswap allowed to use {ICO_BOT.w3.fromWei(wei_allowed,"ether")} from my contract')
        if wei_allowed<ICO_BOT.weth_buy_threshold:
            return False
        else:
            return True



    def set_proper_weth_amount(self):
        if self.get_weth_balance()<ICO_BOT.weth_buy_threshold:
            self.add_weth_to_contract()
##################################################
    ###############MAIN PART######################

    def handle_event(self,event):
        token0,token1,pair = json.loads(Web3.toJSON(event))['args']['token0'],json.loads(Web3.toJSON(event))['args']['token1'],json.loads(Web3.toJSON(event))['args']['pair']
        print(token0,token1,pair)
        if token0==ICO_BOT.weth_goerli or token0==ICO_BOT.eth_goerli:
            token_in = token0
            token_out = token1
        elif token1==ICO_BOT.weth_goerli or token1==ICO_BOT.eth_goerli:
            token_in = token1
            token_out = token0
        else:
            return None
        print(f'ETH or WETH is {token_in},other token is {token_out}')
        return token_in, token_out, pair


    async def log_loop(self,event_filter, poll_interval):
        while True:
            for PairCreated in event_filter.get_new_entries():
                try:
                    token_in, token_out,pair = self.handle_event(PairCreated)
                    print(token_in, token_out, pair)
                except:
                    print(f'return some shity stuff')
                else:
                #self.set_proper_weth_amount()
                    print(f'token {token_in} will be swapped to {token_out}')
                    if self.check_allowance_for_uniswap():
                        self.swap_token(token_in,token_out,ICO_BOT.weth_buy_threshold)
                    else:
                        self.add_approve_to_uniswap(ICO_BOT.weth_allowance_threshold,ICO_BOT.weth_goerli)
                        sleep(180)# check how calcalate the time of approval(success status of approval)
                        self.swap_token(token_in, token_out,ICO_BOT.weth_buy_threshold)

                    # if self.swap_token(token_in,token_out) is not None:
                    #     sleep(120)
                    #     token_in,token_out=token_out,token_in
                    #     print(f'token {token_in} will be swapped back to {token_out}')
                    #     self.swap_token(token_in, token_out)#do we need to give an approval to uniswap for the new token(token_in here) not weth



            await asyncio.sleep(poll_interval)


    # def get_min_amount_to_buy(self,token_in,token_out):
    #     try:
    #         return ICO_BOT.my_contract.functions.getAmountOutMin(token_in,token_out,ICO_BOT.weth_buy_threshold).call()
    #     except web3.exceptions.ContractLogicError:
    #         print(f'Not enough liquidity. Try another pair or another amount')
    #         return None


    def get_min_amount_to_buy(self,token_in,token_out, amount_to_buy):
        try:
            res = ICO_BOT.my_contract.functions.getAmountOutMin(token_in,token_out,amount_to_buy).call()
            print(f'It should return about {res} of token {token_out} for {amount_to_buy} of {token_in} token')
            return res  #ICO_BOT.weth_buy_threshold
        except web3.exceptions.ContractLogicError:
            print(f'Not enough liquidity. Try another pair or another amount')
            return None

    def swap_token(self,token_in,token_out,amount_to_buy):
        if self.get_min_amount_to_buy(token_in,token_out,amount_to_buy) is not None and self.get_min_amount_to_buy(token_in,token_out,amount_to_buy)!=0:
            nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
            tx = ICO_BOT.my_contract.functions._swap_token(token_in,token_out,ICO_BOT.weth_buy_threshold,self.get_min_amount_to_buy(token_in,token_out,amount_to_buy),ICO_BOT.my_contract_address).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas})
            signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
            ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        else:
            print(f'we cannot swap these tokens due to the lack of liquidity')
            return None

    def get_gas_price(self):
        return ICO_BOT.w3.eth.gas_price
###############################################################
    ######OPERATIONS WITH BALANCE #####

    def withdraw_weth(self,amount):
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.my_contract.functions.send_weth_to_wallet(amount).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas})
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx,ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)


    def get_token_balance(self,token):
        return ICO_BOT.my_contract.functions.get_balance_token(token).call()



    def set_take_profit(self):
        pass

    def set_stop_loss(self):
        pass


    def main(self):
        event_filter = ICO_BOT.contract.events.PairCreated.createFilter(fromBlock='latest')
        asyncio.run(self.log_loop(event_filter, 2))


#85357340
if __name__ == '__main__':
    ico_bot1 = ICO_BOT()
    # print(ico_bot1.get_min_amount_to_buy('0xF80f64DDee6f994E2FbE71974E44b50F76e575Ce','0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'))
    # ico_bot1.approve_contract_to_use_my_weth()
    # sleep(180)
    # ico_bot1.add_weth_to_contract()
    # print(ico_bot1.get_gas_price())
    # print(ico_bot1.get_min_amount_to_buy('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0x37F3721eB87850F00ECe180c239c55d71d61dFEC'))
    # ico_bot1.swap_token('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0x12E80d2Cf0B64D5FaE3942b3E08322494566d4ad')
    ico_bot1.main()
    # ico_bot1.swap_token('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6', '0xCBB9E0434A8c40eEDA57a1CE232d39272a5EC05C')
    #print(ico_bot1.get_min_amount_to_buy('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0x609d184a2d866c9af700E29AB23214dAd2b90146'))
    # ico_bot1.swap_token('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0x609d184a2d866c9af700E29AB23214dAd2b90146')
    #ico_bot1.withdraw_weth(110000000000000000)
    #ico_bot1.approve_contract_to_use_my_weth()
    #sleep(20)
    # ico_bot1.get_min_amount_to_buy('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0x37027FC3FA4b2fC7d34996D28a7845394448c248')
    # ico_bot1.add_weth_to_contract()#add check for allowance of contract
    # ico_bot1.main()
