from web3 import Web3
import web3
import json
import asyncio

class ICO_BOT:
    infura_url = 'https://mainnet.infura.io/v3/6cda95a972fe4e168a9057235825b257'
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
    my_contract_address='0xacC57823188129BB8504aC25fb5Fdd7185FC59C4'
    my_contract_abi=json.loads('''[
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
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
		"name": "approve_for_uniswap",
		"outputs": [],
		"stateMutability": "payable",
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
	},
	{
		"inputs": [],
		"name": "get_balance",
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
		"stateMutability": "payable",
		"type": "receive"
	}
]''')
    my_contract = w3.eth.contract(address=my_contract_address,abi = my_contract_abi)


    #def __init__(self):
        #self.main()

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
            pass
        print(f'ETH or WETH is {token_in},other token is {token_out}')
        return token_in, token_out


    async def log_loop(self,event_filter, poll_interval):
        while True:
            for PairCreated in event_filter.get_new_entries():
                token_in, token_out = self.handle_event(PairCreated)
                #self.get_min_amount_to_buy(token_in,token_out)
            await asyncio.sleep(poll_interval)

    def get_min_amount_to_buy(self,token_in,token_out,amount_in):
        try:
        # nonce=ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        # tx = {'nonce':nonce,'from':ICO_BOT.my_address_in_goeri}
        # tx_raw= ICO_BOT.my_contract.functions.getAmountOutMin(token_in,token_out,amount_in).buildTransaction(tx)
        # tx_singed = ICO_BOT.w3.eth.account.signTransaction(tx_raw,ICO_BOT.private_key)
        # ICO_BOT.w3.eth.sendRawTransaction(tx_singed)
            print(ICO_BOT.my_contract.functions.getAmountOutMin(token_in,token_out,amount_in).call())
        except web3.exceptions.ContractLogicError:
            print(f'Not enough liquidity. Try another pair or another amount')


    def set_take_profit(self):
        pass

    def set_stop_loss(self):
        pass


    def main(self):
        event_filter = ICO_BOT.contract.events.PairCreated.createFilter(fromBlock='latest')
        asyncio.run(self.log_loop(event_filter, 2))


#85357340
ico_bot1 = ICO_BOT()
# ico_bot1.get_min_amount_to_buy('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0xCBB9E0434A8c40eEDA57a1CE232d39272a5EC05C',1000000000000000)
ico_bot1.get_min_amount_to_buy('0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0x5C47740624Eac41cbf60Ff91b64A0500De4291E0',100000000000000000)