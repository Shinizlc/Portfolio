from web3 import Web3
import json
abi = json.loads('''[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "send_and_approve_WETH",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]''')
key = 'ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
my_wallet = '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
my_address = '0xc2D404b004BA9F92dab8b1D149eeB0c992085f1D'
weth_address = '0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'
abi_weth = json.loads('''[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]''')
goerli_url = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
w3 = Web3(Web3.HTTPProvider(goerli_url))
my_contract  = w3.eth.contract(address = my_address,abi = abi)
weth_contact = w3.eth.contract(address = weth_address,abi = abi_weth)
nonce = w3.eth.get_transaction_count(my_wallet)
# print(nonce)
# tx=weth_contact.functions.approve(my_address,1000000000000000000).build_transaction({'nonce':nonce})
# signed_tx = w3.eth.account.signTransaction(tx,key)
# w3.eth.sendRawTransaction(signed_tx.rawTransaction)


#######
# print(type(nonce))
print(my_contract.abi)
tx2 = my_contract.functions.send_and_approve_WETH().build_transaction({'nonce':nonce,'value':10000000000000000,'gas':3000000})
signed_tx = w3.eth.account.signTransaction(tx2,key)
w3.eth.sendRawTransaction(signed_tx.rawTransaction)



