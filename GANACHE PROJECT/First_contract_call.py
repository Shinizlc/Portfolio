from web3 import Web3
import json
from art import tprint
ganache_url='http://127.0.0.1:7545'
# rinkeby_url = 'https://rinkeby.infura.io/v3/6cda95a972fe4e168a9057235825b257'
w3 = Web3(Web3.HTTPProvider(ganache_url))
abi=json.loads('''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "depost_funds",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "test_deposit",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "address_and_value",
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
		"name": "all_donators",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]''')
tprint('First Contract')
contract_address = '0xc20733b5781713649cb303A4c4D823bAd4e31107'
contract = w3.eth.contract(address=contract_address,abi = abi)
contact_function = contract.functions.test_deposit()#funciton can be called or make transaction to function

# print(w3.eth.accounts)
# tx_hash = contact_function.transact({"from": w3.eth.accounts[0], "value": 100000000000000000})#91.2871
# print(tx_hash)

#print(contract.caller.add(1,2))


