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

def first_thread():
    for i in range(10):
        print('progressing thread 1')
        sleep(2)


def second_thread():
    for i in range(5):
        print('progressing thread 2')
        sleep(1)
#
#
def main_function():
    print(f'start main programm')
    thread1 = threading.Thread(target=first_thread)
    thread2 = threading.Thread(target=second_thread)
    thread1.start()
    thread2.start()
    thread2.join()
    print(f'end main programm')
#
#
#
if __name__ == '__main__':
    main_function()


# def test(a,b,c=4):
#     print(a,b,c)
#
# test(1,2,c=None)