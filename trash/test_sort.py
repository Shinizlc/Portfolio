from collections import Counter

d='''test1 test2 test3
test4 test5 test6'''

d={'a':14,'b':2}
print(sorted(d.items(),key=lambda x:x[1], reverse=True))