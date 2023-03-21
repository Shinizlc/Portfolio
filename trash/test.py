# a=[1,2,34,5]
# b=[1,2,3]
# c = [k for k in a for l in b if k==l]
# print(c)
# from collections import defaultdict
# a=[12,4443,2323,12]
# d=defaultdict(int)
# for l in a:
#     d[l]+=1
#
# print(dict(d))
#


# class Test1:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname=surname
#
#     def some_func(self):
#         print('some text')
#
# class Test2(Test1):
#     def __init__(self,name,surname,position):
#         super().__init__(name,surname)
#         self.position=position
#         super().some_func()
#
#
# t1=Test2('alex','semerikov','manager')
#
#
# print(t1.name)

import threading
from time import sleep
# def test_func(name):
#     print(f'first statement in {name}')
#     sleep(5)
#     print(f'second statement in {name}')
#
# #threads=[]
#
# def main_function():
#     print(f'start main function')
#     for i in range(5):
#         task = threading.Thread(target=test_func,args=(i,))
#         task.start()
#         #threads.append(task)
#     task.join()
#     print(f'end main function')
#
# if __name__ == '__main__':
#     main_function()

import threading
from time import sleep

# def first_thread():
#     for i in range(10):
#         print('progressing thread 1')
#         sleep(2)
#
#
# def second_thread():
#     for i in range(5):
#         print('progressing thread 2')
#         sleep(1)
# #
# #
# def main_function():
#     print(f'start main programm')
#     thread1 = threading.Thread(target=first_thread)
#     thread2 = threading.Thread(target=second_thread)
#     thread1.start()
#     thread2.start()
#     thread2.join()
#     print(f'end main programm')
# #
# #
# #
# if __name__ == '__main__':
#     main_function()
#
#
# # def test(a,b,c=4):
# #     print(a,b,c)
# #
# # test(1,2,c=None)



# from contextlib import contextmanager
#
# @contextmanager
# def funct_generator(name,surname,age):
#     class Parent:
#         def __init__(self,name,surname,age):
#             self.name = name
#             self.surname=surname
#             self.age = age
#         def print_fullname(self):
#             return self.name+' '+ self.surname
#     parent = Parent(name,surname,age)
#     yield parent
#     print('end of generator')
#
# with funct_generator('Alex','Semerikov',36) as gen:
#     print(gen.print_fullname())

# d={'a':3,'c':43,'d':1}
# print({k:v for k,v in sorted(d.items(),key=lambda x:x[1])})






# class Child(Parent):
#     def __init__(self,name,surname,age,sex):
#         self.sex=sex
#         super().__init__(name, surname, age)
#     def full_info(self):
#         return self.name, self.surname,self.age,self.sex
#
#
#
# child1 = Child('Aleksei','Semerikov',36,'f')
# print(child1.full_info())


# from decimal import Decimal,getcontext
# #
# getcontext().prec = 32
# # x= round(Decimal(1)/Decimal(33266599933266599933266599933266),30)
# # print(x)



# class Test:
#     v = 5
#     k = 10
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#     def ordinary(self):
#         print(self.x,self.y,self.v)
#
#     @staticmethod
#     def test_static(a,b):
#         print(a+b)
#
#     @classmethod
#     def test_classmethod(cls,first, last):
#         print(first,last,cls.v,cls.k)

#
# import requests
# from pprint import pprint
# # Etherscan API key
# API_KEY = 'NVIAZVXB6NTI36RCGFHXGXFYN6WY2FJ9FR'
#
# # URL for gas price
# GAS_PRICE_URL = f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={API_KEY}'
#
# # Function to get current gas price
# def get_gas_price():
#     with requests.get(GAS_PRICE_URL) as link:
#         data = int(link.json()['result']['FastGasPrice'])
#         return data
#
#
#
# get_gas_price()





# class Test:
#     singletone = None
#     def __new__(cls):
#         if cls.singletone is None:
#             cls.singletone = object.__new__(cls)
#             return cls.singletone
#
#     def __init__(self):
#         print(f'new object is created')
#
#     @classmethod
#     def __del__(cls):
#         cls.singletone = None
#
#
# test1 = Test()
# test2 = Test()


# import asyncio
# async def test_async(n):
#     print(f'begin of programm with {n}')
#     await asyncio.sleep(n)
#     print(f'end of programm with {n}')
#
#
# def main():
#
#     # l = [test_async(i) for i in range(10)]
#     # task = asyncio.gather(*l)
#     # await task
#     task = asyncio.create_task(test_async(5))
#     loop = asyncio.get_event_loop()
#     loop.
#     loop.run_until_complete(task)
    # loop = asyncio.get_running_loop()
    # loop.run_until_complete(task)

# asyncio.run(main())
#
# import asyncio
# async def test_coroutine(i):
#     print(f'this is coroutine{i}')
#
#
# async def main_coroutine():
#     list_of_coroutines = [test_coroutine(i) for i in range(10)]
#     for i in list_of_coroutines:print(type(i))
#     gathered = asyncio.gather(*list_of_coroutines)
#     task = asyncio.create_task(gathered)
#     await asyncio.sleep(10)
#     await task
#
# asyncio.run(main_coroutine())





# class Test:
#     def __init__(self):
#         self.__var1 = 5
#
#     @property
#     def var(self):
#         return self.__var1
#
#     @var.setter
#     def var(self,v):
#         self.__var1 = v
#
#
#
#
#
# test = Test()
# test.__dict__['var']= '43434343nkgfkb'
# test.var = 10
# print(test.var)
# print(test.__dict__)



# def generator():
#     a=[1,2,3,45]
#     for i in map(lambda x:x*2, a):
#         yield i
#         print(f'something {i}')
# x = generator()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# def domain_name(url):
#     try:
#         url = url.split('//')[1]
#         if url.split('.')[0] == 'www':
#             return url.split('.')[1]
#         else:
#             return url.split('.')[0]
#     except:
#         if url.split('.')[0] == 'www':
#             return url.split('.')[1]
#         else:
#             return url.split('.')[0]


#
# class Call:
#     def __init__(self,val):
#         self.val = val
#
#     def __call__(self, *args, **kwargs):
#         print('something')
#
# call1 = Call(5)
# call1()

def repeat(N):
    if N
        print('*'* N)
        repeat(N-1)

repeat(5)