# def decor(func):
#     def wrapper(ar):
#         d=func(ar)
#         return d+2
#     return wrapper
#
# @decor
# def some_function(a):
#     return(a)
#
# print(some_function(5))


# w = [i for i in range(1,20)]
#
# def gen():
#     for i in range(1,20):
#         yield i
# d=gen()
# print(next(d))
# print(next(d))
# print(next(d))


# g=(i for i in range(1,20))
# print(next(g))
# print(next(g))



# def read_file():
#     with open('text_file.txt','r',encoding='koi8-r') as file:
#         for line in file.readlines():
#             yield line


# import json
# json_str='[{"a":5},{"b":6}]'
# Js = json.loads(json_str)
# js_str = json.dumps(Js)
# print(type(js_str))
# from datetime import datetime
# print(datetime.fromtimestamp(int('1620950399999')/1000))

import pandas as pd
# from datetime import datetime,timedelta
#
# print(datetime.now()-timedelta(2))
#
# a=[1,2,3,4]
# def test_yield(a):
#     for i in a:
#         yield i*2
#
# d = test_yield(a)
# print(next(d))
# print(next(d))
# print(24021055262063930508653/10**24)



from contextlib import contextmanager,asynccontextmanager

# import asyncio
# from time import sleep
# @asynccontextmanager
# async def test_contextmanager():
#     print(f'beginning contextmanager')
#     yield f'yield part'
#     await asyncio.sleep(5)
#     print(f'end of context manager')
#
# async def test():
#     async with test_contextmanager() as cm:
#         print(cm)
#         print(cm)
#
# asyncio.run(test())



# from contextlib import contextmanager
# from time import perf_counter,sleep
# @contextmanager
# def Timer():
#     start =perf_counter()
#     yield None
#     print(perf_counter()- start)
#
#
# with Timer() as timer:
#     sleep(2)
#     print(timer)

balance = 1000
smallest_unit_balance = balance * (10 ** (18 - 18))
print(smallest_unit_balance)