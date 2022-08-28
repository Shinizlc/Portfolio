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
a=[1,43,232,32,43]
d={}
for i in a:
    d[i] = d.get(i, 0)+1
#print([set(k,v) for k,v in d.items()])

# print({k:v for k,v in sorted(d.items(),key=lambda x:x[1],reverse=True)})
#
# every_other_index = slice(0,None,2)
# print(a[every_other_index])
print([a[i] for i in range(0,len(a),2)])



# print(a[2:])


# from collections import Counter
# c = Counter(a)
# print(c.most_common())



#
# d1={'k1':12,'k2':1332}
# d2={'k3':2323,'k4':325885454}
# d3={**d1,**d2}
# print(d3)