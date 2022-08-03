# import pyforest
from collections import Counter
# t='some string\nsome string2'
# for line in tqdm.tqdm(t.splitlines()):
#     my_counter=Counter(line.split(' '))
# print(my_counter)

########
# s={'a':5454,'b':12,'c':1}
# print({k:v for k,v in  sorted(s.items(),key=lambda x:x[0])})
#########
from pprint import pprint
# d={}
text='''first line
second line
third line'''
# for line in text.splitlines():
#     for word in line.split(' '):
#         d[word] = d.get(word,0)+1
# pprint(d)

# d=Counter()
# for line in text.splitlines():
#     for word in line.split(' '):
#         d[word]=d[word]+1
# pprint(d)

# a=[4343,322,12215,3232]
# b=[1,2,3,4]
# c=list(zip(a,b))
# result=filter(lambda x:x[0]+x[1]<=400,c)
# print(list(result))


from random import randint
val=randint(1,10)
print(val)

while True:
    your_val = input('Enter your value\n')
    if val==int(your_val):
        print('you guessed')
        break
    elif val>int(your_val):
        print('your value is smaller then the value')
    else:
        print('you value is bigger')
