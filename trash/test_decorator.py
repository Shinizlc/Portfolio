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




