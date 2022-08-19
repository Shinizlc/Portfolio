from web3 import Web3
import json
from art import tprint
ganache_url='http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))
abi=json.loads('''[
	{
		"constant": true,
		"inputs": [],
		"name": "test",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]''')
tprint('First Contract')
contract_address = '0x6610Eb7cC750733b3d3b260E867F1604b6c3d70b'
contract = w3.eth.contract(address=contract_address,abi = abi)
print(contract.functions.test().call())
#print(contract.caller.add(1,2))


