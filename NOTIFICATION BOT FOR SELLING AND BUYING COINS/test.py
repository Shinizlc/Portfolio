# def test():
#     try:
#         #inner_func(323)
#         def inner_func(val):
#             try:
#                 return val/12
#             except:
#                 print(f'we cannot divide string by int')
#         return inner_func('some shit')
#     except:
#         print(f'outer exception there is no such function')
#
#
# # print(test())
# a=[1,43,232,32,43]
# d={}
# for i in a:
#     d[i] = d.get(i, 0)+1


#print([set(k,v) for k,v in d.items()])

# print({k:v for k,v in sorted(d.items(),key=lambda x:x[1],reverse=True)})
#
# every_other_index = slice(0,None,2)
# print(a[every_other_index])
# print([a[i] for i in range(0,len(a),2)])



# print(a[2:])


# from collections import Counter
# c = Counter(a)
# print(c.most_common())



#
# d1={'k1':12,'k2':1332}
# d2={'k3':2323,'k4':325885454}
# d3={**d1,**d2}
# print(d3)



# def test_func(x=2,y=5):
#     return x+y
#
# print(test_func(332,3232))

# a=[12,23,43]
# b=a
# print(a is b)
# b[0]=1
# print(a[0])
# print(b[0])
# print(id(a))
# print(id(b))

# c=121244343
# print(str(c).count('1'))



    # args = locals() #create dictionary from function args
    # l = [i for i in args.values()]
    # print(l)




from collections import defaultdict
#l = [2, 4, 0, 100, 4, 11, 2602, 36]
# l = [160, 3, 1719, 19, 11, 13, -21]
# d=defaultdict(list)
# def find_outlier(l):
#     for i in l:
#         if i%2==0 and len(d['odd'])<=1:
#             d['even'].append(i)
#         elif i%2==0 and len(d['odd'])>1:
#             return i
#         elif i%2!=0 and len(d['even'])<=1:
#             d['odd'].append(i)
#         elif i%2==0 and len(d['odd'])>=1 and len(d['even'])>=1:
#             return d['odd']
#         elif i % 2!= 0 and len(d['odd']) >= 1 and len(d['even']) >= 1:
#             return d['even']
#         else:
#             return i
# print(find_outlier(l))

#
# def get_sum(a,b):
#     k=0
#     for i in range(a,b+1):
#         print(i)
#         k += i
#     return k
#
#
# print(get_sum(0,-1))

# def find_outlier(integers):
#     k=0
#     flag = None
#     for i in integers:
#         if i%2==0 and flag in (None,'EVEN'):
#             k+=1
#             flag='EVEN'
#         elif i%2!=0 and flag in(None,'ODD'):
#             k+=1
#             flag='ODD'
#         elif i%2==0 and flag=="ODD" and k>1:
#             return i
#         elif i%2!=0 and flag=='EVEN' and k>1:
#             return i
# l = [2, 4, 0, 100, 4, 11, 2602, 36]


import re
# def validate_pin(pin):
#     if re.search(r'^[0-9]{4}[^ \n]+$',pin.strip('\n')) or re.search(r'^[0-9]{6}$',pin.strip('\n')):
#         return True
#     return False
#



# print(re.findall(r'[A-Z,a-z]+', 'breakCamelCase'))
# print(re.findall(r'\b\w+@\w+\.\w+\b', 'the client mail is asemerikov@gmail.com'))


# class Test_variables():
#     def __init__(self,var):
#         self.var = var
#     def f_func(self):
#         self.var = 1+2
#     def s_func(self):
#         return self.var+232
#
#     def __str__(self):
#         return f'some shit'
#
#
#     def __add__(self, other):
#         return self.var+other.var
#
#
# a=Test_variables(3)
# b=Test_variables(10)
# print(vars(Test_variables))
# print(dir(Test_variables))
from collections import defaultdict
d= defaultdict(list)
l = [2, 4, 0, 100, 4, 11, 2602, 36]
def check(l):
    for i in l:
        if i%2==0:
            if len(d['even']) == 1 and len(d['odd']==1):
                return d['odd']
            else:
                d['even'].append(i)
        else:
            if len(d['even']) == 1 and len(d['odd'] == 1):
                return d['even']
            else:
                d['odd'].append()

check(l)


