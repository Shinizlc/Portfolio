# from web3 import Web3

#
# ganache_url='http://127.0.0.1:7545'
# address1='0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
# address2='0x02b16a6332eE7343F443d9e9a279682D467d87fD'
# private_key = 'ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
# #nonce = Web3.eth.get_balance('0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86')
#
#
# w3 = Web3(Web3.HTTPProvider(ganache_url))
# print(w3.isConnected())
# nonce = w3.eth.get_transaction_count('0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86')
#
# tx = {
#     'nonce': nonce,
#     'to': address2,
#     'value': w3.toWei(1, 'ether'),
#     'gas': 2100000,
#     'gasPrice': w3.toWei('50', 'gwei')
# }
#
#
#
# singed_tx= w3.eth.account.sign_transaction(tx,private_key)
# send_tx=w3.eth.send_raw_transaction(singed_tx.rawTransaction)
# print(w3.toHex(send_tx))

# from threading import Thread
# from multiprocessing import Process
#
# from time import sleep
# def func_print(i):
#     print(i)
#     sleep(5)
#     print(i)
#
# if __name__ == '__main__':
#     print(f'begining of main program')
#     for i in range(5):
#         process=Thread(target=func_print,args=(i,))
#         process.start()
#     process.join()
#
#     print(f'end of main program')



# import asyncio
# async def another_func():
#     print(f'begining of another program')
#     await asyncio.sleep(5)
#     print(f'end of another func')
# async def main():
#     task = asyncio.create_task(another_func())
#     print(f'begining of main program')
#     await asyncio.sleep(2)
#     #await another_func()
#     print(f'end of main program')
#     await task
#
# asyncio.run(main())


from web3 import Web3
import json
import asyncio


infura_url = 'https://mainnet.infura.io/v3/6cda95a972fe4e168a9057235825b257'
goerli_url = 'https://goerli.infura.io/v3/6cda95a972fe4e168a9057235825b257'
web3 = Web3(Web3.HTTPProvider(goerli_url))
uniswap_router = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
weth_goerli = '0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6'
eth_goerli = '0x8d27431c473E83611847D195d325972e80D1F4c1'
contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)

def handle_event(event):
    token0,token1,pair = json.loads(Web3.toJSON(event))['args']['token0'],json.loads(Web3.toJSON(event))['args']['token1'],json.loads(Web3.toJSON(event))['args']['pair']
    print(pair)
    if token0==weth_goerli or token0==eth_goerli:
        token_in = token0
        token_out = token1
        print(f'ETH or WETH is {token_in},other token is {token_out}')
    elif token1==weth_goerli or token1==eth_goerli:
        token_in = token1
        token_out = token0
        print(f'ETH or WETH is {token_in},other token is {token_out}')
    else:
        print(f'Both != to eth or weth')



async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)




def main():
    event_filter = contract.events.PairCreated.createFilter(fromBlock='latest')
    asyncio.run(log_loop(event_filter, 2))

if __name__ == "__main__":
    main()







