####
# a=[32,4,3,45,7,6]
# d={a[elem]:a[elem+1] for elem in range(0,len(a)-1,2)}
# print(d)
#
# d2={k:v for k,v in sorted(d.items(),key=lambda x:x[1])}
# print(d2)
#
#
from pprint import pprint
from collections import deque,Counter
import json
import smtplib, ssl
# a=['apple','orange','orange','orange','grape']
# d=Counter()
# for word in a:
#     d[word]+=1
# for k,v in d.items():
#     if v>1:
#         pprint(k)


#d={'AlexeyS':'X','AlexeyE':'X','EvgenyV':'P','DmitryE':'S','DmitryS':'X','SergeyL':'D'}
# def scheduler_rotation(d:dict)->dict:
#     # for i in zip(d.keys(),d.values()):
#     #     print(i)
#     deq_dict = deque(d.values())
#     deq_dict.rotate()
#     return dict(zip(d.keys(), deq_dict))
#
# if __name__ == '__main__':
#     with open('current_scheduler.json','r') as file_r:
#         d = json.load(file_r)
#     upg_sched = scheduler_rotation(d)
#     data_to_send=json.dumps(upg_sched,indent=4)
#     with open('current_scheduler.json','w') as file_w:
#         json.dump(upg_sched,file_w,indent=4)
#
#
# port = 8025
# smtp_server = "127.0.0.1"
# sender_email = "my@gmail.com"
# receiver_email = "test@testmail.com"
# #password = input("Type your password and press enter: ")
# #context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#    # server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, data_to_send)


# def split_list(l:list)->list:
#     if len(l)%2 == 0:
#         n = len(l)//2
#     else:
#         n= len(l)//2+1
#     return [l[i:i+n] for i in range(0,len(l),n)]
#
#
# print(split_list([]))

# import re
# print(90/(6*60)) # 1 min= 0.25 degre
#
# def str_to_min(t:str):
#     l=re.findall(r'([0-9]+):([0-9]+)',t)
#
#     return int(l[0][0])*60+int(l[0][1])
#
# def min_to_deg(min:int)->float:
#     return min-6*60*0.25
#
# if __name__ == '__main__':
#     print(str_to_min('6:00'))
#     print(min_to_deg(360))


# d={'f':3232,'d':123,'c':567}
#
# print({k:v for k,v in sorted(d.items(),key=lambda x:x[1])})
# d={'a':345,'b':32323232}
# print(d.items())
# print({k:v for k,v in sorted(d.items(),key=lambda x:x[1])})

import argparse
import os

# parser=argparse.ArgumentParser()
# parser.add_argument('input',type=str,help='Enter your indir')
# parser.add_argument('output',type=str,help='Enter output dir')
# args = parser.parse_args()
# print(os.readlink('get_locations.py'))



# import test_import.get_locations
# a='''ewbfkewbfhe4554
# nrenkfre
# nrjenre'''
# k=0
# for line in a.splitlines():
#     for chars in line:
#         if chars.isdigit():
#             k+=int(chars)
#         else:
#             continue
# print(k)


from collections import defaultdict
d = defaultdict(list)
for k in range(1,10):
    d[k].append('test')
print(d)

