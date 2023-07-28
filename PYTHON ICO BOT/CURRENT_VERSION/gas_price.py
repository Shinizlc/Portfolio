import requests as re
# from web3 import Web3
def get_gas_price():
    with requests.get('https://ethgasstation.info/json/ethgasAPI.json') as link:
        data = link.json()
        infura_url = 'https://mainnet.infura.io/v3/6cda95a972fe4e168a9057235825b257'
        # w3  = Web3(Web3.HTTPProvider(infura_url))
        # gas_price = w3.eth.gasPrice
        # gas_price = gas_price/10**8
        return data['fastest']/10


print(get_gas_price())




