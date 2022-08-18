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
web3 = Web3(Web3.HTTPProvider(infura_url))
uniswap_router = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
uniswap_factory = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)

def handle_event(event):
    print(Web3.toJSON(event))


# asynchronous defined function to loop
# this loop sets up an event filter and is looking for new entires for the "PairCreated" event
# this loop runs on a poll interval
async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)


# when main is called
# create a filter for the latest block and look for the "PairCreated" event for the uniswap factory contract
# run an async loop
# try to run the log_loop function above every 2 seconds
def main():
    event_filter = contract.events.PairCreated.createFilter(fromBlock='latest')
    asyncio.run(log_loop(event_filter, 2))

    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(
    #         asyncio.gather(
    #             log_loop(event_filter, 2)))
    #             # log_loop(block_filter, 2),
    #             # log_loop(tx_filter, 2)))
    # finally:
    #     # close loop to free up system resources
    #     loop.close()


if __name__ == "__main__":
    main()







