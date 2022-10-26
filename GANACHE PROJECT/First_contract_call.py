from web3 import Web3
import json
from art import tprint
#ganache_url='http://127.0.0.1:7545'
#rinkeby_url = 'https://rinkeby.infura.io/v3/6cda95a972fe4e168a9057235825b257'
goerli_url  = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
w3 = Web3(Web3.HTTPProvider(goerli_url))
abi=json.loads('''[
	{
		"inputs": [],
		"name": "deposit_here",
		"outputs": [],
		"stateMutability": "payable",
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
tprint('First Contract')
contract_address = '0x1A493dca988E8B4E2a7f4c4Eb29e142566ff85cb'
contract = w3.eth.contract(address=contract_address,abi = abi)

contact_function = contract.functions.get_balance().call()#funciton can be called or make transaction to function
print(contact_function)
print(w3.eth.accounts)
#tx_hash = contact_function.transact({"from": '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86', "value": 10000000000000000})#91.2871
# print(tx_hash)

#print(contract.caller.add(1,2))


