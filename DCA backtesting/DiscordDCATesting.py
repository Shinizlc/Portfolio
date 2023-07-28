import requests as re
from time import sleep
from sklearn.model_selection import ParameterGrid
headers = {'authorization': 'OTQ0NTE1MjM0ODIxOTk2NTg0.YhFbHQ.3rjhllzsacckNlyAsQVwmAX-I1c'}

grid = ParameterGrid()



data={'content':'!dcabacktest -pair DOGE/USDT -tp 0.35 -bo 10 -so 10 -mstc 6 -sos 2.7 -os 1.9 -ss 0.7'}
#re.post('https://discord.com/api/v9/channels/862822214045925407/messages',data=data,headers=headers)


