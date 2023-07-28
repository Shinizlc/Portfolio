import asyncio
async def main_func():
    # for token in ['token1','token2','token3','token4','token5','token6']:
        # await swap_token(token)
    token1 = asyncio.create_task(swap_token('token1'))
    token2 = asyncio.create_task(swap_token('token2'))
    token3 = asyncio.create_task(swap_token('token3'))
    # await token1
    # await token2
    # await token3
    print('end of main program')

async def swap_token(token_a):
    print(f'before swap of {token_a}')
    await asyncio.sleep(5)
    print(f'after swap of {token_a}')


asyncio.run(main_func())