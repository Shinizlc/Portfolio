from web3 import Web3
import json
contract_address = '0x8f802C71930E8A9CDE39B91d13DF23527ccD484a'
abi = json.loads('''[
	{
		"inputs": [],
		"name": "deposit",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_greeting",
				"type": "string"
			}
		],
		"name": "setGreeting",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "greet",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]''')

ganache_url = 'http://127.0.0.1:7545'
goerli_url  = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
private_key='ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
from_address='0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
w3 =  Web3(Web3.HTTPProvider(goerli_url))
contract = w3.eth.contract(address=contract_address,abi = abi)
nonce = w3.eth.get_transaction_count(from_address)
raw_tx = {'nonce': nonce,
  #  'to': '0x8f802C71930E8A9CDE39B91d13DF23527ccD484a',
    'value': w3.toWei(0.01, 'ether'),
    'gas': 2100000,
    'gasPrice': w3.toWei('50', 'gwei')

}


# print(w3.eth.accounts)#работает в ганеше

# key = contract.functions.deposit().buildTransaction(raw_tx)
# tx_hash = w3.eth.account.signTransaction(key,private_key)
# w3.eth.sendRawTransaction(tx_hash.rawTransaction)


key = contract.functions.setGreeting('TEETETTE').buildTransaction({'nonce': nonce})
tx_singed = w3.eth.account.signTransaction(key,private_key)
w3.eth.sendRawTransaction(tx_singed.rawTransaction)
print(contract.functions.greet().call())











###Работает в ганеш, но не работает в tester
##сетях,выдает 'code': -32601, 'message': 'The method eth_sendTransaction does not exist/is not available'}

# print(contract.functions.setGreeting("TESTTTTT").transact({'from':'0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'}))
# print(contract.functions.greet().call())



