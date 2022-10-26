from art import tprint
# class TEST_SOME_FUNC:
#     def __init__(self,name,lastname):
#         self.name = name
#         self.lastname = lastname
#
#
#     def __str__(self):
#         return self.name+' '+ self.lastname
#     def __eq__(self,other):
#         if self.name==other.name and self.lastname==other.lastname:return True
#         return False



    # @staticmethod
    # def static_func(a:int,b:int):
    #     print(a+b)
#
# l=[TEST_SOME_FUNC(n,l) for l in ['alex','sergei'] for n in ['semerikov','vadimov']]


# name=['alex','sergei']
# lastname=['semerikov','vadimov']
# l = [TEST_SOME_FUNC(full_name[0],full_name[1]) for full_name in zip(name,lastname)]
# print(l[0]==l[1])

# class test_sum:
#     def __init__(self,first_value,second_value):
#         self.first_value = first_value
#         self.second_value = second_value
#     def __add__(self,other):
#         return self.first_value+other.first_value
#
#
# t1 = test_sum(1,2)
# t2 = test_sum(2,3)
# print(t1+t2)


l=[1,2,34,4]
# i = iter(l)
# print(next( ))
# print(next(i))



def gen(k):
    for n,i in enumerate(l):
        yield k[n]


g = gen(l)
print(next(g))
print(next(g))

