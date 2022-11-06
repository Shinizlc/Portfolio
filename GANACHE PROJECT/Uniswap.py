from web3 import Web3
from art import tprint
import json
abi = json.loads('''[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_amount_to_send",
				"type": "uint256"
			}
		],
		"name": "swap_token",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "test_local_var",
		"outputs": [],
		"stateMutability": "nonpayable",
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
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "some_arr",
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
contract_address = ''
signature = 'ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
from_address = '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
goerli_url = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
w3 = Web3(Web3.HTTPProvider(goerli_url))
contract = w3.eth.contract(address = contract_address,abi = abi)
nonce = w3.eth.get_transaction_count(from_address)
tprint('Uniswap project')
print(contract.functions.get_balance().call())
key = contract.functions.swap_token(10000000000000000).buildTransaction({'from':from_address,'nonce':nonce})
tx_code = w3.eth.signTransaction(key,signature)
w3.eth.sendRawTransaction(tx_code.rawTransaction)