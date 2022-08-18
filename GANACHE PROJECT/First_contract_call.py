from web3 import Web3
import json
from art import tprint
ganache_url='http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))
abi=json.loads('''[
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_firstNo",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_secondNo",
          "type": "uint256"
        }
      ],
      "name": "add",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_val",
          "type": "uint256"
        }
      ],
      "name": "multiply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    }
  ]''')
tprint('First Contract')
contract_address = '0x4633348C73f70FbCf721773B9cDe886cdDDB759c'
contract = w3.eth.contract(address=contract_address,abi = abi)
#print(contract.functions.add(1,2).call())
print(contract.caller.add(1,2))